Summary:           E-Mail filtering framework using Sendmail's Milter interface
Name:              mimedefang
Version:           2.84
Release:           9%{?dist}
License:           GPLv2+
URL:               https://mimedefang.org/
Source0:           https://mimedefang.org/static/%{name}-%{version}.tar.gz
Source1:           https://mimedefang.org/static/%{name}-%{version}.tar.gz.sig
Source2:           gpgkey-FC2E9B645468698FD7B21655C1842E2A126F42E0.gpg
Source3:           README.FEDORA
Source4:           mimedefang.service
Source5:           mimedefang-multiplexor.service
Source6:           mimedefang-wrapper
Source7:           mimedefang.tmpfilesd
Requires:          perl-MailTools >= 1.15, perl(Mail::SpamAssassin) >= 1.6
Requires:          perl(IO::Stringy) >= 1.212, perl(MIME::Base64) >= 3.03
Requires(pre):     shadow-utils
Requires(post):    perl(Digest::SHA1)
%if 0%{?rhel} > 6 || 0%{?fedora} > 23
Requires(post):    systemd
Requires(preun):   systemd
Requires(postun):  systemd
BuildRequires:     systemd
%else
Requires(post):    /sbin/chkconfig
Requires(preun):   /sbin/service, /sbin/chkconfig
Requires(postun):  /sbin/service
%endif
%if 0%{?rhel} > 7 || 0%{?fedora} > 25
BuildRequires:     sendmail-milter-devel >= 8.12.0
%else
BuildRequires:     sendmail-devel >= 8.12.0
%endif
BuildRequires:     gcc, %{_sbindir}/sendmail, perl-devel, perl-generators
BuildRequires:     perl(ExtUtils::MakeMaker), perl(ExtUtils::Embed)
BuildRequires:     gnupg2

%description
MIMEDefang is an e-mail filter program which works with Sendmail 8.12
and later. It filters all e-mail messages sent via SMTP. MIMEDefang
splits multi-part MIME messages into their components and potentially
deletes or modifies the various parts. It then reassembles the parts
back into an e-mail message and sends it on its way.

There are some caveats you should be aware of before using MIMEDefang.
MIMEDefang potentially alters e-mail messages. This breaks a "gentleman's
agreement" that mail transfer agents do not modify message bodies. This
could cause problems, for example, with encrypted or signed messages.

%prep
gpgv2 --keyring %{SOURCE2} %{SOURCE1} %{SOURCE0}
%setup -q
cp -pf %{SOURCE3} .

%build
%configure --with-milterlib=%{_libdir} --with-user=defang --disable-check-perl-modules --disable-anti-virus
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT INSTALL='install -p' INSTALL_STRIP_FLAG='' install-redhat

# Fix config file, create log directory and remove duplicate
sed -e '1d' -i $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/%{name}
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/log/%{name}
rm -f $RPM_BUILD_ROOT%{_sysconfdir}/mail/sa-mimedefang.cf.example

# Install systemd/tmpfiles or initscript files
%if 0%{?rhel} > 6 || 0%{?fedora} > 23
install -D -p -m 644 %{SOURCE4} $RPM_BUILD_ROOT%{_unitdir}/%{name}.service
install -D -p -m 644 %{SOURCE5} $RPM_BUILD_ROOT%{_unitdir}/%{name}-multiplexor.service
install -D -p -m 755 %{SOURCE6} $RPM_BUILD_ROOT%{_libexecdir}/%{name}-wrapper
install -D -p -m 644 %{SOURCE7} $RPM_BUILD_ROOT%{_tmpfilesdir}/%{name}.conf
rm -f $RPM_BUILD_ROOT%{_sysconfdir}/rc.d/init.d/%{name}
%else
sed -e 's/2345/-/' -i $RPM_BUILD_ROOT%{_sysconfdir}/rc.d/init.d/%{name}
# Avoid smfi_setsymlist usage due to memory leaks in Sendmail < 8.14.4
%if 0%{?rhel} > 5 || 0%{?fedora} > 10
sed -e 's/\(-m $MX_SOCKET\)/\1 -y/' -i $RPM_BUILD_ROOT%{_sysconfdir}/rc.d/init.d/%{name}
%endif
%endif

# Create a dummy file and install perl script for later executing
touch $RPM_BUILD_ROOT%{_sysconfdir}/mail/mimedefang-ip-key
sed -e '1s@^@#!%{_bindir}/perl\n@' gen-ip-validator.pl > gen-ip-validator.pl.new
install -m 755 gen-ip-validator.pl.new $RPM_BUILD_ROOT%{_bindir}/gen-ip-validator.pl
touch -c -r gen-ip-validator.pl $RPM_BUILD_ROOT%{_bindir}/gen-ip-validator.pl

# Convert everything to UTF-8
iconv -f iso-8859-1 -t utf-8 -o Changelog.utf8 Changelog
touch -c -r Changelog Changelog.utf8
mv -f Changelog.utf8 Changelog

%pre
getent group defang > /dev/null || %{_sbindir}/groupadd -r defang
getent passwd defang > /dev/null || %{_sbindir}/useradd -r -g defang -d %{_localstatedir}/spool/MIMEDefang -s /sbin/nologin -c "MIMEDefang User" defang
exit 0

%post
%if 0%{?rhel} > 6 || 0%{?fedora} > 23
%systemd_post %{name}.service
%else
/sbin/chkconfig --add %{name}
%endif
if [ ! -f %{_sysconfdir}/mail/mimedefang-ip-key ]; then
  %{_bindir}/gen-ip-validator.pl > %{_sysconfdir}/mail/mimedefang-ip-key
fi

%preun
%if 0%{?rhel} > 6 || 0%{?fedora} > 23
%systemd_preun %{name}.service
%else
if [ $1 -eq 0 ]; then
  /sbin/service %{name} stop > /dev/null 2>&1 || :
  /sbin/chkconfig --del %{name}
fi
%endif

%postun
%if 0%{?rhel} > 6 || 0%{?fedora} > 23
%systemd_postun_with_restart %{name}.service
%else
if [ $1 -ne 0 ]; then
  /sbin/service %{name} condrestart > /dev/null 2>&1 || :
fi
%endif

%files
%{!?_licensedir:%global license %%doc}
%license COPYING
%doc README README.{NONROOT,SECURITY,SOPHIE,SPAMASSASSIN,VEXIRA,FEDORA}
%doc Changelog contrib/{word-to-html,linuxorg,fang.pl} examples/*filter*
%dir %attr(0750,defang,defang) %{_localstatedir}/log/%{name}
%dir %attr(0750,defang,defang) %{_localstatedir}/spool/MIMEDefang
%dir %attr(0750,defang,defang) %{_localstatedir}/spool/MD-Quarantine
%{_bindir}/*
%{_mandir}/man?/*
%if 0%{?rhel} > 6 || 0%{?fedora} > 23
%{_unitdir}/%{name}.service
%{_unitdir}/%{name}-multiplexor.service
%{_libexecdir}/%{name}-wrapper
%{_tmpfilesdir}/%{name}.conf
%else
%{_sysconfdir}/rc.d/init.d/%{name}
%endif
%config(noreplace) %{_sysconfdir}/mail/mimedefang-filter
%config(noreplace) %{_sysconfdir}/mail/sa-mimedefang.cf
%ghost %config(noreplace) %{_sysconfdir}/mail/mimedefang-ip-key
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.84-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.84-8
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.84-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.84-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.84-5
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.84-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.84-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.84-2
- Perl 5.28 rebuild

* Thu Mar 22 2018 Robert Scheck <robert@fedoraproject.org> 2.84-1
- Upgrade to 2.84 (#1559208)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.83-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 2.83-2
- Rebuilt for switch to libxcrypt

* Wed Nov 01 2017 Robert Scheck <robert@fedoraproject.org> 2.83-1
- Upgrade to 2.83 (#1508217)

* Mon Oct 09 2017 Robert Scheck <robert@fedoraproject.org> 2.82-1
- Upgrade to 2.82 (#1489992)

* Sun Sep 03 2017 Robert Scheck <robert@fedoraproject.org> 2.81-1
- Upgrade to 2.81 (#1487543, #1487804)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.80-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Sun Jul 30 2017 Florian Weimer <fweimer@redhat.com> - 2.80-2
- Rebuild with binutils fix for ppc64le (#1475636)

* Thu Jul 27 2017 Robert Scheck <robert@fedoraproject.org> 2.80-1
- Upgrade to 2.80 (#1474551)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.79-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.79-3
- Perl 5.26 rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.79-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Nov 29 2016 Robert Scheck <robert@fedoraproject.org> 2.79-1
- Upgrade to 2.79 (#1380052)

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.78-8
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.78-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 09 2016 Robert Scheck <robert@fedoraproject.org> 2.78-6
- Avoid chown-ing and chmod-ing /dev/null (#1296288 #c6)

* Sun Jan 03 2016 Robert Scheck <robert@fedoraproject.org> 2.78-5
- Provide native systemd service (#789768, #1279452)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.78-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.78-3
- Perl 5.22 rebuild

* Tue May 05 2015 Robert Scheck <robert@fedoraproject.org> 2.78-2
- Fix wrong interpreter of mimedefang-util script (#1218754)

* Thu Apr 23 2015 Robert Scheck <robert@fedoraproject.org> 2.78-1
- Upgrade to 2.78 (#1213639)

* Wed Apr 22 2015 Robert Scheck <robert@fedoraproject.org> 2.77-1
- Upgrade to 2.77 (#1213639)

* Sun Mar 29 2015 Robert Scheck <robert@fedoraproject.org> 2.76-1
- Upgrade to 2.76 (#1206857)

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.75-4
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.75-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.75-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 21 2014 Robert Scheck <robert@fedoraproject.org> 2.75-1
- Upgrade to 2.75

* Sat Aug 31 2013 Robert Scheck <robert@fedoraproject.org> 2.74-1
- Upgrade to 2.74 (#971523, thanks to Philip Prindeville)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.73-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 2.73-5
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.73-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Oct 24 2012 Robert Scheck <robert@fedoraproject.org> 2.73-3
- Re-enabled embedded perl feature (thanks to Alexander Dalloz)

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.73-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jan 23 2012 Robert Scheck <robert@fedoraproject.org> 2.73-1
- Upgrade to 2.73 (#759805, thanks to Philip Prindeville)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.72-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Dec 26 2011 Robert Scheck <robert@fedoraproject.org> 2.72-3
- Removed requirement on sendmail-cf for postfix (#754847)

* Sat Oct 08 2011 Robert Scheck <robert@fedoraproject.org> 2.72-2
- Added build requirement to perl(ExtUtils::MakeMaker)
- Reflected changed parameters to disable binary stripping

* Sat Oct 08 2011 Robert Scheck <robert@fedoraproject.org> 2.72-1
- Upgrade to 2.72

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.71-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Oct 05 2010 Robert Scheck <robert@fedoraproject.org> 2.71-1
- Upgrade to 2.71

* Sun Mar 28 2010 Robert Scheck <robert@fedoraproject.org> 2.68-1
- Upgrade to 2.68

* Mon Dec 21 2009 Robert Scheck <robert@fedoraproject.org> 2.67-3
- Rebuilt against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.67-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Apr 05 2009 Robert Scheck <robert@fedoraproject.org> 2.67-1
- Upgrade to 2.67

* Mon Feb 23 2009 Robert Scheck <robert@fedoraproject.org> 2.65-2
- Rebuilt against gcc 4.4 and rpm 4.6

* Thu Sep 04 2008 Robert Scheck <robert@fedoraproject.org> 2.65-1
- Upgrade to 2.65

* Sat Feb 09 2008 Robert Scheck <robert@fedoraproject.org> 2.64-1
- Upgrade to 2.64

* Wed Aug 29 2007 Robert Scheck <robert@fedoraproject.org> 2.63-1
- Upgrade to 2.63
- Updated the license tag according to the guidelines

* Mon May 07 2007 Robert Scheck <robert@fedoraproject.org> 2.62-2
- Changed sendmail build requirement slightly (#237157)

* Mon Apr 16 2007 Robert Scheck <robert@fedoraproject.org> 2.62-1
- Upgrade to 2.62

* Wed Feb 14 2007 Robert Scheck <robert@fedoraproject.org> 2.61-1
- Upgrade to 2.61 (#228757)

* Tue Dec 19 2006 Robert Scheck <robert@fedoraproject.org> 2.58-3
- Use Unix::Syslog over deprecated Sys::Syslog support (#219988)

* Sat Dec 16 2006 Robert Scheck <robert@fedoraproject.org> 2.58-2
- Include the /etc/mail/mimedefang-ip-key file (#219381)

* Wed Nov 08 2006 Robert Scheck <robert@fedoraproject.org> 2.58-1
- Upgrade to 2.58 (#212657)

* Tue Oct 03 2006 Robert Scheck <robert@fedoraproject.org> 2.57-5
- Rebuilt

* Sat Sep 16 2006 Robert Scheck <robert@fedoraproject.org> 2.57-4
- Removed two hardcoded versioned requirements (#196101 #c13)

* Mon Sep 11 2006 Robert Scheck <robert@fedoraproject.org> 2.57-3
- Disable stripping to have a non-empty -debuginfo package
- Added %%configure parameter for finding libmilter.a on x86_64

* Wed Jun 21 2006 Robert Scheck <robert@fedoraproject.org> 2.57-2
- Changes to match with Fedora Packaging Guidelines (#196101)

* Tue Jun 20 2006 Robert Scheck <robert@fedoraproject.org> 2.57-1
- Upgrade to 2.57

* Tue Mar 07 2006 Robert Scheck <robert@fedoraproject.org> 2.56-1
- Upgrade to 2.56

* Mon Feb 06 2006 Robert Scheck <robert@fedoraproject.org> 2.55-1
- Upgrade to 2.55

* Sat Dec 24 2005 Robert Scheck <robert@fedoraproject.org> 2.54-1
- Upgrade to 2.54

* Mon Sep 19 2005 Robert Scheck <robert@fedoraproject.org> 2.53-1
- Upgrade to 2.53

* Thu Jun 02 2005 Robert Scheck <robert@fedoraproject.org> 2.52-1
- Upgrade to 2.52

* Sun Mar 13 2005 Robert Scheck <robert@fedoraproject.org> 2.51-2
- Rebuilt against gcc 4.0

* Tue Feb 08 2005 Robert Scheck <robert@fedoraproject.org> 2.51-1
- Upgrade to 2.51

* Mon Dec 13 2004 Robert Scheck <robert@fedoraproject.org> 2.49-1
- Upgrade to 2.49

* Sun Nov 07 2004 Robert Scheck <robert@fedoraproject.org> 2.47-1
- Upgrade to 2.47 and some spec file cleanups

* Mon Oct 04 2004 Robert Scheck <robert@fedoraproject.org> 2.45-1
- Upgrade to 2.45 and lots of spec file cleanups

* Thu Jul 15 2004 Robert Scheck <robert@fedoraproject.org> 2.44-1
- Upgrade to 2.44
- Move sa-mimedefang.cf from /etc/mail/spamassassin to /etc/mail

* Mon May 10 2004 Robert Scheck <robert@fedoraproject.org> 2.43-1
- Upgrade to 2.43

* Wed Mar 31 2004 Robert Scheck <robert@fedoraproject.org> 2.42-1
- Upgrade to 2.42

* Thu Mar 18 2004 Robert Scheck <robert@fedoraproject.org> 2.41-1
- Upgrade to 2.41
- Few fixes and cleanup in the spec file

* Mon Mar 08 2004 Robert Scheck <robert@fedoraproject.org> 2.40-1
- Upgrade to 2.40

* Wed Jan 07 2004 Robert Scheck <robert@fedoraproject.org> 2.39-2
- Fixed spec file problems with chkconfig

* Sat Nov 29 2003 Robert Scheck <robert@fedoraproject.org> 2.39-1
- Upgrade to 2.39

* Sat Oct 11 2003 Robert Scheck <robert@fedoraproject.org> 2.38-1
- Upgrade to 2.38
- Initial spec file for Red Hat Linux

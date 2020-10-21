Summary: Transparent SMTP/LMTP proxy filter using spamassassin
Name: spampd
Version: 2.30
Release: 33%{?dist}
License: GPLv2+
URL: http://www.worlddesign.com/index.cfm/rd/mta/spampd.htm
Source0: http://www.worlddesign.com/Content/rd/mta/spampd/spampd-%{version}.tar.gz
Source1: spampd.service
Source2: README.systemd
Source3: spampd.sysconfig
# Fix POD errors, <https://github.com/mpaperno/spampd/issues/1>
Patch0:  spampd-2.30-Fix-POD-errors.patch
Patch1:  spampd-2.30-untaint.patch
Patch2:  spampd-2.30-no-pid-file.patch

BuildRequires: perl-generators
BuildRequires: perl-podlators
BuildRequires: perl-Pod-Html
BuildRequires: systemd-units

Requires(pre): /usr/sbin/useradd
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

BuildArch: noarch

%description
Spampd is a program used within an e-mail delivery system to scan messages for
possible Unsolicited Commercial E-mail (UCE, aka spam) content. It uses
SpamAssassin (SA) to do the actual message scanning. Spampd acts as a
transparent SMTP/LMTP proxy between two mail servers, and during the
transaction it passes the mail through SA. If SA decides the mail could be
spam, then spampd will ask SA to add some headers and a report to the message
indicating it's spam and why.


%prep
%setup -q
%patch0 -p1
%patch1 -p0 -b .untaint
%patch2 -p0 -b .no-pid-file
%{__rm} -f spampd.html
%{__chmod} -x changelog.txt
%{__cp} %{SOURCE2} .


%build
%{__make} spampd.8
%{__make} spampd.html


%install
%{__rm} -rf %{buildroot}
# Main program
%{__install} -D -p -m 0755 spampd \
    %{buildroot}%{_sbindir}/spampd
# Man page
%{__install} -D -p -m 0644 spampd.8 \
    %{buildroot}%{_mandir}/man8/spampd.8
# Init script
%{__install} -D -p -m 0644 %{SOURCE1} \
    %{buildroot}%{_unitdir}/spampd.service
# Sysconfig
%{__install} -D -p -m 0644 %{SOURCE3} \
    %{buildroot}%{_sysconfdir}/sysconfig/spampd
# Home directory
%{__mkdir_p} %{buildroot}/var/spool/spampd



%pre
/usr/sbin/useradd -r -M -s /sbin/nologin -d /var/spool/spampd \
    spampd &>/dev/null || :

%post
%systemd_post spampd.service

%preun
%systemd_preun spampd.service

%postun
%systemd_postun_with_restart spampd.service

%files
%doc changelog.txt spampd.html README.systemd
%config(noreplace) %{_sysconfdir}/sysconfig/spampd
%{_unitdir}/spampd.service
%{_sbindir}/spampd
%{_mandir}/man8/spampd.8*
%attr(0750,spampd,spampd) /var/spool/spampd/


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.30-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.30-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.30-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.30-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.30-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.30-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.30-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.30-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.30-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Dec 18 2015 Bojan Smojver <bojan@rexursive.com> - 2.30-24
- want sa-update.timer in the service file
- add perl-podlators to BuildRequires: build failing for F-24
- add perl-Pod-Html to BuildRequires: build failing for F-24

* Tue Aug 11 2015 Bojan Smojver <bojan@rexursive.com> - 2.30-23
- fix bug #1252113: remove exec permission from service file

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.30-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.30-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May  7 2014 Bojan Smojver <bojan@rexursive.com> - 2.30-20
- set user/group in systemd service file to avoid executing as root

* Fri Apr 25 2014 Bojan Smojver <bojan@rexursive.com> - 2.30-19
- set --maxsize=500 by default to be in line with SA

* Thu Apr 24 2014 Bojan Smojver <bojan@rexursive.com> - 2.30-18
- move --tagall and --local-only options to sysconfig, to be able to override
- use short option names where possible

* Fri Jan 31 2014 Bojan Smojver <bojan@rexursive.com> - 2.30-17
- provide default sysconfig file

* Mon Dec 09 2013 Bojan Smojver <bojan@rexursive.com> - 2.30-16
- convert to systemd
- untaint some variables (Perl 5.18)
- do not create PID file if not detaching

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.30-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild
- Fix POD errors

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 2.30-14
- Perl 5.18 rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.30-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.30-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.30-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.30-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Sep 29 2009 Warren Togami <wtogami@redhat.com> - 2.30-9
- Mail::SPF::Query is long obsolete, replaced by SPF::Query
  removing this artificial dep because SPF is nearly useless

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.30-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri May  8 2009 Matthias Saou <http://freshrpms.net/> 2.30-7
- Require perl(Mail::SPF::Query) to have SPF checks available by default.

* Sun Apr 12 2009 Matthias Saou <http://freshrpms.net/> 2.30-6
- Update init script to the new style.
- Add missing Requires(pre): /usr/sbin/useradd.

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Aug  6 2007 Matthias Saou <http://freshrpms.net/> 2.30-4
- Update License field.
- Remove dist tag, since the package will seldom change.

* Mon Jan 29 2007 Matthias Saou <http://freshrpms.net/> 2.30-3
- Fix %%pre typo (/dev/nulll).
- Silence %%setup.
- Add scriplet chkconfig and service requirements.

* Tue Nov  7 2006 Matthias Saou <http://freshrpms.net/> 2.30-2
- Initial RPM release.


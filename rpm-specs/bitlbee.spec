%bcond_without otr

%if 0%{?fedora} >= 15 || 0%{?rhel} >= 7
%bcond_without systemd
%else
%bcond_with systemd
%endif

# libpurple requires forkdaemon or inetd mode, however forkdaemon needed
# adapted SELinux policy in former times.
%if 0%{?fedora} >= 22 || 0%{?rhel} >= 7
%bcond_without purple
%else
%bcond_with purple
%endif

Summary:           IRC to other chat networks gateway
Name:              bitlbee
Version:           3.6
Release:           3%{?dist}
License:           GPLv2+ and MIT
URL:               https://www.bitlbee.org/
Source0:           https://get.bitlbee.org/src/%{name}-%{version}.tar.gz
# Downstream: Run bitlbee as non-root and bind to 127.0.0.1 only
Patch0:            bitlbee-forkdaemon.patch
# Downstream: Still support glib2 < 2.32 for RHEL/CentOS 6 for now
Patch1:            bitlbee-3.6-glib2.patch

Requires(pre):     shadow-utils
BuildRequires:     gcc
BuildRequires:     glib2-devel >= 2.16
BuildRequires:     gnutls-devel
%if %{with systemd}
BuildRequires:     pkgconfig(systemd)
%{?systemd_requires}
%else
Requires(preun):   /sbin/service
Requires:          xinetd
%endif
%if %{with otr}
BuildRequires:     libotr-devel >= 4.0
%endif
%if %{with purple}
BuildRequires:     libpurple-devel
%endif
BuildRequires:     %{_bindir}/python3

# Documentation (user-guide.html)
BuildRequires:     libxslt
BuildRequires:     docbook-style-xsl

%description
BitlBee is an IRC to other chat networks gateway. BitlBee can be used as
an IRC server which forwards everything you say to people on other chat
networks like XMPP/Jabber (including Google Talk and Hipchat) and Twitter
microblogging network (and all other Twitter API compatible services like
status.net). There are also plugins for facebook and steam, and even more
protocols can be used via libpurple.

%package devel
Summary:           Development files for bitlbee
Requires:          %{name}%{?_isa} = %{version}-%{release}, pkgconfig

%description devel
The bitlbee-devel package includes header files necessary for building and
developing programs and plugins which use bitlbee.

%if %{with otr}
%package otr
Summary:           OTR plugin for bitlbee
Requires:          %{name}%{?_isa} = %{version}-%{release}

%description otr
The bitlbee-otr package includes OTR plugin for bitlbee. Off-the-Record
messaging, commonly referred to as OTR, provides perfect forward secrecy
and malleable encryption.
%endif

%prep
echo With OTR %with_otr
echo With systemd %with_systemd
%setup -q
%if %{with systemd}
%patch0 -p1
%endif
%if 0%{?rhel} == 6
%patch1 -p1
%endif

%build
# Note that we cannot use openssl in Fedora packages ... it breaks GPL
export PYTHON="%{_bindir}/python3"
export CFLAGS="$RPM_OPT_FLAGS"
./configure \
  --prefix=%{_prefix} \
  --bindir=%{_sbindir} \
  --etcdir=%{_sysconfdir}/%{name} \
  --mandir=%{_mandir} \
  --datadir=%{_datadir}/%{name} \
  --config=%{_localstatedir}/lib/%{name} \
  --pcdir=%{_libdir}/pkgconfig \
  --plugindir=%{_libdir}/%{name} \
  --strip=0 \
  --plugins=1 \
  --ssl=gnutls \
  --jabber=1 \
  --twitter=1 \
%if %{with purple}
  --purple=1 \
%endif
%if %{with otr}
  --otr=plugin
%endif

make %{?_smp_mflags}
(cd doc/user-guide/ && make user-guide.html)

%install
make DESTDIR=$RPM_BUILD_ROOT install install-dev install-etc

# Install some files manually to their correct destination
mkdir -p $RPM_BUILD_ROOT{%{_localstatedir}/lib,%{_libdir}}/%{name}/
%if %{with systemd}
make DESTDIR=$RPM_BUILD_ROOT install-systemd
%else
install -D -p -m 644 doc/%{name}.xinetd $RPM_BUILD_ROOT%{_sysconfdir}/xinetd.d/%{name}
%endif
install -D -p -m 644 %{name}.conf $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/%{name}.conf

%pre
getent group %{name} > /dev/null || %{_sbindir}/groupadd -r %{name}
getent passwd %{name} > /dev/null || %{_sbindir}/useradd -r -g %{name} -d %{_localstatedir}/lib/%{name} -s /sbin/nologin -c "BitlBee User" %{name}
exit 0

%if %{with systemd}
%post
  %systemd_post %{name}.service
%endif

%preun
%if %{with systemd}
  %systemd_preun %{name}.service
%else
if [ $1 -eq 0 ]; then
  /sbin/service xinetd condrestart > /dev/null 2>&1
fi
%endif

%postun
%if %{with systemd}
  %systemd_postun_with_restart %{name}.service
%else
if [ $1 -eq 1 ]; then
  /sbin/service xinetd condrestart > /dev/null 2>&1
fi
%endif

%files
%license COPYING
%doc doc/{AUTHORS,CHANGES,CREDITS,FAQ,README}
%doc doc/user-guide/user-guide.html
%attr(0750,bitlbee,bitlbee) %dir %{_sysconfdir}/%{name}/
%attr(0640,bitlbee,bitlbee) %config(noreplace) %{_sysconfdir}/%{name}/*
%{_sbindir}/%{name}
%dir %{_libdir}/%{name}/
%{_datadir}/%{name}/
%{_mandir}/man?/%{name}*
%attr(0750,bitlbee,bitlbee) %dir %{_localstatedir}/lib/%{name}/
%if %{with systemd}
%{_unitdir}/%{name}*
%else
%config(noreplace) %{_sysconfdir}/xinetd.d/%{name}
%endif

%files devel
%doc doc/example_plugin.c
%{_includedir}/%{name}/
%{_libdir}/pkgconfig/%{name}.pc

%if %{with otr}
%files otr
%{_libdir}/%{name}/otr.so
%endif

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 29 2019 Robert Scheck <robert@fedoraproject.org> 3.6-1
- Upgrade to 3.6

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.2-0.3.20180919git0b1448f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.2-0.2.20180919git0b1448f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Sep 19 2018 Adam Williamson <awilliam@redhat.com> - 3.5.2-0.1.20180919git0b1448f
- Bump to latest git snapshot (for openssl 1.1 and twitter fixes)

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.5.1-6
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 30 2017 Robert Scheck <robert@fedoraproject.org> 3.5.1-1
- Upgrade to 3.5.1

* Mon Jan 09 2017 Matěj Cepl <mcepl@redhat.com> - 3.5-1
- New upstream release (#1411171)

* Tue Jun 14 2016 Matěj Cepl <mcepl@redhat.com> - 3.4.2-2
- Switch off build OTR plugin for EL6 (see
  https://bugs.bitlbee.org/ticket/1163 for explanation, and if desired
  an user must build himself https://github.com/dequis/bitlbee-otr3;
  fixes #1346182).

* Sun Mar 20 2016 Matěj Cepl <mcepl@redhat.com> - 3.4.2-1
- New upstream release (#1319428)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Matej Cepl <mcepl@redhat.com> - 3.4.1-1
- New upstream release (#1205936)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar 26 2015 Matej Cepl <mcepl@redhat.com> - 3.4-1
- New upstream release.
- Requires libotr >= 4 (so EPEL-6 will require new build of libotr 4)

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Aug 07 2014 Robert Scheck <robert@fedoraproject.org> 3.2.2-4
- Disable libpurple due to dbus issues also in EPEL (#1126930)

* Tue Jul 22 2014 Robert Scheck <robert@fedoraproject.org> 3.2.2-3
- Really disable libpurple support for Fedora except Rawhide

* Mon Jul 14 2014 Robert Scheck <robert@fedoraproject.org> 3.2.2-2
- Enable forkdaemon due lacking SELinux policy in Rawhide only
- Disable libpurple conflicting with the daemon mode (#1117553)

* Sun Jul 06 2014 Robert Scheck <robert@fedoraproject.org> 3.2.2-1
- Upgrade to 3.2.2 (#1116567)
- Enable libpurple support additionally to built-in protocols

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 29 2014 Matěj Cepl <mcepl@redhat.com> - 3.2.1-4
- Add server_args to /etc/xinetd.d/bitlbee (#1102062)

* Wed Feb 05 2014 Matěj Cepl <mcepl@redhat.com> - 3.2.1-3
- Eliminate our own bitlbee.xinetd by patching the upstream one.

* Wed Dec 18 2013 Robert Scheck <robert@fedoraproject.org> 3.2.1-2
- Some spec file cleanups and ensure that RHEL 5 builds again

* Thu Nov 28 2013 Matěj Cepl <mcepl@redhat.com> - 3.2.1-1
- Update to the latest upstream (mainly Twitter API issues, #1035504)

* Tue Sep 24 2013 Adam Williamson <awilliam@redhat.com> - 3.2-7.20130713bzr997
- let's just go to latest upstream bzr, since there's no new release
- drop nss-crash-rhbz922447.patch, merged upstream as rev 987

* Fri Aug 16 2013 Matěj Cepl <mcepl@redhat.com> - 3.2-6
- systemd socket should be opened over IPv6 as well (#949303)
- return fix for NSS crash (#922447)

* Fri Aug 16 2013 Matěj Cepl <mcepl@redhat.com> - 3.2-5
- Add a conditional patch for F>=20 to build with libotr4

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Apr 02 2013 Matěj Cepl <mcepl@redhat.com> - 3.2-3
- Add upstream patch to avoid double-free crash (#922447)

* Thu Mar 14 2013 Robert Scheck <robert@fedoraproject.org> 3.2-2
- Add accidentially lost OTR support for RHEL 5 and 6 (#919912)

* Wed Feb 20 2013 Robert Scheck <robert@fedoraproject.org> 3.2-1
- Upgrade to 3.2 (#912675, thanks to Eike Hein and Rex Dieter)
- Use the new systemd macros (#850048, thanks to Václav Pavlín)

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jul 24 2012 Matej Cepl <mcepl@redhat.com> - 3.0.5-4
- The last version of SSL/NSS patch for the upstream #714

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 21 2012 Matej Cepl <mcepl@redhat.com> - 3.0.5-2
- Add more error handling to lib/ssl_nss.c
- Checking patches for compatibility with the current state of the word
  and updating comments.
- Improve otr conditional

* Sat Mar 31 2012 Adam Williamson <awilliam@redhat.com> - 3.0.5-1
- new upstream release 3.0.5

* Sat Jan 14 2012 Adam Williamson <awilliam@redhat.com> - 3.0.4-3
- add upstream fix for a high-priority twitter disconnect/crasher

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Williamson <awilliam@redhat.com> - 3.0.4-1
- new upstream release 3.0.4
- drop 823_822.diff (merged upstream obviously)

* Fri Nov 11 2011 Adam Williamson <awilliam@redhat.com> - 3.0.3-6
- 823_822.diff: fix MSN login (upstream rev #823)

* Thu Aug 04 2011 Matěj Cepl <mcepl@redhat.com> - 3.0.3-5
- Tiny typo in systemd units.

* Sat Jul 30 2011 Matěj Cepl <mcepl@redhat.com> - 3.0.3-4
- Rebuilt against new libraries.

* Thu Jul 28 2011 Matěj Cepl <mcepl@redhat.com> - 3.0.3-3
- Add Restart=always to systemd (following discussion on upstream #738).

* Mon Jul 25 2011 Matěj Cepl <mcepl@redhat.com> - 3.0.3-2
- One more fix to the systemd unit files (#705096)

* Wed Mar 09 2011 Matěj Cepl <mcepl@redhat.com> - 3.0.2-1
- New upstream release. We can eliminate parts which were already merged
  upstream (ssl_pending patch)

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jan 09 2011 Matěj Cepl <mcepl@redhat.com> - 3.0.1-8
- Fix crash when no SRV record is provided (#668190); fix by Ricky Zhou

* Wed Dec 29 2010 Matěj Cepl <mcepl@redhat.com> - 3.0.1-7
- Adding more missing systemd-support pieces and eliminate xinetd on F<15

* Tue Dec 28 2010 Matěj Cepl <mcepl@redhat.com> - 3.0.1-6
- commented all patches with status of their upstreaming
- two tiny fixes for SSL implementation (#666022)

* Mon Dec 27 2010 Matěj Cepl <mcepl@redhat.com> - 3.0.1-5
- Systemd support

* Mon Dec 27 2010 Matěj Cepl <mcepl@redhat.com> - 3.0.1-4
- Add Ricky Zhou's fixed patch for libresolv (#663934)

* Sun Dec 26 2010 Matěj Cepl <mcepl@redhat.com> - 3.0.1-3
- Add bitlbee-des3-implement patch with working ssl_des3_encrypt
  implementation by Ricky Zhou.

* Sat Dec 25 2010 Matěj Cepl <mcepl@redhat.com> - 3.0.1-2
- Implement missing ssl_pending() (Fix by Ricky Zhou, #665553)

* Sat Dec 04 2010 Matěj Cepl <mcepl@redhat.com> - 3.0.1-1
- New upstream release
- Switched to NSS (3DES still via lib/des.c)
- Added -otr subpackage with optional OTR plugin.

* Sun Nov 21 2010 Matěj Cepl <mcepl@redhat.com> - 3.0-2
- Get rid of bad regexp magic, now with pure DESTDIR.

* Fri Oct 22 2010 Matěj Cepl <mcepl@redhat.com> - 3.0-1
- New upstream release.

* Sun Jul 04 2010 Robert Scheck <robert@fedoraproject.org> 1.2.8-1
- Upgrade to 1.2.8

* Sat May 15 2010 Robert Scheck <robert@fedoraproject.org> 1.2.7-1
- Upgrade to 1.2.7

* Sun Apr 25 2010 Robert Scheck <robert@fedoraproject.org> 1.2.6a-3
- Updated the description to reflect twitter support
- Really fixed the optional libresolv patch this time

* Tue Apr 20 2010 Robert Scheck <robert@fedoraproject.org> 1.2.6a-2
- Remerged the optional libresolv patch for 1.2.6a

* Tue Apr 20 2010 Robert Scheck <robert@fedoraproject.org> 1.2.6a-1
- Upgrade to 1.2.6a (#584071)

* Thu Mar 18 2010 Robert Scheck <robert@fedoraproject.org> 1.2.5-1
- Upgrade to 1.2.5

* Sat Oct 17 2009 Robert Scheck <robert@fedoraproject.org> 1.2.4-1
- Upgrade to 1.2.4

* Mon Aug 17 2009 Robert Scheck <robert@fedoraproject.org> 1.2.3-4
- Updated libresolv patch to not segfault when connecting to the
  Jabber/XMPP server if there's no SRV record (#506719, #501786)
- Added -devel subpackage with header files for plugins (#504882)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Robert Scheck <robert@fedoraproject.org> 1.2.3-2
- Rebuilt against gcc 4.4 and rpm 4.6

* Sun Sep 07 2008 Robert Scheck <robert@fedoraproject.org> 1.2.3-1
- Upgrade to 1.2.3 (#461424)

* Wed Aug 27 2008 Robert Scheck <robert@fedoraproject.org> 1.2.2-1
- Upgrade to 1.2.2 (#460355)

* Mon Jul 07 2008 Robert Scheck <robert@fedoraproject.org> 1.2.1-1
- Upgrade to 1.2.1 (thanks to Matěj Cepl)

* Tue Apr 15 2008 Robert Scheck <robert@fedoraproject.org> 1.2-1
- Upgrade to 1.2 (#439047, thanks to Matěj Cepl)

* Sun Feb 10 2008 Robert Scheck <robert@fedoraproject.org> 1.0.4-2
- Rebuilt against gcc 4.3

* Wed Aug 29 2007 Robert Scheck <robert@fedoraproject.org> 1.0.4-1
- Upgrade to 1.0.4
- Updated the license tag according to the guidelines

* Mon May 07 2007 Robert Scheck <robert@fedoraproject.org> 1.0.3-6
- Rebuilt

* Sat Oct 21 2006 Robert Scheck <robert@fedoraproject.org> 1.0.3-5
- Create a bitlbee user and condrestart xinetd instead of reload

* Fri Aug 04 2006 Robert Scheck <robert@fedoraproject.org> 1.0.3-4
- Switched to gnutls per default for SSL support (#196591 #c12)

* Mon Jun 26 2006 Robert Scheck <robert@fedoraproject.org> 1.0.3-3
- Added patch for using CFLAGS env (#196591 #c4, upstream #171)

* Sun Jun 25 2006 Robert Scheck <robert@fedoraproject.org> 1.0.3-2
- Changes to match with Fedora Packaging Guidelines (#196591)

* Sun Jun 25 2006 Robert Scheck <robert@fedoraproject.org> 1.0.3-1
- Upgrade to 1.0.3

* Sun Apr 02 2006 Robert Scheck <robert@fedoraproject.org> 1.0.2-1
- Upgrade to 1.0.2

* Sun Jan 15 2006 Robert Scheck <robert@fedoraproject.org> 1.0.1-1
- Upgrade to 1.0.1

* Wed Dec 28 2005 Robert Scheck <robert@fedoraproject.org> 1.0-2
- Rebuilt against gcc 4.1

* Mon Dec 05 2005 Robert Scheck <robert@fedoraproject.org> 1.0-1
- Upgrade to 1.0

* Sat Nov 12 2005 Robert Scheck <robert@fedoraproject.org> 0.92-4
- Rebuilt against openssl 0.9.8a

* Sun Aug 28 2005 Robert Scheck <robert@fedoraproject.org> 0.92-3
- Added patch, that allows specifying the Jabber server manually
- Don't start bitlbee per default as xinetd service

* Sun Jul 03 2005 Robert Scheck <robert@fedoraproject.org> 0.92-2
- Added patch giving ICQ/AIM support for typing notifications

* Fri Jul 01 2005 Robert Scheck <robert@fedoraproject.org> 0.92-1
- Upgrade to 0.92
- Initial spec file for Fedora Core

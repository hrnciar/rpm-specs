%undefine __cmake_in_source_build

# linphone currently FTBFS rawhide/f29+
%if 0%{?fedora} < 29
#global jingle 1
%endif

Name:    kopete
Summary: Instant messenger
Version: 20.08.1
Release: 1%{?dist}

License: GPLv2+ and GFDL
URL:     https://www.kde.org/applications/internet/kopete/
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0: http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz

## upstream patches

## upstreamable patches
Patch100: kopete-17.08.3-openssl-1.1.patch

BuildRequires: gcc-c++ gcc
BuildRequires: desktop-file-utils

BuildRequires: extra-cmake-modules
BuildRequires: kf5-rpm-macros

BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5Crash)
BuildRequires: cmake(KF5DBusAddons)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(KF5Emoticons)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5KCMUtils)
BuildRequires: cmake(KF5KHtml)
BuildRequires: cmake(KF5NotifyConfig)
BuildRequires: cmake(KF5Parts)
BuildRequires: cmake(KF5TextEditor)
BuildRequires: cmake(KF5Wallet)
BuildRequires: cmake(KF5KDELibs4Support)

BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(Qt5Xml)
BuildRequires: cmake(Qt5Sql)
BuildRequires: cmake(Qt5Test)

BuildRequires: cmake(Phonon4Qt5)

BuildRequires: cmake(KF5Contacts)
BuildRequires: cmake(KF5IdentityManagement)
BuildRequires: cmake(KF5Libkleo)

BuildRequires: cmake(KF5DNSSD)

BuildRequires: cmake(Qca-qt5)

BuildRequires: giflib-devel
BuildRequires: perl-generators

BuildRequires: pkgconfig(alsa)
BuildRequires: openslp-devel
BuildRequires: pkgconfig(libgadu) >= 1.8.0
# jingle dependencies
%if 0%{?jingle:1}
BuildRequires: expat-devel
BuildRequires: linphone-devel
BuildRequires: pkgconfig(mediastreamer)
BuildRequires: openssl-devel
BuildRequires: pkgconfig(jsoncpp)
BuildRequires: pkgconfig(ortp)
%endif
BuildRequires: openssl-devel
BuildRequires: pkgconfig(jasper)
BuildRequires: pkgconfig(libidn)
BuildRequires: pkgconfig(libotr)
BuildRequires: pkgconfig(libv4l2)
BuildRequires: pkgconfig(libxslt)
BuildRequires: pkgconfig(meanwhile)
BuildRequires: pkgconfig(speex)
BuildRequires: pkgconfig(sqlite3)
BuildRequires: libvncserver-devel
BuildRequires: openldap-devel

Obsoletes: kopete-cryptography < %{version}-%{release}

Provides: bundled(iris) = 2.0.0

Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: qca-qt5-ossl%{?_isa}

Conflicts: kde-l10n < 17.08.3-5

%description
%{summary}.

%package libs
Summary: Runtime libraries for %{name}
Requires: %{name} = %{version}-%{release}
%description libs
%{summary}.

%package devel
Summary: Developer files for %{name}
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
%description devel
%{summary}.


%prep
%autosetup -p1


%build
# disable oscar support due to FTBFS,
# https://bugs.kde.org/show_bug.cgi?id=393372
%{cmake_kf5} \
  %{?!jingle:-DWITH_libjingle:BOOL=OFF} \
  -DWITH_wlm:BOOL=OFF
%cmake_build


%install
%cmake_install

%find_lang %{name} --all-name --with-html


%check
desktop-file-validate %{buildroot}%{_kde4_datadir}/applications/org.kde.kopete.desktop


%files -f %{name}.lang
%license COPYING*
%{_kf5_sysconfdir}/xdg/kopete*
%{_kf5_bindir}/kopete
%if 0%{?jingle}
%{_kf5_bindir}/libjingle-call
%endif
%{_kf5_bindir}/winpopup-*
%{_kf5_datadir}/applications/org.kde.kopete.desktop
%{_kf5_metainfodir}/org.kde.kopete.appdata.xml
%{_kf5_datadir}/config.kcfg/*.kcfg
%{_kf5_datadir}/kopete/
%{_kf5_datadir}/kopete_history/
%{_kf5_datadir}/sounds/Kopete_*
%{_kf5_datadir}/kconf_update/kopete*
%{_kf5_datadir}/knotifications5/kopete.*
%{_kf5_datadir}/kservices5/*.desktop
%{_kf5_datadir}/kservices5/*.protocol
%{_kf5_datadir}/kservices5/kconfiguredialog/kopete_*
%{_kf5_datadir}/kservicetypes5/kopete*.desktop
%{_kf5_datadir}/kxmlgui5/kopete*/
%{_kf5_datadir}/icons/hicolor/*/*/*
%{_kf5_datadir}/icons/oxygen/*/*/*
%{_kf5_datadir}/qlogging-categories5/%{name}*

%ldconfig_scriptlets libs

%files libs
%{_kf5_libdir}/libkopete*.so.*
%{_kf5_libdir}/liboscar.so.*
%{_kf5_libdir}/libqgroupwise.so
%{_kf5_qtplugindir}/*.so
%{_kf5_qtplugindir}/accessible/chatwindowaccessiblewidgetfactory.so

%files devel
%{_includedir}/kopete/
%{_kf5_libdir}/libkopete*.so
%{_kf5_libdir}/liboscar.so
%{_kf5_datadir}/dbus-1/interfaces/org.kde.*.xml


%changelog
* Tue Sep 15 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.08.1-1
- 20.08.1

* Tue Aug 18 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.08.0-1
- 20.08.0

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20.04.3-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20.04.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.04.3-1
- 20.04.3

* Fri Jun 12 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.04.2-1
- 20.04.2

* Wed May 27 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.04.1-1
- 20.04.1

* Sat May 02 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.04.0-1
- 20.04.0

* Sat Mar 07 2020 Rex Dieter <rdieter@fedoraproject.org> - 19.12.3-1
- 19.12.3

* Tue Feb 04 2020 Rex Dieter <rdieter@fedoraproject.org> - 19.12.2-1
- 19.12.2

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 19.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 13 2020 Rex Dieter <rdieter@fedoraproject.org> - 19.12.1-1
- 19.12.1

* Tue Nov 12 2019 Rex Dieter <rdieter@fedoraproject.org> - 19.08.3-1
- 19.08.3

* Thu Oct 17 2019 Rex Dieter <rdieter@fedoraproject.org> - 19.08.2-1
- 19.08.2

* Fri Oct 04 2019 Rex Dieter <rdieter@fedoraproject.org> - 19.08.1-1
- 19.08.1

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 19.04.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 12 2019 Rex Dieter <rdieter@fedoraproject.org> - 19.04.3-1
- 19.04.3

* Tue Jun 04 2019 Rex Dieter <rdieter@fedoraproject.org> - 19.04.2-1
- 19.04.2

* Wed May 08 2019 Rex Dieter <rdieter@fedoraproject.org> - 19.04.1-1
- 19.04.1

* Fri Mar 08 2019 Rex Dieter <rdieter@fedoraproject.org> - 18.12.3-1
- 18.12.3

* Tue Feb 05 2019 Rex Dieter <rdieter@fedoraproject.org> - 18.12.2-1
- 18.12.2

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 18.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 08 2019 Rex Dieter <rdieter@fedoraproject.org> - 18.12.1-1
- 18.12.1

* Sun Dec 16 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.12.0-1
- 18.12.0

* Tue Nov 06 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.08.3-1
- 18.08.3

* Wed Oct 10 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.08.2-1
- 18.08.2

* Mon Oct 01 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.08.1-1
- 18.08.1

* Mon Sep 10 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.04.3-4
- Requires: qca-qt5-ossl (#1625314)

* Wed Aug 15 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.04.3-3
- Conflicts: kde-l10n < 17.08.3-5

* Mon Jul 23 2018 Than Ngo <than@redhat.com> - 18.04.3-2
- fixed FTBFS

* Fri Jul 13 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.04.3-1
- 18.04.3

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 18.04.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 06 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.04.2-1
- 18.04.2

* Wed May 09 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.04.1-1
- 18.04.1

* Tue Apr 24 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.04.0-2
- enable oscar support (pull in upstream fix, kde#393372)

* Sat Apr 21 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.04.0-1
- 18.04.0
- disable wlm (deprecated)
- oscar disabled (for now, kde#393372)
- libjingle disabled f29+ (linphon/mediastreamer FTBFS)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 17.08.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 17.08.3-4
- Remove obsolete scriptlets

* Fri Jan 05 2018 Kevin Kofler <Kevin@tigcc.ticalc.org> - 17.08.3-3
- fix build against OpenSSL 1.1

* Tue Dec 26 2017 Björn Esser <besser82@fedoraproject.org> - 17.08.3-2
- Rebuilt for jsoncpp.so.20

* Wed Nov 08 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.08.3-1
- 17.08.3

* Wed Oct 11 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.08.2-1
- 17.08.2

* Thu Sep 28 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.08.1-1
- 17.08.1

* Fri Sep 01 2017 Björn Esser <besser82@fedoraproject.org> - 17.04.3-2
- Rebuilt for jsoncpp-1.8.3

* Thu Aug 03 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.04.3-1
- 17.04.3

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 17.04.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 17.04.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 15 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.04.2-1
- 17.04.2

* Sun Jun 04 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.04.1-1
- 17.04.1

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 16.12.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Mar 10 2017 Rex Dieter <rdieter@fedoraproject.org> - 16.12.3-1
- 16.12.3

* Sat Feb 11 2017 Rex Dieter <rdieter@fedoraproject.org> - 16.12.2-2
- backport CVE-2017-5593 security fix, update URL

* Thu Feb 09 2017 Rex Dieter <rdieter@fedoraproject.org> - 16.12.2-1
- 16.12.2

* Tue Jan 10 2017 Rex Dieter <rdieter@fedoraproject.org> - 16.12.1-1
- 16.12.1

* Mon Dec 05 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.08.3-1
- 16.08.3

* Mon Dec 05 2016 Than Ngo <than@redhat.com> - 16.08.2-2
- rebuild against new jasper-2.0.0

* Thu Oct 13 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.08.2-1
- 16.08.2

* Tue Oct 04 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.08.1-3
- rebuild

* Thu Sep 22 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.08.1-2
- Provides: bundled(iris) = 2.0.0 (#737305)

* Wed Sep 07 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.08.1-1
- 16.08.1

* Tue Aug 16 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.08.0-2
- respin

* Sat Aug 13 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.08.0-1
- 16.08.0

* Sat Aug 06 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.07.90-1
- 16.07.90

* Sun Jul 31 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.07.80-1
- 16.07.80

* Sat Jul 09 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.04.3-1
- 16.04.3

* Sun Jun 12 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.04.2-1
- 16.04.2

* Sun May 08 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.04.1-1
- 16.04.1

* Mon Apr 18 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.04.0-1
- 16.04.0

* Mon Apr 18 2016 Rex Dieter <rdieter@fedoraproject.org> - 15.12.3-3
- update URL (#1325270)

* Tue Mar 29 2016 Björn Esser <fedora@besser82.io> - 15.12.3-2
- Rebuilt for libjsoncpp.so.1

* Tue Mar 15 2016 Rex Dieter <rdieter@fedoraproject.org> - 15.12.3-1
- 15.12.3

* Tue Feb 23 2016 Rex Dieter <rdieter@fedoraproject.org> 15.12.2-3
- disable msn/wlm support

* Tue Feb 16 2016 Than Ngo <than@redhat.com> - 15.12.2-2
- fix build failure with gcc6

* Mon Feb 15 2016 Rex Dieter <rdieter@fedoraproject.org> - 15.12.2-1
- 15.12.2

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 15.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 10 2016 Rex Dieter <rdieter@fedoraproject.org> - 15.12.1-1
- 15.12.1

* Tue Dec 22 2015 Rex Dieter <rdieter@fedoraproject.org> - 15.12.0-1
- 15.12.0
- omit -cryptography support on f24 (no more kde4 kdepim/kleopatra)

* Sat Dec 05 2015 Rex Dieter <rdieter@fedoraproject.org> - 15.08.3-1
- 15.08.3

* Mon Nov 02 2015 Rex Dieter <rdieter@fedoraproject.org> - 15.08.2-1
- 15.08.2, .spec cosmetics, update URL
- WITH_skype=OFF, could consider -skype subpkg too (#1262715)
- use bundled iris, fixes jabber support (#1253041)

* Thu Aug 20 2015 Than Ngo <than@redhat.com> - 15.08.0-1
- 15.08.0

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 15.04.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 10 2015 Rex Dieter <rdieter@fedoraproject.org> - 15.04.2-1
- 15.04.2

* Thu May 28 2015 Rex Dieter <rdieter@fedoraproject.org> - 15.04.1-1
- 15.04.1

* Sat Apr 18 2015 Rex Dieter <rdieter@fedoraproject.org> - 15.04.0-1
- 15.04.0

* Sun Mar 01 2015 Rex Dieter <rdieter@fedoraproject.org> - 14.12.3-1
- 14.12.3

* Tue Feb 24 2015 Than Ngo <than@redhat.com> - 14.12.2-1
- 14.12.2

* Fri Jan 30 2015 Rex Dieter <rdieter@fedoraproject.org> 14.12.1-2
- kopete-cryptography subpkg (non %%fedora case probably needswork)

* Sat Jan 17 2015 Rex Dieter <rdieter@fedoraproject.org> - 14.12.1-1
- 14.12.1

* Fri Nov 14 2014 Tom Callaway <spot@fedoraproject.org> - 4.14.3-2
- rebuild for new libsrtp

* Sun Nov 09 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.14.3-1
- 4.14.3

* Sun Oct 12 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.14.2-1
- 4.14.2

* Sat Sep 27 2014 Rex Dieter <rdieter@fedoraproject.org> 4.14.1-2
- enable cryptography plugin

* Tue Sep 16 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.14.1-1
- 4.14.1

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Aug 15 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.14.0-1
- 4.14.0

* Tue Aug 05 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.13.97-1
- 4.13.97

* Tue Jul 15 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.13.3-1
- 4.13.3

* Mon Jun 09 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.13.2-1
- 4.13.2

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.13.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun May 11 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.13.1-1
- 4.13.1

* Thu Apr 24 2014 Rex Dieter <rdieter@fedoraproject.org> 4.13.0-2
- rebuild (iris)

* Sat Apr 12 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.13.0-1
- 4.13.0

* Fri Apr 04 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.12.97-1
- 4.12.97

* Sun Mar 23 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.12.95-1
- 4.12.95

* Wed Mar 19 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.12.90-1
- 4.12.90

* Sun Mar 02 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.12.3-1
- 4.12.3

* Fri Jan 31 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.12.2-1
- 4.12.2

* Fri Jan 10 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.12.1-1
- 4.12.1

* Thu Dec 19 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.12.0-1
- 4.12.0

* Sun Dec 01 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.11.97-1
- 4.11.97

* Sat Nov 23 2013 Rex Dieter <rdieter@fedoraproject.org> 4.11.95-2
- (re)enable system iris (f21+)

* Thu Nov 21 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.11.95-1
- 4.11.95

* Sat Nov 16 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.11.90-1
- 4.11.90

* Sat Nov 02 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.11.3-1
- 4.11.3

* Sat Sep 28 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.11.2-1
- 4.11.2

* Wed Sep 04 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.11.1-1
- 4.11.1

* Sat Aug 17 2013 Rex Dieter <rdieter@fedoraproject.org> 4.11.0-2
- BR: libotr-devel sqlite-devel

* Sun Aug 11 2013 Rex Dieter <rdieter@fedoraproject.org> 4.11.0-1
- 4.11.0

* Tue Jul 30 2013 Rex Dieter <rdieter@fedoraproject.org> 4.10.97-1
- 4.10.97

* Wed Jul 24 2013 Rex Dieter <rdieter@fedoraproject.org> 4.10.95-1
- 4.10.95

* Mon Jul 08 2013 Rex Dieter <rdieter@fedoraproject.org> 4.10.90-2
- mediastreamer29.patch (kde#318825)
- BR: pkgconfig(alsa)

* Fri Jun 28 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.10.90-1
- 4.10.90

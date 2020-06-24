%global krita_python 1

# try to workaround f32+ FTBFS
#global _legacy_common_support 1

Name:           krita
Version:        4.2.9
Release:        4%{?dist}
Summary:        Krita is a sketching and painting program
License:        GPLv2+
URL:            http://krita.org
%global versiondir %(echo %{version} | cut -d. -f1-3)
#global versiondir %{version}
Source0:        http://download.kde.org/stable/krita/%{versiondir}/krita-%{version}.tar.xz

## upstream patches (lookaside cache)

%global kf5_ver 5.7
BuildRequires:  extra-cmake-modules >= 5.7
BuildRequires:  kf5-rpm-macros
BuildRequires:  cmake(KF5Archive)
BuildRequires:  cmake(KF5Completion)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5GuiAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5ItemModels)
BuildRequires:  cmake(KF5ItemViews)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5WindowSystem)

BuildRequires:  qt5-qtbase-devel >= 5.6
BuildRequires:  cmake(Qt5Multimedia)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Xml)
BuildRequires:  cmake(Qt5X11Extras)

BuildRequires:  boost-devel
# FTBFS against f27's giflib-4.1.6
%if 0%{?fedora} > 27
BuildRequires:  giflib-devel >= 5
%else
BuildConflicts: giflib-devel < 5
%endif
BuildRequires:  libtiff-devel
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(eigen3)
BuildRequires:  pkgconfig(exiv2)
BuildRequires:  pkgconfig(gsl)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libraw)
BuildRequires:  pkgconfig(OpenColorIO)
BuildRequires:  pkgconfig(OpenEXR)
BuildRequires:  pkgconfig(poppler-qt5)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(xi)
BuildRequires:  quazip-qt5-devel
BuildRequires:  zlib-devel

%if 0%{?krita_python}
BuildRequires:  sip
BuildRequires:  python3-sip-devel
BuildRequires:  python3-qt5-devel

Requires: python3-qt5-base
%{?_sip_api:Requires: python3-pyqt5-sip-api(%{_sip_api_major}) >= %{_sip_api}}
%endif

Obsoletes:      calligra-krita < 3.0
Provides:       calligra-krita = %{version}-%{release}

Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%description
Krita is a sketching and painting program.
It was created with the following types of art in mind:
- concept art
- texture or matte painting
- illustrations and comics

%package        libs
Summary:        Shared libraries for %{name}
Obsoletes:      calligra-krita-libs < 3.0
Provides:       calligra-krita-libs = %{version}-%{release}
Requires:       %{name} = %{version}-%{release}
%description    libs
%{summary}.


%prep
%autosetup -p1


%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

%make_build -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

%find_lang %{name} --all-name --with-html


%files -f %{name}.lang
%doc README.md
%license COPYING*
%config(noreplace) %{_sysconfdir}/xdg/kritarc
%{_kf5_bindir}/krita
%{_kf5_libdir}/kritaplugins/
%{_kf5_metainfodir}/org.kde.krita.appdata.xml
%{_kf5_datadir}/applications/org.kde.krita.desktop
%{_kf5_datadir}/applications/krita*.desktop
%{_kf5_datadir}/color-schemes/*
%{_kf5_datadir}/color/icc/*
%{_kf5_datadir}/icons/hicolor/*/*/*
%{_kf5_datadir}/krita/
%{_kf5_datadir}/kritaplugins/
# fixme:  /org/krita -> /org/kde/krita ?
%{_kf5_qmldir}/org/krita/
%if 0%{?krita_python}
%{_kf5_bindir}/kritarunner
%{_kf5_libdir}/krita-python-libs/
%endif

%ldconfig_scriptlets libs

%files libs
%{_kf5_libdir}/libkrita*.so.*
# FIXME: exclude (only) lib*.so symlinks
%{_kf5_libdir}/libkrita*.so


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 4.2.9-4
- Rebuilt for Python 3.9

* Mon May 11 2020 Gwyn Ciesla <gwync@protonmail.com> - 4.2.9-3
- Rebuild for new LibRaw

* Mon Mar 30 2020 Rex Dieter <rdieter@fedoraproject.org> - 4.2.9-2
- drop _legacy_common_support FTBFS workaround

* Mon Mar 23 2020 Rex Dieter <rdieter@fedoraproject.org> - 4.2.9-1
- 4.2.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Marek Kasik <mkasik@redhat.com> - 4.2.8.2-2
- Rebuild for poppler-0.84.0

* Sat Nov 30 2019 Rex Dieter <rdieter@fedoraproject.org> - 4.2.8.2-1
- 4.2.8.2

* Fri Oct 18 2019 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 4.2.6-2
- Restore python support (#1735972)

* Wed Sep 11 2019 Rex Dieter <rdieter@fedoraproject.org> 4.2.6-1
- 4.2.6

* Wed Aug 21 2019 Rex Dieter <rdieter@fedoraproject.org> - 4.2.5-5
- disable python support on f32+ until FTBFS issues are sorted out

* Wed Aug 21 2019 Miro Hrončok <mhroncok@redhat.com> - 4.2.5-4
- Rebuilt for Python 3.8

* Tue Aug 20 2019 Susi Lehtola <jussilehtola@fedoraproject.org> - 4.2.5-3
- Rebuilt for GSL 2.6.

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 4.2.5-2
- Rebuilt for Python 3.8

* Sat Aug 17 2019 Rex Dieter <rdieter@fedoraproject.org> - 4.2.5-1
- 4.2.5

* Tue Aug 13 2019 Rex Dieter <rdieter@fedoraproject.org> - 4.2.3-1
- 4.2.3

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 01 2019 Rex Dieter <rdieter@fedoraproject.org> - 4.2.2-1
- 4.2.2

* Tue Jun 04 2019 Rex Dieter <rdieter@fedoraproject.org> - 4.2.1-1
- 4.2.1

* Sun May 12 2019 Rex Dieter <rdieter@fedoraproject.org> - 4.1.8-5
- add PyQt5-related runtime dep(s)

* Sat May 11 2019 Rex Dieter <rdieter@fedoraproject.org> 4.1.8-4
- enable python support

* Thu Apr 11 2019 Richard Shaw <hobbes1069@gmail.com> - 4.1.8-3
- Rebuild for OpenEXR 2.3.0.

* Thu Apr 04 2019 Richard Shaw <hobbes1069@gmail.com> - 4.1.8-2
- Rebuild for OpenColorIO 1.1.1.

* Wed Mar 06 2019 Rex Dieter <rdieter@fedoraproject.org> - 4.1.8-1
- 4.1.8

* Thu Jan 31 2019 Kalev Lember <klember@redhat.com> - 4.1.7-6
- Rebuilt for Boost 1.69

* Wed Jan 30 2019 Rex Dieter <rdieter@fedoraproject.org> - 4.1.7-5
- rebuild (exiv2)

* Fri Jan 25 2019 Jonathan Wakely <jwakely@redhat.com> - 4.1.7-4
- Rebuilt for Boost 1.69

* Tue Jan 15 2019 Rex Dieter <rdieter@fedoraproject.org> - 4.1.7-3
- rebuild

* Mon Dec 17 2018 Rex Dieter <rdieter@fedoraproject.org> - 4.1.7-2
- pull in upstream fixes

* Thu Dec 13 2018 Rex Dieter <rdieter@fedoraproject.org> - 4.1.7-1
- 4.1.7

* Sun Oct 14 2018 Rex Dieter <rdieter@fedoraproject.org> - 4.1.5-1
- 4.1.5

* Tue Aug 28 2018 Rex Dieter <rdieter@fedoraproject.org> - 4.1.1-2
- pull in candidate upstream LibRaw-0.19/FTBFS fix

* Mon Jul 16 2018 Rex Dieter <rdieter@fedoraproject.org> - 4.1.1-1
- krita-4.1.1 (#1601439)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Rex Dieter <rdieter@fedoraproject.org> - 4.1.0-1
- krita-4.1.0 (#1595237)

* Wed Jun 13 2018 Rex Dieter <rdieter@fedoraproject.org> - 4.0.4-1
- krita-4.0.4 (#1590798)

* Sat May 12 2018 Rex Dieter <rdieter@fedoraproject.org> - 4.0.3-1
- krita-4.0.3

* Tue May 08 2018 Rex Dieter <rdieter@fedoraproject.org> - 4.0.2-1
- krita-4.0.2 (#1575789)

* Mon Apr 09 2018 Rex Dieter <rdieter@fedoraproject.org> - 4.0.1-1
- krita-4.0.1 (#1557986)

* Fri Mar 23 2018 Marek Kasik <mkasik@redhat.com> - 4.0.0-2
- Rebuild for poppler-0.63.0

* Tue Mar 20 2018 Rex Dieter <rdieter@fedoraproject.org> - 4.0.0-1
- krita-4.0.0 (#1557986)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 26 2018 Rex Dieter <rdieter@fedoraproject.org> - 3.3.3-1
- krita-3.3.3 (#1532426)

* Tue Jan 23 2018 Jonathan Wakely <jwakely@redhat.com> - 3.3.2.1-4
- Rebuilt for Boost 1.66

* Sat Jan 13 2018 Richard Shaw <hobbes1069@gmail.com> - 3.3.2.1-3
- Rebuild for OpenColorIO 1.1.0.

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.3.2.1-2
- Remove obsolete scriptlets

* Thu Nov 02 2017 Rex Dieter <rdieter@fedoraproject.org> - 3.3.2.1-1
- krita-3.3.2.1

* Wed Oct 11 2017 Rex Dieter <rdieter@fedoraproject.org> - 3.3.1-1
- krita-3.3.1

* Mon Sep 25 2017 Rex Dieter <rdieter@fedoraproject.org> - 3.3.0-1
- krita-3.3.0

* Fri Aug 25 2017 Rex Dieter <rdieter@fedoraproject.org> - 3.2.1-1
- krita-3.2.1

* Wed Aug 16 2017 Rex Dieter <rdieter@fedoraproject.org> - 3.2.0-1
- krita-3.2.0, clean/update build deps

* Mon Jul 31 2017 Rex Dieter <rdieter@fedoraproject.org> - 3.1.4-6
- rebuild (gsl)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Jonathan Wakely <jwakely@redhat.com> - 3.1.4-4
- Rebuilt for s390x binutils bug

* Tue Jul 18 2017 Jonathan Wakely <jwakely@redhat.com> - 3.1.4-3
- Rebuilt for Boost 1.64

* Fri May 26 2017 Rex Dieter <rdieter@fedoraproject.org> - 3.1.4-2
- backport Qt 5.9 FTBFS fix, more robust %%find_lang usage

* Fri May 26 2017 Rex Dieter <rdieter@fedoraproject.org> - 3.1.4-1
- 3.1.4 (#1448598)

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Tue May 02 2017 Rex Dieter <rdieter@fedoraproject.org> - 3.1.2.1-2
- rebuild (exiv2)

* Mon Mar 20 2017 Rex Dieter <rdieter@fedoraproject.org> - 3.1.2.1-1
- krita-3.1.2.1

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 29 2016 Rich Mattes <richmattes@gmail.com> - 3.1.1-3
- Rebuild for eigen3-3.3.1

* Wed Dec 28 2016 Jon Ciesla <limburgher@gmail.com> - 3.1.1-2
- Rebuild for new LibRaw.

* Mon Dec 19 2016 Helio Chissini de Castro <helio@kde.org> - 3.1.1-1
- New upstream version

* Sun Oct 09 2016 Rex Dieter <rdieter@fedoraproject.org> - 3.0.1-1
- 3.0.1

* Sun Oct 09 2016 Rex Dieter <rdieter@fedoraproject.org> - 3.0-4
- -libs: fix Obsoletes, drop %%exclude

* Thu Jun 02 2016 Than Ngo <than@redhat.com> - 3.0-3
- rebuild against new kf5 (workaround for the build failure on arm with gcc6 bz#1342095)

* Tue May 31 2016 Helio Chissini de Castro <helio@kde.org> - 3.0-2
- Fixed requested changes to package reviewing
- Added official tarball.

* Mon May 30 2016 Helio Chissini de Castro <helio@kde.org> - 3.0-1
- Krita 3.0 upstream release

* Tue May 24 2016 Helio Chissini de Castro <helio@kde.org> - 2.99.91-1
- New upstream devel release
- Krita sketch gone

* Mon May 09 2016 Helio Chissini de Castro <helio@kde.org> - 2.99.90-1
- Initial new Krita package

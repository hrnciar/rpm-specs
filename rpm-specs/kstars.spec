%undefine __cmake_in_source_build

Name:    kstars
Summary: Desktop Planetarium
Version: 3.4.3
Release: 5%{?dist}

# We have to use epoch now, KStars is no longer part of KDE Applications and
# uses its own (lower) version now
# https://community.kde.org/Applications/17.12_Release_Notes#Tarballs_that_we_do_not_ship_anymore
Epoch:   1

License: GPLv2+
URL:     http://edu.kde.org/kstars

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0: http://download.kde.org/%{stable}/%{name}/%{name}-%{version}.tar.xz

## upstream patches

## upstreamable patches

## Fedora specific patches
Patch101: kstars-2.9.6-fix-compilerflag-exceptions.patch

BuildRequires: desktop-file-utils
BuildRequires: extra-cmake-modules
BuildRequires: gettext
BuildRequires: kf5-karchive-devel
BuildRequires: kf5-kbookmarks-devel
BuildRequires: kf5-kcodecs-devel
BuildRequires: kf5-kcompletion-devel
BuildRequires: kf5-kconfig-devel
BuildRequires: kf5-kconfigwidgets-devel
BuildRequires: kf5-kcoreaddons-devel
BuildRequires: kf5-kcrash-devel
BuildRequires: kf5-kdbusaddons-devel
BuildRequires: kf5-kdeclarative-devel
BuildRequires: kf5-kdnssd-devel
BuildRequires: kf5-kdoctools-devel
BuildRequires: kf5-kglobalaccel-devel
BuildRequires: kf5-kguiaddons-devel
BuildRequires: kf5-khtml-devel
BuildRequires: kf5-ki18n-devel
BuildRequires: kf5-kiconthemes-devel
BuildRequires: kf5-kinit-devel >= 5.10.0-3
BuildRequires: kf5-kio-devel
BuildRequires: kf5-kitemviews-devel
BuildRequires: kf5-kjobwidgets-devel
BuildRequires: kf5-knewstuff-devel
BuildRequires: kf5-knotifications-devel
BuildRequires: kf5-knotifyconfig-devel
BuildRequires: kf5-kplotting-devel
BuildRequires: kf5-kservice-devel
BuildRequires: kf5-ktexteditor-devel
BuildRequires: kf5-ktextwidgets-devel
BuildRequires: kf5-kwidgetsaddons-devel
BuildRequires: kf5-kwindowsystem-devel
BuildRequires: kf5-kxmlgui-devel
BuildRequires: kf5-rpm-macros
BuildRequires: libappstream-glib
BuildRequires: libnova-devel
BuildRequires: LibRaw-devel
BuildRequires: pkgconfig(cfitsio)
BuildRequires: pkgconfig(eigen3)
BuildRequires: pkgconfig(gsl)
BuildRequires: pkgconfig(Qt5Gui) pkgconfig(Qt5Qml) pkgconfig(Qt5Quick) pkgconfig(Qt5Xml) pkgconfig(Qt5Sql) 
BuildRequires: pkgconfig(Qt5Svg) pkgconfig(Qt5OpenGL) pkgconfig(Qt5Multimedia) pkgconfig(Qt5Test)
BuildRequires: pkgconfig(Qt5DataVisualization)
BuildRequires: pkgconfig(Qt5WebSockets)
BuildRequires: qtkeychain-qt5-devel
BuildRequires: pkgconfig(wcslib)
BuildRequires: zlib-devel
BuildRequires: pkgconfig(libindi) >= 1.5.0
%if 0%{?fedora}
BuildRequires: xplanet
%endif

%{?kf5_kinit_requires}

# Require libindi to enable Ekos properly
Requires:  libindi 
# astrometry is useful for astrophotography with KStars, not required for
# usage as planetarium
Suggests:  astrometry
#  https://bugzilla.redhat.com/show_bug.cgi?id=1557673
Requires:  qt5-qtquickcontrols%{?_isa}
%if 0%{?fedora}
Requires:  xplanet
%endif


# when split occurred
Obsoletes: kdeedu-kstars < 4.7.0-10
Obsoletes: kdeedu-kstars-libs < 4.7.0-10
Provides:  kdeedu-kstars = %{epoch}:%{version}-%{release}

%description
KStars is a Desktop Planetarium.  It provides an accurate graphical
simulation of the night sky, from any location on Earth, at any date and
time.  The display includes up to 100 million stars, 13,000 deep-sky objects,
all 8 planets, the Sun and Moon, and thousands of comets and asteroids.


%prep
%setup -q

%patch101 -p1 -b .fix_cflag_exception

%build
%{cmake_kf5}
%cmake_build


%install
%cmake_install

%find_lang %{name} --all-name --with-html

## unpackaged files
rm -fv %{buildroot}%{_kf5_libdir}/libhtmesh.a


%check
# primarily care about validation on fedora only
# (ie, generally, if fedora is ok, then so is epel7)
%if 0%{?fedora}
appstream-util validate-relax --nonet %{buildroot}%{_kf5_metainfodir}/org.kde.kstars.appdata.xml
%endif
desktop-file-validate %{buildroot}%{_kf5_datadir}/applications/org.kde.kstars.desktop


%if 0%{?rhel} && 0%{?rhel} < 8
%post
touch --no-create %{_kf5_datadir}/icons/hicolor  &> /dev/null || :

%posttrans
gtk-update-icon-cache %{_kf5_datadir}/icons/hicolor &> /dev/null || :

%postun
if [ $1 -eq 0 ] ; then
touch --no-create %{_kf5_datadir}/icons/hicolor &> /dev/null || :
gtk-update-icon-cache %{_kf5_datadir}/icons/hicolor &> /dev/null || :
fi
%endif

%files -f %{name}.lang
%license COPYING COPYING.DOC
%doc AUTHORS ChangeLog README.* TODO
%{_kf5_bindir}/kstars
%{_kf5_metainfodir}/org.kde.kstars.appdata.xml
%{_kf5_datadir}/applications/org.kde.kstars.desktop
%{_kf5_datadir}/config.kcfg/kstars.kcfg
%{_kf5_datadir}/knotifications5/kstars.notifyrc
%{_kf5_datadir}/sounds/KDE-KStars-*
%{_kf5_datadir}/kstars/
%{_kf5_datadir}/icons/hicolor/*/*/*


%changelog
* Thu Oct 01 2020 Jeff Law  <law@redhat.com> - 1:3.4.3-5
- Avoid local symbol binding by forcing application to build with -fPIC
- Re-enable LTO

* Wed Sep 23 2020 Christian Dersch <lupinix@fedoraproject.org> - 1:3.4.3-4
- Build with LTO disabled, fixes #1881915

* Tue Aug 25 2020 Christian Dersch <lupinix@mailbox.org> - 1:3.4.3-3
- Rebuilt for INDI 1.8.6

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 20 2020 Christian Dersch <lupinix@fedoraproject.org> - 1:3.4.3-1
- new version

* Fri Jun 26 2020 Marie Loise Nolden <loise@kde.org> - 1:3.4.2-1
- Update to 3.4.2 with Qt 5.15 support

* Mon May 18 2020 Mattia Verga <mattia.verga@protonmail.com> - 1:3.3.6-5
- Rebuilt for LibRaw 0.20Beta1

* Mon Mar 23 2020 Mattia Verga <mattia.verga@protonmail.com> - 1:3.3.6-4
- Rebuilt for wcslib 7.2

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.3.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 14 2019 Richard Shaw <hobbes1069@gmail.com> - 1:3.3.6-2
- Rebuilt for qt5-qtdatavis3d 5.13.2.

* Sun Oct 20 2019 Christian Dersch <lupinix@fedoraproject.org> - 1:3.3.6-1
- new version

* Tue Aug 20 2019 Susi Lehtola <jussilehtola@fedoraproject.org> - 1:3.2.1-3
- Rebuilt for GSL 2.6.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Apr 28 2019 Christian Dersch <lupinix@mailbox.org> - 1:3.2.1-1
- new version

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.9.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Aug 18 2018 Christian Dersch <lupinix.fedora@gmail.com> - 1:2.9.8-1
- new version
- drop patch for KDE #397010 (fixed upstream)

* Tue Jul 31 2018 Christian Dersch <lupinix.fedora@gmail.com> - 1:2.9.7-3
- Add patch to fix KDE #397010

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 1:2.9.7-2
- Rebuild with fixed binutils

* Sun Jul 29 2018 Christian Dersch <lupinix@mailbox.org> - 1:2.9.7-1
- new version

* Thu Jul 19 2018 Christian Dersch <lupinix@fedoraproject.org> - 1:2.9.6-3
- Rebuilt for LibRaw soname bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.9.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat May 26 2018 Christian Dersch <lupinix@mailbox.org> - 1:2.9.6-1
- new version

* Sun Mar 18 2018 Rex Dieter <rdieter@fedoraproject.org> - 1:2.9.3-2
- Requires: qt5-qtquickcontrols (#1557673)
- .spec cosmetics: use %%make_build, omit deprecated scriptlets

* Wed Feb 28 2018 Christian Dersch <lupinix@mailbox.org> - 1:2.9.3-1
- new version

* Fri Feb 23 2018 Christian Dersch <lupinix@mailbox.org> - 1:2.9.2-3
- rebuilt for cfitsio 3.420 (so version bump)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 30 2018 Christian Dersch <lupinix@mailbox.org> - 1:2.9.2-1
- new version

* Wed Jan 10 2018 Christian Dersch <lupinix@mailbox.org> - 1:2.9.1-1
- update to 2.9.1
- rebased kstars-2.9.1-make_libindi_required.patch

* Mon Jan 08 2018 Christian Dersch <lupinix@mailbox.org> - 1:2.8.9-3
- rebuilt (libindi-1.6.2)

* Tue Jan 02 2018 Christian Dersch <lupinix@fedoraproject.org> - 1:2.8.9-2
- rebuild (libindi-1.6.0)

* Sat Dec 16 2017 Christian Dersch <lupinix@mailbox.org> - 1:2.8.9-1
- update to 2.8.9
- removed kstars-2.8.8-remove_duplicate_file.patch (applied upstream)

* Fri Dec 15 2017 Christian Dersch <lupinix@mailbox.org> - 1:2.8.8-1
- update to 2.8.8
- KStars has been split out from KDE Applications, using own versioning now
- https://community.kde.org/Applications/17.12_Release_Notes#Tarballs_that_we_do_not_ship_anymore
- rebased kstars-2.8.8-make_libindi_required.patch
- added patch kstars-2.8.8-cmake_cmp0071.patch for new cmake policy
- added kstars-2.8.8-remove_duplicate_file.patch (upstream fix)

* Wed Nov 08 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.08.3-1
- 17.08.3

* Thu Oct 12 2017 Christian Dersch - 17.08.2-2
- Require libindi on runtime

* Wed Oct 11 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.08.2-1
- 17.08.2

* Sat Oct 07 2017 Christian Dersch <lupinix@mailbox.org> - 17.08.1-3
- rebuilt for libindi 1.5.0

* Wed Oct 04 2017 Christian Dersch <lupinix@mailbox.org> - 17.08.1-2
- Added Suggests: astrometry, useful for astrophotography with KStars

* Wed Sep 06 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.08.1-1
- 17.08.1

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 16.12.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 16.12.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 16.12.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Thu Mar 09 2017 Rex Dieter <rdieter@fedoraproject.org> - 16.12.3-1
- 16.12.3

* Mon Feb 27 2017 Christian Dersch <lupinix@mailbox.org> - 16.12.2-4
- rebuilt

* Sun Feb 26 2017 Christian Dersch <lupinix@mailbox.org> - 16.12.2-3
- rebuilt for libindi-1.4.0, including patches for proper detection

* Sun Feb 26 2017 Christian Dersch <lupinix@mailbox.org> - 16.12.2-2
- rebuilt for libindi-1.4.0

* Thu Feb 09 2017 Rex Dieter <rdieter@fedoraproject.org> - 16.12.2-1
- 16.12.2

* Wed Jan 11 2017 Rex Dieter <rdieter@fedoraproject.org> - 16.12.1-1
- 16.12.1

* Wed Dec 28 2016 Rich Mattes <richmattes@gmail.com> - 16.12.0-3
- Rebuild for eigen3-3.3.1

* Wed Dec 28 2016 Jon Ciesla <limburgher@gmail.com> - 16.12.0-2
- Rebuild for new LibRaw.

* Thu Dec 15 2016 Christian Dersch <lupinix@mailbox.org> - 16.12.0-1
- new version

* Thu Dec 15 2016 Christian Dersch <lupinix@mailbox.org> - 16.08.3-2
- Rebuild for libindi 1.3.1

* Mon Dec 05 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.08.3-1
- 16.08.3

* Thu Oct 13 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.08.2-1
- 16.08.2

* Wed Sep 07 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.08.1-1
- 16.08.1

* Fri Aug 12 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.08.0-1
- 16.08.0

* Sat Aug 06 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.07.90-1
- 16.07.90

* Sat Jul 30 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.07.80-1
- 16.07.80

* Sat Jul 09 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.04.3-1
- 16.04.3

* Sun Jun 12 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.04.2-1
- 16.04.2

* Sun May 08 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.04.1-1
- 16.04.1

* Sat May 07 2016 Christian Dersch <lupinix@mailbox.org> - 16.04.0-3
- libindi is also available at epel7

* Sat Apr 23 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.04.0-2
- rebuild (wcslib)

* Fri Apr 22 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.04.0-1
- 16.04.0

* Thu Mar 31 2016 Christian Dersch <lupinix@mailbox.org> - 15.12.3-2
- Rebuilt for wcslib 5.14

* Tue Mar 15 2016 Rex Dieter <rdieter@fedoraproject.org> - 15.12.3-1
- 15.12.3

* Fri Feb 19 2016 Christian Dersch <lupinix@mailbox.org> - 15.12.2-2
- Added patch to make libindi a hard requirement

* Sun Feb 14 2016 Rex Dieter <rdieter@fedoraproject.org> - 15.12.2-1
- 15.12.2

* Tue Feb 02 2016 Christian Dersch <lupinix@mailbox.org> - 15.12.1-2
- Rebuild for libindi 1.2.0
- Added patch kstars-15.12.1-fix-gcc6-stdnamespace.patch (fix build with gcc6) 

* Mon Jan 25 2016 Rex Dieter <rdieter@fedoraproject.org> - 15.12.1-1
- 15.12.1

* Mon Dec 28 2015 Rex Dieter <rdieter@fedoraproject.org> 15.12.0-1
- 15.12.0

* Mon Nov 30 2015 Rex Dieter <rdieter@fedoraproject.org> - 15.08.3-1
- 15.08.3

* Mon Sep 07 2015 Christian Dersch <lupinix@fedoraproject.org> - 15.08.0-2
- rebuilt against libindi 1.1.0

* Thu Aug 20 2015 Than Ngo <than@redhat.com> - 15.08.0-1
- 15.08.0

* Mon Jun 29 2015 Rex Dieter <rdieter@fedoraproject.org> 15.04.3-1
- 15.04.3

* Mon Jun 29 2015 Rex Dieter <rdieter@fedoraproject.org> - 15.04.2-4
- pull in upstream fix for 348880 - Ekos doesn't save images with Index > 100 (kde#348880)
- fix appdata id tag

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 15.04.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Christian Dersch <lupinix@fedoraproject.org> - 15.04.2-2
- added patch to fix https://bugs.kde.org/show_bug.cgi?id=348880

* Thu Jun 04 2015 Rex Dieter <rdieter@fedoraproject.org> 15.04.2-1
- 15.04.2, fix appdata

* Mon Jun 01 2015 Rex Dieter <rdieter@fedoraproject.org> 15.04.1-3
- %%{?kf5_kinit_requires}

* Mon Jun 01 2015 Christian Dersch <chrisdersch@gmail.com> - 15.04.1-2
- add kf5-kinit to dependencies (fixes #1226825)

* Thu May 28 2015 Rex Dieter <rdieter@fedoraproject.org> - 15.04.1-1
- 15.04.1

* Tue Apr 14 2015 Rex Dieter <rdieter@fedoraproject.org> - 15.04.0-1
- 15.04.0

* Sun Mar 01 2015 Rex Dieter <rdieter@fedoraproject.org> - 14.12.3-1
- 14.12.3

* Wed Feb 25 2015 Christian Dersch <lupinix@fedoraproject.org> - 14.12.2-2
- disaled libindi support temporarily due to INDI API changes
- libindi will be enabled again soon, when we moved to the KF5 based Kstars

* Tue Feb 24 2015 Than Ngo <than@redhat.com> - 14.12.2-1
- 14.12.2

* Sat Jan 17 2015 Rex Dieter <rdieter@fedoraproject.org> - 14.12.1-1
- 14.12.1

* Mon Dec 01 2014 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.14.3-1.2
- BR pkgconfig(libindi) >= 0.9.8 (#1168104)

* Sun Nov 30 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.14.3-1.1
- Menu item Device missing in kstars (#1168104)

* Sun Nov 09 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.14.3-1
- 4.14.3

* Sun Oct 12 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.14.2-1
- 4.14.2

* Wed Sep 17 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.14.1-1
- 4.14.1

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.13.97-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Aug 11 2014 Rex Dieter <rdieter@fedoraproject.org> 4.13.97-2
- %%check: appstream validation

* Tue Aug 05 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.13.97-1
- 4.13.97

* Fri Jul 18 2014 Rex Dieter <rdieter@fedoraproject.org> 4.13.3-2
- BR: wcslib-devel

* Mon Jul 14 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.13.3-1
- 4.13.3

* Mon Jun 09 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.13.2-1
- 4.13.2

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.13.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Jun 02 2014 Rex Dieter <rdieter@fedoraproject.org> 4.13.1-2
- Requires: pykde4 (#1103853)

* Sun May 11 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.13.1-1
- 4.13.1

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

* Fri Jan 10 2014 Orion Poplawski <orion@cora.nwra.com> - 4.12.0-2
- Rebuild for cfitsio 3.360

* Thu Dec 19 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.12.0-1
- 4.12.0

* Sun Dec 01 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.11.97-1
- 4.11.97

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

* Thu Aug 08 2013 Than Ngo <than@redhat.com> - 4.11.0-1
- 4.11.0

* Thu Jul 25 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.10.97-1
- 4.10.97

* Tue Jul 23 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.10.95-1
- 4.10.95

* Fri Jun 28 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.10.90-1
- 4.10.90

* Sat Jun 01 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.10.4-1
- 4.10.4

* Mon May 06 2013 Than Ngo <than@redhat.com> - 4.10.3-1
- 4.10.3

* Mon Apr 01 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.10.2-1
- 4.10.2

* Fri Mar 22 2013 Rex Dieter <rdieter@fedoraproject.org> 4.10.1-3
- rebuild (cfitsio)

* Wed Mar 20 2013 Rex Dieter <rdieter@fedoraproject.org> 4.10.1-2
- rebuild (cfitsio)

* Sat Mar 02 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.10.1-1
- 4.10.1

* Fri Feb 01 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.10.0-1
- 4.10.0

* Tue Jan 22 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.9.98-1
- 4.9.98

* Fri Jan 04 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.9.97-1
- 4.9.97

* Thu Dec 20 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.9.95-1
- 4.9.95

* Tue Dec 04 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.9.90-1
- 4.9.90

* Mon Dec 03 2012 Than Ngo <than@redhat.com> - 4.9.4-1
- 4.9.4

* Sat Nov 03 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.9.3-1
- 4.9.3

* Sat Sep 29 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.9.2-1
- 4.9.2

* Mon Sep 03 2012 Than Ngo <than@redhat.com> - 4.9.1-1
- 4.9.1

* Thu Jul 26 2012 Lukas Tinkl <ltinkl@redhat.com> - 4.9.0-1
- 4.9.0

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.8.97-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jul 12 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.8.97-1
- 4.8.97

* Thu Jun 28 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.8.95-1
- 4.8.95

* Sun Jun 10 2012 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.8.90-2
- safer glibc TIME_UTC FTBFS patch

* Sun Jun 10 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.8.90-1
- 4.8.90

* Sun Jun 03 2012 Jaroslav Reznik <jreznik@redhat.com> - 4.8.80-1
- 4.8.80

* Mon Apr 30 2012 Jaroslav Reznik <jreznik@redhat.com> - 4.8.3-1
- 4.8.3

* Fri Mar 30 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.8.2-1
- 4.8.2

* Mon Mar 05 2012 Jaroslav Reznik <jreznik@redhat.com> - 4.8.1-1
- 4.8.1

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.8.0-2
- Rebuilt for c++ ABI breakage

* Sun Jan 22 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.8.0-1
- 4.8.0

* Wed Jan 04 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.7.97-1
- 4.7.97

* Thu Dec 22 2011 Radek Novacek <rnovacek@redhat.com> - 4.7.95-1
- 4.7.95

* Sun Dec 04 2011 Rex Dieter <rdieter@fedoraproject.org> - 4.7.90-1
- 4.7.90

* Thu Dec 01 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.80-1
- 4.7.80

* Sat Oct 29 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.3-1
- 4.7.3

* Tue Oct 04 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.2-1
- 4.7.2

* Wed Sep 21 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.1-3
- update URL, %%description

* Tue Sep 20 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.1-2
- %%doc: COPYING README ...
- License: GPLv2

* Sat Sep 17 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.1-1
- 4.7.1

* Tue Aug 30 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.0-10
- first try


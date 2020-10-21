Name: qmapshack
Version: 1.15.0
Release: 3%{?dist}
Summary: GPS mapping and management tool

License: GPLv3+ and BSD
URL: https://bitbucket.org/maproom/qmapshack/wiki/Home
Source0: https://github.com/Maproom/qmapshack/archive/V_%{version}/%{name}-%{version}.tar.gz
# don't rely on proj for cmake config
Patch2: FindPROJ4.patch
Recommends: routino
Recommends: qmaptool

BuildRequires: gcc-c++
%if 0%{?rhel}
BuildRequires: cmake3
%else
BuildRequires: cmake
%endif
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Xml)
BuildRequires: pkgconfig(Qt5Script)
BuildRequires: pkgconfig(Qt5Sql)
BuildRequires: pkgconfig(Qt5WebEngineWidgets)
BuildRequires: pkgconfig(Qt5UiTools)
BuildRequires: qt5-qttools-devel
BuildRequires: proj-devel
BuildRequires: gdal-devel
BuildRequires: zlib-devel
BuildRequires: routino-devel
BuildRequires: alglib-devel
BuildRequires: quazip-qt5-devel
BuildRequires: libjpeg-devel
BuildRequires: desktop-file-utils

# because new dependency on WebEngine
ExclusiveArch: %{qt5_qtwebengine_arches}


%description
QMapShack provides a versatile tool for GPS maps in GeoTiff format as well as
Garmin's img vector map format. You can also view and edit your GPX tracks.
QMapShack is the successor of QLandkarteGT.

Main features:
- use of several work-spaces
- use several maps on a work-space
- handle data project-oriented
- exchange data with the device by drag-n-drop


%package -n qmaptool
Summary: Create raster maps from paper map scans
URL: https://bitbucket.org/maproom/qmaptool/wiki/Home

%description -n qmaptool
This is a tool to create raster maps from paper map scans. QMapTool can be
considered as a front-end to the well-known GDAL package. It complements
QMapShack.


%prep
%setup -q -n %{name}-V_%{version}
%if 0%{?fedora} && 0%{?fedora} < 31
# starting with F-31 we have proj package with the cmake config
%patch2 -p1
%endif


%build
%cmake -DBUILD_SHARED_LIBS:BOOL=OFF
%cmake_build


%install
%cmake_install

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/qmaptool.desktop

%files
%license LICENSE
%doc changelog.txt
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/QMapShack.*
%{_datadir}/pixmaps/QMapShack.png
%{_datadir}/%{name}/
%{_datadir}/doc/HTML/QMSHelp.q??
%{_mandir}/man1/%{name}.*

%files -n qmaptool
%{_bindir}/qmaptool
%{_bindir}/qmt_*
%{_datadir}/applications/qmaptool.desktop
%{_datadir}/icons/hicolor/*/apps/QMapTool.*
%{_datadir}/pixmaps/QMapTool.png
%{_datadir}/qmaptool/
%{_datadir}/qmt_*/
%{_datadir}/doc/HTML/QMTHelp.q??
%{_mandir}/man1/qmaptool.*
%{_mandir}/man1/qmt_*.*


%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 14 2020 Dan Horák <dan@danny.cz> - 1.15.0-1
- update to 1.15.0 (#1751288)

* Thu May 21 2020 Sandro Mani <manisandro@gmail.com> - 1.14.0-4
- Rebuild (gdal)

* Tue Mar 03 2020 Sandro Mani <manisandro@gmail.com> - 1.14.0-3
- Rebuild (gdal)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 26 2019 Dan Horák <dan@danny.cz> - 1.14.0-1
- update to 1.14.0 (#1751288)
- drop support for RHEL <= 7 - no QtWebEngine there

* Wed Jul 24 2019 Dan Horák <dan@danny.cz> - 1.13.1-7
- update to 1.13.1

* Tue May 14 2019 Dan Horák <dan@danny.cz> - 1.13.0-6
- allow build in F<=30

* Tue Apr 16 2019 Dan Horák <dan@danny.cz> - 1.13.0-5
- update to 1.13.0 (#1697564)

* Sat Feb 23 2019 Sandro Mani <manisandro@gmail.com> - 1.12.3-4
- Rebuild (alglib)

* Sat Feb 09 2019 Dan Horák <dan@danny.cz> - 1.12.3-3
- update to 1.12.3 (#1672366)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Dec 22 2018 Dan Horák <dan@danny.cz> - 1.12.1-1
- update to 1.12.1

* Tue Sep 04 2018 Dan Horák <dan@danny.cz> - 1.12.0-1
- update to 1.12.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jul 01 2018 Sandro Mani <manisandro@gmail.com> - 1.11.1-2
- Rebuild (alglib)

* Thu Apr 19 2018 Dan Horák <dan@danny.cz> - 1.11.1-1
- update to 1.11.1 (#1569518)

* Mon Mar 12 2018 Dan Horák <dan@danny.cz> - 1.11.0-1
- update to 1.11.0 (#1551560)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Dec 31 2017 Sandro Mani <manisandro@gmail.com> - 1.10.0-2
- Rebuild (alglib)

* Thu Dec 21 2017 Dan Horák <dan@danny.cz> - 1.10.0-1
- update to 1.10.0 (#1528494)

* Mon Sep 18 2017 Dan Horák <dan@danny.cz> - 1.9.1-1
- update to 1.9.1 (#1492506)

* Thu Aug 24 2017 Sandro Mani <manisandro@gmail.com> - 1.9.0-2
- Rebuild (alglib)

* Wed Aug 02 2017 Dan Horák <dan@danny.cz> - 1.9.0-1
- update to 1.9.0 (#1474557)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Dan Horák <dan@danny.cz> - 1.8.1-1
- update to 1.8.1 (#1450653)

* Fri May 12 2017 Sandro Mani <manisandro@gmail.com> - 1.8.0-2
- Rebuild (alglib)

* Mon Mar 27 2017 Dan Horák <dan@danny.cz> - 1.8.0-1
- update to 1.8.0

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 31 2017 Dan Horák <dan@danny.cz> - 1.7.2-2
- Rebuilt for proj 4.9.3

* Tue Dec 13 2016 Dan Horák <dan[at]danny.cz> - 1.7.2-1
- update to 1.7.2

* Tue Sep 13 2016 Dan Horák <dan[at]danny.cz> - 1.7.1-1
- update to 1.7.1

* Tue Sep 13 2016 Dan Horák <dan[at]danny.cz> - 1.7.0-1
- update to 1.7.0

* Thu Jul 14 2016 Dan Horák <dan[at]danny.cz> - 1.6.3-1
- update to 1.6.3

* Mon Jul 04 2016 Dan Horák <dan[at]danny.cz> - 1.6.2-1
- update to 1.6.2

* Mon Mar 28 2016 Dan Horák <dan[at]danny.cz> - 1.6.1-1
- update to 1.6.1

* Fri Feb 26 2016 Dan Horák <dan[at]danny.cz> - 1.6.0-1
- update to 1.6.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Nov 22 2015 Dan Horák <dan[at]danny.cz> - 1.5.1-1
- update to 1.5.1

* Thu Nov 12 2015 Dan Horák <dan[at]danny.cz> - 1.4.0-1
- update to 1.4.0

* Mon Jul 27 2015 Dan Horák <dan@danny.cz> - 1.3.0-2
- rebuild for GDAL 2.0

* Thu Jul 02 2015 Dan Horák <dan[at]danny.cz> - 1.3.0-1
- update to 1.3.0

* Wed Jun 24 2015 Dan Horák <dan[at]danny.cz> - 1.2.2-1
- update to 1.2.2
- add missing desktop-database scriptlets
- fix license tag

* Tue Apr 14 2015 Dan Horák <dan[at]danny.cz> - 1.2.0-1
- update to 1.2.0

* Sun Apr 05 2015 Dan Horák <dan[at]danny.cz> - 1.1.0-1
- initial Fedora version

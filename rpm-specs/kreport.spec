%undefine __cmake_in_source_build

# uncomment to enable bootstrap mode
#global bootstrap 1

%if !0%{?bootstrap}
# some known failures, ping upstream
#global tests 1
%endif

Name:    kreport
Summary: Framework for creation and generation of reports
Version: 3.2.0
Release: 3%{?dist}

License: LGPLv2+

Url:     https://community.kde.org/KReport
Source0: http://download.kde.org/stable/%{name}/src/%{name}-%{version}.tar.xz

## upstreamable patches
# fix/sanitize pkgconfig deps
Patch100: kreport-3.0.2-pkgconfig.patch

BuildRequires: gcc-c++

BuildRequires: extra-cmake-modules
BuildRequires: kf5-rpm-macros
BuildRequires: cmake(Qt5PrintSupport)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(Qt5Xml)
BuildRequires: cmake(Qt5Qml)

BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5WidgetsAddons)
BuildRequires: cmake(KF5GuiAddons)
BuildRequires: cmake(KF5Config)

BuildRequires: cmake(KPropertyWidgets) >= %{version}
BuildRequires: kproperty-devel >= %{version}
Requires:      kproperty%{?_isa} >= %{version}
# default python interpreter (ie, /usr/bin/python)
BuildRequires: python3

# autodeps
BuildRequires: cmake
BuildRequires: pkgconfig

# plugins
BuildRequires: cmake(Marble)
BuildRequires: cmake(Qt5WebKitWidgets)

%if 0%{?tests}
BuildRequires: cmake(Qt5Test)
BuildRequires: xorg-x11-server-Xvfb
%endif

%description
A framework for creation and generation of reports in multiple formats.

%package devel
Summary: Developer files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: cmake(KPropertyWidgets) >= %{version}
Requires: cmake(KF5CoreAddons)
Requires: cmake(KF5WidgetsAddons)
Requires: cmake(KF5GuiAddons)
%description devel
%{summary}.


%prep
%autosetup -p1


%build
%{cmake_kf5} \
  -DBUILD_TESTING:BOOL=%{?tests:ON}%{?!tests:OFF} \
  -DPYTHON_EXECUTABLE:PATH="%{__python3}"
%cmake_build


%install
%cmake_install

%find_lang_kf5 kreport_barcodeplugin_qt
%find_lang_kf5 kreport_mapsplugin_qt
%find_lang_kf5 kreport_qt
%find_lang_kf5 kreport_webplugin_qt
cat *_qt.lang > all.lang


%check
## tests have known failures, TODO: consult upstream
%if 0%{?tests}
export CTEST_OUTPUT_ON_FAILURE=1
#xvfb-run -a \
make test ARGS="--output-on-failure --timeout 20" -C %{_target_platform} ||:
%endif


%ldconfig_scriptlets

%files -f all.lang
%license COPYING.LIB
%{_libdir}/libKReport3.so.4*
%dir %{_qt5_plugindir}/kreport3/
# TODO: consider splitting some into subpkgs (maps/marble in particular)
%{_qt5_plugindir}/kreport3/org.kde.kreport.barcode.so
%{_qt5_plugindir}/kreport3/org.kde.kreport.maps.so
%{_qt5_plugindir}/kreport3/org.kde.kreport.web.so
%{_kf5_datadir}/kservicetypes5/kreport_elementplugin.desktop
# .rcc icon resources
%{_datadir}/kreport3/

%files devel
%{_includedir}/KReport3/
%{_libdir}/libKReport3.so
%{_libdir}/cmake/KReport3/
%{_libdir}/pkgconfig/KReport3.pc
%{_kf5_archdatadir}/mkspecs/modules/qt_KReport3.pri


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 22 2020 Rex Dieter <rdieter@fedoraproject.org> - 3.2.0-2
- BR: python3

* Mon Feb 03 2020 Rex Dieter <rdieter@fedoraproject.org> - 3.2.0-1
- 3.2.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 15 2018 Iryna Shcherbina <ishcherb@redhat.com> - 3.1.0-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Sun Mar 11 2018 Rex Dieter <rdieter@fedoraproject.org> - 3.1.0-1
- 3.1.0

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.94-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 22 2018 Rex Dieter <rdieter@fedoraproject.org> - 3.0.94-1
- 3.0.94

* Thu Jan 18 2018 Rex Dieter <rdieter@fedoraproject.org> - 3.0.2-6
- rebuild (marble)

* Wed Sep 13 2017 Rex Dieter <rdieter@fedoraproject.org> - 3.0.2-5
- rebuild (marble)

* Fri Aug 18 2017 Rex Dieter <rdieter@fedoraproject.org> - 3.0.2-4
- move rcc icon resource to main/runtime pkg, runtime complains if missing

* Sat Aug 12 2017 Rex Dieter <rdieter@fedoraproject.org> - 3.0.2-3
- add/tighten dep on kproperty

* Fri Aug 11 2017 Rex Dieter <rdieter@fedoraproject.org> - 3.0.2-2
- fix/sanitize pkgconfig deps

* Fri Aug 11 2017 Rex Dieter <rdieter@fedoraproject.org> - 3.0.2-1
- 3.0.2

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Apr 12 2017 Rex Dieter <rdieter@fedoraproject.org> - 3.0.1-0.1
- first try

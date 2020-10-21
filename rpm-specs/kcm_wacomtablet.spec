%undefine __cmake_in_source_build

Name:    kcm_wacomtablet
Summary: KDE Control module for Wacom Graphictablets
Version: 3.2.0
Release: 2%{?dist}

License: GPLv2+
# mirror
URL:     https://github.com/KDE/wacomtablet
Source0: https://download.kde.org/stable/wacomtablet/%{version}/wacomtablet-%{version}.tar.xz

## upstream patches
Patch24: 0024-Fix-build-with-Qt-5.15.patch
# fix for Qt 5.15 but breaks building against older Qt
#Patch35: 0035-Fix-Qt-5.15-obsoletions.patch

BuildRequires: extra-cmake-modules
BuildRequires: kf5-ki18n-devel
BuildRequires: kf5-kdbusaddons-devel
BuildRequires: kf5-kdoctools-devel
BuildRequires: kf5-kglobalaccel-devel
BuildRequires: kf5-knotifications-devel
BuildRequires: kf5-kwidgetsaddons-devel
BuildRequires: kf5-kwindowsystem-devel
BuildRequires: kf5-kxmlgui-devel
BuildRequires: kf5-plasma-devel
BuildRequires: kf5-rpm-macros

BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtdeclarative-devel
BuildRequires: qt5-qtx11extras-devel

BuildRequires: pkgconfig(libwacom)
BuildRequires: pkgconfig(xcb-xinput)
BuildRequires: pkgconfig(xi)
BuildRequires: pkgconfig(xorg-wacom)
BuildRequires: pkgconfig(xrandr)

ExcludeArch: s390 s390x

Obsoletes: kcm-wacomtablet < 1.3.7-2
Provides:  kcm-wacomtablet = %{version}-%{release}

%description
This module implements a GUI for the Wacom Linux Drivers and extends it
with profile support to handle different button/pen layouts per profile.


%prep
%autosetup -p1 -n wacomtablet-%{version}


%build
%cmake_kf5

%cmake_build


%install
%cmake_install

%find_lang %{name} --all-name --with-html


%files -f %{name}.lang
%doc AUTHORS
%license COPYING*
%{_datadir}/dbus-1/interfaces/org.kde.Wacom*.xml
%{_kf5_sysconfdir}/xdg/wacomtablet.*
%{_kf5_bindir}/kde_wacom_tabletfinder
%{_kf5_datadir}/applications/kde_wacom_tabletfinder.desktop
%{_kf5_datadir}/kservices5/kcm_wacomtablet.desktop
%{_kf5_datadir}/kservices5/plasma-applet-org.kde.plasma.wacomtablet.desktop
%{_kf5_datadir}/kservices5/plasma-dataengine-wacomtablet.desktop
%{_kf5_datadir}/knotifications5/wacomtablet.notifyrc
%{_kf5_datadir}/plasma/plasmoids/org.kde.plasma.wacomtablet/
%{_kf5_datadir}/plasma/services/wacomtablet.operations
%{_kf5_datadir}/wacomtablet/
%{_kf5_metainfodir}/org.kde.plasma.wacomtablet.appdata.xml
%{_kf5_metainfodir}/org.kde.wacomtablet.metainfo.xml
%{_qt5_plugindir}/kcm_wacomtablet.so
%{_kf5_plugindir}/kded/wacomtablet.so
%{_qt5_plugindir}/plasma/dataengine/plasma_engine_wacomtablet.so


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 21 2020 Rex Dieter <rdieter@fedoraproject.org> - 3.2.0-1
- 3.2.0, pull in Qt 5.15 fix

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Apr 28 2019 Rex Dieter <rdieter@fedoraproject.org> - 3.1.1-2
- update deps, fix/workaround FindX11.cmake issue

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Dec 21 2018 Rex Dieter <rdieter@fedoraproject.org> - 3.1.1-1
- 3.1.1

* Sun Sep 02 2018 Rex Dieter <rdieter@fedoraproject.org> - 3.1.0-1
- 3.1.0 (#1624665)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-0.7.beta2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-0.6.beta2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Dec 29 2017 Rex Dieter <rdieter@fedoraproject.org> - 3.0.0-0.5.beta2
- 3.0.0-beta2 (aka 2.9.82), +translations

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-0.4.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-0.3.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-0.2.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Feb 16 2016 Rex Dieter <rdieter@fedoraproject.org> 3.0.0-0.1.beta1
- 3.0.0-beta1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3.20150702gitg8ad842e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Sep 02 2015 Jason L Tibbitts III <tibbs@math.uh.edu> - 2.1.0-2.20150702gitg8ad842e
- New snapshot.

* Thu Jul 02 2015 Jason L Tibbitts III <tibbs@math.uh.edu> - 2.1.0-1.20150702gitde80d02
- Update to latest kf5-port HEAD.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-0.3.20141123.ede16d1git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed May 27 2015 Rex Dieter <rdieter@fedoraproject.org> 2.1.0-0.2.20141123.ede16d1git
- 2.1.0 20141123 snapshot

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.0.2-2
- Rebuilt for GCC 5 C++11 ABI change

* Wed Oct 15 2014 Rex Dieter <rdieter@fedoraproject.org> 2.0.2-1
- 2.0.2

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 28 2014 Rex Dieter <rdieter@fedoraproject.org>  2.0.1-1
- kcm_wacomtablet-2.0.1 (#1114238)

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Dec 05 2012 Dan Horák <dan[at]danny.cz> - 1.3.7-3
- no wacom on s390(x)

* Thu Nov 29 2012 Mario Santagiuliana <fedora@marionline.it> - 1.3.7-2
- Rename to kcm_wacomtablet

* Mon Nov 19 2012 Mario Santagiuliana <fedora@marionline.it> - 1.3.7-1
- Initial build
- spec file created by rdieter

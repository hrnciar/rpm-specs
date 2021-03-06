%global repo dde-kwin

Name:           deepin-kwin
Version:        0.1.0
Release:        10%{?dist}
Summary:        KWin configuration for Deepin Desktop Environment
License:        GPLv3+
URL:            https://github.com/linuxdeepin/%{repo}
Source0:        %{url}/archive/%{version}/%{repo}-%{version}.tar.gz
# https://git.archlinux.org/svntogit/community.git/commit/trunk?h=packages/deepin-kwin&id=aac44be15651bbaa2d4f7d100ecd9dbc4a79236a
# Fix runtime issue with kwin 5.17
Patch0:         kwin-5.17.patch
Patch1:         https://github.com/linuxdeepin/dde-kwin/pull/106.patch
Patch2:         deepin-kwin-fix-build-qt-5.15.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  kwin-devel
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  gsettings-qt-devel
BuildRequires:  libepoxy-devel
BuildRequires:  dtkcore-devel
BuildRequires:  kf5-kwayland-devel
BuildRequires:  kf5-kglobalaccel-devel
BuildRequires:  cmake(KDecoration2)
BuildRequires:  qt5-linguist
# for libQt5EdidSupport.a
BuildRequires:  qt5-qtbase-static
BuildRequires:  qt5-qtbase-private-devel
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}
Requires:       deepin-qt5integration%{?_isa}
Requires:       kwin%{?_isa} >= 5.17
# since F31
Obsoletes:      deepin-wm <= 1.9.38
Obsoletes:      deepin-wm-switcher <= 1.1.9
Obsoletes:      deepin-metacity <= 3.22.24
Obsoletes:      deepin-metacity-devel <= 3.22.24
Obsoletes:      deepin-mutter <= 3.20.38
Obsoletes:      deepin-mutter-devel <= 3.20.38

%description
This package provides a kwin configuration that used as the new WM for Deepin
Desktop Environment.

%package devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       kwin-devel%{?_isa}
Requires:       qt5-qtx11extras-devel%{?_isa}
Requires:       gsettings-qt-devel%{?_isa}
Requires:       dtkcore-devel%{?_isa}
Requires:       kf5-kglobalaccel-devel%{?_isa}


%description devel
Header files and libraries for %{name}.

%prep
%setup -q -n %{repo}-%{version}
%patch0 -p2
%patch1 -p1
%patch2 -p1

sed -i 's:/lib:/%{_lib}:' plugins/kwin-xcb/lib/CMakeLists.txt
sed -i 's:/usr/lib:%{_libdir}:' plugins/kwin-xcb/plugin/main.cpp
sed -i 's:/usr/lib:%{_libexecdir}:' deepin-wm-dbus/deepinwmfaker.cpp

%build
# help find (and prefer) qt5 utilities, e.g. qmake, lrelease
export PATH=%{_qt5_bindir}:$PATH
%cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} -DCMAKE_BUILD_TYPE=Release -DKWIN_VERSION=$(rpm -q --qf '%%{version}' kwin-devel)
%cmake_build

%install
%cmake_install
chmod 755 %{buildroot}%{_bindir}/kwin_no_scale

%ldconfig_scriptlets

%files
%doc CHANGELOG.md
%license LICENSE
%{_sysconfdir}/xdg/*
%{_bindir}/deepin-wm-dbus
%{_bindir}/kwin_no_scale
%{_libdir}/libkwin-xcb.so.*
%{_qt5_plugindir}/org.kde.kdecoration2/libdeepin-chameleon.so
%{_qt5_plugindir}/platforms/lib%{repo}-xcb.so
#{_qt5_plugindir}/kwin/effects/plugins/
%{_datadir}/dde-kwin-xcb/
%{_datadir}/applications/kwin-wm-multitaskingview.desktop
%{_datadir}/dbus-1/services/*.service
%{_datadir}/dbus-1/interfaces/*.xml
%{_datadir}/kwin/scripts/*
%{_datadir}/kwin/tabbox/*

%files devel
%{_libdir}/libkwin-xcb.so
%{_libdir}/pkgconfig/%{repo}.pc
%{_includedir}/%{repo}

%changelog
* Fri Sep 11 2020 Jan Grulich <jgrulich@redhat.com> - 0.1.0-10
- rebuild (qt5)

* Fri Aug  7 2020 Robin Lee <cheeselee@fedoraproject.org> - 0.1.0-9
- Improve compatibility with new CMake macro

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-9
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 06 2020 Rex Dieter <rdieter@fedoraproject.org> - 0.1.0-7
- rebuild (qt5)

* Thu Feb 27 2020 Robin Lee <cheeselee@fedoraproject.org> - 0.1.0-6
- Fix path conflict with kdeplasma-addons (RHBZ#1807283)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 23 2019 Robin Lee <cheeselee@fedoraproject.org> - 0.1.0-4
- Fix runtime issue with kwin 5.17

* Mon Dec 09 2019 Jan Grulich <jgrulich@redhat.com> - 0.1.0-3
- rebuild (qt5)

* Wed Sep 25 2019 Jan Grulich <jgrulich@redhat.com> - 0.1.0-2
- rebuild (qt5)

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 17 2019 Jan Grulich <jgrulich@redhat.com> - 0.0.4-3
- rebuild (qt5)

* Wed Jun 05 2019 Jan Grulich <jgrulich@redhat.com> - 0.0.4-2
- rebuild (qt5)

* Mon Apr 22 2019 Robin Lee <cheeselee@fedoraproject.org> - 0.0.4-1
- new version

* Mon Apr 15 2019 Robin Lee <cheeselee@fedoraproject.org> - 0.0.3.2-1
- Update to 0.0.3.2

* Fri Apr 12 2019 Robin Lee <cheeselee@fedoraproject.org> - 0.0.3.1-1
- Initial packaging

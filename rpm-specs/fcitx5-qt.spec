%global forgeurl https://github.com/fcitx/fcitx5-qt
%global commit 932e25f361f588a1e87f57e8a994bba80bf8798d
%forgemeta
%global __provides_exclude_from ^%{_libdir}/(fcitx5|qt5)/.*\\.so$


Name:           fcitx5-qt
Version:        0
Release:        0.5%{?dist}
Summary:        Qt library and IM module for fcitx5
# Fcitx5Qt{4,5}DBusAddons Library and Input context plugin are released under BSD.
License:        LGPLv2+ and BSD
URL:            %{forgeurl}
Source:         %{forgesource}
# upstream don't use /usr/libexec, patch to fix
Patch0:         0001-use-usr-libexec-instead.patch


BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(xkbcommon-x11)
BuildRequires:  pkgconfig(Fcitx5Utils)
BuildRequires:  pkgconfig(Qt5)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui) 
BuildRequires:  gettext
BuildRequires:  qt5-qtbase-private-devel
# This needs to be rebuilt on every minor Qt5 version bump
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}

%description
Qt library and IM module for fcitx5.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       fcitx5-devel

%description devel
Development files for %{name}

%prep
%forgeautosetup -p1

%build
%cmake -GNinja -DENABLE_QT4=False
%cmake_build 

%install
%cmake_install

%find_lang %{name}


%files -f %{name}.lang
%license LICENSES/LGPL-2.1-or-later.txt
%doc README.md 
%{_libdir}/libFcitx5Qt5DBusAddons.so.1
%{_libdir}/libFcitx5Qt5WidgetsAddons.so.2
%{_libdir}/libFcitx5Qt5DBusAddons.so.*.*
%{_libdir}/libFcitx5Qt5WidgetsAddons.so.*.*
%{_libdir}/fcitx5/qt5/
%{_qt5_plugindir}/platforminputcontexts/libfcitx5platforminputcontextplugin.so
%{_libexecdir}/fcitx5/

%files devel
%{_includedir}/Fcitx5Qt5/
%{_libdir}/cmake/Fcitx5Qt5*
%{_libdir}/libFcitx5Qt5DBusAddons.so
%{_libdir}/libFcitx5Qt5WidgetsAddons.so

%changelog
* Fri Oct 16 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.5
- update to 932e25f361f588a1e87f57e8a994bba80bf8798d upstream commit

* Wed Sep 16 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.4
- Upstream commit f5adc1bd85a89a1d3888052fa9403c8e9b454bfa
- make provides sane

* Sat Sep 12 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.3.20200912git02bbbf6
- Rebuild for fcitx5, QT5
- Upstream commit 02bbbf671dc44e83ef8eb9352483e67ad43381e3

* Sun Aug 16 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.2.20200811git3ddd34a
- rebuilt

* Wed Aug 12 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.1.20200811git3ddd34a
- initial package

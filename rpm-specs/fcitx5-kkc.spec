%global forgeurl https://github.com/fcitx/fcitx5-kkc
%global commit   0ffde563576b3ac4f62c55f5508251de3f22fd0b
%forgemeta
%global __provides_exclude_from ^%{_libdir}/fcitx5/.*\\.so$

Name:           fcitx5-kkc
Version:        0
Release:        0.3%{?dist}
Summary:        Libkkc input method support for Fcitx5
License:        GPLv3+
Url:            %{forgeurl}
Source:         %{forgesource}


BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  extra-cmake-modules
BuildRequires:  cmake(Fcitx5Core)
BuildRequires:  cmake(Fcitx5Qt5WidgetsAddons)
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(kkc-1.0)
BuildRequires:  pkgconfig(Qt5Core) >= 5.7
BuildRequires:  pkgconfig(Qt5Gui) >= 5.7
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.7
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  gettext
Requires:       hicolor-icon-theme
Requires:       fcitx5-data

%description
This provides libkkc input method support for fcitx5. Released under GPL3+.

%prep
%forgeautosetup

%build
%cmake -GNinja
%cmake_build

%install
%cmake_install

%find_lang %{name}

%files -f %{name}.lang
%doc README.md
%license LICENSES/GPL-3.0-or-later.txt
%{_libdir}/fcitx5/kkc.so
%{_libdir}/fcitx5/qt5/libfcitx5-kkc-config.so

%{_datadir}/fcitx5/addon/kkc.conf
%{_datadir}/fcitx5/inputmethod/kkc.conf

%dir %{_datadir}/fcitx5/kkc
%{_datadir}/fcitx5/kkc/dictionary_list
%{_datadir}/fcitx5/kkc/rule

%{_datadir}/icons/hicolor/*/apps/fcitx-kkc.png

%changelog
* Fri Oct 16 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.3
- update to 0ffde563576b3ac4f62c55f5508251de3f22fd0b upstream commit

* Sat Sep 12 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.2
- Rebuild for fcitx5

* Mon Aug 31 09:58:21 CST 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.1.20200831git7c6d0b5
- Initial Package


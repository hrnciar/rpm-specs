%global forgeurl https://github.com/fcitx/fcitx5-skk
%global commit   eff9bc32bcccdae65dcae05adfc9eb7a642a667e
%forgemeta
%global __provides_exclude_from ^%{_libdir}/fcitx5/.*\\.so$

Name:       fcitx5-skk
Version:    0
Release:    0.4%{?dist}
Summary:    Japanese SKK (Simple Kana Kanji) Engine for Fcitx5
License:    GPLv3+
URL:        %{forgeurl}
Source:     %{forgesource}

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  extra-cmake-modules
BuildRequires:  fcitx5-qt-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Fcitx5Core)
BuildRequires:  pkgconfig(libskk)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(Qt5)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  gettext
BuildRequires:  intltool
Requires:       skkdic
Requires:       hicolor-icon-theme
Requires:       fcitx5-data

%description
Fcitx5-skk is an SKK (Simple Kana Kanji) engine for Fcitx.  It provides
Japanese input method using libskk.

%prep
%forgesetup

%build
%cmake -GNinja
%cmake_build

%install
%cmake_install

%find_lang %{name}

%files -f %{name}.lang
%license LICENSES/GPL-3.0-or-later.txt
%doc README.md 
%{_libdir}/fcitx5/qt5/libfcitx5-skk-config.so
%{_libdir}/fcitx5/skk.so
%{_datadir}/fcitx5/addon/skk.conf
%{_datadir}/fcitx5/inputmethod/skk.conf
%dir %{_datadir}/fcitx5/skk
%{_datadir}/fcitx5/skk/dictionary_list
%{_datadir}/icons/hicolor/64x64/apps/fcitx-skk.png

%changelog
* Fri Oct 16 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.4
- update to eff9bc32bcccdae65dcae05adfc9eb7a642a667e upstream commit

* Sat Sep 12 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.3
- Rebuild for fcitx5
- Upstream commit cc9261407b496a5708dca642deec5bcafe1cf58c

* Sun Aug 16 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.2.20200813git02fb41d
- rebuilt

* Thu Aug 13 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.1.20200813git02fb41d
- Initial Package
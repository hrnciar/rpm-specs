%global forgeurl https://github.com/fcitx/fcitx5-chewing
%global commit   7f7ea5e8229de495be2168ef571615f012730ff0
%forgemeta
%global __provides_exclude_from ^%{_libdir}/fcitx5/.*\\.so$

Name:       fcitx5-chewing
Version:    0
Release:    0.3%{?dist}
Summary:    Chewing Wrapper for Fcitx
License:    GPLv2+
URL:        %{forgeurl}
Source:     %{forgesource}

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  intltool
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(Fcitx5Core)
BuildRequires:  pkgconfig(chewing)
BuildRequires:  gettext
Requires:       hicolor-icon-theme
Requires:       fcitx5-data

%description
fcitx5-chewing is a Chewing Wrapper for Fcitx.

Chewing is a set of free intelligent Chinese 
Phonetic IME.


%prep
%forgesetup

%build
%cmake -GNinja
%cmake_build

%install
%cmake_install

%find_lang %{name}

%files -f %{name}.lang
%license LICENSES/GPL-2.0-or-later.txt
%doc README.md 
%{_libdir}/fcitx5/chewing.so
%{_datadir}/fcitx5/addon/chewing.conf
%{_datadir}/fcitx5/inputmethod/chewing.conf
%{_datadir}/icons/hicolor/48x48/apps/fcitx-chewing.png

%changelog
* Sat Sep 12 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.3
- Rebuild for fcitx5

* Sun Aug 16 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.2.20200813git7f7ea5e
- rebuilt

* Thu Aug 13 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.1.20200813git7f7ea5e
- Initial Package

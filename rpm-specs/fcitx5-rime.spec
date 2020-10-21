%global forgeurl https://github.com/fcitx/fcitx5-rime
%global commit   e20996d752e3b2882d35c15630fa4b75da177485
%forgemeta
%global __provides_exclude_from ^%{_libdir}/fcitx5/.*\\.so$


Name:           fcitx5-rime
Version:        0
Release:        0.5%{?dist}
Summary:        RIME support for Fcitx
License:        LGPLv2+
URL:            %{forgeurl}
Source:         %{forgesource}


BuildRequires:  brise 
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  gettext
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Fcitx5Core)
BuildRequires:  pkgconfig(Fcitx5Module)
BuildRequires:  pkgconfig(rime)
Requires:       hicolor-icon-theme
Requires:       fcitx5-data
Requires:       brise

%description
RIME(中州韻輸入法引擎) is mainly a Traditional Chinese 
input method engine.

%prep
%forgesetup

%build
%cmake -GNinja
%cmake_build 

%install
%cmake_install

%find_lang %{name}

%check
%ctest

%files -f %{name}.lang
%license LICENSES/LGPL-2.1-or-later.txt
%doc README.md 
%{_libdir}/fcitx5/rime.so
%{_datadir}/fcitx5/*/rime.conf
%{_datadir}/icons/hicolor/*/*/*


%changelog
* Fri Oct 16 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.5
- update to e20996d752e3b2882d35c15630fa4b75da177485 upstream commit

* Sat Sep 12 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.4
- Rebuild for fcitx5
- Upstream commit 6da82ec569e3a83a94f7c1fff71fce885a6b2252

* Sat Aug 22 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.3.20200811gite4fc600
- add missing Requires

* Sun Aug 16 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.2.20200811gite4fc600
- rebuilt

* Wed Aug 12 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.1.20200811gite4fc600
- initial package

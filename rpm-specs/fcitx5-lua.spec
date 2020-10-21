%global forgeurl https://github.com/fcitx/fcitx5-lua
%global commit   ff218dd82db069d4a502a3eb212a80184c592ce0
%forgemeta
%global __provides_exclude_from ^%{_libdir}/fcitx5/.*\\.so$


Name:           fcitx5-lua
Version:        0
Release:        0.3%{?dist}
Summary:        Lua support for fcitx
License:        LGPLv2+
URL:            %{forgeurl}
Source:         %{forgesource}


BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(lua)
BuildRequires:  pkgconfig(Fcitx5Core)
BuildRequires:  pkgconfig(Fcitx5Module)
Requires:       fcitx5-data

%description
Lua support for fcitx.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       fcitx5-devel

%description devel
Devel files for fcitx5-lua

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
%{_libdir}/fcitx5/luaaddonloader.so
%{_datadir}/fcitx5/addon/imeapi.conf
%{_datadir}/fcitx5/addon/luaaddonloader.conf
%{_datadir}/fcitx5/lua

%files devel
%{_includedir}/Fcitx5/Module/fcitx-module/luaaddonloader
%{_libdir}/cmake/Fcitx5ModuleLuaAddonLoader


%changelog
* Sat Sep 12 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.3
- Rebuild for fcitx5
- Upstream commit ff218dd82db069d4a502a3eb212a80184c592ce0

* Sun Aug 16 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.2.20200811gitd705404
- rebuilt

* Wed Aug 12 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.1.20200811gitd705404
- initial package

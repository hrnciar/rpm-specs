%global forgeurl https://github.com/fcitx/fcitx5-chinese-addons
%global commit   6f856b73802f009f0cfa935115f5911e835b6231
%forgemeta
%global dictver 20121124
%global __provides_exclude_from ^%{_libdir}/fcitx5/.*\\.so$

Name:           fcitx5-chinese-addons
Version:        0
Release:        0.4%{?dist}
Summary:        Chinese related addon for fcitx5
License:        LGPLv2+
URL:            %{forgeurl}
Source:         %{forgesource}
Source1:        https://download.fcitx-im.org/data/py_table-%{dictver}.tar.gz
Source2:        https://download.fcitx-im.org/data/py_stroke-%{dictver}.tar.gz


BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  fcitx5-qt-devel
BuildRequires:  fcitx5-lua-devel
BuildRequires:  gcc-c++
BuildRequires:  libime-devel
BuildRequires:  ninja-build
BuildRequires:  gettext-devel
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(fmt)
BuildRequires:  pkgconfig(Qt5WebKit)
BuildRequires:  pkgconfig(Qt5WebKitWidgets)
BuildRequires:  pkgconfig(opencc)
BuildRequires:  pkgconfig(Fcitx5Core)
BuildRequires:  pkgconfig(Fcitx5Module)
Requires:       hicolor-icon-theme
Requires:       %{name}-data = %{version}-%{release}
Requires:       fcitx5-lua
Requires:       fcitx5-data

%description
This provides pinyin and table input method
support for fcitx5. Released under LGPL-2.1+.

im/pinyin/emoji.txt is derived from Unicode 
CLDR with modification.

%package data
Summary:        Data files of %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       hicolor-icon-theme
Requires:       fcitx5-lua
Requires:       fcitx5-data

%description data
The %{name}-data package provides shared data for %{name}.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       fcitx5-devel

%description devel
devel files for fcitx5-chinese-addons

%prep
%forgesetup
ln -s %{S:1} modules/pinyinhelper
ln -s %{S:2} modules/pinyinhelper

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
%{_bindir}/scel2org5
%{_libdir}/fcitx5/*.so
%{_libdir}/fcitx5/qt5/libpinyindictmanager.so

%files data
%dir %{_datadir}/fcitx5/pinyin
%dir %{_datadir}/fcitx5/punctuation
%dir %{_datadir}/fcitx5/pinyinhelper
%{_datadir}/fcitx5/addon/*.conf
%{_datadir}/fcitx5/inputmethod/*.conf
%{_datadir}/fcitx5/lua/imeapi/extensions/pinyin.lua
%{_datadir}/fcitx5/pinyin/*.dict
%{_datadir}/fcitx5/pinyinhelper/py_*.mb
%{_datadir}/fcitx5/punctuation/punc.mb.*
%dir %{_datadir}/fcitx5/chttrans
%{_datadir}/fcitx5/chttrans/gbks2t.tab
%{_datadir}/icons/hicolor/*/apps/*

%files devel
%{_includedir}/Fcitx5/Module/fcitx-module/*
%{_libdir}/cmake/Fcitx5Module*

%changelog
* Fri Oct 16 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.4
- update to 6f856b73802f009f0cfa935115f5911e835b6231 upstream commit

* Sat Sep 12 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.3
- Rebuild for fcitx5
- upstream commit 591848d9c22724d788bf17a2e10f19531d635689

* Sun Aug 16 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.2.20200811gitef9beb7
- rebuilt

* Wed Aug 12 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.1.20200811gitef9beb7
- initial package


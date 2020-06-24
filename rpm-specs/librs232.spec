%global date          20190917
%global commit0       1c29a279484ee4850611b76a6571566e0ec133bb
%global shortcommit0  %(c=%{commit0}; echo ${c:0:7})
%global the_owner     srdgame

Name:           librs232
Version:        1.0.3
Release:        10.%{date}git%{shortcommit0}%{?dist}
Summary:        Library for serial communications over RS-232 with Lua bindings
License:        MIT
Url:            https://github.com/%{the_owner}/%{name}/
Source:         https://github.com/%{the_owner}/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{version}-%{date}git%{shortcommit0}.tar.gz
# Fix compilation error
# Upstrem reference: https://patch-diff.githubusercontent.com/raw/srdgame/librs232/pull/7.patch
Patch0:         https://patch-diff.githubusercontent.com/raw/%{the_owner}/%{name}/pull/7.patch#/%{name}-%{version}-fix-compilation-error.patch

BuildRequires:  /usr/bin/git
BuildRequires:  gcc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  lua >= 5.1
BuildRequires:  lua-devel >= 5.1


%description
%{name} is a multi-platform library that provides support for communicating
over serial ports (e.g. RS-232). It also provides Lua bindings.


%package devel
Summary: Development files for %{name}
License: MIT
Requires: %{name}%{?_isa} = %{version}-%{release}


%description devel
The %{name}-devel package contains C header files for developing
applications that use %{name} library.


%package -n lua-%{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Summary: Lua bindings for %{name}
License: MIT
Requires: lua(abi) = %{lua_version}


%description -n lua-%{name}
The lua-%{name} package provides Lua binding for %{name} library.
It allows Lua programs to communicate over serial ports.


%prep
%autosetup -S git -n %{name}-%{commit0}
export LUA_INCLUDE=
./autogen.sh
%configure --disable-static


%build
%make_build


%install
%make_install
# Remove unneeded .la files
find %{buildroot} -name '*.la' -exec rm {} \;


%files
%license COPYING
%doc AUTHORS doc/example.lua
%{_libdir}/*.so.*


%ldconfig_scriptlets


%files devel
%{_libdir}/*.so
%{_includedir}/%{name}
%{_libdir}/pkgconfig/%{name}*.pc


%files -n lua-%{name}
%{lua_libdir}/*.so


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-10.20190917git1c29a27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 13 2019 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 1.0.3-9.20190917git1c29a27
- Drop patch upstream merged
- Update to the latest available version
- Add patch to fix compilation error

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-7.20171229git21ecc3c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-6.20171229git21ecc3c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-5.20171229git21ecc3c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-4.20171229git21ecc3c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 03 2018 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 1.0.3-3.20171229git21ecc3c
- Drop patch upstream merged
- Configure warning patch added

* Thu Dec 21 2017 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 1.0.3-2.20171219gitc0a3c75
- Drop patch upstream merged

* Tue Sep 26 2017 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 1.0.3-1.20160327git4de45dd
- Initial RPM release.

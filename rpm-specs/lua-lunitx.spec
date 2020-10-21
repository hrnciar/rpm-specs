Name:           lua-lunitx
Version:        0.8.1
Release:        2%{?dist}
Summary:        Unit testing framework for Lua

License:        MIT
URL:            https://github.com/dcurrie/lunit/
Source0:        https://github.com/dcurrie/lunit/archive/%{version}.tar.gz#/lunitx-%{version}.tar.gz

# for running tests
# also, macros are in lua-devel
BuildRequires:  lua-devel >= 5.2

BuildArch:      noarch

Provides:       lua-lunit = %{version}-%{release}
Obsoletes:      lua-lunit <= 0.5-18

%description
This is lunitx Version 0.8.1, an extended version of Lunit
for Lua 5.2, 5.3, and 5.4.

Lunit is a unit testing framework for lua.


%prep
%autosetup -n lunit-%{version}


%install
mkdir -p %{buildroot}%{_bindir}
cp -p extra/lunit.sh %{buildroot}%{_bindir}/lunit

mkdir -p %{buildroot}%{lua_pkgdir}
cp -pr lua/* %{buildroot}%{lua_pkgdir}


%check
# for self test, without --dontforce lunit will try to load its launcher which is a shell script
LUA_PATH='%{buildroot}%{lua_pkgdir}/?.lua;;' %{buildroot}%{_bindir}/lunit --dontforce test/selftest.lua


%files
%license LICENSE
%doc ANNOUNCE CHANGES DOCUMENTATION examples README*
%{_bindir}/lunit
%{lua_pkgdir}/*


%changelog
* Thu Aug 27 2020 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.8.1-2
- Use standard Lua macros

* Tue Aug 25 2020 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.8.1-1
- Initial Fedora package (replacing lua-lunit)

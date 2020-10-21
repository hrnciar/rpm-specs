# see https://luarocks.org/modules/siffiejoe/bit32/5.3.5-1
%global srcname lua-compat-5.3
%global srcver 0.9

Name:           lua-bit32
Version:        5.3.5
Release:        1%{?dist}
Summary:        Lua 5.2 bit manipulation library

License:        MIT
URL:            https://luarocks.org/modules/siffiejoe/bit32
Source0:        https://github.com/keplerproject/%{srcname}/archive/v%{srcver}.tar.gz#/%{srcname}-%{srcver}.tar.gz

BuildRequires:  gcc
BuildRequires:  lua-devel

%description
bit32 is the native Lua 5.2 bit manipulation library, in the version from Lua
5.3; it is compatible with Lua 5.1 to 5.4.


%prep
%autosetup -n %{srcname}-%{srcver}


%build
gcc %{optflags} -I/usr/include -I./c-api $(pkg-config --libs lua) lbitlib.c \
    -shared -fPIC -o bit32.so -DLUA_COMPAT_BITLIB


%install
install -Dpm 755 bit32.so %{buildroot}%{lua_libdir}/bit32.so


%files
%license LICENSE
# README.md doesn't mention bit32
%{lua_libdir}/bit32.so


%changelog
* Mon Aug 31 2020 Michel Alexandre Salim <salimma@fedoraproject.org> - 5.3.5-1-1
- Update to 5.3.5

* Wed May 10 2017 Michel Alexandre Salim <salimma@fedoraproject.org> - 5.3.0-2
- Remove defattr

* Mon May 08 2017 Michel Alexandre Salim <salimma@fedoraproject.org> - 5.3.0-1
- Initial package

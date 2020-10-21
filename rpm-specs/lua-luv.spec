%global lua_54_version 5.4
%global lua_54_incdir %{_includedir}/lua-%{lua_54_version}
%global lua_54_libdir %{_libdir}/lua/%{lua_54_version}
%global lua_54_pkgdir %{_datadir}/lua/%{lua_54_version}
%global lua_54_builddir obj-lua54

%global lua_51_version 5.1
%global lua_51_incdir %{_includedir}/lua-%{lua_51_version}
%global lua_51_libdir %{_libdir}/lua/%{lua_51_version}
%global lua_51_pkgdir %{_datadir}/lua/%{lua_51_version}
%global lua_51_builddir obj-lua51

%global real_version 1.36.0
%global extra_version 0

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  libuv-devel
BuildRequires:  lua >= %{lua_54_version}
BuildRequires:  lua-devel >= %{lua_54_version}
BuildRequires:  compat-lua >= %{lua_51_version}
BuildRequires:  compat-lua-devel >= %{lua_51_version}
BuildRequires:  lua5.1-compat53

Name:           lua-luv
Version:        %{real_version}.%{extra_version}
Release:        4%{?dist}

License:        ASL 2.0
Summary:        Bare libuv bindings for lua
Url:            https://github.com/luvit/luv

Requires:       lua(abi) = %{lua_54_version}

Source0:        https://github.com/luvit/luv/archive/%{real_version}-%{extra_version}/luv-%{version}.tar.gz
Patch0:         luv-1.36.0-lua-5.4.patch

%if 0%{?el8}
# libuv-devel is from the CentOS Devel repo, only available on
# aarch64, ppc64le, and x86_64:
# https://mirrors.edge.kernel.org/centos/8-stream/Devel/
# bz# 1829151
ExcludeArch:    s390x
%endif

%description
This library makes libuv available to lua scripts. It was made
for the luvit project but should usable from nearly any lua
project.

The library can be used by multiple threads at once. Each thread
is assumed to load the library from a different lua_State. Luv
will create a unique uv_loop_t for each state. You can't share uv
handles between states/loops.

The best docs currently are the libuv docs themselves. Hopefully
soon we'll have a copy locally tailored for lua.

%package devel
Summary:        Development files for lua-luv
Requires:       lua-luv%{?_isa} = %{version}-%{release}

%description devel
Files required for lua-luv development

%package -n lua5.1-luv
Summary:        Bare libuv bindings for lua 5.1
Requires:       lua(abi) = %{lua_51_version}

%description -n lua5.1-luv
This library makes libuv available to lua scripts. It was made
for the luvit project but should usable from nearly any lua
project.

The library can be used by multiple threads at once. Each thread
is assumed to load the library from a different lua_State. Luv
will create a unique uv_loop_t for each state. You can't share uv
handles between states/loops.

The best docs currently are the libuv docs themselves. Hopefully
soon we'll have a copy locally tailored for lua.

%package -n lua5.1-luv-devel
Summary:        Development files for lua5.1-luv
Requires:       lua5.1-luv%{?_isa} = %{version}-%{release}

%description -n lua5.1-luv-devel
Files required for lua5.1-luv development

%prep
%autosetup -p1 -n luv-%{real_version}-%{extra_version}

# Remove bundled dependencies
rm -rf deps

# Remove network sensitive tests gh#luvit/luv#340
rm -f tests/test-dns.lua

%build
# lua
mkdir %{lua_54_builddir}

pushd %{lua_54_builddir}
%cmake .. \
    -DWITH_SHARED_LIBUV=ON \
    -DBUILD_MODULE=ON \
    -DBUILD_SHARED_LIBS=ON \
    -DWITH_LUA_ENGINE=Lua \
    -DLUA_BUILD_TYPE=System \
    -DINSTALL_LIB_DIR=%{_libdir} \
    -DLUA_INCLUDE_DIR=%{lua_54_incdir}

%cmake_build
popd

# lua-compat
mkdir %{lua_51_builddir}

pushd %{lua_51_builddir}
%cmake .. \
    -DWITH_SHARED_LIBUV=ON \
    -DBUILD_MODULE=ON \
    -DBUILD_SHARED_LIBS=ON \
    -DWITH_LUA_ENGINE=Lua \
    -DLUA_BUILD_TYPE=System \
    -DINSTALL_LIB_DIR=%{_libdir} \
    -DLUA_COMPAT53_DIR=%{lua_51_incdir} \
    -DLUA_INCLUDE_DIR=%{lua_51_incdir} \
    -DLUA_LIBRARY=%{_libdir}/liblua-%{lua_51_version}.so

%cmake_build
popd

%install
# lua-5.3
install -d -m 0755 %{buildroot}%{lua_54_libdir}
install -m 0755 -p %{lua_54_builddir}/%{_vpath_builddir}/luv.so %{buildroot}%{lua_54_libdir}/luv.so

install -d -m 0755 %{buildroot}%{lua_54_incdir}/luv
for f in lhandle.h lreq.h luv.h util.h; do
    install -m 0644 -p src/$f %{buildroot}%{lua_54_incdir}/luv/$f
done

# lua-5.1
install -d -m 0755 %{buildroot}%{lua_51_libdir}
install -m 0755 -p %{lua_51_builddir}/%{_vpath_builddir}/luv.so %{buildroot}%{lua_51_libdir}/luv.so

install -d -m 0755 %{buildroot}%{lua_51_incdir}/luv
for f in lhandle.h lreq.h luv.h util.h; do
    install -m 0644 -p src/$f %{buildroot}%{lua_51_incdir}/luv/$f
done

%check
# lua-5.1
ln -sf %{lua_51_builddir}/%{_vpath_builddir}/luv.so luv.so
lua-5.1 tests/run.lua
rm luv.so
# lua-5.4
ln -sf %{lua_54_builddir}/%{_vpath_builddir}/luv.so luv.so
lua tests/run.lua
rm luv.so

%files
%doc README.md
%license LICENSE.txt
%{lua_libdir}/luv.so

%files devel
%dir %{lua_54_incdir}
%dir %{lua_54_incdir}/luv/
%{lua_54_incdir}/luv/lhandle.h
%{lua_54_incdir}/luv/lreq.h
%{lua_54_incdir}/luv/luv.h
%{lua_54_incdir}/luv/util.h

%files -n lua5.1-luv
%doc README.md
%license LICENSE.txt
%{lua_51_libdir}/luv.so

%files -n lua5.1-luv-devel
%dir %{lua_51_incdir}
%dir %{lua_51_incdir}/luv/
%{lua_51_incdir}/luv/lhandle.h
%{lua_51_incdir}/luv/lreq.h
%{lua_51_incdir}/luv/luv.h
%{lua_51_incdir}/luv/util.h

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.36.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 30 2020 Tom Callaway <spot@fedoraproject.org> - 1.36.0.0-3
- fix for lua 5.4
- adjust logic for new cmake weirdness (f33+)

* Tue Jun 30 2020 Björn Esser <besser82@fedoraproject.org> - 1.36.0.0-2
- Rebuilt for Lua 5.4

* Tue Apr 28 2020 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.36.0.0-1
- Update to version 1.36.0-0
- Support building on EPEL 8

* Sat Feb 29 2020 Andreas Schneider <asn@redhat.com> - 1.34.2.1-1
-  Update to version 1.34.2-1
  - https://github.com/luvit/luv/releases/tag/1.34.2-0
  - https://github.com/luvit/luv/releases/tag/1.34.2-1

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.34.1.1-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 21 2020 Andreas Schneider <asn@redhat.com> - 1.34.1.1-0
- Update to version 1.34.1-1

* Tue Oct 29 2019 Andreas Schneider <asn@redhat.com> - 1.32.0.0-0
- Update to version 1.32.0-0

* Tue Oct 01 2019 Andreas Schneider <asn@redhat.com> - 1.30.1.1-5
- Fixed versioning

* Tue Oct 01 2019 Andreas Schneider <asn@redhat.com> - 1.30.1-4.1
- Update to version 1.30.1-1
- Removed luv-1.30-include_lua_header.patch
- Added missing Requires for devel packages
- Fixed source URL
- Fixed license
- Preserved timestamps

* Mon Sep 30 2019 Andreas Schneider <asn@redhat.com> - 1.30.1-3
- Fixed BR for lua 5.3

* Mon Sep 30 2019 Andreas Schneider <asn@redhat.com> - 1.30.1-2
- Added BR for gcc
- Renamed lua globals

* Tue Sep 24 2019 Andreas Schneider <asn@redhat.com> - 1.30.1-1
- Initial version 1.30.1-0

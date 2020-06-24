%{!?lua_version: %global lua_version %{lua: print(string.sub(_VERSION, 5))}}
%{!?lua_libdir: %global lua_libdir %{_libdir}/lua/%{lua_version}}
%{!?lua_pkgdir: %global lua_pkgdir %{_datadir}/lua/%{lua_version}}

%{!?lua_compat_version: %global lua_compat_version 5.1}
%{!?lua_compat_libdir: %global lua_compat_libdir %{_libdir}/lua/%{lua_compat_version}}
%{!?lua_compat_pkgdir: %global lua_compat_pkgdir %{_datadir}/lua/%{lua_compat_version}}
%{!?lua_compat_builddir: %global lua_compat_builddir %{_builddir}/compat-lua-%{name}-%{version}-%{release}}

Summary:        Lua binding for OpenSSL library
Name:           lua-sec
Version:        0.9
Release:        2%{?dist}
License:        MIT
URL:            https://github.com/brunoos/luasec
Source0:        https://github.com/brunoos/luasec/archive/v%{version}/luasec-%{version}.tar.gz
%if 0%{?fedora} >= 16 || 0%{?rhel} >= 7
Requires:       lua(abi) = %{lua_version}
%else
Requires:       lua >= %{lua_version}
%endif
Requires:       lua-socket
BuildRequires:  gcc
BuildRequires:  lua-devel
BuildRequires:  openssl-devel >= 1.0.2

%description
Lua binding for OpenSSL library to provide TLS/SSL communication.
It takes an already established TCP connection and creates a secure
session between the peers.

%if 0%{?fedora} >= 20
%package -n lua%{lua_compat_version}-sec
Summary:        Lua %{lua_compat_version} binding for OpenSSL library
Obsoletes:      lua-sec-compat < 0.7
Provides:       lua-sec-compat = %{version}-%{release}
Provides:       lua-sec-compat%{?_isa} = %{version}-%{release}
Requires:       lua(abi) = %{lua_compat_version}
BuildRequires:  compat-lua-devel >= %{lua_compat_version}

%description -n lua%{lua_compat_version}-sec
Lua %{lua_compat_version} binding for OpenSSL library to provide TLS/SSL communication.
It takes an already established TCP connection and creates a secure
session between the peers.
%endif

%prep
%setup -q -n luasec-%{version}

%if 0%{?fedora} >= 20
rm -rf %{lua_compat_builddir}
cp -a . %{lua_compat_builddir}
%endif

%build
%make_build linux \
  CFLAGS="$RPM_OPT_FLAGS -fPIC -I. -I%{_includedir} -DWITH_LUASOCKET -DLUASOCKET_DEBUG -DLUA_COMPAT_APIINTCASTS" \
  LD="gcc -shared" LDFLAGS="-fPIC -shared -L./luasocket $RPM_LD_FLAGS"

%if 0%{?fedora} >= 20
pushd %{lua_compat_builddir}
%make_build linux \
  CFLAGS="$RPM_OPT_FLAGS -fPIC -I. -I%{_includedir}/lua-%{lua_compat_version} -DWITH_LUASOCKET -DLUASOCKET_DEBUG -DLUA_COMPAT_APIINTCASTS" \
  LD="gcc -shared" LDFLAGS="-fPIC -shared -L./luasocket $RPM_LD_FLAGS"
popd
%endif

%install
%make_install \
  CFLAGS="$RPM_OPT_FLAGS -fPIC -I. -I%{_includedir} -DWITH_LUASOCKET -DLUASOCKET_DEBUG -DLUA_COMPAT_APIINTCASTS" \
  LD="gcc -shared" LDFLAGS="-fPIC -shared -L./luasocket $RPM_LD_FLAGS" \
  LUAPATH=%{lua_pkgdir} LUACPATH=%{lua_libdir}

%if 0%{?fedora} >= 20
pushd %{lua_compat_builddir}
%make_install \
  CFLAGS="$RPM_OPT_FLAGS -fPIC -I. -I%{_includedir}/lua-%{lua_compat_version} -DWITH_LUASOCKET -DLUASOCKET_DEBUG -DLUA_COMPAT_APIINTCASTS" \
  LD="gcc -shared" LDFLAGS="-fPIC -shared -L./luasocket $RPM_LD_FLAGS" \
  LUAPATH=%{lua_compat_pkgdir} LUACPATH=%{lua_compat_libdir}
popd
%endif

%files
%license LICENSE
%doc CHANGELOG
%{lua_libdir}/ssl.so
%{lua_pkgdir}/ssl.lua
%dir %{lua_pkgdir}/ssl
%{lua_pkgdir}/ssl/*.lua

%if 0%{?fedora} >= 20
%files -n lua%{lua_compat_version}-sec
%license LICENSE
%doc CHANGELOG
%{lua_compat_libdir}/ssl.so
%{lua_compat_pkgdir}/ssl.lua
%dir %{lua_compat_pkgdir}/ssl
%{lua_compat_pkgdir}/ssl/*.lua
%endif

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 05 2019 Robert Scheck <robert@fedoraproject.org> 0.9-1
- Upgrade to 0.9 (#1767708)

* Wed Oct 23 2019 Robert Scheck <robert@fedoraproject.org> 0.8.2-1
- Upgrade to 0.8.2 (#1760499)

* Sat Aug 17 2019 Robert Scheck <robert@fedoraproject.org> 0.8.1-1
- Upgrade to 0.8.1 (#1742784)

* Sat Jul 27 2019 Robert Scheck <robert@fedoraproject.org> 0.8-1
- Upgrade to 0.8

* Fri Jul 26 2019 Robert Scheck <robert@fedoraproject.org> 0.7-1
- Upgrade to 0.7

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 18 2017 Robert Scheck <robert@fedoraproject.org> 0.6-1
- Upgrade to 0.6 (#1423914)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jan 16 2015 Tom Callaway <spot@fedoraproject.org> - 0.5-4
- rebuild for lua 5.3

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 14 2014 Jan Kaluza <jkaluza@redhat.com> - 0.5-1
- update to luasec-0.5 (#1000622)
- build -compat subpackage against compat-lua

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun May 12 2013 Tom Callaway <spot@fedoraproject.org> - 0.4.1-5
- rebuild for lua 5.2

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Mar 06 2012 Johan Cwiklinski <johan AT x-tnd DOT be> 0.4.1-2
- Remove __mkdir macros

* Tue Mar 06 2012 Johan Cwiklinski <johan AT x-tnd DOT be> 0.4.1-1
- 0.4.1
- Add lua as a Requires (bz #551763)

* Fri Jan 01 2010 Johan Cwiklinski <johan AT x-tnd DOT be> 0.4-1
- Initial packaging

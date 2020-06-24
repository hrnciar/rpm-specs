%{!?luaver: %global luaver %(lua -e "print(string.sub(_VERSION, 5))" || echo 0)}
%global lualibdir %{_libdir}/lua/%{luaver}
%global luapkgdir %{_datadir}/lua/%{luaver}

%global luacompatver 5.1
%global luacompatlibdir %{_libdir}/lua/%{luacompatver}
%global luacompatpkgdir %{_datadir}/lua/%{luacompatver}

%global luapkgname luaossl

Name:           lua-%{luapkgname}
Version:        20190731
Release:        2%{?dist}
Summary:        Most comprehensive OpenSSL module in the Lua universe

License:        MIT
URL:            https://github.com/wahern/%{luapkgname}
Source0:        https://github.com/wahern/%{luapkgname}/archive/rel-%{version}/%{name}-%{version}.tar.gz

%if 0%{?fedora}
Patch1:         0001-openssl-in-fedora-has-patches-for-EPV_KDF.patch
%endif

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  lua
BuildRequires:  lua-devel

%if 0%{?fedora} || 0%{?rhel} > 7
BuildRequires:  compat-lua
BuildRequires:  compat-lua-devel
%endif

Requires:       lua(abi) = %{luaver}

%description
luaossl is a comprehensive binding to OpenSSL for Lua 5.1, 5.2, and later.

%if 0%{?fedora} || 0%{?rhel} > 7
%package -n lua%{luacompatver}-%{luapkgname}
Summary:        Most comprehensive OpenSSL module in the Lua universe
Requires:       lua(abi) = %{luacompatver}

%description -n lua%{luacompatver}-%{luapkgname}
luaossl is a comprehensive binding to OpenSSL for Lua 5.1, 5.2, and later.
%endif

%package doc
Summary:        Documentation for OpenSSL Lua module
BuildArch:      noarch
Requires:       %{name} = %{version}
%if 0%{?fedora} || 0%{?rhel} > 7
Requires:       lua%{luacompatver}-%{luapkgname} = %{version}
%endif

%description doc
Documentation for the Stackable Continuation Queues library
for the Lua Programming Language

%prep
%setup -q -n %{luapkgname}-rel-%{version}

%if 0%{?fedora}
%patch1 -p1
%endif

%build
export CFLAGS="%{?optflags} -fPIC"
export LDFLAGS="%{?build_ldflags}"
make LUA_APIS="%{luaver}" %{?_smp_mflags} prefix=%{_prefix} libdir=%{_libdir}

%if 0%{?fedora} || 0%{?rhel} > 7
make LUA_APIS="%{luacompatver}" %{?_smp_mflags} prefix=%{_prefix} libdir=%{_libdir} CFLAGS="$CFLAGS -I%{_includedir}/lua-%{luacompatver}"
%endif

%install
make DESTDIR=%{buildroot} prefix=%{_prefix} libdir=%{_libdir} install%{luaver}
install -d -m 0755 %{buildroot}%{_pkgdocdir}
install -p -m 0644 doc/luaossl.pdf %{buildroot}%{_pkgdocdir}/luaossl.pdf

%if 0%{?fedora} || 0%{?rhel} > 7
make DESTDIR=%{buildroot} prefix=%{_prefix} libdir=%{_libdir} install%{luacompatver}
%endif

%files
%{luapkgdir}/openssl
%{luapkgdir}/openssl.lua
%{lualibdir}/_openssl.so
%license LICENSE

%if 0%{?fedora} || 0%{?rhel} > 7
%files -n lua%{luacompatver}-%{luapkgname}
%{luacompatpkgdir}/openssl
%{luacompatpkgdir}/openssl.lua
%{luacompatlibdir}/_openssl.so
%license LICENSE
%endif

%files doc
%{_pkgdocdir}
%doc %{_pkgdocdir}/luaossl.pdf

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20190731-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 05 2019 Tomas Krizek <tomas.krizek@nic.cz> - 20190805-1
- New upstream release https://github.com/wahern/luaossl/releases/tag/rel-20190731
- Use more portable way of passing build flags

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20181207-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 08 2019 Tomas Krizek <tomas.krizek@nic.cz> - 20181207-1
- Initial package for F28+ and EPEL 7+

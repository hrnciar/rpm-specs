%{!?lua_version: %global lua_version %{lua: print(string.sub(_VERSION, 5))}}
%{!?lua_libdir: %global lua_libdir %{_libdir}/lua/%{lua_version}}

Summary:	Cyrus SASL library for Lua
Name:		lua-cyrussasl
Version:	1.1.0
Release:	10%{?dist}
License:	BSD
URL:		https://github.com/JorjBauer/lua-cyrussasl
Source:		https://github.com/JorjBauer/lua-cyrussasl/archive/v%{version}/%{name}-%{version}.tar.gz
%if 0%{?fedora} >= 16 || 0%{?rhel} >= 7
Requires:	lua(abi) = %{lua_version}
%else
Requires:	lua >= %{lua_version}
%endif
BuildRequires:	gcc, lua-devel, cyrus-sasl-devel

%description
Lua bindings for the Cyrus SASL APIs.

%prep
%setup -q

%build
%make_build CFLAGS="$RPM_OPT_FLAGS -fPIC" LDFLAGS="-shared -fPIC -lsasl2 %{?__global_ldflags}" 

%install
install -D -p -m 755 cyrussasl.so $RPM_BUILD_ROOT%{lua_libdir}/cyrussasl.so

%files
%license LICENSE
%doc README
%{lua_libdir}/cyrussasl.so

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 30 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-9
- Rebuilt for Lua 5.4

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 02 2017 Robert Scheck <robert@fedoraproject.org> 1.1.0-1
- Upgrade to 1.1.0 (#1403598)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jan 15 2015 Tom Callaway <spot@fedoraproject.org> - 1.0.0-3
- lua 5.3
- add missing typerror

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed May 28 2014 Robert Scheck <robert@fedoraproject.org> 1.0.0-1
- Upgrade to 1.0.0
- Initial spec file for Fedora and Red Hat Enterprise Linux

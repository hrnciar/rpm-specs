%undefine __cmake_in_source_build
# Optional DNS over HTTP support
%bcond_without doh

Name:		flamethrower
Version:	0.11.0
Release:	1%{?dist}
Summary:	A DNS performance and functional testing utility

License:	ASL 2.0
URL:		https://github.com/DNS-OARC/flamethrower
Source0:	%{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# No Patch:

BuildRequires:	gcc-c++, make
BuildRequires:	cmake
BuildRequires:	libuv-devel
BuildRequires:	ldns-devel
BuildRequires:	gnutls-devel
BuildRequires:	pandoc
%if %{with doh}
BuildRequires:	libnghttp2-devel
%endif

%description
Flamethrower is a small, fast, configurable tool for
functional testing, benchmarking, and stress testing
DNS servers and networks. It supports IPv4, IPv6, UDP and TCP,
and has a modular system for generating queries used in the tests.

It was built as an alternative to dnsperf, and many
of the command line options are compatible.

%prep
%autosetup -n %{name}-%{version} -p1

%build
%cmake -DCMAKE_SKIP_BUILD_RPATH=TRUE \
%if %{with doh}
-DDOH_ENABLE=ON \
%endif

%cmake_build


%install
%cmake_install
install -m 0644 -pD man/flame.1 ${RPM_BUILD_ROOT}%{_mandir}/man1/flame.1

%check
%ctest

%files
%doc README.md
%license LICENSE
%{_bindir}/flame
%{_libdir}/libflamecore.so
%{_mandir}/man1/flame.1*


%changelog
* Tue Sep 22 2020 Petr Menšík <pemensik@redhat.com> - 0.11.0-1
- Update to 0.11.0

* Fri Aug 07 2020 Petr Menšík <pemensik@redhat.com> - 0.10.2-4
- Update spec to recent cmake macros, fixes rawhide (#1863562)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.2-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Mar 02 2020 Petr Menšík <pemensik@redhat.com> - 0.10.2-1
- Update to 0.10.2

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Oct 07 2019 Petr Menšík <pemensik@redhat.com> - 0.10-3
- Remove explicit library requires

* Wed Oct 02 2019 Petr Menšík <pemensik@redhat.com> - 0.10-2
- Use make install, improve descriptions
- Correct permissions of manual
- Use bindir

* Tue Sep 10 2019 Petr Menšík <pemensik@redhat.com> - 0.10-1
- Initial release



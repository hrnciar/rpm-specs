%global		_hardened_build 1

Name:		libdkimpp
Version:	2.0.0
Release:	6%{?dist}
Summary:	Lightweight and portable DKIM (RFC4871) library

License:	LGPLv3+
URL:		https://github.com/halonsecurity/libdkimpp
Source0:	https://github.com/halonsecurity/libdkimpp/archive/v%{version}.tar.gz

BuildRequires:	cmake
BuildRequires:	coreutils
BuildRequires:	gcc-c++
BuildRequires:	pkgconfig

BuildRequires:	pkgconfig(cppunit)
BuildRequires:	openssl-devel
BuildRequires:	libsodium-devel

%description
libdkim++ is a lightweight and portable DKIM (RFC4871) library for *NIX,
supporting both signing and DMARC/SDID/ADSP verification, sponsored and
used by Halon Security. libdkim++ has extensive unit test coverage and
aims to fully comply with the current RFC.

%package devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the header files and libraries for developing
with %{name}.

%prep
%setup -q

%build
%cmake
%cmake_build

%check
%ctest

%install
%cmake_install

chmod +x $RPM_BUILD_ROOT/%{_libdir}/*.so*

%ldconfig_scriptlets

%files
%license LICENSE
%doc README.md
%{_libdir}/libdkim++.so.*

%files devel
%{_includedir}/libdkim++
%{_libdir}/libdkim++.so
%{_libdir}/pkgconfig/libdkim++.pc


%changelog
* Tue Aug 11 2020 Denis Fateyev <denis@fateyev.com> - 2.0.0-6
- Spec file upgrade and cleanup

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 02 2019 Denis Fateyev <denis@fateyev.com> - 2.0.0-1
- Update to 2.0.0 release

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Mar 21 2017 Denis Fateyev <denis@fateyev.com> - 1.0.10-1
- Update to 1.0.10 release

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed May 25 2016 Denis Fateyev <denis@fateyev.com> - 1.0.9-1
- Update to 1.0.9 release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Dec 10 2015 Denis Fateyev <denis@fateyev.com> - 1.0.8-1
- Initial release

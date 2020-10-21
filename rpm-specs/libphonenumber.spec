Name: libphonenumber
Version: 8.12.8
Release: 2%{?dist}
Summary: Library to handle international phone numbers
# The project itself is ASL 2.0 but contains files from Chromium which are BSD and MIT.
License: ASL 2.0 and BSD and MIT
URL: https://github.com/google/libphonenumber/
Source0: https://github.com/google/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: boost-devel
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: gtest-devel
BuildRequires: libicu-devel
BuildRequires: protobuf-compiler
BuildRequires: protobuf-devel
BuildRequires: re2-devel

%description
Google's common C++ library for parsing, formatting, storing and validating
international phone numbers.


%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1


%build
%cmake cpp
%cmake_build


%install
%cmake_install
find %{buildroot} -name '*.a' -delete
find %{buildroot} -name '*.la' -delete


%files
%doc cpp/README
%license cpp/LICENSE
%{_libdir}/libgeocoding.so.8*
%{_libdir}/libphonenumber.so.8*


%files devel
%{_includedir}/phonenumbers
%{_libdir}/libgeocoding.so
%{_libdir}/libphonenumber.so


%changelog
* Thu Sep 24 2020 Adrian Reber <adrian@lisas.de> - 8.12.8-2
- Rebuilt for protobuf 3.13

* Thu Aug 20 2020 Torrey Sorensen <sorensentor@tuta.io> - 8.12.8-1
- Update to 8.12.8

* Wed Aug 05 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 8.12.7-1
- Update to 8.12.7

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.12.3-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.12.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 14 2020 Adrian Reber <adrian@lisas.de> - 8.12.3-3
- Rebuilt for protobuf 3.12

* Sat May 30 2020 Jonathan Wakely <jwakely@redhat.com> - 8.12.3-2
- Rebuilt for Boost 1.73

* Tue May 19 2020 Nikhil Jha <hi@nikhiljha.com> - 8.12.3-1
- Release 8.12.3

* Tue Mar 31 2020 Nikhil Jha <hi@nikhiljha.com> - 8.12.1-1
- Rebuild for ICU 67

* Tue Mar 31 2020 Nikhil Jha <hi@nikhiljha.com> - 8.12.1-1
- Release 8.12.1

* Wed Mar 25 2020 Nikhil Jha <hi@nikhiljha.com> - 8.12.0-1
- Release 8.12.0

* Fri Dec 27 2019 Anthony Messina <amessina@messinet.com> - 8.11.1-1
- Release 8.11.1

* Sat Oct 05 2019 Anthony Messina <amessina@messinet.com> - 8.10.20-1
- Release 8.10.20

* Wed Jul 31 2019 Anthony Messina <amessina@messinet.com> - 8.10.15-1
- Release 8.10.15

* Fri Apr 19 2019 Anthony Messina <amessina@messinet.com> - 8.10.10-1
- Release 8.10.10

* Sat Feb 16 2019 Anthony Messina <amessina@messinet.com> - 8.10.5-1
- Release 8.10.5

* Fri Oct 26 2018 Anthony Messina <amessina@messinet.com> - 8.9.16-1
- Release 8.9.16

* Sun Aug 19 2018 Anthony Messina <amessina@messinet.com> - 8.9.11-1
- Release 8.9.11
- Refs #100 https://fedoraproject.org/wiki/Changes/Removing_ldconfig_scriptlets
- Refs #103 https://fedoraproject.org/wiki/Changes/Remove_GCC_from_BuildRoot

* Sat Apr 28 2018 Anthony Messina <amessina@messinet.com> - 8.9.4-1
- Release 8.9.4

* Sat Apr 07 2018 Anthony Messina <amessina@messinet.com> - 8.9.3-1
- Release 8.9.3
- https://fedoraproject.org/wiki/Changes/Removing_ldconfig_scriptlets: Refs #100

* Wed Jan 17 2018 Anthony Messina <amessina@messinet.com> - 8.8.9-1
- Initial RPM based on Gil Cattaneo's spec file
  https://gil.fedorapeople.org/libphonenumber.spec
  https://bugzilla.redhat.com/show_bug.cgi?id=1200115

%undefine __cmake_in_source_build

%global intname benchmark
%global lbname lib%{intname}

Name: google-benchmark
Version: 1.5.2
Release: 2%{?dist}

License: ASL 2.0
Summary: A microbenchmark support library
URL: https://github.com/google/%{intname}
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0: google-benchmark-gcc11.patch

BuildRequires: gtest-devel
BuildRequires: gmock-devel
BuildRequires: ninja-build
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: gcc

%description
A library to support the benchmarking of functions, similar to unit-tests.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
%{summary}.

%prep
%autosetup -p1 -n %{intname}-%{version}
sed -e '/get_git_version/d' -i CMakeLists.txt
sed -e 's@/lib@/%{_lib}@g' -i cmake/benchmark.pc.in

%build
%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DGIT_VERSION=%{version} \
    -DBENCHMARK_ENABLE_TESTING:BOOL=OFF \
    -DBENCHMARK_ENABLE_INSTALL:BOOL=ON \
    -DBENCHMARK_DOWNLOAD_DEPENDENCIES:BOOL=OFF
%cmake_build

%check
%ctest

%install
%cmake_install

%files
%doc AUTHORS CONTRIBUTORS CONTRIBUTING.md README.md
%license LICENSE
%{_libdir}/%{lbname}*.so.1*

%files devel
%{_libdir}/%{lbname}*.so
%{_includedir}/%{intname}
%{_libdir}/cmake/%{intname}
%{_libdir}/pkgconfig/%{intname}.pc

%changelog
* Wed Oct 14 2020 Jeff Law <law@redhat.com> - 1.5.2-2
- Fix missing #include for gcc-11

* Sat Sep 12 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 1.5.2-1
- Updated to version 1.5.2.

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jul 19 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 1.5.1-1
- Updated to version 1.5.1.
- Fixed RHBZ#1858127.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 28 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 1.5.0-1
- Updated to version 1.5.0.

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 25 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 1.4.1-1
- Initial SPEC release.

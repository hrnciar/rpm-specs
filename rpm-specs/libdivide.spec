# There are no ELF objects in this package, so turn off debuginfo generation.
%global debug_package %{nil}

Name:           libdivide
Version:        3.0
Release:        3%{?dist}
Summary:        Optimized integer division

License:        zlib or Boost
URL:            http://libdivide.com/
Source0:        https://github.com/ridiculousfish/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++

%global _description %{expand:
This package contains a header-only C/C++ library for optimizing integer
division.  Integer division is one of the slowest instructions on most
CPUs, e.g. on current x64 CPUs a 64-bit integer division has a latency
of up to 90 clock cycles whereas a multiplication has a latency of only
3 clock cycles.  libdivide allows you to replace expensive integer
division instructions by a sequence of shift, add and multiply
instructions that will calculate the integer division much faster.

On current CPUs you can get a speedup of up to 10x for 64-bit integer
division and a speedup of up to to 5x for 32-bit integer division when
using libdivide.  libdivide also supports SSE2, AVX2 and AVX512 vector
division which provides an even larger speedup.}

%description %_description

%package        devel
Summary:        Development files for %{name}
Requires:       cmake-filesystem
Provides:       libdivide-static = %{version}-%{release}

%description    devel %_description

%prep
%autosetup

%build
%cmake
%cmake_build

%install
%cmake_install

%check
%ctest

%files devel
%doc CHANGELOG.md README.md doc
%license LICENSE.txt
%{_includedir}/%{name}.h
%{_libdir}/cmake/%{name}/

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct 16 2019 Jerry James <loganjerry@gmail.com> - 3.0-1
- New upstream version
- Package cannot be noarch due to the cmake files

* Mon Sep 16 2019 Jerry James <loganjerry@gmail.com> - 2.0-1
- Initial RPM

# TESTING NOTE: An OpenCL device is needed to run the tests.  Since the koji
# builders may or may not have a GPU, we use the CPU-only POCL implementation.
# However:
# - POCL is not available on ppc64, ppc64le, or s390x due to failing tests.
# - Builds with POCL on 32-bit ARM fail with an undefined symbol error:
#   __gnu_f2h_ieee.  This symbol is defined in libLLVM, but we are building
#   with gcc/g++, not clang.  Since POCL is built with clang, this appears to
#   be a POCL bug.
# - Builds with POCL on aarch64 fail one DAXPY test, not yet diagnosed.
# That leaves only 32-bit and 64-bit x86 as platforms that can run the tests.

Name:           clblast
Version:        1.5.1
Release:        1%{?dist}
Summary:        Tuned OpenCL BLAS routines

License:        ASL 2.0
URL:            https://cnugteren.github.io/clblast/clblast.html
Source0:        https://github.com/CNugteren/CLBlast/archive/%{version}/%{name}-%{version}.tar.gz
# Fix name clashes between macros in altivec.h and standard types on ppc64le
Patch0:         %{name}-altivec.patch

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  ocl-icd-devel
BuildRequires:  openblas-devel
%ifarch %{ix86} x86_64
BuildRequires:  pocl-devel
# Work around bz 1734850
BuildRequires:  compiler-rt
%endif

%description
CLBlast is a modern, lightweight, performant and tunable OpenCL BLAS
library written in C++11.  It is designed to leverage the full
performance potential of a wide variety of OpenCL devices from different
vendors, including desktop and laptop GPUs, embedded GPUs, and other
accelerators.  CLBlast implements BLAS routines: basic linear algebra
subprograms operating on vectors and matrices.  See the CLBlast website
for performance reports on various devices as well as the latest CLBlast
news.

The library is not tuned for all possible OpenCL devices: if
out-of-the-box performance is poor, please run the tuners first.

%package devel
Summary:        Headers and libraries for CLBlast
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake-filesystem%{?_isa}
Requires:       ocl-icd-devel%{?_isa}

%description devel
Headers and libraries for developing applications that use CLBlast.

%package tuners
Summary:        Tuners for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description tuners
Programs to tune %{name} for your OpenCL device.

%prep
%autosetup -p0 -n CLBlast-%{version}

# Fix the path to the openblas headers
sed -i 's,openblas/include,include/openblas,' cmake/Modules/FindCBLAS.cmake

%build
%cmake -DTESTS:BOOL=ON .
%make_build

%install
%make_install

%ifarch %{ix86} x86_64
%check
make alltests
%endif

%files
%license LICENSE
%doc CHANGELOG CONTRIBUTING.md README.md ROADMAP.md
%{_libdir}/lib{%name}.so.1
%{_libdir}/lib{%name}.so.%{version}

%files devel
%doc doc
%{_includedir}/%{name}*.h
%{_libdir}/lib{%name}.so
%{_libdir}/cmake/CLBLast/
%{_libdir}/pkgconfig/%{name}.pc

%files tuners
%{_bindir}/*

%changelog
* Tue Feb 18 2020 Jerry James <loganjerry@gmail.com> - 1.5.1-1
- Version 1.5.1

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Dec 15 2018 Jerry James <loganjerry@gmail.com> - 1.5.0-1
- New upstream version

* Sat Sep  1 2018 Jerry James <loganjerry@gmail.com> - 1.4.1-1
- Initial RPM

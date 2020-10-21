Name:		teem
Version:	1.11.0
Release:	13%{?dist}
Summary:	Libraries for scientific raster data processing and visualizing

License:	LGPLv2+
URL:		http://teem.sourceforge.net
Source0:	http://downloads.sourceforge.net/project/teem/teem/%{version}/%{name}-%{version}-src.tar.gz
Patch0:		lib_install_dir.patch

BuildRequires:  gcc-c++
BuildRequires:	gcc
BuildRequires:	cmake
BuildRequires:	bzip2-devel
BuildRequires:	fftw-devel
BuildRequires:	libpng-devel
BuildRequires:	zlib-devel

%description
Teem is a coordinated group of libraries for representing, processing,
and visualizing scientific raster data. Teem includes command-line tools
that permit the library functions to be quickly applied to files and streams,
without having to write any code. The most important and useful libraries
in Teem are:

- Nrrd (and the unu command-line tool on top of it) supports a range
  of operations for transforming N-dimensional raster data (resample, crop,
  slice, project, histogram, etc.), as well as the NRRD file format
  for storing arrays and their meta-information.
- Gage: fast convolution-based measurements at arbitrary point locations
  in volume datasets (scalar, vector, tensor, etc.)
- Mite: a multi-threaded ray-casting volume render with transfer functions
  based on any quantity Gage can measure
- Ten: for estimating, processing, and visualizing diffusion tensor fields,
  including fiber tractography methods.


%package libs
Summary:	Libraries for scientific raster data processing and visualizing

%description libs
Teem is a coordinated group of libraries for representing, processing,
and visualizing scientific raster data.

%package devel
Summary:	Libraries for scientific raster data processing and visualizing
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}
Requires:	cmake%{?_isa}

%description devel
Teem is a coordinated group of libraries for representing, processing,
and visualizing scientific raster data. This package contains development
files.


%prep
%autosetup -n %{name}-%{version}-src -p1


%build
%cmake \
    -DCMAKE_SKIP_INSTALL_RPATH=ON \
    -DTeem_USE_LIB_INSTALL_SUBDIR=ON \
    -DTeem_FFTW3=ON \
%cmake_build


%install
%cmake_install

%check
# tests fail on 32-bit arches
# seems that computation accuracy is arch-dependant
%global _smp_mflags -j1
%ifarch x86_64
%ctest
%endif

%ldconfig_scriptlets libs

%files
%doc README.txt
%{_bindir}/*

%files libs
%license LICENSE.txt
%{_libdir}/libteem.so.*

%files devel
%doc Examples/sanity/
%{_includedir}/teem/
%{_libdir}/libteem.so
%{_libdir}/cmake/Teem-%{version}/


%changelog
* Fri Sep 04 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.11.0-13
- Use cmake macros to fix build

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-12
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Nov 25 2015 Dmitry Mikhirev <mikhirev@gmail.com> 1.11.0-1
- Initial package

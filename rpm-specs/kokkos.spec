Name:           kokkos
Version:        3.1.01
%global         sover 3.1.1
Release:        1%{?dist}
Summary:        Kokkos C++ Performance Portability Programming 
#no support for 32-bit archs https://github.com/kokkos/kokkos/issues/2312
ExcludeArch: i686 armv7hl

License:        BSD 
URL:            https://github.com/kokkos/kokkos
Source0:        https://github.com/kokkos/kokkos/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake3 >= 3.0
BuildRequires:  hwloc-devel

%global kokkos_desc \
Kokkos Core implements a programming model in C++ for writing performance \
portable applications targeting all major HPC platforms. For that purpose \
it provides abstractions for both parallel execution of code and data \
management.  Kokkos is designed to target complex node architectures with \
N-level memory hierarchies and multiple types of execution resources. It \
currently can use OpenMP, Pthreads and CUDA as backend programming models.

%description
%{kokkos_desc}

%package devel
Summary:        Development package for  %{name} packages
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       hwloc-devel
%description devel
%{kokkos_desc}

This package contains the development files of %{name}.

%prep
%setup -q

%build
mkdir build
pushd build

%{cmake3} \
  -DKokkos_ENABLE_TESTS=On \
  -DCMAKE_INSTALL_INCLUDEDIR=include/kokkos \
  -DKokkos_ENABLE_AGGRESSIVE_VECTORIZATION=ON \
  -DKokkos_ENABLE_DEPRECATED_CODE=ON \
  -DKokkos_ENABLE_OPENMP=ON \
  -DKokkos_ENABLE_SERIAL=ON \
  -DKokkos_ENABLE_HWLOC=ON \
  ..
%make_build
popd

%install
%make_install -C build

%check
make -C build test CTEST_OUTPUT_ON_FAILURE=1 %{?testargs}

%files
%doc README.md
%license LICENSE
%{_libdir}/libkokkos*.so.%{sover}

%files devel
%{_libdir}/libkokkos*.so
%{_libdir}/cmake/Kokkos
%{_includedir}/kokkos
%{_bindir}/nvcc_wrapper

%changelog
* Wed May 06 2020 Christoph Junghans <junghans@votca.org> - 3.1.01-1
- Version bump to v3.1.01 (bug #1824998)
- drop 2961.patch - merge upstream

* Thu Apr 16 2020 Christoph Junghans <junghans@votca.org> - 3.1.00-1
- Version bump to v3.1.00 (bug #1824998)

* Thu Feb 27 2020 Christoph Junghans <junghans@votca.org> - 3.0.00-1
- Version bump to 3.0.00

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-0.3.20200107gite79d6b7.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 15 2020 Christoph Junghans <junghans@votca.org> - 3.0.0-0.2.20200107gite79d6b7.1
- Added missing hwloc dep

* Sun Jan 12 2020 Christoph Junghans <junghans@votca.org> - 3.0.0-0.2.20200107gite79d6b7
- bump to latest release candidate snapshot

* Mon Dec 23 2019 Christoph Junghans <junghans@votca.org> - 3.0.0-0.2.20191219gitcb90e9
- bump to latest release candidate snapshot

* Fri Dec 20 2019 Christoph Junghans <junghans@votca.org> - 3.0.0-0.2.20191216git6619d83
- bump to latest snapshot and enable Kokkos_ENABLE_DEPRECATED_CODE
- disable StackTrace Unittests

* Sun Sep 29 2019 Christoph Junghans <junghans@votca.org> - 3.0.0-0.2.20190929git445c176
- bump to latest snapshot and enable AGGRESSIVE_VECTORIZATION

* Wed Sep 18 2019 Christoph Junghans <junghans@votca.org> - 3.0.0-0.1.190912gitd93e239
- initial commit (bug #1751409)

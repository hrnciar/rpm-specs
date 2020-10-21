Summary:        A lightweight C++ utility library
Name:           elements-alexandria
Version:        2.16
Release:        3%{?dist}
License:        LGPLv3+
URL:            https://github.com/astrorama/Alexandria.git
Source0:        https://github.com/astrorama/Alexandria/archive/%{version}/%{name}-%{version}.tar.gz
# This file is used to link the documentation to cppreference.com
# It is downloaded from:
# https://upload.cppreference.com/w/File:cppreference-doxygen-web.tag.xml
Source1:        cppreference-doxygen-web.tag.xml
# Fix a bad memory access when fixing an axis
Patch0:         elements-alexandria_fixaxis.patch
# Fixes for failing tests on architectures other than x86_64
Patch1:         elements-alexandria_arch.patch

%global elements_version 5.10

BuildRequires: CCfits-devel
BuildRequires: boost-devel >= 1.53
BuildRequires: cfitsio-devel
BuildRequires: cppunit-devel
BuildRequires: elements-devel = %{elements_version}
BuildRequires: log4cpp-devel
# Required for the generation of the documentation
BuildRequires: elements-doc = %{elements_version}
BuildRequires: doxygen
BuildRequires: graphviz
BuildRequires: texlive-latex
%if 0%{?fedora} >= 30
BuildRequires: texlive-newunicodechar
%endif
BuildRequires: texlive-dvips

BuildRequires: gcc-c++ > 4.7
BuildRequires: cmake >= 2.8.5
%if 0%{?fedora} >= 30
BuildRequires: python3
BuildRequires: python3-pytest
BuildRequires: python3-devel
%else
BuildRequires: python2
BuildRequires: python2-pytest
BuildRequires: python2-devel
%endif

%if 0%{?rhel} && 0%{?rhel} <= 7
Requires: cmake%{?_isa}
%else
Requires: cmake-filesystem%{?_isa}
%endif

%global cmakedir %{_libdir}/cmake/ElementsProject

%global makedir %{_datadir}/Elements/make
%global confdir %{_datadir}/Elements
%global auxdir %{_datadir}/auxdir
%global docdir %{_docdir}/Alexandria

%if 0%{?fedora} >= 30
%global python_sitearch %{python3_sitearch}
%else
%global python_sitearch %{python2_sitearch}
%endif

%description
A lightweight C++ utility library.

%package devel
Summary: The development part of the %{name} package
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: elements-devel%{?_isa} = %{elements_version}

%description devel
The development part of the %{name} package.

%package doc
Summary: Documentation for package %{name}
License: LGPLv3+ and CC-BY-SA
BuildArch: noarch
Requires: elements-doc = %{elements_version}

%description doc
Documentation for package %{name}

%prep
%autosetup -n Alexandria-%{version} -p1

%build
export VERBOSE=1
EXTRA_CMAKE_FLAGS="-DUSE_ENV_FLAGS=ON"
%if 0%{?fedora} >= 30
EXTRA_CMAKE_FLAGS="${EXTRA_CMAKE_FLAGS} -DPYTHON_EXPLICIT_VERSION=3"
%else
EXTRA_CMAKE_FLAGS="${EXTRA_CMAKE_FLAGS} -DPYTHON_EXPLICIT_VERSION=2"
%endif
# Build
%cmake -B "%{_vpath_builddir}" -DELEMENTS_BUILD_TESTS=ON -DELEMENTS_INSTALL_TESTS=OFF -DSQUEEZED_INSTALL:BOOL=ON -DINSTALL_DOC:BOOL=ON \
    -DUSE_SPHINX=OFF --no-warn-unused-cli \
    -DCMAKE_LIB_INSTALL_SUFFIX=%{_lib} -DUSE_VERSIONED_LIBRARIES=ON ${EXTRA_CMAKE_FLAGS}
# Copy cppreference-doxygen-web.tag.xml into the build directory
mkdir -p "%{_vpath_builddir}/doc/doxygen"
cp -v "%{SOURCE1}" "%{_vpath_builddir}/doc/doxygen"

%make_build -C "%{_vpath_builddir}"

%install
export VERBOSE=1
%make_install -C "%{_vpath_builddir}"

%check
make test -C "%{_vpath_builddir}"

%files
%license LICENSE
%{cmakedir}/AlexandriaEnvironment.xml

%{_libdir}/libAlexandriaKernel.so.%{version}
%{_libdir}/libConfiguration.so.%{version}
%{_libdir}/libGridContainer.so.%{version}
%{_libdir}/libHistogram.so.%{version}
%{_libdir}/libNdArray.so.%{version}
%{_libdir}/libMathUtils.so.%{version}
%{_libdir}/libPhysicsUtils.so.%{version}
%{_libdir}/libSOM.so.%{version}
%{_libdir}/libSourceCatalog.so.%{version}
%{_libdir}/libTable.so.%{version}
%{_libdir}/libXYDataset.so.%{version}

%{python_sitearch}/ALEXANDRIA_VERSION.py*
%{python_sitearch}/ALEXANDRIA_INSTALL.py*
%if 0%{?fedora} >= 30
%{python_sitearch}/__pycache__/ALEXANDRIA*.pyc
%endif

%files devel
%{_libdir}/libAlexandriaKernel.so
%{_libdir}/libConfiguration.so
%{_libdir}/libGridContainer.so
%{_libdir}/libHistogram.so
%{_libdir}/libNdArray.so
%{_libdir}/libMathUtils.so
%{_libdir}/libPhysicsUtils.so
%{_libdir}/libSOM.so
%{_libdir}/libSourceCatalog.so
%{_libdir}/libTable.so
%{_libdir}/libXYDataset.so

%{_includedir}/ALEXANDRIA_VERSION.h
%{_includedir}/ALEXANDRIA_INSTALL.h
%{_includedir}/AlexandriaKernel/
%{_includedir}/Table/
%{_includedir}/XYDataset/
%{_includedir}/GridContainer/
%{_includedir}/Histogram/
%{_includedir}/NdArray/
%{_includedir}/SourceCatalog/
%{_includedir}/Configuration/
%{_includedir}/MathUtils/
%{_includedir}/PhysicsUtils/
%{_includedir}/SOM/

%{cmakedir}/AlexandriaBuildEnvironment.xml
%{cmakedir}/AlexandriaExports.cmake
%{cmakedir}/AlexandriaExports-relwithdebinfo.cmake
%{cmakedir}/AlexandriaPlatformConfig.cmake
%{cmakedir}/AlexandriaKernelExport.cmake
%{cmakedir}/TableExport.cmake
%{cmakedir}/XYDatasetExport.cmake
%{cmakedir}/GridContainerExport.cmake
%{cmakedir}/HistogramExport.cmake
%{cmakedir}/NdArrayExport.cmake
%{cmakedir}/SourceCatalogExport.cmake
%{cmakedir}/ConfigurationExport.cmake
%{cmakedir}/MathUtilsExport.cmake
%{cmakedir}/PhysicsUtilsExport.cmake
%{cmakedir}/SOMExport.cmake
%{cmakedir}/AlexandriaConfigVersion.cmake
%{cmakedir}/AlexandriaConfig.cmake

%files doc
%license LICENSE
%{docdir}

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.16-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 17 2020 Alejandro Alvarez Ayllon <alejandro.alvarezayllon@unige.ch> 2.16-1
- New upstream release 2.16

* Thu May 28 2020 Jonathan Wakely <jwakely@redhat.com> - 2.14.1-7
- Rebuilt for Boost 1.73

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.14.1-6
- Rebuilt for Python 3.9

* Wed Feb 26 2020 Alejandro Alvarez Ayllon <a.alvarezayllon@gmail.com> - 2.14.1-5
- Rebuild for Fedora 33

* Mon Feb 03 2020 Alejandro Alvarez Ayllon <a.alvarezayllon@gmail.com> - 2.14.1-4
- Rebuild for elements 5.8-6

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 13 2020 Alejandro Alvarez Ayllon <alejandro.alvarezayllon@unige.ch> 2.14.1-2
- Fix conditional dependency on cmake-filesystem
- Add LICENSE file to the main package

* Fri Jan 10 2020 Alejandro Alvarez Ayllon <alejandro.alvarezayllon@unige.ch> 2.14.1-1
- Initial RPM

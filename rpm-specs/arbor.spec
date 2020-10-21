%global _description %{expand:
Arbor is a high-performance library for Computational Neuroscience simulations.

Some key features include:

- Asynchronous spike exchange that overlaps compute and communication.
- Efficient sampling of voltage and current on all back ends.
- Efficient implementation of all features on GPU.
- Reporting of memory and energy consumption (when available on platform).
- An API for addition of new cell types, e.g. LIF and Poisson spike generators.
- Validation tests against numeric/analytic models and NEURON.

Documentation is available at https://arbor.readthedocs.io/en/latest/
}

# Best to start with the serial version when debugging build failures
%bcond_without mpich
%bcond_without openmpi

%bcond_without tests

#%%global commit  fb5d4ea736282dce14c3284bc5db748b082db957
#%%global checkoutdate  20200225
#%%global shortcommit %%(c=%%{commit}; echo ${c:0:7})

Name:           arbor
Version:        0.3
Release:        7%{?dist}
Summary:        Multi-compartment neural network simulation library

License:        BSD
URL:            https://github.com/arbor-sim/%{name}
%if 0%{?commit:1}
Source0:        %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
%else
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
%endif
# Use the system copy of pybind11
# https://github.com/arbor-sim/arbor/issues/915
Patch0:         %{name}-0001-Use-system-pybind11.patch

# This patch changes ext/CMakeLists.txt for automatically using tinyopt libraries by cmake command.
Patch1:         %{name}-tinyopt_cmake.patch

# Random123 does not support these
ExcludeArch:    mips64r2 mips32r2 s390 s390x

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  gtest-devel
BuildRequires:  json-devel
BuildRequires:  libunwind-devel
BuildRequires:  pybind11-devel
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  Random123-devel
BuildRequires:  tclap-devel
Provides:       python3-%{name} = %{version}-%{release}
%{?python_provide:%python_provide python3-%{name}}
# For validation, but we don't have these BRs
# BuildRequires:  julia julia-sundials julia-unitful julia-JSON

%description %{_description}

%package devel
Summary:    Development files for %{name}
Requires:   %{name}%{?_isa} = %{version}-%{release}
Provides:   %{name}-static = %{version}-%{release}

%description devel %{_description}

%package doc
# Does not require the main package, since it may be installed by people using
# the MPI builds
Summary:    Documentation for %{name}
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme

%description doc %{_description}

%if %{with mpich}
%package mpich
Summary:        MPICH build for %{name}
BuildRequires:  mpich-devel
BuildRequires:  rpm-mpi-hooks
BuildRequires:  python3-mpi4py-mpich

Requires:       mpich
Requires:       python3-mpich
Requires:       python3-mpi4py-mpich
Provides:       python3-%{name}-mpich = %{version}-%{release}
%{?python_provide:%python_provide python3-%{name}-mpich}

%description mpich %{_description}

%package mpich-devel
Summary:    Development files for %{name}-mpich
Requires:   %{name}-mpich%{?_isa} = %{version}-%{release}
Provides:   %{name}-mpich-static = %{version}-%{release}

%description mpich-devel %{_description}
%endif

%if %{with openmpi}
%package openmpi
Summary:        OpenMPI build for %{name}
BuildRequires:  openmpi-devel
BuildRequires:  rpm-mpi-hooks
BuildRequires:  python3-mpi4py-openmpi

Requires:       openmpi
Requires:       python3-openmpi
Requires:       python3-mpi4py-openmpi
Provides:       python3-%{name}-openmpi = %{version}-%{release}
%{?python_provide:%python_provide python3-%{name}-openmpi}

%description openmpi %{_description}

%package openmpi-devel
Summary:    Development files for %{name}-openmpi
Requires:   %{name}-openmpi%{?_isa} = %{version}-%{release}
Provides:   %{name}-openmpi-static = %{version}-%{release}

%description openmpi-devel %{_description}
%endif

%prep
%if 0%{?commit:1}
%autosetup -n %{name}-%{commit} -S git
%else
%autosetup -p1
%endif

# Do not build external libraries
# tclap and json and random123
sed -i -e 's/ ext-random123//' CMakeLists.txt
# Remove ext folders, unbundle libraries
rm -vrf ext/google-benchmark ext/json ext/random123 ext/sphinx_rtd_theme
mv ext/tinyopt/LICENSE ext/tinyopt/LICENSE-tinyopt
# Disable doc build: we built it ourselves
sed -i '/add_subdirectory(doc)/ d' CMakeLists.txt
# tclap and json are both header only
find . -type f -name "CMakeLists.txt" -exec sed -i -e 's/ext-tclap//' -e 's/ext-json//' {} 2>/dev/null ';'

# Correct Python shebangs in all files
find . -type f -name "*" -exec sed -i 's|^#![  ]*/usr/bin/env.*python.*$|#!/usr/bin/python3|' {} 2>/dev/null ';'
# We set it, remove the hard coded bits from CMakeLists.txt
sed -i '/set(arb_pyexecdir/ d' python/CMakeLists.txt

# builddir for serial
mkdir build-serial

%if %{with mpich}
    mkdir build-mpich
%endif

%if %{with openmpi}
    mkdir build-openmpi
%endif

%build
# Best to use && so that if anything in the chain fails, the build also fails
# straight away
%global do_cmake_config %{expand: \
echo
echo "*** BUILDING %{name}-%{version}$MPI_COMPILE_TYPE ***"
echo
pushd build$MPI_COMPILE_TYPE  &&
    cmake \\\
        -DCMAKE_C_FLAGS_RELEASE:STRING="-DNDEBUG" \\\
        -DCMAKE_CXX_FLAGS_RELEASE:STRING="-DNDEBUG" \\\
        -DCMAKE_Fortran_FLAGS_RELEASE:STRING="-DNDEBUG" \\\
        -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \\\
        -DCMAKE_INSTALL_PREFIX:PATH=$MPI_HOME \\\
        -DINCLUDE_INSTALL_DIR:PATH=$MPI_INCLUDE \\\
        -DLIB_INSTALL_DIR:PATH=$MPI_LIB \\\
        -DSYSCONF_INSTALL_DIR:PATH=%{_sysconfdir} \\\
        -DSHARE_INSTALL_PREFIX:PATH=%{_datadir} \\\
        -DCMAKE_SKIP_RPATH:BOOL=ON \\\
        -DCMAKE_BUILD_TYPE:STRING="release" \\\
%ifarch x86_64 i686 aarch64
        -DARB_VECTORIZE:BOOL=ON \\\
%else
        -DARB_VECTORIZE:BOOL=OFF \\\
%endif
%ifarch %{power64}
        -DARB_ARCH=power8 \\\
%endif
        -DARB_WITH_MPI:BOOL=$MPI_YES \\\
        -DARB_WITH_GPU:BOOL=OFF \\\
%ifnarch armv7hl
        -DARB_ARCH:STRING="native" \\\
%endif
        -DCMAKE_INSTALL_LIBDIR=%{_lib} \\\
        -DARB_WITH_PYTHON:BOOL=ON \\\
        -Darb_pyexecdir:STRING=$MPI_PYTHON3_SITEARCH \\\
%if "%{_lib}" == "lib64"
        -DLIB_SUFFIX=64 .. &&
%else
        -DLIB_SUFFIX=""  .. &&
%endif
popd || exit -1;

# Upstream only supports static libraries
# https://github.com/arbor-sim/arbor/issues/916
# -DBUILD_SHARED_LIBS:BOOL=ON \\\
# Missing BRs
# -DARB_BUILD_VALIDATION_DATA:BOOL=ON \\\
}

%global do_make_build %{expand: \
    %make_build -C build$MPI_COMPILE_TYPE || exit -1
    %make_build -C build$MPI_COMPILE_TYPE tests || exit -1
}

# Build serial version, dummy arguments
%global __cc gcc
%global __cxx g++
%set_build_flags
export MPI_SUFFIX=""
export MPI_HOME=%{_prefix}
export MPI_INCLUDE=%{_includedir}
export MPI_LIB=%{_libdir}
export MPI_YES=OFF
export MPI_COMPILE_TYPE="-serial"
export MPI_PYTHON3_SITEARCH=%{python3_sitearch}
%{do_cmake_config}
%{do_make_build}

# Manually make docs in the serial build
sphinx-build-%{python3_version} -b html doc html
# Remove uneeded dotfiles
rm -rfv html/{.buildinfo,.doctrees}


# Build mpich version
%if %{with mpich}
%{_mpich_load}
%global __cc mpicc
%global __cxx mpicxx
%set_build_flags
export CC=mpicc
export CXX=mpicxx
export FC=mpif90
export F77=mpif77
export MPI_YES=ON
export MPI_COMPILE_TYPE="-mpich"
%{do_cmake_config}
%{do_make_build}

%{_mpich_unload}
%endif

# Build OpenMPI version
%if %{with openmpi}
%{_openmpi_load}
%global __cc mpicc
%global __cxx mpicxx
%set_build_flags
export CC=mpicc
export CXX=mpicxx
export FC=mpif90
export F77=mpif77
export MPI_YES=ON
# Python 3
export MPI_COMPILE_TYPE="-openmpi"
%{do_cmake_config}
%{do_make_build}

%{_openmpi_unload}
%endif

%install
# Install everything
%global do_install %{expand: \
echo
echo "*** INSTALLING %{name}-%{version}$MPI_COMPILE_TYPE ***"
echo
    %make_install -C build$MPI_COMPILE_TYPE || exit -1
}

# install serial version
export MPI_SUFFIX=""
export MPI_HOME=%{_prefix}
export MPI_BIN=%{_bindir}
export MPI_YES=OFF
export MPI_COMPILE_TYPE="-serial"
%{do_install}


# Install MPICH version
%if %{with mpich}
%{_mpich_load}
export MPI_COMPILE_TYPE="-mpich"
%{do_install}

# Place in correct mpi libdir
%if "%{_lib}" == "lib64"
    mv -v $RPM_BUILD_ROOT/%{_libdir}/mpich/lib64 $RPM_BUILD_ROOT/$MPI_LIB/
%endif

pushd $RPM_BUILD_ROOT/$MPI_BIN
    mv -v modcc{,$MPI_SUFFIX} -v
popd
%{_mpich_unload}
%endif

# Install OpenMPI version
%if %{with openmpi}
%{_openmpi_load}
export MPI_COMPILE_TYPE="-openmpi"
%{do_install}

# Correct location
%if "%{_lib}" == "lib64"
    mv -v $RPM_BUILD_ROOT/%{_libdir}/openmpi/lib64 $RPM_BUILD_ROOT/$MPI_LIB/
%endif

pushd $RPM_BUILD_ROOT/$MPI_BIN
    mv -v modcc{,$MPI_SUFFIX} -v
popd
%{_openmpi_unload}
%endif


%if %{with tests}
%check
# Run for serial only. our builders are not using MPI
# these tests segfault, filter out
pushd build-serial
    ./bin/unit --gtest_filter=-*mc_event_delivery*:*fvm_lowered*:*mc_cell_group*
popd
%endif


%files
%license LICENSE ext/tinyopt/LICENSE-tinyopt
%doc README.md
%{_bindir}/modcc
%{python3_sitearch}/%{name}


%files devel
%{_includedir}/%{name}
%{_includedir}/%{name}env
%{_libdir}/cmake/%{name}
%{_libdir}/libarbor.a
%{_libdir}/libarborenv.a

%files doc
%license LICENSE
%doc html


%if %{with mpich}
%files mpich
%doc README.md
%license LICENSE ext/tinyopt/LICENSE-tinyopt
%{_libdir}/mpich/bin/modcc_mpich
%{python3_sitearch}/mpich/%{name}

%files mpich-devel
%{_libdir}/mpich/include/%{name}
%{_libdir}/mpich/include/%{name}env
%{_libdir}/mpich/lib/cmake/%{name}
%{_libdir}/mpich/lib/libarbor.a
%{_libdir}/mpich/lib/libarborenv.a
%endif

%if %{with openmpi}
%files openmpi
%doc README.md
%license LICENSE ext/tinyopt/LICENSE-tinyopt
%{_libdir}/openmpi/bin/modcc_openmpi
%{python3_sitearch}/openmpi/%{name}

%files openmpi-devel
%{_libdir}/openmpi/include/%{name}
%{_libdir}/openmpi/include/%{name}env
%{_libdir}/openmpi/lib/cmake/%{name}
%{_libdir}/openmpi/lib/libarbor.a
%{_libdir}/openmpi/lib/libarborenv.a
%endif

%changelog
* Mon Oct 05 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.3-7
- Explicitly require setuptools

* Fri Aug 28 2020 Jeff Law <law@redhat.com> - 0.3-6
- Re-enable LTO
- Do not force -march=native on armv7hl so that build architecture does not bleed
  into the binaries.  This should probably be done on all targets

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Jeff Law <law@redhat.com> - 0.3-4
- Disable LTO for armv7hl build

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 28 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.3-2
- Update build flags to ensure CC and CXX are set correctly
- https://lists.fedoraproject.org/archives/list/scitech@lists.fedoraproject.org/thread/BNKLXKY4O7BOTZ7LH7XDUTQO6FG2UWUT/#BNKLXKY4O7BOTZ7LH7XDUTQO6FG2UWUT

* Mon Jun 08 2020 Antonio Trande <sagitter@fedoraproject.org> - 0.3-2
- Move Provides lines to runtime packages
- Add patch for using tinyopt libraries

* Sat Jun 06 2020 Antonio Trande <sagitter@fedoraproject.org> - 0.3-1
- Release 0.3

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.2-8.20200225gitfb5d4ea736282dce14c3284bc5db748b082db957
- Rebuilt for Python 3.9

* Thu Apr 02 2020 Björn Esser <besser82@fedoraproject.org> - 0.2.2-7.20200225gitfb5d4ea736282dce14c3284bc5db748b082db957
- Fix string quoting for rpm >= 4.16

* Wed Feb 26 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.2.2-5.20200226gitfb5d4ea736282dce14c3284bc5db748b082db957
- Use new snapshot that fixes errors on 32 bit systems
- No longer excludes i686 and armv7hl
- Drop unneeded patch.

* Sun Feb 23 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.2.2-5.20200223gitf12f934f365d9e68f01bfd857982be80da2ddd10
- Build from latest upstream snapshot
- Freshen patch
- Add exclude arches

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Dec 10 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.2.2-3
- Enable tests
- Add patch for test crash

* Mon Dec 09 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.2.2-2
- Remove arch info in provides for static
- Temporarily disable tests
- use python3-devel
- Add documentation in separate sub-package
- add python3-{mpich,openmpi} as requires that own MPI_PYTHON3_SITEARCH directories
- Improve summaries for sub-packages to please rpmlint

* Sat Dec 07 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.2.2-1
- Update to latest release

* Sun Jan 13 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.1-1
- Initial rpm package

# We build the python bit separately - their build system doesn't let me build
# and install separately - everything is done at install time

# We do not build the developer documentation with doxygen. Advanced developers
# that develop based on the source git tree can build it themselves
# Switch them off if you want
%bcond_without mpich
%bcond_without openmpi

# Tests include source linters and so on, and require a specific older version
# of vera and clang and so forth, so we simply rely on upstream CI here
%bcond_with tests

Name:           nest
Version:        2.20.0

%global gittag v%{version}

Release:        5%{?dist}
Summary:        The neural simulation tool

License:        GPLv2+
URL:            http://www.nest-simulator.org/
Source0:        https://github.com/%{name}/%{name}-simulator/archive/%{gittag}/%{name}-%{version}.tar.gz
Source1:        README-Fedora.md

# 1. Let it build and install the cythonised shared object But we still build
# our python modules ourselves

# 2. The helpindex must be generated after the help files have been installed
# to the install location, so we do this manually because the script doesn't
# respect rpmbuildroot and so on
# Patch0:         %%{name}-0000-disable-pybits.patch
Patch0:         0001-Disable-python-setups.patch


BuildRequires:  ncurses-devel
BuildRequires:  gsl-devel
BuildRequires:  readline-devel
BuildRequires:  python3-devel
BuildRequires:  python3-Cython
BuildRequires:  python3-nose
BuildRequires:  libtool-ltdl-devel
BuildRequires:  cmake
BuildRequires:  libtool
BuildRequires:  doxygen
BuildRequires:  graphviz
BuildRequires:  gcc-c++
BuildRequires:  libneurosim-devel
Requires:       %{name}-common

%global _description %{expand:
NEST is a simulator for spiking neural network models that focuses on the
dynamics, size and structure of neural systems rather than on the exact
morphology of individual neurons. The development of NEST is coordinated by the
NEST Initiative.  NEST is ideal for networks of spiking neurons of any size,
for example: Models of information processing e.g. in the visual or auditory
cortex of mammals; Models of network activity dynamics, e.g. laminar cortical
networks or balanced random networks; Models of learning and plasticity.
Please read the README-Fedora.md file provided in each package for information
on how these NEST packages are to be used.

Documentation is available separately in the nest-doc package.
}

%description %_description

%package common
BuildArch:  noarch
Summary:    Common files for %{name}

%description common %_description

%package headers
BuildArch:  noarch
Summary:    Header files for %{name}

%description headers %_description

%package doc
BuildArch:  noarch
Summary:    Documentation for %{name}

%description doc %_description


%package -n python3-%{name}
Summary:    Python3 bindings for nest
Requires:   %{name} = %{version}-%{release}
Requires:   %{name}-common = %{version}-%{release}
Requires:   %{py3_dist numpy} %{py3_dist scipy}
Recommends: %{py3_dist matplotlib}
Recommends: %{py3_dist ipython}
%{?python_provide:%python_provide python3-%{name}}

%description -n python3-%{name} %_description

%if %{with openmpi}
%package openmpi
Summary:        %{name} built with openmpi
BuildRequires:  openmpi-devel
BuildRequires:  rpm-mpi-hooks
BuildRequires:  libneurosim-openmpi-devel
BuildRequires:  MUSIC-openmpi-devel
BuildRequires:  MUSIC-openmpi
Requires:       openmpi
Requires:       %{name}-openmpi-common = %{version}-%{release}

%description openmpi %_description

%package openmpi-common
Summary:    Common files for %{name} built with openmpi support

%description openmpi-common %_description

%package openmpi-headers
Summary:    Header files for %{name} built with openmpi support

%description openmpi-headers %_description

%package -n python3-%{name}-openmpi
Summary:    Python3 bindings for nest with openmpi support
BuildRequires:  rpm-mpi-hooks
Requires:   openmpi
Requires:   %{name}-openmpi = %{version}-%{release}
Requires:   %{name}-openmpi-common = %{version}-%{release}
Requires:   %{py3_dist numpy} %{py3_dist scipy}
Recommends: %{py3_dist matplotlib}
Recommends: %{py3_dist ipython}
%{?python_provide:%python_provide python3-%{name}-openmpi}

%description -n python3-%{name}-openmpi %_description
%endif

%if %{with mpich}
%package mpich
Summary:        %{name} built with mpich
BuildRequires:  mpich-devel
BuildRequires:  rpm-mpi-hooks
BuildRequires:  libneurosim-mpich-devel
BuildRequires:  MUSIC-mpich-devel
BuildRequires:  MUSIC-mpich
Requires:       mpich
Requires:       %{name}-mpich-common = %{version}-%{release}

%description mpich %_description

%package mpich-common
Summary:    Common files for %{name} built with mpich support

%description mpich-common %_description

%package mpich-headers
Summary:    Header files for %{name} built with mpich support

%description mpich-headers %_description


%package -n python3-%{name}-mpich
Summary:    Python3 bindings for nest with mpich support
BuildRequires:  rpm-mpi-hooks
Requires:   %{name}-mpich = %{version}-%{release}
Requires:   %{name}-mpich-common = %{version}-%{release}
Requires:   mpich
Requires:   %{py3_dist numpy} %{py3_dist scipy}
Recommends: %{py3_dist matplotlib}
Recommends: %{py3_dist ipython}
%{?python_provide:%python_provide python3-%{name}-mpich}

%description -n python3-%{name}-mpich %_description
%endif

%prep
%autosetup -c -n %{name}-simulator-%{version} -N
cp %{SOURCE1} ./ -v
cp %{name}-simulator-%{version}/LICENSE . -v

# Tweaks
pushd %{name}-simulator-%{version}
# Apply the patch
%patch0 -p1
# We'll set it ourselves - easier for mpi implementations
sed -i.orig '/PYEXECDIR/ d' cmake/ProcessOptions.cmake
# These files are all in standard locations so we don't need them
# Loading an MPI module sets up PATH correctly
sed -i '/PATH=/ d' extras/nest_vars.sh.in
# Set the correct PYTHONPATH using nest_vars.sh
# loading an MPI module DOES NOT seem to set the python path
sed -i 's|NEST_PYTHON_PREFIX=$NEST_INSTALL_DIR/@PYEXECDIR@|NEST_PYTHON_PREFIX=@PYEXECDIR@|' extras/nest_vars.sh.in
popd

# Find py3 version of libneurosim in the py3 builds/packages
sed -i 's/pyneurosim/py3neurosim/' %{name}-simulator-%{version}/cmake/FindLibNeurosim.cmake

# Correct shebangs for py3
find %{name}-simulator-%{version}/ -name "*.py" -exec sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' '{}' \;

%if %{with mpich}
    cp -a %{name}-simulator-%{version} %{name}-simulator-%{version}-mpich

    # Don't generate docs for each build
    sed -i '/add_subdirectory.*doc/ d' %{name}-simulator-%{version}-mpich/CMakeLists.txt
    # Don't install examples and extras for each
    sed -i '/add_subdirectory.*examples/ d' %{name}-simulator-%{version}-mpich/CMakeLists.txt
    # Don't install tests in docdir either
    sed -i '/add_subdirectory.*testsuite/ d' %{name}-simulator-%{version}-mpich/CMakeLists.txt
%endif

%if %{with openmpi}
    cp -a %{name}-simulator-%{version} %{name}-simulator-%{version}-openmpi

    # Don't generate docs for these
    sed -i '/add_subdirectory.*doc/ d' %{name}-simulator-%{version}-openmpi/CMakeLists.txt
    # Don't install examples and extras for each
    sed -i '/add_subdirectory.*examples/ d' %{name}-simulator-%{version}-openmpi/CMakeLists.txt
    # Don't install tests in docdir either
    sed -i '/add_subdirectory.*testsuite/ d' %{name}-simulator-%{version}-openmpi/CMakeLists.txt
%endif

%build
# On armv7 we get a failure with LTO.  The log has no useful information in it
# but my guess is we ran out of memory on the builder.  Disable LTO for armv7
%ifarch armv7hl
%define _lto_cflags %{nil}
%endif

%set_build_flags

%global do_cmake_config \
echo  \
echo "*** BUILDING %{name}-simulator-%{version}$MPI_COMPILE_TYPE ***"  \
echo  \
export PYEXECDIR=$MPI_SITEARCH  \
export PYNEST_CFLAGS="%{optflags}"  \
export PYNEST_CXXFLAGS="%{optflags}"  \
%set_build_flags \
pushd %{name}-simulator-%{version}$MPI_COMPILE_TYPE  && \
    cmake \\\
        -DCMAKE_C_FLAGS_RELEASE:STRING="-DNDEBUG" \\\
        -DCMAKE_CXX_FLAGS_RELEASE:STRING="-DNDEBUG" \\\
        -DCMAKE_Fortran_FLAGS_RELEASE:STRING="-DNDEBUG" \\\
        -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \\\
        -DCMAKE_INSTALL_INCLUDEDIR:PATH=$MPI_INCLUDE \\\
        -DCMAKE_INSTALL_LIBDIR:PATH=$MPI_LIB \\\
        -DSYSCONF_INSTALL_DIR:PATH=%{_sysconfdir} \\\
        -DSHARE_INSTALL_PREFIX:PATH=%{_datadir} \\\
        -DCMAKE_SKIP_RPATH:BOOL=ON \\\
        -Dwith-mpi:BOOL=$MPI_YES \\\
        -Dwith-gsl:BOOL=ON \\\
        -Dwith-libneurosim:PATH=$MPI_HOME \\\
        -Dwith-python:STRING=$PYTHON_VERSION  \\\
        -DPYEXECDIR:PATH=$MPI_SITEARCH \\\
        -DCMAKE_INSTALL_PREFIX:PATH=$MPI_HOME \\\
        -DBUILD_SHARED_LIBS:BOOL=ON \\\
%if %{music} \
        -Dwith-music:BOOL=ON \\\
        -DMUSIC_INCLUDE_DIR:PATH=$MPI_INCLUDE/music.hh \\\
        -DMUSIC_LIBRARY:PATH=$MPI_LIB/libmusic.so \\\
        -DMUSIC_EXECUTABLE:PATH=$MPI_BIN/music$MPI_SUFFIX \\\
%else \
        -Dwith-music:BOOL=OFF \\\
%endif \
%if "%{_lib}" == "lib64" \
        -DLIB_SUFFIX=64 . && \
%else                      \
        -DLIB_SUFFIX="" . && \
%endif \
popd || exit -1;

%global do_make_build \
    %make_build -C %{name}-simulator-%{version}$MPI_COMPILE_TYPE || exit -1

%global do_pybuild \
pushd %{name}-simulator-%{version}$MPI_COMPILE_TYPE  && \
    pushd pynest && \
        $PYTHON_BIN setup.py build \
    popd && \
    pushd topology && \
        $PYTHON_BIN setup.py build \
    popd && \
    pushd extras/ConnPlotter && \
        $PYTHON_BIN setup.py build \
    popd && \
popd || exit -1;

# Build serial version, dummy arguments
# Disable music, which requires MPI to be ON
%global music 0
export MPI_PYTHON3_SITEARCH="%{python3_sitearch}"
export MPI_COMPILER=serial
export MPI_SUFFIX=""
export MPI_HOME=%{_prefix}
export MPI_BIN=%{_bindir}
export MPI_INCLUDE=%{_includedir}
export MPI_LIB=%{_libdir}
export MPI_YES=OFF
# Python 3
export MPI_COMPILE_TYPE=""
export PYTHON_VERSION="3"
export PYTHON_BIN="%{__python3}"
export MPI_SITEARCH=$MPI_PYTHON3_SITEARCH
%{do_cmake_config}
%{do_make_build}
%{do_pybuild}

# Enable music support
%global music 1
# Build mpich version
%if %{with mpich}
%{_mpich_load}
export CC=mpicc
export CXX=mpicxx
export FC=mpif90
export F77=mpif77
export MPI_YES=ON
# Python 3
export MPI_COMPILE_TYPE="-mpich"
export PYTHON_VERSION="3"
export PYTHON_BIN="%{__python3}"
export MPI_SITEARCH=$MPI_PYTHON3_SITEARCH
%{do_cmake_config}
%{do_make_build}
%{do_pybuild}

%{_mpich_unload}
%endif

# Build OpenMPI version
%if %{with openmpi}
%{_openmpi_load}
export CC=mpicc
export CXX=mpicxx
export FC=mpif90
export F77=mpif77
export MPI_YES=ON
# Python 3
export MPI_COMPILE_TYPE="-openmpi"
export PYTHON_VERSION="3"
export PYTHON_BIN="%{__python3}"
export MPI_SITEARCH=$MPI_PYTHON3_SITEARCH
%{do_cmake_config}
%{do_make_build}
%{do_pybuild}

%{_openmpi_unload}
%endif

%install
# Install everything
%global do_install \
echo  \
echo "*** INSTALLING %{name}-simulator-%{version}$MPI_COMPILE_TYPE ***"  \
echo  \
    %make_install -C %{name}-simulator-%{version}$MPI_COMPILE_TYPE || exit -1


# Only install the pynestkernel
%global do_pynestkernel_install \
pushd %{name}-simulator-%{version}$MPI_COMPILE_TYPE && \
    pushd pynest && \
        install -m 0755 -p -D -t $RPM_BUILD_ROOT/$MPI_SITEARCH/%{name} pynestkernel.so \
    popd && \
popd || exit -1;

# Install the other python bits
%global do_pyinstall \
pushd %{name}-simulator-%{version}$MPI_COMPILE_TYPE && \
    pushd pynest && \
        $PYTHON_BIN setup.py install --skip-build --root $RPM_BUILD_ROOT --install-lib=$MPI_SITEARCH && \
    popd && \
    pushd topology && \
        $PYTHON_BIN setup.py install --skip-build --root $RPM_BUILD_ROOT --install-lib=$MPI_SITEARCH && \
    popd && \
    pushd extras/ConnPlotter && \
        $PYTHON_BIN setup.py install --skip-build --root $RPM_BUILD_ROOT && \
    popd && \
popd || exit -1;


# install serial version
export MPI_SUFFIX=""
export MPI_HOME=%{_prefix}
export MPI_BIN=%{_bindir}
export MPI_YES=OFF
# Python 3
export MPI_COMPILE_TYPE=""
export MPI_SITEARCH="%{python3_sitearch}"
export PYTHON_BIN="%{__python3}"
%{do_install}
%{do_pyinstall}

# Update the helpindex manually
# Should this go in %%post of the doc package maybe?
pushd %{name}-simulator-%{version}/extras/help_generator
    %{__python3} -B generate_helpindex.py $RPM_BUILD_ROOT/%{_docdir}/%{name}/
popd


# Install MPICH version
%if %{with mpich}
%{_mpich_load}
# Python 3
export MPI_COMPILE_TYPE="-mpich"
export MPI_SITEARCH=$MPI_PYTHON3_SITEARCH
export PYTHON_BIN="%{__python3}"
%{do_install}
%{do_pyinstall}

# Remove duplicated docs
rm -rf $RPM_BUILD_ROOT/%{_libdir}/mpich/share/doc/%{name}
# Correct doc location
sed -i 's|NEST_DOC_DIR=$NEST_INSTALL_DIR/share/doc/nest|NEST_DOC_DIR=/usr/share/doc/nest/|' $RPM_BUILD_ROOT/$MPI_BIN/nest_vars.sh
# Remove unneeded scripts
rm -rf $RPM_BUILD_ROOT/%{_libdir}/mpich/share/%{name}/{extras,help_generator}

# Rename binaries to add MPI suffix
pushd $RPM_BUILD_ROOT/$MPI_BIN/
    mv -v %{name}{,$MPI_SUFFIX}
    mv -v %{name}_vars{,$MPI_SUFFIX}.sh
    mv -v %{name}-config{,$MPI_SUFFIX}
    mv -v %{name}_serial{,$MPI_SUFFIX}
    mv -v %{name}_indirect{,$MPI_SUFFIX}
    mv -v sli{,$MPI_SUFFIX}
popd

%{_mpich_unload}
%endif

# Install OpenMPI version
%if %{with openmpi}
%{_openmpi_load}
# Python 3
export MPI_COMPILE_TYPE="-openmpi"
export MPI_SITEARCH=$MPI_PYTHON3_SITEARCH
export PYTHON_BIN="%{__python3}"
%{do_install}
%{do_pyinstall}

# Remove duplicated docs
rm -rf $RPM_BUILD_ROOT/%{_libdir}/openmpi/share/doc/%{name}
# Correct doc location
sed -i 's|NEST_DOC_DIR=$NEST_INSTALL_DIR/share/doc/nest|NEST_DOC_DIR=/usr/share/doc/nest/|' $RPM_BUILD_ROOT/$MPI_BIN/nest_vars.sh
# Remove duplicated scripts
rm -rf $RPM_BUILD_ROOT/%{_libdir}/openmpi/share/%{name}/{extras,help_generator}

# Rename binaries to add MPI suffix
pushd $RPM_BUILD_ROOT/$MPI_BIN/
    mv -v %{name}{,$MPI_SUFFIX}
    mv -v %{name}_vars{,$MPI_SUFFIX}.sh
    mv -v %{name}-config{,$MPI_SUFFIX}
    mv -v %{name}_serial{,$MPI_SUFFIX}
    mv -v %{name}_indirect{,$MPI_SUFFIX}
    mv -v sli{,$MPI_SUFFIX}
popd
%{_openmpi_unload}
%endif


%if %{with tests}
%check
%global do_tests \
echo  \
echo "*** TESTING %{name}-simulator-%{version}$MPI_COMPILE_TYPE ***"  \
echo  \
source $RPM_BUILD_ROOT/$NEST_BINDIR/nest_vars.sh \
export NEST_DOC_DIR=$RPM_BUILD_ROOT/$NEST_DOC_DIR
export NEST_DATA_DIR=$RPM_BUILD_ROOT/$NEST_DATA_DIR
PATH=$RPM_BUILD_ROOT/$NEST_BINDIR/:$PATH $RPM_BUILD_ROOT/$NEST_DATA_DIR/extras/do_tests.sh --source-dir=SKIP \
nosetests $NEST_PYTHONDIR/nest/tests $NEST_PYTHONDIR/nest/topology/tests

# No sli suite here, since we didn't build it for py3
%global do_tests_3 \
echo  \
echo "*** TESTING %{name}-simulator-%{version}$MPI_COMPILE_TYPE ***"  \
echo  \
nosetests-3 $NEST_PYTHONDIR/nest/tests $NEST_PYTHONDIR/nest/topology/tests


export MPI_COMPILE_TYPE=""
export NEST_BINDIR="%{_bindir}"
export PYTHON_VERSION="3"
export PYTHON_BIN="%{__python3}"
export NEST_PYTHONDIR=%{python3_sitearch}
%{do_tests_3}

# Test mpich version
%if %{with mpich}
%{_mpich_load}
export MPI_COMPILE_TYPE="-mpich"
export NEST_BINDIR=$MPI_BIN
export NEST_PYTHONDIR=$MPI_PYTHON3_SITEARCH
export PYTHON_VERSION="3"
export PYTHON_BIN="%{__python3}"
%{do_tests_3}

%{_mpich_unload}
%endif

# Test OpenMPI version
%if %{with openmpi}
%{_openmpi_load}
export MPI_COMPILE_TYPE="-openmpi"
export PYTHON_VERSION="3"
export PYTHON_BIN="%{__python3}"
export MPI_SITEARCH=$MPI_PYTHON3_SITEARCH
%{do_tests_3}

%{_openmpi_unload}
%endif
%endif

%files
%license LICENSE
%doc README-Fedora.md
%{_bindir}/%{name}
%{_bindir}/sli
%{_bindir}/%{name}_vars.sh
%{_bindir}/%{name}-config
%{_bindir}/%{name}_serial
%{_bindir}/%{name}_indirect
%{_libdir}/libconngen.so
%{_libdir}/libmodels.so
%{_libdir}/libnest.so
%{_libdir}/libnestkernel.so
%{_libdir}/libnestutil.so
%{_libdir}/libprecise.so
%{_libdir}/librandom.so
%{_libdir}/libsli.so
%{_libdir}/libsli_readline.so
%{_libdir}/libtopology.so

%files common
%{_datadir}/%{name}

%files headers
%{_includedir}/%{name}

%files doc
%doc %{_pkgdocdir}

%files -n python3-%{name}
%{python3_sitearch}/%{name}
%{python3_sitearch}/PyNEST-nest_%{version}-py%{python3_version}.egg-info
%{python3_sitearch}/Topology-nest_%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/ConnPlotter
%{python3_sitelib}/ConnPlotter-0.7a-py%{python3_version}.egg-info

%if %{with mpich}
%files mpich
%license LICENSE
%doc README-Fedora.md
%{_libdir}/mpich/bin/%{name}_mpich
%{_libdir}/mpich/bin/%{name}_vars_mpich.sh
%{_libdir}/mpich/bin/%{name}-config_mpich
%{_libdir}/mpich/bin/%{name}_serial_mpich
%{_libdir}/mpich/bin/%{name}_indirect_mpich
%{_libdir}/mpich/bin/sli_mpich
%{_libdir}/mpich/lib/libconngen.so
%{_libdir}/mpich/lib/libmodels.so
%{_libdir}/mpich/lib/libnest.so
%{_libdir}/mpich/lib/libnestkernel.so
%{_libdir}/mpich/lib/libnestutil.so
%{_libdir}/mpich/lib/libprecise.so
%{_libdir}/mpich/lib/librandom.so
%{_libdir}/mpich/lib/libsli.so
%{_libdir}/mpich/lib/libsli_readline.so
%{_libdir}/mpich/lib/libtopology.so

%files mpich-common
%{_libdir}/mpich/share/%{name}

%files mpich-headers
%{_includedir}/mpich-%{_arch}/%{name}

%files -n python3-%{name}-mpich
%license LICENSE
%{python3_sitearch}/mpich/%{name}
%{python3_sitearch}/mpich/PyNEST-nest_%{version}-py%{python3_version}.egg-info
%{python3_sitearch}/mpich/Topology-nest_%{version}-py%{python3_version}.egg-info
%endif

%if %{with openmpi}
%files openmpi
%license LICENSE
%doc README-Fedora.md
%{_libdir}/openmpi/bin/%{name}_openmpi
%{_libdir}/openmpi/bin/%{name}_vars_openmpi.sh
%{_libdir}/openmpi/bin/%{name}-config_openmpi
%{_libdir}/openmpi/bin/%{name}_serial_openmpi
%{_libdir}/openmpi/bin/%{name}_indirect_openmpi
%{_libdir}/openmpi/bin/sli_openmpi
%{_libdir}/openmpi/lib/libconngen.so
%{_libdir}/openmpi/lib/libmodels.so
%{_libdir}/openmpi/lib/libnest.so
%{_libdir}/openmpi/lib/libnestkernel.so
%{_libdir}/openmpi/lib/libnestutil.so
%{_libdir}/openmpi/lib/libprecise.so
%{_libdir}/openmpi/lib/librandom.so
%{_libdir}/openmpi/lib/libsli.so
%{_libdir}/openmpi/lib/libsli_readline.so
%{_libdir}/openmpi/lib/libtopology.so


%files openmpi-common
%{_libdir}/openmpi/share/%{name}

%files openmpi-headers
%{_includedir}/openmpi-%{_arch}/%{name}

%files -n python3-%{name}-openmpi
%license LICENSE
%{python3_sitearch}/openmpi/%{name}
%{python3_sitearch}/openmpi/PyNEST-nest_%{version}-py%{python3_version}.egg-info
%{python3_sitearch}/openmpi/Topology-nest_%{version}-py%{python3_version}.egg-info
%endif

%changelog
* Mon Aug 10 2020 Jeff Law <law@redhat.com> - 2.20.0-5
- Disable LTO on armv7hl for now

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.20.0-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.20.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.20.0-2
- Rebuilt for Python 3.9

* Sat Feb 01 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 2.20.0-1
- Update to 2.20.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct 16 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 2.18.0-7
- Rebuild with MUSIC support
- MUSIC requires MPI support to be enabled

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.18.0-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Wed Aug 21 2019 Miro Hrončok <mhroncok@redhat.com> - 2.18.0-5
- Rebuilt for Python 3.8

* Tue Aug 20 2019 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.18.0-4
- Rebuilt for GSL 2.6.

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.18.0-3
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 19 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 2.18.0-1
- Update to 2.18
- Re-enable 32bit arches
- Update patch
- Drop py2 support

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.16.0-11
- Rebuild for readline 8.0

* Thu Feb 14 2019 Orion Poplawski <orion@nwra.com>
- Rebuild for openmpi 3.1.3

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.16.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 23 2019 Björn Esser <besser82@fedoraproject.org> - 2.16.0-8
- Append curdir to CMake invokation. (#1668512)

* Sat Dec 29 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 2.16.0-7
- Move matplotlib and ipython to weak deps

* Mon Dec 17 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 2.16.0-6
- Correct location of MPI headers
- Use CMAKE directives to specify lib location

* Fri Dec 14 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 2.16.0-5
- Add required suffixes to MPI binaries
- Explicitly mention all shared objects

* Sat Nov 24 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 2.16.0-4
- Use bcond
- Enable libneurosim support

* Sun Oct 28 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 2.16.0-3
- Spec improvements
- Use release conditional for uniformity
- Create source directories in the build directory

* Thu Oct 18 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 2.16.0-2
- Make py3 default build
- Disable py2 build
- Use README file instead of creating it in the spec.
- Correct NEST_DOC_DIR to point to correct doc files for all variants (#1639678)

* Fri Oct 05 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 2.16.0-1
- Exclude 32 bit architectures: https://github.com/nest/nest-simulator/issues/1031
- Use python version specific shebangs
- Update to latest upstream release
- Place headers in separate packages

* Fri Jul 27 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 2.14.0-4
- Improve readme
- Disable tests for the time being while I check builds

* Thu Jul 26 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 2.14.0-3
- Enable tests
- Use autosetup
- Improve description
- Improve make usage

* Tue Jul 24 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 2.14.0-2
- Enable mpi builds
- Do not make mpi packages noarch, since MPI_HOME is arch dependent
- Do not remove nest config files---the environment variables are used by programs

* Sun Jun 24 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 2.14.0-1
- Update to latest release
- remove developer docs
- fix build
- improve commands

* Mon Apr 25 2016 Ankur Sinha <ankursinha AT fedoraproject DOT org> 2.10.0-22.git79b2f01
- Update to latest commit - test tammioppen changes

* Mon Apr 25 2016 Ankur Sinha <ankursinha AT fedoraproject DOT org> 2.10.0-21.git58fcecb
- Update to latest commit

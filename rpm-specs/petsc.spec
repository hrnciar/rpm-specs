# Testing ?
%bcond_without check

## Debug builds ?
%bcond_with debug
#

# Define _pkgdocdir macro on epel
%{?el7:%global _pkgdocdir %{_docdir}/%{name}}
#

%if 0%{?fedora}
%bcond_without mpich
%bcond_without openmpi
%endif

%if %{?__isa_bits:%{__isa_bits}}%{!?__isa_bits:32} == 64
%bcond_without arch64
%else
%bcond_with arch64
%endif

%bcond_without blas
%if %{with arch64}
%bcond_without blas64
%endif

%if 0%{?rhel} && 0%{?rhel} >= 7
%bcond_without mpich
%bcond_without openmpi
%endif

%if 0%{?rhel} == 7
%global dts devtoolset-8-
%endif

#
## PETSC looks incompatible with serial MUMPS
%bcond_without mumps_serial
#
## Sundials needs mpi ??
%bcond_with sundials_serial
#
%bcond_without superlu
#

## Suitesparse
## Currently, suitesparse-5.4.0 is available on Fedora 32+, but this version of PETSc needs at least 5.6.0
%bcond_with suitesparse
%if 0%{?fedora} && 0%{?fedora} >= 32
%bcond_with suitesparse64
%endif
#

## SuperLUDIST needs parmetis
%bcond_without superludist
%bcond_with superlumt
#

## Metis
%bcond_without metis
#

# hdf5' is required by 'cgns'
%bcond_without cgns
%bcond_without hdf5

# 'scalapack' is required by 'mumps'
%if %{with openmpi}
%bcond_without mpi
# PETSC-3.* is incompatible with Sundials 3+
%bcond_with sundials
%bcond_without scalapack
%bcond_without mumps
%bcond_without ptscotch
%bcond_without hypre
%endif

%if %{with mpich}
%bcond_without mpi
# PETSC-3.* is incompatible with Sundials 3+
%bcond_with sundials
%bcond_without scalapack
%bcond_without mumps
%bcond_without ptscotch
%bcond_without hypre
%endif

%global releasever 3.13

%global petsc_build_options \\\
 %if %{with debug} \
 CFLAGS="-O0 -g -Wl,-z,now -fPIC" CXXFLAGS="-O0 -g -Wl,-z,now -fPIC" FFLAGS="-O0 -g -Wl,-z,now -fPIC -I%{_libdir}/gfortran/modules" COPTFLAGS="-O0 -g -Wl,-z,now" \\\
  CXXOPTFLAGS="-O0 -g -Wl,-z,now" FOPTFLAGS="-O0 -g -Wl,-z,now -I%{_libdir}/gfortran/modules" LDFLAGS="$LDFLAGS -fPIC" \\\
  FCFLAGS="-O0 -g -Wl,-z,now -fPIC -I%{_libdir}/gfortran/modules" \\\
 %else \
 CFLAGS="$CFLAGS -O3 -fPIC" CXXFLAGS="$CXXFLAGS -O3 -fPIC" FFLAGS="$FFLAGS -O3 -fPIC" LDFLAGS="$LDFLAGS -fPIC" \\\
  COPTFLAGS="$CFLAGS" CXXOPTFLAGS="$CXXFLAGS" FOPTFLAGS="$FFLAGS" \\\
  FCFLAGS="$FFLAGS -O3 -fPIC" \\\
 %endif \
 --CC_LINKER_FLAGS="$LDFLAGS" \\\
 --FC_LINKER_FLAGS="$LDFLAGS -lgfortran" \\\
 --with-default-arch=0 --with-make=1 \\\
 --with-cmake-exec=%{_bindir}/cmake3 --with-ctest-exec=%{_bindir}/ctest3 \\\
 --with-single-library=1 \\\
 --with-precision=double \\\
 --with-petsc-arch=%{_arch} \\\
 --with-clanguage=C \\\
 --with-shared-libraries=1 \\\
 --with-fortran-interfaces=1 \\\
 --with-windows-graphics=0 \\\
 --CC=gcc \\\
 --FC=gfortran \\\
 --CXX=g++ \\\
 --with-shared-ld=ld \\\
 --with-pic=1 \\\
 --with-clib-autodetect=0 \\\
 --with-fortranlib-autodetect=0 \\\
 --with-threadsafety=0 --with-log=1 \\\
 %if 0%{?fedora} \
  --with-cxxlib-autodetect=0 \\\
 %endif \
 %if %{with debug} \
  --with-debugging=1 \\\
 %else \
  --with-debugging=0 \\\
 %endif \
 %if %{with mumps_serial} \
  --with-mumps-serial=1 \\\
 %endif \
  --with-mpi=0 \\\
 %if %{with hdf5} \
  --with-hdf5=1 \\\
  --with-hdf5-include= \\\
  --with-hdf5-lib="-lhdf5 -lhdf5_hl" \\\
 %endif \
 %if %{with cgns} \
  --with-cgns=1 \\\
  --with-cgns-include= \\\
  --with-cgns-lib=-lcgns \\\
 %endif \
  --with-x=1 \\\
  --with-openmp=0 \\\
  --with-hwloc=0 \\\
  --with-ssl=0 \\\
 %if %{with sundials_serial} \
  --with-sundials=1 \\\
  --with-sundials-include=%{_includedir} \\\
  --with-sundials-lib="-lsundials_nvecserial -lsundials_cvode" \\\
 %endif \
 %if %{with metis} \
   --with-metis=1 \\\
 %endif \
  --with-pthread=1 \\\
  --with-valgrind=1

%global petsc_mpibuild_options \\\
 %if %{with debug} \
 CFLAGS="-O0 -g -Wl,-z,now -fPIC" CXXFLAGS="-O0 -g -Wl,-z,now -fPIC" FFLAGS="-O0 -g -Wl,-z,now -fPIC -I${MPI_FORTRAN_MOD_DIR}" COPTFLAGS="-O0 -g -Wl,-z,now" \\\
  CXXOPTFLAGS="-O0 -g -Wl,-z,now" FOPTFLAGS="-O0 -g -Wl,-z,now -I${MPI_FORTRAN_MOD_DIR}" LDFLAGS="$LDFLAGS -fPIC" \\\
  FCFLAGS="-O0 -g -Wl,-z,now -fPIC -I${MPI_FORTRAN_MOD_DIR}" \\\
 %else \
 CFLAGS="$CFLAGS -O3 -fPIC" CXXFLAGS="$CXXFLAGS -O3 -fPIC" FFLAGS="$FFLAGS -O3 -fPIC" LDFLAGS="$LDFLAGS -fPIC" \\\
  COPTFLAGS="$CFLAGS" CXXOPTFLAGS="$CXXFLAGS" FOPTFLAGS="$FFLAGS" \\\
  FCFLAGS="$FFLAGS -O3 -fPIC" \\\
 %endif \
  --CC_LINKER_FLAGS="$LDFLAGS" \\\
  --with-default-arch=0 --with-make=1 \\\
  --with-cmake-exec=%{_bindir}/cmake3 --with-ctest-exec=%{_bindir}/ctest3 \\\
  --with-single-library=1 \\\
  --with-precision=double \\\
  --with-petsc-arch=%{_arch} \\\
  --with-clanguage=C \\\
  --with-shared-libraries=1 \\\
  --with-fortran-interfaces=1 \\\
  --with-windows-graphics=0 \\\
  --with-cc=mpicc \\\
  --with-cxx=mpicxx \\\
  --with-fc=mpif77 \\\
  --with-shared-ld=ld \\\
  --with-pic=1 \\\
  --with-clib-autodetect=0 \\\
  --with-fortranlib-autodetect=0 \\\
 %if 0%{?fedora} \
  --with-cxxlib-autodetect=0 \\\
 %endif \
  --with-threadsafety=0 --with-log=1 \\\
 %if %{with debug} \
  --with-debugging=1 \\\
 %else \
  --with-debugging=0 \\\
 %endif \
 %if %{with scalapack} \
  --with-scalapack=1 \\\
  --with-scalapack-lib="-L$MPI_LIB -lscalapack" \\\
  --with-scalapck-include="" \\\
 %endif \
 %if %{with mpi} \
  --with-mpi=1 \\\
 %endif \
 %if %{with cgns} \
  --with-cgns=1 \\\
  --with-cgns-include= \\\
  --with-cgns-lib=-lcgns \\\
 %endif \
 %if %{with hdf5} \
  --with-hdf5=1 \\\
  --with-hdf5-include= \\\
  --with-hdf5-lib="-L$MPI_LIB -lhdf5 -lhdf5_hl" \\\
 %endif \
 %if %{with ptscotch} \
  --with-ptscotch=1 \\\
  --with-ptscotch-include= \\\
  --with-ptscotch-lib="-L$MPI_LIB -lptscotch -lscotch -lptscotcherr -lscotcherr" \\\
 %endif \
 %if %{with mumps} \
  --with-mumps=1 \\\
 %endif \
 %if %{with sundials} \
  --with-sundials=1 \\\
  --with-sundials-include=$MPI_INCLUDE \\\
  --with-sundials-lib=-lsundials_nvecparallel \\\
 %endif \
 %if %{with metis} \
   --with-metis=1 \\\
 %endif \
 %if %{with superludist} \
  --with-superlu_dist=1 \\\
  --with-superlu_dist-include=$MPI_INCLUDE/superlu_dist \\\
  --with-superlu_dist-lib=-lsuperlu_dist \\\
 %endif \
  --with-x=1 \\\
  --with-openmp=0 \\\
  --with-hwloc=0 \\\
  --with-ssl=0 \\\
 %if %{with hypre} \
  --with-hypre=1 \\\
  --with-hypre-include=$MPI_INCLUDE/hypre \\\
  --with-hypre-lib="-L$MPI_LIB -lHYPRE" \\\
 %endif \
 %if %{with fftw} \
  --with-fftw=1 \\\
  --with-fftw-include= \\\
  --with-fftw-lib="-L$MPI_LIB -lfftw3_mpi -lfftw3" \\\
 %endif \
  --with-pthread=1 \\\
  --with-valgrind=1


Name:    petsc
Summary: Portable Extensible Toolkit for Scientific Computation
Version: %{releasever}.2
Release: 1%{?dist}
License: BSD
URL:     https://www.mcs.anl.gov/petsc
Source0: https://www.mcs.anl.gov/petsc/mirror/release-snapshots/petsc-%{version}.tar.gz

## Remove rpath flags
Patch0:  %{name}-3.11-no-rpath.patch

## Rename library name for 64-bit integer package
Patch1:  %{name}-lib64.patch

# Reverting patch for Hypre-2.11.2
Patch2:  %{name}-3.11-hypre_2.11.2_reverting.patch

Patch3:  %{name}-3.13-fix_mumps_includes.patch
Patch4:  %{name}-3.13.0-fix_metis64.patch
Patch5:  %{name}-3.13.0-fix_sundials_version.patch
Patch6:  %{name}-3.13.0-fix_pkgconfig_file.patch

Patch7:  %{name}-3.13-bug634.patch

%if %{with superlu}
BuildRequires: SuperLU-devel >= 5.2.0
%endif
%if %{with superlumt}
BuildRequires: SuperLUMT-devel
%endif
%if %{with mumps_serial}
BuildRequires: MUMPS-devel >= 5.2.1
%endif
%if %{with metis}
BuildRequires: metis-devel >= 5.1.0
%endif
%if %{with suitesparse}
BuildRequires: suitesparse-devel >= 5.6.0
%endif
%if %{with blas}
BuildRequires: openblas-devel, openblas-srpm-macros
%endif
BuildRequires: %{?dts}gcc, %{?dts}gcc-c++, cmake3
BuildRequires: %{?dts}gcc-gfortran
BuildRequires: libX11-devel
%if 0%{?el7}
BuildRequires: python2-devel
%else
BuildRequires: python3-devel
%endif
BuildRequires: pcre-devel
%if 0%{?el7}
BuildRequires: pkgconfig
%else
BuildRequires: pkgconf-pkg-config
%endif
%if %{with hdf5}
BuildRequires: hdf5-devel
%endif
%if %{with cgns}
BuildRequires: cgnslib-devel
BuildRequires: hdf5-devel
%endif
BuildRequires: valgrind-devel
BuildRequires: tcsh
BuildRequires: xorg-x11-server-Xvfb
Requires:      gcc-gfortran%{?_isa}

%description
PETSc, pronounced PET-see (the S is silent), is a suite of data structures
and routines for the scalable (parallel) solution of scientific applications
modeled by partial differential equations.

%package devel
Summary:    Portable Extensible Toolkit for Scientific Computation (developer files)
Requires:   %{name}%{?_isa} = %{version}-%{release}
%if 0%{?el7}
Requires: pkgconfig%{?_isa}
%else
Requires: pkgconf-pkg-config%{?_isa}
%endif
%description devel
Portable Extensible Toolkit for Scientific Computation (developer files).

%package doc
Summary:    Portable Extensible Toolkit for Scientific Computation (documentation files)
%if 0%{?el7}
BuildRequires: python2-sphinx
%else
BuildRequires: python3-sphinx
%endif
BuildArch:  noarch
%description doc
Portable Extensible Toolkit for Scientific Computation.
PDF and HTML documentation files.

%if %{with arch64}
%package -n petsc64
Summary: Portable Extensible Toolkit for Scientific Computation (64bit INTEGER)
BuildRequires: openblas-serial64 >= 0.2.19-1
BuildRequires: openblas-devel >= 0.2.19-1
%if %{with metis}
BuildRequires: metis64-devel >= 5.1.0
%endif
Requires:   gcc-gfortran%{?_isa}

%description -n petsc64
PETSc, pronounced PET-see (the S is silent), is a suite of data structures
and routines for the scalable (parallel) solution of scientific applications
modeled by partial differential equations (64bit INTEGER).

%package -n petsc64-devel
Requires:   %{name}64%{?_isa} = %{version}-%{release}
Requires:   gcc-gfortran%{?_isa}
%if 0%{?el7}
Requires: pkgconfig%{?_isa}
%else
Requires: pkgconf-pkg-config%{?_isa}
%endif
Summary: Portable Extensible Toolkit for Scientific Computation (64bit INTEGER)

%description -n petsc64-devel
Portable Extensible Toolkit for Scientific Computation (developer files)
(64bit INTEGER).
%endif

#############################################################################
#########
%if %{with openmpi}
%package openmpi
Summary:    Portable Extensible Toolkit for Scientific Computation (OpenMPI)
BuildRequires: openmpi-devel
%if %{with hdf5}
BuildRequires: hdf5-openmpi-devel
%endif
%if %{with cgns}
BuildRequires: cgnslib-devel
BuildRequires: hdf5-openmpi-devel
%endif
%if %{with ptscotch}
BuildRequires: ptscotch-openmpi-devel
%endif
%if %{with scalapack}
BuildRequires: scalapack-openmpi-devel
%if 0%{?rhel} || 0%{?fedora} < 32
BuildRequires: blacs-openmpi-devel
%endif
%endif
%if %{with mumps}
BuildRequires: MUMPS-openmpi-devel >= 5.2.1
%endif
%if %{with sundials}
BuildRequires: sundials-openmpi-devel
%endif
%if %{with superludist}
BuildRequires: superlu_dist-openmpi-devel >= 6.1.1
%endif
%if %{with fftw}
BuildRequires: fftw-devel
BuildRequires: fftw-openmpi-devel
%endif
%if %{with hypre}
BuildRequires: hypre-openmpi-devel
%endif
%if %{with blas}
BuildRequires: openblas-devel, openblas-srpm-macros
%endif
Requires:   gcc-gfortran%{?_isa}

%description openmpi
PETSc, pronounced PET-see (the S is silent), is a suite of data structures
and routines for the scalable (parallel) solution of scientific applications
modeled by partial differential equations.

%package openmpi-devel
Summary:    Portable Extensible Toolkit for Scientific Computation (OpenMPI)
Requires:   %{name}-openmpi%{?_isa} = %{version}-%{release}
Requires:   openmpi-devel%{?_isa}
%description openmpi-devel
Portable Extensible Toolkit for Scientific Computation (developer files).
%endif
######
###############################################################################
######
%if %{with mpich}
%package mpich
Summary:    Portable Extensible Toolkit for Scientific Computation (MPICH)
BuildRequires: mpich-devel
%if %{with hdf5}
BuildRequires: hdf5-mpich-devel
%endif
%if %{with cgns}
BuildRequires: cgnslib-devel
BuildRequires: hdf5-mpich-devel
%endif
%if %{with ptscotch}
BuildRequires: ptscotch-mpich-devel
%endif
%if %{with scalapack}
BuildRequires: scalapack-mpich-devel
%if 0%{?rhel} || 0%{?fedora} < 32
BuildRequires: blacs-mpich-devel
%endif
%endif
%if %{with mumps}
BuildRequires: MUMPS-mpich-devel >= 5.2.1
%endif
%if %{with sundials}
BuildRequires: sundials-mpich-devel
%endif
%if %{with superludist}
BuildRequires: superlu_dist-mpich-devel >= 6.1.1
%endif
%if %{with hypre}
BuildRequires: hypre-mpich-devel
%endif
%if %{with fftw}
BuildRequires: fftw-devel
BuildRequires: fftw-mpich-devel
%endif
%if %{with blas}
BuildRequires: openblas-devel, openblas-srpm-macros
%endif
Requires:   gcc-gfortran%{?_isa}

%global mpichversion %(rpm -qi mpich | awk -F': ' '/Version/ {print $2}')
Requires:   mpich%{?_isa} >= 0:%{mpichversion}-1

%description mpich
PETSc, pronounced PET-see (the S is silent), is a suite of data structures
and routines for the scalable (parallel) solution of scientific applications
modeled by partial differential equations.

%package mpich-devel
Summary:    Portable Extensible Toolkit for Scientific Computation (MPICH)
Requires:   %{name}-mpich%{?_isa} = %{version}-%{release}
%if 0%{?el7}
# https://bugzilla.redhat.com/show_bug.cgi?id=1397192
Requires:       mpich-devel
%else
Requires:       mpich-devel%{?_isa}
%endif
%description mpich-devel
Portable Extensible Toolkit for Scientific Computation (developer files).
%endif
######
#############################################################################

%prep
%setup -qc

pushd %{name}-%{version}

%patch7 -p1 -b .bug634

%if 0%{?fedora} || 0%{?rhel} >= 8
find . -name 'setup.py' | xargs pathfix.py -pn -i "%{__python3}"
find . -name 'configure' | xargs pathfix.py -pn -i "%{__python3}"
find config -name '*.py' | xargs pathfix.py -pn -i "%{__python3}"
find src/benchmarks/streams -name '*.py' | xargs pathfix.py -pn -i "%{__python3}"
%endif

%if 0%{?el7}
%patch2 -R -p1
%endif
popd

%if %{with arch64}
cp -a %{name}-%{version} build64
pushd build64
%patch1 -p0
%patch4 -p1 -b .metis64
popd
%endif

pushd %{name}-%{version}
%patch0 -p0
%patch5 -p1
%patch6 -p1
popd

%if %{with openmpi}
cp -a %{name}-%{version} buildopenmpi_dir
%endif
%if %{with mpich}
cp -a %{name}-%{version} buildmpich_dir
%endif

# Do NOT move up this patch
pushd %{name}-%{version}
%patch3 -p1
popd

%build
pushd %{name}-%{version}
%if 0%{?el7}
%{?dts:source /opt/rh/devtoolset-8/enable}
%configure --with-cc=/opt/rh/devtoolset-8/root/usr/bin/gcc --with-cxx=/opt/rh/devtoolset-8/root/usr/bin/g++ --with-fc=/opt/rh/devtoolset-8/root/usr/bin/gfortran \
%else
%configure --with-cc=gcc --with-cxx=g++ --with-fc=gfortran \
%endif
 %{petsc_build_options} \
 --with-64-bit-indices=0 \
%if %{with blas}
 --with-blas-lapack-lib=-lopenblasp --known-64-bit-blas-indices=0 \
%endif
 %if %{with superlu}
  --with-superlu=1 \
  --with-superlu-include=%{_includedir}/SuperLU \
  --with-superlu-lib=-lsuperlu \
%endif
%if %{with suitesparse}
 --with-suitesparse=1 \
 --with-suitesparse-include=%{_includedir}/suitesparse \
 --with-suitesparse-lib="-lumfpack -lklu -lcholmod -lamd"
%endif
#cat config.log && exit 1
##

RPM_BUILD_NCPUS="`%{_bindir}/getconf _NPROCESSORS_ONLN`"
make \
 V=1 MAKE_NP=$RPM_BUILD_NCPUS PETSC_DIR=%{_builddir}/%{name}-%{version}/%{name}-%{version} PETSC_ARCH=%{_arch} all
popd

%if %{with arch64}
pushd build64
%if 0%{?el7}
%{?dts:source /opt/rh/devtoolset-8/enable}
%configure --with-cc=/opt/rh/devtoolset-8/root/usr/bin/gcc --with-cxx=/opt/rh/devtoolset-8/root/usr/bin/g++ --with-fc=/opt/rh/devtoolset-8/root/usr/bin/gfortran \
%else
%configure --with-cc=gcc --with-cxx=g++ --with-fc=gfortran \
%endif
 %{petsc_build_options} \
 --with-64-bit-indices=1 \
%if %{with blas64}
 --with-blas-lapack-lib=-lopenblasp64 --known-64-bit-blas-indices=1 \
%endif
%if %{with suitesparse64}
 --with-suitesparse=1 \
 --with-suitesparse-include=%{_includedir}/suitesparse \
 --with-suitesparse-lib="-lumfpack64 -lklu64 -lcholmod64 -lamd64"
%endif
##

RPM_BUILD_NCPUS="`%{_bindir}/getconf _NPROCESSORS_ONLN`"
make \
 V=1 MAKE_NP=$RPM_BUILD_NCPUS PETSC_DIR=%{_builddir}/%{name}-%{version}/build64 PETSC_ARCH=%{_arch} all
popd
%endif

%if %{with openmpi}
pushd buildopenmpi_dir

%if 0%{?el7}
%{?dts:source /opt/rh/devtoolset-8/enable}
%endif

%{_openmpi_load}
%configure \
 --FC_LINKER_FLAGS="$LDFLAGS -lgfortran -lmpi_mpifh" \
 --LIBS=" -lmpi_mpifh" \
 %{petsc_mpibuild_options} \
 --with-64-bit-indices=0 \
%if %{with blas}
 --with-blas-lapack-lib=-lopenblasp --known-64-bit-blas-indices=0
%endif
#cat config.log
#exit 1

RPM_BUILD_NCPUS="`%{_bindir}/getconf _NPROCESSORS_ONLN`"
make \
 V=1 MAKE_NP=$RPM_BUILD_NCPUS PETSC_DIR=%{_builddir}/%{name}-%{version}/buildopenmpi_dir PETSC_ARCH=%{_arch} all
%{_openmpi_unload}
popd
%endif

%if %{with mpich}
pushd buildmpich_dir

%if 0%{?el7}
%{?dts:source /opt/rh/devtoolset-8/enable}
%endif

%{_mpich_load}
%configure \
 --FC_LINKER_FLAGS="$LDFLAGS -lgfortran -lmpifort" \
 --LIBS=" -lmpifort" \
 %{petsc_mpibuild_options} \
 --with-64-bit-indices=0 \
%if %{with blas}
 --with-blas-lapack-lib=-lopenblasp --known-64-bit-blas-indices=0
%endif
#cat config.log
#exit 1

RPM_BUILD_NCPUS="`%{_bindir}/getconf _NPROCESSORS_ONLN`"
make \
 V=1 MAKE_NP=$RPM_BUILD_NCPUS PETSC_DIR=%{_builddir}/%{name}-%{version}/buildmpich_dir PETSC_ARCH=%{_arch} all
%{_mpich_unload}
popd
%endif

%install
pushd %{name}-%{version}
mkdir -p $RPM_BUILD_ROOT%{_libdir} $RPM_BUILD_ROOT%{_includedir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_fmoddir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_libdir}/%{name}/conf

install -pm 755 %{_arch}/lib/libpetsc.* $RPM_BUILD_ROOT%{_libdir}
ln -sf libpetsc.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libpetsc.so
ln -sf libpetsc.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libpetsc.so.%{releasever}

install -pm 644 %{_arch}/include/*.h $RPM_BUILD_ROOT%{_includedir}/%{name}/
install -pm 644 %{_arch}/include/*.mod $RPM_BUILD_ROOT%{_fmoddir}/%{name}/
cp -a include/* $RPM_BUILD_ROOT%{_includedir}/%{name}/

cp -a %{_arch}/lib/pkgconfig $RPM_BUILD_ROOT%{_libdir}/
pushd $RPM_BUILD_ROOT%{_libdir}/pkgconfig
ln -s PETSc.pc petsc.pc
popd

install -pm 644 %{_arch}/lib/petsc/conf/petscrules $RPM_BUILD_ROOT%{_libdir}/%{name}/conf/
install -pm 644 %{_arch}/lib/petsc/conf/petscvariables $RPM_BUILD_ROOT%{_libdir}/%{name}/conf/
install -pm 644 lib/petsc/conf/rules $RPM_BUILD_ROOT%{_libdir}/%{name}/conf/
install -pm 644 lib/petsc/conf/variables $RPM_BUILD_ROOT%{_libdir}/%{name}/conf/
sed -e 's|%{_builddir}/%{name}-%{version}/%{name}-%{version}|%{_prefix}|g' -i $RPM_BUILD_ROOT%{_libdir}/%{name}/conf/petscvariables
sed -e 's|%{_builddir}/%{name}-%{version}/%{name}-%{version}/%{_arch}/|%{_prefix}|g' -i $RPM_BUILD_ROOT%{_libdir}/%{name}/conf/petscvariables
sed -e 's|-L%{_prefix}/%{_arch}/lib|-L%{_libdir}|g' -i $RPM_BUILD_ROOT%{_libdir}/%{name}/conf/petscvariables
sed -e 's|-I%{_prefix}/%{_arch}/include|-I%{_includedir}/%{name} -I%{_fmoddir}/%{name}|g' -i $RPM_BUILD_ROOT%{_libdir}/%{name}/conf/petscvariables
sed -e 's|${PETSC_DIR}/${PETSC_ARCH}/lib|${PETSC_DIR}/%{_lib}|g' -i $RPM_BUILD_ROOT%{_libdir}/%{name}/conf/variables
sed -e 's|${PETSC_DIR}/${PETSC_ARCH}/lib|${PETSC_DIR}/%{_lib}|g' -i $RPM_BUILD_ROOT%{_libdir}/%{name}/conf/rules
popd

%if %{with arch64}
pushd build64
mkdir -p $RPM_BUILD_ROOT%{_libdir} $RPM_BUILD_ROOT%{_includedir}/%{name}64
mkdir -p $RPM_BUILD_ROOT%{_fmoddir}/%{name}64
mkdir -p $RPM_BUILD_ROOT%{_libdir}/%{name}64/conf
mkdir -p $RPM_BUILD_ROOT%{_libdir}/pkgconfig

install -pm 755 %{_arch}/lib/libpetsc64.* $RPM_BUILD_ROOT%{_libdir}
ln -sf libpetsc64.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libpetsc64.so
ln -sf libpetsc64.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libpetsc64.so.%{releasever}

install -pm 644 %{_arch}/include/*.h $RPM_BUILD_ROOT%{_includedir}/%{name}64/
install -pm 644 %{_arch}/include/*.mod $RPM_BUILD_ROOT%{_fmoddir}/%{name}64/
cp -a include/* $RPM_BUILD_ROOT%{_includedir}/%{name}64/

cp -p %{_arch}/lib/pkgconfig/PETSc.pc $RPM_BUILD_ROOT%{_libdir}/pkgconfig/PETSc64.pc
pushd $RPM_BUILD_ROOT%{_libdir}/pkgconfig
ln -s PETSc64.pc petsc64.pc
popd

install -pm 644 %{_arch}/lib/petsc/conf/petscrules $RPM_BUILD_ROOT%{_libdir}/%{name}64/conf/
install -pm 644 %{_arch}/lib/petsc/conf/petscvariables $RPM_BUILD_ROOT%{_libdir}/%{name}64/conf/
install -pm 644 lib/petsc/conf/rules $RPM_BUILD_ROOT%{_libdir}/%{name}64/conf/
install -pm 644 lib/petsc/conf/variables $RPM_BUILD_ROOT%{_libdir}/%{name}64/conf/
sed -e 's|%{_builddir}/%{name}-%{version}/build64|%{_prefix}|g' -i $RPM_BUILD_ROOT%{_libdir}/%{name}64/conf/petscvariables
sed -e 's|%{_builddir}/%{name}-%{version}/build64/%{_arch}/|%{_prefix}|g' -i $RPM_BUILD_ROOT%{_libdir}/%{name}64/conf/petscvariables
sed -e 's|-L%{_prefix}/%{_arch}/lib|-L%{_libdir}|g' -i $RPM_BUILD_ROOT%{_libdir}/%{name}64/conf/petscvariables
sed -e 's|-I%{_prefix}/%{_arch}/include/|-I%{_includedir}/%{name}64 -I%{_fmoddir}/%{name}64|g' -i $RPM_BUILD_ROOT%{_libdir}/%{name}64/conf/petscvariables
sed -e 's|${PETSC_DIR}/${PETSC_ARCH}/lib|${PETSC_DIR}/%{_lib}|g' -i $RPM_BUILD_ROOT%{_libdir}/%{name}64/conf/variables
sed -e 's|${PETSC_DIR}/${PETSC_ARCH}/lib|${PETSC_DIR}/%{_lib}|g' -i $RPM_BUILD_ROOT%{_libdir}/%{name}64/conf/rules
popd
%endif

%if %{with openmpi}
pushd buildopenmpi_dir
%{_openmpi_load}
mkdir -p $RPM_BUILD_ROOT$MPI_LIB $RPM_BUILD_ROOT$MPI_INCLUDE/%{name}
mkdir -p $RPM_BUILD_ROOT$MPI_FORTRAN_MOD_DIR/%{name}
mkdir -p $RPM_BUILD_ROOT$MPI_LIB/%{name}/conf

install -pm 755 %{_arch}/lib/libpetsc.* $RPM_BUILD_ROOT$MPI_LIB
ln -sf libpetsc.so.%{version} $RPM_BUILD_ROOT$MPI_LIB/libpetsc.so
ln -sf libpetsc.so.%{version} $RPM_BUILD_ROOT$MPI_LIB/libpetsc.so.%{releasever}

install -pm 644 %{_arch}/include/*.h $RPM_BUILD_ROOT$MPI_INCLUDE/%{name}/
install -pm 644 %{_arch}/include/*.mod $RPM_BUILD_ROOT$MPI_FORTRAN_MOD_DIR/%{name}/
cp -a include/* $RPM_BUILD_ROOT$MPI_INCLUDE/%{name}/

cp -a %{_arch}/lib/pkgconfig $RPM_BUILD_ROOT$MPI_LIB/
sed -e 's|-I${includedir}/petsc|-I%{_includedir}/openmpi-%{_arch}/petsc|g' -i $RPM_BUILD_ROOT$MPI_LIB/pkgconfig/PETSc.pc
sed -e 's|-L${libdir}|-L%{_libdir}/openmpi/lib|g' -i $RPM_BUILD_ROOT$MPI_LIB/pkgconfig/PETSc.pc
sed -e 's|ldflag_rpath=-L|ldflag_rpath=-L%{_libdir}/openmpi/lib|g' -i $RPM_BUILD_ROOT$MPI_LIB/pkgconfig/PETSc.pc
pushd $RPM_BUILD_ROOT$MPI_LIB/pkgconfig
ln -s PETSc.pc petsc.pc
popd

install -pm 644 %{_arch}/lib/petsc/conf/petscrules $RPM_BUILD_ROOT$MPI_LIB/%{name}/conf/
install -pm 644 %{_arch}/lib/petsc/conf/petscvariables $RPM_BUILD_ROOT$MPI_LIB/%{name}/conf/
install -pm 644 lib/petsc/conf/rules $RPM_BUILD_ROOT$MPI_LIB/%{name}/conf/
install -pm 644 lib/petsc/conf/variables $RPM_BUILD_ROOT$MPI_LIB/%{name}/conf/
sed -e 's|%{_builddir}/%{name}-%{version}/buildopenmpi_dir|%{_prefix}|g' -i $RPM_BUILD_ROOT$MPI_LIB/%{name}/conf/petscvariables
sed -e 's|%{_builddir}/%{name}-%{version}/buildopenmpi_dir/%{_arch}/|%{_prefix}|g' -i $RPM_BUILD_ROOT$MPI_LIB/%{name}/conf/petscvariables
sed -e 's|-L%{_prefix}/%{_arch}/lib|-L%{_libdir}/openmpi/lib|g' -i $RPM_BUILD_ROOT$MPI_LIB/%{name}/conf/petscvariables
sed -e 's|-I%{_prefix}/%{_arch}/include|-I%{_includedir}/openmpi-%{_arch}/%{name} -I%{_fmoddir}/openmpi/%{name}|g' -i $RPM_BUILD_ROOT$MPI_LIB/%{name}/conf/petscvariables
sed -e 's|${PETSC_DIR}/${PETSC_ARCH}/lib|${PETSC_DIR}/%{_lib}/openmpi/lib|g' -i $RPM_BUILD_ROOT$MPI_LIB/%{name}/conf/variables
sed -e 's|${PETSC_DIR}/${PETSC_ARCH}/lib|${PETSC_DIR}/%{_lib}/openmpi/lib|g' -i $RPM_BUILD_ROOT$MPI_LIB/%{name}/conf/rules
%{_openmpi_unload}
popd
%endif

%if %{with mpich}
pushd buildmpich_dir
%{_mpich_load}
mkdir -p $RPM_BUILD_ROOT$MPI_LIB $RPM_BUILD_ROOT$MPI_INCLUDE/%{name}
mkdir -p $RPM_BUILD_ROOT$MPI_FORTRAN_MOD_DIR/%{name}
mkdir -p $RPM_BUILD_ROOT$MPI_LIB/%{name}/conf

install -pm 755 %{_arch}/lib/libpetsc.* $RPM_BUILD_ROOT$MPI_LIB
ln -sf libpetsc.so.%{version} $RPM_BUILD_ROOT$MPI_LIB/libpetsc.so
ln -sf libpetsc.so.%{version} $RPM_BUILD_ROOT$MPI_LIB/libpetsc.so.%{releasever}

install -pm 644 %{_arch}/include/*.h $RPM_BUILD_ROOT$MPI_INCLUDE/%{name}/
install -pm 644 %{_arch}/include/*.mod $RPM_BUILD_ROOT$MPI_FORTRAN_MOD_DIR/%{name}/
cp -a include/* $RPM_BUILD_ROOT$MPI_INCLUDE/%{name}/

cp -a %{_arch}/lib/pkgconfig $RPM_BUILD_ROOT$MPI_LIB/
sed -e 's|-I${includedir}/petsc|-I%{_includedir}/mpich-%{_arch}/petsc|g' -i $RPM_BUILD_ROOT$MPI_LIB/pkgconfig/PETSc.pc
sed -e 's|-L${libdir}|-L%{_libdir}/mpich/lib|g' -i $RPM_BUILD_ROOT$MPI_LIB/pkgconfig/PETSc.pc
sed -e 's|ldflag_rpath=-L|ldflag_rpath=-L%{_libdir}/mpich/lib|g' -i $RPM_BUILD_ROOT$MPI_LIB/pkgconfig/PETSc.pc
pushd $RPM_BUILD_ROOT$MPI_LIB/pkgconfig
ln -s PETSc.pc petsc.pc
popd

install -pm 644 %{_arch}/lib/petsc/conf/petscrules $RPM_BUILD_ROOT$MPI_LIB/%{name}/conf/
install -pm 644 %{_arch}/lib/petsc/conf/petscvariables $RPM_BUILD_ROOT$MPI_LIB/%{name}/conf/
install -pm 644 lib/petsc/conf/rules $RPM_BUILD_ROOT$MPI_LIB/%{name}/conf/
install -pm 644 lib/petsc/conf/variables $RPM_BUILD_ROOT$MPI_LIB/%{name}/conf/
sed -e 's|%{_builddir}/%{name}-%{version}/buildmpich_dir|%{_prefix}|g' -i $RPM_BUILD_ROOT$MPI_LIB/%{name}/conf/petscvariables
sed -e 's|%{_builddir}/%{name}-%{version}/buildmpich_dir/%{_arch}/|%{_prefix}|g' -i $RPM_BUILD_ROOT$MPI_LIB/%{name}/conf/petscvariables
sed -e 's|-L%{_prefix}/%{_arch}/lib|-L%{_libdir}/mpich/lib|g' -i $RPM_BUILD_ROOT$MPI_LIB/%{name}/conf/petscvariables
sed -e 's|-I%{_prefix}/%{_arch}/include|-I%{_includedir}/mpich-%{_arch}/%{name} -I%{_fmoddir}/mpich/%{name}|g' -i $RPM_BUILD_ROOT$MPI_LIB/%{name}/conf/petscvariables
sed -e 's|${PETSC_DIR}/${PETSC_ARCH}/lib|${PETSC_DIR}/%{_lib}/mpich/lib|g' -i $RPM_BUILD_ROOT$MPI_LIB/%{name}/conf/variables
sed -e 's|${PETSC_DIR}/${PETSC_ARCH}/lib|${PETSC_DIR}/%{_lib}/mpich/lib|g' -i $RPM_BUILD_ROOT$MPI_LIB/%{name}/conf/rules
%{_mpich_unload}
popd
%endif

# Move html documentation in _pkgdocdir
pushd $RPM_BUILD_ROOT%{_includedir}
mkdir -p $RPM_BUILD_ROOT%{_pkgdocdir}/headers
for i in `find . -name "*.h.html" -type f -print`; do
    mv $i $RPM_BUILD_ROOT%{_pkgdocdir}/headers
done
for i in `find . -name "*.html" -type f -print`; do
    mv $i $RPM_BUILD_ROOT%{_pkgdocdir}/headers
done
find . -name "Makefile" -type f -print | xargs /bin/rm -f
popd
cp -a %{name}-%{version}/docs/* $RPM_BUILD_ROOT%{_pkgdocdir}
#

%ldconfig_scriptlets

%if %{with arch64}
%ldconfig_scriptlets -n petsc64
%endif

%if %{with check}
%check
%if %{with openmpi}
%{_openmpi_load}
export LD_LIBRARY_PATH=%{_builddir}/%{name}-%{version}/buildopenmpi_dir/%{_arch}/lib
export PETSC_DIR=%{_builddir}/%{name}-%{version}/buildopenmpi_dir
export PETSC_ARCH=%{_arch}
export MPI_INTERFACE_HOSTNAME=localhost
%if %{with debug}
export PETSCVALGRIND_OPTIONS=" --tool=memcheck --leak-check=yes --track-origins=yes"
export CFLAGS="-O0 -g -Wl,-z,now -fPIC"
export CXXFLAGS="-O0 -g -Wl,-z,now -fPIC"
export FFLAGS="-O0 -g -Wl,-z,now -fPIC -I%{_libdir}/gfortran/modules"
xvfb-run -a make all test -C buildopenmpi_dir V=1 MPIEXEC='%{_builddir}/%{name}-%{version}/buildopenmpi_dir/lib/petsc/bin/petscmpiexec -valgrind'
%else
xvfb-run -a make all test -C buildopenmpi_dir V=1
%endif
%{_openmpi_unload}
%endif

%if 0%{?fedora} || 0%{?rhel} >= 7
%if %{with mpich}
%{_mpich_load}
export LD_LIBRARY_PATH=%{_builddir}/%{name}-%{version}/buildmpich_dir/%{_arch}/lib
export PETSC_DIR=%{_builddir}/%{name}-%{version}/buildmpich_dir
export PETSC_ARCH=%{_arch}
export MPI_INTERFACE_HOSTNAME=localhost
%if %{with debug}
export PETSCVALGRIND_OPTIONS=" --tool=memcheck --leak-check=yes --track-origins=yes"
export CFLAGS="-O0 -g -Wl,-z,now -fPIC"
export CXXFLAGS="-O0 -g -Wl,-z,now -fPIC"
export FFLAGS="-O0 -g -Wl,-z,now -fPIC -I%{_libdir}/gfortran/modules"
xvfb-run -a make all test -C buildmpich_dir V=1 MPIEXEC='%{_builddir}/%{name}-%{version}/buildmpich_dir/lib/petsc/bin/petscmpiexec -valgrind'
%else
xvfb-run -a make all test -C buildmpich_dir V=1
%endif
%{_mpich_unload}
%endif
%endif

export LD_LIBRARY_PATH=%{_libdir}:%{_builddir}/%{name}-%{version}/%{name}-%{version}/%{_arch}/lib
export PETSC_DIR=%{_builddir}/%{name}-%{version}/%{name}-%{version}
export PETSC_ARCH=%{_arch}

%if %{with debug}
export PETSCVALGRIND_OPTIONS=" --tool=memcheck --leak-check=yes --track-origins=yes"
export CFLAGS="-O0 -g -Wl,-z,now -fPIC"
export CXXFLAGS="-O0 -g -Wl,-z,now -fPIC"
export FFLAGS="-O0 -g -Wl,-z,now -fPIC -I%{_libdir}/gfortran/modules"
xvfb-run -a make all test -C %{name}-%{version} V=1 MPIEXEC='%{_builddir}/%{name}-%{version}/%{name}-%{version}/lib/petsc/bin/petscmpiexec -valgrind'
%else
xvfb-run -a make all test -C %{name}-%{version} V=1
%endif

%if %{with arch64}
export LD_LIBRARY_PATH=%{_libdir}:%{_builddir}/%{name}-%{version}/build64/%{_arch}/lib
export PETSC_DIR=%{_builddir}/%{name}-%{version}/build64
export PETSC_ARCH=%{_arch}

## 'make test' needs to link against -lpetsc
## Crude fix:
ln -s %{_builddir}/%{name}-%{version}/build64/%{_arch}/lib/libpetsc64.so %{_builddir}/%{name}-%{version}/build64/%{_arch}/lib/libpetsc.so

%if %{with debug}
export PETSCVALGRIND_OPTIONS=" --tool=memcheck --leak-check=yes --track-origins=yes"
export CFLAGS="-O0 -g -Wl,-z,now -fPIC"
export CXXFLAGS="-O0 -g -Wl,-z,now -fPIC"
export FFLAGS="-O0 -g -Wl,-z,now -fPIC -I%{_libdir}/gfortran/modules"
xvfb-run -a make all test -C build64 V=1 MPIEXEC='%{_builddir}/%{name}-%{version}/build64/lib/petsc/bin/petscmpiexec -valgrind'
%else
xvfb-run -a make all test -C build64 V=1
%endif
%endif
%endif

%files
%license %{name}-%{version}/LICENSE
%{_libdir}/libpetsc.so.*

%files devel
%{_libdir}/pkgconfig/*.pc
%{_libdir}/%{name}/
%{_libdir}/libpetsc.so
%{_includedir}/%{name}/
%{_fmoddir}/%{name}/

%files doc
%license %{name}-%{version}/LICENSE
%{_pkgdocdir}/

%if %{with arch64}
%files -n petsc64
%license build64/LICENSE
%{_libdir}/libpetsc64.so.*

%files -n petsc64-devel
%{_libdir}/pkgconfig/*.pc
%{_libdir}/%{name}64/
%{_libdir}/libpetsc64.so
%{_includedir}/%{name}64/
%{_fmoddir}/%{name}64/
%endif

%if %{with openmpi}
%files openmpi
%license buildopenmpi_dir/LICENSE
%{_libdir}/openmpi/lib/libpetsc.so.*

%files openmpi-devel
%{_libdir}/openmpi/lib/libpetsc.so
%{_libdir}/openmpi/lib/%{name}/
%{_libdir}/openmpi/lib/pkgconfig/*.pc
%{_includedir}/openmpi-%{_arch}/%{name}/
%if 0%{?el7}
%{_fmoddir}/openmpi-%{_arch}/%{name}/
%else
%{_fmoddir}/openmpi/%{name}/
%endif
%endif

%if %{with mpich}
%files mpich
%license buildmpich_dir/LICENSE
%{_libdir}/mpich/lib/libpetsc.so.*

%files mpich-devel
%{_libdir}/mpich/lib/libpetsc.so
%{_libdir}/mpich/lib/%{name}/
%{_libdir}/mpich/lib/pkgconfig/*.pc
%{_includedir}/mpich-%{_arch}/%{name}/
%if 0%{?el7}
%{_fmoddir}/mpich-%{_arch}/%{name}/
%else
%{_fmoddir}/mpich/%{name}/
%endif
%endif

%changelog
* Fri Jun 05 2020 Antonio Trande <sagitter@fedoraproject.org> - 3.13.2-1
- Release 3.13.2
- Compiled against openblas-threads

* Fri May 08 2020 Björn Esser <besser82@fedoraproject.org> - 3.13.1-2
- Rebuild (cgnslib)

* Sun May 03 2020 Antonio Trande <sagitter@fedoraproject.org> - 3.13.1-1
- Release 3.13.1

* Sun Apr 12 2020 Nicolas Chauvet <kwizart@gmail.com> - 3.13.0-2
- Rebuilt for MUMPS 5.3

* Fri Apr 10 2020 Antonio Trande <sagitter@fedoraproject.org> - 3.13.0-1
- Release 3.13.0
- Fix hdf5/cgns support
- Fix pkgconfig cflags
- Enable superludist

* Fri Feb 21 2020 Sandro Mani <manisandro@gmail.com> - 3.12.4-3
- Rebuild (cgnslib)

* Mon Feb 17 2020 Sandro Mani <manisandro@gmail.com> - 3.12.4-2
- Rebuild (cgnslib)

* Thu Feb 13 2020 Antonio Trande <sagitter@fedoraproject.org> - 3.12.4-1
- Release 3.12.4

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 10 2020 Antonio Trande <sagitter@fedoraproject.org> - 3.12.3-1
- Release 3.12.3

* Sun Jan 05 2020 Antonio Trande <sagitter@fedoraproject.org> - 3.12.2-2
- Fix Changelog
- Use mpiblacs on EPEL 7 and Fedora < 32

* Sat Nov 23 2019 Antonio Trande <sagitter@fedoraproject.org> - 3.12.2-1
- Release 3.12.2

* Wed Oct 23 2019 Antonio Trande <sagitter@fedoraproject.org> - 3.12.1-1
- Release 3.12.1

* Sun Oct 20 2019 Antonio Trande <sagitter@fedoraproject.org> - 3.12.0-2
- Patched for hypre-2.18.0

* Fri Oct 18 2019 Antonio Trande <sagitter@fedoraproject.org> - 3.12.0-1
- Release 3.12.0
- Rebuild for hypre 2.18.0

* Tue Oct 01 2019 Antonio Trande <sagitter@fedoraproject.org> - 3.11.3-10
- New rebuild

* Tue Oct 01 2019 Antonio Trande <sagitter@fedoraproject.org> - 3.11.3-9
- Explicit required MPICH version (rhbz#1757279)

* Thu Sep 19 2019 Orion Poplawski <orion@nwra.com> - 3.11.3-8
- Rebuild for hypre 2.17.0

* Wed Sep 11 2019 Orion Poplawski <orion@nwra.com> - 3.11.3-7
- Build for python3 only, without dts for EPEL8

* Mon Aug 26 2019 Antonio Trande <sagitter@fedoraproject.org> - 3.11.3-6
- Rebuilt for MPICH 3.2.1

* Wed Aug 21 2019 Antonio Trande <sagitter@fedoraproject.org> - 3.11.3-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 23 2019 Antonio Trande <sagitter@fedoraproject.org> - 3.11.3-3
- Complete rebuild

* Fri Jul 19 2019 Antonio Trande <sagitter@fedoraproject.org> - 3.11.3-2
- Rebuild for MUMPS-5.2.1
- Use Python 2 on EPEL

* Thu Jun 27 2019 Antonio Trande <sagitter@fedoraproject.org> - 3.11.3-1
- Release 3.11.3

* Sat May 25 2019 Antonio Trande <sagitter@fedoraproject.org> - 3.11.2-1
- Release 3.11.2

* Fri May 03 2019 Antonio Trande <sagitter@fedoraproject.org> - 3.11.1-2
- Rebuild for OpenMPI-4

* Mon Apr 15 2019 Antonio Trande <sagitter@fedoraproject.org> - 3.11.1-1
- Release 3.11.1
- Switch to Python3
- Use openblas always

* Sat Mar 16 2019 Orion Poplawski <orion@nwra.com> - 3.10.4-2
- Rebuild for hdf5 1.10.5

* Tue Mar 12 2019 Antonio Trande <sagitter@fedoraproject.org> - 3.10.4-1
- Release 3.10.4

* Tue Mar 12 2019 Sandro Mani <manisandro@gmail.com> - 3.10.3-4
- Rebuild (cgnslib)

* Thu Feb 14 2019 Orion Poplawski <orion@nwra.com> - 3.10.3-3
- Rebuild for openmpi 3.1.3

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec 20 2018 Antonio Trande <sagitter@fedoraproject.org> - 3.10.3-1
- Release 3.10.3

* Thu Nov 29 2018 Orion Poplawski <orion@nwra.com> - 3.10.2-2
- Re-enable OpenMPI tests - fixed with openmpi 2.1.6rc1

* Tue Oct 23 2018 Antonio Trande <sagitter@fedoraproject.org> - 3.10.2-1
- Update to 3.10.2
- Disable check of OpenMPI libraries on x86 temporarely (rhbz#1639646)

* Tue Oct 23 2018 Antonio Trande <sagitter@fedoraproject.org> - 3.9.3-5
- Fix paths inside of the 'rules' config files

* Fri Aug 03 2018 Antonio Trande <sagitter@fedoraproject.org> - 3.9.3-4
- Fix conditional macros for MPI builds

* Thu Aug 02 2018 Antonio Trande <sagitter@fedoraproject.org> - 3.9.3-3
- Exclude OpenMPI build on Fedora 28 s390x
- Patched for using Hypre-2.11.2 on epel7

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 3.9.3-2
- Rebuild with fixed binutils

* Fri Jul 27 2018 Antonio Trande <sagitter@fedoraproject.org> - 3.9.3-1
- Update to 3.9.3

* Thu Jul 19 2018 Sandro Mani <manisandro@gmail.com> - 3.9.0-5
- Rebuild (scotch)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri May 04 2018 Antonio Trande <sagitter@fedoraproject.org> - 3.9.0-3
- Use unversioned directory for installing configuration files

* Thu Apr 26 2018 Antonio Trande <sagitter@fedoraproject.org> - 3.9.0-2
- Set again the MPI builds on Fedora

* Wed Apr 11 2018 Antonio Trande <sagitter@fedoraproject.org> - 3.9.0-1
- Update to 3.9.0

* Fri Mar 30 2018 Antonio Trande <sagitter@fedoraproject.org> - 3.8.4-1
- Update to 3.8.4
- Exclude MPI builds on s390 archirectures if fedora < 28 only
- Patched for using Hypre-2.14.0

* Tue Feb 06 2018 Antonio Trande <sagitter@fedoraproject.org> - 3.8.3-5
- Use unversioned directory for installing configuration files

* Tue Feb 06 2018 Antonio Trande <sagitter@fedoraproject.org> - 3.8.3-4
- Fix pkgconfig request on rhel

* Sun Feb 04 2018 Antonio Trande <sagitter@fedoraproject.org> - 3.8.3-3
- cgns/hdf5 support enabled (bz#1541616)

* Sat Feb 03 2018 Antonio Trande <sagitter@fedoraproject.org> - 3.8.3-2
- Fix PETSC_LIB_DIR variables
- cgns/hdf5 support temporarily disabled (bz#1541616)

* Sun Jan 28 2018 Antonio Trande <sagitter@fedoraproject.org> - 3.8.3-1
- Update to 3.8.3
- Rebuild for sundials-3.1.0

* Thu Dec 14 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.8.1-4
- Not build 64-bit integer libraries on epel6

* Sun Dec 03 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.8.1-3
- Build 64-bit integer libraries on epel7

* Sun Dec 03 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.8.1-2
- Fix Fortran MPI library path on epel

* Wed Nov 22 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.8.1-1
- Update to 3.8.1
- Disable Sundials
- Enable MUMPS on serial build

* Mon Nov 13 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.8.0-5
- Install .mod files (bz#1212557)

* Thu Nov 09 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.8.0-4
- Fix soname version

* Wed Nov 08 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.8.0-3
- Rebuild for hypre-2.13.0
- Disable sundials on MPI builds

* Sun Oct 29 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.8.0-2
- Define openblas arches

* Tue Oct 03 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.8.0-1
- Update to 3.8.0
- with-mpiuni-fortran-binding option deprecated
- Remove obsolete patch2

* Mon Oct 02 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.7.7-5
- Disable debugging
- Unset default compiler flags when tests are built

* Sun Oct 01 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.7.7-4
- Rebuild for debugging

* Sun Oct 01 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.7.7-3
- Exclude MPI builds on s390x

* Sat Sep 30 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.7.7-2
- Enable mpiuni-fortran-binding on MPI builds

* Tue Sep 26 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.7.7-1
- Update to 3.7.7
- Move petscvariables/petscrules under a private directory of libdir

* Wed Aug 16 2017 Antonio Trande <sagitterATfedoraproject.org> - 3.7.6-9
- Rebuild for lapack 3.7.1 (moved to 64_ suffix)

* Sun Aug 13 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.7.6-8
- Option for Fedora < 25 definitively removed

* Sun Aug 13 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.7.6-7
- Superlu_dist needs parmetis
- Use MPI variables

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed May 17 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.7.6-4
- Fix Requires packages

* Mon May 15 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.7.6-3
- Move petscvariables/petscrules under private directory of /usr/share

* Fri May 12 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.7.6-2
- Move petscvariables/petscrules under private directory of /usr/lib

* Fri May 05 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.7.6-1
- Update to 3.7.6
- Install petscvariables/petscrules
- Install pkgconfig files

* Sun Apr 09 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.7.5-4
- Exclude aarch64 on fedora < 25

* Sat Mar 25 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.7.5-3
- Rebuild for MUMPS-5.1.1

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 04 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.7.5-1
- Update to 3.7.5

* Fri Dec 02 2016 Antonio Trande <sagitter@fedoraproject.org> - 3.7.4-14
- Conditionalize mpich-devel%%{?_isa} (bz#1397192)

* Tue Nov 01 2016 Antonio Trande <sagitter@fedoraproject.org> - 3.7.4-13
- New architectures

* Wed Oct 26 2016 Antonio Trande <sagitter@fedoraproject.org> - 3.7.4-12
- Fix OpenMPI builds

* Tue Oct 25 2016 Antonio Trande <sagitter@fedoraproject.org> - 3.7.4-11
- Fix s390x builds again

* Tue Oct 25 2016 Antonio Trande <sagitter@fedoraproject.org> - 3.7.4-10
- Fix s390x builds

* Mon Oct 24 2016 Antonio Trande <sagitter@fedoraproject.org> - 3.7.4-9
- Build 64bit-int libs (bz#1382916)

* Sat Oct 22 2016 Antonio Trande <sagitter@fedoraproject.org> - 3.7.4-8
- Build 64bit-int libs (bz#1382916)

* Fri Oct 21 2016 Antonio Trande <sagitter@fedoraproject.org> - 3.7.4-7
- Install missing header files

* Wed Oct 19 2016 Antonio Trande <sagitter@fedoraproject.org> - 3.7.4-6
- Add the -O3 to restore vectorization over the RPM defaults
- Remove gmp support

* Thu Oct 13 2016 Antonio Trande <sagitter@fedoraproject.org> - 3.7.4-5
- 64bit-int libs not built (bz#1382916)
- Enable gmp and suitesparse support

* Thu Oct 13 2016 Antonio Trande <sagitter@fedoraproject.org> - 3.7.4-4
- superlu and fftw enabled
- Fixed settings of compiler flags
- Disable flags for "hardened" builds

* Mon Oct 10 2016 Antonio Trande <sagitter@fedoraproject.org> - 3.7.4-3
- Enabled fftw-mpi support (Fedora > 24)
- Omitted PAPI (obsolete)
- Omitted tetgen support (used with C++) 

* Sun Oct 09 2016 Antonio Trande <sagitter@fedoraproject.org> - 3.7.4-2
- Default optimization level (-O2)

* Sun Oct 09 2016 Antonio Trande <sagitter@fedoraproject.org> - 3.7.4-1
- Update to 3.7.4
- PAPI support disabled (upstream advice)

* Sat Oct 08 2016 Antonio Trande <sagitter@fedoraproject.org> - 3.7.3-8
- Add tcsh as BR package
- Patched for disabling petscnagupgrade.py check

* Fri Oct 07 2016 Antonio Trande <sagitter@fedoraproject.org> - 3.7.3-7
- Use Make for testing

* Thu Oct 06 2016 Antonio Trande <sagitter@fedoraproject.org> - 3.7.3-6
- Remove linkage to mpiblacs
- Tests enabled

* Thu Oct 06 2016 Antonio Trande <sagitter@fedoraproject.org> - 3.7.3-5
- hwloc/metis (needs parmetis) disabled (upstream advice)
- X support enabled
- Libraries detection disabled

* Wed Oct 05 2016 Antonio Trande <sagitter@fedoraproject.org> - 3.7.3-4
- Fix library paths

* Wed Oct 05 2016 Antonio Trande <sagitter@fedoraproject.org> - 3.7.3-3
- Fix PTScotch

* Wed Oct 05 2016 Antonio Trande <sagitter@fedoraproject.org> - 3.7.3-2
- Disabled fftw support

* Wed Sep 28 2016 Antonio Trande <sagitter@fedoraproject.org> - 3.7.3-1
- Update to 3.7.3
- Remove module files

* Tue Sep 13 2016 Antonio Trande <sagitter@fedoraproject.org> - 3.7.2-12
- Fix MAKE_NP option
- Remove --known-endian option
- Use architecture condition for openblas
- Fix unused-direct-shlib-dependency warnings

* Fri Aug 26 2016 Antonio Trande <sagitter@fedoraproject.org> - 3.7.2-11
- Use SuperLU on >=f25 only

* Thu Aug 25 2016 Antonio Trande <sagitter@fedoraproject.org> - 3.7.2-10
- Some fixes for epel6 builds
- Add -O3 flag
- Headers installed under a private directory
- Use %%{_modulesdir} macro
- Use 'openblas' instead of 'blas'

* Wed Aug 10 2016 Antonio Trande <sagitter@fedoraproject.org> - 3.7.2-9
- Fortran modules moved into devel sub-packages
- Some fixes of SPEC file's lines
- Set compiler/linker flags against PAPI-5.1.1 on epel6

* Thu Jul 28 2016 Dave Love <loveshack@fedoraproject.org> - 3.7.2-8
- Support el6
- Add cgnslib support

* Sat Jul 23 2016 Antonio Trande <sagitter@fedoraproject.org> - 3.7.2-7
- Rebuild with Hypre support

* Sun Jul 10 2016 Antonio Trande <sagitter@fedoraproject.org> - 3.7.2-6
- Packed additional header files
- Tests performed on EPEL7

* Mon Jun 27 2016 Antonio Trande <sagitter@fedoraproject.org> - 3.7.2-5
- Perform tests one-by-one
- Packaged all documentation files

* Mon Jun 27 2016 Antonio Trande <sagitter@fedoraproject.org> - 3.7.2-4
- Build OpenMPI/MPICH libraries
- Fix known-endian option

* Mon Jun 27 2016 Antonio Trande <sagitter@fedoraproject.org> - 3.7.2-3
- Disable additional libraries
- Build a minimal PETSC

* Fri Jun 24 2016 Antonio Trande <sagitter@fedoraproject.org> - 3.7.2-2
- Perform test

* Sun Jun 19 2016 Antonio Trande <sagitter@fedoraproject.org> - 3.7.2-1
- New package

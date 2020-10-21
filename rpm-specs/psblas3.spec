%global with_mpich 1
%global with_openmpi 1
%global with_serial 1

%if 0%{?fedora} >= 33
%global blaslib flexiblas
%else
%global blaslib openblas
%endif

%if %{?__isa_bits:%{__isa_bits}}%{!?__isa_bits:32} == 64
%global arch64 0
%else
%global arch64 0
%endif

# Use devtoolset 8
%if 0%{?rhel} && 0%{?rhel} == 7
%global dts devtoolset-8-
%endif

# Workarounf for GCC-10
# https://gcc.gnu.org/gcc-10/porting_to.html
%if 0%{?fedora} && 0%{?fedora} > 31
%global fc_optflags %{build_fflags} -fallow-argument-mismatch
%endif

%if 0%{?rhel} || 0%{?fedora} < 32
%global fc_optflags %{build_fflags}
%endif

%global major_version 3
%global major_minor %{major_version}.6
%global postrelease_version -4

Name: psblas3
Summary: Parallel Sparse Basic Linear Algebra Subroutines
Version: %{major_minor}.1
Release: 11%{?dist}
License: BSD
URL: https://github.com/sfilippone/psblas3
Source0: https://github.com/sfilippone/psblas3/archive/v%{version}%{?postrelease_version}/psblas3-%{version}%{?postrelease_version}.tar.gz

# Call default Fedora ldflags when linker creates links 
Patch0: %{name}-fix_ldflags.patch

# Rename libraries for psblas3_64
Patch1: %{name}-rename_libs_for_arch64.patch

BuildRequires: suitesparse-devel
BuildRequires: %{blaslib}-devel
BuildRequires: metis-devel

%description
The PSBLAS library, developed with the aim to facilitate the parallelization
of computationally intensive scientific applications,
is designed to address parallel implementation of iterative solvers for sparse
linear systems through the distributed memory paradigm.
It includes routines for multiplying sparse matrices by dense matrices,
solving block diagonal systems with triangular diagonal entries,
preprocessing sparse matrices, and contains additional routines for
dense matrix operations.
The current implementation of PSBLAS addresses a distributed memory execution
model operating with message passing.

%if 0%{?with_serial}
%package serial
Summary: %{name} serial mode
BuildRequires: %{?dts}gcc-gfortran
BuildRequires: %{?dts}gcc, %{?dts}gcc-c++
Requires: %{name}-common = %{version}-%{release}
Requires: gcc-gfortran%{?_isa}

%description serial
The PSBLAS library, developed with the aim to facilitate the parallelization
of computationally intensive scientific applications,
is designed to address parallel implementation of iterative solvers for sparse
linear systems through the distributed memory paradigm.
It includes routines for multiplying sparse matrices by dense matrices,
solving block diagonal systems with triangular diagonal entries,
preprocessing sparse matrices, and contains additional routines for
dense matrix operations.
The current implementation of PSBLAS addresses a distributed memory execution
model operating with message passing.
This is a PSBLAS version in pure serial mode.

%package serial-devel
Summary: Development files for %{name}
Requires: %{name}-serial%{?_isa} = %{version}-%{release}
Provides: %{name}-serial-static = %{version}-%{release}
%description serial-devel
Shared links, header files and static libraries for serial %{name}.
%endif

%package common
Summary: Documentation files for %{name}
BuildArch: noarch
#BuildRequires: texlive-tex4ht, texlive-latex, doxygen, ghostscript
#BuildRequires: texlive-fancybox, texlive-kpathsea, texlive-metafont
#BuildRequires: texlive-mfware, texlive-iftex
%description common
HTML, PDF and license files of %{name}.

########################################################
%if 0%{?arch64}
%package -n %{name}_64
Summary: %{name} for long-integer (8-byte) data
BuildRequires: suitesparse64-devel
BuildRequires: %{blaslib}-devel
BuildRequires: metis64-devel

Requires: %{name}-common = %{version}-%{release}
%description -n psblas3_64
The PSBLAS library, developed with the aim to facilitate the parallelization
of computationally intensive scientific applications,
is designed to address parallel implementation of iterative solvers for sparse
linear systems through the distributed memory paradigm.
It includes routines for multiplying sparse matrices by dense matrices,
solving block diagonal systems with triangular diagonal entries,
preprocessing sparse matrices, and contains additional routines for
dense matrix operations.
The current implementation of PSBLAS addresses a distributed memory execution
model operating with message passing.
This is a PSBLAS version for long-integer (8-byte) data.

%package -n %{name}_64-devel
Summary: The %{name}_64 headers and development-related files
Requires: %{name}_64%{?_isa} = %{version}-%{release}
Provides: %{name}_64-static = %{version}-%{release}
%description -n %{name}_64-devel
Shared links, header files and static libraries for %{name}_64.
%endif
##########################################################

########################################################
%if 0%{?with_openmpi}
%package openmpi
Summary: OpenMPI %{name}
BuildRequires:	openmpi-devel

Requires: openmpi%{?_isa}
Requires: %{name}-common = %{version}-%{release}
%description openmpi
The PSBLAS library, developed with the aim to facilitate the parallelization
of computationally intensive scientific applications,
is designed to address parallel implementation of iterative solvers for sparse
linear systems through the distributed memory paradigm.
It includes routines for multiplying sparse matrices by dense matrices,
solving block diagonal systems with triangular diagonal entries,
preprocessing sparse matrices, and contains additional routines for
dense matrix operations.
The current implementation of PSBLAS addresses a distributed memory execution
model operating with message passing.
This is a OpenMPI PSBLAS version.

%package openmpi-devel
Summary: The OpenMPI %{name} headers and development-related files
Requires: %{name}-openmpi%{?_isa} = %{version}-%{release}
Provides: %{name}-openmpi-static = %{version}-%{release}
%description openmpi-devel
Shared links, header files and static libraries for OpenMPI %{name}.
%endif
##########################################################
########################################################
%if 0%{?with_mpich}
%package mpich
Summary: MPICH %{name}
BuildRequires:	mpich-devel

Requires: mpich%{?_isa}
Requires: %{name}-common = %{version}-%{release}
%description mpich
The PSBLAS library, developed with the aim to facilitate the parallelization
of computationally intensive scientific applications,
is designed to address parallel implementation of iterative solvers for sparse
linear systems through the distributed memory paradigm.
It includes routines for multiplying sparse matrices by dense matrices,
solving block diagonal systems with triangular diagonal entries,
preprocessing sparse matrices, and contains additional routines for
dense matrix operations.
The current implementation of PSBLAS addresses a distributed memory execution
model operating with message passing.
This is a MPICH PSBLAS version.

%package mpich-devel
Summary: The MPICH %{name} headers and development-related files
Requires: %{name}-mpich%{?_isa} = %{version}-%{release}
Provides: %{name}-mpich-static = %{version}-%{release}
%description mpich-devel
Shared links, header files and static libraries for MPICH %{name}.
%endif
##########################################################

%prep
%setup -qc -n psblas3-%{version}%{?postrelease_version}

pushd psblas3-%{version}%{?postrelease_version}
%patch0 -p0
popd

#######################################################
## Copy source for MPI versions
%if 0%{?with_openmpi}
cp -a psblas3-%{version}%{?postrelease_version} openmpi-build
%endif
%if 0%{?with_mpich}
cp -a psblas3-%{version}%{?postrelease_version} mpich-build
%endif
######################################################

#######################################################
## Copy source for long-integer version
%if 0%{?arch64}
cp -a psblas3-%{version}%{?postrelease_version} build64
pushd build64
%patch1 -p1
popd
%endif
#####################################################

%build
%if 0%{?with_serial}
cd psblas3-%{version}%{?postrelease_version}

%if 0%{?el7}
%{?dts:source /opt/rh/devtoolset-8/enable}
%endif

%configure \
 --enable-serial --with-fcopt="%{?fc_optflags} -Wno-unused-variable -Wno-unused-dummy-argument -fPIC" \
 --with-ccopt="%{build_cflags} -fPIC" --with-include-path="%{_includedir}/%{blaslib} -I%{_fmoddir}" \
 --with-metis=-lmetis --with-amd=-lamd --with-blas=-l%{blaslib} --with-lapack= \
 --with-amdincdir=%{_includedir}/suitesparse
%make_build

# Make shared libraries
pushd lib
gfortran -shared %{__global_ldflags} -Wl,--whole-archive libpsb_base.a -Wl,-no-whole-archive -Wl,-Bdynamic -L%{_libdir} -l%{blaslib} -lgfortran -lm -Wl,-soname,libpsb_base.so.%{version} -o libpsb_base.so.%{version}

gfortran -shared %{__global_ldflags} -Wl,--whole-archive libpsb_krylov.a -Wl,-no-whole-archive -Wl,-Bdynamic -L./ -lpsb_base -L%{_libdir} -l%{blaslib} -lgfortran -lm -Wl,-soname,libpsb_krylov.so.%{version} -o libpsb_krylov.so.%{version}

gfortran -shared %{__global_ldflags} -Wl,--whole-archive libpsb_prec.a -Wl,-no-whole-archive -Wl,-Bdynamic -L./ -lpsb_base -L%{_libdir} -l%{blaslib} -lgfortran -lm -Wl,-soname,libpsb_prec.so.%{version} -o libpsb_prec.so.%{version}

gfortran -shared %{__global_ldflags} -Wl,--whole-archive libpsb_util.a -Wl,-no-whole-archive -Wl,-Bdynamic -L./ -lpsb_base -L%{_libdir} -l%{blaslib} -lmetis -lamd -lgfortran -lm -Wl,-soname,libpsb_util.so.%{version} -o libpsb_util.so.%{version}
popd

cd ../

#make -C test/util MODDIR=../../modules -j1
##

%if 0%{?arch64}
cd build64

%if 0%{?el7}
%{?dts:source /opt/rh/devtoolset-8/enable}
%endif

%configure \
 --enable-serial --enable-long-integers --with-fcopt="%{?fc_optflags} -Wno-unused-variable -Wno-unused-dummy-argument -fPIC" \
 --with-ccopt="%{build_cflags} -fPIC" --with-include-path="%{_includedir}/%{blaslib} -I%{_fmoddir}" \
 --with-metis=-lmetis64 --with-amd=-lamd64 --with-blas=-l%{blaslib}64 --with-lapack= \
 --with-amdincdir=%{_includedir}/suitesparse
%make_build

# Make shared libraries
pushd lib
gfortran -shared %{__global_ldflags} -Wl,--whole-archive libpsb64_base.a -Wl,-no-whole-archive -Wl,-Bdynamic -L%{_libdir} -l%{blaslib}64 -lgfortran -lm -Wl,-soname,libpsb64_base.so.%{version} -o libpsb64_base.so.%{version}

gfortran -shared %{__global_ldflags} -Wl,--whole-archive libpsb64_krylov.a -Wl,-no-whole-archive -Wl,-Bdynamic -L./ -lpsb64_base -L%{_libdir} -l%{blaslib}64 -lgfortran -lm -Wl,-soname,libpsb64_krylov.so.%{version} -o libpsb64_krylov.so.%{version}

gfortran -shared %{__global_ldflags} -Wl,--whole-archive libpsb64_prec.a -Wl,-no-whole-archive -Wl,-Bdynamic -L./ -lpsb64_base -L%{_libdir} -l%{blaslib}64 -lgfortran -lm -Wl,-soname,libpsb_prec.so.%{version} -o libpsb_prec.so.%{version}

gfortran -shared %{__global_ldflags} -Wl,--whole-archive libpsb64_util.a -Wl,-no-whole-archive -Wl,-Bdynamic -L./ -lpsb64_base -L%{_libdir} -l%{blaslib}64 -lmetis64 -lamd64 -lgfortran -lm -Wl,-soname,libpsb64_util.so.%{version} -o libpsb64_util.so.%{version}
popd

cd ../

%endif
%endif

#######################################################
## Build MPI versions
%if 0%{?with_openmpi}
pushd openmpi-build
%{_openmpi_load}
export CC=mpicc
%configure \
 --with-fcopt="%{?fc_optflags} -Wno-unused-variable -Wno-unused-dummy-argument -fPIC" \
 --with-ccopt="%{build_cflags} -fPIC" --with-include-path="%{_includedir}/%{blaslib} -I${MPI_FORTRAN_MOD_DIR}" \
 MPIFC=mpifort MPICC=mpicc \
 --with-metis=-lmetis --with-amd=-lamd --with-blas=-l%{blaslib} --with-lapack= \
 --with-amdincdir=%{_includedir}/suitesparse
%make_build

# Make shared libraries
cd lib
mpifort -shared %{__global_ldflags} -Wl,--whole-archive libpsb_base.a -Wl,-no-whole-archive -Wl,-Bdynamic -L$MPI_LIB -Wl,-rpath -Wl,$MPI_LIB -Wl,--enable-new-dtags -lmpi_mpifh -L%{_libdir} -l%{blaslib} -lgfortran -lm -Wl,-soname,libpsb_base.so.%{version} -o libpsb_base.so.%{version}

mpifort -shared %{__global_ldflags} -Wl,--whole-archive libpsb_krylov.a -Wl,-no-whole-archive -Wl,-Bdynamic -L./ -lpsb_base -L$MPI_LIB -Wl,-rpath -Wl,$MPI_LIB -Wl,--enable-new-dtags -lmpi_mpifh -L%{_libdir} -l%{blaslib} -lmetis -lamd -lgfortran -lm -lrt -Wl,-soname,libpsb_krylov.so.%{version} -o libpsb_krylov.so.%{version}

mpifort -shared %{__global_ldflags} -Wl,--whole-archive libpsb_prec.a -Wl,-no-whole-archive -Wl,-Bdynamic -L./ -lpsb_base -L$MPI_LIB -Wl,-rpath -Wl,$MPI_LIB -Wl,--enable-new-dtags -lmpi_mpifh -L%{_libdir} -l%{blaslib} -lmetis -lamd -lgfortran -lm -lrt -Wl,-soname,libpsb_prec.so.%{version} -o libpsb_prec.so.%{version}

mpifort -shared %{__global_ldflags} -Wl,--whole-archive libpsb_util.a -Wl,-no-whole-archive -Wl,-Bdynamic -L./ -lpsb_base -L$MPI_LIB -Wl,-rpath -Wl,$MPI_LIB -Wl,--enable-new-dtags -lmpi_mpifh -L%{_libdir} -l%{blaslib} -lmetis -lamd -lgfortran -lm -lrt -Wl,-soname,libpsb_util.so.%{version} -o libpsb_util.so.%{version}
cd ../

%{_openmpi_unload}
popd
%endif

%if 0%{?with_mpich}
pushd mpich-build
%{_mpich_load}
export CC=mpicc
%configure \
 --with-fcopt="%{?fc_optflags} -Wno-unused-variable -Wno-unused-dummy-argument -fPIC" \
 --with-ccopt="%{build_cflags} -fPIC" --with-include-path="%{_includedir}/%{blaslib} -I${MPI_FORTRAN_MOD_DIR}" \
 MPIFC=mpif90 MPICC=mpicc \
 --with-metis=-lmetis --with-amd=-lamd --with-blas=-l%{blaslib} --with-lapack= \
 --with-amdincdir=%{_includedir}/suitesparse
%make_build

# Make shared libraries
cd lib

%if 0%{?fedora}
export MPIFLIB=-lmpifort
%else
export MPIFLIB=-lmpich
%endif

mpif90 -shared %{__global_ldflags} -Wl,--whole-archive libpsb_base.a -Wl,-no-whole-archive -Wl,-Bdynamic -L$MPI_LIB -Wl,-rpath -Wl,$MPI_LIB -Wl,-z,noexecstack $MPIFLIB -L%{_libdir} -l%{blaslib} -lgfortran -lm -Wl,-soname,libpsb_base.so.%{version} -o libpsb_base.so.%{version}

mpif90 -shared %{__global_ldflags} -Wl,--whole-archive libpsb_krylov.a -Wl,-no-whole-archive -Wl,-Bdynamic -L./ -lpsb_base -L$MPI_LIB -Wl,-rpath -Wl,$MPI_LIB -Wl,-z,noexecstack $MPIFLIB -L%{_libdir} -l%{blaslib} -lmetis -lamd -lgfortran -lm -lrt -Wl,-soname,libpsb_krylov.so.%{version} -o libpsb_krylov.so.%{version}

mpif90 -shared %{__global_ldflags} -Wl,--whole-archive libpsb_prec.a -Wl,-no-whole-archive -Wl,-Bdynamic -L./ -lpsb_base -L$MPI_LIB -Wl,-rpath -Wl,$MPI_LIB -Wl,-z,noexecstack $MPIFLIB -L%{_libdir} -l%{blaslib} -lmetis -lamd -lgfortran -lm -lrt -Wl,-soname,libpsb_prec.so.%{version} -o libpsb_prec.so.%{version}

mpif90 -shared %{__global_ldflags} -Wl,--whole-archive libpsb_util.a -Wl,-no-whole-archive -Wl,-Bdynamic -L./ -lpsb_base -L$MPI_LIB -Wl,-rpath -Wl,$MPI_LIB $MPIFLIB -Wl,-z,noexecstack -L%{_libdir} -l%{blaslib} -lmetis -lamd -lgfortran -lm -lrt -Wl,-soname,libpsb_util.so.%{version} -o libpsb_util.so.%{version}
cd ../

%{_mpich_unload}
popd
%endif
#######################################################
%if 0%{?with_serial}
%ldconfig_scriptlets serial
%endif

%install
%if 0%{?with_serial}
pushd psblas3-%{version}%{?postrelease_version}
mkdir -p $RPM_BUILD_ROOT%{_includedir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_fmoddir}/%{name}

pushd lib
install -pm 755 *.so.%{version} $RPM_BUILD_ROOT%{_libdir}/
install -pm 644 *.a $RPM_BUILD_ROOT%{_libdir}/

ln -sf %{_libdir}/libpsb_base.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libpsb_base.so.%{major_version}
ln -sf %{_libdir}/libpsb_base.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libpsb_base.so.%{major_minor}
ln -sf %{_libdir}/libpsb_base.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libpsb_base.so

ln -sf %{_libdir}/libpsb_krylov.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libpsb_krylov.so.%{major_version}
ln -sf %{_libdir}/libpsb_krylov.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libpsb_krylov.so.%{major_minor}
ln -sf %{_libdir}/libpsb_krylov.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libpsb_krylov.so

ln -sf %{_libdir}/libpsb_prec.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libpsb_prec.so.%{major_version}
ln -sf %{_libdir}/libpsb_prec.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libpsb_prec.so.%{major_minor}
ln -sf %{_libdir}/libpsb_prec.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libpsb_prec.so

ln -sf %{_libdir}/libpsb_util.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libpsb_util.so.%{major_version}
ln -sf %{_libdir}/libpsb_util.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libpsb_util.so.%{major_minor}
ln -sf %{_libdir}/libpsb_util.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libpsb_util.so
popd

install -pm 644 modules/*.mod $RPM_BUILD_ROOT%{_fmoddir}/%{name}
install -pm 644 include/*.h $RPM_BUILD_ROOT%{_includedir}/%{name}/
popd
%endif

%if 0%{?arch64}
pushd build64
mkdir -p $RPM_BUILD_ROOT%{_includedir}/%{name}64
mkdir -p $RPM_BUILD_ROOT%{_fmoddir}/%{name}64

pushd lib
install -pm 755 *.so.%{version} $RPM_BUILD_ROOT%{_libdir}/
install -pm 644 *.a $RPM_BUILD_ROOT%{_libdir}/

ln -sf %{_libdir}/libpsb64_base.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libpsb64_base.so.%{major_version}
ln -sf %{_libdir}/libpsb64_base.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libpsb64_base.so.%{major_minor}
ln -sf %{_libdir}/libpsb64_base.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libpsb64_base.so

ln -sf %{_libdir}/libpsb64_krylov.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libpsb64_krylov.so.%{major_version}
ln -sf %{_libdir}/libpsb64_krylov.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libpsb64_krylov.so.%{major_minor}
ln -sf %{_libdir}/libpsb64_krylov.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libpsb64_krylov.so

ln -sf %{_libdir}/libpsb64_prec.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libpsb64_prec.so.%{major_version}
ln -sf %{_libdir}/libpsb64_prec.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libpsb64_prec.so.%{major_minor}
ln -sf %{_libdir}/libpsb64_prec.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libpsb64_prec.so

ln -sf %{_libdir}/libpsb64_util.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libpsb64_util.so.%{major_version}
ln -sf %{_libdir}/libpsb64_util.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libpsb64_util.so.%{major_minor}
ln -sf %{_libdir}/libpsb64_util.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libpsb64_util.so
popd

install -pm 644 modules/*.mod $RPM_BUILD_ROOT%{_fmoddir}/%{name}64
install -pm 644 include/*.h $RPM_BUILD_ROOT%{_includedir}/%{name}64/
popd
%endif

#######################################################
## Install MPI versions
%if 0%{?with_openmpi}
pushd openmpi-build
%{_openmpi_load}
mkdir -p $RPM_BUILD_ROOT$MPI_LIB
mkdir -p $RPM_BUILD_ROOT$MPI_INCLUDE/%{name}
mkdir -p $RPM_BUILD_ROOT$MPI_FORTRAN_MOD_DIR/%{name}

cd lib
install -pm 755 *.so.%{version} $RPM_BUILD_ROOT$MPI_LIB/
install -pm 644 *.a $RPM_BUILD_ROOT$MPI_LIB/

ln -sf $MPI_LIB/libpsb_base.so.%{version} $RPM_BUILD_ROOT$MPI_LIB/libpsb_base.so.%{major_version}
ln -sf $MPI_LIB/libpsb_base.so.%{version} $RPM_BUILD_ROOT$MPI_LIB/libpsb_base.so.%{major_minor}
ln -sf $MPI_LIB/libpsb_base.so.%{version} $RPM_BUILD_ROOT$MPI_LIB/libpsb_base.so

ln -sf $MPI_LIB/libpsb_krylov.so.%{version} $RPM_BUILD_ROOT$MPI_LIB/libpsb_krylov.so.%{major_version}
ln -sf $MPI_LIB/libpsb_krylov.so.%{version} $RPM_BUILD_ROOT$MPI_LIB/libpsb_krylov.so.%{major_minor}
ln -sf $MPI_LIB/libpsb_krylov.so.%{version} $RPM_BUILD_ROOT$MPI_LIB/libpsb_krylov.so

ln -sf $MPI_LIB/libpsb_prec.so.%{version} $RPM_BUILD_ROOT$MPI_LIB/libpsb_prec.so.%{major_version}
ln -sf $MPI_LIB/libpsb_prec.so.%{version} $RPM_BUILD_ROOT$MPI_LIB/libpsb_prec.so.%{major_minor}
ln -sf $MPI_LIB/libpsb_prec.so.%{version} $RPM_BUILD_ROOT$MPI_LIB/libpsb_prec.so

ln -sf $MPI_LIB/libpsb_util.so.%{version} $RPM_BUILD_ROOT$MPI_LIB/libpsb_util.so.%{major_version}
ln -sf $MPI_LIB/libpsb_util.so.%{version} $RPM_BUILD_ROOT$MPI_LIB/libpsb_util.so.%{major_minor}
ln -sf $MPI_LIB/libpsb_util.so.%{version} $RPM_BUILD_ROOT$MPI_LIB/libpsb_util.so
cd ../

install -pm 644 modules/*.mod $RPM_BUILD_ROOT$MPI_FORTRAN_MOD_DIR/%{name}
install -pm 644 include/*.h $RPM_BUILD_ROOT$MPI_INCLUDE/%{name}/
%{_openmpi_unload}
popd
%endif

%if 0%{?with_mpich}
pushd mpich-build
%{_mpich_load}
mkdir -p $RPM_BUILD_ROOT$MPI_LIB
mkdir -p $RPM_BUILD_ROOT$MPI_INCLUDE/%{name}
mkdir -p $RPM_BUILD_ROOT$MPI_FORTRAN_MOD_DIR/%{name}

cd lib
install -pm 755 *.so.%{version} $RPM_BUILD_ROOT$MPI_LIB/
install -pm 644 *.a $RPM_BUILD_ROOT$MPI_LIB/

ln -sf $MPI_LIB/libpsb_base.so.%{version} $RPM_BUILD_ROOT$MPI_LIB/libpsb_base.so.%{major_version}
ln -sf $MPI_LIB/libpsb_base.so.%{version} $RPM_BUILD_ROOT$MPI_LIB/libpsb_base.so.%{major_minor}
ln -sf $MPI_LIB/libpsb_base.so.%{version} $RPM_BUILD_ROOT$MPI_LIB/libpsb_base.so

ln -sf $MPI_LIB/libpsb_krylov.so.%{version} $RPM_BUILD_ROOT$MPI_LIB/libpsb_krylov.so.%{major_version}
ln -sf $MPI_LIB/libpsb_krylov.so.%{version} $RPM_BUILD_ROOT$MPI_LIB/libpsb_krylov.so.%{major_minor}
ln -sf $MPI_LIB/libpsb_krylov.so.%{version} $RPM_BUILD_ROOT$MPI_LIB/libpsb_krylov.so

ln -sf $MPI_LIB/libpsb_prec.so.%{version} $RPM_BUILD_ROOT$MPI_LIB/libpsb_prec.so.%{major_version}
ln -sf $MPI_LIB/libpsb_prec.so.%{version} $RPM_BUILD_ROOT$MPI_LIB/libpsb_prec.so.%{major_minor}
ln -sf $MPI_LIB/libpsb_prec.so.%{version} $RPM_BUILD_ROOT$MPI_LIB/libpsb_prec.so

ln -sf $MPI_LIB/libpsb_util.so.%{version} $RPM_BUILD_ROOT$MPI_LIB/libpsb_util.so.%{major_version}
ln -sf $MPI_LIB/libpsb_util.so.%{version} $RPM_BUILD_ROOT$MPI_LIB/libpsb_util.so.%{major_minor}
ln -sf $MPI_LIB/libpsb_util.so.%{version} $RPM_BUILD_ROOT$MPI_LIB/libpsb_util.so
cd ../

install -pm 644 modules/*.mod $RPM_BUILD_ROOT$MPI_FORTRAN_MOD_DIR/%{name}
install -pm 644 include/*.h $RPM_BUILD_ROOT$MPI_INCLUDE/%{name}/
%{_mpich_unload}
popd
%endif
#######################################################

%if 0%{?with_serial}
%files serial
%{_libdir}/*.so.*

%files serial-devel
%{_libdir}/*.so
%{_libdir}/*.a
%{_fmoddir}/%{name}/
%{_includedir}/%{name}/

%if 0%{?arch64}
%files -n %{name}_64
%{_libdir}/libpsb64*.so.*

%files -n %{name}_64-devel
%{_libdir}/libpsb64*.so
%{_libdir}/libpsb64*.a
%{_fmoddir}/%{name}64/
%{_includedir}/%{name}64/
%endif
%endif

%files common
%doc psblas3-%{version}%{?postrelease_version}/README.md psblas3-%{version}%{?postrelease_version}/Changelog
%doc psblas3-%{version}%{?postrelease_version}/ReleaseNews
%doc psblas3-%{version}%{?postrelease_version}/docs/html psblas3-%{version}%{?postrelease_version}/docs/*.pdf
%license psblas3-%{version}%{?postrelease_version}/LICENSE

#######################################################
## MPI versions
%if 0%{?with_openmpi}
%files openmpi
%{_libdir}/openmpi/lib/*.so.*

%files openmpi-devel
%{_libdir}/openmpi/lib/*.so
%{_libdir}/openmpi/lib/*.a
%{_includedir}/openmpi-%{_arch}/%{name}/
%if 0%{?fedora} || 0%{?rhel} > 7
%{_fmoddir}/openmpi/%{name}/
%else
%{_fmoddir}/openmpi-%{_arch}/%{name}/
%endif
%endif

%if 0%{?with_mpich}
%files mpich
%{_libdir}/mpich/lib/*.so.*

%files mpich-devel
%{_libdir}/mpich/lib/*.so
%{_libdir}/mpich/lib/*.a
%{_includedir}/mpich-%{_arch}/%{name}/
%if 0%{?fedora} || 0%{?rhel} > 7
%{_fmoddir}/mpich/%{name}/
%else
%{_fmoddir}/mpich-%{_arch}/%{name}/
%endif
%endif
######################################################

%changelog
* Thu Aug 13 2020 Iñaki Úcar <iucar@fedoraproject.org> - 3.6.1-11
- https://fedoraproject.org/wiki/Changes/FlexiBLAS_as_BLAS/LAPACK_manager

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 18 2020 Antonio Trande <sagitter@fedoraproject.org> - 3.6.1-9
- Release 3.6.1-4

* Sun Jun 28 2020 Antonio Trande <sagitter@fedoraproject.org> - 3.6.1-8
- Release 3.6.1-3

* Sat Apr 11 2020 Antonio Trande <sagitter@fedoraproject.org> - 3.6.1-7
- Fix Fortran optimization compiler flags

* Sat Apr 11 2020 Antonio Trande <sagitter@fedoraproject.org> - 3.6.1-6
- Release 3.6.1-2
- Drop MUMPS as dependency

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 26 2020 Antonio Trande <sagitter@fedoraproject.org> - 3.6.1-4
- Workaround for GCC-10 (-fallow-argument-mismatch)

* Sat Dec 21 2019 Antonio Trande <sagitter@fedoraproject.org> - 3.6.1-3
- Rebuild for MUMPS-5.2.1 on EPEL7

* Fri Dec 20 2019 Antonio Trande <sagitter@fedoraproject.org> - 3.6.1-2
- Use devtoolset-8 on EPEL7

* Fri Dec 20 2019 Antonio Trande <sagitter@fedoraproject.org> - 3.6.1-1
- Release 3.6.1
- Remove format-security flags

* Sun Dec 15 2019 Antonio Trande <sagitter@fedoraproject.org> - 3.6.1-0.2.rc1
- Disable -Wl,--as-needed flags

* Fri Dec 13 2019 Antonio Trande <sagitter@fedoraproject.org> - 3.6.1-0.1.rc1
- Pre-release 3.6.1-rc1

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jul 20 2019 Antonio Trande <sagitter@fedoraproject.org> - 3.6.0-4
- Rebuild for mumps-5.2.1

* Thu Feb 14 2019 Orion Poplawski <orion@nwra.com> - 3.6.0-3
- Rebuild for openmpi 3.1.3

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Dec 04 2018 Antonio Trande <sagitter@fedoraproject.org> - 3.6.0-1
- Release 3.6.0

* Fri Nov 09 2018 Antonio Trande <sagitter@fedoraproject.org> - 3.6.0-0.1
- Pre-release 3.6.0-rc1

* Fri Nov 02 2018 Antonio Trande <sagitter@fedoraproject.org> - 3.5.2-5
- Enable MPI builds

* Fri Nov 02 2018 Antonio Trande <sagitter@fedoraproject.org> - 3.5.2-4
- Update to release 3.5.2-2

* Fri Sep 14 2018 Antonio Trande <sagitter@fedoraproject.org> - 3.5.2-3
- Fix upstream bug #9 (rhbz #1628858)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Antonio Trande <sagitter@fedoraproject.org> - 3.5.2-1
- Update to release 3.5.2

* Wed Apr 11 2018 Antonio Trande <sagitter@fedoraproject.org> - 3.5.1-1
- Update to release 3.5.1

* Sat Feb 17 2018 Antonio Trande <sagitter@fedoraproject.org> - 3.5.0-19
- Use %%ldconfig_scriptlets

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Antonio Trande <sagitter@fedoraproject.org> - 3.5.0-17
- Minor fix post-release 3.5.0-3
- Rebuild for GCC-8

* Thu Dec 07 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.5.0-16
- Hotfix post-release 3.5.0-2

* Sun Nov 12 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.5.0-15
- Update to post-release 3.5.0-1

* Mon Nov 06 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.5.0-14
- Use -Wl,-Bdynamic for linking psb_base library

* Mon Nov 06 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.5.0-13
- Install static libraries
- Use -Wl,-Bdynamic for linking

* Sun Nov 05 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.5.0-12
- libpsb_util serial library linked to Metis/AMD

* Sat Nov 04 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.5.0-11
- Metis/AMD unused by psblas3-serial

* Sat Nov 04 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.5.0-10
- Fix unused-direct-shlib-dependency

* Thu Nov 02 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.5.0-9
- MPI builds activated

* Thu Nov 02 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.5.0-8
- Remove -Wl,--as-needed flag

* Tue Oct 31 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.5.0-7
- Install header files in a private MPI directory

* Sun Oct 29 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.5.0-6
- Fix MPICH fortran links

* Sat Oct 28 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.5.0-5
- Rebuild against openblas

* Fri Oct 27 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.5.0-4
- Fix unused-direct-shlib-dependency warnings

* Thu Oct 26 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.5.0-3
- Fix ldconfig scriptlet

* Thu Oct 26 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.5.0-2
- PSBLAS not compiled on epel6

* Thu Oct 26 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.5.0-1
- Update to 3.5.0 (stable release)
- Rebuilt against blas

* Wed May 31 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.5.0-0.1.rc2
- Update to 3.5.0-rc2

* Fri Feb 10 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.4.1-4
- Packed example files

* Thu Feb 09 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.4.1-3
- Rebuilt against atlas

* Thu Feb 09 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.4.1-2
- Fortran module's directory renamed

* Tue Feb 07 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.4.1-1
- Update to 3.4.1
- Drop obsolete patch

* Fri Feb 03 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.4.0-3
- Rebuild without disable-serial option

* Fri Feb 03 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.4.0-2
- Set MPICH Fortran compiler on RHEL7

* Thu Feb 02 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.4.0-1
- First package

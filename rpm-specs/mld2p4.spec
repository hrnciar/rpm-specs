## Debug builds?
%bcond_with debug
#

%global with_mpich 1
%global with_openmpi 1
%global with_serial 1

# Use devtoolset 8
%if 0%{?rhel} && 0%{?rhel} == 7
%global dts devtoolset-8-
BuildRequires: %{?dts}gcc-gfortran
BuildRequires: %{?dts}gcc, %{?dts}gcc-c++
%endif

%global major_version 2
%global major_minor %{major_version}.2
%global postrelease_version %{nil}

# -Werror=format-security flag is not valid for Fortran
%global fc_optflags $(echo "%optflags" | sed -e 's/-Werror=format-security//')

%global mumps_version 5.3.1

%global libname libmld_prec

Name: mld2p4
Summary: MultiLevel Domain Decomposition Parallel Preconditioners Package based on PSBLAS
Version: %{major_minor}.2
Release: 1%{?dist}
License: BSD
URL: https://github.com/sfilippone/mld2p4-2
Source0: https://github.com/sfilippone/mld2p4-2/archive/v%{version}%{?postrelease_version}/mld2p4-2-%{version}%{?postrelease_version}.tar.gz

BuildRequires: gcc-gfortran
BuildRequires: suitesparse-devel
BuildRequires: openblas-devel, openblas-srpm-macros

%description
The MULTI-LEVEL DOMAIN DECOMPOSITION PARALLEL PRECONDITIONERS PACKAGE BASED
ON PSBLAS (MLD2P4) provides multi-level Schwarz preconditioners,
to be used in the iterative solutions of sparse linear systems:

				Ax=b

where $A$ is a square, real or complex, sparse matrix with a symmetric
sparsity pattern.
These preconditioners have the following general features:

- both additive and hybrid multilevel variants are implemented, i.e.
variants that are additive among the levels and inside each level,
and variants that are multiplicative among the levels and additive inside
each level; the basic Additive Schwarz (AS) preconditioners are obtained by
considering only one level;

- a purely algebraic approach is used to generate a sequence of coarse-level
corrections to a basic AS preconditioner, without explicitly using any
information on the geometry of the original problem
(e.g. the discretization of a PDE).
The smoothed aggregation technique is applied as algebraic coarsening strategy.

%if 0%{?with_serial}
%package serial
Summary: %{name} serial mode
BuildRequires: psblas3-serial-devel >= 3.6.1-6
BuildRequires: MUMPS-devel
BuildRequires: SuperLU-devel
Requires: %{name}-common = %{version}-%{release}
Requires: gcc-gfortran%{?_isa}

%description serial
The MULTI-LEVEL DOMAIN DECOMPOSITION PARALLEL PRECONDITIONERS PACKAGE BASED
ON PSBLAS (MLD2P4) provides multi-level Schwarz preconditioners,
to be used in the iterative solutions of sparse linear systems:

				Ax=b

where $A$ is a square, real or complex, sparse matrix with a symmetric
sparsity pattern.
These preconditioners have the following general features:

- both additive and hybrid multilevel variants are implemented, i.e.
variants that are additive among the levels and inside each level,
and variants that are multiplicative among the levels and additive inside
each level; the basic Additive Schwarz (AS) preconditioners are obtained by
considering only one level;

- a purely algebraic approach is used to generate a sequence of coarse-level
corrections to a basic AS preconditioner, without explicitly using any
information on the geometry of the original problem
(e.g. the discretization of a PDE).
The smoothed aggregation technique is applied as algebraic coarsening strategy.

%package serial-devel
Summary: Development files for %{name}
Requires: %{name}-serial%{?_isa} = %{version}-%{release}
%description serial-devel
Shared links and header files of serial %{name}.
%endif

%package common
Summary: Documentation files for %{name}
BuildArch: noarch
BuildRequires: texlive-tex4ht, texlive-latex, doxygen, ghostscript
BuildRequires: texlive-fancybox, texlive-kpathsea, texlive-metafont
BuildRequires: texlive-mfware
%description common
HTML, PDF and license files of %{name}.

########################################################
%if 0%{?with_openmpi}
%package openmpi
Summary: OpenMPI %{name}
BuildRequires: MUMPS-openmpi-devel
BuildRequires: openmpi-devel
BuildRequires: psblas3-openmpi-devel >= 3.6.1-6
BuildRequires: superlu_dist-openmpi-devel
%if 0%{?rhel} && 0%{?rhel} < 8
BuildRequires: blacs-openmpi-devel
%endif

Requires: openmpi%{?_isa}
Requires: %{name}-common = %{version}-%{release}
Requires: gcc-gfortran%{?_isa}
%description openmpi
The MULTI-LEVEL DOMAIN DECOMPOSITION PARALLEL PRECONDITIONERS PACKAGE BASED
ON PSBLAS (MLD2P4) provides multi-level Schwarz preconditioners,
to be used in the iterative solutions of sparse linear systems:

				Ax=b

where $A$ is a square, real or complex, sparse matrix with a symmetric
sparsity pattern.
These preconditioners have the following general features:

- both additive and hybrid multilevel variants are implemented, i.e.
variants that are additive among the levels and inside each level,
and variants that are multiplicative among the levels and additive inside
each level; the basic Additive Schwarz (AS) preconditioners are obtained by
considering only one level;

- a purely algebraic approach is used to generate a sequence of coarse-level
corrections to a basic AS preconditioner, without explicitly using any
information on the geometry of the original problem
(e.g. the discretization of a PDE).
The smoothed aggregation technique is applied as algebraic coarsening strategy.

%package openmpi-devel
Summary: The %{name} headers and development-related files
Requires: %{name}-openmpi%{?_isa} = %{version}-%{release}
%description openmpi-devel
Shared links, header files for OpenMPI %{name}.
%endif
##########################################################
########################################################
%if 0%{?with_mpich}
%package mpich
Summary: MPICH %{name}
BuildRequires: MUMPS-mpich-devel
BuildRequires: mpich-devel
BuildRequires: psblas3-mpich-devel >= 3.6.1-6
BuildRequires: superlu_dist-mpich-devel
%if 0%{?rhel} && 0%{?rhel} < 8
BuildRequires: blacs-mpich-devel
%endif

Requires: mpich%{?_isa}
Requires: %{name}-common = %{version}-%{release}
Requires: gcc-gfortran%{?_isa}
%description mpich
The MULTI-LEVEL DOMAIN DECOMPOSITION PARALLEL PRECONDITIONERS PACKAGE BASED
ON PSBLAS (MLD2P4) provides multi-level Schwarz preconditioners,
to be used in the iterative solutions of sparse linear systems:

				Ax=b

where $A$ is a square, real or complex, sparse matrix with a symmetric
sparsity pattern.
These preconditioners have the following general features:

- both additive and hybrid multilevel variants are implemented, i.e.
variants that are additive among the levels and inside each level,
and variants that are multiplicative among the levels and additive inside
each level; the basic Additive Schwarz (AS) preconditioners are obtained by
considering only one level;

- a purely algebraic approach is used to generate a sequence of coarse-level
corrections to a basic AS preconditioner, without explicitly using any
information on the geometry of the original problem
(e.g. the discretization of a PDE).
The smoothed aggregation technique is applied as algebraic coarsening strategy.

%package mpich-devel
Summary: The %{name} headers and development-related files
Requires: %{name}-mpich%{?_isa} = %{version}-%{release}
%description mpich-devel
Shared links, header files for MPICH %{name}.
%endif
##########################################################

%prep
%setup -qc -n %{name}-2-%{version}%{?postrelease_version}

mv %{name}-2-%{version}%{?postrelease_version} serial-build

#######################################################
## Copy source for MPI versions
%if 0%{?with_openmpi}
cp -a serial-build openmpi-build
%endif
%if 0%{?with_mpich}
cp -a serial-build mpich-build
%endif
######################################################

%build
%if 0%{?with_serial}
cd serial-build
export LIBBLAS=-lopenblas
export INCBLAS=-I%{_includedir}/openblas

%if 0%{?el7}
%{?dts:source /opt/rh/devtoolset-8/enable}
%endif

%if %{with debug}
export FCFLAGS="-O0 -g -fPIC"
export CFLAGS="-O0 -g -fPIC"
  ./configure --enable-serial --with-fcopt="-O0 -g -fPIC -I%{_fmoddir} $INCBLAS" --with-ccopt="-O0 -g -fPIC $INCBLAS" \
  LDFLAGS="%{__global_ldflags} -fPIC" CPPFLAGS="-I%{_includedir}/psblas3 $INCBLAS" \
%else
export FCFLAGS="%{?fc_optflags} -fPIC"
  %configure --enable-serial --with-fcopt="%{?fc_optflags} -fPIC $INCBLAS" --with-ccopt="%{optflags} -fPIC $INCBLAS" \
  LDFLAGS="%{__global_ldflags} -fPIC" CPPFLAGS="-I%{_includedir}/psblas3 $INCBLAS" \
%endif
  --with-psblas-libdir=%{_libdir} --with-psblas-moddir=%{_fmoddir}/psblas3 --with-psblas-incdir=%{_includedir}/psblas3 \
  --with-blas=$LIBBLAS --with-lapack=$LIBLAPACK \
  --with-mumps="-ldmumps -lcmumps -lsmumps -lzmumps" --with-mumpsincdir="%{_includedir}/MUMPS" \
  --with-mumpsmoddir=%{_fmoddir}/MUMPS-%{mumps_version} \
  --with-superlu=-lsuperlu --with-superluincdir=%{_includedir}/SuperLU \
  --with-umfpack=-lumfpack --with-umfpackincdir=%{_includedir}/suitesparse
#cat config.log
#exit 1
%make_build

# Make shared libraries
pushd lib
gfortran -shared %{__global_ldflags} -Wl,--whole-archive %{libname}.a -Wl,-no-whole-archive -Wl,-Bdynamic -L%{_libdir} $LIBBLAS $LIBLAPACK -lpsb_base -lpsb_prec -ldmumps -lcmumps -lsmumps -lzmumps -lumfpack -lsuperlu -lgfortran -lm -Wl,-soname,%{libname}.so.%{version} -o %{libname}.so.%{version}
popd

cd ../
%endif

#######################################################
## Build MPI versions
%if 0%{?with_openmpi}
pushd openmpi-build

%if 0%{?el7}
%{?dts:source /opt/rh/devtoolset-8/enable}
%endif

%{_openmpi_load}
export CC=mpicc
export LIBBLAS=-lopenblas
export INCBLAS=-I%{_includedir}/openblas
%if %{with debug}
export FCFLAGS="-O0 -g -fPIC"
export CFLAGS="-O0 -g -fPIC"
  ./configure --with-fcopt="-O0 -g -fPIC -I${MPI_FORTRAN_MOD_DIR} $INCBLAS" --with-ccopt="-O0 -g -fPIC $INCBLAS" \
  LDFLAGS="%{__global_ldflags} -fPIC" CPPFLAGS="-I$MPI_INCLUDE/psblas3 $INCBLAS" \
%else
export FCFLAGS="%{?fc_optflags} -fPIC"
  %configure --with-fcopt="%{?fc_optflags} -fPIC $INCBLAS" --with-ccopt="%{optflags} -fPIC $INCBLAS" \
  LDFLAGS="%{__global_ldflags} -fPIC" CPPFLAGS="-I$MPI_INCLUDE/psblas3 $INCBLAS" \
%endif
  MPIFC=mpifort MPICC=mpicc \
  --with-psblas-libdir=$MPI_LIB --with-psblas-moddir=$MPI_FORTRAN_MOD_DIR/psblas3 --with-psblas-incdir=$MPI_INCLUDE/psblas3 \
  --with-blas=$LIBBLAS --with-lapack=$LIBLAPACK \
  --with-mumps="-ldmumps -lcmumps -lsmumps -lzmumps" --with-mumpsincdir="$MPI_INCLUDE/MUMPS" \
  --with-mumpsmoddir=$MPI_FORTRAN_MOD_DIR/MUMPS-%{mumps_version} \
  --with-superludist=-lsuperlu_dist --with-superludistincdir=$MPI_INCLUDE/superlu_dist \
  --with-umfpack=-lumfpack --with-umfpackincdir=%{_includedir}/suitesparse
%make_build

# Make shared libraries
cd lib
mpifort -shared %{__global_ldflags} -Wl,--whole-archive %{libname}.a -Wl,-no-whole-archive -Wl,-Bdynamic -L%{_libdir} $LIBBLAS $LIBLAPACK -lumfpack -lgfortran -lm -L$MPI_LIB -Wl,-rpath -Wl,$MPI_LIB -Wl,--enable-new-dtags -lmpi -lmpi_mpifh -L$MPI_LIB -lpsb_base -lpsb_prec -ldmumps -lcmumps -lsmumps -lzmumps -lsuperlu_dist -Wl,-soname,%{libname}.so.%{version} -o %{libname}.so.%{version}
cd ../
%{_openmpi_unload}
popd
%endif

%if 0%{?with_mpich}
pushd mpich-build

%if 0%{?el7}
%{?dts:source /opt/rh/devtoolset-8/enable}
%endif

%{_mpich_load}
export CC=mpicc
export LIBBLAS=-lopenblas
export INCBLAS=-I%{_includedir}/openblas
%if %{with debug}
export FCFLAGS="-O0 -g -fPIC"
export CFLAGS="-O0 -g -fPIC"
  ./configure --with-fcopt="-O0 -g -fPIC -I${MPI_FORTRAN_MOD_DIR} $INCBLAS" --with-ccopt="-O0 -g -fPIC $INCBLAS" \
  LDFLAGS="%{__global_ldflags} -fPIC" CPPFLAGS="-I$MPI_INCLUDE/psblas3 $INCBLAS" \
%else
export FCFLAGS="%{?fc_optflags} -fPIC"
  %configure --with-fcopt="%{?fc_optflags} -fPIC $INCBLAS" --with-ccopt="%{optflags} -fPIC $INCBLAS" \
  LDFLAGS="%{__global_ldflags} -fPIC" CPPFLAGS="-I$MPI_INCLUDE/psblas3 $INCBLAS" \
%endif
 MPIFC=mpif90 MPICC=mpicc \
  --with-psblas-libdir=$MPI_LIB --with-psblas-moddir=$MPI_FORTRAN_MOD_DIR/psblas3 --with-psblas-incdir=$MPI_INCLUDE/psblas3 \
  --with-blas=$LIBBLAS --with-lapack=$LIBLAPACK \
  --with-mumps="-ldmumps -lcmumps -lsmumps -lzmumps" --with-mumpsincdir="$MPI_FORTRAN_MOD_DIR/MUMPS-%{mumps_version} -I$MPI_INCLUDE/MUMPS" \
  --with-mumpsmoddir=$MPI_FORTRAN_MOD_DIR/MUMPS-%{mumps_version} \
  --with-superludist=-lsuperlu_dist --with-superludistincdir=$MPI_INCLUDE/superlu_dist \
  --with-umfpack=-lumfpack --with-umfpackincdir=%{_includedir}/suitesparse
%make_build

# Make shared libraries
cd lib
mpif90 -shared %{__global_ldflags} -Wl,--whole-archive %{libname}.a -Wl,-no-whole-archive -Wl,-Bdynamic -L%{_libdir} $LIBBLAS $LIBLAPACK -lumfpack  -lgfortran -lm -L$MPI_LIB -Wl,-rpath -Wl,$MPI_LIB -Wl,-z,noexecstack -lmpich -L$MPI_LIB -lpsb_base -lpsb_prec -ldmumps -lcmumps -lsmumps -lzmumps -lsuperlu_dist -Wl,-soname,%{libname}.so.%{version} -o %{libname}.so.%{version}
cd ../
%{_mpich_unload}
popd
%endif

%if 0%{?with_serial}
%ldconfig_scriptlets serial
%endif

%install
%if 0%{?with_serial}
pushd serial-build
mkdir -p $RPM_BUILD_ROOT%{_libdir}
mkdir -p $RPM_BUILD_ROOT%{_includedir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_fmoddir}/%{name}

pushd lib
install -pm 755 *.so.%{version} $RPM_BUILD_ROOT%{_libdir}

ln -sf %{_libdir}/%{libname}.so.%{version} $RPM_BUILD_ROOT%{_libdir}/%{libname}.so.%{major_version}
ln -sf %{_libdir}/%{libname}.so.%{version} $RPM_BUILD_ROOT%{_libdir}/%{libname}.so.%{major_minor}
ln -sf %{_libdir}/%{libname}.so.%{version} $RPM_BUILD_ROOT%{_libdir}/%{libname}.so
popd

install -pm 644 modules/*.mod $RPM_BUILD_ROOT%{_fmoddir}/%{name}/
install -pm 644 include/*.h $RPM_BUILD_ROOT%{_includedir}/%{name}/
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
install -pm 755 *.so.%{version} $RPM_BUILD_ROOT$MPI_LIB

ln -sf $MPI_LIB/%{libname}.so.%{version} $RPM_BUILD_ROOT$MPI_LIB/%{libname}.so.%{major_version}
ln -sf $MPI_LIB/%{libname}.so.%{version} $RPM_BUILD_ROOT$MPI_LIB/%{libname}.so.%{major_minor}
ln -sf $MPI_LIB/%{libname}.so.%{version} $RPM_BUILD_ROOT$MPI_LIB/%{libname}.so
cd ../

install -pm 644 modules/*.mod $RPM_BUILD_ROOT$MPI_FORTRAN_MOD_DIR/%{name}/
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
install -pm 755 *.so.%{version} $RPM_BUILD_ROOT$MPI_LIB

ln -sf $MPI_LIB/%{libname}.so.%{version} $RPM_BUILD_ROOT$MPI_LIB/%{libname}.so.%{major_version}
ln -sf $MPI_LIB/%{libname}.so.%{version} $RPM_BUILD_ROOT$MPI_LIB/%{libname}.so.%{major_minor}
ln -sf $MPI_LIB/%{libname}.so.%{version} $RPM_BUILD_ROOT$MPI_LIB/%{libname}.so
cd ../

install -pm 644 modules/*.mod $RPM_BUILD_ROOT$MPI_FORTRAN_MOD_DIR/%{name}/
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
%{_includedir}/%{name}/
%{_fmoddir}/%{name}/

%files common
%doc serial-build/README* serial-build/Changelog
%doc serial-build/docs/html serial-build/docs/*.pdf
%doc serial-build/ReleaseNews
%license serial-build/LICENSE
%endif

#######################################################
## MPI versions
%if 0%{?with_openmpi}
%files openmpi
%{_libdir}/openmpi/lib/*.so.*

%files openmpi-devel
%{_libdir}/openmpi/lib/*.so
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
%{_includedir}/mpich-%{_arch}/%{name}/
%if 0%{?fedora} || 0%{?rhel} > 7
%{_fmoddir}/mpich/%{name}/
%else
%{_fmoddir}/mpich-%{_arch}/%{name}/
%endif
%endif
######################################################

%changelog
* Sat May 09 2020 Antonio Trande <sagitter@fedoraproject.org> - 2.2.2-1
- Release 2.2.2

* Fri Apr 24 2020 Antonio Trande <sagitter@fedoraproject.org> - 2.2.2-0.1.rc1
- Pre-release 2.2.2-rc1

* Sun Apr 12 2020 Nicolas Chauvet <kwizart@gmail.com> - 2.2.1-7
- Rebuilt for MUMPS 5.3

* Sat Apr 11 2020 Antonio Trande <sagitter@fedoraproject.org> - 2.2.1-6
- Release 2.2.1-1
- Rebuild for MUMPS-5.3.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 05 2020 Antonio Trande <sagitter@fedoraproject.org> - 2.2.1-4
- Force devtoolset-8 linkages

* Sun Jan 05 2020 Antonio Trande <sagitter@fedoraproject.org> - 2.2.1-3
- New rebuild

* Sat Dec 21 2019 Antonio Trande <sagitter@fedoraproject.org> - 2.2.1-2
- Fix MPICH compiler on EPEL7

* Fri Dec 20 2019 Antonio Trande <sagitter@fedoraproject.org> - 2.2.1-1
- Release 2.2.1
- Remove format-security flags
- Use devtoolset-8 on EPEL7

* Sun Dec 15 2019 Antonio Trande <sagitter@fedoraproject.org> - 2.2.1-0.1.rc1
- Release 2.2.1-rc1
- Rebuild for psblas3-3.6.1-rc1

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jul 20 2019 Antonio Trande <sagitter@fedoraproject.org> - 2.2.0-5
- Rebuild for mumps-5.2.1

* Fri Feb 15 2019 Orion Poplawski <orion@nwra.com> - 2.2.0-4
- Rebuild for openmpi 3.1.3

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 16 2019 Antonio Trande <sagitter@fedoraproject.org> - 2.2.0-2
- Release 2.2.0-4

* Fri Dec 14 2018 Antonio Trande <sagitter@fedoraproject.org> - 2.2.0-1
- Release 2.2.0-3

* Fri Nov 09 2018 Antonio Trande <sagitter@fedoraproject.org> - 2.2.0-0.1
- Pre-release 2.2.0-rc1

* Mon Sep 17 2018 Antonio Trande <sagitter@fedoraproject.org> - 2.1.1-2
- Rebuild for psblas3-3.5.2 +bugfix

* Sun Sep 16 2018 Antonio Trande <sagitter@fedoraproject.org> - 2.1.1-1
- Release 2.1.1

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-0.10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Antonio Trande <sagitter@fedoraproject.org> - 2.1.1-0.9
- Rebuild for psblas3-3.5.2

* Wed Apr 25 2018 Antonio Trande <sagitter@fedoraproject.org> - 2.1.1-0.8
- Rebuild after SuperLU-5.2.1 fixing

* Tue Apr 24 2018 Antonio Trande <sagitter@fedoraproject.org> - 2.1.1-0.7
- Rebuild for SuperLU-5.2.1

* Wed Apr 11 2018 Antonio Trande <sagitter@fedoraproject.org> - 2.1.1-0.6
- Rebuild for psblas3-3.5.1

* Wed Mar 07 2018 Adam Williamson <awilliam@redhat.com> - 2.1.1-0.5
- Rebuild to fix GCC 8 mis-compilation
  See https://da.gd/YJVwk ("GCC 8 ABI change on x86_64")

* Sat Feb 17 2018 Antonio Trande <sagitter@fedoraproject.org> - 2.1.1-0.4
- Use %%ldconfig_scriptlets

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 30 2018 Antonio Trande <sagitter@fedoraproject.org> - 2.1.1-0.2
- Pre-release 2.1.1-rc2

* Sat Jan 27 2018 Antonio Trande <sagitter@fedoraproject.org> - 2.1.1-0.1.20180127git147f37
- Pre-release 2.1.1

* Thu Nov 23 2017 Antonio Trande <sagitter@fedoraproject.org> - 2.1.0-6
- Force gfortran to use -Wl,--as-needed

* Sun Nov 05 2017 Antonio Trande <sagitter@fedoraproject.org> - 2.1.0-5
- Linked to 'c' 's' 'z' mumps libraries
- Use -Wl,-Bdynamic for linking

* Wed Nov 01 2017 Antonio Trande <sagitter@fedoraproject.org> - 2.1.0-4
- Set debug builds

* Sat Oct 28 2017 Antonio Trande <sagitter@fedoraproject.org> - 2.1.0-3
- Rebuild against openblas

* Fri Oct 27 2017 Antonio Trande <sagitter@fedoraproject.org> - 2.1.0-2
- Set links for minimun required libs of MUMPS

* Thu Oct 26 2017 Antonio Trande <sagitter@fedoraproject.org> - 2.1.0-1
- Update to 2.1.0 (stable release)
- Rebuilt against blas

* Wed May 31 2017 Antonio Trande <sagitter@fedoraproject.org> - 2.1.0-0.6.rc1
- Compile against superlu_dist

* Wed May 31 2017 Antonio Trande <sagitter@fedoraproject.org> - 2.1.0-0.5.rc1
- Update to 2.1.0-rc1

* Fri Feb 10 2017 Antonio Trande <sagitter@fedoraproject.org> - 2.1-0.4
- Rebuild new source code

* Fri Feb 03 2017 Antonio Trande <sagitter@fedoraproject.org> - 2.1-0.3
- Rebuild without disable-serial option
- Packed examples and tests

* Fri Feb 03 2017 Antonio Trande <sagitter@fedoraproject.org> - 2.1-0.2
- Set MPICH Fortran compiler on RHEL7

* Thu Feb 02 2017 Antonio Trande <sagitter@fedoraproject.org> - 2.1-0.1
- First package

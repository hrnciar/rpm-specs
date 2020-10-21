# Warning:
# Anyone editing this spec file please make sure the same spec file
# works on other fedora and epel releases, which are supported by this software.
# No quick Rawhide-only fixes will be allowed.

%if 0%{?el6}
unsupported https://gitlab.com/QEF/q-e/issues/113
%quit
%endif

# missing on el6
%{?!_fmoddir: %global _fmoddir %{_libdir}/gfortran/modules}

%if 0%{?fedora} >= 32
%global extra_gfortran_flags -fallow-argument-mismatch
%else
%global extra_gfortran_flags %{nil}
%endif

%if 0%{?fedora} || 0%{?el8}
%global python python3
%else
%global python python
%endif

%if 0%{?fedora} >= 33 || 0%{?rhel} >= 9
%global blaslib flexiblas
%else
%global blaslib openblas
%endif

%if 0%{?el6}
# el6/ppc64 Error: No Package found for mpich-devel
ExclusiveArch:		x86_64 %{ix86}
%else
%{!?openblas_arches:%global openblas_arches x86_64 %{ix86} armv7hl %{power64} aarch64}
# qe-6.4.1 fails to find openblas, fftw on other %%{openblas_arches} than those below
ExclusiveArch:		x86_64 %{ix86}
%endif

# disable compilation warnings
%global wnoflags -Wno-unused-variable -Wno-conversion -Wno-unused-dummy-argument -Wno-character-truncation -Wno-missing-include-dirs -Wno-unused-function -Wno-maybe-unitialized

Name:			quantum-espresso
Version:		6.5
Release:		4%{?dist}
Summary:		A suite for electronic-structure calculations and materials modeling

Provides:               bundled(FoXlibf)

License:		GPLv2+
# BSD: PP/src/bgw2pw.f90
# BSD: PP/src/pw2bgw.f90
# LGPLv2+: Modules/bspline.f90
# LGPLv2+: Modules/libxc.f90
# LGPLv2+: install/iotk_config.h
# MIT: install/install-sh
# zlib/libpng: clib/md5.c
# zlib/libpng: clib/md5.h
URL:			http://www.quantum-espresso.org/
Source0:		https://github.com/QEF/q-e/archive/qe-%{version}.tar.gz

# pseudopotentials not included in the source and needed by PW/tests
# cd test-suite && make pseudo  # then remove those included in the source
Source1:		pseudo.tar.gz

# handle license on el{6,7}: global must be defined after the License field above
%{!?_licensedir: %global license %doc}

BuildRequires:		make
%if 0%{?fedora} || 0%{?el8}
BuildRequires:		python3
BuildRequires:		python3-numpy
%else
BuildRequires:		python
BuildRequires:		numpy
%endif
BuildRequires:		gcc-gfortran
BuildRequires:		%{blaslib}-devel
BuildRequires:		fftw3-devel

BuildRequires:		openssh-clients

Requires:		openssh-clients

%global desc_base \
QUANTUM ESPRESSO is an integrated suite of Open-Source computer codes for\
electronic-structure calculations and materials modeling at the nanoscale.\
It is based on density-functional theory, plane waves, and pseudopotentials.


%description
%{desc_base}

Serial version. Includes iotk executables.


%package devel
Summary:		%{name} - devel

%description devel
%{desc_base}

This package contains modules and headers.


%package static
Summary:		%{name} - static libraries

%description static
%{desc_base}

This package contains static libraries.


%package openmpi
Summary:		%{name} - openmpi version
BuildRequires:		openmpi-devel
BuildRequires:		scalapack-openmpi-devel
Requires:		openmpi
%if 0%{?el6}
BuildRequires:		scalapack-openmpi
BuildRequires:		blacs-openmpi
%endif
%if 0%{?el7} || 0%{?el6}
Requires:		scalapack-openmpi
Requires:		blacs-openmpi
%endif

%description openmpi
%{desc_base}

This package contains the openmpi version.


%package openmpi-devel
Summary:		%{name} - devel openmpi version
BuildRequires:		openmpi
Requires:		openmpi

%description openmpi-devel
%{desc_base}

This package contains modules and headers for openmpi.


%package openmpi-static
Summary:		%{name} - static libraries openmpi version
BuildRequires:		openmpi
Requires:		openmpi

%description openmpi-static
%{desc_base}

This package contains static libraries for openmpi.


%package mpich
Summary:		%{name} - mpich version
BuildRequires:		mpich-devel
BuildRequires:		scalapack-mpich-devel
Requires:		mpich
%if 0%{?el6}
BuildRequires:		scalapack-mpich
BuildRequires:		blacs-mpich
%endif
%if 0%{?el7} || 0%{?el6}
Requires:		scalapack-mpich
Requires:		blacs-mpich
%endif

%description mpich
%{desc_base}

This package contains the mpich version.


%package mpich-devel
Summary:		%{name} - devel mpich version
BuildRequires:		mpich
Requires:		mpich

%description mpich-devel
%{desc_base}

This package contains modules and headers for mpich.


%package mpich-static
Summary:		%{name} - static libraries mpich version
BuildRequires:		mpich
Requires:		mpich

%description mpich-static
%{desc_base}

This package contains static libraries for mpich.


%prep
%setup -q -n q-e-qe-%{version}

# remove bundled libraries
rm -rf archive/lapack*gz
rm -rf archive/blas*gz
rm -rf archive/ELPA*gz

# use specified compiler flags
sed -i 's|@fflags@|@cflags@|' install/make.inc.in
# build exx
sed -i 's|MANUAL_DFLAGS  =|MANUAL_DFLAGS  = -DEXX|' install/make.inc.in
# workaround to compile UtilXlib/mp.f90 "Type mismatch between actual argument at (1) and actual argument at (2)"
sed -i 's|MANUAL_DFLAGS  =|MANUAL_DFLAGS  = %{extra_gfortran_flags}|' install/make.inc.in

# Horror! Tests use $HOME/tmp or /tmp by default!
sed -i 's#TMP_DIR=.*#TMP_DIR=./tmp#' environment_variables
sed -i 's#ESPRESSO_TMPDIR=.*#ESPRESSO_TMPDIR=./tmp#' test-suite/ENVIRONMENT
# NO network access during build!
sed -i 's#NETWORK_PSEUDO=.*#NETWORK_PSEUDO=/dev/null#' environment_variables
sed -i 's#NETWORK_PSEUDO=.*#NETWORK_PSEUDO=/dev/null#' test-suite/ENVIRONMENT
# must set ESPRESSO_ROOT explicitly
sed -i "s#ESPRESSO_ROOT=.*#ESPRESSO_ROOT=${PWD}#" test-suite/ENVIRONMENT
# set TESTCODE_NPROCS
sed -i "s#TESTCODE_NPROCS=.*#TESTCODE_NPROCS=2#" test-suite/ENVIRONMENT
# increase test verbosity
sed -i "s#--verbose#-vvv#" test-suite/Makefile
# bash uses source and not include
sed -i "s#include #source #" test-suite/run-cp.sh
sed -i "s#include #source #" test-suite/run-pw.sh
# don't use python2
sed -i "s#python2#%{python}#" test-suite/testcode/bin/testcode.py

# remove -D__XLF on ppc64
# http://qe-forge.org/pipermail/pw_forum/2009-January/085834.html
sed -i '/D__XLF/d' install/configure
# remove -D__LINUX_ESSL on ppc64
sed -i 's/try_dflags -D__LINUX_ESSL/try_dflags/' install/configure
sed -i 's/have_essl=1/have_essl=0/' install/configure

# FoX needs -fPIC on f31
sed -i 's|FOX_FLAGS =|FOX_FLAGS = -fPIC|' install/make.inc.in

# Enable discovery of flexiblas
sed -i 's/openblas/openblas flexiblas/' install/configure


%build
# Have to do off-root builds to be able to build many versions at once
mv install install.orig

# To avoid replicated code define a macro
%global dobuild() \
mkdir -p bin$MPI_SUFFIX&& \
mkdir -p iotk$MPI_SUFFIX&& \
if test -z "$MPI_SUFFIX"; then MPIF90='gfortran %{extra_gfortran_flags} %{optflags}'; CONFIGURE='--disable-parallel'; fi&& \
if test -n "$MPI_SUFFIX"; then MPIF90='mpif90 %{extra_gfortran_flags} %{optflags}'; CONFIGURE='--enable-parallel --with-scalapack=yes --with-elpa=no'; fi&& \
if [ "$MPI_SUFFIX" == "_openmpi" ] && [ -r "$MPI_LIB/libmpi_f90.so" ]; then export LIBMPI='-lmpi -lmpi_f90 -lmpi_f77'; fi&& \
if [ "$MPI_SUFFIX" == "_openmpi" ] && [ -r "$MPI_LIB/libmpi_usempi.so" ]; then export LIBMPI='-lmpi -lmpi_usempi -lmpi_mpifh'; fi&& \
if [ "$MPI_SUFFIX" == "_openmpi" ] && [ -r "$MPI_LIB/libmpi_usempif08.so" ]; then export LIBMPI='-lmpi -lmpi_usempif08 -lmpi_mpifh'; fi&& \
if [ "$MPI_SUFFIX" == "_mpich2" ]; then export LIBMPI='-lmpich'; fi&& \
if [ "$MPI_SUFFIX" == "_mpich" ]; then export LIBMPI='-lmpich'; fi&& \
    CC=gcc \
    CXX=c++ \
    F90='gfortran %{extra_gfortran_flags} %{optflags}' \
    MPIF90='$MPIF90 %{extra_gfortran_flags} %{optflags}' \
    FCFLAGS='%{extra_gfortran_flags} %{optflags}' \
    CFLAGS='%{extra_gfortran_flags} %{optflags} %{wnoflags}' \
    FFLAGS='%{extra_gfortran_flags} %{optflags}' \
    BLAS_LIBS='-l%{blaslib}' \
    LAPACK_LIBS='-l%{blaslib}' \
    FFT_LIBS='-lfftw3' \
    MPI_LIBS="-L${MPI_LIB} $LIBMPI" \
    SCALAPACK_LIBS="-L${MPI_LIB} -lscalapack" \
    %{_configure} $CONFIGURE&& \
%{__make} all&& \
for f in bin/*; do cp -pL $f bin$MPI_SUFFIX/`basename ${f}`; done&& \
if test -d upftools; then for f in upftools/*.x; do cp -pL $f bin$MPI_SUFFIX/`basename ${f}`; done; fi&& \
cp -pL iotk/src/libiotk.a iotk/src/*.mod iotk$MPI_SUFFIX&& \
%{__make} clean


# build openmpi version
cp -rp install.orig install
%{_openmpi_load}
%dobuild
%{_openmpi_unload}
rm -rf install

# build mpich version
cp -rp install.orig install
%{_mpich_load}
%dobuild
%{_mpich_unload}
rm -rf install

# build serial version
cp -rp install.orig install
MPI_SUFFIX=_serial %dobuild


%install

# To avoid replicated code define a macro
%global doinstall() \
mkdir -p $RPM_BUILD_ROOT/$MPI_BIN&& \
mkdir -p $RPM_BUILD_ROOT/$MPI_LIB&& \
mkdir -p $RPM_BUILD_ROOT/$MPI_FORTRAN_MOD_DIR&& \
for f in bin$MPI_SUFFIX/*; do install -p -m 755 ${f} $RPM_BUILD_ROOT/$MPI_BIN/`basename ${f}`$EXE_SUFFIX; done&& \
install -p -m 755 iotk$MPI_SUFFIX/*.a $RPM_BUILD_ROOT/$MPI_LIB&& \
install -p -m 755 iotk$MPI_SUFFIX/*.mod $RPM_BUILD_ROOT/$MPI_FORTRAN_MOD_DIR

# install openmpi version
%{_openmpi_load}
EXE_SUFFIX=$MPI_SUFFIX %doinstall
%{_openmpi_unload}

# install mpich version
%{_mpich_load}
EXE_SUFFIX=$MPI_SUFFIX %doinstall
# https://bugzilla.redhat.com/show_bug.cgi?id=1154991
mkdir -p $RPM_BUILD_ROOT%{_fmoddir}/mpich%{?_cc_name_suffix}
if test -d $RPM_BUILD_ROOT%{_includedir}/mpich-%{_arch}%{?_cc_name_suffix};
then
mv -f $RPM_BUILD_ROOT%{_includedir}/mpich-%{_arch}%{?_cc_name_suffix}/* $RPM_BUILD_ROOT%{_fmoddir}/mpich%{?_cc_name_suffix}
rm -rf $RPM_BUILD_ROOT%{_includedir}
fi
%{_mpich_unload}

# install serial version
EXE_SUFFIX="" MPI_SUFFIX="_serial" MPI_BIN=%{_bindir} MPI_LIB=%{_libdir} MPI_FORTRAN_MOD_DIR=%{_fmoddir} %doinstall


%check

# clean removes all extra pseudo - must copy them now
tar zxf %{SOURCE1}

%if 0%{?el6}
export TIMEOUT_OPTS='3600'
%else
export TIMEOUT_OPTS='--preserve-status --kill-after 10 1800'
%endif

# To avoid replicated code define a macro
%global docheck() \
ldd bin$MPI_SUFFIX/pw.x && \
cp -rp test-suite.orig test-suite&& \
pushd test-suite&& \
for script in run-*.sh; do \
sed -i "s<}/bin/<}/bin$MPI_SUFFIX/<" ${script}&& \
sed -i "s<}/PW/src/<}/bin$MPI_SUFFIX/<" ${script}; \
done&& \
if [ $MPI_SUFFIX == _serial ]; then \
timeout ${TIMEOUT_OPTS} %{__make} run-tests-serial 2>&1 | tee ../tests$MPI_SUFFIX.log \
else \
timeout ${TIMEOUT_OPTS} %{__make} run-tests-parallel 2>&1 | tee ../tests$MPI_SUFFIX.log \
fi&& \
popd&& \
cat test-suite/pw_atom/test* && \
rm -rf test-suite

mv test-suite test-suite.orig

# check serial version
MPI_SUFFIX=_serial %docheck

# check openmpi version
%{_openmpi_load}
which mpirun
%docheck
%{_openmpi_unload}

# this will fail for mpich2 on el6 - mpd would need to be started ...
# check mpich version
%{_mpich_load}
which mpirun
%docheck
%{_mpich_unload}

# restore tests
mv test-suite.orig test-suite


%files
%license License
%{_bindir}/*.x
%{_bindir}/iotk


%files devel
%license License
%{_fmoddir}/iotk*.mod


%files static
%license License
%{_libdir}/libiotk.a


%files openmpi
%license License
%{_libdir}/openmpi%{?_opt_cc_suffix}/bin/*.x_openmpi
%{_libdir}/openmpi%{?_opt_cc_suffix}/bin/iotk_openmpi


%files openmpi-devel
%license License
# https://bugzilla.redhat.com/show_bug.cgi?id=1154982
%if 0%{?el6} || 0%{?el7}
%{_fmoddir}/openmpi%{?_cc_name_suffix}-%{_arch}/iotk*.mod
%else
%{_fmoddir}/openmpi%{?_cc_name_suffix}/iotk*.mod
%endif


%files openmpi-static
%license License
%{_libdir}/openmpi%{?_cc_name_suffix}/lib/libiotk.a


%files mpich
%license License
%{_libdir}/mpich%{?_opt_cc_suffix}/bin/*.x_mpich
%{_libdir}/mpich%{?_opt_cc_suffix}/bin/iotk_mpich


%files mpich-devel
%license License
# https://bugzilla.redhat.com/show_bug.cgi?id=1154982
%if 0%{?el6} || 0%{?el7}
%{_fmoddir}/mpich%{?_cc_name_suffix}-%{_arch}/iotk*.mod
%else
%{_fmoddir}/mpich%{?_cc_name_suffix}/iotk*.mod
%endif


%files mpich-static
%license License
%{_libdir}/mpich%{?_cc_name_suffix}/lib/libiotk.a


%changelog
* Fri Aug 28 2020 Iñaki Úcar <iucar@fedoraproject.org> - 6.5-4
- https://fedoraproject.org/wiki/Changes/FlexiBLAS_as_BLAS/LAPACK_manager

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Mar 02 2020 Marcin Dulak <Marcin.Dulak@gmail.com> - 6.5-2
- python and numpy br for epel8

* Fri Feb 14 2020 Marcin Dulak <Marcin.Dulak@gmail.com> - 6.5-1
- new upstream release
- -fallow-argument-mismatch fix for gfortran 10
- fix serial and parallel test-suite build (use 1 and 2 processors respectively)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 17 2019 Marcin Dulak <Marcin.Dulak@gmail.com> - 6.4.1-1
- new upstream release
- kill hanging tests after timeout
- disable failed architectures: configure fails to find openblas, fftw on other %%{openblas_arches} than x86_64 %%{ix86}

* Thu Feb 14 2019 Orion Poplawski <orion@nwra.com> - 5.4.0-20
- Rebuild for openmpi 3.1.3

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 02 2018 Iryna Shcherbina <shcherbina.iryna@gmail.com> - 5.4.0-17
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Mar 07 2018 Adam Williamson <awilliam@redhat.com> - 5.4.0-16
- Rebuild to fix GCC 8 mis-compilation
  See https://da.gd/YJVwk ("GCC 8 ABI change on x86_64")

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Oct 21 2016 Orion Poplawski <orion@cora.nwra.com> - 5.4.0-11
- Rebuild for openmpi 2.0

* Fri Sep 16 2016 Marcin Dulak <Marcin.Dulak@gmail.com> - 5.4.0-10
- upsteam update
- speedup the tests by running on single core so koji %%{arm} builds finish within the timeout (bug #1356620)
- get rid of D__XLF and D__LINUX_ESSL on ppc64

* Tue Sep  6 2016 Peter Robinson <pbrobinson@fedoraproject.org> 5.3.0-9
- Sync openblas ExclusiveArch

* Thu Feb 18 2016 Marcin Dulak <Marcin.Dulak@gmail.com> - 5.3.0-8
- use only 2 cores for tests (bug #1308481)
- defattr removed

* Sat Feb 13 2016 Marcin Dulak <Marcin.Dulak@gmail.com> - 5.3.0-7
- explicit Requires are needed for scalapack, blacs on el6 (bug #1301922)
    
* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 12 2016 Marcin Dulak <Marcin.Dulak@gmail.com> 5.3.0-5
- upsteam update
- switch to test-suite
- no more upftools?

* Mon Jan  4 2016 Marcin Dulak <Marcin.Dulak@gmail.com> 5.2.1-4
- disable compilation warnings
- use lua for copying pseudos
- removed common package

* Sat Dec 19 2015 Marcin Dulak <Marcin.Dulak@gmail.com> 5.2.1-3
- fix ExclusiveArch
- license is GPLv2+
- OMP_NUM_THREADS removed
- use %%{optflags}

* Fri Dec 18 2015 Dave Love <loveshack@fedoraproject.org> - 5.2.1-2
- Require %%{name}-common, not %%{name}-common%%{?_isa}

* Wed Dec 16 2015 Marcin Dulak <Marcin.Dulak@gmail.com> 5.1.2-1
- initial build


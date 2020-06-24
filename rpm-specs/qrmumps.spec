# Testing
%ifnarch %{arm}
%global with_check 1
%endif

Name: qrmumps
Version: 2.0
Release: 19%{?dist}
Summary: A multithreaded multifrontal QR solver
License: LGPLv3+
URL: http://buttari.perso.enseeiht.fr/qr_mumps/

# This is a private source link provided by upstream directly
Source0: http://buttari.perso.enseeiht.fr/qr_mumps/releases/%{version}/qr_mumps-%{version}.tgz

# Custom Makefile changed for Fedora and built from Make.inc/Makefile.gfortran.PAR in the source.
Source1: %{name}-Makefile.inc

Patch0: %{name}-gcc10.patch

# Files for testing
Source2: http://www.cise.ufl.edu/research/sparse/MM/vanHeukelum/cage6.tar.gz
Source3: http://www.cise.ufl.edu/research/sparse/MM/Meszaros/pltexpa.tar.gz
Source4: http://www.cise.ufl.edu/research/sparse/MM/Yoshiyasu/image_interp.tar.gz

BuildRequires: gcc-gfortran
%ifarch %{openblas_arches}
BuildRequires: openblas-devel
%else
BuildRequires: blas-devel
BuildRequires: lapack-devel
%endif
BuildRequires: metis-devel >= 5.1.0-12
BuildRequires: scotch-devel
BuildRequires: suitesparse-devel
BuildRequires: perl-devel
%if 0%{?fedora}
BuildRequires: perl-generators
%endif

Requires: gcc-gfortran%{?_isa}

Provides: qr_mumps = 0:%{version}-%{release}
Obsoletes: qr_mumps < 0:2.0-4

%description
qr_mumps is a software package for the solution of sparse,
linear systems on multicore computers.
It implements a direct solution method based on the QR
factorization of the input matrix. Therefore, it is suited
to solving sparse least-squares problems and to computing
the minimum-norm solution of sparse, underdetermined problems.
It can obviously be used for solving square problems in which
case the stability provided by the use of orthogonal transformations
comes at the cost of a higher operation count with respect to solvers
based on, e.g., the LU factorization.
qr_mumps supports real and complex, single or double precision arithmetic.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
Shared links and header files of %{name}.

%package doc
Summary: PDF documentation files of %{name}
BuildArch: noarch
%description doc
PDF documentation files of %{name}.

########################################################

%prep
%autosetup -n qr_mumps-%{version} -p1

cp -p %{SOURCE1} makeincs/Make.inc.fedora

%build

%ifarch %{openblas_arches}
export LIBBLAS=-lopenblas
export INCBLAS=-I%{_includedir}/openblas
%else
export LIBBLAS=-lblas
export LIBLAPACK=-llapack
export INCBLAS=-I%{_includedir}
%endif

# Parallel Make is not supported
make BUILD=build PLAT=fedora ARITH='d s c z' \
 topdir=$PWD \
 CC=gcc \
 FC=gfortran \
 FCFLAGS="%{build_fflags} -Wno-unused-variable -fopenmp -fPIC" \
 CFLAGS="%{build_cflags} -fopenmp -fPIC" \
 CDEFS=" -Dhave_metis -Dhave_scotch -Dhave_colamd" \
 FDEFS=" -Dhave_metis -Dhave_scotch -Dhave_colamd" \
 LCOLAMD=-lcolamd \
 ICOLAMD=" -I%{_includedir}/suitesparse" \
 LBLAS=$LIBBLAS \
 LLAPACK=$LIBLAPACK \
 LMETIS=" -lmetis" \
 IMETIS=" -I%{_includedir}" \
 LSCOTCH=" -lscotch -lscotcherr" \
 ISCOTCH=" -I%{_includedir}"

# Make shared libraries
pushd build/lib

export LCOLAMD=-lcolamd
export LMETIS=-lmetis
export LSCOTCH="-lscotch -lscotcherr"

gfortran -shared %{__global_ldflags} -fPIC -Wl,-z,now -Wl,--whole-archive libqrm_common.a -Wl,-no-whole-archive -L%{_libdir} $LMETIS $LCOLAMD -lgfortran -lm -Wl,-soname,libqrm_common.so.%{version} -o libqrm_common.so.%{version}

gfortran -shared %{__global_ldflags} -fPIC -Wl,-z,now -Wl,--whole-archive libdqrm.a libqrm_common.a -Wl,-no-whole-archive -L./ -lqrm_common -L%{_libdir} $LIBBLAS $LIBLAPACK $LSCOTCH $LMETIS $LCOLAMD -lgfortran -lm -Wl,-soname,libdqrm.so.%{version} -o libdqrm.so.%{version}

gfortran -shared %{__global_ldflags} -fPIC -Wl,-z,now -Wl,--whole-archive libcqrm.a libqrm_common.a -Wl,-no-whole-archive -L./ -lqrm_common -L%{_libdir} $LIBBLAS $LIBLAPACK $LSCOTCH $LMETIS $LCOLAMD -lgfortran -lm -Wl,-soname,libcqrm.so.%{version} -o libcqrm.so.%{version}

gfortran -shared %{__global_ldflags} -fPIC -Wl,-z,now -Wl,--whole-archive libzqrm.a libqrm_common.a -Wl,-no-whole-archive -L./ -lqrm_common -L%{_libdir} $LIBBLAS $LIBLAPACK $LSCOTCH $LMETIS $LCOLAMD -lgfortran -lm -Wl,-soname,libzqrm.so.%{version} -o libzqrm.so.%{version}

gfortran -shared %{__global_ldflags} -fPIC -Wl,-z,now -Wl,--whole-archive libsqrm.a libqrm_common.a -Wl,-no-whole-archive -L./ -lqrm_common -L%{_libdir} $LIBBLAS $LIBLAPACK $LSCOTCH $LMETIS $LCOLAMD -lgfortran -lm -Wl,-soname,libsqrm.so.%{version} -o libsqrm.so.%{version}
popd

%ldconfig_scriptlets

%if 0%{?with_check}
%check
pushd build/testing

%ifarch %{openblas_arches}
export LIBBLAS=-lopenblas
export INCBLAS=-I%{_includedir}/openblas
%else
export LIBBLAS=-lblas
export LIBLAPACK=-llapack
export INCBLAS=-I%{_includedir}
%endif

make BUILD=./ PLAT=fedora ARITH='d s c z' \
 topdir=../../ \
 CC=gcc \
 FC=gfortran \
 FCFLAGS="-O0 -g -Wno-unused-variable -I%{_fmoddir} -fopenmp -fPIC -Wl,-z,now" \
 CFLAGS="-O0 -g -fopenmp -fPIC -Wl,-z,now" \
 CDEFS=" -Dhave_metis -Dhave_scotch -Dhave_colamd" \
 FDEFS=" -Dhave_metis -Dhave_scotch -Dhave_colamd" \
 LCOLAMD=-lcolamd \
 ICOLAMD=" -I%{_includedir}/suitesparse" \
 LBLAS=$LIBBLAS \
 LLAPACK=$LIBLAPACK \
 LMETIS=" -lmetis" \
 IMETIS=" -I%{_includedir}" \
 LSCOTCH=" -lscotch -lscotcherr" \
 ISCOTCH=" -I%{_includedir}"

echo 3 > matfile.txt
tar -zxf %{SOURCE2}; echo cage6/cage6.mtx >> matfile.txt
tar -zxf %{SOURCE3}; echo pltexpa/pltexpa.mtx >> matfile.txt
tar -zxf %{SOURCE4}; echo image_interp/image_interp.mtx >> matfile.txt

export LD_LIBRARY_PATH=$RPM_BUILD_ROOT%{_libdir}:%{_libdir}
export QRM_NUM_THREADS=2
./dqrm_testing
./sqrm_testing
./cqrm_testing
./zqrm_testing
%endif

%install
mkdir -p $RPM_BUILD_ROOT%{_includedir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_fmoddir}/%{name}

pushd build/lib
install -pm 755 *.so.%{version} $RPM_BUILD_ROOT%{_libdir}

ln -sf %{_libdir}/libqrm_common.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libqrm_common.so.2
ln -sf %{_libdir}/libqrm_common.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libqrm_common.so

ln -sf %{_libdir}/libdqrm.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libdqrm.so.2
ln -sf %{_libdir}/libdqrm.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libdqrm.so

ln -sf %{_libdir}/libcqrm.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libcqrm.so.2
ln -sf %{_libdir}/libcqrm.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libcqrm.so

ln -sf %{_libdir}/libzqrm.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libzqrm.so.2
ln -sf %{_libdir}/libzqrm.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libzqrm.so

ln -sf %{_libdir}/libsqrm.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libsqrm.so.2
ln -sf %{_libdir}/libsqrm.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libsqrm.so
popd

install -pm 644 build/include/*.h $RPM_BUILD_ROOT%{_includedir}/%{name}/
install -pm 644 build/include/*.mod $RPM_BUILD_ROOT%{_fmoddir}/%{name}/

%files
%license doc/COPYING.LESSER
%doc Changelog.org
%{_libdir}/lib*qrm.so.*
%{_libdir}/libqrm_common.so.*

%files devel
%{_includedir}/%{name}/
%{_fmoddir}/%{name}/
%{_libdir}/lib*qrm.so
%{_libdir}/libqrm_common.so

%files doc
%license doc/COPYING.LESSER
%doc doc/pdf/*.pdf

%changelog
* Mon Feb 03 2020 Antonio Trande <sagitter@fedoraproject.org> - 2.0-19
- Patched for GCC 10

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 26 2020 Antonio Trande <sagitter@fedoraproject.org> - 2.0-17
- Workaround for GCC 10 (-fallow-argument-mismatch)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 19 2018 Sandro Mani <manisandro@gmail.com> - 2.0-14
- Rebuild (scotch)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Feb 17 2018 Antonio Trande <sagitter@fedoraproject.org> - 2.0-12
- Use %%ldconfig_scriptlets

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Antonio Trande <sagitterATfedoraproject.org> - 2.0-10
- Rebuild for GCC-8
- Disable tests

* Sat Nov 04 2017 Antonio Trande <sagitterATfedoraproject.org> - 2.0-9
- Rebuild against openblas except s390x/arm arches
- Set a custom macro for openblas arches
- Rebuild against COLAMD

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 31 2017 Antonio Trande <sagitterATfedoraproject.org> - 2.0-5
- Rebuild for gcc-gfortran

* Sun Dec 04 2016 Antonio Trande <sagitterATfedoraproject.org> - 2.0-4
- Package renamed as qrmumps for packaging needs
- Set Provides Obsoletes tags
- License changed to LGPLv3+

* Thu Jul 07 2016 Antonio Trande <sagitterATfedoraproject.org> - 2.0-3
- Fix symbolic links
- Fix unused-direct-shlib-dependency warnings

* Thu Jul 07 2016 Antonio Trande <sagitterATfedoraproject.org> - 2.0-2
- Fix %%doc line

* Thu Jul 07 2016 Antonio Trande <sagitterATfedoraproject.org> - 2.0-1
- Update to 2.0

* Mon Mar 07 2016 Antonio Trande <sagitterATfedoraproject.org> - 1.2-3
- Fixed ln commands

* Fri Feb 19 2016 Antonio Trande <sagitterATfedoraproject.org> - 1.2-2
- Use Conditional Builds macro
- Remove pkgconfig BR

* Sat Feb 13 2016 Antonio Trande <sagitterATfedoraproject.org> - 1.2-1
- Initial package

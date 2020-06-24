%global tarname FreeFem-sources
%global tarvers 4.6

%bcond_without serial

# Allow disabling building with/against openmpi
# Build with --without openmpi to not build openmpi
%bcond_without openmpi

# Allow disabling building with/against mpich
# Build with --without openmpi to not build mpich
%bcond_without mpich

# Don't exercise %%check on the archs below.
# They fail/hang for yet undetermined causes.
# Build with --with checks to force building them.
# Build with --without checks to skip building them.
%ifarch ppc64le aarch64 s390x armv7hl
%bcond_with checks
%else
%bcond_without checks
%endif

Summary: PDE solving tool
Name: freefem++
Version: %{expand:%(echo %tarvers | tr - .)}
Release: 1%{?dist}
URL: https://freefem.org
Source0: https://github.com/FreeFem/FreeFem-sources/archive/v%{tarvers}.tar.gz#/%{tarname}-%{tarvers}.tar.gz

Patch01: 0001-Build-fixes.patch
Patch02: 0002-Fix-formating-buffers.patch
Patch03: 0003-Wsign-compare.patch
Patch04: 0004-Wimplicit-function-declaration.patch
Patch05: 0005-Wreorder.patch
Patch06: 0006-Remove-src-medit-eigenv.h.patch
Patch07: 0007-Wformat-overflow.patch
Patch08: 0008-Use-test-e-instead-of-test-f.patch
Patch09: 0009-Fix-quoting.patch
Patch10: 0010-Use-prebuilt-FreeFEM-documentation.pdf.patch
Patch11: 0011-Install-docs-into-docdir.patch
Patch12: 0012-Use-libdir-to-setup-ff_prefix_dir.patch
Patch13: 0013-Misc-build-fixes.patch
Patch14: 0014-Wmisleading-indentation.patch

# --disable-download doesn't work
# Bundle hpddm.zip to prevent downloading during builds.
# cf. hpddm in 3rdparty/getall
%if "%{tarvers}" == "4.6"
%global hpddm_gitcommit e8639ff
%global hpddm_gitdate 20200229
%global ffvers 4.6
%endif
%if "%{tarvers}" == "4.5"
%global hpddm_gitcommit 83c462a
%global hpddm_gitdate 20191205
%global ffvers 4.5
%endif
Source1: https://github.com/hpddm/hpddm/archive/%{hpddm_gitcommit}/master.zip#/hpddm-%{hpddm_gitdate}git%{hpddm_gitcommit}.zip

# FreeFEM doesn't build docs anymore.
# Use pre-build binary, d/l'ed from
# https://doc.freefem.org/pdf/FreeFEM-documentation.pdf
Source2: FreeFEM-documentation-4.2.1-20190919.pdf

Source3: https://www.ljll.math.upmc.fr/frey/ftp/archives/freeyams.2012.02.05.tgz

License: LGPLv2+

# for 3rdparty/getall
BuildRequires: perl(strict) perl(Getopt::Std) perl(Digest::MD5)

BuildRequires:	flex
BuildRequires:	bison
BuildRequires:	gcc-c++
BuildRequires:	gcc-gfortran
BuildRequires:	glut-devel
BuildRequires:	gsl-devel
BuildRequires:	libGLU-devel

BuildRequires:	arpack-devel
BuildRequires:	gmm-devel
BuildRequires:	fftw-devel
BuildRequires:	hdf5-devel
BuildRequires:	lapack-devel
BuildRequires:	metis-devel
BuildRequires:	MUMPS-devel
BuildRequires:	NLopt-devel
BuildRequires:	openblas-devel
BuildRequires:	petsc-devel
BuildRequires:	scotch-devel
BuildRequires:	suitesparse-devel
BuildRequires:	SuperLU-devel
BuildRequires:	tetgen-devel

%description
A PDE oriented language using Finite Element Method FreeFem++ is an
implementation of a language dedicated to the finite element method. It
provides you a way to solve Partial Differential Equations (PDE) simply.

Problems involving partial differential equations (pde) of  several
branches of physics such as fluid-structure interactions require
interpolations of data on several meshes and their manipulation within
one program.

FreeFem++ is an extension of freefem, freefem+ written in C++.

%if %{with openmpi}
%package openmpi
Summary: PDE solving tool - OpenMPI version
BuildRequires:	/etc/profile.d/modules.sh
BuildRequires:	openmpi-devel
BuildRequires:	arpack-devel
BuildRequires:	openblas-devel
BuildRequires:	fftw-devel
BuildRequires:	hdf5-devel
BuildRequires:	lapack-devel
BuildRequires:	suitesparse-devel
BuildRequires:	SuperLU-devel

BuildRequires:	hdf5-openmpi-devel
BuildRequires:	blacs-openmpi-devel
BuildRequires:	MUMPS-openmpi-devel
BuildRequires:	petsc-openmpi-devel
BuildRequires:	ptscotch-openmpi-devel
BuildRequires:	scalapack-openmpi-devel
Requires: %{name} = %{version}-%{release}

%description openmpi
This package contains the OpenMPI version of FreeFem++.
%endif

%if %{with mpich}
%package mpich
Summary: PDE solving tool - MPICH version
BuildRequires:  /etc/profile.d/modules.sh
BuildRequires:	mpich-devel
BuildRequires:	arpack-devel
BuildRequires:  openblas-devel
BuildRequires:	fftw-devel
BuildRequires:	hdf5-devel
BuildRequires:	lapack-devel
BuildRequires:  suitesparse-devel
BuildRequires:  SuperLU-devel

BuildRequires:	hdf5-mpich-devel
BuildRequires:	blacs-mpich-devel
BuildRequires:  MUMPS-mpich-devel
BuildRequires:  petsc-mpich-devel
BuildRequires:  ptscotch-mpich-devel
BuildRequires:	scalapack-mpich-devel

BuildRequires:  asio-devel

Requires: %{name} = %{version}-%{release}

%description mpich
This package contains the MPICH version of FreeFem++.
%endif


%prep
%setup -q -c -T -a 0

mv %{tarname}-%{tarvers} serial
pushd serial
%patch01 -p1
%patch02 -p1
%patch03 -p1
%patch04 -p1
%patch05 -p1
%patch06 -p1
%patch07 -p1
%patch08 -p1
%patch09 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1

# HACK: scotch.h doesn't include stdint.h and stdio.h
# This break configure scripts
cat << EOF > scotch_wrapper.h
#include <stdint.h>
#include <stdio.h>
#include <scotch.h>
EOF
sed -i -e 's|\[scotch.h\]|\[scotch_wrapper.h\]|' configure.ac

# SuperLU5
# includes are in /usr/include/SuperLU
sed -i -e 's,superlu/superlu_enum_consts.h,/usr/include/SuperLU/superlu_enum_consts.h,' configure.ac

# Bogus permissions
find . -type f -perm 755 \( -name "*.c*" -o -name "*.h*" -o -name "*.edp" -o -name "*.idp" \) | xargs chmod 644

autoreconf -vif

mkdir -p 3rdparty/pkg
cp %{SOURCE1} 3rdparty/pkg/hpddm.zip
cp %{SOURCE2} FreeFEM-documentation.pdf
cp %{SOURCE3} 3rdparty/pkg/
popd

# MPI flavors
%{?with_openmpi:cp -r serial openmpi}
%{?with_mpich:cp -r serial mpich}

%build
%if %{with serial}
pushd serial
%configure \
	INSTALL="%{__install} -p" \
	--disable-optim \
	--disable-download \
	--enable-hpddm --enable-download_hpddm \
	--enable-yams --enable-download_yams \
	--enable-gmm \
	--with-blas="-L%{_libdir} -lopenblas" \
	--without-cadna \
	--with-mpi=no \
	--docdir=%{_pkgdocdir} \
	CPPFLAGS="-I$(pwd) -I/usr/include/MUMPS" \
	CFLAGS="%{optflags} -fPIC" \
	CXXFLAGS="%{optflags} -fPIC"
make -C 3rdparty CFLAGS="%{optflags} -fPIC"
make -C 3rdparty/yams CFLAGS="%{optflags} -fPIC"
make
popd
%endif

for mpi in %{?with_mpich:mpich} %{?with_openmpi:openmpi} ; do
  pushd ${mpi}
  . /etc/profile.d/modules.sh
  module load mpi/${mpi}-%{_arch}
  %configure \
	INSTALL="%{__install} -p" \
	--disable-optim \
	--disable-download \
	--enable-hpddm --enable-download_hpddm \
	--enable-yams --enable-download_yams \
	--with-blas="-L%{_libdir} -lopenblas" \
	--without-cadna \
	--with-mpi=yes \
	--docdir=%{_pkgdocdir} \
	CFLAGS="%{optflags} -fPIC" \
	CXXFLAGS="%{optflags} -fPIC"
  make -C 3rdparty CFLAGS="%{optflags} -fPIC"
  make -C 3rdparty/yams CFLAGS="%{optflags} -fPIC"
  make
  module unload mpi/${mpi}-%{_arch}
  popd
done

%install
%if %{with serial}
pushd serial
make DESTDIR=%{buildroot} install
chmod 744 %{buildroot}%{_libdir}/ff++/%{ffvers}/lib/*.so
chmod 644 %{buildroot}%{_libdir}/ff++/%{ffvers}/lib/WHERE*
pushd %{buildroot}%{_datadir}/FreeFEM
popd
# the binary with no suffix should be the generic X11 one according to README
# the build system makes it identical to -nw version, so overwrite it
ln -sf FreeFem++-nw %{buildroot}%{_bindir}/FreeFem++
popd
%endif

for mpi in %{?with_mpich:mpich} %{?with_openmpi:openmpi} ; do
  pushd $mpi
  make DESTDIR=`pwd`/buildtree install
  for bin in FreeFem++-mpi ff-mpirun ; do
    install -D -m 755 -p buildtree/%{_bindir}/$bin %{buildroot}%{_libdir}/${mpi}/bin/${bin}_${mpi}
  done
  for lib in MPICG.so mpi-cmaes.so ; do
    install -D -m 744 -p buildtree/%{_libdir}/ff++/%{ffvers}/lib/mpi/$lib %{buildroot}%{_libdir}/${mpi}/lib/ff++/lib/$lib
  done
  popd
done

%check
%if %{with checks}
%if %{with serial}
pushd serial
make check
popd
%endif
%endif

%if %{with serial}
%files
%doc serial/AUTHORS serial/CHANGELOG.md
%doc FreeFEM-documentation.pdf
%license serial/readme/COPYRIGHT
%{_bindir}/FreeFem++
%{_bindir}/FreeFem++-nw
%{_bindir}/bamg
%{_bindir}/cvmsh2
%{_bindir}/ffglut
%{_bindir}/ffmedit
%{_bindir}/ffmaster
%{_libdir}/ff++
%{_bindir}/ff-c++
%{_bindir}/ff-get-dep
%{_datadir}/FreeFEM
# Not useful to install
%exclude %{_bindir}/ff-pkg-download
%endif

%if %{with openmpi}
%files openmpi
%{_libdir}/openmpi/bin/FreeFem++-mpi_openmpi
%{_libdir}/openmpi/bin/ff-mpirun_openmpi
%{_libdir}/openmpi/lib/ff++
%endif

%if %{with mpich}
%files mpich
%{_libdir}/mpich/bin/FreeFem++-mpi_mpich
%{_libdir}/mpich/bin/ff-mpirun_mpich
%{_libdir}/mpich/lib/ff++
%endif

%changelog
* Sun May 03 2020 Ralf Corsépius <corsepiu@fedoraproject.org> - 4.6-1
- Update to 4.6
- Rebase patches.
- BR: asio-devel.

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 06 2019 Ralf Corsépius <corsepiu@fedoraproject.org> - 4.4.2-1
- Update to 4.4.2
- Rebase patches.

* Tue Aug 20 2019 Susi Lehtola <jussilehtola@fedoraproject.org> - 3.62-5
- Rebuilt for GSL 2.6.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.62-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Mar 16 2019 Orion Poplawski <orion@nwra.com> - 3.62-3
- Rebuild for hdf5 1.10.5

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.62-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 25 2019 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.62-1
- Update to 3.62.
- Rebase patches.

* Thu Jan 24 2019 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.61-1
- Update to 3.61.
- Rebase patches.
- Reflect upstream URL having changed.
- Disable checks on arm7vl.

* Thu Aug 23 2018 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.60-1
- Update to 3.60.
- Rebase patches.

* Tue Aug 21 2018 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.59-3
- Switch to using openblas instead of atlas (RHBZ#1618945).
- Enable checks on %%{x86}.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.59-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Feb 24 2018 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.59-1
- Upgrade to 3.59.
- Update patches.
- Reflect upstream having added ffmaster.

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.58-3
- Escape macros in %%changelog

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.58-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Feb 02 2018 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.58-1
- Upgrade to 3.58.
- Drop supporting freefem++ < 3.57.
- Switch to superlu5.

* Fri Feb 02 2018 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.57-2
- Rebuilt for GCC-8.0.1
- Preps for 3.58.

* Mon Dec 11 2017 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.57-1
- Update to 3.57.
- Append --without-cadna to %%configure.
- Build against SuperLU5 for freefem++ >= 3.57.

* Tue Oct 03 2017 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.56.1-1
- Update to 3.56-1.
- Spec file cosmetics.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.56-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.56-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 21 2017 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.56-1
- Update to 3.56.

* Fri Jun 23 2017 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.55-1
- Update to 3.55.
- Remove bogus CFLAGS.
- Don't build unused parts of the source tree.
- Add  0008-Wdelete-non-virtual-dtor.patch (Bogus C++ code).

* Thu May 25 2017 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.53-4
- Unbundle pstream.
- Preps for 3.53-1.
- Add 0007-Unbundle-pstream.patch (Remove bundled pstreams).
- Drop obsolete Obsoletes/Provides.
- Rework CFLAGS handling.

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.53-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Tue May 09 2017 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.53-2
- Add SuperLU43.

* Mon May 08 2017 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.53-1
- Update to 3.53.
- Rework patches.
- Skip %%check except on %%{ix86} ppc64le ppc64 aarch64 s390x.
- Add --with checks, -with openmpi, --with mpich.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.51-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 26 2017 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.51-1
- Update to 3.51.

* Tue Jan 17 2017 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.50.1-1
- Update to 3.50.1.
- Rebase patches.
- Spec cleanup.

* Mon Nov 28 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.50-2
- Enable NLopt.

* Mon Nov 28 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.50-1
- Update to 3.50.

* Fri Oct 21 2016 Orion Poplawski <orion@cora.nwra.com> - 3.49-2
- Rebuild for openmpi 2.0

* Tue Oct 04 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.49-1
- Update to 3.49.
- Eliminate %%dotpl, %%dashpl.

* Thu Sep 08 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.48-1
- Update to 3.48.
- Remove '._*' files.

* Tue Jun 14 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.47-1
- Update to 3.47.

* Mon Apr 11 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.46-1
- Update to 3.46.

* Sat Mar 26 2016 Mukundan Ragavan <nonamedotc@gmail.com> - 3.45-2
- Rebuild for SuperLU soname bump (libsuperlu.so.5.1)

* Sat Mar 12 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.45-1
- Update to 3.45.
- Rebase patches.

* Sat Mar 12 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.44-3
- Bundle hpddm*.zip to prevent downloading while building.

* Mon Feb 22 2016 Orion Poplawski <orion@cora.nwra.com> - 3.44-2
- Rebuild for gsl 2.1

* Sun Feb 21 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.44-1
- Update to 3.44
- Further spec cleanup.
- Drop FreeFem.1 (obsolete).
- Add %%license.

* Thu Feb 18 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.43-1.2
- Update to 3.43-2 (RHBZ#1163130).
- Fix F24FTBFS (RHBZ#1307512).

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.31-9.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Sep 15 2015 Orion Poplawski <orion@cora.nwra.com> - 3.31-8.3
- Rebuild for openmpi 1.10.0

* Sun Jul 26 2015 Sandro Mani <manisandro@gmail.com> - 3.31-7.3
- Rebuild for RPM MPI Requires Provides Change

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.31-6.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 11 2015 Nils Philippsen <nils@redhat.com> - 3.31-5.3
- rebuild for suitesparse-4.4.4

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 3.31-4.3
- Rebuilt for GCC 5 C++11 ABI change

* Tue Apr 07 2015 Ralf Corsépius <corsepiu@fedoraproject.org> 3.31-3.3
- Rebuild (mpich).

* Wed Feb 18 2015 Rex Dieter <rdieter@fedoraproject.org> 3.31-2.3
- rebuild (fltk,gcc5)

* Fri Sep 19 2014 Dominik Mierzejewski <rpm@greysector.net> 3.31-1.3
- update to 3.31-3 (rhbz#1116574)
- disable blas download attempts during build

* Sat Sep 06 2014 Rex Dieter <rdieter@fedoraproject.org> 3.30-5
- rebuild (gmm), use %%{?..} macro variants (for those possibly not defined or set to %%nil))

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.30-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 29 2014 Dominik Mierzejewski <rpm@greysector.net> 3.30-3
- build against tetgen

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun May 25 2014 Dominik Mierzejewski <rpm@greysector.net> 3.30-1
- update to 3.30

* Mon May 12 2014 Tom Callaway <spot@fedoraproject.org> 3.29-2
- compile against new blacs

* Mon Mar 10 2014 Dominik Mierzejewski <rpm@greysector.net> 3.29-1
- update to 3.29
- reduce redundant spec code

* Tue Feb 25 2014 Dominik Mierzejewski <rpm@greysector.net> 3.27-3
- fix compilation and build against SuperLU

* Sun Feb 23 2014 Dominik Mierzejewski <rpm@greysector.net> 3.27-2
- rebuild for mpich-3.1

* Sun Feb 16 2014 Dominik Mierzejewski <rpm@greysector.net> 3.27-1
- update to 3.27

* Fri Dec 06 2013 Nils Philippsen <nils@redhat.com> - 3.26-2.2
- rebuild (suitesparse)

* Thu Nov 28 2013 Dominik Mierzejewski <rpm@greysector.net> 3.26-1.2
- update to 3.26-2
- build with proper multi-MPI support
- build with gmm support
- WIP mumps/metis/scotch support (disabled for now)
- add missing tex dependencies
- drop obsolete patches
- explicitly disable all unavailable dependencies
- drop devel subpackage
- drop obsolete specfile constructs
- fix build with new atlas

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.19-5.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.19-4.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.19-3.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jul 14 2012 Dominik Mierzejewski <rpm@greysector.net> 3.19-2.1
- move MPI plugins to mpi subpackage

* Fri Jul 13 2012 Dominik Mierzejewski <rpm@greysector.net> 3.19-1.1
- update to 3.19-1
- rebased patches
- dropped upstreamed patch
- enable gsl interface
- added missing include which breaks compilation with gcc-4.7

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.12-3
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Feb 27 2011 Dominik Mierzejewski <rpm@greysector.net> 3.12-1
- update to 3.12
- rebased patches

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 14 2010 Dominik Mierzejewski <rpm@greysector.net> 3.11-1
- update to 3.11
- fix build
- fix duplicate binaries in the main package

* Mon Nov 15 2010 Dominik Mierzejewski <rpm@greysector.net> 3.10-1
- update to 3.10-1
- drop no longer necessary gcc-4.5 patch

* Sat Sep 04 2010 Dominik Mierzejewski <rpm@greysector.net> 3.9-3.2
- update to 3.9-2

* Sun Aug 29 2010 Dominik Mierzejewski <rpm@greysector.net> 3.9-2.1
- update to 3.9-1

* Wed Aug 04 2010 Dominik Mierzejewski <rpm@greysector.net> 3.9-1
- update to 3.9
- fix compilation with gcc-4.5.1

* Thu Feb 25 2010 Dominik Mierzejewski <rpm@greysector.net> 3.8-1
- update to 3.8
- fix FTBFS (rhbz #564731)

* Fri Jan 15 2010 Dominik Mierzejewski <rpm@greysector.net> 3.7-1.1
- update to 3.7-1
- disable testsuite again (rhbz #524511)

* Sat Dec  5 2009 Dominik Mierzejewski <rpm@greysector.net> 3.6-1.1
- update to 3.6-1
- drop upstream'd/obsolete patches
- move scripts to %%{_datadir}
- reenable testsuite

* Mon Sep 21 2009 Dominik Mierzejewski <rpm@greysector.net> 3.5-2
- disable testsuite

* Sun Sep 20 2009 Dominik Mierzejewski <rpm@greysector.net> 3.5-1
- update to 3.5
- adjust environment modules setup for current version
- use openmpi instead of lam (regression tests pass locally)
- remove irrelevant READMEs and old changelogs from docs
- add examples to -devel subpackage
- fix some minor build problems

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-6.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Dominik Mierzejewski <rpm@greysector.net> 3.0-5.5
- update to 3.0-5
- fix build with gcc-4.4
- fix build with Fedora-mandated CFLAGS
- sort BRs alphabetically

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-3.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 15 2008 Deji Akingunola <dakingun@gmail.com> - 3.0-2.3
- Rebuild for atlas-3.8.2

* Wed Dec 10 2008 Dominik Mierzejewski <rpm@greysector.net> 3.0-2.2
- update to 3.0-2
- fix compilation
- fix installation paths and path substitution in ff-c++
- preserve timestamps in make install
- add missing BR
- disable regression tests for now

* Fri Dec 05 2008 Dominik Mierzejewski <rpm@greysector.net> 3.0-1.1
- update to 3.0
- fixed build of pdf doc
- dropped obsolete patch

* Wed Oct 01 2008 Dominik Mierzejewski <rpm@greysector.net> 2.24-5.2
- fix encoding of some doc files
- fix author's name in COPYRIGHT

* Sun Sep 28 2008 Dominik Mierzejewski <rpm@greysector.net> 2.24-4.2
- disabled testsuite on ppc64
- kill lamd processes upon completing make check

* Wed Sep 24 2008 Dominik Mierzejewski <rpm@greysector.net> 2.24-3.2
- updated to 2.24-2
- fixed build in rawhide
- re-enable testsuite

* Fri Feb 22 2008 Dominik Mierzejewski <rpm@greysector.net> 2.24-2
- fix build on ppc64

* Fri Feb 22 2008 Dominik Mierzejewski <rpm@greysector.net> 2.24-1
- updated to 2.24

* Wed Feb 20 2008 Dominik Mierzejewski <rpm@greysector.net> 2.23-1
- updated to 2.23
- fixed build with gcc-4.3 (with help from Denis Leroy)
- use file deps for latex tools
- MPI part doesn't build on ppc64 (bug #433870)

* Sun Apr 29 2007 Dominik Mierzejewski <rpm@greysector.net> 2.16-2
- enable testsuite
- remove load tests from testsuite, the rest completes fine

* Sat Apr 28 2007 Dominik Mierzejewski <rpm@greysector.net> 2.16-1
- updated to 2.16-2
- simplified defattr
- work around X11 "detection"
- work around lam's mpicxx.h misdetection in configure

* Tue Mar 27 2007 Dominik Mierzejewski <rpm@greysector.net> 2.14-2
- updated to 2.14-2

* Mon Mar 19 2007 Dominik Mierzejewski <rpm@greysector.net> 2.14-1
- updated to 2.14-1
- removed redundant builddeps

* Thu Nov 23 2006 Dominik Mierzejewski <rpm@greysector.net> 2.11-2
- specfile cleanups
- added manpage from CVS

* Fri Nov 17 2006 Dominik Mierzejewski <rpm@greysector.net> 2.11-1
- updated to 2.11
- specfile cleanups

* Tue Jun 27 2006 Dominik Mierzejewski <rpm@greysector.net>
- updated to latest CVS

* Mon May 15 2006 Dominik Mierzejewski <rpm@greysector.net>
- split into subpackages

* Wed Apr 26 2006 Dominik Mierzejewski <rpm@greysector.net>
- initial build

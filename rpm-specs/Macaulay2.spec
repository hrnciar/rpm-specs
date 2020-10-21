# BUNDLING NOTES
# Macaulay2's memory management scheme requires close cooperation with libgc,
# and some of the supporting libraries must be compiled with special options to
# accomplish this.  In particular, Macaulay2 needs:
# - mathicgb configured --without-tbb
# - mpfr configured with --disable-thread-safe
# - flint linked with the GC-enabled mpfr
# - factory (from Singular) configured with --disable-omalloc --enable-streamio
#   and linked with the flint that is linked with the GC-enabled mpfr
# Since the main Fedora packages are not built in this way, we are forced to
# bundle these packages to avoid random GC-related crashes.  The packages
# memtailor and mathic, which sit underneath mathicgb, must also be bundled or
# we get random GC-related crashes for an as yet undiagnosed reason.
#
# We have to use the static version of the libfplll and givaro library.  They
# have global objects whose constructors run before GC is initialized.  If we
# allow the shared libraries to be unloaded, which happens as a normal part of
# Macaulay2's functioning, then GC tries to free objects it did not allocate,
# which leads to a segfault.
#
# We have to bundle the linbox package.  It has global constructors that cause
# the same problem as libfplll.

# Upstream wants us to build the final commit in a release branch.  We wait
# for a release announcement, then pull from git.  The tarballs in the git repo
# are for upstream's use, not for distributions to build.
%global commit      94c4b7db5dcafeaf2b97315a2bed6ac8ba16ee6b
%global shortcommit %(cut -b -7 <<< %{commit})
%global m2url       https://github.com/Macaulay2/M2

%global emacscommit 7460c448d40571866e8290ac862abbc28c1b5b37
%global emacsurl    https://github.com/Macaulay2/M2-emacs
%global emacsshort  %(cut -b -7 <<< %{emacscommit})

# Address randomization interferes with Macaulay2's memory management scheme,
# and linking with -z now breaks configure.
%undefine _hardened_build

## define to create -common subpkg
#global common 1
#if 0%%{?fedora}
# use system normaliz
%global system_normaliz 1
#endif
# standardize on gmp instead of mpir (mostly for pari/sagemath)
%global gmp 1
%global ISSUE %{?fedora:Fedora-%{fedora}}%{?rhel:RedHatEnterprise-%{rhel}}
%global M2_machine %{_target_cpu}-Linux-%{ISSUE}

# The examples contain some python files which should not be byte compiled
%global _python_bytecompile_extra 0

%if 0%{?fedora} >= 33
%global blaslib flexiblas
%else
%global blaslib openblas
%endif

Summary: System for algebraic geometry and commutative algebra
Name:    Macaulay2
Version: 1.16
Release: 2%{?dist}

License: GPLv2 or GPLv3
URL:     http://macaulay2.com/
%if 0%{?snap:1}
Source0: %{name}-%{version}-%{snap}.tar.xz
%else
Source0: %{m2url}/tarball/%{commit}/%{name}-%{version}.tar.gz
%endif
Source1: %{emacsurl}/tarball/%{emacscommit}/M2-emacs-%{emacsshort}.tar.gz

# Various sizes of the planets icon from macaulay2.com.  See README.icons in
# the tar file for details on how these icons were created.
Source10: Macaulay2-icons.tar.xz
Source11: Macaulay2.desktop
Source20: etags.sh

## BUNDLED code
# Normaliz must sometimes be bundled due to version differences
%global normalizver 3.7.2
Source100: http://www.math.uiuc.edu/Macaulay2/Downloads/OtherSourceCode/normaliz-%{normalizver}.tar.gz
Provides:  bundled(normaliz) = %{normalizver}

# MPFR is bundled because it must be built with different threading options
%global mpfrver 4.1.0
Source101: http://www.mpfr.org/mpfr-%{mpfrver}/mpfr-%{mpfrver}.tar.xz
Provides:  bundled(mpfr) = %{mpfrver}

# FLINT is bundled because it must be linked with the specially-built MPFR
%global flintver 2.6.3
Source102: http://www.flintlib.org/flint-%{flintver}.tar.gz
Provides:  bundled(flint) = %{flintver}

# FACTORY is bundled because it must be built with special options
%global factoryver 4.1.1
Source103: http://faculty.math.illinois.edu/Macaulay2/Downloads/OtherSourceCode/factory-%{factoryver}.tar.gz
Provides:  bundled(factory) = %{factoryver}

# MATHICGB is bundled because it must be built with different threading options
%global mathicgbver 1.0
%global mathicgbcommit 0d70da731a84008143a00cf1effd978dc8607879
Source104: https://github.com/Macaulay2/mathicgb/tarball/%{mathicgbcommit}/mathicgb-%{mathicgbver}.tar.gz
Provides:  bundled(mathicgb) = %{mathicgbver}

# GTEST is bundled because MATHICGB refuses to build otherwise
%global gtestver 1.10.0
Source105: https://faculty.math.illinois.edu/Macaulay2/Downloads/OtherSourceCode/gtest-%{gtestver}.tar.gz

# MEMTAILOR is bundled because it causes garbage collector crashes otherwise
%global memtailorver 1.0
%global memtailorcommit 1d13f96bc7d84b7ac401e6b8c936fad26f08786c
Source106: https://github.com/Macaulay2/memtailor/tarball/%{memtailorcommit}/memtailor-%{memtailorver}.tar.gz
Provides:  bundled(memtailor) = %{memtailorver}

# MATHIC is bundled because it causes garbage collector crashes otherwise
%global mathicver 1.0
%global mathiccommit 44095b846a83c05cbff6f3e8765070e5cda40e67
Source107: https://github.com/Macaulay2/mathic/tarball/%{mathiccommit}/mathic-%{mathicver}.tar.gz
Provides:  bundled(mathic) = %{mathicver}

# LINBOX is bundled because it introduces static global objects
%global linboxver 1.6.3
Source108: https://github.com/linbox-team/linbox/archive/v%{linboxver}}/linbox-%{linboxver}.tar.gz
Provides:  bundled(linbox) = %{linboxver}

## PATCHES FOR BUNDLED code
# Work around an ambiguous overload on 32-bit platforms
Source200: linbox-1.6.3.patch
# Fix factory build failure.  REPLACES the upstream patch.
Source201: factory-4.1.1.patch
# Fix mathicgb build on big endian machines.
Source202: mathicgb-1.0.patch

## FAKE library tarballs that convince Macaulay2 to use the system versions
Source300: frobby_v0.9.0.tar.gz
Source301: cddlib-094h.tar.gz
Source302: lapack-3.6.0.tgz
Source303: 4ti2-1.6.9.tar.gz
Source304: libfplll-5.2.0.tar.gz
Source305: gfan0.6.2.tar.gz
Source306: givaro-4.1.1.tar.gz
Source307: lrslib-062.tar.gz
Source308: TOPCOM-0.17.8.tar.gz
Source309: cohomCalg-0.32.tar.gz
Source310: glpk-4.59.tar.gz
Source311: Csdp-6.2.0.tgz
Source312: mpsolve-3.2.1.tar.gz

# let Fedora optflags override the defaults
Patch0:  %{name}-1.15-optflags.patch
# give the build a little more time and space than upstream permits
Patch1: %{name}-1.16-ulimit.patch
# fix paths to nauty binaries
Patch2:  %{name}-1.11-nauty-paths.patch
# drop 'tests' from default make target
Patch3:  %{name}-1.16-default_make_targets.patch
# disable check for gftables
Patch4:  %{name}-1.16-no_gftables.patch
# adapt to libfplll 5.2.1
Patch5: %{name}-1.15-fplll.patch
# do not override the debug level
Patch6: %{name}-1.12-configure.patch
# fix some -Wformat warnings
Patch7: %{name}-1.16-format.patch
# Fix "error: in conversion to html, unknown TeX control sequence(s): \rightarrow"
Patch8: %{name}-1.16-rightarrow.patch
# Fix minor errors found when building with gcc-11
Patch9: %{name}-gcc11.patch

BuildRequires: 4ti2
BuildRequires: autoconf
BuildRequires: autoconf-archive
BuildRequires: bison
BuildRequires: boost-devel
BuildRequires: cddlib-devel
BuildRequires: chrpath
%if ! 0%{?system_normaliz}
BuildRequires: cmake
%endif
BuildRequires: cohomCalg
BuildRequires: csdp-tools
BuildRequires: desktop-file-utils
%if 0%{?fedora}
BuildRequires: doxygen-latex
%else
BuildRequires: doxygen
%endif
# etags
BuildRequires: emacs
BuildRequires: expat-devel
BuildRequires: factory-gftables
BuildRequires: fflas-ffpack-devel
BuildRequires: flex
BuildRequires: gawk
BuildRequires: gcc-c++
BuildRequires: gcc-gfortran
BuildRequires: gdb
BuildRequires: gdbm-devel
BuildRequires: gettext-devel
BuildRequires: gfan
BuildRequires: git-core
BuildRequires: givaro-static
BuildRequires: glpk-devel
%if 0%{?gmp}
BuildRequires: gmp-devel
%else
BuildRequires: mpir-devel
%endif
BuildRequires: gtest-devel
BuildRequires: iml-devel
BuildRequires: info
BuildRequires: libgfan-devel
BuildRequires: libtool
BuildRequires: libatomic_ops-devel
BuildRequires: libfplll-static
BuildRequires: libfrobby-devel
BuildRequires: libnauty-devel
%if 0%{?system_normaliz}
BuildRequires: libnormaliz-devel >= 3.6.3
%endif
BuildRequires: libtool
BuildRequires: lrslib-devel
BuildRequires: lrslib-utils
BuildRequires: m4ri-devel
BuildRequires: m4rie-devel
BuildRequires: mariadb-devel
BuildRequires: mpsolve-devel
BuildRequires: nauty
BuildRequires: normaliz
BuildRequires: ntl-devel
BuildRequires: %{blaslib}-devel
BuildRequires: pari-devel
BuildRequires: pkgconfig(bdw-gc) >= 7.6.2
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(ncurses)
BuildRequires: polymake
BuildRequires: python3
BuildRequires: qd-devel
BuildRequires: readline-devel 
BuildRequires: time
BuildRequires: tinyxml2-devel
BuildRequires: TOPCOM
BuildRequires: transfig
BuildRequires: valgrind

Requires: 4ti2
Requires: cohomCalg
Requires: csdp-tools
Requires: emacs-filesystem
Requires: factory-gftables
Requires: gfan
Requires: hicolor-icon-theme
Requires: lrslib-utils
Requires: nauty
Requires: TOPCOM

Recommends: mathicgb

%if 0%{?common}
Requires:  %{name}-common = %{version}-%{release}
%else
Obsoletes: Macaulay2-common < %{version}-%{release}
Provides:  Macaulay2-common = %{version}-%{release}
%endif
Obsoletes: Macaulay2-doc < %{version}-%{release} 
Provides:  Macaulay2-doc = %{version}-%{release}
Obsoletes: Macaulay2-emacs < %{version}-%{release}
Provides:  Macaulay2-emacs = %{version}-%{release}

Provides:  macaulay2 = %{version}-%{release}

# M2-help
Requires: xdg-utils

%if 0%{?system_normaliz}
Requires: normaliz
%endif

# Macaulay2 no longer builds successfully on 32-bit platforms
# https://bugzilla.redhat.com/show_bug.cgi?id=1874318
ExcludeArch: %{ix86} %{arm}

# Do not advertise the bundled mpfr
%global __provides_exclude libmpfr.so*


%description
Macaulay 2 is a new software system devoted to supporting research in
algebraic geometry and commutative algebra written by Daniel R. Grayson
and Michael E. Stillman

%package common
Summary: Common files for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description common
%{summary}.


%prep
%setup -q -n %{name}-M2-%{shortcommit}/M2
%setup -q -n %{name}-M2-%{shortcommit}/M2 -T -D -a 10
tar -C Macaulay2/editors/emacs --strip-components=1 -xzf %{SOURCE1}

install -p -m755 %{SOURCE20} ./etags

## bundled code
install -p -m644 %{SOURCE100} BUILD/tarfiles/
%if ! 0%{?system_normaliz}
sed -e '/PROGRAMS =/aPATCHFILE = @abs_srcdir@/patch-$(VERSION)' \
    -e '/PRECONFIGURE/d' \
    -i libraries/normaliz/Makefile.in
%endif
install -p -m644 %{SOURCE101} %{SOURCE102} %{SOURCE103} %{SOURCE105} \
    %{SOURCE108} BUILD/tarfiles/
sed -i 's/\(VERSION = \).*/\1%{mpfrver}/' libraries/mpfr/Makefile.in
sed -e 's/\(VERSION = \).*/\1%{linboxver}/' \
    -e 's/^#\(PATCHFILE\)/\1/' \
    -e 's,--with-gmp.*,GIVARO_CFLAGS=-I$(LIBRARIESDIR) GIVARO_LIBS="%{_libdir}/libgivaro.a",' \
    -i libraries/linbox/Makefile.in
tar -C submodules/mathicgb -xf %{SOURCE104} --strip-components=1
patch -d submodules/mathicgb -p0 < %{SOURCE202}
tar -C submodules/memtailor -xf %{SOURCE106} --strip-components=1
tar -C submodules/mathic -xf %{SOURCE107} --strip-components=1

## patches for bundled code
sed -e 's,--with-blas,&=%{_includedir}/%{blaslib} --with-ntl,' \
    -e 's,2\.6\.0,%{flintver},' \
    -i libraries/flint/Makefile.in
cp -p %{SOURCE200} libraries/linbox/patch-%{linboxver}
cp -p %{SOURCE201} libraries/factory/patch-%{factoryver}

## fake library tarballs
install -p -m644 %{SOURCE300} %{SOURCE301} %{SOURCE302} %{SOURCE303} \
  %{SOURCE304} %{SOURCE305} %{SOURCE306} %{SOURCE307} %{SOURCE308} \
  %{SOURCE309} %{SOURCE310} %{SOURCE311} %{SOURCE312} BUILD/tarfiles/
sed -i '/PRECONFIGURE/d' libraries/{4ti2,cddlib,givaro,normaliz,topcom}/Makefile.in
sed -i 's/VERSION = 4\.0\.4/VERSION = 5.2.0/;/PATCHFILE/d' libraries/fplll/Makefile.in
sed -i '/PATCHFILE/d' libraries/{csdp,frobby,gfan,givaro,mpsolve,normaliz,topcom}/Makefile.in
sed -i '/INSTALLCMD/,/stdinc/d' libraries/frobby/Makefile.in
sed -i 's,install \(lib.*\.a\),ln -s %{_libdir}/\1,' libraries/lapack/Makefile.in

## fake givaro submodule
tar -C submodules/givaro --strip-components=1 -xzf %{SOURCE306}

%patch0 -p1 -b .optflags
%patch1 -p1 -b .ulimit
%patch2 -p1 -b .nauty
%patch3 -p1 -b .default_make_targets
%patch4 -p1 -b .no_gftables
# factory-gftables symlink
mkdir -p BUILD/%{_target_platform}/usr-dist/common/share/Macaulay2/Core
ln -s %{_datadir}/factory \
         BUILD/%{_target_platform}/usr-dist/common/share/Macaulay2/Core/factory
%patch5 -p1 -b .fplll
%patch6 -p1 -b .configure
%patch7 -p1 -b .format
%patch8 -p1 -b .rightarrow
%patch9 -p1 -b .gcc11

# repeatable builds: inject a node name
sed -i 's,`uname -n`,build.fedoraproject.org,' configure.ac

# gdb is used during the build; let it autoload some files
if [ "$HOME" = "/builddir" ]; then
  echo "set auto-load safe-path /" > /builddir/.gdbinit
fi

# Use, but don't build, cddlib, fflas-ffpack, and gc.  Use the static versions
# of libfplll and givaro.  Do not invoke git on a nonrepository.  Link with
# blaslib instead of the reference blas and lapack.  Fix typos.
sed -e 's/^BUILD_cddlib=yes/BUILD_cddlib=no/' \
    -e 's/^BUILD_gc=yes/BUILD_gc=no/' \
    -e 's/BUILD_fflas_ffpack=yes/BUILD_fflas_ffpack=no/' \
    -e 's/^\(GIT_DESCRIPTION=\).*/\1"unknown"/' \
    -e 's,-lfplll,%{_libdir}/libfplll.a -lqd,' \
    -e 's,`\$PKG_CONFIG --libs givaro`,%{_libdir}/libgivaro.a,' \
    -e 's,-lgivaro,%{_libdir}/libgivaro.a,' \
    -e 's,-llapack -lrefblas,-l%{blaslib},' \
    -e 's,\$added_fclibs != yes,"$added_fclibs" != yes,' \
    -i configure.ac

# (re)generate configure
autoreconf -fi .


%build
# This package has a configure test which compiles code and expects it to
# behave in a very specific way (__builtin_return_address).  LTO changs the
# behavior and the configure test does not know how to handle it.
# Until the configure script is fixed this seems like the best thing to do
# Disable LTO
%define _lto_cflags %{nil}

## configure macro currently broken, due to some odd prefix-checks.  probably fixable -- Rex
mkdir -p BUILD/%{_target_platform}
pushd BUILD/%{_target_platform}
# On ppc64le with the compiler in strict mode, the pari declaration of
# vec_insert() is deemed to ambiguate the declaration of the AltiVec function
# __builtin_vec_insert().  We add -fpermissive to downgrade the error to a
# warning, but we should find a better fix.
%ifarch ppc64le
cxxflags="%{optflags} -fsigned-char -fpermissive"
%else
cxxflags="%{optflags} -fsigned-char"
%endif
CPPFLAGS="-I%{_includedir}/cddlib -I%{_includedir}/frobby" \
CFLAGS="%{optflags} -fsigned-char" \
CXXFLAGS="$cxxflags" \
LIBS="-l%{blaslib}" \
../../configure \
  --build=%{_build} \
  --host=%{_host} \
  --with-issue=%{ISSUE} \
  --prefix=%{_prefix} \
  --disable-dumpdata \
  --enable-shared \
  --disable-fc-lib-ldflags \
  --disable-strip \
  --enable-fplll \
  --enable-linbox \
%if 0%{?gmp}
  --with-integer-package=gmp \
%else
  --with-integer-package=mpir \
%endif
  --with-unbuilt-programs="cddplus nauty" \
  --enable-build-libraries="mpfr flint factory lapack fplll givaro linbox gtest"
  # The list of libraries and submodules above should include only those that:
  # 1. We bundle (mpfr, flint, factory, and linbox)
  # 2. We sneakily substitute one library for another (lapack -> blaslib)
  # 3. Have to be linked with the static library (fplll and givaro)
popd

# link with static libraries when global constructors run prior to GC
# initialization.  Otherwise, unloading the shared object causes a crash.
# We have to do this because we pick up references to -lgivaro from other
# packages during the configure script execution.
for fil in $(grep -Erl -e '-lfplll|-lgivaro' .); do
  sed -e 's,-lfplll,%{_libdir}/libfplll.a,' \
      -e 's,-lgivaro,%{_libdir}/libgivaro.a,' \
      -i.orig $fil
  touch -r $fil.orig $fil
  rm -f $fil.orig
done

make -C BUILD/%{_target_platform} VERBOSE=true Verbose=true IgnoreExampleErrors=true

# log errors
find BUILD/%{_target_platform}/ -name *.errors -execdir echo {} \; -execdir cat {} \;


%install
make install -C BUILD/%{_target_platform} DESTDIR=%{buildroot} IgnoreExampleErrors=true

# link, don't copy, the binaries
mbindir=%{buildroot}%{_libexecdir}/Macaulay2/bin
for fil in checkregularity chiro2circuits chiro2cocircuits cohomcalg csdp lrs \
    normaliz points2allfinetriangs points2alltriangs points2chiro \
    points2finetriang points2finetriangs points2flips points2nallfinetriangs \
    points2nalltriangs points2nfinetriangs points2nflips points2ntriangs \
    points2triangs points2volume; do
  rm -f $mbindir/$fil
  ln -s %{_bindir}/$fil $mbindir/$fil
done

# app img
for sz in 64 72 96 128 192 256 512; do
  sz2=${sz}x${sz}
  mkdir -p %{buildroot}%{_datadir}/icons/hicolor/$sz2/apps
  install -p -m644 icons/NinePlanets-${sz2}.png \
                   %{buildroot}%{_datadir}/icons/hicolor/$sz2/apps/%{name}.png
done

desktop-file-install --vendor="" \
  --dir=%{buildroot}%{_datadir}/applications \
  %{SOURCE11}

# Byte compile the Emacs files, and move the documentation
pushd %{buildroot}%{_emacs_sitelispdir}/%{name}
mv M2-emacs* %{buildroot}%{_pkgdocdir}
mv README.md %{buildroot}%{_pkgdocdir}/README-emacs.md
%{_emacs_bytecompile} *.el
popd

## unpackaged files
# info dir
rm -fv %{buildroot}%{_infodir}/dir

# Delete misinstalled memtailor, mathic, and mathicgb libraries
rm -fr %{buildroot}/builddir


%check
CFLAGS="%{optflags}" \
CXXFLAGS="%{optflags}" \
LDFLAGS="$RPM_LD_FLAGS" \
time make -k check -C BUILD/%{_target_platform} Verbose=true ||:


%files
%{_bindir}/M2
%{_bindir}/M2-binary
%{_prefix}/lib/Macaulay2/
%{_libexecdir}/Macaulay2/

%if 0%{?common}
%files common
%endif
%{_datadir}/Macaulay2/
%{_datadir}/applications/*Macaulay2.desktop
%{_datadir}/icons/hicolor/*/*/*
%{_docdir}/Macaulay2/
%{_infodir}/*.info*
%{_mandir}/man1/*
%{_emacs_sitelispdir}/%{name}/


%changelog
* Thu Oct 15 2020 Jeff Law <law@redhat.com> - 1.16-2
- Add missing #includes for gcc-11

* Mon Aug 31 2020 Jerry James <loganjerry@gmail.com> - 1.16-1
- Version 1.16
- Drop upstreamed patch: -xdg_open
- Add -ulimit patch for the slower builders
- Add -format and -rightarrow patches
- Bundle packages due to garbage collector crashes: linbox, memtailor, mathic
- Drop the XEmacs subpackage; XEmacs support no longer works

* Sun Aug 16 2020 Iñaki Úcar <iucar@fedoraproject.org> - 1.15.1.0-5
- https://fedoraproject.org/wiki/Changes/FlexiBLAS_as_BLAS/LAPACK_manager

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.1.0-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul  1 2020 Jeff Law <law@redhat.com> - 1.15.1.0-2
- Disable LTO

* Wed Jun  3 2020 Jerry James <loganjerry@gmail.com> - 1.15.1.0-1
- Version 1.15.1.0
- Drop upstreamed patches: -no_Werror, -mpir, -pthreads, -fflas-ffpack,
  -fno-common, -gtest, -pthreads

* Tue Feb 11 2020 Jerry James <loganjerry@gmail.com> - 1.14.0.1-4
- Add -fno-common patch to fix FTBFS with GCC 10

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 10 2020 Jerry James <loganjerry@gmail.com> - 1.14.0.1-3
- Rebuild for ntl 11.4.3

* Fri Nov  1 2019 Jerry James <loganjerry@gmail.com> - 1.14.0.1-2
- Rebuild for givaro 4.1.1, fflas-ffpack 2.4.3, and linbox 1.6.3

* Thu Sep 26 2019 Jerry James <loganjerry@gmail.com> - 1.14.0.1-1
- Macaulay2-1.14.0.1
- Drop upstreamed -format and -exception patches
- Also bundle libmpc since it is linked with mpfr
- Drop fix for F26 symlink-file snafu
- Build with python 3 instead of python 2

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.12.0.1-5
- Rebuild for readline 8.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Nov 20 2018 Jerry James <loganjerry@gmail.com> - 1.12.0.1-3
- Rebuild for lrslib 070

* Wed Oct 10 2018 Jerry James <loganjerry@gmail.com> - 1.12.0.1-2
- Rebuild for ntl 11.3.0
- Build with openblas instead of atlas (bz 1618938)

* Fri Aug 10 2018 Jerry James <loganjerry@gmail.com> - 1.12.0.1-1
- Macaulay2-1.12.0.1
- Replace tiny icon of unknown origin with various sizes of upstream's icon
- Remove deprecated entries from the desktop file
- Add upstream mpfr 3.1.6 patches

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul  3 2018 Jerry James <loganjerry@gmail.com> - 1.11-2
- Rebuild for ntl 11.1.0
- Remove scriptlets that call install-info
- Do not byte compile python files in the examples

* Sat Jun  2 2018 Jerry James <loganjerry@gmail.com> - 1.11-1
- Macaulay2-1.11
- Drop upstreamed patches: -verbose_build, -givaro, -pari, -endian
- New patches: -fflas-ffpack, -format, -exception, -fplll, -configure
- Update bundled software
- Refresh INFO_FILES list

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.9.2-8
- Escape macros in %%changelog

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.9.2-6
- Remove obsolete scriptlets

* Wed Oct 11 2017 Jerry James <loganjerry@gmail.com> - 1.9.2-5
- Link rather than copy the normaliz binary
- Fix accidental replacement of factory symlink with a directory

* Sat Sep 30 2017 Jerry James <loganjerry@gmail.com> - 1.9.2-4
- Rebuild for ntl 10.5.0

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Apr  5 2017 Jerry James <loganjerry@gmail.com> - 1.9.2-1
- Macaulay2-1.9.2
- Drop upstreamed patches: -disable_broken_debug_functions, -gc, -rpath,
  -rh_configure_hack
- Add patches: -givaro, -gtest, -pari
- Create fake library and submodule tarballs to fool the build system into
  building in support for system libraries
- Bundle mpfr, flint, and factory to avoid garbage collector crashes
- Replace the (X)Emacs triggers with (x)emacs-filesystem dependencies
- New URLs

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 1.6-33
- Rebuild for readline 7.x

* Thu Oct 20 2016 Jerry James <loganjerry@gmail.com> - 1.6-32
- Rebuild for ntl 10.1.0

* Mon Sep  5 2016 Jerry James <loganjerry@gmail.com> - 1.6-31
- Rebuild for ntl 9.11.0

* Fri Aug 12 2016 Jerry James <loganjerry@gmail.com> - 1.6-30
- Rebuild for fflas-ffpack 2.2.2, givaro 4.0.2, and linbox 1.4.2

* Mon Jul 25 2016 Jerry James <loganjerry@gmail.com> - 1.6-29
- Rebuild for ntl 9.10.0

* Thu Jun  2 2016 Jerry James <loganjerry@gmail.com> - 1.6-28
- Rebuild for ntl 9.9.1

* Fri Apr 29 2016 Jerry James <loganjerry@gmail.com> - 1.6-27
- Rebuild for ntl 9.8.0
- Nauty is now available
- Drop -gcc-template-bug patch; gcc bug has been fixed

* Sat Mar 19 2016 Jerry James <loganjerry@gmail.com> - 1.6-26
- Rebuild for ntl 9.7.0

* Sat Feb 20 2016 Jerry James <loganjerry@gmail.com> - 1.6-25
- Rebuild for ntl 9.6.4
- Add -gcc-template-bug patch to work around gcc bug (bz 1307282)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 14 2016 Jonathan Wakely <jwakely@redhat.com> - 1.6-23
- Rebuilt for Boost 1.60

* Fri Dec  4 2015 Jerry James <loganjerry@gmail.com> - 1.6-22
- Rebuild for ntl 9.6.2
- Add python2 BR for the tests

* Sat Oct 17 2015 Kalev Lember <klember@redhat.com> - 1.6-21
- Rebuilt for libntl soname bump

* Fri Oct 16 2015 Jerry James <loganjerry@gmail.com> - 1.6-20
- Rebuild for ntl 9.4.0

* Tue Sep 29 2015 Rex Dieter <rdieter@fedoraproject.org> 1.6-19
- refresh config.guess/config.sub hack, fix FTBFS on aarch64

* Sat Sep 19 2015 Jerry James <loganjerry@gmail.com> - 1.6-18
- Rebuild for flint 2.5.2 and ntl 9.3.0

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 1.6-17
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-16
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 1.6-15
- rebuild for Boost 1.58

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 18 2015 Jerry James <loganjerry@gmail.com> - 1.6-13
- Rebuild for ntl 9.1.1 and cddlib-094h

* Fri May 15 2015 Jerry James <loganjerry@gmail.com> - 1.6-12
- Bump and rebuild

* Sat May  9 2015 Jerry James <loganjerry@gmail.com> - 1.6-11
- Rebuild for ntl 9.1.0

* Mon Feb  2 2015 Jerry James <loganjerry@gmail.com> - 1.6-10
- Rebuild for ntl 8.1.2

* Mon Jan 26 2015 Petr Machata <pmachata@redhat.com> - 1.6-9
- Rebuild for boost 1.57.0

* Thu Jan 15 2015 Jerry James <loganjerry@gmail.com> - 1.6-8
- Rebuild for ntl 8.1.0
- Fix the desktop file name

* Wed Oct 29 2014 Jerry James <loganjerry@gmail.com> - 1.6-7
- Rebuild for ntl 6.2.1
- Revert Apr 8 HTML creation timeout, now handled upstream
- Revert use of -common subpkg; various arches timeout differently

* Wed Sep 24 2014 Rex Dieter <rdieter@fedoraproject.org> 1.6-6
- enable -common subpkg (to be more compatible with upstream packaging)

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jun 25 2014 Rex Dieter <rdieter@fedoraproject.org> 1.6-4
- restore --build/--host configure options lost in 1.6 update, should help arm

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 1.6-2
- Rebuild for boost 1.55.0

* Mon May 19 2014 Rex Dieter <rdieter@fedoraproject.org> 1.6-1
- Macaulay2-1.6 (#1074594)
- ExcludeArch: %%arm (#1099598)

* Wed May 14 2014 Rex Dieter <rdieter@fedoraproject.org> 1.5-8
- rebuild (gc)

* Tue Apr  8 2014 Jerry James <loganjerry@gmail.com> - 1.5-7
- Build for all arches
- Increase HTML creation timeouts for slower processors, such as ARM
- Add --build and --host invocations to configure to fix mismatched ARM names

* Wed Apr  2 2014 Jerry James <loganjerry@gmail.com> - 1.5-6
- Rebuild for ntl 6.1.0

* Fri Mar 21 2014 Jerry James <loganjerry@gmail.com> - 1.5-5
- The normaliz patch was used; bring it back
- Complete the removal of the system_normaliz variable
- Link with RPM_LD_FLAGS
- Due to use of a static library, explicitly link with -lflint

* Fri Jan 24 2014 Rex Dieter <rdieter@fedoraproject.org> - 1.5-5
- drop unused patches (4ti2, normalize)

* Tue Jan 21 2014 Rex Dieter <rdieter@fedoraproject.org> - 1.5-4
- utilize %%_libexecdir/Macaulay2/... for helper/system binaries
- libdir: %%_libdir => %%_prefix/lib
- -common subpkg option (not used yet)

* Tue Jan 14 2014 Jerry James <loganjerry@gmail.com> - 1.5-3
- Update normaliz interface for normaliz 2.8 and later

* Tue Jul 30 2013 Petr Machata <pmachata@redhat.com> - 1.5-2
- Rebuild for boost 1.54.0

* Thu May 23 2013 Rex Dieter <rdieter@fedoraproject.org> 1.5-1
- Release: 1 (using non-snapshot release tarball now)

* Tue May 21 2013 Rex Dieter <rdieter@fedoraproject.org> - 1.5-0.7.20130401
- update to 20130401 r15955 snapshot release
- (Build)Requires: factory-gftables (see bug #965655)
- refresh INFO_FILES content

* Mon May  6 2013 Jerry James <loganjerry@gmail.com> - 1.5-0.6.20130214
- Rebuild for m4ri 20130416

* Fri Feb 15 2013 Rex Dieter <rdieter@fedoraproject.org> 1.5-0.5.20130214
- r15838 (20130214 snapshot)

* Wed Feb 13 2013 Rex Dieter <rdieter@fedoraproject.org> 1.5-0.4.20120807
- BR: doxygen-latex

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-0.3.20120807
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Aug 07 2012 Rex Dieter <rdieter@fedoraproject.org> 1.5-0.2.20120807
- 1.5 20120807 r15022 snapshot

* Thu Jul 19 2012 Rex Dieter <rdieter@fedoraproject.org> 1.4-9
- rebuild against (Singular's) libfac/factory 3.1.3

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 03 2012 Rex Dieter <rdieter@fedoraproject.org> 1.4-7
- rebuild (pari)

* Sun Jul 1 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.4-6
- Link to gmp not mpir.
- Rebuild with pari 2.5.

* Wed May 30 2012 Rex Dieter <rdieter@fedoraproject.org>
- 1.4-5
- License: GPLv2 or GPLv3 (#821036)
- pkgconfig-style deps

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-4
- Rebuilt for c++ ABI breakage

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Sep 30 2011 Rex Dieter <rdieter@fedoraproject.org> 1.4-2
- rebuild (gdbm)

* Thu May 26 2011 Rex Dieter <rdieter@fedoraproject.org> 1.4-1
- 1.4

* Thu May 26 2011 Rex Dieter <rdieter@fedoraproject.org> 1.3.1-9
- Typo in INFO_FILES (#708086)

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jun 30 2010 Rex Dieter <rdieter@fedoraproject.org> - 1.3.1-7
- BR: cddlib-static (#609698)

* Tue Mar 16 2010 Rex Dieter <rdieter@fedoraproject.org> - 1.3.1-6
- rebuild (factory/libfac)

* Tue Mar 16 2010 Mark Chappell <tremble@fedoraproject.org> - 1.3.1-5
- Run install-info on all of the .info files we installed
- Re-enable the now functional ppc64 build

* Wed Mar 10 2010 Mark Chappell <tremble@fedoraproject.org> - 1.3.1-4
- Add in missing Requires runtime dependancies

* Wed Mar 10 2010 Mark Chappell <tremble@fedoraproject.org> - 1.3.1-3
- GPLv3/GPLv2 conflict, use compat-readline5 - bz#511299

* Tue Mar 09 2010 Mark Chappell <tremble@fedoraproject.org> - 1.3.1-2
- Replace DSO patch with one accepted upstream
- Completely disable static linking

* Wed Feb 24 2010 Mark Chappell <tremble@fedoraproject.org> - 1.3.1-1
- Upstream version increment
- Remove unused patch
- Remove patch applied upstream
- Ensure consistent use of buildroot macro instead of RPM_BUILD_ROOT
- Fix implicit linking DSO failure
- Don't package empty .okay files which simply indicate test passes

* Tue Dec  8 2009 Michael Schwendt <mschwendt@fedoraproject.org> - 1.2-7
- Explicitly BR factory-static and libfac-static in accordance with the
  Packaging Guidelines (factory-devel/libfac-devel are still static-only).

* Tue Sep 22 2009 Rex Dieter <rdieter@fedoraproject.org> - 1.2-6
- fixup/optimize scriplets

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Apr 17 2009 Rex Dieter <rdieter@fedoraproject.org> - 1.2-4
- rebuild for ntl-devel (shared)

* Wed Feb 25 2009 Rex Dieter <rdieter@fedoraproject.org> - 1.2-3
- BR: libfac-devel,factory-devel >= 3.1
- restore ExcludeArch: ppc64 (#253847)

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 13 2009 Rex Dieter <rdieter@fedoraproject.org> 1.2-1
- Macaulay-1.2

* Thu Oct 02 2008 Rex Dieter <rdieter@fedoraproject.org> 1.1-2
- respin (factory/libfac)

* Tue Mar 11 2008 Rex Dieter <rdieter@fedoraproject.org> 1.1-1
- Macaulay2-1.1
- Obsoletes/Provides: Macaulay2-common (upstream compatibility)
- re-enable ppc64 (#253847)
- IgnoreExampleErrors=true

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.9.95-10
- Autorebuild for GCC 4.3

* Tue Dec 18 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 0.9.95-9
- Provides: macaulay2
- respin against new(er) factory,libfac,ntl

* Wed Aug 22 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 0.9.95-8
- ExcludeArch: ppc64 (#253847)

* Tue Aug 21 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 0.9.95-7
- BR: gawk

* Tue Aug 21 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 0.9.95-6
- gc-7.0 patches

* Sat Aug 11 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 0.9.95-5
- License: GPLv2

* Mon Jan 15 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 0.9.95-4
- Ob/Pr: Macaulay2-doc, not -docs (#222609)

* Sat Jan 06 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 0.9.95-3
- re-enable ppc build (#201739)

* Tue Jan 02 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 0.9.95-2
- ./configure --disable-strip, for usable -debuginfo (#220893)

* Mon Dec 18 2006 Rex Dieter <rexdieter[AT]users.sf.net> 0.9.95-1
- Macaulay2-0.9.95

* Wed Nov 22 2006 Rex Dieter <rexdieter[AT]users.sf.net> 0.9.20-0.5.20060808svn
- .desktop Categories: -Application,Scientific,X-Fedora +ConsoleOnly

* Tue Aug 29 2006 Rex Dieter <rexdieter[AT]users.sf.net> 0.9.20-0.4.20060808svn
- fc6 respin

* Tue Aug 08 2006 Rex Dieter <rexdieter[AT]users.sf.net> 0.9.20-0.3.20060808svn
- ExcludeArch: ppc (bug #201739)
- %%ghost (x)emacs site-lisp bits (using hints from fedora-rpmdevtools)

* Tue Aug 08 2006 Rex Dieter <rexdieter[AT]users.sf.net> 0.9.20-0.2.20060808svn
- 20060808 snapshot

* Mon Jul 24 2006 Rex Dieter <rexdieter[AT]users.sf.net> 0.9.20-0.1.20060724svn
- 2006-07-15-0.9.20

* Wed Jul 12 2006 Rex Dieter <rexdieter[AT]users.sf.net> 0.9.10-0.6.20060710svn
- 0.9.10

-* Mon Jul 10 2006 Rex Dieter <rexdieter[AT]users.sf.net> 0.9.8-0.6.cvs20060327
- BR: ncurses-devel

* Fri May 05 2006 Rex Dieter <rexdieter[AT]users.sf.net> 0.9.8-0.4.cvs20060327
- 64bit patch (#188709)

* Wed Apr 12 2006 Rex Dieter <rexdieter[AT]users.sf.net> 0.9.8-0.3.cvs20060327 
- omit x86_64, for now (#188709)

* Tue Apr 11 2006 Rex Dieter <rexdieter[AT]users.sf.net> 0.9.8-0.2.cvs20060327
- 0.9.8 (cvs, no tarball yet)
- drop -doc subpkg (in main now)

* Mon Apr 10 2006 Rex Dieter <rexdieter[AT]users.sf.net> 0.9.2-22
- fix icon location (#188384)

* Thu Mar 30 2006 Rex Dieter <rexdieter[AT]users.sf.net> 0.9.2-21
- really disable %%check (fails on fc5+ anyway) 

* Fri Jan 20 2006 Rex Dieter <rexdieter[AT]users.sf.net> 0.9.2-20
- .desktop: drop Category=Development
- app icon: follow icon spec
- drop -emacs subpkg (in main now) 

* Fri Sep 16 2005 Rex Dieter <rexdieter[AT]users.sf.net> - 0.9.2-19
- disable 'make check' (fc5/buildsystem error), besides, we get a 
  good consistency check when M2 builds all the doc examples.

* Wed Sep 14 2005 Rex Dieter <rexdieter[AT]users.sf.net> - 0.9.2-18
- rebuild against gc-6.6

* Thu May 26 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 0.9.2-17
- rebuild (build system x86_64 repository access failed for 0.9.2-16)
- fix build for GCC 4 (#156223)

* Thu Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 0.9.2-15
- rebuilt

* Mon Feb 21 2005 Rex Dieter <rexdieter[AT]users.sf.net> 0:0.9.2-14
- x86_64 issues (%%_libdir -> %%_prefix/lib )
- remove desktop_file macro usage

* Sat Oct 23 2004 Rex Dieter <rexdieter at sf.net> 0:0.9.2-0.fdr.13
- BR: time (again)
- omit m2_dir/setup (not needed/wanted)

* Mon Oct 18 2004 Rex Dieter <rexdieter at sf.net> 0:0.9.2-0.fdr.12
- actually *apply* gcc34 patch this time.

* Mon Oct 18 2004 Rex Dieter <rexdieter at sf.net> 0:0.9.2-0.fdr.11
- gcc34 patch

* Fri Oct 1 2004 Rex Dieter <rexdieter at sf.net> 0:0.9.2-0.fdr.10
- explicit BR versions for gc-devel, libfac-devel, factory-devel

* Tue Aug 10 2004 Rex Dieter <rexdieter at sf.net> 0:0.9.2-0.fdr.9
- BR: time

* Thu Jun 03 2004 Rex Dieter <rexdieter at sf.net> 0:0.9.2-0.fdr.8
- .desktop: remove Terminaloptions to be desktop agnostic
- .desktop: Categories += Education;Math;Development (Devel only
  added so it shows *somewhere* in gnome menus)

* Tue Jun 01 2004 Rex Dieter <rexdieter at sf.net> 0:0.9.2-0.fdr.7
- disable default 'make check' (util/screen fails on fc2)

* Tue Mar 30 2004 Rex Dieter <rexdieter at sf.net> 0:0.9.2-0.fdr.6
- desktop-file is now on by default
- use separate (not inline) .desktop file

* Mon Jan 05 2004 Rex Dieter <rexdieter at sf.net> 0:0.9.2-0.fdr.5
- fix BuildRequires: desktop-file-utils to satisfy rpmlint.
- put emacs files in emacs subdir too (to follow supplied docs)
- *really* nuke .cvsignore files
- fix desktop-file-install --add-cateagories usage

* Tue Dec 23 2003 Rex Dieter <rexdieter at sf.net> 0:0.9.2-0.fdr.4
- -emacs: use %%defattr
- -emacs: fix M2-init.el

* Mon Nov 17 2003 Rex Dieter <rexdieter at sf.net> 0:0.9.2-0.fdr.3
- update/simplify macros
- desktop_file support.
- emacs subpkg.
- relax Req's on subpkgs to just: Requires: %%name = %%epoch:%%version
- use non-versioned BuildRequires
- remove redundant BuildRequires: gmp-devel
- remove gc patch, no longer needed.
- delete/not-package a bunch of unuseful files.
- use --disable-strip when debug_package is in use.

* Thu Nov 13 2003 Rex Dieter <rexdieter at sf.net> 0:0.9.2-0.fdr.2
- no longer explictly Requires: emacs

* Wed Nov 05 2003 Rex Dieter <rexdieter at sf.net> 0:0.9.2-0.fdr.1
- missing Epoch: 0

* Fri Sep 12 2003 Rex Dieter <rexdieter at sf.net> 0.9.2-0.fdr.0
- fedora'ize


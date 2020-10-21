%global ghdlver 0.38~dev
%global ghdldate 20200827
%global ghdlcommit 4ce9925590a96055dabfdd8646055dd378d33650
%global ghdlshortcommit %(c=%{ghdlcommit}; echo ${c:0:7})
%global ghdlgitrev %{ghdldate}git%{ghdlshortcommit}

%ifarch %{ix86} x86_64
%bcond_without mcode
%else
%bcond_with mcode
%endif

#workaround for another compiler error
#bcond_without llvm

#ifarch %%{ix86} x86_64 ppc64le
%ifarch x86_64 ppc64le
%bcond_without llvm
%else
%bcond_with llvm
%endif

%bcond_with gnatwae

%global DATE 20200826
%global gitrev c59c8927f43fb78d6a72a0ff93a47b36e43282d5
%global gcc_version 10.2.1
%global gcc_major 10
# Note, gcc_release must be integer, if you want to add suffixes to
# %%{release}, append them after %%{gcc_release} on Release: line.
%global gcc_release 3
# Hardening slows the compiler way too much.
%undefine _hardened_build
%if 0%{?fedora} > 27 || 0%{?rhel} > 7
# Until annobin is fixed (#1519165).
%undefine _annotated_build
%endif
%global build_isl 1

Summary: A VHDL simulator, using the GCC technology
Name: ghdl
Version: %{ghdlver}
Release: 9.%{ghdlgitrev}%{?dist}
License: GPLv2+ and GPLv3+ and GPLv3+ with exceptions and GPLv2+ with exceptions and LGPLv2+ and BSD
URL: http://ghdl.free.fr/
# The source for this package was pulled from upstream's vcs.  Use the
# following commands to generate the tarball:
# git clone --depth 1 git://gcc.gnu.org/git/gcc.git gcc-dir.tmp
# git --git-dir=gcc-dir.tmp/.git fetch --depth 1 origin %%{gitrev}
# git --git-dir=gcc-dir.tmp/.git archive --prefix=%%{name}-%%{version}-%%{DATE}/ %%{gitrev} | xz -9e > %%{name}-%%{version}-%%{DATE}.tar.xz
# rm -rf gcc-dir.tmp
Source0: gcc-%{gcc_version}-%{DATE}.tar.xz
%global isl_version 0.16.1

Patch0: gcc10-hack.patch
Patch1: gcc10-i386-libgomp.patch
Patch3: gcc10-libgomp-omp_h-multilib.patch
Patch4: gcc10-libtool-no-rpath.patch
Patch5: gcc10-isl-dl.patch
Patch7: gcc10-no-add-needed.patch
Patch8: gcc10-foffload-default.patch
Patch9: gcc10-Wno-format-security.patch
Patch10: gcc10-rh1574936.patch
Patch12: gcc10-pr96383.patch
Patch13: gcc10-pr96385.patch
Patch14: gcc10-pr96690.patch

Source100: https://github.com/ghdl/ghdl/archive/%{ghdlcommit}/%{name}-%{ghdlshortcommit}.tar.gz
Patch100: ghdl-llvmflags.patch
Patch101: ghdl-llvm11.patch
# From: Thomas Sailer <t.sailer@alumni.ethz.ch>
# To: ghdl-discuss@gna.org
# Date: Thu, 02 Apr 2009 15:36:00 +0200
# https://gna.org/bugs/index.php?13390
Patch106: ghdl-ppc64abort.patch
Requires: gcc

Patch200: gcc-config.patch

BuildRequires: binutils >= 2.31
BuildRequires: zlib-devel, gettext, bison, flex
BuildRequires: texinfo
BuildRequires: gmp-devel >= 4.1.2-8, mpfr-devel >= 2.2.1, libmpc-devel >= 0.8.1
BuildRequires: gcc, gcc-c++
# Make sure pthread.h doesn't contain __thread tokens
# Make sure glibc supports stack protector
# Make sure glibc supports DT_GNU_HASH
BuildRequires: glibc-devel >= 2.4.90-13
BuildRequires: elfutils-devel >= 0.147
BuildRequires: elfutils-libelf-devel >= 0.147
%if %{build_isl}
BuildRequires: isl = %{isl_version}
BuildRequires: isl-devel = %{isl_version}
%if 0%{?__isa_bits} == 64
Requires: libisl.so.15()(64bit)
%else
Requires: libisl.so.15
%endif
%endif
Requires: binutils >= 2.31
Requires: libgcc >= %{gcc_version}

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: gcc-gnat
# for x86, we also build the mcode version; if on x86_64, we need some 32bit libraries
%if %{with llvm}
BuildRequires: libedit-devel
BuildRequires: clang
BuildRequires: llvm
BuildRequires: llvm-devel
BuildRequires: llvm-static
%endif

Requires: ghdl-grt = %{version}-%{release}
Provides: bundled(libiberty)

# gcc-gnat only available on these:
ExclusiveArch: %{GNAT_arches}

# the following arches are not supported by the base compiler:
ExcludeArch: armv7hl

# Make sure we don't use clashing namespaces
%global _vendor fedora_ghdl

%global _gnu %{nil}
%global gcc_target_platform %{_target_platform}

# do not strip libgrt.a -- makes debugging tedious otherwise
%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's#/usr/lib/rpm/redhat/brp-strip-static-archive .*##g')

%description
GHDL is the open-source analyzer, compiler, simulator and (experimental)
synthesizer for VHDL, a Hardware Description Language (HDL). GHDL implements
the VHDL language according to the 1987, 1993 and 2002 versions of the IEEE
1076 VHDL standard, and partial for 2008. It compiles VHDL files and creates
a binary that simulates (or executes) your design. GHDL can also translate
a design into a VHDL 1993 netlist, or it can be plugged into Yosys for
open-source synthesis.

Since GHDL is a compiler (i.e., it generates object files), you can call
functions or procedures written in a foreign language, such as C, C++, Ada95
or Python.

%package grt
Summary: GHDL runtime libraries
# rhbz #316311
Requires: zlib-devel, libgnat >= 4.3

%description grt
This package contains the runtime libraries needed to link ghdl-compiled
object files into simulator executables. grt contains the simulator kernel
that tracks signal updates and schedules processes.

%ifarch %{ix86} x86_64
%if %{with mcode}
%package mcode
Summary: GHDL with mcode backend
Requires: ghdl-mcode-grt = %{version}-%{release}

%description mcode
This package contains the ghdl compiler with the mcode backend. The mcode
backend provides for faster compile time at the expense of longer run time.

%package mcode-grt
Summary: GHDL mcode runtime libraries

%description mcode-grt
This package contains the runtime libraries needed to link ghdl-mcode-compiled
object files into simulator executables. mcode-grt contains the simulator kernel
that tracks signal updates and schedules processes.
%endif
%endif

%if %{with llvm}
%package llvm
Summary: GHDL with LLVM backend
Requires: ghdl-llvm-grt = %{version}-%{release}

%description llvm
This package contains the ghdl compiler with the LLVM backend. The LLVM
backend is experimental.

%package llvm-grt
Summary: GHDL LLVM runtime libraries

%description llvm-grt
This package contains the runtime libraries needed to link ghdl-llvm-compiled
object files into simulator executables. llvm-grt contains the simulator kernel
that tracks signal updates and schedules processes.
%endif

%prep
%setup -q -n gcc-%{gcc_version}-%{DATE} -a 100
%patch0 -p0 -b .hack~
%patch1 -p0 -b .i386-libgomp~
%patch3 -p0 -b .libgomp-omp_h-multilib~
%patch4 -p0 -b .libtool-no-rpath~
%if %{build_isl}
%patch5 -p0 -b .isl-dl~
%endif
%patch7 -p0 -b .no-add-needed~
%patch8 -p0 -b .foffload-default~
%patch9 -p0 -b .Wno-format-security~
%if 0%{?fedora} >= 29 || 0%{?rhel} > 7
%patch10 -p0 -b .rh1574936~
%endif
%patch12 -p0 -b .pr96383~
%patch13 -p0 -b .pr96385~
%patch14 -p0 -b .pr96690~

%patch200 -p1
pushd libiberty
autoconf -f
popd
pushd intl
autoconf -f
popd

echo 'Red Hat %{version}-%{gcc_release}' > gcc/DEV-PHASE

cp -a libstdc++-v3/config/cpu/i{4,3}86/atomicity.h

./contrib/gcc_update --touch

LC_ALL=C sed -i -e 's/\xa0/ /' gcc/doc/options.texi

sed -i -e 's/Common Driver Var(flag_report_bug)/& Init(1)/' gcc/common.opt

# This test causes fork failures, because it spawns way too many threads
rm -f gcc/testsuite/go.test/test/chan/goroutines.go

# ghdl
mv ghdl-%{ghdlcommit} ghdl
%patch100 -p0 -b .llvmflags~
%patch101 -p0 -b .llvm11~

# fix library and include path
pushd ghdl
sed -i.orig -e 's|\"lib\"|\"%{_lib}\"|' -e 's|\"include\"|\"include/ghdl\"|' src/ghdldrv/ghdlsynth.adb
sed -i.orig -e 's|\"lib\"|\"%{_lib}\"|' -e 's|\"include\"|\"include/ghdl\"|' src/ghdldrv/ghdlvpi.adb
popd

%if %{without gnatwae}
perl -i -pe 's,-gnatwae,,' ghdl/dist/gcc/Make-lang.in
%endif

%if %{with mcode}
cp -r ghdl ghdl-mcode
pushd ghdl-mcode
perl -i -pe 's,^libdirsuffix=.*$,libdirsuffix=%{_lib}/ghdl/mcode,' configure
perl -i -pe 's,^libdirreverse=.*$,libdirreverse=../../..,' configure
popd
%endif

%if %{with llvm}
cp -r ghdl ghdl-llvm
pushd ghdl-llvm
perl -i -pe 's,^libdirsuffix=.*$,libdirsuffix=%{_lib}/ghdl/llvm,' configure
perl -i -pe 's,^libdirreverse=.*$,libdirreverse=../../..,' configure
popd
%endif

echo 'Red Hat %{version}-%{gcc_release}' > gcc/DEV-PHASE

pushd ghdl
./configure --prefix=/usr --with-gcc=.. --enable-libghdl --enable-synth
make copy-sources
popd

%patch106 -p0 -b .ppc64abort

%build

# build mcode on x86
%if %{with mcode}
pushd ghdl-mcode
./configure \
%if %{without gnatwae}
	--disable-werror \
%endif
	--prefix=/usr --enable-libghdl --enable-synth
make %{?_smp_mflags}
popd
%endif

%if %{with llvm}
pushd ghdl-llvm
./configure --prefix=/usr \
%if %{without gnatwae}
	--disable-werror \
%endif
	--with-llvm-config=/usr/bin/llvm-config --enable-libghdl --enable-synth
make %{?_smp_mflags} LDFLAGS=-Wl,--build-id
popd
%endif

# Undo the broken autoconf change in recent Fedora versions
export CONFIG_SITE=NONE

CC=gcc
CXX=g++
OPT_FLAGS=`echo %{optflags}|sed -e 's/\(-Wp,\)\?-D_FORTIFY_SOURCE=[12]//g'`
OPT_FLAGS=`echo $OPT_FLAGS|sed -e 's/-flto=auto//g;s/-flto//g;s/-ffat-lto-objects//g'`
OPT_FLAGS=`echo $OPT_FLAGS|sed -e 's/-m64//g;s/-m32//g;s/-m31//g'`
OPT_FLAGS=`echo $OPT_FLAGS|sed -e 's/-mfpmath=sse/-mfpmath=sse -msse2/g'`
OPT_FLAGS=`echo $OPT_FLAGS|sed -e 's/ -pipe / /g'`
OPT_FLAGS=`echo $OPT_FLAGS|sed -e 's/-Werror=format-security/-Wformat-security/g'`
%ifarch %{ix86}
OPT_FLAGS=`echo $OPT_FLAGS|sed -e 's/-march=i.86//g'`
%endif
OPT_FLAGS=`echo "$OPT_FLAGS" | sed -e 's/[[:blank:]]\+/ /g'`
case "$OPT_FLAGS" in
  *-fasynchronous-unwind-tables*)
    sed -i -e 's/-fno-exceptions /-fno-exceptions -fno-asynchronous-unwind-tables /' \
      libgcc/Makefile.in
    ;;
esac


rm -rf obj-%{gcc_target_platform}
mkdir obj-%{gcc_target_platform}
pushd obj-%{gcc_target_platform}

CONFIGURE_OPTS="\
	--prefix=%{_prefix} --mandir=%{_mandir} --infodir=%{_infodir} \
	--with-bugurl=http://bugzilla.redhat.com/bugzilla \
	--enable-shared --enable-threads=posix --enable-checking=release \
%ifarch ppc64le
	--enable-targets=powerpcle-linux \
%endif
	--disable-multilib \
	--with-system-zlib --enable-__cxa_atexit --disable-libunwind-exceptions \
	--enable-gnu-unique-object --enable-linker-build-id --with-gcc-major-version-only \
	--with-linker-hash-style=gnu \
	--enable-plugin --enable-initfini-array \
%if %{build_isl}
	--with-isl \
%else
	--without-isl \
%endif
%ifarch %{arm}
	--disable-sjlj-exceptions \
%endif
%ifarch ppc64le
	--enable-secureplt \
%endif
%ifarch ppc64le s390x
	--with-long-double-128 \
%endif
%ifarch ppc64le
	--with-cpu-32=power8 --with-tune-32=power8 --with-cpu-64=power8 --with-tune-64=power8 \
%endif
%ifarch %{ix86} x86_64
	--enable-cet \
	--with-tune=generic \
%endif
%if 0%{?rhel} >= 7
%ifarch %{ix86}
	--with-arch=x86-64 \
%endif
%ifarch x86_64
	--with-arch_32=x86-64 \
%endif
%else
%ifarch %{ix86}
	--with-arch=i686 \
%endif
%ifarch x86_64
	--with-arch_32=i686 \
%endif
%endif
%ifarch s390 s390x
%if 0%{?rhel} >= 7
%if 0%{?rhel} > 7
	--with-arch=zEC12 --with-tune=z13 \
%else
	--with-arch=z196 --with-tune=zEC12 \
%endif
%else
%if 0%{?fedora} >= 26
	--with-arch=zEC12 --with-tune=z13 \
%else
	--with-arch=z9-109 --with-tune=z10 \
%endif
%endif
	--enable-decimal-float \
%endif
%ifarch armv7hl
	--with-tune=generic-armv7-a --with-arch=armv7-a \
	--with-float=hard --with-fpu=vfpv3-d16 --with-abi=aapcs-linux \
%endif
	--build=%{gcc_target_platform} \
	"

CC="$CC" CXX="$CXX" CFLAGS="$OPT_FLAGS" \
	CXXFLAGS="`echo " $OPT_FLAGS " | sed 's/ -Wall / /g;s/ -fexceptions / /g' \
		  | sed 's/ -Wformat-security / -Wformat -Wformat-security /'`" \
	XCFLAGS="$OPT_FLAGS" TCFLAGS="$OPT_FLAGS" \
	../configure --enable-bootstrap=no \
	--enable-languages=vhdl \
	$CONFIGURE_OPTS

make %{?_smp_mflags}
pushd gcc/vhdl
gnatmake -c -aI%{_builddir}/gcc-%{gcc_version}-%{DATE}/gcc/vhdl ortho_gcc-main \
  -cargs -g -Wall -fexceptions -fstack-protector-strong --param=ssp-buffer-size=4 -grecord-gcc-switches -specs=/usr/lib/rpm/redhat/redhat-hardened-cc1 \
%ifarch %{ix86} x86_64
  -mtune=generic \
%endif
%ifarch ppc64le
  -mcpu=power8 -mtune=power8 \
%endif
  -gnata -gnat05 -gnaty3befhkmr
#-gnatwae
popd

make %{?_smp_mflags}

popd

%install
# install mcode on x86
%if %{with mcode}
pushd ghdl-mcode
make DESTDIR=%{buildroot} install
mv %{buildroot}/%{_bindir}/ghdl %{buildroot}/%{_bindir}/ghdl-mcode
popd
%endif

# install llvm
%if %{with llvm}
pushd ghdl-llvm
%make_install
mv %{buildroot}/%{_bindir}/ghdl %{buildroot}/%{_bindir}/ghdl-llvm
popd
%endif

# install gcc
%make_install -C obj-%{gcc_target_platform}

PBINDIR=`pwd`/obj-%{gcc_target_platform}/gcc/

pushd ghdl
make bindir=${PBINDIR} GHDL1_GCC_BIN="--GHDL1=${PBINDIR}/ghdl1" ghdllib
%make_install
popd

# Add additional libraries to link
(
echo "-lgnat-`gnatmake --version| sed -n 's/^GNATMAKE \([^.]*\)\..*$/\1/p'`"
) >> %{buildroot}%{_prefix}/lib/ghdl/grt.lst

# Remove files not to be packaged
pushd %{buildroot}
rm -f \
        .%{_bindir}/{cpp,gcc,gccbug,gcov,gcov-dump,gcov-tool,lto-dump} \
        .%{_bindir}/%{gcc_target_platform}-gcc{,-%{gcc_major}} \
        .%{_bindir}/{,%{gcc_target_platform}-}gcc-{ar,nm,ranlib} \
        .%{_includedir}/mf-runtime.h \
        .%{_libdir}/lib{atomic,cc1,gcc_s,gomp,quadmath,ssp}* \
        .%{_infodir}/dir \
        .%{_infodir}/{cpp,cppinternals,gcc,gccinstall,gccint}.info* \
        .%{_infodir}/{libgomp,libquadmath}.info* \
        .%{_datadir}/locale/*/LC_MESSAGES/{gcc,cpplib}.mo \
        .%{_mandir}/man1/{cpp,gcc,gcov,gcov-dump,gcov-tool,lto-dump}.1* \
        .%{_mandir}/man7/{fsf-funding,gfdl,gpl}.7* \
        .%{_prefix}/lib/libgcc_s.* \
        .%{_prefix}/lib/libmudflap.* \
        .%{_prefix}/lib/libmudflapth.* \
        .%{_prefix}/lib/lib{atomic,gomp,quadmath,ssp}* \
        .%{_libdir}/32/libiberty.a

# Remove crt/libgcc, as ghdl invokes the native gcc to perform the linking
rm -f \
        .%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/*crt* \
        .%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/libgc* \
        .%{_libexecdir}/gcc/%{gcc_target_platform}/%{gcc_major}/{cc1,collect2} \
        .%{_libexecdir}/gcc/%{gcc_target_platform}/%{gcc_major}/*lto*

# Remove directory hierarchies not to be packaged
rm -rf \
        .%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/{include,include-fixed,plugin,install-tools} \
        .%{_libexecdir}/gcc/%{gcc_target_platform}/%{gcc_major}/install-tools \
        .%{_libexecdir}/gcc/%{gcc_target_platform}/%{gcc_major}/plugin \

popd

install -d %{buildroot}%{_includedir}/ghdl
mv %{buildroot}%{_includedir}/vpi_user.h %{buildroot}%{_includedir}/ghdl
mv %{buildroot}%{_includedir}/ghdlsynth*.h %{buildroot}%{_includedir}/ghdl
%if "%{_lib}" != "lib"
mv %{buildroot}/usr/lib/libghdlvpi.so %{buildroot}%{_libdir}/
mv %{buildroot}/usr/lib/libghdl-*.so %{buildroot}%{_libdir}/
%endif
# remove static libghdl
rm %{buildroot}/usr/lib/libghdl.{a,link}

%files
%{_bindir}/ghdl
%{_infodir}/ghdl.info.*
# Need to own directory %%{_libexecdir}/gcc even though we only want the
# %%{gcc_target_platform}/%%{gcc_version} subdirectory
%{_libexecdir}/gcc/
%{_mandir}/man1/*
%{_includedir}/ghdl/vpi_user.h
%{_includedir}/ghdl/ghdlsynth*.h
%{_libdir}/libghdl*.so

%files grt
# Need to own directory %%{_libdir}/gcc even though we only want the
# %%{gcc_target_platform}/%%{gcc_version} subdirectory
%{_prefix}/lib/gcc/
%{_prefix}/lib/ghdl/

%if %{with mcode}
%files mcode
%{_bindir}/ghdl-mcode

%files mcode-grt
%dir %{_libdir}/ghdl
%{_libdir}/ghdl/mcode
%endif

%if %{with llvm}
%files llvm
%{_bindir}/ghdl-llvm
%{_bindir}/ghdl1-llvm

%files llvm-grt
%dir %{_libdir}/ghdl
%{_libdir}/ghdl/llvm
%endif

%changelog
* Fri Aug 28 2020 Dan Horák <dan[at]danny.cz> - 0.38~dev-9.20200827git4ce9925
- updated to new ghdl snapshot
- updated to gcc 10.2.1-3
- enabled parallel make

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.38~dev-8.20200702git9828b51
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.38~dev-7.20200702git9828b51
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 20 2020 Jeff Law <law@redhat.com> - 0.38~dev-6.20200702git9828b51
- Fix broken configure tests compromised by LTO

* Fri Jul 03 2020 Dan Horák <dan[at]danny.cz> - 0.38~dev-5.20200702git9828b51
- updated to new ghdl snapshot

* Thu Jun 25 2020 Dan Horák <dan[at]danny.cz> - 0.38~dev-4.20200619git18a71a4
- updated to new ghdl snapshot
- updated to gcc 10.1.1-2

* Tue Jun 23 2020 Matthias Wächter <matthias@waechter.wiz.at> - 0.38~dev-3.20200428gitad4e2f3
- fix dependency on libgnat

* Wed Apr 29 2020 Dan Horák <dan[at]danny.cz> - 0.38~dev-2.20200428gitad4e2f3
- updated to new ghdl snapshot

* Mon Apr 13 2020 Dan Horák <dan[at]danny.cz> - 0.38~dev-1.20200413git9974f20
- updated to new ghdl snapshot

* Mon Apr 06 2020 Björn Esser <besser82@fedoraproject.org> - 0.37dev-16.20200201git5428d6e
- Update patch to fix build with llvm 10 from upstream

* Thu Apr 02 2020 Björn Esser <besser82@fedoraproject.org> - 0.37dev-15.20200201git5428d6e
- Fix string quoting for rpm >= 4.16
- Add patch to fix build with llvm 10

* Sun Feb 02 2020 Dan Horák <dan[at]danny.cz> - 0.37dev-14.20200201git5428d6e
- drop unneeded man page

* Sat Feb 01 2020 Dan Horák <dan[at]danny.cz> - 0.37dev-13.20200201git5428d6e
- updated to new ghdl snapshot

* Wed Jan 29 2020 Dan Horák <dan[at]danny.cz> - 0.37dev-12.20200127gita4fdd19
- rebased to gcc 10.0.1

* Wed Jan 29 2020 Dan Horák <dan[at]danny.cz> - 0.37dev-11.20200127gita4fdd19
- updated to new ghdl snapshot

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.37dev-10.20191224git38c38e7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 28 2019 Dan Horák <dan[at]danny.cz> - 0.37dev-9.20191224git38c38e7
- updated to new ghdl snapshot

* Tue Dec 10 2019 Dan Horák <dan[at]danny.cz> - 0.37dev-8.20191206git208f254
- updated to new ghdl snapshot

* Sun Dec 01 2019 Dan Horák <dan[at]danny.cz> - 0.37dev-7.20191130git3bd9a18
- updated to new ghdl snapshot
- fix library and include path for synth

* Thu Nov 21 2019 Dan Horák <dan[at]danny.cz> - 0.37dev-6.20191121git03862a4
- updated to new ghdl snapshot
- rebased to gcc 9.2.1
- many cleanups

* Sun Nov 03 2019 Dan Horák <dan[at]danny.cz> - 0.37dev-5.20191102git534f39a
- updated to new ghdl snapshot

* Wed Oct  9 2019 Jerry James <loganjerry@gmail.com> - 0.37dev-4.20190923git4ec17bb
- Rebuild for mpfr 4
- Drop multilib support for s390x as glibc32 and gcc have done

* Tue Sep 24 2019 Dan Horák <dan[at]danny.cz> - 0.37dev-3.20190923git4ec17bb
- updated to new ghdl snapshot

* Tue Sep 10 2019 Dan Horák <dan[at]danny.cz> - 0.37dev-2.20190907gitcb34680
- updated to new ghdl snapshot

* Thu Sep 05 2019 Dan Horák <dan[at]danny.cz> - 0.37dev-1.20190820gitf977ba0
- rebased to 0.37dev
- various cleanups and updates

* Fri Aug 23 2019 Dan Horák <dan[at]danny.cz> - 0.35dev-5.20190528git3fafb135.0
- enable ppc64le

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.35dev-4.20190528git3fafb135.0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 28 2019 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.35dev-3.20190528git3fafb135.0
- update to 0.35dev (20190528git3fafb135)
- fix R: libgcc

* Mon May 20 2019 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.35dev-3.20190520git150116d2.0
- update to 0.35dev (20190520git150116d2)
- update gcc to 9.1.1

* Wed Apr 24 2019 Björn Esser <besser82@fedoraproject.org> - 0.35dev-3.20190301gita62344e.0
- Remove hardcoded gzip suffix from GNU info pages

* Fri Mar 01 2019 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.35dev-2.20190301gita62344e.0
- update to 0.35dev (20190301gita62344e)

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.35dev-2.20190129git3c30e3b.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 30 2019 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.35dev-1.20190129git3c30e3b.1
- update base gcc to 8.2.1

* Tue Jan 29 2019 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.35dev-1.20190129git3c30e3b.0
- update to 0.35dev (20190129git3c30e3b)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.35dev-1.20180520git66bb071.0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun May 20 2018 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.35dev-0.20180520git66bb071.0
- update to 0.35dev (git66bb071)

* Thu Mar 15 2018 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.35dev-0.20180315git0edf0a1.0
- update to 0.35dev (git0edf0a1)

* Thu Mar 15 2018 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.35dev-0.20180311git46c5015.0
- update to 0.34dev (git46c5015)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.34dev-1.20170926git685526e.0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Sep 26 2017 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.34dev-0.20170926git685526e.0
- update to 0.34dev (git685526e)

* Tue Aug 15 2017 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.34dev-0.20170815git0879429a.0
- update to 0.34dev (git0879429a)

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.34dev-2.20170715gitc14fe80.0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.34dev-1.20170715gitc14fe80.0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jul 15 2017 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.34dev-0.20170715gitc14fe80.0
- update to 0.34dev (gitc14fe80)

* Wed Jul 12 2017 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.34dev-0.20170712git5783528.0
- update to 0.34dev (git5783528)

* Fri Mar 24 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.34dev-0.20170302git31f8e7a.1
- Use LLVM 3.9

* Thu Mar 02 2017 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.34dev-0.20170302git31f8e7a.0
- update to 0.34dev (git31f8e7a)

* Tue Feb 21 2017 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.34dev-0.20170221git663ebfd.0
- update to 0.34dev (git663ebfd)

* Tue Feb 07 2017 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.34dev-0.20170207gitdb4b46e.0
- update to 0.34dev (gitdb4b46e)

* Fri Jul 01 2016 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.34dev-0.20160702git50d0507.0
- update to 0.34dev (git50d0507)

* Thu May 26 2016 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.34dev-0.20160503git6ccb80e.0
- update to 0.34dev (git6ccb80e)

* Sat Mar 19 2016 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.34dev-0.20160318git8e97758.0
- update to 0.34dev (git8e97758)

* Thu Mar 17 2016 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.34dev-0.20160317gitf1ddf16.0
- update to 0.34dev (gitf1ddf16)

* Wed Feb 24 2016 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.34dev-0.20160224gitf818155.0
- update to 0.34dev (gitf818155)

* Tue Feb 16 2016 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.34dev-0.20160214gite7adf19.0
- update to 0.34dev (gite7adf19)

* Fri Feb 12 2016 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.33dev-1.20151120gitff4bc5f.1
- build fix

* Fri Nov 20 2015 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.33dev-1.20151120gitff4bc5f.0
- update to 0.33dev (gitff4bc5f)

* Mon Nov  9 2015 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.33dev-0.hg914.0
- update to 0.33dev (hg914)

* Fri Oct 30 2015 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.33dev-0.hg903.0
- update to 0.33dev (hg903)

* Mon Oct 19 2015 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.33dev-0.hg899.0
- update to 0.33dev (hg899)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.33dev-1.hg813.0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 04 2015 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.33dev-0.hg813.0
- update to 0.33dev (hg813)

* Sat Mar 14 2015 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.33dev-0.hg700.0
- update to 0.33dev (hg700)

* Thu Mar 12 2015 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.33dev-0.hg692.0
- update to 0.33dev (hg692)

* Wed Mar 11 2015 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.33dev-0.hg688.0
- update to 0.33dev (hg688)
- build mcode backend on x86(-32)
- build LLVM backend

* Wed Nov 19 2014 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.32rc1-0.hg484.0
- update to 0.32rc1 (hg484)

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.31-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.31-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 13 2014 Peter Robinson <pbrobinson@fedoraproject.org> 0.31-4
- Use GNAT_arches rather than an explicit list

* Wed Apr 30 2014 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.31-3
- rebuild for gnat 4.9

* Sat Feb  1 2014 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.31-2
- update to release 0.31

* Wed Dec 18 2013 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.31-1
- change to sourceforge repository

* Tue Dec  3 2013 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.29-4.150svn.3
- prevent format-security warning

* Mon Aug  5 2013 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.29-4.150svn.2
- fix FTBFS

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.29-4.150svn.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul  2 2013 Ville Skyttä <ville.skytta@iki.fi> - 0.29-3.150svn.2
- Compress gcc tarball with xz.

* Wed May  1 2013 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.29-3.150svn.1
- update for gnat 4.8
- texinfo build fix

* Fri Feb  1 2013 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.29-3.150svn.0
- update to svn150 (based on gcc 4.7.2)

* Fri Jan 25 2013 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.29-3.143svn.8
- rebuild for gnat 4.8

* Mon Oct 15 2012 Jon Ciesls <limburgher@gmail.com> - 0.29-3.143svn.7
- Provides: bundled(libiberty)

* Wed Jul 25 2012 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.29-2.143svn.7
- fix siginfo build failure

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.29-2.143svn.7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.29-2.143svn.6
- rebuild for grt file times

* Thu Jan  5 2012 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.29-2.143svn.5
- rebuild for gnat 4.7

* Fri Oct 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.29-2.143svn.4.2
- rebuild with new gmp without compat lib

* Tue Oct 11 2011 Peter Schiffer <pschiffe@redhat.com> - 0.29-2.143svn.4.1
- rebuild with new gmp

* Tue Feb 22 2011 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.29-2.143svn.4
- rebuild for gnat 4.6

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.29-2.143svn.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Feb  1 2011 Dan Horák <dan[at]danny.cz> - 0.29-1.143svn.3
- updated the supported arch list
- remove the offending space in BR: glibc

* Sun Jan 23 2011 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.29-1.143svn.2
- rebuild

* Fri Jul  9 2010 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.29-1.143svn.1
- update to gnat 4.5

* Thu Jul  8 2010 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.29-1.143svn.0
- update to svn143
- move license text to grt subpackage

* Fri Jan 29 2010 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.29-1.138svn.0
- update to svn138

* Fri Jan 15 2010 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.29-1
- update to 0.29

* Wed Dec 30 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.28-0.135svn.0
- update to svn135

* Wed Dec 30 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.28-0.133svn.2
- fix the Process Timeout Chain bugfix

* Wed Dec 30 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.28-0.133svn.1
- fix crash when running ./tb --stats

* Wed Dec 16 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.28-0.133svn.0
- update to svn133, drop upstreamed patches

* Mon Dec 14 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.28-0.131svn.2
- Process Timeout Chain bugfix
- --trace-signals memory leak fix

* Wed Dec  2 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.28-0.131svn.1
- copy v08 libraries instead of symlink

* Wed Dec  2 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.28-0.131svn.0
- update to 0.28/svn131
- symlink v08 libraries to v93 for now

* Wed Sep 23 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.28-0.130svn.0
- update to 0.28/svn130

* Sun Sep 20 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.27-0.126svn.0
- update to svn126

* Sun Jul 26 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.27-0.110svn.8
- this gcc does not understand -mtune=atom

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.27-0.110svn.7.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue May 26 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.27-0.110svn.7
- fix bug in std.textio.read (string)

* Thu Apr  2 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.27-0.110svn.6
- actually add the patch

* Wed Apr  1 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.27-0.110svn.5
- make ieee.math_real more standards compliant

* Sun Mar 15 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.27-0.110svn.4
- gnat version is now 4.4

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.27-0.110svn.3.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 13 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.27-0.110svn.3
- prevent ppc64 abort due to unknown language type

* Fri Feb 13 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.27-0.110svn.2
- rebuild with ppc64

* Thu Oct  9 2008 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.27-0.110svn.1
- rebuild

* Tue Oct  7 2008 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.27-0.110svn.0
- update to svn110

* Tue Oct  7 2008 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.27-0.105svn.0
- update to svn105

* Mon Jun  2 2008 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.26-0.98svn.0
- update to svn98

* Fri May 16 2008 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.26-0.94svn.7
- update to svn94

* Sun Jan  6 2008 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.25-0.89svn.7
- disable Pragma No_Run_Time; it does not seem to make much sense and causes
  problems with gcc-4.3

* Mon Oct  8 2007 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.25-0.89svn.6
- ghdl-grt requires zlib-devel (rhbz 316311)
- make it build with makeinfo >= 4.10

* Fri Aug 24 2007 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.25-0.89svn.5
- excludearch ppc64

* Fri Aug 24 2007 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.25-0.89svn.4
- fix BR

* Fri Aug 24 2007 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.25-0.89svn.3
- fix license tag

* Fri Jan  5 2007 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.25-0.89svn.2
- do not try to set user/group during install

* Fri Jan  5 2007 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.25-0.89svn.1
- back out hunks that cause build failures
- un-exclude ppc

* Mon Nov 20 2006 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.25-0.89svn.0
- update to svn89

* Fri Oct  6 2006 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.25-0.73svn.0
- update to svn73

* Thu Oct  5 2006 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.25-0.71svn.1
- bump release

* Thu Oct  5 2006 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.25-0.71svn.0
- update to svn71

* Sun Aug 27 2006 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.25-0.61svn.0
- update to svn61

* Sun Aug  6 2006 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.24-0.60svn.0
- update to svn60

* Tue Jul 11 2006 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.24-0.59svn.2
- rebuild

* Mon Jul 10 2006 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.24-0.59svn.1
- add missing manpage

* Mon Jul 10 2006 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.24-0.59svn.0
- update to svn59

* Sun Jun 25 2006 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.23-0.58svn.0
- update to svn58

* Tue Jun 20 2006 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.23-0.57svn.0
- update to svn57

* Fri Mar 24 2006 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.22-0.50svn.1
- do not require /lib/libc.so.* on x86_64, this does not work under mock

* Wed Mar 22 2006 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.22-0.50svn.0
- update to svn50, to fix x86_64 breakage
- move grt (ghdl runtime library) into separate package, to allow parallel
  install of i386 and x86_64 grt on x86_64 machines, thus making -m32 work
- back to using FSF gcc as base compiler sources, using core gcc sources
  causes segfaults during library compile on x86_64

* Sun Mar 19 2006 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.22-0.49svn.1
- use core gcc as base compiler sources

* Thu Mar 16 2006 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.22-0.49svn.0
- update to svn49, using gcc 4.1.0

* Mon Mar  6 2006 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.22-0.40svn.0
- update to svn40, to fix an array bounds checking bug apparently
  introduced in svn39

* Thu Feb 16 2006 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.22-0.39svn.0
- update to svn39, to fix some constant bugs

* Tue Feb 14 2006 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.22-0.38svn.1
- rebuild with new compiler for FC5

* Wed Dec 21 2005 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.22-0.38svn.0
- update to svn38, to fix a ghw output bug

* Sun Dec 18 2005 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.21-1
- update to 0.21

* Thu Dec 15 2005 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.21-0.35svn.1
- update to svn35 for more x86_64 "Ada cannot portably call C vararg functions"
  fixes
- first stab at -m32 library building

* Sat Dec 10 2005 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.21-0.33svn.1
- update to svn33, to fix x86_64 issues (real'image, -m32)
- rpmbuild option --without mock enables multilib builds

* Mon Dec  5 2005 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.21-0.24svn.3
- disable multilib and remove exclude of x86_64

* Thu Dec  1 2005 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.21-0.24svn.2
- Exclude ppc because gcc-gnat is missing
- Exclude x86_64 because of mock build issues

* Fri Nov 25 2005 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.21-0.24svn.1
- update to SVN rev 24
- remove additional files to fix x86_64 build

* Tue Nov 22 2005 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.21-0.23svn.1
- update to SVN rev 23

* Mon Nov 14 2005 Paul Howarth <paul@city-fan.org> - 0.21-0.21.1
- spec file cosmetic cleanups
- incorporate some architecture tweaks from gcc package
- remove files we don't want packaged so that we can turn the unpackaged file
  check back on
- use fedora_ghdl as the machine vendor name to avoid namespace clashes with
  other packages
- own {%%{_libdir},%%{_libexecdir}}/gcc directories since this package does not
  depend on gcc
- add buildreq texinfo, needed to make info file
- don't include README, which is aimed at building ghdl rather than using it
- remove install-tools and munged header files, not needed for ghdl
- only run install-info if the info file is installed
- patch ghdl.texi to include info dir entry

* Fri Nov 11 2005 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.21-0.21
- update to 0.21pre, svn rev 21
- incorporate changes from Paul Howarth

* Sat Mar 12 2005 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.18-1
- update to 0.18

* Sat Feb 26 2005 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.17-1
- update to 0.17

* Tue Feb  8 2005 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.16-1
- Initial build.

# Components enabled if supported by target architecture:
%ifarch %ix86 x86_64
  %bcond_without gold
%else
  %bcond_with gold
%endif

%global ver_major_minor 5.0
%global exec_suffix -%{ver_major_minor}
%global install_prefix %{_libdir}/%{name}
%global install_bindir %{install_prefix}/bin
%global install_includedir %{install_prefix}/include
%global install_libdir %{install_prefix}/lib

%global pkg_bindir %{install_bindir}
%global pkg_includedir %{_includedir}/%{name}
%global pkg_libdir %{install_libdir}

# https://bugzilla.redhat.com/show_bug.cgi?id=1538318
%undefine _strict_symbol_defs_build

Name:		llvm%{ver_major_minor}
Version:	%ver_major_minor.1
Release:	11%{?dist}
Summary:	The Low Level Virtual Machine

License:	NCSA
URL:		http://llvm.org
Source0:	http://llvm.org/releases/%{version}/llvm-%{version}.src.tar.xz

# recognize s390 as SystemZ when configuring build
Patch0:		llvm-3.7.1-cmake-s390.patch
Patch2: 	0001-Fix-llvm-config-paths-on-Fedora.patch
# FIXME: Symbol versioning breaks some unittests when statically linking
# libstdc++, so we disable it for now.
Patch4:		0001-Revert-Add-a-linker-script-to-version-LLVM-symbols.patch
Patch5:		0001-CMake-Split-static-library-exports-into-their-own-ex.patch
Patch6:		0001-PowerPC-Don-t-use-xscvdpspn-on-the-P7.patch
Patch7:		0001-Fix-return-type-in-ORC-readMem-client-interface.patch
Patch8:		0001-Ignore-all-duplicate-frame-index-expression.patch
Patch9:		0002-Reinstantiate-old-bad-deduplication-logic-that-was-r.patch
Patch10:	0001-PPC-Avoid-non-simple-MVT-in-STBRX-optimization.patch


BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:	cmake
BuildRequires:	zlib-devel
BuildRequires:  libffi-devel
BuildRequires:	ncurses-devel
BuildRequires:	python3-sphinx
BuildRequires:	multilib-rpm-config
%if %{with gold}
BuildRequires:  binutils-devel
%endif
BuildRequires:  libstdc++-static
# Enable extra functionality when run the LLVM JIT under valgrind.
BuildRequires:  valgrind-devel
# LLVM's LineEditor library will use libedit if it is available.
BuildRequires:  libedit-devel

Requires:	%{name}-libs%{?_isa} = %{version}-%{release}

%description
LLVM is a compiler infrastructure designed for compile-time, link-time,
runtime, and idle-time optimization of programs from arbitrary programming
languages. The compiler infrastructure includes mirror sets of programming
tools as well as libraries with equivalent functionality.

%package devel
Summary:	Libraries and header files for LLVM
Requires:	%{name}%{?_isa} = %{version}-%{release}
# The installed LLVM cmake files will add -ledit to the linker flags for any
# app that requires the libLLVMLineEditor, so we need to make sure
# libedit-devel is available.
Requires:      libedit-devel
Requires(post): %{_sbindir}/alternatives
Requires(postun): %{_sbindir}/alternatives

%description devel
This package contains library and header files needed to develop new native
programs that use the LLVM infrastructure.

%package doc
Summary:	Documentation for LLVM
BuildArch:	noarch
Requires:	%{name} = %{version}-%{release}

%description doc
Documentation for the LLVM compiler infrastructure.

%package libs
Summary:	LLVM shared libraries

%description libs
Shared libraries for the LLVM compiler infrastructure.


%package static
Summary:        LLVM %{ver_major_minor} static libraries
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Requires:       ncurses-devel%{?_isa}

%description static
Static libraries for the LLVM compiler infrastructure.

This package contains LLVM %{ver_major_minor} and can be installed
in parallel with other LLVM versions.

%prep
%autosetup -n llvm-%{version}.src -p1

%ifarch armv7hl

# These tests are marked as XFAIL, but they still run and hang on ARM.
for f in `grep -Rl 'XFAIL.\+arm' test/ExecutionEngine `; do  rm $f; done

%endif

%build
mkdir -p _build
cd _build

%ifarch s390 %{arm} %{ix86}
# use linker flags that prioritize efficiency over speed (try and save memory)
%global optflags %{optflags} -Wl,--no-keep-memory -Wl,--reduce-memory-overheads
# Decrease debuginfo verbosity to reduce memory consumption during final library linking
%global optflags %(echo %{optflags} | sed 's/-g /-g1 /')
%endif

# force off shared libs as cmake macros turns it on.
%cmake .. \
	-DBUILD_SHARED_LIBS:BOOL=OFF \
	-DCMAKE_BUILD_TYPE=RelWithDebInfo \
	-DCMAKE_SHARED_LINKER_FLAGS="-Wl,-Bsymbolic -static-libstdc++" \
%ifarch s390 %{arm}
	-DCMAKE_C_FLAGS_RELWITHDEBINFO="%{optflags} -DNDEBUG" \
	-DCMAKE_CXX_FLAGS_RELWITHDEBINFO="%{optflags} -DNDEBUG" \
%endif
	\
	-DCMAKE_INSTALL_PREFIX=%{install_prefix} \
	-DLLVM_TARGETS_TO_BUILD="X86;AMDGPU;PowerPC;NVPTX;SystemZ;AArch64;ARM;Mips;BPF" \
	-DLLVM_ENABLE_LIBCXX:BOOL=OFF \
	-DLLVM_ENABLE_ZLIB:BOOL=ON \
	-DLLVM_ENABLE_FFI:BOOL=ON \
	-DLLVM_ENABLE_RTTI:BOOL=ON \
%if %{with gold}
	-DLLVM_BINUTILS_INCDIR=%{_includedir} \
%endif
	\
	-DLLVM_BUILD_RUNTIME:BOOL=ON \
	\
	-DLLVM_INCLUDE_TOOLS:BOOL=ON \
	-DLLVM_BUILD_TOOLS:BOOL=ON \
	\
	-DLLVM_INCLUDE_TESTS:BOOL=ON \
	-DLLVM_BUILD_TESTS:BOOL=ON \
	\
	-DLLVM_INCLUDE_EXAMPLES:BOOL=ON \
	-DLLVM_BUILD_EXAMPLES:BOOL=OFF \
	\
	-DLLVM_INCLUDE_UTILS:BOOL=ON \
	-DLLVM_INSTALL_UTILS:BOOL=OFF \
	\
	-DLLVM_INCLUDE_DOCS:BOOL=ON \
	-DLLVM_BUILD_DOCS:BOOL=ON \
	-DLLVM_ENABLE_SPHINX:BOOL=ON \
	-DLLVM_ENABLE_DOXYGEN:BOOL=OFF \
	\
	-DLLVM_BUILD_LLVM_DYLIB:BOOL=ON \
	-DLLVM_DYLIB_EXPORT_ALL:BOOL=ON \
	-DLLVM_LINK_LLVM_DYLIB:BOOL=ON \
	-DLLVM_BUILD_EXTERNAL_COMPILER_RT:BOOL=ON \
	-DLLVM_INSTALL_TOOLCHAIN_ONLY:BOOL=OFF \
	\
	-DSPHINX_WARNINGS_AS_ERRORS=OFF \
	-DLLVM_INSTALL_SPHINX_HTML_DIR=%{_pkgdocdir}/html \
	-DSPHINX_EXECUTABLE=%{_bindir}/sphinx-build-3

make %{?_smp_mflags}

%install
cd _build
make install DESTDIR=%{buildroot}

# Add version suffix to binaries
mkdir -p %{buildroot}/%{_bindir}
for f in `ls %{buildroot}/%{install_bindir}/*`; do
  filename=`basename $f`
  ln -s %{install_bindir}/$filename %{buildroot}/%{_bindir}/$filename%{exec_suffix}
done

# Move header files
mkdir -p %{buildroot}/%{pkg_includedir}
mv %{buildroot}/%{install_includedir}/llvm %{buildroot}/%{pkg_includedir}/
mv %{buildroot}/%{install_includedir}/llvm-c %{buildroot}/%{pkg_includedir}/

# Fix multi-lib
mv %{buildroot}%{_bindir}/llvm-config{%{exec_suffix},%{exec_suffix}-%{__isa_bits}}
%multilib_fix_c_header --file %{pkg_includedir}/llvm/Config/llvm-config.h

# Create ld.so.conf.d entry
mkdir -p %{buildroot}%{_sysconfdir}/ld.so.conf.d
cat >> %{buildroot}%{_sysconfdir}/ld.so.conf.d/%{name}-%{_arch}.conf << EOF
%{pkg_libdir}
EOF

# Add version suffix to man pages and move them to mandir.
mkdir -p %{buildroot}/%{_mandir}/man1
for f in `ls %{buildroot}%{install_prefix}/share/man/man1/*`; do
  filename=`basename $f | cut -f 1 -d '.'`
  mv $f %{buildroot}%{_mandir}/man1/$filename%{exec_suffix}.1
done

# Remove opt-viewer, since this is just a compatibility package.
rm -Rf %{buildroot}%{install_prefix}/share/opt-viewer

%check
cd _build
#make check-all || :

#export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:%{buildroot}/%{_libdir}
test "`%{buildroot}/%{install_bindir}/llvm-config --bindir`" -ef "%{buildroot}/%{pkg_bindir}"
test "`%{buildroot}/%{install_bindir}/llvm-config --libdir`" -ef "%{buildroot}/%{pkg_libdir}"
test "`%{buildroot}/%{install_bindir}/llvm-config --includedir`" -ef "%{buildroot}/%{pkg_includedir}"
test "`%{buildroot}/%{install_bindir}/llvm-config --cmakedir`" -ef "%{buildroot}/%{pkg_libdir}/cmake/llvm"

%post libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%files
%{_bindir}/*
%{pkg_bindir}
%exclude %{_bindir}/llvm-config%{exec_suffix}-%{__isa_bits}
%exclude %{pkg_bindir}/llvm-config
%{_mandir}/man1/*.1.*
%exclude %{_mandir}/man1/llvm-config%{exec_suffix}.1.gz
%license LICENSE.TXT

%files libs
%config(noreplace) %{_sysconfdir}/ld.so.conf.d/%{name}-%{_arch}.conf
%{pkg_libdir}/BugpointPasses.so
%{pkg_libdir}/LLVMHello.so
%if %{with gold}
%{_libdir}/%{name}/lib/LLVMgold.so
%endif
%{pkg_libdir}/libLLVM-%{ver_major_minor}*.so
%{pkg_libdir}/libLTO.so*
%exclude %{pkg_libdir}/libLTO.so
%license LICENSE.TXT

%files devel
%{_bindir}/llvm-config%{exec_suffix}-%{__isa_bits}
%{pkg_bindir}/llvm-config
%{_mandir}/man1/llvm-config%{exec_suffix}.1.gz
%{pkg_includedir}/llvm
%{pkg_includedir}/llvm-c
%{pkg_libdir}/libLTO.so
%{pkg_libdir}/libLLVM.so
%{pkg_libdir}/cmake/llvm

%files static
%{_libdir}/%{name}/lib/*.a

%files doc
%doc %{_pkgdocdir}/html

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 19 2018 Tom Stellard <tstellar@redhat.com> - 5.0.1-7
- Backport r327651 from trunk rhbz#1554349

* Wed Mar 07 2018 Adam Williamson <awilliam@redhat.com> - 5.0.1-6
- Rebuild to fix GCC 8 mis-compilation
  See https://da.gd/YJVwk ("GCC 8 ABI change on x86_64")

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Feb 01 2018 Tom Stellard <tstellar@redhat.com> - 5.0.1-4
- Backport r315279 to fix an issue with rust

* Thu Feb 01 2018 Tom Stellard <tstellar@redhat.com> - 5.0.1-3
- Fix buid with gcc 8

* Sat Jan 27 2018 Tom Stellard <tstellar@redhat.com> - 5.0.1-2
- Work-around LLVMHello.so link failures caused by LD_FLAGS="-Wl,-z,defs"
- https://bugzilla.redhat.com/show_bug.cgi?id=1538318

* Tue Dec 12 2017 Tom Stellard <tstellar@redhat.com> - 5.0.1-1
- 5.0.1 Release

* Tue Dec 12 2017 Tom Stellard <tstellar@redhat.com> - 5.0.0-3
- Update package structure to match llvm4.0.

* Fri Dec 08 2017 Tom Stellard <tstellar@redhat.com> - 5.0.0-2
- Reduce debuginfo size on ARM

* Fri Apr 21 2017 Tom Stellard <tstellar@redhat.com> - 5.0.0-1
- Initial version.

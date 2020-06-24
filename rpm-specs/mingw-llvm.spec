%{?mingw_package_header}

# Disable debuginfo subpackages and debugsource packages for now to use old logic
%undefine _debugsource_packages
%undefine _debuginfo_subpackages

# Override the __debug_install_post argument as this package
# contains both native as well as cross compiled binaries
%global __debug_install_post %%{mingw_debug_install_post}; %{_rpmconfigdir}/find-debuginfo.sh %{?_missing_build_ids_terminate_build:--strict-build-id} %{?_find_debuginfo_opts} "%{_builddir}/%%{?buildsubdir}" %{nil}


%global pkgname llvm
%global ffi_ver 3.1
#global native_llvm_suffix 6.0

Name:          mingw-%{pkgname}
Version:       10.0.0
Release:       1%{?dist}
Summary:       LLVM for MinGW

License:       NCSA
URL:           http://llvm.org
Source0:       https://github.com/llvm/llvm-project/releases/download/llvmorg-%{version}/llvm-%{version}.src.tar.xz

# Don't link llvm tools against both shared library and static libraries from which shared library was created (results in multiple definitions errors)
Patch0:        mingw-llvm_build.patch

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: llvm%{?native_llvm_suffix:%native_llvm_suffix}

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw32-libffi = %{ffi_ver}
BuildRequires: mingw32-zlib

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-gcc-c++
BuildRequires: mingw64-libffi = %{ffi_ver}
BuildRequires: mingw64-zlib


%description
LLVM for MinGW.


%package -n mingw32-%{pkgname}
Summary:       LLVM for MinGW Windows

%description -n mingw32-%{pkgname}
LLVM for MinGW Windows.


%package -n mingw32-%{pkgname}-static
Summary:       LLVM for MinGW Windows - Static libraries
Requires:      mingw32-%{pkgname} = %{version}-%{release}
BuildArch:     noarch

%description -n mingw32-%{pkgname}-static
LLVM for MinGW Windows - Static libraries.

%package -n mingw32-%{pkgname}-tools
Summary:       LLVM for MinGW Windows - Runtime tools
Requires:      mingw32-%{pkgname} = %{version}-%{release}
BuildArch:     noarch

%description -n mingw32-%{pkgname}-tools
LLVM for MinGW Windows - Runtime tools.


%package -n mingw64-%{pkgname}
Summary:       LLVM for MinGW Windows

%description -n mingw64-%{pkgname}
LLVM for MinGW Windows.


%package -n mingw64-%{pkgname}-static
Summary:       LLVM for MinGW Windows - Static libraries
Requires:      mingw64-%{pkgname} = %{version}-%{release}
BuildArch:     noarch

%description -n mingw64-%{pkgname}-static
LLVM for MinGW Windows - Static libraries


%package -n mingw64-%{pkgname}-tools
Summary:       LLVM for MinGW Windows - Runtime tools
Requires:      mingw32-%{pkgname} = %{version}-%{release}
BuildArch:     noarch

%description -n mingw64-%{pkgname}-tools
LLVM for MinGW Windows - Runtime tools.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n %{pkgname}-%{version}.src


%build
# Decrease debuginfo verbosity to reduce memory consumption during final library linking
# Technically only necessary on %%{arm}, but effectively needed everywhere to avoid the build failing due to
#   The following noarch package built differently on different architectures: [...]
mingw32_cflags_="%(echo %mingw32_cflags | sed 's/-g /-g1 /')"
mingw64_cflags_="%(echo %mingw64_cflags | sed 's/-g /-g1 /')"
export MINGW32_CFLAGS="${mingw32_cflags_}"
export MINGW32_CXXFLAGS="${mingw32_cflags_}"
export MINGW64_CFLAGS="${mingw64_cflags_}"
export MINGW64_CXXFLAGS="${mingw64_cflags_}"

# Create toolchain for native build, see cmake/modules/CrossCompile.cmake
# (note that for the native build llvm_create_cross_target_internal is invoked with toolchain = "", hence
# the toolchain file is just .cmake)
cat > cmake/platforms/.cmake <<EOF
SET(CMAKE_SYSTEM_NAME Linux)
SET(CMAKE_CROSSCOMPILING FALSE)

SET(CMAKE_C_COMPILER gcc)
SET(CMAKE_CXX_COMPILER g++)

SET(CMAKE_C_FLAGS "%{optflags}")
SET(CMAKE_CXX_FLAGS "%{optflags}")
SET(CMAKE_EXE_LINKER_FLAGS "%{__global_ldflags}")
EOF

CMAKE_OPTS="
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DBUILD_SHARED_LIBS=OFF \
    -DLLVM_TARGETS_TO_BUILD="X86" \
    -DLLVM_TARGET_ARCH="X86" \
    -DLLVM_INFERRED_HOST_TRIPLE=%{_target} \
    -DLLVM_TABLEGEN=/usr/bin/llvm-tblgen%{?native_llvm_suffix:-%native_llvm_suffix} \
    -DLLVM_ENABLE_LIBCXX=OFF \
    -DLLVM_ENABLE_ZLIB=ON \
    -DLLVM_ENABLE_FFI=ON \
    -DLLVM_ENABLE_RTTI=ON \
    -DLLVM_BUILD_RUNTIME=ON \
    -DLLVM_BUILD_LLVM_DYLIB=ON \
    -DLLVM_LINK_LLVM_DYLIB=ON \
    -DLLVM_BUILD_EXTERNAL_COMPILER_RT=ON \
    -DLLVM_INCLUDE_TESTS=OFF \
    -DLLVM_INCLUDE_DOCS=OFF \
    -DLLVM_INCLUDE_TOOLS=ON \
    -DLLVM_INCLUDE_EXAMPLES=OFF \
    -DLLVM_ENABLE_ASSERTIONS=OFF \
    -DLLVM_INSTALL_TOOLCHAIN_ONLY:BOOL=OFF \
"
mkdir build_win32
pushd build_win32
%mingw32_cmake \
    $CMAKE_OPTS \
    -DLLVM_DEFAULT_TARGET_TRIPLE=%{mingw32_target} \
    -DFFI_INCLUDE_DIR=%{mingw32_libdir}/libffi-%{ffi_ver}/include \
    -DCMAKE_C_FLAGS_RELWITHDEBINFO="${mingw32_cflags_} -DNDEBUG" \
    -DCMAKE_CXX_FLAGS_RELWITHDEBINFO="${mingw32_cflags_} -DNDEBUG"
popd

mkdir build_win64
pushd build_win64
%mingw64_cmake \
    $CMAKE_OPTS \
    -DLLVM_DEFAULT_TARGET_TRIPLE=%{mingw64_target} \
    -DFFI_INCLUDE_DIR=%{mingw64_libdir}/libffi-%{ffi_ver}/include \
    -DCMAKE_C_FLAGS_RELWITHDEBINFO="${mingw64_cflags_} -DNDEBUG" \
    -DCMAKE_CXX_FLAGS_RELWITHDEBINFO="${mingw64_cflags_} -DNDEBUG"
popd

%mingw_make %{?_smp_mflags}


%install
%mingw_make install DESTDIR=%{buildroot}

# Install host llmv-config
install -Dpm 0755 build_win32/NATIVE/bin/llvm-config %{buildroot}%{_prefix}/%{mingw32_target}/bin/llvm-config
install -Dpm 0755 build_win64/NATIVE/bin/llvm-config %{buildroot}%{_prefix}/%{mingw64_target}/bin/llvm-config

# Remove unused files
rm -rf %{buildroot}%{mingw32_datadir}/opt-viewer
rm -rf %{buildroot}%{mingw64_datadir}/opt-viewer


%files -n mingw32-%{pkgname}
%license LICENSE.TXT
%{mingw32_bindir}/llvm-tblgen.exe
%{mingw32_bindir}/LLVM.dll
%{mingw32_bindir}/LTO.dll
%{mingw32_bindir}/Remarks.dll
%{mingw32_includedir}/llvm/
%{mingw32_includedir}/llvm-c/
%{mingw32_libdir}/cmake/llvm/
%{mingw32_libdir}/libLTO.dll.a
%{mingw32_libdir}/libRemarks.dll.a
%{_prefix}/%{mingw32_target}/bin/llvm-config

%files -n mingw32-%{pkgname}-static
%{mingw32_libdir}/libLLVM*.a

%files -n mingw32-%{pkgname}-tools
%exclude %{mingw32_bindir}/llvm-tblgen.exe
%{mingw32_bindir}/*.exe

%files -n mingw64-%{pkgname}
%license LICENSE.TXT
%{mingw64_bindir}/llvm-tblgen.exe
%{mingw64_bindir}/LLVM.dll
%{mingw64_bindir}/LTO.dll
%{mingw64_bindir}/Remarks.dll
%{mingw64_includedir}/llvm/
%{mingw64_includedir}/llvm-c/
%{mingw64_libdir}/cmake/llvm/
%{mingw64_libdir}/libLTO.dll.a
%{mingw64_libdir}/libRemarks.dll.a
%{_prefix}/%{mingw64_target}/bin/llvm-config

%files -n mingw64-%{pkgname}-static
%{mingw64_libdir}/libLLVM*.a

%files -n mingw64-%{pkgname}-tools
%exclude %{mingw64_bindir}/llvm-tblgen.exe
%{mingw64_bindir}/*.exe


%changelog
* Wed Mar 25 2020 Sandro Mani <manisandro@gmail.com> - 10.0.0-1
- Update to 10.0.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 20 2019 Sandro Mani <manisandro@gmail.com> - 9.0.1-1
- Update to 9.0.1

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 9.0.0-2
- Rebuild (Changes/Mingw32GccDwarf2)

* Mon Sep 23 2019 Sandro Mani <manisandro@gmail.com> - 9.0.0-1
- Update to 9.0.0

* Tue Aug 06 2019 Sandro Mani <manisandro@gmail.com> - 8.0.1-1
- Update to 8.0.1

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 23 2019 Sandro Mani <manisandro@gmail.com> - 8.0.0-1
- Update to 8.0.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Dec 25 2018 Sandro Mani <manisandro@gmail.com> - 7.0.1-1
- Update to 7.0.1

* Tue Sep 25 2018 Sandro Mani <manisandro@gmail.com> - 7.0.0-1
- Update to 7.0.0

* Wed Aug 08 2018 Sandro Mani <manisandro@gmail.com> - 6.0.1-1
- Rework spec
- Update to 6.0.1

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jul 23 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 3.0-9
- Do not strip during make install (#1106207)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jul 01 2012 Eric Smith <eric@brouhaha.com> - 3.0-4
- Add patch from upstream to fix call to strerror_s() with too few args.

* Thu May 10 2012 Eric Smith <eric@brouhaha.com> - 3.0-3
- Add patch to force llvm-config to always use PREFIX, rather than
  trying to figure out whether it has been installed.

* Mon May 07 2012 Eric Smith <eric@brouhaha.com> - 3.0-2
- Add OPTIMIZE_OPTION and KEEP_SYMBOLS to make command line to prevent
  symbols from being stripped, in order to get usable debuginfo package.

* Sun May 06 2012 Eric Smith <eric@brouhaha.com> - 3.0-1
- Initial version


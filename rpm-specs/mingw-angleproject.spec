%{?mingw_package_header}

# See also https://github.com/Alexpux/MINGW-packages/tree/master/mingw-w64-angleproject-git

# The reference qt5-qtbase version: qt5 angle modifications from this qt5-qtbase version are used
%global qtrefver 5.9.1

# qt5-qtbase-5.9.1 uses ANGLE chromium/2651:
# https://chromium.googlesource.com/angle/angle/+/chromium/2651
%global commit 8613f4946861a52fd39d3d5c37ca4742d6ef9f55
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global snapshot_rev_short %(echo %snapshot_rev | cut -c1-6)

Name:           mingw-angleproject
Version:        0
Release:        0.26.git%{shortcommit}%{?dist}
Summary:        Almost Native Graphics Layer Engine

License:        BSD
URL:            https://chromium.googlesource.com/angle/angle
BuildArch:      noarch

# commit=%%commit
# shortcommit=$(echo ${commit:0:7})
# git clone https://chromium.googlesource.com/angle/angle
# (cd angle && git archive --format=tar --prefix=angle-$shortcommit/ $commit | gzip > ../angle-$shortcommit.tar.gz)
Source0:        angle-%{shortcommit}.tar.gz
# Additional source files taken from Qt5
Source1:        https://github.com/qt/qtbase/raw/v%{qtrefver}/src/3rdparty/angle/src/libGLESv2/libGLESv2_mingw32.def
Source2:        https://github.com/qt/qtbase/raw/v%{qtrefver}/src/3rdparty/angle/src/libGLESv2/libGLESv2.def
Source3:        https://github.com/qt/qtbase/raw/v%{qtrefver}/src/3rdparty/angle/src/libEGL/libEGL_mingw32.def
Source4:        https://github.com/qt/qtbase/raw/v%{qtrefver}/src/3rdparty/angle/src/libEGL/libEGL.def

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw64-gcc-c++

BuildRequires:  gyp
BuildRequires:  libtool
BuildRequires:  python27

# Patches taken from Qt5
# https://github.com/qt/qtbase/tree/v%%{qtrefver}/src/angle/patches
Patch0:         0001-ANGLE-Improve-Windows-Phone-Support.patch
Patch1:         0002-ANGLE-Dynamically-load-D3D-compiler-from-a-list.patch
Patch2:         0002-ANGLE-Fix-compilation-with-MinGW.patch
Patch3:         0003-ANGLE-Add-support-for-querying-platform-device.patch
Patch4:         0004-ANGLE-Allow-Windows-Phone-to-communicate-swap-region.patch
Patch5:         0005-ANGLE-Fix-compilation-without-d3d11.patch
Patch6:         0006-ANGLE-Fix-Windows-Store-D3D-Trim-and-Level-9-requirements.patch
Patch7:         0007-ANGLE-D3D11-Suppress-keyboard-handling-of-DXGI.patch
Patch8:         0008-ANGLE-Use-pixel-sizes-in-the-XAML-swap-chain.patch
Patch9:         0009-ANGLE-glGetUniform-v-functions-to-work-properly.patch
Patch10:        0010-ANGLE-fixed-usage-of-shared-handles-for-WinRT-WinPho.patch
Patch11:        0012-ANGLE-Fix-initialization-of-zero-sized-window.patch

# Make sure an import library is created and the .def file is used when linking
Patch100:       angle_include-import-library-and-use-def-file.patch

# Fix GLsizeiptr and GLintptr typedefs to match those defined in qopenglext.h
Patch101:       angle_ptrdiff.patch

# Export additional symbols required to build Qt WebKit which uses the shader interface
Patch102:       angle_export-shader-symbols.patch

# Ensure versioned python is invoked
Patch103:       angle_python2.patch


%description
ANGLE is a conformant implementation of the OpenGL ES 2.0 specification that
is hardware‐accelerated via Direct3D. ANGLE v1.0.772 was certified compliant
by passing the ES 2.0.3 conformance tests in October 2011. ANGLE also provides
an implementation of the EGL 1.4 specification.

ANGLE is used as the default WebGL backend for both Google Chrome and
Mozilla Firefox on Windows platforms. Chrome uses ANGLE for all graphics
rendering on Windows, including the accelerated Canvas2D implementation
and the Native Client sandbox environment.

Portions of the ANGLE shader compiler are used as a shader validator and
translator by WebGL implementations across multiple platforms. It is used
on Mac OS X, Linux, and in mobile variants of the browsers. Having one shader
validator helps to ensure that a consistent set of GLSL ES shaders are
accepted across browsers and platforms. The shader translator can be used
to translate shaders to other shading languages, and to optionally apply
shader modifications to work around bugs or quirks in the native graphics
drivers. The translator targets Desktop GLSL, Direct3D HLSL, and even ESSL
for native GLES2 platforms.


%{?mingw_debug_package}


# Win32
%package -n mingw32-angleproject
Summary:        Almost Native Graphics Layer Engine for Win32

%description -n mingw32-angleproject
ANGLE is a conformant implementation of the OpenGL ES 2.0 specification that
is hardware‐accelerated via Direct3D. ANGLE v1.0.772 was certified compliant
by passing the ES 2.0.3 conformance tests in October 2011. ANGLE also provides
an implementation of the EGL 1.4 specification.

ANGLE is used as the default WebGL backend for both Google Chrome and
Mozilla Firefox on Windows platforms. Chrome uses ANGLE for all graphics
rendering on Windows, including the accelerated Canvas2D implementation
and the Native Client sandbox environment.

Portions of the ANGLE shader compiler are used as a shader validator and
translator by WebGL implementations across multiple platforms. It is used
on Mac OS X, Linux, and in mobile variants of the browsers. Having one shader
validator helps to ensure that a consistent set of GLSL ES shaders are
accepted across browsers and platforms. The shader translator can be used
to translate shaders to other shading languages, and to optionally apply
shader modifications to work around bugs or quirks in the native graphics
drivers. The translator targets Desktop GLSL, Direct3D HLSL, and even ESSL
for native GLES2 platforms.


%package -n mingw32-angleproject-static
Summary:       Static version of the mingw32-angleproject library
Requires:      mingw32-angleproject = %{version}-%{release}

%description -n mingw32-angleproject-static
Static version of the mingw32-angleproject library.


# Win64
%package -n mingw64-angleproject
Summary:        Almost Native Graphics Layer Engine for Win64

%description -n mingw64-angleproject
ANGLE is a conformant implementation of the OpenGL ES 2.0 specification that
is hardware‐accelerated via Direct3D. ANGLE v1.0.772 was certified compliant
by passing the ES 2.0.3 conformance tests in October 2011. ANGLE also provides
an implementation of the EGL 1.4 specification.

ANGLE is used as the default WebGL backend for both Google Chrome and
Mozilla Firefox on Windows platforms. Chrome uses ANGLE for all graphics
rendering on Windows, including the accelerated Canvas2D implementation
and the Native Client sandbox environment.

Portions of the ANGLE shader compiler are used as a shader validator and
translator by WebGL implementations across multiple platforms. It is used
on Mac OS X, Linux, and in mobile variants of the browsers. Having one shader
validator helps to ensure that a consistent set of GLSL ES shaders are
accepted across browsers and platforms. The shader translator can be used
to translate shaders to other shading languages, and to optionally apply
shader modifications to work around bugs or quirks in the native graphics
drivers. The translator targets Desktop GLSL, Direct3D HLSL, and even ESSL
for native GLES2 platforms.


%package -n mingw64-angleproject-static
Summary:       Static version of the mingw32-angleproject library
Requires:      mingw64-angleproject = %{version}-%{release}

%description -n mingw64-angleproject-static
Static version of the mingw64-angleproject library.


%prep
%setup -q -n angle-%{shortcommit}
# Install additional .def files
cp -a %{SOURCE1} src/libGLESv2/libGLESv2_mingw32.def
cp -a %{SOURCE2} src/libGLESv2/libGLESv2_mingw64.def
cp -a %{SOURCE3} src/libEGL/libEGL_mingw32.def
cp -a %{SOURCE4} src/libEGL/libEGL_mingw64.def

%patch0 -p4
%patch1 -p4
%patch2 -p4
%patch3 -p4
%patch4 -p4
%patch5 -p4
%patch6 -p4
%patch7 -p4
%patch8 -p4
%patch9 -p4
%patch10 -p4
%patch11 -p4

%patch100 -p1
%patch101 -p1
%patch102 -p1
%patch103 -p1

# Executing .bat scripts on Linux is a no-go so make this a no-op
echo "" > src/copy_compiler_dll.bat
chmod +x src/copy_compiler_dll.bat


%build
# This project uses the gyp build system and various hacks are required to get this project built.
# Therefore the regular Fedora MinGW RPM macros can't be used for this package.

# The gyp build system always uses the environment variable RPM_OPT_FLAGS when it's set
# For MinGW we don't want this, so unset this environment variable
unset RPM_OPT_FLAGS

for target in win32 win64 ; do
    mkdir build_$target
    pushd build_$target
        if [ "$target" = "win32" ] ; then
            export CXX=%{mingw32_cxx}
            export AR=%{mingw32_ar}
        else
            export CXX=%{mingw64_cxx}
            export AR=%{mingw64_ar}
        fi

        gyp -D OS=win -D TARGET=$target -D MSVS_VERSION="" --depth . -I ../build/common.gypi ../src/angle.gyp

        # Parallel build is broken (ar complains <file>.o is not an object because it hasn't finished compiling yet)
        make V=1 CXXFLAGS="-std=c++11 -msse2 -DUNICODE -D_UNICODE -g -I../include -I../src"

        # Also build static libraries (which are needed by the static Qt build)
        # Look in build.log to see what is packed into the respective shared libaries
        ${AR} rcs libGLESv2.a \
            out/Debug/obj.target/src/libGLESv2/entry_points_egl.o \
            out/Debug/obj.target/src/libGLESv2/entry_points_egl_ext.o \
            out/Debug/obj.target/src/libGLESv2/entry_points_gles_2_0.o \
            out/Debug/obj.target/src/libGLESv2/entry_points_gles_2_0_ext.o \
            out/Debug/obj.target/src/libGLESv2/entry_points_gles_3_0.o \
            out/Debug/obj.target/src/libGLESv2/global_state.o \
            out/Debug/obj.target/src/libGLESv2/libGLESv2.o \
            out/Debug/src/libANGLE.a \
            out/Debug/src/libangle_common.a \
            out/Debug/src/libtranslator_static.a \
            out/Debug/src/libtranslator_lib.a \
            out/Debug/src/libpreprocessor.a

        ${AR} rcs libEGL.a \
            out/Debug/obj.target/src/libEGL/libEGL.o \
            out/Debug/src/libANGLE.a \
            out/Debug/src/libtranslator_static.a \
            out/Debug/src/libtranslator_lib.a \
            out/Debug/src/libpreprocessor.a \
            out/Debug/src/libangle_common.a
    popd
done


%install
# The gyp build system doesn't know how to install files
# and gives libraries invalid filenames.. *sigh*
install -Dpm 0755 build_win32/out/Debug/src/libGLESv2.so %{buildroot}%{mingw32_bindir}/libGLESv2.dll
install -Dpm 0755 build_win64/out/Debug/src/libGLESv2.so %{buildroot}%{mingw64_bindir}/libGLESv2.dll

install -Dpm 0755 build_win32/out/Debug/src/libEGL.so %{buildroot}%{mingw32_bindir}/libEGL.dll
install -Dpm 0755 build_win64/out/Debug/src/libEGL.so %{buildroot}%{mingw64_bindir}/libEGL.dll

install -Dpm 0644 build_win32/libGLESv2.dll.a %{buildroot}%{mingw32_libdir}/libGLESv2.dll.a
install -Dpm 0644 build_win32/libGLESv2.a %{buildroot}%{mingw32_libdir}/libGLESv2.a
install -Dpm 0644 build_win64/libGLESv2.dll.a %{buildroot}%{mingw64_libdir}/libGLESv2.dll.a
install -Dpm 0644 build_win64/libGLESv2.a %{buildroot}%{mingw64_libdir}/libGLESv2.a

install -Dpm 0644 build_win32/libEGL.dll.a %{buildroot}%{mingw32_libdir}/libEGL.dll.a
install -Dpm 0644 build_win32/libEGL.a %{buildroot}%{mingw32_libdir}/libEGL.a
install -Dpm 0644 build_win64/libEGL.dll.a %{buildroot}%{mingw64_libdir}/libEGL.dll.a
install -Dpm 0644 build_win64/libEGL.a %{buildroot}%{mingw64_libdir}/libEGL.a

mkdir -p %{buildroot}%{mingw32_includedir}
cp -a include/* %{buildroot}%{mingw32_includedir}/
rm -rf %{buildroot}%{mingw32_includedir}/{platform,export.h}

mkdir -p %{buildroot}%{mingw64_includedir}
cp -a include/* %{buildroot}%{mingw64_includedir}/
rm -rf %{buildroot}%{mingw64_includedir}/{platform,export.h}


%files -n mingw32-angleproject
%license LICENSE
%{mingw32_bindir}/libEGL.dll
%{mingw32_bindir}/libGLESv2.dll
%{mingw32_includedir}/EGL
%{mingw32_includedir}/GLES2
%{mingw32_includedir}/GLES3
%{mingw32_includedir}/GLSLANG
%{mingw32_includedir}/KHR
%{mingw32_includedir}/angle_gl.h
%{mingw32_includedir}/angle_windowsstore.h
%{mingw32_libdir}/libEGL.dll.a
%{mingw32_libdir}/libGLESv2.dll.a

%files -n mingw32-angleproject-static
%{mingw32_libdir}/libEGL.a
%{mingw32_libdir}/libGLESv2.a

%files -n mingw64-angleproject
%license LICENSE
%{mingw64_bindir}/libEGL.dll
%{mingw64_bindir}/libGLESv2.dll
%{mingw64_includedir}/EGL
%{mingw64_includedir}/GLES2
%{mingw64_includedir}/GLES3
%{mingw64_includedir}/GLSLANG
%{mingw64_includedir}/KHR
%{mingw64_includedir}/angle_gl.h
%{mingw64_includedir}/angle_windowsstore.h
%{mingw64_libdir}/libEGL.dll.a
%{mingw64_libdir}/libGLESv2.dll.a

%files -n mingw64-angleproject-static
%{mingw64_libdir}/libEGL.a
%{mingw64_libdir}/libGLESv2.a


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.26.git8613f49
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 0-0.25.git8613f49
- Rebuild (Changes/Mingw32GccDwarf2)
- Add missing BR: python27

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.24.git8613f49
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.23.git8613f49
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.22.git8613f49
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.21.git8613f49
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.20.git8613f49
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 30 2017 Sandro Mani <manisandro@gmail.com> - 0-0.19.git8613f49
- Fix incorrect def files for x64

* Thu Jun 29 2017 Sandro Mani <manisandro@gmail.com> - 0-0.18.git8613f49
- Fix angle_ptrdiff.patch to include stddef.h instead of cstddef

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.17.git8613f49
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 03 2017 Sandro Mani <manisandro@gmail.com> - 0-0.16.git8613f49
- Update to git 8613f49

* Sat May 07 2016 Erik van Pienbroek <epienbro@fedoraproject.org> - 0-0.15.git.30d6c2.20141113
- Fix FTBFS against GCC 6

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.14.git.30d6c2.20141113
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Dec 30 2015 Erik van Pienbroek <epienbro@fedoraproject.org> - 0-0.13.git.30d6c2.20141113
- Use GCC constructors instead of DllMain to avoid conflicts in the static library (RHBZ #1257630)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.12.git.30d6c2.20141113
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Dec 29 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 0-0.11.git.30d6c2.20141113
- Update to 20141113 snapshot (git revision 30d6c2)
- Include all patches which were used by the Qt5 fork
- Reverted some recent commits as they break mingw-qt5-qtwebkit 5.4

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.10.svn2215.20130517
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Feb  4 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 0-0.9.svn2215.20130517
- Automatically LoadLibrary("d3dcompiler_43.dll") when no other D3D compiler is
  already loaded yet. Fixes RHBZ #1057983
- Make sure the libraries are built with debugging symbols
- Rebuild against latest mingw-w64 (fixes Windows XP compatibility, RHBZ #1054481)

* Fri Jan 24 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 0-0.8.svn2215.20130517
- Rebuilt against latest mingw-w64 to fix Windows XP compatibility (RHBZ #1054481)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.7.svn2215.20130517
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat May 18 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 0-0.6.svn2215.20130517
- Export various symbols from the hlsl translator static library in the
  libGLESv2.dll shared library as they are needed by mingw-qt5-qtwebkit.
  The symbols in question are marked as NONAME (hidden)

* Fri May 17 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 0-0.5.svn2215.20130517
- Update to 20130517 snapshot (r2215)

* Thu Apr  4 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 0-0.4.svn1561.20121214
- Added another workaround due to the fact that the gyp
  build system doesn't properly support cross-compilation
  Fixes FTBFS against latest gyp

* Fri Jan 25 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 0-0.3.svn1561.20121214
- Added license
- Resolved various rpmlint warnings
- Prefix the release tag with '0.'

* Mon Dec 24 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 0-0.2.svn1561.20121214
- Added -static subpackages

* Fri Dec 21 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 0-0.1.svn1561.20121214
- Initial release


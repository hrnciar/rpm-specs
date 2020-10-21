%?mingw_package_header

%global name1 boost
Name:           mingw-%{name1}
Version:        1.73.0
Release:        2%{?dist}
Summary:        MinGW Windows port of Boost C++ Libraries

# Replace each . with _ in %%{version}
%global version_enc %{lua:
  local ver = rpm.expand("%{version}")
  ver = ver:gsub("%.", "_")
  print(ver)
}
%global toplev_dirname %{name1}_%{version_enc}

License:        Boost
URL:            http://www.boost.org
Source0:        https://sourceforge.net/projects/%%{name1}/files/%{name1}/%{version}/%{toplev_dirname}.tar.bz2

# https://svn.boost.org/trac/boost/ticket/6150
Patch4:         boost-1.50.0-fix-non-utf8-files.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=828856
# https://bugzilla.redhat.com/show_bug.cgi?id=828857
# https://svn.boost.org/trac/boost/ticket/6701
Patch15:        boost-1.58.0-pool.patch

# https://svn.boost.org/trac/boost/ticket/9038
Patch51:        boost-1.58.0-pool-test_linking.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=1190039
Patch65:        boost-1.73.0-build-optflags.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=1318383
Patch82:        boost-1.66.0-no-rpath.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=1541035
Patch83:        boost-1.73.0-b2-build-flags.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=1818723
Patch86:        boost-1.69-format-allocator.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=1832639
Patch87:        boost-1.69.0-test-cxx20.patch

# https://lists.boost.org/Archives/boost/2020/04/248812.php
Patch88:        boost-1.73.0-cmakedir.patch

# https://github.com/ned14/outcome/issues/223
Patch89:        boost-1.73.0-outcome-assert.patch

# https://github.com/boostorg/beast/pull/1927
Patch90:        boost-1.73.0-beast-coroutines.patch

# https://github.com/boostorg/geometry/issues/721
Patch91:        boost-1.73-geometry-issue721.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=1843105
# https://github.com/boostorg/mpi/pull/119
Patch92:        boost-1.73-mpi-vector-data.patch

# https://svn.boost.org/trac/boost/ticket/7262
Patch1000:      boost-mingw.patch

# https://github.com/boostorg/serialization/pull/42
Patch1002:      boost-1.63.0-codecvtwchar.patch

BuildArch:      noarch

BuildRequires:  file
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-bzip2
BuildRequires:  mingw32-zlib
BuildRequires:  mingw32-expat
BuildRequires:  mingw32-pthreads
BuildRequires:  mingw32-icu
#BuildRequires:  mingw32-win-iconv

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-bzip2
BuildRequires:  mingw64-zlib
BuildRequires:  mingw64-expat
BuildRequires:  mingw64-pthreads
BuildRequires:  mingw64-icu
#BuildRequires:  mingw64-win-iconv

BuildRequires:  perl-interpreter
# These are required by the native package:
#BuildRequires:  mingw32-python
#BuildRequires:  mingw64-python


%description
Boost provides free peer-reviewed portable C++ source libraries.  The
emphasis is on libraries which work well with the C++ Standard
Library, in the hopes of establishing "existing practice" for
extensions and providing reference implementations so that the Boost
libraries are suitable for eventual standardization. (Some of the
libraries have already been proposed for inclusion in the C++
Standards Committee's upcoming C++ Standard Library Technical Report.)

# Win32
%package -n mingw32-boost
Summary:         MinGW Windows Boost C++ library for the win32 target

%description -n mingw32-boost
Boost provides free peer-reviewed portable C++ source libraries.  The
emphasis is on libraries which work well with the C++ Standard
Library, in the hopes of establishing "existing practice" for
extensions and providing reference implementations so that the Boost
libraries are suitable for eventual standardization. (Some of the
libraries have already been proposed for inclusion in the C++
Standards Committee's upcoming C++ Standard Library Technical Report.)

%package -n mingw32-boost-static
Summary:        Static version of the MinGW Windows Boost C++ library
Requires:       mingw32-boost = %{version}-%{release}

%description -n mingw32-boost-static
Static version of the MinGW Windows Boost C++ library.

# Win64
%package -n mingw64-boost
Summary:         MinGW Windows Boost C++ library for the win64 target

%description -n mingw64-boost
Boost provides free peer-reviewed portable C++ source libraries.  The
emphasis is on libraries which work well with the C++ Standard
Library, in the hopes of establishing "existing practice" for
extensions and providing reference implementations so that the Boost
libraries are suitable for eventual standardization. (Some of the
libraries have already been proposed for inclusion in the C++
Standards Committee's upcoming C++ Standard Library Technical Report.)

%package -n mingw64-boost-static
Summary:        Static version of the MinGW Windows Boost C++ library
Requires:       mingw64-boost = %{version}-%{release}

%description -n mingw64-boost-static
Static version of the MinGW Windows Boost C++ library.


%?mingw_debug_package


%prep
%setup -qc
mv %{toplev_dirname} win32

pushd win32
find ./boost -name '*.hpp' -perm /111 | xargs chmod a-x

%patch4 -p1
%patch15 -p0
%patch51 -p1
%patch65 -p1
%patch82 -p1
%patch83 -p1
%patch86 -p1
%patch87 -p2
%patch88 -p1
%patch89 -p1
%patch90 -p1
%patch91 -p1
%patch92 -p1

%patch1000 -p0 -b .mingw
%patch1002 -p1 -b .codecvtwchar
popd

cp -r win32 win64

%build
%if 0%{?mingw_build_win32} == 1
pushd win32
export MINGW32_CXXFLAGS="$MINGW32_CXXFLAGS %{mingw32_cflags}"
export MINGW32_LDFLAGS="$MINGW32_LDFLAGS %{mingw32_ldflags}"
cat >> ./tools/build/src/user-config.jam << "EOF"
import os ;
local MINGW32_CXXFLAGS = [ os.environ MINGW32_CXXFLAGS ] ;
local MINGW32_LDFLAGS = [ os.environ MINGW32_LDFLAGS ] ;

using gcc : : i686-w64-mingw32-g++ : <rc>/usr/bin/i686-w64-mingw32-windres <compileflags>$(MINGW32_CXXFLAGS) <linkflags>$(MINGW32_LDFLAGS) ;
EOF

./bootstrap.sh --with-toolset=gcc --with-icu=%{mingw32_prefix}

echo ============================= build serial ==================
./b2 -d+2 -q %{?_smp_mflags} --layout=tagged \
	--without-mpi --without-graph_parallel --without-python --build-dir=serial \
	variant=release threading=single,multi debug-symbols=on pch=off \
	link=shared,static toolset=gcc target-os=windows address-model=32 stage
popd
%endif
%if 0%{?mingw_build_win64} == 1
pushd win64
export MINGW64_CXXFLAGS="$MINGW64_CXXFLAGS %{mingw64_cflags}"
export MINGW64_LDFLAGS="$MINGW64_LDFLAGS %{mingw64_ldflags}"
cat >> ./tools/build/src/user-config.jam << "EOF"
import os ;
local MINGW64_CXXFLAGS = [ os.environ MINGW64_CXXFLAGS ] ;
local MINGW64_LDFLAGS = [ os.environ MINGW64_LDFLAGS ] ;

using gcc : : x86_64-w64-mingw32-g++ : <rc>/usr/bin/x86_64-w64-mingw32-windres <compileflags>$(MINGW64_CXXFLAGS) <linkflags>$(MINGW64_LDFLAGS) ;
EOF

./bootstrap.sh --with-toolset=gcc --with-icu=%{mingw64_prefix}

echo ============================= build serial ==================
./b2 -d+2 -q %{?_smp_mflags} --layout=tagged \
	--without-mpi --without-graph_parallel --without-python --build-dir=serial \
	variant=release threading=single,multi debug-symbols=on pch=off \
	link=shared,static toolset=gcc target-os=windows address-model=64 stage
popd
%endif

%install
%if 0%{?mingw_build_win32} == 1
pushd win32
echo ============================= install serial ==================
./b2 -d+2 -q %{?_smp_mflags} --layout=tagged \
	--without-mpi --without-graph_parallel --without-python --build-dir=serial \
	--prefix=$RPM_BUILD_ROOT%{mingw32_prefix} \
	--libdir=$RPM_BUILD_ROOT%{mingw32_libdir} \
	variant=release threading=single,multi debug-symbols=on pch=off \
	link=shared,static target-os=windows address-model=32 install
popd
mkdir -p $RPM_BUILD_ROOT%{mingw32_bindir}
mv $RPM_BUILD_ROOT%{mingw32_libdir}/*.dll $RPM_BUILD_ROOT%{mingw32_bindir}
rm -rf $RPM_BUILD_ROOT%{mingw32_libdir}/cmake
%endif
%if 0%{?mingw_build_win64} == 1
pushd win64
echo ============================= install serial ==================
./b2 -d+2 -q %{?_smp_mflags} --layout=tagged \
	--without-mpi --without-graph_parallel --without-python --build-dir=serial \
	--prefix=$RPM_BUILD_ROOT%{mingw64_prefix} \
	--libdir=$RPM_BUILD_ROOT%{mingw64_libdir} \
	variant=release threading=single,multi debug-symbols=on pch=off \
	link=shared,static target-os=windows address-model=64 install
popd
mkdir -p $RPM_BUILD_ROOT%{mingw64_bindir}
mv $RPM_BUILD_ROOT%{mingw64_libdir}/*.dll $RPM_BUILD_ROOT%{mingw64_bindir}
rm -rf $RPM_BUILD_ROOT%{mingw64_libdir}/cmake
%endif

# Win32
%files -n mingw32-boost
%doc win32/LICENSE_1_0.txt
%{mingw32_includedir}/boost
%{mingw32_bindir}/libboost_atomic-mt-x32.dll
%{mingw32_bindir}/libboost_chrono-x32.dll
%{mingw32_bindir}/libboost_chrono-mt-x32.dll
%{mingw32_bindir}/libboost_container-x32.dll
%{mingw32_bindir}/libboost_container-mt-x32.dll
%{mingw32_bindir}/libboost_context-mt-x32.dll
%{mingw32_bindir}/libboost_contract-x32.dll
%{mingw32_bindir}/libboost_contract-mt-x32.dll
%{mingw32_bindir}/libboost_coroutine-x32.dll
%{mingw32_bindir}/libboost_coroutine-mt-x32.dll
%{mingw32_bindir}/libboost_date_time-x32.dll
%{mingw32_bindir}/libboost_date_time-mt-x32.dll
%{mingw32_bindir}/libboost_fiber-mt-x32.dll
%{mingw32_bindir}/libboost_filesystem-x32.dll
%{mingw32_bindir}/libboost_filesystem-mt-x32.dll
%{mingw32_bindir}/libboost_graph-x32.dll
%{mingw32_bindir}/libboost_graph-mt-x32.dll
%{mingw32_bindir}/libboost_iostreams-x32.dll
%{mingw32_bindir}/libboost_iostreams-mt-x32.dll
%{mingw32_bindir}/libboost_locale-mt-x32.dll
%{mingw32_bindir}/libboost_log-x32.dll
%{mingw32_bindir}/libboost_log-mt-x32.dll
%{mingw32_bindir}/libboost_log_setup-x32.dll
%{mingw32_bindir}/libboost_log_setup-mt-x32.dll
%{mingw32_bindir}/libboost_math_c99-x32.dll
%{mingw32_bindir}/libboost_math_c99f-x32.dll
%{mingw32_bindir}/libboost_math_c99f-mt-x32.dll
%{mingw32_bindir}/libboost_math_c99l-x32.dll
%{mingw32_bindir}/libboost_math_c99l-mt-x32.dll
%{mingw32_bindir}/libboost_math_c99-mt-x32.dll
%{mingw32_bindir}/libboost_math_tr1-x32.dll
%{mingw32_bindir}/libboost_math_tr1f-x32.dll
%{mingw32_bindir}/libboost_math_tr1f-mt-x32.dll
%{mingw32_bindir}/libboost_math_tr1l-x32.dll
%{mingw32_bindir}/libboost_math_tr1l-mt-x32.dll
%{mingw32_bindir}/libboost_math_tr1-mt-x32.dll
%{mingw32_bindir}/libboost_nowide-x32.dll
%{mingw32_bindir}/libboost_nowide-mt-x32.dll
%{mingw32_bindir}/libboost_prg_exec_monitor-x32.dll
%{mingw32_bindir}/libboost_prg_exec_monitor-mt-x32.dll
%{mingw32_bindir}/libboost_program_options-x32.dll
%{mingw32_bindir}/libboost_program_options-mt-x32.dll
%{mingw32_bindir}/libboost_random-x32.dll
%{mingw32_bindir}/libboost_random-mt-x32.dll
%{mingw32_bindir}/libboost_regex-x32.dll
%{mingw32_bindir}/libboost_regex-mt-x32.dll
%{mingw32_bindir}/libboost_serialization-x32.dll
%{mingw32_bindir}/libboost_serialization-mt-x32.dll
%{mingw32_bindir}/libboost_stacktrace_basic-x32.dll
%{mingw32_bindir}/libboost_stacktrace_basic-mt-x32.dll
%{mingw32_bindir}/libboost_stacktrace_noop-x32.dll
%{mingw32_bindir}/libboost_stacktrace_noop-mt-x32.dll
%{mingw32_bindir}/libboost_system-x32.dll
%{mingw32_bindir}/libboost_system-mt-x32.dll
%{mingw32_bindir}/libboost_thread-mt-x32.dll
%{mingw32_bindir}/libboost_timer-x32.dll
%{mingw32_bindir}/libboost_timer-mt-x32.dll
%{mingw32_bindir}/libboost_type_erasure-x32.dll
%{mingw32_bindir}/libboost_type_erasure-mt-x32.dll
%{mingw32_bindir}/libboost_unit_test_framework-x32.dll
%{mingw32_bindir}/libboost_unit_test_framework-mt-x32.dll
%{mingw32_bindir}/libboost_wave-x32.dll
%{mingw32_bindir}/libboost_wave-mt-x32.dll
%{mingw32_bindir}/libboost_wserialization-x32.dll
%{mingw32_bindir}/libboost_wserialization-mt-x32.dll
%{mingw32_libdir}/libboost_atomic-mt-x32.dll.a
%{mingw32_libdir}/libboost_chrono-x32.dll.a
%{mingw32_libdir}/libboost_chrono-mt-x32.dll.a
%{mingw32_libdir}/libboost_container-x32.dll.a
%{mingw32_libdir}/libboost_container-mt-x32.dll.a
%{mingw32_libdir}/libboost_context-mt-x32.dll.a
%{mingw32_libdir}/libboost_contract-x32.dll.a
%{mingw32_libdir}/libboost_contract-mt-x32.dll.a
%{mingw32_libdir}/libboost_coroutine-x32.dll.a
%{mingw32_libdir}/libboost_coroutine-mt-x32.dll.a
%{mingw32_libdir}/libboost_date_time-x32.dll.a
%{mingw32_libdir}/libboost_date_time-mt-x32.dll.a
%{mingw32_libdir}/libboost_fiber-mt-x32.dll.a
%{mingw32_libdir}/libboost_filesystem-x32.dll.a
%{mingw32_libdir}/libboost_filesystem-mt-x32.dll.a
%{mingw32_libdir}/libboost_graph-x32.dll.a
%{mingw32_libdir}/libboost_graph-mt-x32.dll.a
%{mingw32_libdir}/libboost_iostreams-x32.dll.a
%{mingw32_libdir}/libboost_iostreams-mt-x32.dll.a
%{mingw32_libdir}/libboost_locale-mt-x32.dll.a
%{mingw32_libdir}/libboost_log-x32.dll.a
%{mingw32_libdir}/libboost_log-mt-x32.dll.a
%{mingw32_libdir}/libboost_log_setup-x32.dll.a
%{mingw32_libdir}/libboost_log_setup-mt-x32.dll.a
%{mingw32_libdir}/libboost_math_c99-x32.dll.a
%{mingw32_libdir}/libboost_math_c99f-x32.dll.a
%{mingw32_libdir}/libboost_math_c99f-mt-x32.dll.a
%{mingw32_libdir}/libboost_math_c99l-x32.dll.a
%{mingw32_libdir}/libboost_math_c99l-mt-x32.dll.a
%{mingw32_libdir}/libboost_math_c99-mt-x32.dll.a
%{mingw32_libdir}/libboost_math_tr1-x32.dll.a
%{mingw32_libdir}/libboost_math_tr1f-x32.dll.a
%{mingw32_libdir}/libboost_math_tr1f-mt-x32.dll.a
%{mingw32_libdir}/libboost_math_tr1l-x32.dll.a
%{mingw32_libdir}/libboost_math_tr1l-mt-x32.dll.a
%{mingw32_libdir}/libboost_math_tr1-mt-x32.dll.a
%{mingw32_libdir}/libboost_nowide-x32.dll.a
%{mingw32_libdir}/libboost_nowide-mt-x32.dll.a
%{mingw32_libdir}/libboost_prg_exec_monitor-x32.dll.a
%{mingw32_libdir}/libboost_prg_exec_monitor-mt-x32.dll.a
%{mingw32_libdir}/libboost_program_options-x32.dll.a
%{mingw32_libdir}/libboost_program_options-mt-x32.dll.a
%{mingw32_libdir}/libboost_random-x32.dll.a
%{mingw32_libdir}/libboost_random-mt-x32.dll.a
%{mingw32_libdir}/libboost_regex-x32.dll.a
%{mingw32_libdir}/libboost_regex-mt-x32.dll.a
%{mingw32_libdir}/libboost_serialization-x32.dll.a
%{mingw32_libdir}/libboost_serialization-mt-x32.dll.a
%{mingw32_libdir}/libboost_stacktrace_basic-x32.dll.a
%{mingw32_libdir}/libboost_stacktrace_basic-mt-x32.dll.a
%{mingw32_libdir}/libboost_stacktrace_noop-x32.dll.a
%{mingw32_libdir}/libboost_stacktrace_noop-mt-x32.dll.a
%{mingw32_libdir}/libboost_system-x32.dll.a
%{mingw32_libdir}/libboost_system-mt-x32.dll.a
%{mingw32_libdir}/libboost_thread-mt-x32.dll.a
%{mingw32_libdir}/libboost_timer-x32.dll.a
%{mingw32_libdir}/libboost_timer-mt-x32.dll.a
%{mingw32_libdir}/libboost_type_erasure-x32.dll.a
%{mingw32_libdir}/libboost_type_erasure-mt-x32.dll.a
%{mingw32_libdir}/libboost_unit_test_framework-x32.dll.a
%{mingw32_libdir}/libboost_unit_test_framework-mt-x32.dll.a
%{mingw32_libdir}/libboost_wave-x32.dll.a
%{mingw32_libdir}/libboost_wave-mt-x32.dll.a
%{mingw32_libdir}/libboost_wserialization-x32.dll.a
%{mingw32_libdir}/libboost_wserialization-mt-x32.dll.a

%files -n mingw32-boost-static
%{mingw32_libdir}/libboost_atomic-mt-x32.a
%{mingw32_libdir}/libboost_chrono-x32.a
%{mingw32_libdir}/libboost_chrono-mt-x32.a
%{mingw32_libdir}/libboost_container-x32.a
%{mingw32_libdir}/libboost_container-mt-x32.a
%{mingw32_libdir}/libboost_context-mt-x32.a
%{mingw32_libdir}/libboost_contract-x32.a
%{mingw32_libdir}/libboost_contract-mt-x32.a
%{mingw32_libdir}/libboost_coroutine-x32.a
%{mingw32_libdir}/libboost_coroutine-mt-x32.a
%{mingw32_libdir}/libboost_date_time-x32.a
%{mingw32_libdir}/libboost_date_time-mt-x32.a
%{mingw32_libdir}/libboost_fiber-mt-x32.a
%{mingw32_libdir}/libboost_filesystem-x32.a
%{mingw32_libdir}/libboost_filesystem-mt-x32.a
%{mingw32_libdir}/libboost_graph-x32.a
%{mingw32_libdir}/libboost_graph-mt-x32.a
%{mingw32_libdir}/libboost_iostreams-x32.a
%{mingw32_libdir}/libboost_iostreams-mt-x32.a
%{mingw32_libdir}/libboost_locale-mt-x32.a
%{mingw32_libdir}/libboost_log-x32.a
%{mingw32_libdir}/libboost_log-mt-x32.a
%{mingw32_libdir}/libboost_log_setup-x32.a
%{mingw32_libdir}/libboost_log_setup-mt-x32.a
%{mingw32_libdir}/libboost_math_c99-x32.a
%{mingw32_libdir}/libboost_math_c99f-x32.a
%{mingw32_libdir}/libboost_math_c99f-mt-x32.a
%{mingw32_libdir}/libboost_math_c99l-x32.a
%{mingw32_libdir}/libboost_math_c99l-mt-x32.a
%{mingw32_libdir}/libboost_math_c99-mt-x32.a
%{mingw32_libdir}/libboost_math_tr1-x32.a
%{mingw32_libdir}/libboost_math_tr1f-x32.a
%{mingw32_libdir}/libboost_math_tr1f-mt-x32.a
%{mingw32_libdir}/libboost_math_tr1l-x32.a
%{mingw32_libdir}/libboost_math_tr1l-mt-x32.a
%{mingw32_libdir}/libboost_math_tr1-mt-x32.a
%{mingw32_libdir}/libboost_nowide-x32.a
%{mingw32_libdir}/libboost_nowide-mt-x32.a
%{mingw32_libdir}/libboost_prg_exec_monitor-x32.a
%{mingw32_libdir}/libboost_prg_exec_monitor-mt-x32.a
%{mingw32_libdir}/libboost_program_options-x32.a
%{mingw32_libdir}/libboost_program_options-mt-x32.a
%{mingw32_libdir}/libboost_random-x32.a
%{mingw32_libdir}/libboost_random-mt-x32.a
%{mingw32_libdir}/libboost_regex-x32.a
%{mingw32_libdir}/libboost_regex-mt-x32.a
%{mingw32_libdir}/libboost_serialization-x32.a
%{mingw32_libdir}/libboost_serialization-mt-x32.a
%{mingw32_libdir}/libboost_stacktrace_basic-x32.a
%{mingw32_libdir}/libboost_stacktrace_basic-mt-x32.a
%{mingw32_libdir}/libboost_stacktrace_noop-x32.a
%{mingw32_libdir}/libboost_stacktrace_noop-mt-x32.a
%{mingw32_libdir}/libboost_system-x32.a
%{mingw32_libdir}/libboost_system-mt-x32.a
%{mingw32_libdir}/libboost_thread-mt-x32.a
%{mingw32_libdir}/libboost_timer-x32.a
%{mingw32_libdir}/libboost_timer-mt-x32.a
%{mingw32_libdir}/libboost_type_erasure-x32.a
%{mingw32_libdir}/libboost_type_erasure-mt-x32.a
%{mingw32_libdir}/libboost_unit_test_framework-x32.a
%{mingw32_libdir}/libboost_unit_test_framework-mt-x32.a
%{mingw32_libdir}/libboost_wave-x32.a
%{mingw32_libdir}/libboost_wave-mt-x32.a
%{mingw32_libdir}/libboost_wserialization-x32.a
%{mingw32_libdir}/libboost_wserialization-mt-x32.a
# static only libraries
%{mingw32_libdir}/libboost_exception-x32.a
%{mingw32_libdir}/libboost_exception-mt-x32.a
%{mingw32_libdir}/libboost_test_exec_monitor-x32.a
%{mingw32_libdir}/libboost_test_exec_monitor-mt-x32.a

# Win64
%files -n mingw64-boost
%doc win64/LICENSE_1_0.txt
%{mingw64_includedir}/boost
%{mingw64_bindir}/libboost_atomic-mt-x64.dll
%{mingw64_bindir}/libboost_chrono-x64.dll
%{mingw64_bindir}/libboost_chrono-mt-x64.dll
%{mingw64_bindir}/libboost_container-x64.dll
%{mingw64_bindir}/libboost_container-mt-x64.dll
%{mingw64_bindir}/libboost_context-mt-x64.dll
%{mingw64_bindir}/libboost_contract-x64.dll
%{mingw64_bindir}/libboost_contract-mt-x64.dll
%{mingw64_bindir}/libboost_coroutine-x64.dll
%{mingw64_bindir}/libboost_coroutine-mt-x64.dll
%{mingw64_bindir}/libboost_date_time-x64.dll
%{mingw64_bindir}/libboost_date_time-mt-x64.dll
%{mingw64_bindir}/libboost_fiber-mt-x64.dll
%{mingw64_bindir}/libboost_filesystem-x64.dll
%{mingw64_bindir}/libboost_filesystem-mt-x64.dll
%{mingw64_bindir}/libboost_graph-x64.dll
%{mingw64_bindir}/libboost_graph-mt-x64.dll
%{mingw64_bindir}/libboost_iostreams-x64.dll
%{mingw64_bindir}/libboost_iostreams-mt-x64.dll
%{mingw64_bindir}/libboost_locale-mt-x64.dll
%{mingw64_bindir}/libboost_log-x64.dll
%{mingw64_bindir}/libboost_log-mt-x64.dll
%{mingw64_bindir}/libboost_log_setup-x64.dll
%{mingw64_bindir}/libboost_log_setup-mt-x64.dll
%{mingw64_bindir}/libboost_math_c99-x64.dll
%{mingw64_bindir}/libboost_math_c99f-x64.dll
%{mingw64_bindir}/libboost_math_c99f-mt-x64.dll
%{mingw64_bindir}/libboost_math_c99l-x64.dll
%{mingw64_bindir}/libboost_math_c99l-mt-x64.dll
%{mingw64_bindir}/libboost_math_c99-mt-x64.dll
%{mingw64_bindir}/libboost_math_tr1-x64.dll
%{mingw64_bindir}/libboost_math_tr1f-x64.dll
%{mingw64_bindir}/libboost_math_tr1f-mt-x64.dll
%{mingw64_bindir}/libboost_math_tr1l-x64.dll
%{mingw64_bindir}/libboost_math_tr1l-mt-x64.dll
%{mingw64_bindir}/libboost_math_tr1-mt-x64.dll
%{mingw64_bindir}/libboost_nowide-x64.dll
%{mingw64_bindir}/libboost_nowide-mt-x64.dll
%{mingw64_bindir}/libboost_prg_exec_monitor-x64.dll
%{mingw64_bindir}/libboost_prg_exec_monitor-mt-x64.dll
%{mingw64_bindir}/libboost_program_options-x64.dll
%{mingw64_bindir}/libboost_program_options-mt-x64.dll
%{mingw64_bindir}/libboost_random-x64.dll
%{mingw64_bindir}/libboost_random-mt-x64.dll
%{mingw64_bindir}/libboost_regex-x64.dll
%{mingw64_bindir}/libboost_regex-mt-x64.dll
%{mingw64_bindir}/libboost_serialization-x64.dll
%{mingw64_bindir}/libboost_serialization-mt-x64.dll
%{mingw64_bindir}/libboost_stacktrace_basic-x64.dll
%{mingw64_bindir}/libboost_stacktrace_basic-mt-x64.dll
%{mingw64_bindir}/libboost_stacktrace_noop-x64.dll
%{mingw64_bindir}/libboost_stacktrace_noop-mt-x64.dll
%{mingw64_bindir}/libboost_system-x64.dll
%{mingw64_bindir}/libboost_system-mt-x64.dll
%{mingw64_bindir}/libboost_thread-mt-x64.dll
%{mingw64_bindir}/libboost_timer-x64.dll
%{mingw64_bindir}/libboost_timer-mt-x64.dll
%{mingw64_bindir}/libboost_type_erasure-x64.dll
%{mingw64_bindir}/libboost_type_erasure-mt-x64.dll
%{mingw64_bindir}/libboost_unit_test_framework-x64.dll
%{mingw64_bindir}/libboost_unit_test_framework-mt-x64.dll
%{mingw64_bindir}/libboost_wave-x64.dll
%{mingw64_bindir}/libboost_wave-mt-x64.dll
%{mingw64_bindir}/libboost_wserialization-x64.dll
%{mingw64_bindir}/libboost_wserialization-mt-x64.dll
%{mingw64_libdir}/libboost_atomic-mt-x64.dll.a
%{mingw64_libdir}/libboost_chrono-x64.dll.a
%{mingw64_libdir}/libboost_chrono-mt-x64.dll.a
%{mingw64_libdir}/libboost_container-x64.dll.a
%{mingw64_libdir}/libboost_container-mt-x64.dll.a
%{mingw64_libdir}/libboost_context-mt-x64.dll.a
%{mingw64_libdir}/libboost_contract-x64.dll.a
%{mingw64_libdir}/libboost_contract-mt-x64.dll.a
%{mingw64_libdir}/libboost_coroutine-x64.dll.a
%{mingw64_libdir}/libboost_coroutine-mt-x64.dll.a
%{mingw64_libdir}/libboost_date_time-x64.dll.a
%{mingw64_libdir}/libboost_date_time-mt-x64.dll.a
%{mingw64_libdir}/libboost_fiber-mt-x64.dll.a
%{mingw64_libdir}/libboost_filesystem-x64.dll.a
%{mingw64_libdir}/libboost_filesystem-mt-x64.dll.a
%{mingw64_libdir}/libboost_graph-x64.dll.a
%{mingw64_libdir}/libboost_graph-mt-x64.dll.a
%{mingw64_libdir}/libboost_iostreams-x64.dll.a
%{mingw64_libdir}/libboost_iostreams-mt-x64.dll.a
%{mingw64_libdir}/libboost_locale-mt-x64.dll.a
%{mingw64_libdir}/libboost_log-x64.dll.a
%{mingw64_libdir}/libboost_log-mt-x64.dll.a
%{mingw64_libdir}/libboost_log_setup-x64.dll.a
%{mingw64_libdir}/libboost_log_setup-mt-x64.dll.a
%{mingw64_libdir}/libboost_math_c99-x64.dll.a
%{mingw64_libdir}/libboost_math_c99f-x64.dll.a
%{mingw64_libdir}/libboost_math_c99f-mt-x64.dll.a
%{mingw64_libdir}/libboost_math_c99l-x64.dll.a
%{mingw64_libdir}/libboost_math_c99l-mt-x64.dll.a
%{mingw64_libdir}/libboost_math_c99-mt-x64.dll.a
%{mingw64_libdir}/libboost_math_tr1-x64.dll.a
%{mingw64_libdir}/libboost_math_tr1f-x64.dll.a
%{mingw64_libdir}/libboost_math_tr1f-mt-x64.dll.a
%{mingw64_libdir}/libboost_math_tr1l-x64.dll.a
%{mingw64_libdir}/libboost_math_tr1l-mt-x64.dll.a
%{mingw64_libdir}/libboost_math_tr1-mt-x64.dll.a
%{mingw64_libdir}/libboost_nowide-x64.dll.a
%{mingw64_libdir}/libboost_nowide-mt-x64.dll.a
%{mingw64_libdir}/libboost_prg_exec_monitor-x64.dll.a
%{mingw64_libdir}/libboost_prg_exec_monitor-mt-x64.dll.a
%{mingw64_libdir}/libboost_program_options-x64.dll.a
%{mingw64_libdir}/libboost_program_options-mt-x64.dll.a
%{mingw64_libdir}/libboost_random-x64.dll.a
%{mingw64_libdir}/libboost_random-mt-x64.dll.a
%{mingw64_libdir}/libboost_regex-x64.dll.a
%{mingw64_libdir}/libboost_regex-mt-x64.dll.a
%{mingw64_libdir}/libboost_serialization-x64.dll.a
%{mingw64_libdir}/libboost_serialization-mt-x64.dll.a
%{mingw64_libdir}/libboost_stacktrace_basic-x64.dll.a
%{mingw64_libdir}/libboost_stacktrace_basic-mt-x64.dll.a
%{mingw64_libdir}/libboost_stacktrace_noop-x64.dll.a
%{mingw64_libdir}/libboost_stacktrace_noop-mt-x64.dll.a
%{mingw64_libdir}/libboost_system-x64.dll.a
%{mingw64_libdir}/libboost_system-mt-x64.dll.a
%{mingw64_libdir}/libboost_thread-mt-x64.dll.a
%{mingw64_libdir}/libboost_timer-x64.dll.a
%{mingw64_libdir}/libboost_timer-mt-x64.dll.a
%{mingw64_libdir}/libboost_type_erasure-x64.dll.a
%{mingw64_libdir}/libboost_type_erasure-mt-x64.dll.a
%{mingw64_libdir}/libboost_unit_test_framework-x64.dll.a
%{mingw64_libdir}/libboost_unit_test_framework-mt-x64.dll.a
%{mingw64_libdir}/libboost_wave-x64.dll.a
%{mingw64_libdir}/libboost_wave-mt-x64.dll.a
%{mingw64_libdir}/libboost_wserialization-x64.dll.a
%{mingw64_libdir}/libboost_wserialization-mt-x64.dll.a

%files -n mingw64-boost-static
%{mingw64_libdir}/libboost_atomic-mt-x64.a
%{mingw64_libdir}/libboost_chrono-x64.a
%{mingw64_libdir}/libboost_chrono-mt-x64.a
%{mingw64_libdir}/libboost_container-x64.a
%{mingw64_libdir}/libboost_container-mt-x64.a
%{mingw64_libdir}/libboost_context-mt-x64.a
%{mingw64_libdir}/libboost_contract-x64.a
%{mingw64_libdir}/libboost_contract-mt-x64.a
%{mingw64_libdir}/libboost_coroutine-x64.a
%{mingw64_libdir}/libboost_coroutine-mt-x64.a
%{mingw64_libdir}/libboost_date_time-x64.a
%{mingw64_libdir}/libboost_date_time-mt-x64.a
%{mingw64_libdir}/libboost_fiber-mt-x64.a
%{mingw64_libdir}/libboost_filesystem-x64.a
%{mingw64_libdir}/libboost_filesystem-mt-x64.a
%{mingw64_libdir}/libboost_graph-x64.a
%{mingw64_libdir}/libboost_graph-mt-x64.a
%{mingw64_libdir}/libboost_iostreams-x64.a
%{mingw64_libdir}/libboost_iostreams-mt-x64.a
%{mingw64_libdir}/libboost_locale-mt-x64.a
%{mingw64_libdir}/libboost_log-x64.a
%{mingw64_libdir}/libboost_log-mt-x64.a
%{mingw64_libdir}/libboost_log_setup-x64.a
%{mingw64_libdir}/libboost_log_setup-mt-x64.a
%{mingw64_libdir}/libboost_math_c99-x64.a
%{mingw64_libdir}/libboost_math_c99f-x64.a
%{mingw64_libdir}/libboost_math_c99f-mt-x64.a
%{mingw64_libdir}/libboost_math_c99l-x64.a
%{mingw64_libdir}/libboost_math_c99l-mt-x64.a
%{mingw64_libdir}/libboost_math_c99-mt-x64.a
%{mingw64_libdir}/libboost_math_tr1-x64.a
%{mingw64_libdir}/libboost_math_tr1f-x64.a
%{mingw64_libdir}/libboost_math_tr1f-mt-x64.a
%{mingw64_libdir}/libboost_math_tr1l-x64.a
%{mingw64_libdir}/libboost_math_tr1l-mt-x64.a
%{mingw64_libdir}/libboost_math_tr1-mt-x64.a
%{mingw64_libdir}/libboost_nowide-x64.a
%{mingw64_libdir}/libboost_nowide-mt-x64.a
%{mingw64_libdir}/libboost_prg_exec_monitor-x64.a
%{mingw64_libdir}/libboost_prg_exec_monitor-mt-x64.a
%{mingw64_libdir}/libboost_program_options-x64.a
%{mingw64_libdir}/libboost_program_options-mt-x64.a
%{mingw64_libdir}/libboost_random-x64.a
%{mingw64_libdir}/libboost_random-mt-x64.a
%{mingw64_libdir}/libboost_regex-x64.a
%{mingw64_libdir}/libboost_regex-mt-x64.a
%{mingw64_libdir}/libboost_serialization-x64.a
%{mingw64_libdir}/libboost_serialization-mt-x64.a
%{mingw64_libdir}/libboost_stacktrace_basic-x64.a
%{mingw64_libdir}/libboost_stacktrace_basic-mt-x64.a
%{mingw64_libdir}/libboost_stacktrace_noop-x64.a
%{mingw64_libdir}/libboost_stacktrace_noop-mt-x64.a
%{mingw64_libdir}/libboost_system-x64.a
%{mingw64_libdir}/libboost_system-mt-x64.a
%{mingw64_libdir}/libboost_thread-mt-x64.a
%{mingw64_libdir}/libboost_timer-x64.a
%{mingw64_libdir}/libboost_timer-mt-x64.a
%{mingw64_libdir}/libboost_type_erasure-x64.a
%{mingw64_libdir}/libboost_type_erasure-mt-x64.a
%{mingw64_libdir}/libboost_unit_test_framework-x64.a
%{mingw64_libdir}/libboost_unit_test_framework-mt-x64.a
%{mingw64_libdir}/libboost_wave-x64.a
%{mingw64_libdir}/libboost_wave-mt-x64.a
%{mingw64_libdir}/libboost_wserialization-x64.a
%{mingw64_libdir}/libboost_wserialization-mt-x64.a
# static only libraries
%{mingw64_libdir}/libboost_exception-x64.a
%{mingw64_libdir}/libboost_exception-mt-x64.a
%{mingw64_libdir}/libboost_test_exec_monitor-x64.a
%{mingw64_libdir}/libboost_test_exec_monitor-mt-x64.a

%changelog
* Tue Aug 04 2020 Thomas Sailer <t.sailer@alumni.ethz.ch> - 1.73.0-2
- fix compile flags typo

* Tue Aug 04 2020 Thomas Sailer <t.sailer@alumni.ethz.ch> - 1.73.0-1
- update to 1.73.0

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.69.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.69.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 02 2020 Thomas Sailer <t.sailer@alumni.ethz.ch> - 1.69.0-1
- update to 1.69.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.66.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 1.66.0-5
- Rebuild (Changes/Mingw32GccDwarf2)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.66.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.66.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 20 2018 Thomas Sailer <t.sailer@alumni.ethz.ch> - 1.66.0-2
- rebuilt
- add gcc BR

* Tue Mar 20 2018 Thomas Sailer <t.sailer@alumni.ethz.ch> - 1.66.0-1
- update to 1.66.0

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.64.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Sep 13 2017 Thomas Sailer <t.sailer@alumni.ethz.ch> - 1.64.0-1
- update to 1.64.0

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.63.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Mar 01 2017 Thomas Sailer <t.sailer@alumni.ethz.ch> - 1.63.0-1
- update to 1.63.0

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.60.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Feb 02 2016 Thomas Sailer <t.sailer@alumni.ethz.ch> - 1.60.0-1
- update to 1.60.0

* Wed Sep 02 2015 Thomas Sailer <t.sailer@alumni.ethz.ch> - 1.59.0-1
- update to 1.59.0

* Wed Sep 02 2015 Thomas Sailer <t.sailer@alumni.ethz.ch> - 1.58.0-1
- update to 1.58.0

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.57.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May  4 2015 Thomas Sailer <t.sailer@alumni.ethz.ch> - 1.57.0-1
- update to 1.57.0

* Mon Jun 30 2014 Thomas Sailer <t.sailer@alumni.ethz.ch> - 1.55.0-1
- update to 1.55.0

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.54.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Jul 30 2013 Thomas Sailer <t.sailer@alumni.ethz.ch> - 1.54.0-1
- update to 1.54.0

* Sat Jul 20 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.53.0-2
- Fix the build when the native libicu-devel is installed
- Fix FTBFS on recent mingw-w64 and also use intrinsics based
  versions of the Interlocked symbols which are better optimized

* Sun Mar  3 2013 Thomas Sailer <t.sailer@alumni.ethz.ch> - 1.53.0-1
- update to 1.53.0

* Sun Jan 27 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.50.0-2
- Rebuild against mingw-gcc 4.8 (win64 uses SEH exceptions now)

* Tue Dec  4 2012 Thomas Sailer <t.sailer@alumni.ethz.ch> - 1.50.0-1
- update to 1.50.0
- revert to bjam build

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.48.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 15 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.48.0-9
- Improved summary (RHBZ #831849)

* Wed Apr 25 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.48.0-8
- Rebuild against mingw-bzip2

* Fri Mar 16 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.48.0-7
- Added win64 support (contributed by Jay Higley)

* Wed Mar 07 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.48.0-6
- Renamed the source package to mingw-boost (RHBZ #800845)
- Fixed source URL
- Use mingw macros without leading underscore
- Dropped unneeded RPM tags

* Sat Mar  3 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.48.0-5
- Fix compilation failure when including interlocked.hpp in c++11 mode (RHBZ #799332)

* Tue Feb 28 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.48.0-4
- Rebuild against the mingw-w64 toolchain

* Fri Feb 10 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.48.0-3
- Don't provide the cmake files any more as they are broken and cmake
  itself already provides its own boost detection mechanism.
  Should fix detection of boost by mingw32-qpid-cpp. RHBZ #597020, RHBZ #789399
- Added patch which makes boost install dll's to %%{_mingw32_bindir}
  instead of %%{_mingw32_libdir}. The hack in the %%install section
  to manually move the dll's is dropped now

* Sat Jan 14 2012 Thomas Sailer <t.sailer@alumni.ethz.ch> - 1.48.0-2
- update cmakeify patch

* Sat Jan 14 2012 Thomas Sailer <t.sailer@alumni.ethz.ch> - 1.48.0-1
- update to 1.48.0

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.47.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Sep  2 2011 Thomas Sailer <t.sailer@alumni.ethz.ch> - 1.47.0-1
- update to 1.47.0

* Tue Jun 28 2011 Kalev Lember <kalev@smartlink.ee> - 1.46.1-2
- Rebuilt for mingw32-gcc 4.6

* Tue Jun 21 2011 Thomas Sailer <t.sailer@alumni.ethz.ch> - 1.46.1-1
- update to 1.46.1

* Sat May 21 2011 Kalev Lember <kalev@smartlink.ee> - 1.46.0-0.3.beta1
- Own the _mingw32_datadir/cmake/boost/ directory

* Fri Apr 22 2011 Kalev Lember <kalev@smartlink.ee> - 1.46.0-0.2.beta1
- Rebuilt for pseudo-reloc version mismatch (#698827)

* Wed Feb  9 2011 Thomas Sailer <t.sailer@alumni.ethz.ch> - 1.46.0-0.1.beta1
- update to 1.46.0-beta1

* Thu Nov 18 2010 Thomas Sailer <t.sailer@alumni.ethz.ch> - 1.44.0-1
- update to 1.44.0

* Thu Jun  3 2010 Thomas Sailer <t.sailer@alumni.ethz.ch> - 1.41.0-2
- update to gcc 4.5

* Wed Jan 20 2010 Thomas Sailer <t.sailer@alumni.ethz.ch> - 1.41.0-1
- update to 1.41.0

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.39.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 22 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 1.39.0-2
- add debuginfo packages

* Thu Jun 18 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 1.39.0-1
- update to 1.39.0

* Thu May 28 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 1.37.0-4
- use boost buildsystem to build DLLs

* Wed May 27 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 1.37.0-3
- use mingw32 ar

* Tue May 26 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 1.37.0-2
- fix %%defattr
- fix description of static package
- add comments that detail the failures linking the test framework / exec monitor DLL's

* Sun May 24 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 1.37.0-1
- update to 1.37.0
- actually tell the build system about the target os
- build also boost DLL's that depend on other boost DLL's

* Fri Jan 23 2009 Richard W.M. Jones <rjones@redhat.com> - 1.34.1-4
- Include license file.

* Fri Jan 23 2009 Richard W.M. Jones <rjones@redhat.com> - 1.34.1-3
- Use _smp_mflags.

* Fri Oct 24 2008 Richard W.M. Jones <rjones@redhat.com> - 1.34.1-2
- Initial RPM release.

%bcond_without check
%undefine __cmake_in_source_build

Summary:       Compiler and toolchain infrastructure library for WebAssembly
Name:          binaryen
Version:       97
Release:       1%{?dist}

URL:           https://github.com/WebAssembly/binaryen
Source0:       %{url}/archive/version_%{version}/%{name}-version_%{version}.tar.gz
# https://github.com/WebAssembly/binaryen/issues/2999
Patch1:        %{name}-95-lib-tests.patch
License:       ASL 2.0

# tests fail on big-endian
# https://github.com/WebAssembly/binaryen/issues/2983
ExcludeArch:   ppc64 s390x
BuildRequires: cmake3
BuildRequires: gcc-c++
%if %{with check}
BuildRequires: nodejs
%endif

# filter out internal shared library
%global __provides_exclude_from ^%{_libdir}/%{name}/.*$
%global __requires_exclude ^libbinaryen\\.so.*$

%description
Binaryen is a compiler and toolchain infrastructure library for WebAssembly,
written in C++. It aims to make compiling to WebAssembly easy, fast, and
effective:

* Easy: Binaryen has a simple C API in a single header, and can also be used
  from JavaScript. It accepts input in WebAssembly-like form but also accepts
  a general control flow graph for compilers that prefer that.

* Fast: Binaryen's internal IR uses compact data structures and is designed for
  completely parallel codegen and optimization, using all available CPU cores.
  Binaryen's IR also compiles down to WebAssembly extremely easily and quickly
  because it is essentially a subset of WebAssembly.

* Effective: Binaryen's optimizer has many passes that can improve code very
  significantly (e.g. local coloring to coalesce local variables; dead code
  elimination; precomputing expressions when possible at compile time; etc.).
  These optimizations aim to make Binaryen powerful enough to be used as a
  compiler backend by itself. One specific area of focus is on
  WebAssembly-specific optimizations (that general-purpose compilers might not
  do), which you can think of as wasm minification , similar to minification for
  JavaScript, CSS, etc., all of which are language-specific (an example of such
  an optimization is block return value generation in SimplifyLocals).

%prep
%setup -q -n %{name}-version_%{version}
%patch1 -p1

%build
%cmake3 \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DCMAKE_INSTALL_LIBDIR=%{_libdir}/%{name} \
    -DCMAKE_INSTALL_RPATH=\\\$ORIGIN/../%{_lib}/%{name} \
    -DENABLE_WERROR=OFF \

%cmake3_build

%install
%cmake3_install

%if %{with check}
%check
./check.py \
    --binaryen-bin %{buildroot}%{_bindir} \
    --binaryen-lib %{buildroot}%{_libdir}/%{name} \

%endif

%files
%license LICENSE
%doc README.md
%{_bindir}/wasm-as
%{_bindir}/wasm-ctor-eval
%{_bindir}/wasm-dis
%{_bindir}/wasm-emscripten-finalize
%{_bindir}/wasm-metadce
%{_bindir}/wasm-opt
%{_bindir}/wasm-reduce
%{_bindir}/wasm-shell
%{_bindir}/wasm2js
%{_includedir}/binaryen-c.h
%{_libdir}/%{name}/libbinaryen.so

%changelog
* Wed Oct 07 2020 Dominik Mierzejewski <rpm@greysector.net> 97-1
- update to 97 (#1880087)

* Tue Aug 18 2020 Dominik Mierzejewski <rpm@greysector.net> 96-1
- update to 96
- drop obsolete patch

* Wed Jul 29 2020 Dominik Mierzejewski <rpm@greysector.net> 95-3
- fix build on F31/F32

* Tue Jul 28 2020 Dominik Mierzejewski <rpm@greysector.net> 95-2
- use built binaries in tests
- fix (r)paths to internal shared library
- filter internal shared library from Provides/Requires

* Tue Jul 21 2020 Dominik Mierzejewski <rpm@greysector.net> 95-1
- initial build

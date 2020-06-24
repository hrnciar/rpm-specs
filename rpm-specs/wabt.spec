%bcond_without check
%global ts_commit 0e7987efba9c13c5a65c2c14a8f2f04b3820e8d3
%global ts_shortcommit %(c=%{ts_commit}; echo ${c:0:7})
%global wc_commit d9a80099d496b5cdba6f3fe8fc77586e0e505ddc
%global wc_shortcommit %(c=%{wc_commit}; echo ${c:0:7})

Summary: The WebAssembly Binary Toolkit
Name: wabt
Version: 1.0.15
Release: 1%{?dist}
URL: https://github.com/WebAssembly/wabt
Source0: https://github.com/WebAssembly/wabt/archive/%{version}/%{name}-%{version}.tar.gz
Source1: https://github.com/WebAssembly/testsuite/archive/%{ts_commit}/%{name}-testsuite-%{ts_shortcommit}.tar.gz
Source2: https://github.com/WebAssembly/wasm-c-api/archive/%{wc_commit}/%{name}-wasm-c-api-%{wc_shortcommit}.tar.gz
# hard-code version instead of using git for release tarball
Patch0: wabt-nogit.patch
License: ASL 2.0
BuildRequires: cmake
BuildRequires: gcc-c++
%if %{with check}
BuildRequires: gtest-devel
BuildRequires: python3-ply
%endif
# wasm.h from https://github.com/WebAssembly/wasm-c-api/ is used for build
Provides: bundled(wasm-c-api) = %{wc_commit}

%description
WABT (we pronounce it "wabbit") is a suite of tools for WebAssembly. These tools
are intended for use in (or for development of) toolchains or other systems that
want to manipulate WebAssembly files. Unlike the WebAssembly spec interpreter
(which is written to be as simple, declarative and "speccy" as possible), they
are written in C/C++ and designed for easier integration into other systems.
Unlike Binaryen these tools do not aim to provide an optimization platform or a
higher-level compiler target; instead they aim for full fidelity and compliance
with the spec (e.g. 1:1 round-trips with no changes to instructions).

%prep
%setup -q
%patch0 -p1
%if %{with check}
rmdir third_party/{testsuite,wasm-c-api}
tar xzf %{S:1} -C third_party
mv third_party/testsuite{-%{ts_commit},}
tar xzf %{S:2} -C third_party
mv third_party/wasm-c-api{-%{wc_commit},}
pushd test
# https://github.com/WebAssembly/wabt/issues/1044
# https://github.com/WebAssembly/wabt/issues/1045
# https://github.com/WebAssembly/wabt/issues/1063
pushd wasm2c/spec
# https://github.com/WebAssembly/wabt/issues/1365
%ifarch armv7hl
rm skip-stack-guard-page.txt
%endif
%ifarch i686 ppc64 ppc64le
rm conversions.txt
%endif
%ifarch i686
rm \
  float_exprs.txt\
  float_literals.txt\
  float_memory.txt\
  float_misc.txt\

%endif
%ifarch ppc64
rm f{32,64}.txt
%endif
popd
pushd spec
%ifarch i686
rm \
  float_exprs.txt\
  float_misc.txt\
  local_tee.txt\
  simd/simd_f32x4_arith.txt\
  simd/simd_f64x2_arith.txt\

%endif
%ifarch ppc64 ppc64le
rm {,nontrapping-float-to-int-conversions/}conversions.txt
%endif
popd
popd
%endif

%build
# work around https://github.com/WebAssembly/wabt/issues/988
mkdir -p build
cd build
%cmake -DUSE_SYSTEM_GTEST=ON ..
%make_build

%install
cd build
%make_install

%if %{with check}
# ~250 tests fail on big-endian arches
%ifnarch ppc64 s390x
%check
test/run-tests.py -v --timeout=40 %{?_smp_mflags}
%endif
%endif

%files
%license LICENSE
%doc README.md
%{_bindir}/spectest-interp
%{_bindir}/wasm-decompile
%{_bindir}/wasm-interp
%{_bindir}/wasm-objdump
%{_bindir}/wasm-opcodecnt
%{_bindir}/wasm-strip
%{_bindir}/wasm-validate
%{_bindir}/wasm2c
%{_bindir}/wasm2wat
%{_bindir}/wast2json
%{_bindir}/wat-desugar
%{_bindir}/wat2wasm
%{_mandir}/man1/spectest-interp.1*
%{_mandir}/man1/wasm-decompile.1*
%{_mandir}/man1/wasm-interp.1*
%{_mandir}/man1/wasm-objdump.1*
%{_mandir}/man1/wasm-opcodecnt.1*
%{_mandir}/man1/wasm-strip.1*
%{_mandir}/man1/wasm-validate.1*
%{_mandir}/man1/wasm2c.1*
%{_mandir}/man1/wasm2wat.1*
%{_mandir}/man1/wast2json.1*
%{_mandir}/man1/wat-desugar.1*
%{_mandir}/man1/wat2wasm.1*

%changelog
* Wed May 06 2020 Dominik Mierzejewski <rpm@greysector.net> 1.0.15-1
- update to 1.0.15 (#1832317)
- pathfix.py no longer required, upstream moved to python3-only
- skip new failing tests in i686 and ppc64le (reported upstream)

* Fri Mar 20 2020 Dominik Mierzejewski <rpm@greysector.net> 1.0.13-1
- update to 1.0.13 (#1792557)
- drop obsolete patch and work-arounds
- bundle wasm-c-api (only wasm.h used for build)
- double test timeout again to prevent failures on armv7hl

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Sep 28 2019 Dominik Mierzejewski <rpm@greysector.net> 1.0.12-1
- update to 1.0.12 (#1755644)
- drop obsolete patch
- disable regress/regress-30.txt until fixed for python3
- fix running test/wasm2c/spec tests under python3

* Thu Sep 12 2019 Dominik Mierzejewski <rpm@greysector.net> 1.0.11-1
- update to 1.0.11
- drop obsolete patches

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 15 2019 Dominik Mierzejewski <rpm@greysector.net> 1.0.10-2
- backport some fixes for test failures from upstream git
- run tests in parallel and double timeout to prevent failures on armv7hl

* Thu Mar 14 2019 Dominik Mierzejewski <rpm@greysector.net> 1.0.10-1
- initial build

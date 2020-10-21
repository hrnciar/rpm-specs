%undefine __cmake_in_source_build
%bcond_without check
%global ts_commit d2163dace09d647bccf34b9b82a6f05a3b23cf29
%global ts_shortcommit %(c=%{ts_commit}; echo ${c:0:7})
%global wc_commit d9a80099d496b5cdba6f3fe8fc77586e0e505ddc
%global wc_shortcommit %(c=%{wc_commit}; echo ${c:0:7})

Summary: The WebAssembly Binary Toolkit
Name: wabt
Version: 1.0.19
Release: 1%{?dist}
URL: https://github.com/WebAssembly/wabt
Source0: https://github.com/WebAssembly/wabt/archive/%{version}/%{name}-%{version}.tar.gz
Source1: https://github.com/WebAssembly/testsuite/archive/%{ts_commit}/%{name}-testsuite-%{ts_shortcommit}.tar.gz
Source2: https://github.com/WebAssembly/wasm-c-api/archive/%{wc_commit}/%{name}-wasm-c-api-%{wc_shortcommit}.tar.gz
# hard-code version instead of using git for release tarball
Patch0: wabt-nogit.patch
License: ASL 2.0
BuildRequires: cmake3
BuildRequires: gcc-c++
%if %{with check}
BuildRequires: gtest-devel
BuildRequires: python%{python3_pkgversion}-ply
%endif
# wasm.h from https://github.com/WebAssembly/wasm-c-api/ is used for build
Provides: bundled(wasm-c-api) = %{wc_commit}
# too many test failures on big-endian
# https://github.com/WebAssembly/wabt/issues/1063
ExcludeArch: ppc64 s390x

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
# https://github.com/WebAssembly/wabt/issues/1365
%ifarch armv7hl
rm wasm2c/spec/skip-stack-guard-page.txt
%endif
# https://github.com/WebAssembly/wabt/issues/1044
%ifarch i686
rm spec/float_exprs.txt
rm spec/float_misc.txt
rm spec/local_tee.txt
rm spec/simd/simd_f32x4_arith.txt
rm spec/simd/simd_f64x2_arith.txt
rm wasm2c/spec/float_literals.txt
rm wasm2c/spec/float_memory.txt
rm wasm2c/spec/float_misc.txt
rm wasm2c/spec/float_exprs.txt
%endif
# https://github.com/WebAssembly/wabt/issues/1045
%ifarch ppc64le
rm spec/conversions.txt
rm spec/nontrapping-float-to-int-conversions/conversions.txt
rm wasm2c/spec/conversions.txt
%endif
popd
%endif

%build
%cmake3 -DUSE_SYSTEM_GTEST=ON
%cmake3_build

%install
%cmake3_install

%if %{with check}
%check
test/run-tests.py -v --bindir %{_vpath_builddir} --timeout=40 %{?_smp_mflags}
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
* Mon Aug 17 2020 Dominik Mierzejewski <rpm@greysector.net> 1.0.19-1
- update to 1.0.19 (#1838384)
- drop obsolete patches
- adapt to https://www.fedoraproject.org/wiki/Changes/CMake_to_do_out-of-source_builds

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 24 2020 Jeff Law <law@redhat.com> 1.0.17-2
- Use __cmake_in_source_build

* Tue Jul 14 2020 Dominik Mierzejewski <rpm@greysector.net> 1.0.17-1
- update to 1.0.17 (#1838384)
- backport a fix for 32-bit arches
- stop pretending it works on big-endian
- use names and macros portable across Fedora and EPEL

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

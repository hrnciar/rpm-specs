%global major 78

# LTO - Enable in Release builds, but consider disabling for development as it increases compile time
%global build_with_lto    1

# Require tests to pass?
%global require_tests     1

%if 0%{?build_with_lto}
# LTO is default since F33 and F32 package is backported as is, so no LTO there
%else
%define _lto_cflags %{nil}
%endif

# Require libatomic for ppc
%ifarch ppc
%global system_libatomic 1
%endif

# Big endian platforms
%ifarch ppc ppc64 s390 s390x
%global big_endian 1
%endif

Name:           mozjs%{major}
Version:        78.4.0
Release:        1%{?dist}
Summary:        SpiderMonkey JavaScript library

License:        MPLv2.0 and MPLv1.1 and BSD and GPLv2+ and GPLv3+ and LGPLv2+ and AFL and ASL 2.0
URL:            https://developer.mozilla.org/en-US/docs/Mozilla/Projects/SpiderMonkey
Source0:        https://ftp.mozilla.org/pub/firefox/releases/%{version}esr/source/firefox-%{version}esr.source.tar.xz

# Patches from mozjs68, rebased for mozjs78:
Patch01:        fix-soname.patch
Patch02:        copy-headers.patch
Patch03:        tests-increase-timeout.patch
Patch09:        icu_sources_data.py-Decouple-from-Mozilla-build-system.patch
Patch10:        icu_sources_data-Write-command-output-to-our-stderr.patch

# Build fixes - https://hg.mozilla.org/mozilla-central/rev/ca36a6c4f8a4a0ddaa033fdbe20836d87bbfb873
Patch12:        emitter.patch

# Build fixes
Patch14:        init_patch.patch
# TODO: Check with mozilla for cause of these fails and re-enable spidermonkey compile time checks if needed
Patch15:        spidermonkey_checks_disable.patch

# armv7 fixes
Patch17:        armv7_disable_WASM_EMULATE_ARM_UNALIGNED_FP_ACCESS.patch

# s390x/ppc64 fixes, TODO: file bug report upstream?
Patch18:        spidermonkey_style_check_disable_s390x.patch
Patch19:        0001-Skip-failing-tests-on-ppc64-and-s390x.patch

BuildRequires:  autoconf213
BuildRequires:  cargo
BuildRequires:  clang-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  nasm
BuildRequires:  llvm
BuildRequires:  llvm-devel
BuildRequires:  icu
BuildRequires:  rust
BuildRequires:  perl-devel
BuildRequires:  pkgconfig(libffi)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-six
BuildRequires:  readline-devel
BuildRequires:  zip
%if 0%{?system_libatomic}
BuildRequires:  libatomic
%endif

%description
SpiderMonkey is the code-name for Mozilla Firefox's C++ implementation of
JavaScript. It is intended to be embedded in other applications
that provide host environments for JavaScript.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q -n firefox-%{version}/js/src

pushd ../..
%patch01 -p1
%patch02 -p1
%patch03 -p1
%patch09 -p1
%patch10 -p1

%patch12 -p1

%patch14 -p1
%patch15 -p1

%ifarch armv7hl
# Disable WASM_EMULATE_ARM_UNALIGNED_FP_ACCESS as it causes the compilation to fail
# https://bugzilla.mozilla.org/show_bug.cgi?id=1526653
%patch17 -p1
%endif

%ifarch s390x
%patch18 -p1
%endif

# Fixes for ppc64 and s390x, there is no need to keep it in ifarch here since mozilla tests support ifarch conditions
%patch19 -p1

# Copy out the LICENSE file
cp LICENSE js/src/
popd

# Remove zlib directory (to be sure using system version)
rm -rf ../../modules/zlib

%build
# Prefer GCC for now
export CC=gcc
export CXX=g++

# Workaround
# error: options `-C embed-bitcode=no` and `-C lto` are incompatible
# error: could not compile `jsrust`.
# https://github.com/japaric/cargo-call-stack/issues/25
export RUSTFLAGS="-C embed-bitcode"

%if 0%{?build_with_lto}
# https://github.com/ptomato/mozjs/commit/36bb7982b41e0ef9a65f7174252ab996cd6777bd
export CARGO_PROFILE_RELEASE_LTO=true
%endif

export CFLAGS="%{optflags}"
export CXXFLAGS="$CFLAGS"
export LINKFLAGS="%{?__global_ldflags}"
export PYTHON="%{__python3}"

autoconf-2.13
%configure \
  --without-system-icu \
  --with-system-zlib \
  --disable-tests \
  --disable-strip \
  --with-intl-api \
  --enable-readline \
  --enable-shared-js \
  --disable-optimize \
  --enable-pie \
  --disable-jemalloc

%if 0%{?big_endian}
echo "Generate big endian version of config/external/icu/data/icud67l.dat"
pushd ../..
  icupkg -tb config/external/icu/data/icudt67l.dat config/external/icu/data/icudt67b.dat
  rm -f config/external/icu/data/icudt*l.dat
popd
%endif

%make_build

%install
%make_install

# Fix permissions
chmod -x %{buildroot}%{_libdir}/pkgconfig/*.pc

# Avoid multilib conflicts
case `uname -i` in
  i386 | ppc | s390 | sparc )
    wordsize="32"
    ;;
  x86_64 | ppc64 | s390x | sparc64 )
    wordsize="64"
    ;;
  *)
    wordsize=""
    ;;
esac

if test -n "$wordsize"
then
  mv %{buildroot}%{_includedir}/mozjs-%{major}/js-config.h \
     %{buildroot}%{_includedir}/mozjs-%{major}/js-config-$wordsize.h

  cat >%{buildroot}%{_includedir}/mozjs-%{major}/js-config.h <<EOF
#ifndef JS_CONFIG_H_MULTILIB
#define JS_CONFIG_H_MULTILIB

#include <bits/wordsize.h>

#if __WORDSIZE == 32
# include "js-config-32.h"
#elif __WORDSIZE == 64
# include "js-config-64.h"
#else
# error "unexpected value for __WORDSIZE macro"
#endif

#endif
EOF

fi

# Remove unneeded files
rm %{buildroot}%{_bindir}/js%{major}-config
rm %{buildroot}%{_libdir}/libjs_static.ajs

# Rename library and create symlinks, following fix-soname.patch
mv %{buildroot}%{_libdir}/libmozjs-%{major}.so \
   %{buildroot}%{_libdir}/libmozjs-%{major}.so.0.0.0
ln -s libmozjs-%{major}.so.0.0.0 %{buildroot}%{_libdir}/libmozjs-%{major}.so.0
ln -s libmozjs-%{major}.so.0 %{buildroot}%{_libdir}/libmozjs-%{major}.so

%check
# Run SpiderMonkey tests
%if 0%{?require_tests}
PYTHONPATH=tests/lib %{__python3} tests/jstests.py -d -s -t 1800 --no-progress --wpt=disabled ../../js/src/dist/bin/js%{major}
%else
PYTHONPATH=tests/lib %{__python3} tests/jstests.py -d -s -t 1800 --no-progress --wpt=disabled ../../js/src/dist/bin/js%{major} || :
%endif

# Run basic JIT tests
%if 0%{?require_tests}
PYTHONPATH=tests/lib %{__python3} jit-test/jit_test.py -s -t 1800 --no-progress ../../js/src/dist/bin/js%{major} basic
%else
PYTHONPATH=tests/lib %{__python3} jit-test/jit_test.py -s -t 1800 --no-progress ../../js/src/dist/bin/js%{major} basic || :
%endif

%ldconfig_scriptlets

%files
%doc README.html
%license LICENSE
%{_libdir}/libmozjs-%{major}.so.0*

%files devel
%{_bindir}/js%{major}
%{_libdir}/libmozjs-%{major}.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/mozjs-%{major}/

%changelog
* Mon Oct 19 2020 Frantisek Zatloukal <fzatlouk@redhat.com> - 78.4.0-1
- Update to 78.4.0

* Tue Sep 22 2020 Frantisek Zatloukal <fzatlouk@redhat.com> - 78.3.0-1
- Update to 78.3.0

* Mon Aug 24 2020 Frantisek Zatloukal <fzatlouk@redhat.com> - 78.2.0-1
- Update to 78.2.0

* Mon Aug 17 2020 Frantisek Zatloukal <fzatlouk@redhat.com> - 78.1.0-2
- Add BR: python3-setuptools
- Backport fix for https://bugzilla.mozilla.org/show_bug.cgi?id=1654696
- Set CARGO_PROFILE_RELEASE_LTO=true

* Tue Jul 28 2020 Frantisek Zatloukal <fzatlouk@redhat.com> - 78.1.0-1
- Initial mozjs78 package based on mozjs68

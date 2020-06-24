# ======================================================
# Conditionals and other variables controlling the build
# ======================================================

%global pybasever 3.4

# pybasever without the dot:
%global pyshortver 34

%global pylibdir %{_libdir}/python%{pybasever}
%global dynload_dir %{pylibdir}/lib-dynload

# SOABI is defined in the upstream configure.in from Python-3.2a2 onwards,
# for PEP 3149:
#   http://www.python.org/dev/peps/pep-3149/

# ("configure.in" became "configure.ac" in Python 3.3 onwards, and in
# backports)

# ABIFLAGS, LDVERSION and SOABI are in the upstream Makefile
# With Python 3.3, we lose the "u" suffix due to PEP 393
%global ABIFLAGS_optimized m
%global ABIFLAGS_debug     dm

%global LDVERSION_optimized %{pybasever}%{ABIFLAGS_optimized}
%global LDVERSION_debug     %{pybasever}%{ABIFLAGS_debug}

%global SOABI_optimized cpython-%{pyshortver}%{ABIFLAGS_optimized}
%global SOABI_debug     cpython-%{pyshortver}%{ABIFLAGS_debug}

# All bytecode files are now in a __pycache__ subdirectory, with a name
# reflecting the version of the bytecode (to permit sharing of python libraries
# between different runtimes)
# See http://www.python.org/dev/peps/pep-3147/
# For example,
#   foo/bar.py
# now has bytecode at:
#   foo/__pycache__/bar.cpython-34.pyc
#   foo/__pycache__/bar.cpython-34.pyo
%global bytecode_suffixes .cpython-34.py?

# Python's configure script defines SOVERSION, and this is used in the Makefile
# to determine INSTSONAME, the name of the libpython DSO:
#   LDLIBRARY='libpython$(VERSION).so'
#   INSTSONAME="$LDLIBRARY".$SOVERSION
# We mirror this here in order to make it easier to add the -gdb.py hooks.
# (if these get out of sync, the payload of the libs subpackage will fail
# and halt the build)
%global py_SOVERSION 1.0
%global py_INSTSONAME_optimized libpython%{LDVERSION_optimized}.so.%{py_SOVERSION}
%global py_INSTSONAME_debug     libpython%{LDVERSION_debug}.so.%{py_SOVERSION}

%global with_debug_build 0

%global with_gdb_hooks 1

%global with_systemtap 1

# some arches don't have valgrind so we need to disable its support on them
%ifarch %{valgrind_arches}
%global with_valgrind 1
%else
%global with_valgrind 0
%endif

%global with_gdbm 1

# Change from yes to no to turn this off
%global with_computed_gotos yes

# Turn this to 0 to turn off the "check" phase:
%global run_selftest_suite 1

# Disable automatic bytecompilation. The python3 binary is not yet be
# available in /usr/bin when Python is built. Also, the bytecompilation fails
# on files that test invalid syntax.
%undefine py_auto_byte_compile

# We need to get a newer configure generated out of configure.in for the following
# patches:
#   patch 55 (systemtap)
#   patch 113 (more config flags)
#
# For patch 55 (systemtap), we need to get a new header for configure to use
#
# configure.in requires autoconf-2.65, but the version in Fedora is currently
# autoconf-2.66
#
# For now, we'll generate a patch to the generated configure script and
# pyconfig.h.in on a machine that has a local copy of autoconf 2.65
#
# Instructions on obtaining such a copy can be seen at
#   http://bugs.python.org/issue7997
#
# To make it easy to regenerate the patch, this specfile can be run in two
# ways:
# (i) regenerate_autotooling_patch  0 : the normal approach: prep the
# source tree using a pre-generated patch to the "configure" script, and do a
# full build
# (ii) regenerate_autotooling_patch 1 : intended to be run on a developer's
# workstation: prep the source tree without patching configure, then rerun a
# local copy of autoconf-2.65, regenerate the patch, then exit, without doing
# the rest of the build
%global regenerate_autotooling_patch 0


# ==================
# Top-level metadata
# ==================
Summary: Version 3.4 of the Python programming language
Name: python%{pyshortver}
%global general_version %{pybasever}.10
#global prerel ...
%global upstream_version %{general_version}%{?prerel}
Version: %{general_version}%{?prerel:~%{prerel}}
Release: 10%{?dist}
License: Python

# Whether to use RPM build wheels from the python-{pip,setuptools}-wheel package
# Uses upstream bundled prebuilt wheels otherwise
# Python 3.4 is not supported in pip 19.2+!
%bcond_with rpmwheels

# =======================
# Build-time requirements
# =======================

# (keep this list alphabetized)

BuildRequires: autoconf
BuildRequires: bluez-libs-devel
BuildRequires: bzip2
BuildRequires: bzip2-devel

# expat 2.1.0 added the symbol XML_SetHashSalt without bumping SONAME.  We use
# it (in pyexpat) in order to enable the fix in Python-3.2.3 for CVE-2012-0876:
BuildRequires: expat-devel >= 2.1.0

BuildRequires: findutils
BuildRequires: gcc-c++
%if %{with_gdbm}
BuildRequires: gdbm-devel
%endif
BuildRequires: glibc-all-langpacks
BuildRequires: glibc-devel
BuildRequires: gmp-devel
BuildRequires: libffi-devel
BuildRequires: libGL-devel
BuildRequires: libX11-devel
BuildRequires: ncurses-devel
# workaround http://bugs.python.org/issue19804 (test_uuid requires ifconfig)
BuildRequires: net-tools
BuildRequires: openssl-devel
BuildRequires: pkgconfig
BuildRequires: readline-devel
BuildRequires: sqlite-devel

%if 0%{?with_systemtap}
BuildRequires: systemtap-sdt-devel
# (this introduces a dependency on "python", in that systemtap-sdt-devel's
# /usr/bin/dtrace is a python 2 script)
%global tapsetdir      /usr/share/systemtap/tapset
%endif # with_systemtap

BuildRequires: tar
BuildRequires: tcl-devel
BuildRequires: tix-devel
BuildRequires: tk-devel

%if 0%{?with_valgrind}
BuildRequires: valgrind-devel
%endif

BuildRequires: xz-devel
BuildRequires: zlib-devel

Requires: expat >= 2.1.0
# Python 3 built with glibc >= 2.24.90-26 needs to require it (rhbz#1410644).
Requires: glibc%{?_isa} >= 2.24.90-26
BuildRequires: python-rpm-macros

%if %{with rpmwheels}
BuildRequires: python-setuptools-wheel
BuildRequires: python-pip-wheel
%endif

# People might want to dnf install pythonX.Y instead of pythonXY
Provides: python%{pybasever} = %{version}-%{release}

# =======================
# Source code and patches
# =======================

Source: http://www.python.org/ftp/python/%{general_version}/Python-%{upstream_version}.tar.xz

# Supply an RPM macro "py_byte_compile" for the python3-devel subpackage
# to enable specfiles to selectively byte-compile individual files and paths
# with different Python runtimes as necessary:
Source3: macros.pybytecompile%{pybasever}

# Systemtap tapset to make it easier to use the systemtap static probes
# (actually a template; LIBRARY_PATH will get fixed up during install)
# Written by dmalcolm; not yet sent upstream
Source5: libpython.stp

# Example systemtap script using the tapset
# Written by wcohen, mjw, dmalcolm; not yet sent upstream
Source6: systemtap-example.stp

# Another example systemtap script that uses the tapset
# Written by dmalcolm; not yet sent upstream
Source7: pyfuntop.stp

# A simple script to check timestamps of bytecode files
# Run in check section with Python that is currently being built
# Written by bkabrda
Source8: check-pyc-and-pyo-timestamps.py

# Fixup distutils/unixccompiler.py to remove standard library path from rpath:
# Was Patch0 in ivazquez' python3000 specfile:
Patch1:         Python-3.1.1-rpath.patch

# 00055 #
# Systemtap support: add statically-defined probe points
# Patch sent upstream as http://bugs.python.org/issue14776
# with some subsequent reworking to cope with LANG=C in an rpmbuild
# (where sys.getfilesystemencoding() == 'ascii')
Patch55: 00055-systemtap.patch

Patch102: 00102-lib64.patch

# 00104 #
# Only used when "%{_lib}" == "lib64"
# Another lib64 fix, for distutils/tests/test_install.py; not upstream:
Patch104: 00104-lib64-fix-for-test_install.patch

# 00111 #
# Patch the Makefile.pre.in so that the generated Makefile doesn't try to build
# a libpythonMAJOR.MINOR.a (bug 550692):
# Downstream only: not appropriate for upstream
Patch111: 00111-no-static-lib.patch

# 00113 #
# Add configure-time support for the COUNT_ALLOCS and CALL_PROFILE options
# described at http://svn.python.org/projects/python/trunk/Misc/SpecialBuilds.txt
# so that if they are enabled, they will be in that build's pyconfig.h, so that
# extension modules will reliably use them
# Not yet sent upstream
Patch113: 00113-more-configuration-flags.patch

# 00125 #
# COUNT_ALLOCS is useful for debugging, but the upstream behaviour of always
# emitting debug info to stdout on exit is too verbose and makes it harder to
# use the debug build.  Add a "PYTHONDUMPCOUNTS" environment variable which
# must be set to enable the output on exit
# Not yet sent upstream
Patch125: 00125-less-verbose-COUNT_ALLOCS.patch

# 00131 #
# The four tests in test_io built on top of check_interrupted_write_retry
# fail when built in Koji, for ppc and ppc64; for some reason, the SIGALRM
# handlers are never called, and the call to write runs to completion
# (rhbz#732998)
Patch131: 00131-disable-tests-in-test_io.patch

# 00132 #
# Add non-standard hooks to unittest for use in the "check" phase below, when
# running selftests within the build:
#   @unittest._skipInRpmBuild(reason)
# for tests that hang or fail intermittently within the build environment, and:
#   @unittest._expectedFailureInRpmBuild
# for tests that always fail within the build environment
#
# The hooks only take effect if WITHIN_PYTHON_RPM_BUILD is set in the
# environment, which we set manually in the appropriate portion of the "check"
# phase below (and which potentially other python-* rpms could set, to reuse
# these unittest hooks in their own "check" phases)
Patch132: 00132-add-rpmbuild-hooks-to-unittest.patch

# 00134 #
# Fix a failure in test_sys.py when configured with COUNT_ALLOCS enabled
# Not yet sent upstream
Patch134: 00134-fix-COUNT_ALLOCS-failure-in-test_sys.patch

# 00135 #
# test_weakref's test_callback_in_cycle_resurrection doesn't work with
# COUNT_ALLOCS, as the metrics keep "C" alive.  Work around this for our
# debug build:
# Not yet sent upstream
Patch135: 00135-fix-test-within-test_weakref-in-debug-build.patch

# 00137 #
# Some tests within distutils fail when run in an rpmbuild:
Patch137: 00137-skip-distutils-tests-that-fail-in-rpmbuild.patch

# 00139 #
# ARM-specific: skip known failure in test_float:
#  http://bugs.python.org/issue8265 (rhbz#706253)
Patch139: 00139-skip-test_float-known-failure-on-arm.patch

# ideally short lived patch disabling a test thats fragile on different arches
Patch140: python3-arm-skip-failing-fragile-test.patch

# 00141 #
# Fix tests for case when  tests for case when configured with
# COUNT_ALLOCS (debug build): http://bugs.python.org/issue19527
# Applies to: test_gc, test_module, test_io, test_logging, test_warnings,
#             test_threading
Patch141: 00141-fix-tests_with_COUNT_ALLOCS.patch

# 00143 #
# Fix the --with-tsc option on ppc64, and rework it on 32-bit ppc to avoid
# aliasing violations (rhbz#698726)
# Sent upstream as http://bugs.python.org/issue12872
Patch143: 00143-tsc-on-ppc.patch

# 00146 #
# Support OpenSSL FIPS mode (e.g. when OPENSSL_FORCE_FIPS_MODE=1 is set)
# - handle failures from OpenSSL (e.g. on attempts to use MD5 in a
#   FIPS-enforcing environment)
# - add a new "usedforsecurity" keyword argument to the various digest
#   algorithms in hashlib so that you can whitelist a callsite with
#   "usedforsecurity=False"
# (sent upstream for python 3 as http://bugs.python.org/issue9216 ; see RHEL6
# python patch 119)
# - enforce usage of the _hashlib implementation: don't fall back to the _md5
#   and _sha* modules (leading to clearer error messages if fips selftests
#   fail)
# - don't build the _md5 and _sha* modules; rely on the _hashlib implementation
#   of hashlib
# (rhbz#563986)
# Note: Up to Python 3.4.0.b1, upstream had their own implementation of what
# they assumed would become sha3. This patch was adapted to give it the
# usedforsecurity argument, even though it did nothing (OpenSSL didn't have
# sha3 implementation at that time).In 3.4.0.b2, sha3 implementation was reverted
# (see http://bugs.python.org/issue16113), but the alterations were left in the
# patch, since they may be useful again if upstream decides to rerevert sha3
# implementation and OpenSSL still doesn't support it. For now, they're harmless.
Patch146: 00146-hashlib-fips.patch

# 00150 #
# temporarily disable rAssertAlmostEqual in test_cmath on PPC (bz #750811)
# caused by a glibc bug. This patch can be removed when we have a glibc with
# the patch mentioned here:
#   http://sourceware.org/bugzilla/show_bug.cgi?id=13472
Patch150: 00150-disable-rAssertAlmostEqual-cmath-on-ppc.patch

# 00155 #
# Avoid allocating thunks in ctypes unless absolutely necessary, to avoid
# generating SELinux denials on "import ctypes" and "import uuid" when
# embedding Python within httpd (rhbz#814391)
Patch155: 00155-avoid-ctypes-thunks.patch

# 00157 #
# Update uid/gid handling throughout the standard library: uid_t and gid_t are
# unsigned 32-bit values, but existing code often passed them through C long
# values, which are signed 32-bit values on 32-bit architectures, leading to
# negative int objects for uid/gid values >= 2^31 on 32-bit architectures.
#
# Introduce _PyObject_FromUid/Gid to convert uid_t/gid_t values to python
# objects, using int objects where the value will fit (long objects otherwise),
# and _PyArg_ParseUid/Gid to convert int/long to uid_t/gid_t, with -1 allowed
# as a special case (since this is given special meaning by the chown syscall)
#
# Update standard library to use this throughout for uid/gid values, so that
# very large uid/gid values are round-trippable, and -1 remains usable.
# (rhbz#697470)
Patch157: 00157-uid-gid-overflows.patch

# 00160 #
# Python 3.3 added os.SEEK_DATA and os.SEEK_HOLE, which may be present in the
# header files in the build chroot, but may not be supported in the running
# kernel, hence we disable this test in an rpm build.
# Adding these was upstream issue http://bugs.python.org/issue10142
# Not yet sent upstream
Patch160: 00160-disable-test_fs_holes-in-rpm-build.patch

# 00163 #
# Some tests within test_socket fail intermittently when run inside Koji;
# disable them using unittest._skipInRpmBuild
# Not yet sent upstream
Patch163: 00163-disable-parts-of-test_socket-in-rpm-build.patch

# 0164 #
# some tests in test._io interrupted_write-* fail on PPC (rhbz#846849)
# testChainingDescriptors  test in test_exceptions fails on PPc, too (rhbz#846849)
# disable those tests so that rebuilds on PPC can continue
Patch164: 00164-disable-interrupted_write-tests-on-ppc.patch

# 00170 #
# In debug builds, try to print repr() when a C-level assert fails in the
# garbage collector (typically indicating a reference-counting error
# somewhere else e.g in an extension module)
# Backported to 2.7 from a patch I sent upstream for py3k
#   http://bugs.python.org/issue9263  (rhbz#614680)
# hiding the proposed new macros/functions within gcmodule.c to avoid exposing
# them within the extension API.
# (rhbz#850013
Patch170: 00170-gc-assertions.patch

# 00173 #
# Workaround for ENOPROTOOPT seen in Koji withi test.support.bind_port()
# (rhbz#913732)
Patch173: 00173-workaround-ENOPROTOOPT-in-bind_port.patch

# 00178 #
# Don't duplicate various FLAGS in sysconfig values
# http://bugs.python.org/issue17679
# Does not affect python2 AFAICS (different sysconfig values initialization)
Patch178: 00178-dont-duplicate-flags-in-sysconfig.patch

# 00179 #
# Workaround for https://bugzilla.redhat.com/show_bug.cgi?id=951802
# Reported upstream in http://bugs.python.org/issue17737
# This patch basically looks at every frame and if it is somehow corrupted,
# it just stops printing the traceback - it doesn't fix the actual bug.
# This bug seems to only affect ARM.
# Doesn't seem to affect Python 2 AFAICS.
Patch179: 00179-dont-raise-error-on-gdb-corrupted-frames-in-backtrace.patch

# 00180 #
# Enable building on ppc64p7
# Not appropriate for upstream, Fedora-specific naming
Patch180: 00180-python-add-support-for-ppc64p7.patch

# 00184 #
# Fix for https://bugzilla.redhat.com/show_bug.cgi?id=979696
# Fixes build of ctypes against libffi with multilib wrapper
# Python recognizes ffi.h only if it contains "#define LIBFFI_H",
# but the wrapper doesn't contain that, which makes the build fail
# We patch this by also accepting "#define ffi_wrapper_h"
Patch184: 00184-ctypes-should-build-with-libffi-multilib-wrapper.patch

# 00186 #
# Fix for https://bugzilla.redhat.com/show_bug.cgi?id=1023607
# Previously, this fixed a problem where some *.py files were not being
# bytecompiled properly during build. This was result of py_compile.compile
# raising exception when trying to convert test file with bad encoding, and
# thus not continuing bytecompilation for other files.
# This was fixed upstream, but the test hasn't been merged yet, so we keep it
Patch186: 00186-dont-raise-from-py_compile.patch

# 00188 #
# Downstream only patch that should be removed when we compile all guaranteed
# hashlib algorithms properly. The problem is this:
# - during tests, test_hashlib is imported and executed before test_lib2to3
# - if at least one hash function has failed, trying to import it triggers an
#   exception that is being caught and exception is logged:
#   http://hg.python.org/cpython/file/2de806c8b070/Lib/hashlib.py#l217
# - logging the exception makes logging module run basicConfig
# - when lib2to3 tests are run again, lib2to3 runs basicConfig again, which
#   doesn't do anything, because it was run previously
#   (logging.root.handlers != []), which means that the default setup
#   (most importantly logging level) is not overriden. That means that a test
#   relying on this will fail (test_filename_changing_on_output_single_dir)
Patch188: 00188-fix-lib2to3-tests-when-hashlib-doesnt-compile-properly.patch

# 00189 #
# Instead of bundled wheels, use our RPM packaged wheels from
# /usr/share/python-wheels
Patch189: 00189-use-rpm-wheels.patch

# Tests requiring SIGHUP to work don't work in Koji
# see rhbz#1088233
Patch194: temporarily-disable-tests-requiring-SIGHUP.patch

# 00196
#
#  Fix test_gdb failure on ppc64le
Patch196: 00196-test-gdb-match-addr-before-builtin.patch

# 00200 #
# Fix for gettext plural form headers (lines that begin with "#")
# Note: Backported from scl
Patch200: 00200-gettext-plural-fix.patch

# 00201 #
# Fixes memory leak in gdbm module (rhbz#977308)
# This was upstreamed as a part of bigger patch, but for our purposes
# this is ok: http://bugs.python.org/issue18404
# Note: Backported from scl
Patch201: 00201-fix-memory-leak-in-gdbm.patch

# test_threading fails in koji dues to it's handling of signals
Patch203: 00203-disable-threading-test-koji.patch

# 00250 #
# After  glibc-2.24.90, Python 3 failed to start on EL7 kernel
# rhbz#1410175: https://bugzilla.redhat.com/show_bug.cgi?id=1410175
# http://bugs.python.org/issue29157
# Using the patch for python 2 as it is closer to the logic used
# for random.c in Python 3.4
# https://hg.python.org/cpython/rev/13a39142c047
Patch250: 00250-getentropy.patch

# 00273 #
# Skip test_float_with_comma, which fails in Koji with UnicodeDecodeError
# See https://bugzilla.redhat.com/show_bug.cgi?id=1484497
Patch273: 00273-skip-float-test.patch

# 00290 #
# Not every target system may provide a crypt() function in its stdlibc
# and may use an external or replacement library, like libxcrypt, for
# providing such functions.
# Fixed upstream: https://bugs.python.org/issue32635
Patch290: 00290-cryptmodule-Include-crypt.h-for-declaration-of-crypt.patch

# 00315 #
# Fix mktime() error in test_email
# http://bugs.python.org/issue35317
# https://bugzilla.redhat.com/show_bug.cgi?id=1652843
Patch315: 00315-test_email-mktime.patch

# 00320 #
# Security fix for CVE-2019-10160: Information Disclosure due to urlsplit improper NFKC normalization
# Fixed upstream for later branches: https://bugs.python.org/issue36742
# Resolves: https://bugzilla.redhat.com/show_bug.cgi?id=1718867
Patch320: 00320-CVE-2019-10160.patch

# 00321 #
# OpenSSL 1.1.1 support for Python 3.4
# https://bugzilla.redhat.com/show_bug.cgi?id=1685612
# Rejected upstream https://github.com/python/cpython/pull/12211
# and Python 3.4 reached end-of-life.
Patch321: 00321-python34-openssl-1.1.1.patch

# 00322 #
# Skip test_ssl and test_asyncio tests failing with OpenSSL 1.1.1
# https://bugzilla.redhat.com/show_bug.cgi?id=1685609
Patch322: 00322-test_ssl-skip-openssl111.patch

# 00332 #
# Fix CVE-2019-16056: Don't parse email addresses containing
# multiple '@' characters.
# Fixed upstream and backported from the 3.5 branch:
# https://bugs.python.org/issue34155
# Resolves: https://bugzilla.redhat.com/show_bug.cgi?id=1750457
Patch332: 00332-CVE-2019-16056.patch

# 00343 #
# bpo-38965: Fix faulthandler._stack_overflow() on GCC 10
# Fixed upstream and backported from the 3.7 branch:
# https://bugs.python.org/issue38965
# https://github.com/python/cpython/commit/f4a21d3b239bf4f4e4e2a8a5936b9b040645b246
Patch343: 00343-faulthandler-gcc10.patch

# (New patches go here ^^^)
#
# When adding new patches to "python" and "python3" in Fedora 17 onwards,
# please try to keep the patch numbers in-sync between the two specfiles:
#
#   - use the same patch number across both specfiles for conceptually-equivalent
#     fixes, ideally with the same name
#
#   - when a patch is relevant to both specfiles, use the same introductory
#     comment in both specfiles where possible (to improve "diff" output when
#     comparing them)
#
#   - when a patch is only relevant for one of the two specfiles, leave a gap
#     in the patch numbering in the other specfile, adding a comment when
#     omitting a patch, both in the manifest section here, and in the "prep"
#     phase below
#
# Hopefully this will make it easier to ensure that all relevant fixes are
# applied to both versions.

# This is the generated patch to "configure"; see the description of
#   %{regenerate_autotooling_patch}
# above:
Patch5000: 05000-autotool-intermediates.patch


# ======================================================
# Additional metadata, and subpackages
# ======================================================

URL: http://www.python.org/

# We don't want to provide this
# No package in Fedora shall ever depend on this
%global __requires_exclude ^python\\(abi\\) = 3\\..$
%global __provides_exclude ^python\\(abi\\) = 3\\..$

%if %{with rpmwheels}
Requires: python-setuptools-wheel
Requires: python-pip-wheel
%else
Provides: bundled(python3dist(setuptools)) = 28.8.0
Provides: bundled(python3dist(packaging)) = 16.7
Provides: bundled(python3dist(pyparsing)) = 2.1.10
Provides: bundled(python3dist(six)) = 1.10.0
Provides: bundled(python3dist(appdirs)) = 1.4.0

Provides: bundled(python3dist(pip)) = 9.0.1
Provides: bundled(python3dist(appdirs)) = 1.4.0
Provides: bundled(python3dist(distlib)) = 0.2.4
Provides: bundled(python3dist(distro)) = 1.0.1
Provides: bundled(python3dist(html5lib)) = 1.0~b10
Provides: bundled(python3dist(six)) = 1.10.0
Provides: bundled(python3dist(colorama)) = 0.3.7
Provides: bundled(python3dist(requests)) = 2.11.1
Provides: bundled(python3dist(CacheControl)) = 0.11.7
Provides: bundled(python3dist(lockfile)) = 0.12.2
Provides: bundled(python3dist(progress)) = 1.2
Provides: bundled(python3dist(packaging)) = 16.8
Provides: bundled(python3dist(pyparsing)) = 2.1.10
Provides: bundled(python3dist(retrying)) = 1.3.3
Provides: bundled(python3dist(webencodings)) = 0.5
%endif

%description
Python %{pybasever} package for developers.

This package exists to allow developers to test their code against an older
version of Python. This is not a full Python stack and if you wish to run
your applications with Python %{pybasever}, see other distributions
that support it, such as CentOS or RHEL with Software Collections.


# ======================================================
# The prep phase of the build:
# ======================================================

%prep
%setup -q -n Python-%{upstream_version}

%if 0%{?with_systemtap}
# Provide an example of usage of the tapset:
cp -a %{SOURCE6} .
cp -a %{SOURCE7} .
%endif # with_systemtap

# Ensure that we're using the system copy of various libraries, rather than
# copies shipped by upstream in the tarball:
#   Remove embedded copy of expat:
rm -r Modules/expat || exit 1

#   Remove embedded copy of libffi:
for SUBDIR in darwin libffi libffi_arm_wince libffi_msvc libffi_osx ; do
  rm -r Modules/_ctypes/$SUBDIR || exit 1 ;
done

#   Remove embedded copy of zlib:
rm -r Modules/zlib || exit 1

# Don't build upstream Python's implementation of these crypto algorithms;
# instead rely on _hashlib and OpenSSL.
#
# For example, in our builds hashlib.md5 is implemented within _hashlib via
# OpenSSL (and thus respects FIPS mode), and does not fall back to _md5
# TODO: there seems to be no OpenSSL support in Python for sha3 so far
# when it is there, also remove _sha3/ dir
for f in md5module.c sha1module.c sha256module.c sha512module.c; do
    rm Modules/$f
done

#
# Apply patches:
#
%patch1 -p1
# 3: upstream as of Python 3.3.1

%if 0%{?with_systemtap}
%patch55 -p1 -b .systemtap
%endif

%if "%{_lib}" == "lib64"
%patch102 -p1
%patch104 -p1
%endif


%patch111 -p1
%patch113 -p1

%patch125 -p1 -b .less-verbose-COUNT_ALLOCS

%ifarch ppc %{power64}
%patch131 -p1
%endif

%patch132 -p1
%patch134 -p1
%patch135 -p1
%patch137 -p1

%ifarch %{arm}
%patch139 -p1
%patch140 -p1
%endif

%patch141 -p1
%patch143 -p1 -b .tsc-on-ppc
%patch146 -p1

%ifarch ppc %{power64}
%patch150 -p1
%endif

%patch155 -p1
%patch157 -p1
%patch160 -p1
%patch163 -p1

%ifarch ppc %{power64}
%patch164 -p1
%endif

%patch173 -p1
%patch178 -p1
%patch179 -p1
%patch180 -p1
%patch184  -p1
%patch186 -p1
%patch188 -p1

%if %{with rpmwheels}
%patch189 -p1
rm Lib/ensurepip/_bundled/*.whl
rmdir Lib/ensurepip/_bundled
%endif

%patch194 -p1
%patch196 -p1
%patch203 -p1
%patch250 -p1
%patch273 -p1
%patch290 -p1
%patch315 -p1
%patch320 -p1
%patch321 -p1
%patch322 -p1
%patch332 -p1
%patch343 -p1

# Currently (2010-01-15), http://docs.python.org/library is for 2.6, and there
# are many differences between 2.6 and the Python 3 library.
#
# Fix up the URLs within pydoc to point at the documentation for this
# MAJOR.MINOR version:
#
sed --in-place \
    --expression="s|http://docs.python.org/library|http://docs.python.org/%{pybasever}/library|g" \
    Lib/pydoc.py || exit 1

%if ! 0%{regenerate_autotooling_patch}
# Normally we apply the patch to "configure"
# We don't apply the patch if we're working towards regenerating it
%patch5000 -p0 -b .autotool-intermediates
%endif

# ======================================================
# Configuring and building the code:
# ======================================================

%build
topdir=$(pwd)
export CFLAGS="$RPM_OPT_FLAGS -D_GNU_SOURCE -fPIC -fwrapv"
export CXXFLAGS="$RPM_OPT_FLAGS -D_GNU_SOURCE -fPIC -fwrapv"
export CPPFLAGS="`pkg-config --cflags-only-I libffi`"
export OPT="$RPM_OPT_FLAGS -D_GNU_SOURCE -fPIC -fwrapv"
export LINKCC="gcc"
export CFLAGS="$CFLAGS `pkg-config --cflags openssl`"
export LDFLAGS="$RPM_LD_FLAGS `pkg-config --libs-only-L openssl`"

%if 0%{regenerate_autotooling_patch}
# If enabled, this code regenerates the patch to "configure", using a
# local copy of autoconf-2.65, then exits the build
#
# The following assumes that the copy is installed to ~/autoconf-2.65/bin
# as per these instructions:
#   http://bugs.python.org/issue7997

for f in pyconfig.h.in configure ; do
    cp $f $f.autotool-intermediates ;
done

# Rerun the autotools:
autoreconf

# Regenerate the patch:
gendiff . .autotool-intermediates > %{PATCH5000}


# Exit the build
exit 1
%endif

# Define a function, for how to perform a "build" of python for a given
# configuration:
BuildPython() {
  ConfName=$1	
  BinaryName=$2
  SymlinkName=$3
  ExtraConfigArgs=$4
  PathFixWithThisBinary=$5
  MoreCFlags=$6

  ConfDir=build/$ConfName

  echo STARTING: BUILD OF PYTHON FOR CONFIGURATION: $ConfName - %{_bindir}/$BinaryName
  mkdir -p $ConfDir

  pushd $ConfDir

  # Use the freshly created "configure" script, but in the directory two above:
  %global _configure $topdir/configure

%configure \
  --enable-ipv6 \
  --enable-shared \
  --with-computed-gotos=%{with_computed_gotos} \
  --with-dbmliborder=gdbm:ndbm:bdb \
  --with-system-expat \
  --with-system-ffi \
  --enable-loadable-sqlite-extensions \
%if 0%{?with_systemtap}
  --with-systemtap \
%endif
%if 0%{?with_valgrind}
  --with-valgrind \
%endif
  $ExtraConfigArgs \
  %{nil}

  # Set EXTRA_CFLAGS to our CFLAGS (rather than overriding OPT, as we've done
  # in the past).
  # This should fix a problem with --with-valgrind where it adds
  #   -DDYNAMIC_ANNOTATIONS_ENABLED=1
  # to OPT which must be passed to all compilation units in the build,
  # otherwise leading to linker errors, e.g.
  #    missing symbol AnnotateRWLockDestroy
  #
  # Invoke the build:
  make EXTRA_CFLAGS="$CFLAGS $MoreCFlags" %{?_smp_mflags}

  popd
  echo FINISHED: BUILD OF PYTHON FOR CONFIGURATION: $ConfDir
}

# Use "BuildPython" to support building with different configurations:

%if 0%{?with_debug_build}
BuildPython debug \
  python-debug \
  python%{pybasever}-debug \
%ifarch %{ix86} x86_64 ppc %{power64}
  "--with-pydebug --with-tsc --with-count-allocs --with-call-profile --without-ensurepip" \
%else
  "--with-pydebug --with-count-allocs --with-call-profile --without-ensurepip" \
%endif
  false \
  -O0
%endif # with_debug_build

BuildPython optimized \
  python \
  python%{pybasever} \
  "--without-ensurepip" \
  true

# ======================================================
# Installing the built code:
# ======================================================

%install
topdir=$(pwd)
rm -fr %{buildroot}
mkdir -p %{buildroot}%{_prefix} %{buildroot}%{_mandir}

InstallPython() {

  ConfName=$1	
  PyInstSoName=$2
  MoreCFlags=$3

  ConfDir=build/$ConfName

  echo STARTING: INSTALL OF PYTHON FOR CONFIGURATION: $ConfName
  mkdir -p $ConfDir

  pushd $ConfDir

make install DESTDIR=%{buildroot} INSTALL="install -p" EXTRA_CFLAGS="$MoreCFlags"

  popd

  # We install a collection of hooks for gdb that make it easier to debug
  # executables linked against libpython3* (such as /usr/bin/python3 itself)
  #
  # These hooks are implemented in Python itself (though they are for the version
  # of python that gdb is linked with, in this case Python 2.7)
  #
  # gdb-archer looks for them in the same path as the ELF file, with a -gdb.py suffix.
  # We put them in the debuginfo package by installing them to e.g.:
  #  /usr/lib/debug/usr/lib/libpython3.2.so.1.0.debug-gdb.py
  #
  # See https://fedoraproject.org/wiki/Features/EasierPythonDebugging for more
  # information
  #
  # Copy up the gdb hooks into place; the python file will be autoloaded by gdb
  # when visiting libpython.so, provided that the python file is installed to the
  # same path as the library (or its .debug file) plus a "-gdb.py" suffix, e.g:
  #  /usr/lib/debug/usr/lib64/libpython3.2.so.1.0.debug-gdb.py
  # (note that the debug path is /usr/lib/debug for both 32/64 bit)
  #
  # Initially I tried:
  #  /usr/lib/libpython3.1.so.1.0-gdb.py
  # but doing so generated noise when ldconfig was rerun (rhbz:562980)
  #
%if 0%{?with_gdb_hooks}
  DirHoldingGdbPy=%{_prefix}/lib/debug/%{_libdir}
  PathOfGdbPy=$DirHoldingGdbPy/$PyInstSoName.debug-gdb.py

  mkdir -p %{buildroot}$DirHoldingGdbPy
  cp Tools/gdb/libpython.py %{buildroot}$PathOfGdbPy
%endif # with_gdb_hooks

  echo FINISHED: INSTALL OF PYTHON FOR CONFIGURATION: $ConfName
}

# Use "InstallPython" to support building with different configurations:

# Install the "debug" build first, so that we can move some files aside
%if 0%{?with_debug_build}
InstallPython debug \
  %{py_INSTSONAME_debug} \
  -O0
%endif # with_debug_build

# Now the optimized build:
InstallPython optimized \
  %{py_INSTSONAME_optimized}

install -d -m 0755 ${RPM_BUILD_ROOT}%{pylibdir}/site-packages/__pycache__

# Documentation tools
install -m755 -d %{buildroot}%{pylibdir}/Doc
cp -ar Doc/tools %{buildroot}%{pylibdir}/Doc/

# Fix for bug #136654
rm -f %{buildroot}%{pylibdir}/email/test/data/audiotest.au %{buildroot}%{pylibdir}/test/audiotest.au

%if "%{_lib}" == "lib64"
install -d -m 0755 %{buildroot}/%{_prefix}/lib/python%{pybasever}/site-packages/__pycache__
%endif

# Make python3-devel multilib-ready (bug #192747, #139911)
%global _pyconfig32_h pyconfig-32.h
%global _pyconfig64_h pyconfig-64.h

%ifarch %{power64} s390x x86_64 ia64 alpha sparc64 aarch64
%global _pyconfig_h %{_pyconfig64_h}
%else
%global _pyconfig_h %{_pyconfig32_h}
%endif

# ABIFLAGS, LDVERSION and SOABI are in the upstream Makefile
%global ABIFLAGS_optimized m
%global ABIFLAGS_debug     dm

%global LDVERSION_optimized %{pybasever}%{ABIFLAGS_optimized}
%global LDVERSION_debug     %{pybasever}%{ABIFLAGS_debug}

%global SOABI_optimized cpython-%{pyshortver}%{ABIFLAGS_optimized}
%global SOABI_debug     cpython-%{pyshortver}%{ABIFLAGS_debug}

%if 0%{?with_debug_build}
%global PyIncludeDirs python%{LDVERSION_optimized} python%{LDVERSION_debug}

%else
%global PyIncludeDirs python%{LDVERSION_optimized}
%endif

for PyIncludeDir in %{PyIncludeDirs} ; do
  mv %{buildroot}%{_includedir}/$PyIncludeDir/pyconfig.h \
     %{buildroot}%{_includedir}/$PyIncludeDir/%{_pyconfig_h}
  cat > %{buildroot}%{_includedir}/$PyIncludeDir/pyconfig.h << EOF
#include <bits/wordsize.h>

#if __WORDSIZE == 32
#include "%{_pyconfig32_h}"
#elif __WORDSIZE == 64
#include "%{_pyconfig64_h}"
#else
#error "Unknown word size"
#endif
EOF
done

# Fix for bug 201434: make sure distutils looks at the right pyconfig.h file
# Similar for sysconfig: sysconfig.get_config_h_filename tries to locate
# pyconfig.h so it can be parsed, and needs to do this at runtime in site.py
# when python starts up (bug 653058)
#
# Split this out so it goes directly to the pyconfig-32.h/pyconfig-64.h
# variants:
sed -i -e "s/'pyconfig.h'/'%{_pyconfig_h}'/" \
  %{buildroot}%{pylibdir}/distutils/sysconfig.py \
  %{buildroot}%{pylibdir}/sysconfig.py

# Switch all shebangs to refer to the specific Python version.
LD_LIBRARY_PATH=./build/optimized ./build/optimized/python \
  Tools/scripts/pathfix.py \
  -i "%{_bindir}/python%{pybasever}" -p \
  %{buildroot} \
  %{?with_gdb_hooks:%{buildroot}$DirHoldingGdbPy/*.py}

# Remove shebang lines from .py files that aren't executable, and
# remove executability from .py files that don't have a shebang line:
find %{buildroot} -name \*.py \
  \( \( \! -perm /u+x,g+x,o+x -exec sed -e '/^#!/Q 0' -e 'Q 1' {} \; \
  -print -exec sed -i '1d' {} \; \) -o \( \
  -perm /u+x,g+x,o+x ! -exec grep -m 1 -q '^#!' {} \; \
  -exec chmod a-x {} \; \) \)

# Remove tests for tools, we don't ship those
rm -rf %{buildroot}%{pylibdir}/test/test_tools

# .xpm and .xbm files should not be executable:
find %{buildroot} \
  \( -name \*.xbm -o -name \*.xpm -o -name \*.xpm.1 \) \
  -exec chmod a-x {} \;

# Remove executable flag from files that shouldn't have it:
chmod a-x \
  %{buildroot}%{pylibdir}/distutils/tests/Setup.sample

# Get rid of DOS batch files:
find %{buildroot} -name \*.bat -exec rm {} \;

# Get rid of backup files:
find %{buildroot}/ -name "*~" -exec rm -f {} \;
find . -name "*~" -exec rm -f {} \;
# Junk, no point in putting in -test sub-pkg
rm -f ${RPM_BUILD_ROOT}/%{pylibdir}/idlelib/testcode.py*

# Get rid of stray patch file from buildroot:
rm -f %{buildroot}%{pylibdir}/test/test_imp.py.apply-our-changes-to-expected-shebang # from patch 4

# Fix end-of-line encodings:
find %{buildroot}/ -name \*.py -exec sed -i 's/\r//' {} \;

# Fix an encoding:
iconv -f iso8859-1 -t utf-8 %{buildroot}/%{pylibdir}/Demo/rpc/README > README.conv && mv -f README.conv %{buildroot}/%{pylibdir}/Demo/rpc/README

# Note that
#  %{pylibdir}/Demo/distutils/test2to3/setup.py
# is in iso-8859-1 encoding, and that this is deliberate; this is test data
# for the 2to3 tool, and one of the functions of the 2to3 tool is to fixup
# character encodings within python source code

# Do bytecompilation with the newly installed interpreter.
# This is similar to the script in macros.pybytecompile
# compile *.pyo
find %{buildroot} -type f -a -name "*.py" -print0 | \
    LD_LIBRARY_PATH="%{buildroot}%{dynload_dir}/:%{buildroot}%{_libdir}" \
    PYTHONPATH="%{buildroot}%{_libdir}/python%{pybasever} %{buildroot}%{_libdir}/python%{pybasever}/site-packages" \
    xargs -0 %{buildroot}%{_bindir}/python%{pybasever} -O -c 'import py_compile, sys; [py_compile.compile(f, dfile=f.partition("%{buildroot}")[2]) for f in sys.argv[1:]]' || :
# compile *.pyc
find %{buildroot} -type f -a -name "*.py" -print0 | \
    LD_LIBRARY_PATH="%{buildroot}%{dynload_dir}/:%{buildroot}%{_libdir}" \
    PYTHONPATH="%{buildroot}%{_libdir}/python%{pybasever} %{buildroot}%{_libdir}/python%{pybasever}/site-packages" \
    xargs -0 %{buildroot}%{_bindir}/python%{pybasever} -O -c 'import py_compile, sys; [py_compile.compile(f, dfile=f.partition("%{buildroot}")[2], optimize=0) for f in sys.argv[1:]]' || :

# Fixup permissions for shared libraries from non-standard 555 to standard 755:
find %{buildroot} \
    -perm 555 -exec chmod 755 {} \;

# Install macros for rpm:
mkdir -p %{buildroot}/%{_rpmconfigdir}/macros.d/
install -m 644 %{SOURCE3} %{buildroot}/%{_rpmconfigdir}/macros.d/

# Ensure that the curses module was linked against libncursesw.so, rather than
# libncurses.so (bug 539917)
ldd %{buildroot}/%{dynload_dir}/_curses*.so \
    | grep curses \
    | grep libncurses.so && (echo "_curses.so linked against libncurses.so" ; exit 1)

# Ensure that the debug modules are linked against the debug libpython, and
# likewise for the optimized modules and libpython:
for Module in %{buildroot}/%{dynload_dir}/*.so ; do
    case $Module in
    *.%{SOABI_debug})
        ldd $Module | grep %{py_INSTSONAME_optimized} &&
            (echo Debug module $Module linked against optimized %{py_INSTSONAME_optimized} ; exit 1)

        ;;
    *.%{SOABI_optimized})
        ldd $Module | grep %{py_INSTSONAME_debug} &&
            (echo Optimized module $Module linked against debug %{py_INSTSONAME_debug} ; exit 1)
        ;;
    esac
done

#
# Systemtap hooks:
#
%if 0%{?with_systemtap}
# Install a tapset for this libpython into tapsetdir, fixing up the path to the
# library:
mkdir -p %{buildroot}%{tapsetdir}
%ifarch %{power64} s390x x86_64 ia64 alpha sparc64 aarch64
%global libpython_stp_optimized libpython%{pybasever}-64.stp
%global libpython_stp_debug     libpython%{pybasever}-debug-64.stp
%else
%global libpython_stp_optimized libpython%{pybasever}-32.stp
%global libpython_stp_debug     libpython%{pybasever}-debug-32.stp
%endif

sed \
   -e "s|LIBRARY_PATH|%{_libdir}/%{py_INSTSONAME_optimized}|" \
   %{_sourcedir}/libpython.stp \
   > %{buildroot}%{tapsetdir}/%{libpython_stp_optimized}

%if 0%{?with_debug_build}
# In Python 3, python3 and python3-debug don't point to the same binary,
# so we have to replace "python3" with "python3-debug" to get systemtap
# working with debug build
sed \
   -e "s|LIBRARY_PATH|%{_libdir}/%{py_INSTSONAME_debug}|" \
   -e 's|"python3"|"python3-debug"|' \
   %{_sourcedir}/libpython.stp \
   > %{buildroot}%{tapsetdir}/%{libpython_stp_debug}
%endif # with_debug_build

%endif # with_systemtap

# Rename the script that differs on different arches to arch specific name
mv %{buildroot}%{_bindir}/python%{LDVERSION_optimized}-{,`uname -m`-}config
echo -e '#!/bin/sh\nexec `dirname $0`/python%{LDVERSION_optimized}-`uname -m`-config "$@"' > \
  %{buildroot}%{_bindir}/python%{LDVERSION_optimized}-config
echo '[ $? -eq 127 ] && echo "Could not find python%{LDVERSION_optimized}-`uname -m`-config. Look around to see available arches." >&2' >> \
  %{buildroot}%{_bindir}/python%{LDVERSION_optimized}-config
  chmod +x %{buildroot}%{_bindir}/python%{LDVERSION_optimized}-config

# Remove stuff that would conflict with python3 package
mv %{buildroot}%{_bindir}/python{3,%{pyshortver}}
rm %{buildroot}%{_bindir}/*3  # also matches 2to3
rm %{buildroot}%{_bindir}/python3-*
rm %{buildroot}%{_bindir}/pyvenv
rm %{buildroot}%{_libdir}/libpython3.so
rm %{buildroot}%{_mandir}/man1/python3.1*
rm %{buildroot}%{_libdir}/pkgconfig/python3.pc

# ======================================================
# Running the upstream test suite
# ======================================================

%check

# first of all, check timestamps of bytecode files
find %{buildroot} -type f -a -name "*.py" -print0 | \
    LD_LIBRARY_PATH="%{buildroot}%{dynload_dir}/:%{buildroot}%{_libdir}" \
    PYTHONPATH="%{buildroot}%{_libdir}/python%{pybasever} %{buildroot}%{_libdir}/python%{pybasever}/site-packages" \
    xargs -0 %{buildroot}%{_bindir}/python%{pybasever} %{SOURCE8}


topdir=$(pwd)
CheckPython() {
  ConfName=$1	
  ConfDir=$(pwd)/build/$ConfName

  echo STARTING: CHECKING OF PYTHON FOR CONFIGURATION: $ConfName

  # Note that we're running the tests using the version of the code in the
  # builddir, not in the buildroot.

  # Run the upstream test suite, setting "WITHIN_PYTHON_RPM_BUILD" so that the
  # our non-standard decorators take effect on the relevant tests:
  #   @unittest._skipInRpmBuild(reason)
  #   @unittest._expectedFailureInRpmBuild
  # test_faulthandler.test_register_chain currently fails on ppc64le and
  #   aarch64, see upstream bug http://bugs.python.org/issue21131
  # test_buffer fails with Decimal on ppc64le,
  #   see https://bugzilla.redhat.com/show_bug.cgi?id=1544833
  # test_with_pip doesn't work with new pip on 3.4, there is deprecation warning
  WITHIN_PYTHON_RPM_BUILD= \
  LD_LIBRARY_PATH=$ConfDir $ConfDir/python -m test.regrtest \
    --verbose --findleaks \
    -x test_distutils \
    %ifarch ppc64le aarch64
    -x test_faulthandler \
    %endif
    %ifarch %{power64} s390 s390x armv7hl aarch64
    -x test_gdb \
    %endif
    -x test_venv \

  echo FINISHED: CHECKING OF PYTHON FOR CONFIGURATION: $ConfName

}

%if 0%{run_selftest_suite}

# Check each of the configurations:
%if 0%{?with_debug_build}
CheckPython debug
%endif # with_debug_build
CheckPython optimized

%endif # run_selftest_suite


%files
%doc README
%doc Misc/README.valgrind Misc/valgrind-python.supp Misc/gdbinit
%license %{pylibdir}/LICENSE.txt

%{_bindir}/pydoc%{pybasever}
%{_bindir}/python%{pybasever}
%{_bindir}/python%{pyshortver}
%{_bindir}/python%{pybasever}m
%{_bindir}/pyvenv-%{pybasever}
%{_mandir}/*/*

%{pylibdir}/

%if "%{_lib}" == "lib64"
%attr(0755,root,root) %dir %{_prefix}/lib/python%{pybasever}
%attr(0755,root,root) %dir %{_prefix}/lib/python%{pybasever}/site-packages
%attr(0755,root,root) %dir %{_prefix}/lib/python%{pybasever}/site-packages/__pycache__/
%endif

%{_libdir}/%{py_INSTSONAME_optimized}
%if 0%{?with_systemtap}
%dir %(dirname %{tapsetdir})
%dir %{tapsetdir}
%{tapsetdir}/%{libpython_stp_optimized}
%doc systemtap-example.stp pyfuntop.stp
%endif

%{_includedir}/python%{LDVERSION_optimized}/

%{_bindir}/python%{pybasever}-config
%{_bindir}/python%{LDVERSION_optimized}-config
%{_bindir}/python%{LDVERSION_optimized}-*-config
%{_libdir}/libpython%{LDVERSION_optimized}.so
%{_libdir}/pkgconfig/python-%{LDVERSION_optimized}.pc
%{_libdir}/pkgconfig/python-%{pybasever}.pc
%exclude %{_rpmconfigdir}/macros.d/macros.pybytecompile%{pybasever}

%{_bindir}/2to3-%{pybasever}
%{_bindir}/idle%{pybasever}

# https://bugzilla.redhat.com/show_bug.cgi?id=1476593
%exclude /usr/lib/debug%{_libdir}/__pycache__/libpython%{pybasever}m.so.1.0.debug-gdb.cpython-%{pyshortver}.py*
%exclude /usr/lib/debug%{_libdir}/libpython%{pybasever}m.so.1.0.debug-gdb.py

%if 0%{?with_debug_build}
%{_bindir}/python%{LDVERSION_debug}

%{_libdir}/%{py_INSTSONAME_debug}
%if 0%{?with_systemtap}
%{tapsetdir}/%{libpython_stp_debug}
%endif

%{_includedir}/python%{LDVERSION_debug}
%{_bindir}/python%{LDVERSION_debug}-config
%{_libdir}/libpython%{LDVERSION_debug}.so
%{_libdir}/libpython%{LDVERSION_debug}.so.1.0
%{_libdir}/pkgconfig/python-%{LDVERSION_debug}.pc

%endif # with_debug_build


# ======================================================
# Finally, the changelog:
# ======================================================

%changelog
* Mon Mar 30 2020 Tomas Hrnciar <thrnciar@redhat.com> - 3.4.10-10
- Add missing provides for packages bundled in bundled pip/setuptools (rhbz#1775574)

* Thu Feb 13 2020 Victor Stinner <vstinner@python.org> - 3.4.10-9
- Fix test_faulthandler for GCC 10 (rhbz#1799090)
- Fix also faulthandler.register(chain=True) stack.

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 09 2019 Charalampos Stratakis <cstratak@redhat.com> - 3.4.10-7
- Fix CVE-2019-16056 (rhbz#1750457)

* Thu Sep 05 2019 Charalampos Stratakis <cstratak@redhat.com> - 3.4.10-6
- Fix CVE-2019-10160 (rhbz#1718867)

* Wed Aug 28 2019 Miro Hrončok <mhroncok@redhat.com> - 3.4.10-5
- Use bundled wheels, prepare for pip 19.2+

* Sat Aug 10 2019 Miro Hrončok <mhroncok@redhat.com> - 3.4.10-4
- Build against OpenSSL 1.1.x, not 1.0.x

* Wed Jul 31 2019 Victor Stinner <vstinner@redhat.com> - 3.4.10-3
- Add OpenSSL 1.1.1 support (rhbz#1685612)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.4.10-1
- Update to 3.4.10

* Tue Mar 05 2019 Miro Hrončok <mhroncok@redhat.com> - 3.4.10~rc1-1
- Update to 3.4.10rc1

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.4.9-8
- Rebuild for readline 8.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Björn Esser <besser82@fedoraproject.org> - 3.4.9-6
- Rebuilt for libcrypt.so.2 (#1666033)

* Fri Jan 11 2019 Björn Esser <besser82@fedoraproject.org> - 3.4.9-5
- Add missing semicolon in patch 00290

* Mon Sep 24 2018 Miro Hrončok <mhroncok@redhat.com> - 3.4.9-4
- Security fix for CVE-2018-14647 (#1631822)

* Tue Aug 21 2018 Miro Hrončok <mhroncok@redhat.com> - 3.4.9-3
- Use RPM built wheels of pip and setuptools in ensurepip instead of bundled ones

* Wed Aug 08 2018 Miro Hrončok <mhroncok@redhat.com> - 3.4.9-2
- Fix bundled pip/setuptools versions

* Sun Aug 05 2018 Miro Hrončok <mhroncok@redhat.com> - 3.4.9-1
- Rebased to 3.4.9

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Apr 24 2018 Miro Hrončok <mhroncok@redhat.com> - 3.4.8-3
- Fix multiprocessing regression on newer glibcs
- Enable test_multiprocessing_fork(server) and _spawn again
Resolves: rhbz#1569933

* Fri Apr 20 2018 Miro Hrončok <mhroncok@redhat.com> - 3.4.8-2
- Do not ship the Tools directory
- Skip test_multiprocessing_fork(server) and _spawn for now

* Tue Feb 13 2018 Petr Viktorin <pviktori@redhat.com> - 3.4.8-1
- Update to 3.4.8 bugfix release
- Add patch 00290 to fix build with libxcrypt
- Disable test_buffer on ppc64le

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 3.4.7-3
- Rebuilt for switch to libxcrypt

* Fri Dec 08 2017 Miro Hrončok <mhroncok@redhat.com> - 3.4.7-2
- Fix for CVE-2017-1000158
- rhbz#1519601: https://bugzilla.redhat.com/show_bug.cgi?id=1519601

* Thu Nov 02 2017 Charalampos Stratakis <cstratak@redhat.com> - 3.4.7-1
- Update to 3.4.7

* Mon Aug 14 2017 David "Sanqui" Labský <dlabsky@redhat.com> - 3.4.5-8
- Drop unused db4-devel dependency

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 3.4.5-4
- Rebuild for readline 7.x

* Tue Jan 10 2017 Charalampos Stratakis <cstratak@redhat.com> - 3.4.5-3
- Require glibc >= 2.24.90-26 (rhbz#1410644)
- Don't blow up on EL7 kernel (random generator) (rhbz#1410175, rhbz#1410187)

* Fri Oct 21 2016 Miro Hrončok <mhroncok@redhat.com> - 3.4.5-2
- Reword the description
- On Fedora 26+, BR compat-openssl10-devel

* Thu Sep 22 2016 Miro Hrončok <mhroncok@redhat.com> - 3.4.5-1
- Updated to 3.4.5

* Thu Aug 11 2016 Miro Hrončok <mhroncok@redhat.com> - 3.4.3-11
- Imported from F23

# ======================================================
# Conditionals and other variables controlling the build
# ======================================================

%global pybasever 3.5

# pybasever without the dot:
%global pyshortver 35

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

# https://fedoraproject.org/wiki/Changes/Python_Upstream_Architecture_Names
# For a very long time we have converted "upstream architecture names" to "Fedora names".
# This made sense at the time, see https://github.com/pypa/manylinux/issues/687#issuecomment-666362947
# However, with manylinux wheels popularity growth, this is now a problem.
# Wheels built on a Linux that doesn't do this were not compatible with ours and vice versa.
# We now have a compatibility layer to workaround a problem,
# but we also no longer use the legacy arch names in Fedora 34+.
# This bcond controls the behavior. The defaults should be good for anybody.
%if 0%{?fedora} >= 34 || 0%{?rhel} >= 9
%bcond_with legacy_archnames
%else
%bcond_without legacy_archnames
%endif
# When we use the upstream arch triplets, we convert them from the legacy ones
# This is reversed in prep when %%with legacy_archnames, so we keep both macros
%global platform_triplet_legacy %{_arch}-linux%{_gnu}
%global platform_triplet_upstream %{expand:%(echo %{platform_triplet_legacy} | sed -E \\
    -e 's/^arm(eb)?-linux-gnueabi$/arm\\1-linux-gnueabihf/' \\
    -e 's/^mips64(el)?-linux-gnu$/mips64\\1-linux-gnuabi64/' \\
    -e 's/^ppc(64)?(le)?-linux-gnu$/powerpc\\1\\2-linux-gnu/')}
%if %{with legacy_archnames}
%global platform_triplet %{platform_triplet_legacy}
%else
%global platform_triplet %{platform_triplet_upstream}
%endif

%global SOABI_optimized cpython-%{pyshortver}%{ABIFLAGS_optimized}-%{platform_triplet}
%global SOABI_debug     cpython-%{pyshortver}%{ABIFLAGS_debug}-%{platform_triplet}

# All bytecode files are now in a __pycache__ subdirectory, with a name
# reflecting the version of the bytecode (to permit sharing of python libraries
# between different runtimes)
# See http://www.python.org/dev/peps/pep-3147/
# For example,
#   foo/bar.py
# now has bytecode at:
#   foo/__pycache__/bar.cpython-35.pyc
#   foo/__pycache__/bar.cpython-35.pyo
%global bytecode_suffixes .cpython-35*.py?

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

# ==================
# Top-level metadata
# ==================
Name: python%{pybasever}
Summary: Version %{pybasever} of the Python programming language
URL: https://www.python.org/

%global general_version %{pybasever}.10
#global prerel ...
%global upstream_version %{general_version}%{?prerel}
Version: %{general_version}%{?prerel:~%{prerel}}
Release: 2%{?dist}
License: Python

# Whether to use RPM build wheels from the python-{pip,setuptools}-wheel package
# Uses upstream bundled prebuilt wheels otherwise
%bcond_without rpmwheels

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
BuildRequires: git-core
BuildRequires: glibc-all-langpacks
BuildRequires: glibc-devel
BuildRequires: gmp-devel
BuildRequires: gnupg2
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

%if %{with rpmwheels}
BuildRequires: python-setuptools-wheel
BuildRequires: python-pip-wheel
%endif

Requires:      expat >= 2.1.0

# Python 3 built with glibc >= 2.24.90-26 needs to require it (rhbz#1410644).
Requires: glibc%{?_isa} >= 2.24.90-26

BuildRequires: python-rpm-macros

# Provide and obsolete the old python3X name
Provides:  python%{pyshortver} = %{version}-%{release}
Obsoletes: python%{pyshortver} < %{version}-%{release}

# =======================
# Source code and patches
# =======================

Source0: %{url}ftp/python/%{general_version}/Python-%{upstream_version}.tar.xz
Source1: %{url}ftp/python/%{general_version}/Python-%{upstream_version}.tar.xz.asc
Source2: %{url}static/files/pubkeys.txt

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
# Originally written by bkabrda
Source8: check-pyc-timestamps.py

# (Patches taken from github.com/fedora-python/cpython)

# 00001 # 4ce8d6d97da140622e90f3bc3339d602e41f1b14
# Fixup distutils/unixccompiler.py to remove standard library path from rpath
# Was Patch0 in ivazquez' python3000 specfile
Patch1: 00001-rpath.patch

# 00055 # f79a3778fb58416d7d8dad1c92c1fa1e7265ef23
# Systemtap support
#
# Add statically-defined probe points
# Patch sent upstream as http://bugs.python.org/issue14776
# with some subsequent reworking to cope with LANG=C in an rpmbuild
# (where sys.getfilesystemencoding() == 'ascii')
Patch55: 00055-systemtap.patch

# 00102 # 073ae9c4c844f2ef3acfb24aee5e311a3403b614
# Change the various install paths to use /usr/lib64/ instead or /usr/lib/
#
# Only used when "%%{_lib}" == "lib64".
Patch102: 00102-lib64.patch

# 00111 # 0b2461b3b5fe0241b8045b65c77e761808a67620
# Don't try to build a libpythonMAJOR.MINOR.a
#
# Downstream only: not appropriate for upstream.
#
# See https://bugzilla.redhat.com/show_bug.cgi?id=556092
Patch111: 00111-no-static-lib.patch

# 00132 # 75c270b8641ddff06c0edf7be7cc444e6debb6d7
# Add rpmbuild hooks to unittest
#
# Add non-standard hooks to unittest for use in the "check" phase, when
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

# 00137 # ddb14da3b15a1f6cfda5ab94919f624c91294e00
# Skip tests within distutils failing when run in an rpmbuild
Patch137: 00137-skip-distutils-tests-that-fail-in-rpmbuild.patch

# 00143 # 4f886e3c73c66a62c1cf93d700f9f20016d7e533
# Fix the --with-tsc option on ppc64
#
# And rework it on 32-bit ppc to avoid aliasing violations
# See https://bugzilla.redhat.com/show_bug.cgi?id=698726
# Sent upstream as http://bugs.python.org/issue12872
Patch143: 00143-tsc-on-ppc.patch

# 00155 # 0ef7ae83073c1bbe610d4678ed56ae775fd6e174
# avoid allocating thunks in ctypes unless absolutely necessary
#
# Avoid allocating thunks in ctypes unless absolutely necessary, to avoid
# generating SELinux denials on "import ctypes" and "import uuid" when
# embedding Python within httpd
# See https://bugzilla.redhat.com/show_bug.cgi?id=814391
Patch155: 00155-avoid-ctypes-thunks.patch

# 00157 # 9e7157d043899e27b602630edb78d7c395ed2f8b
# Update uid/gid handling throughout the standard library
#
# uid_t and gid_t are unsigned 32-bit values, but existing code often passed
# them through C long values, which are signed 32-bit values on 32-bit
# architectures, leading to negative int objects for uid/gid values >= 2^31
# on 32-bit architectures.
#
# Introduce _PyObject_FromUid/Gid to convert uid_t/gid_t values to python
# objects, using int objects where the value will fit (long objects otherwise),
# and _PyArg_ParseUid/Gid to convert int/long to uid_t/gid_t, with -1 allowed
# as a special case (since this is given special meaning by the chown syscall)
#
# Update standard library to use this throughout for uid/gid values, so that
# very large uid/gid values are round-trippable, and -1 remains usable.
# See https://bugzilla.redhat.com/show_bug.cgi?id=697470
Patch157: 00157-uid-gid-overflows.patch

# 00160 # f69288aba24c43c506c3e90e2aa658e436e76e72
# Disable test_fs_holes in RPM build
#
# Python 3.3 added os.SEEK_DATA and os.SEEK_HOLE, which may be present in the
# header files in the build chroot, but may not be supported in the running
# kernel, hence we disable this test in an rpm build.
# Adding these was upstream issue http://bugs.python.org/issue10142
Patch160: 00160-disable-test_fs_holes-in-rpm-build.patch

# 00163 # 88e26259f7da12e17adb936815aa421d84c69f09
# Disable parts of test_socket in RPM build
#
# Some tests within test_socket fail intermittently when run inside Koji;
# disable them using unittest._skipInRpmBuild
Patch163: 00163-disable-parts-of-test_socket-in-rpm-build.patch

# 00170 # b83c202ebc888d0ce38cc7017663c824a1df5237
# In debug builds, try to print repr() when a C-level assert fails
#
# In debug builds, try to print repr() when a C-level assert fails in the
# garbage collector (typically indicating a reference-counting error
# somewhere else e.g in an extension module)
# The new macros/functions within gcmodule.c are hidden to avoid exposing
# them within the extension API.
# Sent upstream: http://bugs.python.org/issue9263
# See https://bugzilla.redhat.com/show_bug.cgi?id=614680
Patch170: 00170-gc-assertions.patch

# 00178 # a94ff354536408c95c354df86deb0a1633ac4c4d
# Don't duplicate various FLAGS in sysconfig values
#
# http://bugs.python.org/issue17679
# Does not affect python2 AFAICS (different sysconfig values initialization)
Patch178: 00178-dont-duplicate-flags-in-sysconfig.patch

# 00186 # e84b8f1eb8d092ffde6382b983133f60c8cbc0b8
# Fix for https://bugzilla.redhat.com/show_bug.cgi?id=1023607
#
# Previously, this fixed a problem where some *.py files were not being
# bytecompiled properly during build. This was result of py_compile.compile
# raising exception when trying to convert test file with bad encoding, and
# thus not continuing bytecompilation for other files.
# This was fixed upstream, but the test hasn't been merged yet, so we keep it
Patch186: 00186-dont-raise-from-py_compile.patch

# 00188 # d6d36f893f2d0413e259e73b3a6295b40488f009
# Fix lib2to3 tests when hashlib doesn't compile properly
#
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

# 00189 # 15a0492e41d13b4513befef87bc943f19498c09b
# Instead of bundled wheels, use our RPM packaged wheels
#
# We keep them in /usr/share/python-wheels
Patch189: 00189-use-rpm-wheels.patch
# The following versions of setuptools/pip are bundled when this patch is not applied.
# The versions are written in Lib/ensurepip/__init__.py, this patch removes them.
# When the bundled setuptools/pip wheel is updated, the patch no longer applies cleanly.
# In such cases, the patch needs to be amended and the versions updated here:
%global pip_version 9.0.1
%global setuptools_version 28.8.0

# 00205 # acb31cbf04decda6abbf87ab7682dfcba07433c8
# Make LIBPL respect lib64
#
# LIBPL variable in makefile takes LIBPL from configure.ac
# but the LIBPL variable defined there doesn't respect libdir macro
Patch205: 00205-make-libpl-respect-lib64.patch

# 00264 # 7abc0ebe38ad77b08cde6d3e4914e0e724154d89
# Fix test failing on aarch64
#
# test_pass_by_value was added in Python 3.5.4 and on aarch64
# it is catching an error that was there, but wasn't tested before.
# Since the Python 3.5 branch is on security bug fix mode only
# we backport the fix from the master branch.
# Fixed upstream: http://bugs.python.org/issue29804
Patch264: 00264-fix-test-failing-on-aarch64.patch

# 00270 # b71de510b1d74e9c8952ccc73712c54ef181325b
# Fix test_alpn_protocols from test_ssl
#
# openssl > 1.1.0f changed the behaviour of the ALPN hook.
# Fixed upstream: http://bugs.python.org/issue30714
Patch270: 00270-fix-ssl-alpn-hook-test.patch

# 00273 # 13dac13ccb8b184ec60d3ef6920ec24cba4bdb79
# Skip test_float_with_comma, which fails in Koji with UnicodeDecodeError
#
# See https://bugzilla.redhat.com/show_bug.cgi?id=1484497
# Reported upstream: https://bugs.python.org/issue31900
Patch273: 00273-skip-float-test.patch

# 00290 # 2f09d1fb6b997ff7e57244628b8d7cd8ac6a2c11
# Include crypt.h for declaration of crypt
#
# Not every target system may provide a crypt() function in its stdlibc
# and may use an external or replacement library, like libxcrypt, for
# providing such functions.
# Fixed upstream: https://bugs.python.org/issue32635
Patch290: 00290-cryptmodule-Include-crypt.h-for-declaration-of-crypt.patch

# 00315 # 3958b022be96dd973bf0f0ac81a6411b5553649f
# Fix mktime() error in test_email
#
# Fix mktime() overflow error in test_email: run
# test_localtime_daylight_true_dst_true() and
# test_localtime_daylight_false_dst_true() with a specific timezone.
#
# http://bugs.python.org/issue35317
# https://bugzilla.redhat.com/show_bug.cgi?id=1652843
Patch315: 00315-test_email-mktime.patch

# 00343 # 058ff9673b969960dd94fe336cc2e93ff8a1c675
# Fix test_faulthandler on GCC 10
#
# bpo-38965: Fix faulthandler._stack_overflow() on GCC 10
# Fixed upstream and backported from the 3.7 branch:
# https://bugs.python.org/issue38965
# https://github.com/python/cpython/commit/f4a21d3b239bf4f4e4e2a8a5936b9b040645b246
#
# bpo-21131: Fix faulthandler.register(chain=True) stack (GH-15276)
# https://bugs.python.org/issue21131
# https://github.com/python/cpython/commit/ac827edc493d3ac3f5b9b0cc353df1d4b418a9aa
Patch343: 00343-faulthandler-gcc10.patch

# 00348 # 4665197982c61e99325fbdf5c737550650ebdcb3
# Always disable lchmod on Linux.
#
# Backport of commit, upstream is doing only security fixes for python35
# https://bugs.python.org/issue34652
# https://github.com/python/cpython/commit/40caa05fa4d1810a1a6bfc34e0ec930c351089b7
Patch348: 00348-always-disable-lchmod.patch

# 00353 # d246570e993ea9c55de96d39450b5cb12756a478
# Original names for architectures with different names downstream
#
# https://fedoraproject.org/wiki/Changes/Python_Upstream_Architecture_Names
#
# Pythons in RHEL/Fedora used different names for some architectures
# than upstream and other distros (for example ppc64 vs. powerpc64).
# This was patched in patch 274, now it is sedded if %%with legacy_archnames.
#
# That meant that an extension built with the default upstream settings
# (on other distro or as an manylinux wheel) could not been found by Python
# on RHEL/Fedora because it had a different suffix.
# This patch adds the legacy names to importlib so Python is able
# to import extensions with a legacy architecture name in its
# file name.
# It work both ways, so it support both %%with and %%without legacy_archnames.
#
# WARNING: This patch has no effect on Python built with bootstrap
# enabled because Python/importlib_external.h is not regenerated
# and therefore Python during bootstrap contains importlib from
# upstream without this feature. It's possible to include
# Python/importlib_external.h to this patch but it'd make rebasing
# a nightmare because it's basically a binary file.
Patch353: 00353-architecture-names-upstream-downstream.patch

# (New patches go here ^^^)
#
# When adding new patches to "python" and "python3" in Fedora, EL, etc.,
# please try to keep the patch numbers in-sync between all specfiles.
#
# More information, and a patch number catalog, is at:
#
#     https://fedoraproject.org/wiki/SIGs/Python/PythonPatches


# ======================================================
# Additional metadata, and subpackages
# ======================================================

# We'll not provide this, on purpose
# No package in Fedora shall ever depend on this
# Provides: python(abi) = %%{pybasever}
%global __requires_exclude ^python\\(abi\\) = 3\\..$
%global __provides_exclude ^python\\(abi\\) = 3\\..$

%if %{with rpmwheels}
Requires: python-setuptools-wheel
Requires: python-pip-wheel
%else
Provides: bundled(python3dist(pip)) = %{pip_version}
Provides: bundled(python3dist(setuptools)) = %{setuptools_version}
%endif

%description
Python %{pybasever} package for developers.

This package exists to allow developers to test their code against an older
version of Python. This is not a full Python stack and if you wish to run
your applications with Python %{pybasever}, see other distributions
that support it, such as CentOS or RHEL with Software Collections
or older Fedora releases.


# ======================================================
# The prep phase of the build:
# ======================================================

%prep
%gpgverify -k2 -s1 -d0
%autosetup -S git_am -N -n Python-%{upstream_version}

# Apply initial patches manually
%apply_patch -q %{PATCH1}

%if 0%{?with_systemtap}
%apply_patch -q %{PATCH55}
%endif

%if "%{_lib}" == "lib64"
%apply_patch -q %{PATCH102}
%endif

%apply_patch -q %{PATCH111}
%apply_patch -q %{PATCH132}
%apply_patch -q %{PATCH137}
%apply_patch -q %{PATCH143}
%apply_patch -q %{PATCH155}
%apply_patch -q %{PATCH157}
%apply_patch -q %{PATCH160}
%apply_patch -q %{PATCH163}
%apply_patch -q %{PATCH170}
%apply_patch -q %{PATCH178}
%apply_patch -q %{PATCH186}
%apply_patch -q %{PATCH188}

%if %{with rpmwheels}
%apply_patch -q %{PATCH189}
rm Lib/ensurepip/_bundled/*.whl
%endif

# Apply the remaining patches
%autopatch -m 190

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

## Disabling hashlib patch for now as it needs to be reimplemented
## for OpenSSL 1.1.0.
# Don't build upstream Python's implementation of these crypto algorithms;
# instead rely on _hashlib and OpenSSL.
#
# For example, in our builds hashlib.md5 is implemented within _hashlib via
# OpenSSL (and thus respects FIPS mode), and does not fall back to _md5
# TODO: there seems to be no OpenSSL support in Python for sha3 so far
# when it is there, also remove _sha3/ dir
#for f in md5module.c sha1module.c sha256module.c sha512module.c; do
#    rm Modules/$f
#done

# Currently (2010-01-15), http://docs.python.org/library is for 2.6, and there
# are many differences between 2.6 and the Python 3 library.
#
# Fix up the URLs within pydoc to point at the documentation for this
# MAJOR.MINOR version:
#
sed --in-place \
    --expression="s|http://docs.python.org/library|http://docs.python.org/%{pybasever}/library|g" \
    Lib/pydoc.py || exit 1

# When we use the legacy arch names, we need to change them in configure and configure.ac
%if %{with legacy_archnames}
sed -i configure configure.ac \
    -e 's/\b%{platform_triplet_upstream}\b/%{platform_triplet_legacy}/'
%endif


# ======================================================
# Configuring and building the code:
# ======================================================

%build

# The build process embeds version info extracted from the Git repository
# into the Py_GetBuildInfo and sys.version strings.
# Our Git repository is artificial, so we don't want that.
# Tell configure to not use git.
export HAS_GIT=not-found

topdir=$(pwd)
export CFLAGS="$RPM_OPT_FLAGS -D_GNU_SOURCE -fPIC -fwrapv"
export CXXFLAGS="$RPM_OPT_FLAGS -D_GNU_SOURCE -fPIC -fwrapv"
export CPPFLAGS="`pkg-config --cflags-only-I libffi`"
export OPT="$RPM_OPT_FLAGS -D_GNU_SOURCE -fPIC -fwrapv"
export LINKCC="gcc"
export CFLAGS="$CFLAGS `pkg-config --cflags openssl`"
export LDFLAGS="$RPM_LD_FLAGS `pkg-config --libs-only-L openssl`"


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

  # Regenerate generated importlib frozen modules (see patch 353)
  %make_build EXTRA_CFLAGS="$CFLAGS $MoreCFlags" regen-importlib

  %make_build EXTRA_CFLAGS="$CFLAGS $MoreCFlags"

  popd
  echo FINISHED: BUILD OF PYTHON FOR CONFIGURATION: $ConfDir
}

# Use "BuildPython" to support building with different configurations:

%if 0%{?with_debug_build}
BuildPython debug \
  python-debug \
  python%{pybasever}-debug \
%ifarch %{ix86} x86_64 ppc %{power64}
  "--with-pydebug --with-tsc --without-ensurepip" \
%else
  "--with-pydebug --without-ensurepip" \
%endif
  false \
  -O0
%endif # with_debug_build

BuildPython optimized \
  python \
  python%{pybasever} \
%ifarch %{ix86} x86_64
  "--without-ensurepip --enable-optimizations" \
%else
   "--without-ensurepip" \
%endif
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

  %make_install EXTRA_CFLAGS="$MoreCFlags"

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

rm ${RPM_BUILD_ROOT}%{_bindir}/2to3

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

%ifarch %{power64} s390x x86_64 ia64 alpha sparc64 aarch64 %{mips64}
%global _pyconfig_h %{_pyconfig64_h}
%else
%global _pyconfig_h %{_pyconfig32_h}
%endif

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
# compile *.pyc
find %{buildroot} -type f -a -name "*.py" -print0 | \
    LD_LIBRARY_PATH="%{buildroot}%{dynload_dir}/:%{buildroot}%{_libdir}" \
    PYTHONPATH="%{buildroot}%{_libdir}/python%{pybasever} %{buildroot}%{_libdir}/python%{pybasever}/site-packages" \
    xargs -0 %{buildroot}%{_bindir}/python%{pybasever} -O -c 'import py_compile, sys; [py_compile.compile(f, dfile=f.partition("%{buildroot}")[2], optimize=opt) for opt in range(3) for f in sys.argv[1:]]' || :

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
%ifarch %{power64} s390x x86_64 ia64 alpha sparc64 aarch64 %{mips64}
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
rm %{buildroot}%{_bindir}/*3
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

# For ppc64 we need a larger stack than default (rhbz#1292462)
%ifarch %{power64}
  ulimit -a
  ulimit -s 16384
%endif

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
  # all SSL related tests are skipped
  #   see https://mail.python.org/archives/list/python-dev@python.org/message/3Z6X4LPSNRHHW4QPLLAVSNYY6CS6DDNR/
  WITHIN_PYTHON_RPM_BUILD= \
  LD_LIBRARY_PATH=$ConfDir $ConfDir/python -m test.regrtest \
    --verbose --findleaks \
    -x test_distutils \
    %ifarch ppc64le aarch64
    -x test_faulthandler \
    %endif
    %ifarch %{mips64}
    -x test_ctypes \
    %endif
    %ifarch %{power64} s390 s390x armv7hl aarch64 %{mips}
    -x test_gdb \
    %endif
    -x test_asyncio \
    -x test_ftplib \
    -x test_httplib \
    -x test_poplib \
    -x test_ssl\
    -x test_urllib2_localnet \

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
%exclude /usr/lib/debug%{_libdir}/__pycache__/libpython%{pybasever}m.so.1.0.debug-gdb.cpython-%{pyshortver}.*py*
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
* Mon Oct 05 2020 Miro Hrončok <mhroncok@redhat.com> - 3.5.10-2
- Use upstream architecture names on Fedora 34+
- https://fedoraproject.org/wiki/Changes/Python_Upstream_Architecture_Names

* Mon Sep 07 2020 Tomas Hrnciar <thrnciar@redhat.com> - 3.5.10-1
- Update to 3.5.10

* Tue Aug 25 2020 Tomas Hrnciar <thrnciar@redhat.com> - 3.5.10rc1-1
- Update to 3.5.10rc1

* Wed Aug 12 2020 Petr Viktorin <pviktori@redhat.com> - 3.5.9-9
- In sys.version and initial REPL message, list the source commit as "default"

* Thu Aug 06 2020 Lumír Balhar <lbalhar@redhat.com> - 3.5.9-8
- Add support for upstream architectures' names (patch 353)

* Tue Aug 04 2020 Miro Hrončok <mhroncok@redhat.com> - 3.5.9-7
- Avoid infinite loop when reading specially crafted TAR files (CVE-2019-20907)
Resolves: rhbz#1856481
- Resolve hash collisions for Pv4Interface and IPv6Interface (CVE-2020-14422)
Resolves: rhbz#1854926

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed May 06 2020 Miro Hrončok <mhroncok@redhat.com> - 3.5.9-5
- Rename from python35 to python3.5

* Tue May 05 2020 Tomas Hrnciar <thrnciar@redhat.com> - 3.5.9-4
- Fix a build/test failure with glibc 2.31.9000+ (#1819759)

* Wed Feb 12 2020 Miro Hrončok <mhroncok@redhat.com> - 3.5.9-3
- Update the ensurepip module to work with setuptools >= 45

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 25 2019 Miro Hrončok <mhroncok@redhat.com> - 3.5.9-1
- Update to 3.5.9 (version number update only)

* Wed Oct 30 2019 Miro Hrončok <mhroncok@redhat.com> - 3.5.8-2
- Use the correct upstream tarball
- https://mail.python.org/archives/list/python-dev@python.org/message/OYNQS2BZYABXACBRHBHV4RCEPQU5R6EP/

* Tue Oct 29 2019 Miro Hrončok <mhroncok@redhat.com> - 3.5.8-1
- Update to 3.5.8

* Sat Oct 12 2019 Miro Hrončok <mhroncok@redhat.com> - 3.5.8~rc2-1
- Update to 3.5.8rc2

* Mon Sep 09 2019 Miro Hrončok <mhroncok@redhat.com> - 3.5.8~rc1-1
- Update to 3.5.8rc1

* Sat Aug 10 2019 Miro Hrončok <mhroncok@redhat.com> - 3.5.7-4
- Build against OpenSSL 1.1.x, not 1.0.x

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 02 2019 Victor Stinner <vstinner@redhat.com> - 3.5.7-2
- Skip test_ssl and test_asyncio tests failing with OpenSSL 1.1.1 (rhbz#1685609)

* Tue Mar 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.5.7-1
- Update to 3.5.7

* Tue Mar 05 2019 Miro Hrončok <mhroncok@redhat.com> - 3.5.7~rc1-1
- Update to 3.5.7rc1

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.5.6-6
- Rebuild for readline 8.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Björn Esser <besser82@fedoraproject.org> - 3.5.6-4
- Rebuilt for libcrypt.so.2 (#1666033)

* Mon Sep 24 2018 Miro Hrončok <mhroncok@redhat.com> - 3.5.6-3
- Security fix for CVE-2018-14647 (#1631822)

* Tue Aug 21 2018 Miro Hrončok <mhroncok@redhat.com> - 3.5.6-2
- Use RPM built wheels of pip and setuptools in ensurepip instead of bundled ones

* Sun Aug 05 2018 Miro Hrončok <mhroncok@redhat.com> - 3.5.6-1
- Rebased to version 3.5.6

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 23 2018 Miro Hrončok <mhroncok@redhat.com> - 3.5.5-2
- Fix multiprocessing regression on newer glibcs
- Enable test_multiprocessing_fork(server) and _spawn again
Resolves: rhbz#1569933

* Fri Apr 20 2018 Miro Hrončok <mhroncok@redhat.com> - 3.5.5-1
- Rebased to version 3.5.5
- Do not ship the Tools directory
- Skip test_multiprocessing_fork(server) and _spawn for now
- Skip test_rapid_restart on non x86 arches
- Skip test_buffer on ppc64le

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 3.5.4-3
- Rebuilt for switch to libxcrypt

* Tue Dec 05 2017 Miro Hrončok <mhroncok@redhat.com> - 3.5.4-2
- Fix for CVE-2017-1000158
- rhbz#1519603: https://bugzilla.redhat.com/show_bug.cgi?id=1519603

* Mon Oct 30 2017 Charalampos Stratakis <cstratak@redhat.com> - 3.5.4-1
- Rebased to version 3.5.4

* Mon Aug 14 2017 David "Sanqui" Labský <dlabsky@redhat.com> - 3.5.3-5
- Drop unused db4-devel dependency

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 26 2017 Charalampos Stratakis <cstratak@redhat.com> - 3.5.3-2
- Fix test_alpn_protocols from test_ssl

* Thu May 11 2017 Charalampos Stratakis <cstratak@redhat.com> - 3.5.3-1
- Rebased to version 3.5.3 from F25
- Enable profile guided optimizations for x86_64 and i686 architectures
- Make pip installable in a new venv when using the --system-site-packages flag
- Fix syntax error in %%py_byte_compile macro
- Add patch 259 to work around magic number bump in Python 3.5.3

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 3.5.2-8
- Rebuild for readline 7.x

* Tue Jan 10 2017 Charalampos Stratakis <cstratak@redhat.com> - 3.5.2-7
- Require glibc >= 2.24.90-26 (rhbz#1410644)

* Thu Jan 05 2017 Miro Hrončok <mhroncok@redhat.com> - 3.5.2-6
- Don't blow up on EL7 kernel (random generator) (rhbz#1410175, rhbz#1410187)

* Sun Jan 01 2017 Miro Hrončok <mhroncok@redhat.com> - 3.5.2-5
- Update description

* Sun Jan 01 2017 Miro Hrončok <mhroncok@redhat.com> - 3.5.2-4
- Add patch for OpenSSL 1.1.0

* Fri Oct 21 2016 Miro Hrončok <mhroncok@redhat.com> - 3.5.2-3
- Reword the description

* Tue Sep 13 2016 Miro Hrončok <mhroncok@redhat.com> - 3.5.2-2
- Fixed .pyc bytecompilation
- Remove unused configure flags

* Mon Aug 15 2016 Tomas Orsava <torsava@redhat.com> - 3.5.2-1
- Rebased to version 3.5.2 from F26

* Tue Aug 09 2016 Miro Hrončok <mhroncok@redhat.com> - 3.5.1-14
- Imported from F25

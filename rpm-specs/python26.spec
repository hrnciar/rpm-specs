#define __python_ver 26
%global unicode ucs4

%global _default_patch_fuzz 2

%global pybasever 2.6
%global pyshortver 26
%global main_python 0
%global python python%{pyshortver}
%global pylibdir %{_libdir}/python%{pybasever}
%global tools_dir %{pylibdir}/Tools
%global demo_dir %{pylibdir}/Demo
%global doc_tools_dir %{pylibdir}/Doc/tools
%global dynload_dir %{pylibdir}/lib-dynload
%global site_packages %{pylibdir}/site-packages

# Python's configure script defines SOVERSION, and this is used in the Makefile
# to determine INSTSONAME, the name of the libpython DSO:
#   LDLIBRARY='libpython$(VERSION).so'
#   INSTSONAME="$LDLIBRARY".$SOVERSION
# We mirror this here in order to make it easier to add the -gdb.py hooks.
# (if these get out of sync, the payload of the libs subpackage will fail
# and halt the build)
%global py_SOVERSION 1.0
%global py_INSTSONAME libpython%{pybasever}.so.%{py_SOVERSION}

%global with_gdb_hooks 1

%global with_systemtap 1

%global with_valgrind 1
%global with_valgrind_config_opt --with-valgrind

# Turn this to 0 to turn off the "check" phase:
%global run_selftest_suite 1

# Disable automatic bytecompilation. The python2.6 binary is not yet be
# available in /usr/bin when Python is built. Also, the bytecompilation fails
# on files that test invalid syntax.
%undefine py_auto_byte_compile


# Disable strict symbol checks in the link editor.
# See: https://src.fedoraproject.org/rpms/redhat-rpm-config/c/078af19
%undefine _strict_symbol_defs_build


Summary: Version %{pybasever} of the Python programming language
Name: %{python}
Version: 2.6.9
Release: 22%{?dist}
License: Python
Source: http://www.python.org/ftp/python/%{version}/Python-%{version}.tar.xz


# We install a collection of hooks for gdb that make it easier to debug
# executables linked against libpython (such as /usr/lib/python itself)
#
# These hooks are implemented in Python itself
#
# gdb-archer looks for them in the same path as the ELF file, with a -gdb.py suffix.
# We put them in the debuginfo package by installing them to e.g.:
#  /usr/lib/debug/usr/lib/libpython2.6.so.1.0.debug-gdb.py
#
# See https://fedoraproject.org/wiki/Features/EasierPythonDebugging for more
# information
#
# Downloaded from:
#  http://bugs.python.org/issue8032
# This is Tools/gdb/libpython.py from v5 of the patch
Source1: python-gdb.py

# Systemtap tapset to make it easier to use the systemtap static probes,
# allowing the use of "python.function.entry" and "python.function.return",
# rather than requiring scripts to spell out the full path to the python
# library.
# This is actually a template; LIBRARY_PATH will get fixed up during install:
Source3: libpython.stp

# Example systemtap script using the tapset: shows the hierarchy of pure-python
# function calls and returns:
Source4: systemtap-example.stp

# Another example systemtap script that uses the tapset: shows a "top"-like
# view of python function calls:
Source5: pyfuntop.stp

Source6: modulator
Source7: pynche

Source8: ordereddict-1.2-py2.6.egg-info

Patch0: python-2.6.2-config.patch
Patch1: Python-2.2.1-pydocnogui.patch

# Fixup configure.in and setup.py to build against system expat library.
# Adapted from http://svn.python.org/view?view=rev&revision=77169
Patch3: python-2.6.2-with-system-expat.patch

Patch4: python-2.5-cflags.patch

Patch6: python-2.5.1-plural-fix.patch
Patch7: python-2.5.1-sqlite-encoding.patch

Patch10: python-2.6.2-binutils-no-dep.patch
Patch11: python-2.5.1-codec-ascii-tolower.patch

Patch13: python-2.5.1-socketmodule-constants.patch
Patch14: python-2.5.1-socketmodule-constants2.patch

Patch16: python-2.6-rpath.patch

# Fix distutils to follow the Fedora/RHEL/CentOS policies of having .pyo files
Patch51: python-2.6-distutils_rpm.patch

# Automatically disable arena allocator when run under valgrind:
# From http://bugs.python.org/issue2422
#   http://bugs.python.org/file9872/disable-pymalloc-on-valgrind-py26.patch
# with the "configure" part removed; appears to be identical to the version committed to 2.7
Patch52: disable-pymalloc-on-valgrind-py26.patch

# lib64 patches
Patch101: python-2.3.4-lib64-regex.patch
Patch102: python-2.6-lib64.patch

# SELinux patches
#Patch110: python-2.6.5-ctypes-noexecmem.patch

# Patch the Makefile.pre.in so that the generated Makefile doesn't try to build
# a libpythonMAJOR.MINOR.a (bug 550692):
Patch111: python-2.6.2-no-static-lib.patch

# Add flags for statvfs.f_flag to the constant list in posixmodule (i.e. "os")
# (rhbz:553020); partially upstream as http://bugs.python.org/issue7647
Patch112: python-2.6.2-statvfs-f_flag-constants.patch

# Fix an incompatibility between pyexpat and the system expat-2.0.1 that led to
# a segfault running test_pyexpat.py (rhbz:583931)
# Sent upstream as http://bugs.python.org/issue9054
Patch117: python-2.6.2-fix-expat-issue9054.patch

# Support OpenSSL FIPS mode:
# - handle failures from OpenSSL (e.g. on attempts to use MD5 in a
#   FIPS-enforcing environment)
# - add a new "usedforsecurity" keyword argument to the various digest
#   algorithms in hashlib so that you can whitelist a callsite with
#   "usedforsecurity=False"
# (sent upstream for python 3 as http://bugs.python.org/issue9216; this is a
# backport to python 2.6)
# - enforce usage of the _hashlib implementation: don't fall back to the _md5
#   and _sha* modules (leading to clearer error messages if fips selftests
#   fail)
# - don't build the _md5 and _sha* modules; rely on the _hashlib implementation
#   of hashlib
Patch119: python-2.6.5-hashlib-fips.patch

# Fix a 2.7-ism accidentally added upstream into 2.6.6's selftest suite that
# leads to a failure in test_posix when run as root
# Sent upstream as http://bugs.python.org/issue10585
Patch120: python-2.6.6-fix-test_setgroups.patch

# Fix dbm.contains on ppc64 and s390x (rhbz#626756)
# Sent upstream as http://bugs.python.org/issue9687
Patch121: fix-dbm_contains-on-64bit-bigendian.patch

# Add various lib2to3/tests/data and various directories below it to
# Makefile.pre.in's LIBSUBDIRS, so that they get installed, for use by the
# "test" subpackage (rhbz#625395)
# Based on upstream r71740 vs r71395, but also removing some usages of "with"
# with multiple context managers from py2_test_grammar (as this was introduced in
# 3.1/2.7):
Patch122: python-2.6.6-install-missing-lib2to3-test-files.patch

# test_commmands fails on SELinux systems due to a change in the output
# of "ls" (http://bugs.python.org/issue7108) (rhbz#625393)
Patch123: fix-test_commands-expected-ls-output-issue7108.patch

# Make "pydoc -k" more robust in the face of broken modules
# (rhbz#603073; patch sent upstream as http://bugs.python.org/issue7425 )
Patch124: make-pydoc-more-robust-001.patch

# Use an ephemeral port for IDLE, enabling multiple instances to be run
# (cherrypick upstream r71126 for http://bugs.python.org/issue1529142
# rhbz#639222)
Patch125: use-ephemeral-port-for-IDLE.patch

# Systemtap support: add statically-defined probe points "function__entry" and
# "function__return" to the bytecode dispatch loop (rhbz#569695)
Patch126: python-2.6.6-systemtap.patch

# Port subprocess to use the "poll" system call (via "select.poll"), rather
# than the "select" system call (via "select.select"), avoiding an arbitrary
# limit on the number of filedescriptors that can be monitored, and thus on the
# number of subprocesses.
#
# Upstream issue http://bugs.python.org/issue3392
#
# This is a backport of upstream r73825, r73916 and r73818 from "trunk" to 2.6
# (rhbz#650588)
Patch127: python-2.6.6-subprocess-poll.patch

# Allow the "no_proxy" env variable to override "ftp_proxy" in urllib2, by
# ensuring that req.host is set in ProxyHandler.proxy_open() (rhbz#637895)
Patch128: python-2.6.6-urllib2-ftp-no-proxy.patch

# Try to print repr() when an C-level assert fails in the garbage collector,
# typically indicating a reference-counting error somewhere else (e.g in an
# extension module)
# Backported to 2.6 from a patch I sent upstream for py3k
#   http://bugs.python.org/issue9263  (rhbz#614680)
# hiding the proposed new macros/functions within gcmodule.c to avoid exposing
# them within the extension API.
#Patch129: python-2.6.6-gc-assertions.patch

# Prevent _sqlite3.so being built with a redundant RPATH of _libdir:
# (rhbz#634944)
Patch130: python-2.6.6-remove-sqlite-rpath.patch


# Add an optional "timeout" argument to the subprocess module (rhbz#567229)
#
# This is a non-standard extension to Python 2.6, but is based on an upstream
# proposal being tracked for Python 3 as:
#    http://bugs.python.org/issue5673
# 
# The "timeout" argument is a number of seconds, which can be an integer or a
# float (though there are no precision guarantees)
#
# This change adds the "timeout" argument to the following API entrypoints:
#   subprocess.call
#   Popen.communicate
#   Popen.wait
#
# A TimeoutExpired exception will be raised after the given number of seconds
# elapses, if the call has not yet returned.
#
# Based on upstream subprocess-timeout-v5.patch, with fixes for
# assertStderrEqual, and marking the API as non-standard
Patch131: python-2.6.6-subprocess-timeout.patch

# Fix a regression in 2.6.6 relative to 2.6.5 in urllib2
# (ased on upstream SVN commit 84207; rhbz#669847)
Patch132: python-2.6.6-fix-urllib2-AbstractBasicAuthHandler.patch

# Add workaround for bug in Rhythmbox exposed by 2.6.6 (rhbz#684991)
Patch133: python-2.6.6-rhythmbox-workaround.patch

# Fix incompatibility between 2.6.6 and M2Crypto.SSL.SSLTimeoutError from our
# m2crypto-0.18-timeouts.patch (rhbz#681811)
Patch134: python-2.6.6-fix-EINTR-check-for-nonstandard-exceptions.patch

# A new test in 2.6.6 fails on 64-bit big-endian architectures (rhbz#677392)
Patch135: python-test_structmembers.patch

# Backport of improvements to the forthcoming Python 3.3's "crypt" module,
# adding precanned ways of salting a password  (rhbz#681878)
# Based on r88500 patch to py3k from forthcoming Python 3.3
# plus 6482dd1c11ed, 0586c699d467, 62994662676a, plus edits to docstrings to
# note that this additional functionality is not standard within 2.6
Patch136: python-2.6.6-crypt-module-salt-backport.patch

# Fix race condition in parallel make that could lead to graminit.c failing
# to compile, or linker errors with "undefined reference to
# `_PyParser_Grammar'":
# See e.g. http://bugs.python.org/issue10013
Patch137: python-2.6.6-fix-parallel-make.patch

# Fix for CVE-2011-1015, based on
# http://hg.python.org/cpython/raw-rev/c6c4398293bd
Patch139: python-2.6.6-CVE-2011-1015.patch

# Backport the fix for transient failures in multiprocess's
# forking.Process.poll() from 2.7 to 2.6 (rhbz#685234):
Patch141: python-2.6.6-fix-transient-multiprocessing-failures.patch

# Port _multiprocessing.Connection.poll() to use the "poll" syscall, rather
# than "select", allowing large numbers of subprocesses (rhbz#713082)
Patch142: python-2.6.6-use-poll-for-multiprocessing-socket-connection.patch

# Backport to 2.6 of the upstream fix allowing getpass.getpass() to be
# interrupted using Ctrl-C or Ctrl-Z (rhbz#689794)
Patch143: python-2.6.6-allow-getpass-to-be-interrupted.patch

# Memory leak fixes for readline module (rhbz#699740)
#
#   Based on upstream fix for upstream issue #9450:
Patch144: python-2.6.6-readline-introduce-py-free-history-entry.patch
#
#   Based on upstream fix for upstream issue #8065; fixes leaks in
# readline.get_history_length() and readline.get_history_item():
Patch145: python-2.6.6-readline-introduce-get-history-length.patch

# subprocess.Popen's communicate() could sometimes fail on short-lived
# processes with:  OSError: [Errno 32] Broken pipe
# Backport the fix for this from 2.7 to 2.6.6: (rhbz#667431)
Patch146: python-2.6.6-Popen-communicate-EPIPE.patch

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
Patch147: python-2.6.6-uid-gid-overflows.patch

# Update distutils.sysconfig so that if CFLAGS is defined in the environment,
# when building extension modules, it is appended to the full compilation
# flags from Python's Makefile, rather than instead reducing the compilation
# flags to the subset within OPT and adding it to those:
# (rhbz#727364)
Patch148: python-2.6.6-distutils-cflags.patch

# Patch distutils to create ~/.pypirc securely
# (http://bugs.python.org/issue13512; CVE-2011-4944):
Patch152: python-2.6.6-CVE-2011-4944.patch

# ...and patch configure.in to verify that XML_SetHashSalt is present within
# the expat library:
Patch154: python-2.6.6-check-for-XML_SetHashSalt.patch

# Add an explicit RPATH to pyexpat.so pointing at the directory
# containing the system expat (which has the extra XML_SetHashSalt
# symbol), to avoid an ImportError with a link error if there's an
# LD_LIBRARY_PATH containing a "vanilla" build of expat (without the
# symbol) (rhbz#833271):
Patch155: python-2.6.6-add-RPATH-to-pyexpat.patch

# Avoid allocating thunks in ctypes unless absolutely necessary, to avoid
# generating SELinux denials on "import ctypes" and "import uuid" when
# embedding Python within httpd (rhbz#814391)
Patch156: python-2.6.6-avoid-ctypes-thunks.patch

# Avoid infinite loop in logging.handlers.SysLogHandler with eventlet when
# the syslog daemon is stopped, due to missing close of socket in error
# handling.  Cherrypick of upstream fix for http://bugs.python.org/issue15179
# (rhbz#835460)
Patch157: python-2.6.6-fix-SysLogHandler-error-handling.patch

# Fix subprocess to call wait() with timeout argument only if calling
# functions were called with this argument in the first place
# (resp. they have timeout != None).
# See https://bugzilla.redhat.com/show_bug.cgi?id=958868
Patch158: python-2.6.6-fix-subprocess-timeout.patch

# Add a "-p" option to pathfix.py, to preserve the mtime of the input files
# (to help keep equal .pyc/.pyo files across architectures)
# py3k version sent upstream as http://bugs.python.org/issue10140
Patch159: python-2.6.6-pathfix-preserve-timestamp.patch

# Remove BOM insertion code from SysLogHandler that causes messages to be
# treated as EMERG level (rhbz#845802)
Patch160: python-2.6.6-prepends-UTF8-BOM-syslog-messages.patch

# Fix Python not reading Alternative Subject Names from some SSL
# certificates (rhbz#928390)
Patch161: python-2.6.6-SSLSocket-getpeercert-empty-SAN.patch

# Don't let failed incoming SSL connection stay open forever
# (rhbz#960168)
Patch162: python-2.6.6-ssl-connection-stays-open.patch

# Add an explicit RPATH to _elementtree.so pointing at the directory
# containing system expat (rhbz#962779)
Patch163: python-2.6.6-add-RPATH-to-elementtree.patch

# Backport of collections.OrderedDict from Python 2.7 (rhbz#929258)
Patch164: python-2.6.6-ordereddict-backport.patch

# Change unradom to throw proper exception
# (rhbz#893034)
Patch165: python-2.6.6-urandom-proper-exception.patch

# Add try-except to catch OSError in WatchedFileHandler's emit function
# (rhbz#919163)
Patch166: python-2.6.6-logging-watchedfilehandler.patch

# Add wrapper for select.select function to restart a system call interrupted 
# by EINTR
# (rhbz#948025)
Patch167: python-2.6.6-socketserver-eintr-retry.patch

# urlparse should parse query and fragment for arbitrary schemes
# (rhbz#978129)
# Note: this fix consists of two patches: the first one introduced regression
# and the second one fixes it
Patch168: python-2.6.6-urlparse-should-parse-fragments-for-arbitrary-schemes.patch
Patch169: python-2.6.6-readd-urlparse-removed-module-attributes.patch

# Fix sqlite3.Cursor.lastrowid under a Turkish locale.
# (rhbz#841937)
Patch170: python-2.6.6-Turkish-installation-fails.patch

# fix for _ssl's _get_peer_alt_names leaking memory
# http://bugs.python.org/issue13458
# (rhbz#1002983)
Patch172: python-2.6.6-ssl-memory-leak-_get_peer_alt_names.patch

# fix for subprocess.Popen.communicate() being broken by SIGCHLD handler
# http://bugs.python.org/issue9127
# rhbz#1065537
Patch173: python-2.6.6-fix-subprocess-Popen-communicate-broken-by-SIGCHLD.patch

# fix for iteration over files vith very long lines
# http://bugs.python.org/issue22526
# rhbz#794632
Patch174: python-2.6.6-fix-file-iteration-long-lines.patch

# make multiprocessing ignore EINTR
# http://bugs.python.org/issue17097
# rhbz#1180864
Patch175: python-2.6.6-multiprocessing-ignore-eintr.patch 

# add choices for sort option of cProfile for better output message
# http://bugs.python.org/issue23420
# rhbz#1160640
Patch176: python-2.6.6-cprofile-sort-option.patch

# make Popen.communicate catch EINTR error
# http://bugs.python.org/issue12493
# rhbz#1073165
Patch177: python-2.6.6-communicate-handle-eintr.patch

# let ConfigParser handle options without values
# rhbz#1031709
Patch178: python-2.6.6-have-ConfigParser-handle-options-without-values.patch

# 2.6 unittest doesnt have unittest.skip so sometimes the test is simply deleted
#########################
# MOCK FAILURES
#########################
# test_distutils:
#   test_get_outputs - ld can't find lpython2.6 - deleted
#   test_home_installation - recognize platform lib dir - fixed
# test_file:
#   testStdin -  seeks sys.stdin but doesn't work as expected in mock/brew - deleted
# test_socket
#   testSockName - gethostname doesn't work in mock/brew - skip
# test_subprocess
#   test_wait_when_sigchild_ignored - added optional subdir arg into test_support.py.findfile
##########################
# BREW SPECIFIC FAILURES
##########################
# test_socket, test_ftplib, test_asynchat, test_asyncore, test_httplib, test_poplib
#   multiple failures in brew because of missing socket.SO_REUSEPORT see rhbz#913732
# test_subprocess
#   test_leaking_fds_on_error failed because of the dir permissions in brew - fixed
# test_distutils:test_install
#   test_home_installation_scheme failed because of multilib support - fixed
Patch179: python-2.6.6-fix-and-skip-tests.patch

# Fix logging module error when multiprocessing module is not initialized
# http://bugs.python.org/issue8200
# https://bugzilla.redhat.com/show_bug.cgi?id=1204966
Patch180: python-2.6.6-fix-logging-module-init-when-multiprocessing-not-initialized.patch

# Fixes for CVE-2014-7185/4650/1912 CVE-2013-1752
# rhbz#1206572
Patch181: CVE-2014-7185.patch
Patch182: CVE-2014-4650.patch
Patch183: CVE-2014-1912.patch

# 00184
# Fix for https://bugzilla.redhat.com/show_bug.cgi?id=979696
# Fixes build of ctypes against libffi with multilib wrapper
# Python recognizes ffi.h only if it contains "#define LIBFFI_H",
# but the wrapper doesn't contain that, which makes the build fail
# We patch this by also accepting "#define ffi_wrapper_h"
Patch184: 00184-ctypes-should-build-with-libffi-multilib-wrapper.patch

# enable-deepcopy-with-instance-methods.patch
# Python Issue #1515
# Resolves: rhbz#1223037
Patch185: enable-deepcopy-with-instance-methods.patch

# Skip db related tests
Patch186: python26-skip-db-tests.patch

# 00212 #
# Fix test breakage with version 2.2.0 of Expat
# rhbz#1353918: https://bugzilla.redhat.com/show_bug.cgi?id=1353918
# FIXED UPSTREAM: http://bugs.python.org/issue27369
Patch212: 00212-fix-test-pyexpat-failure.patch

# Force all child threads to terminate in TestForkInThread, so no zombie
# processes get left behind with stalled threads which hang Python builds
# https://bugs.python.org/issue26456
Patch230: 00230-force-all-child-threads-to-terminate-in-TestForkInThread.patch

# Weaken callback count inequality
# Fixed upstream: http://bugs.python.org/issue20901
Patch231: weaken-callback-count-inequality.patch

# 00286 #
# CVE-2017-1000158
# Check & prevent integer overflow in PyString_DecodeEscape
# Fixed upstream: https://bugs.python.org/issue30657
Patch286: 00286-pystring-decodeescape-integer-overflow.patch

# 00287 #
# Not every target system may provide a crypt() function in its stdlibc
# and may use an external or replacement library, like libxcrypt, for
# providing such functions.
# Fixed upstream: https://bugs.python.org/issue32635
Patch287: 00287-cryptmodule-Include-crypt.h-for-declaration-of-crypt.patch

# 00289 #
# Disable automatic detection for the nis module
# (we handle it it in Setup.dist, see Patch0)
Patch289: 00289-disable-nis-detection.patch

# 00310 #
# CVE-2018-14647
# Use XML_SetHashSalt in _elementtree
# rhbz#1631822
# Fixed upstream https://bugs.python.org/issue34623
Patch310: 00310-use-xml-sethashsalt-in-elementtree.patch

BuildRequires: readline-devel, gmp-devel
BuildRequires: ncurses-devel, gdbm-devel, zlib-devel

%if 0%{?fedora} >= 26
BuildRequires: compat-openssl10-devel
%else
BuildRequires: openssl-devel
%endif

# CVE-2012-0876: we require a build of expat that contains the new symbol
# XML_SetHashSalt (added upstream in 2.1.0 without bumping SONAME, and
# backported in this version-release):
BuildRequires: expat-devel >= 2.0.1-10

BuildRequires: libGL-devel tk tix gcc-c++ libX11-devel glibc-devel
BuildRequires: bzip2 tar /usr/bin/find pkgconfig tcl-devel tk-devel
BuildRequires: tix-devel bzip2-devel sqlite-devel
BuildRequires: autoconf automake
BuildRequires: libffi-devel
%if 0%{?with_valgrind}
BuildRequires: valgrind-devel
%endif # with_valgrind

%if 0%{?with_systemtap}
BuildRequires: systemtap-sdt-devel
%global tapsetdir      /usr/share/systemtap/tapset
%endif

# For the nis module
BuildRequires: libnsl2-devel
BuildRequires: libtirpc-devel

# Something in the build system has python shebangs
# We'll use python2 to excute them
BuildRequires: python2
# And pathfix.py to switch the shebang
BuildRequires: %{_bindir}/pathfix.py
# This brings BR on python2 and python3, but meh...


# We don't want to provide this
# No package in Fedora shall ever depend on this
%global __requires_exclude ^python\\(abi\\) = 2\\..$
%global __provides_exclude ^python\\(abi\\) = 2\\..$

# People might want to dnf install pythonX.Y instead of pythonXY
Provides: python%{pybasever} = %{version}-%{release}

URL: http://www.python.org/

%description
Python %{pybasever} package for developers.

This package exists to allow developers to test their code against an older
version of Python. This is not a full Python stack and if you wish to run
your applications with Python %{pybasever}, see other distributions
that support it, such as CentOS or RHEL 6.


%prep
%setup -q -n Python-%{version}

%if 0%{?with_systemtap}
# Provide an example of usage of the tapset:
cp -a %{SOURCE4} .
cp -a %{SOURCE5} .
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

#
# Apply patches:
#
%patch0 -p1 -b .rhconfig
%patch3 -p1 -b .expat
%patch1 -p1 -b .no_gui

%patch4 -p1 -b .cflags

%patch6 -p1 -b .plural
%patch7 -p1

%if "%{_lib}" == "lib64"
%patch101 -p1 -b .lib64-regex
%patch102 -p1 -b .lib64
%endif

%patch10 -p1 -b .binutils-no-dep
%patch11 -p1 -b .ascii-tolower

%patch13 -p1 -b .socketmodule
%patch14 -p1 -b .socketmodule2

%patch16 -p1 -b .rpath

%patch51 -p1 -b .brprpm
%if 0%{?with_valgrind}
%patch52 -p1 -b .disable-pymalloc-on-valgrind
%endif

%ifarch alpha ia64
# 64bit, but not lib64 arches need this too...
%patch101 -p1 -b .lib64-regex
%endif

#patch110 -p1 -b .selinux
%patch111 -p1 -b .no-static-lib

%patch112 -p1 -b .statvfs-f-flag-constants

%patch117 -p0 -b .fix-expat-issue9054

%patch119 -p1 -b .hashlib-fips

%patch120 -p0

%patch121 -p0 -b .fix-dbm-contains-on-64bit-bigendian

%patch122 -p1 

%patch123 -p1

%patch124 -p0

%patch125 -p1

%if 0%{?with_systemtap}
%patch126 -p1 -b .systemtap
%endif

%patch127 -p1

%patch128 -p1

#patch129 -p1

%patch130 -p1

%patch131 -p1

%patch132 -p1

%patch133 -p1

%patch134 -p1

%patch135 -p0

%patch136 -p1
mv Modules/cryptmodule.c Modules/_cryptmodule.c

%patch137 -p1 -b .fix-parallel-make

%patch139 -p1

%patch141 -p1

%patch142 -p1

%patch143 -p1

%patch144 -p1 -b .readline-introduce-py-free-history-entry
%patch145 -p1 -b .readline-introduce-get-history-length

%patch146 -p1

%patch147 -p1

%patch148 -p1

%patch152 -p1

%patch154 -p1 -b .check-for-XML_SetHashSalt

%patch155 -p1 -b .add-RPATH-to-pyexpat

%patch156 -p1
%patch157 -p1

%patch158 -p1

%patch159 -p1

%patch160 -p0

%patch161 -p1

%patch162 -p2

%patch163 -p0

%patch164 -p1

%patch165 -p1

%patch166 -p1

%patch167 -p1

%patch168 -p1

%patch169 -p1

%patch170 -p1

%patch172 -p1

%patch173 -p1

%patch174 -p1

%patch175 -p1

%patch176 -p1

%patch177 -p1

%patch178 -p1

%patch179 -p1

%patch180 -p1

%patch181 -p1

%patch182 -p1

%patch183 -p1

%patch184 -p1

%patch185 -p1

%patch186 -p1

%patch212 -p1

%patch230 -p1

%patch231 -p1

%patch286 -p1

%patch287 -p1

%patch289 -p1

%patch310 -p1

# Don't build these crypto algorithms; instead rely on _hashlib and OpenSSL:
for f in md5module.c md5.c shamodule.c sha256module.c sha512module.c; do
    rm Modules/$f
done

# This shouldn't be necesarry, but is right now (2.2a3)
find -name "*~" |xargs rm -f

# Reset timestamps on .py files to that of the tarball, to minimize .pyc/.pyo
# differences between architectures:
find -name "*.py" -exec touch -r %{SOURCE0} "{}" \;

# Fix shebangs used in the build process
pathfix.py -pni %{_bindir}/python2 Parser/asdl_c.py

%build
topdir=`pwd`
export CFLAGS="$RPM_OPT_FLAGS -D_GNU_SOURCE -fPIC -fwrapv"
export CXXFLAGS="$RPM_OPT_FLAGS -D_GNU_SOURCE -fPIC -fwrapv"
export CPPFLAGS="`pkg-config --cflags-only-I libffi`"
export OPT="$RPM_OPT_FLAGS -D_GNU_SOURCE -fPIC -fwrapv"
export LINKCC="gcc"
if pkg-config openssl ; then
  export CFLAGS="$CFLAGS `pkg-config --cflags openssl`"
  export LDFLAGS="$LDFLAGS `pkg-config --libs-only-L openssl`"
fi
# Force CC
export CC=gcc
# For patches 3, 4, 52, 154 and 287 we need to get a newer
# configure generated out of configure.in
autoconf

# Patch 287 requires to regenerate the autoheader.
autoheader

# Preserve timestamps when installing, to minimize .pyc/.pyo differences
# across architectures:
export INSTALL="/usr/bin/install -p -c"

%configure \
    --enable-ipv6 \
    --enable-unicode=%{unicode} \
    --enable-shared \
    --with-system-ffi \
    --with-system-expat \
    %{?with_valgrind_config_opt} \
%if 0%{?with_systemtap}
  --with-dtrace \
  --with-tapset-install-dir=%{tapsetdir} \
%endif
   %{nil}

make OPT="$CFLAGS -DNDEBUG" %{?_smp_mflags}

# pathfix.py currently only works with files matching ^[a-zA-Z0-9_]+\.py$
# when crawling through directories, so we handle the special cases manually
LD_LIBRARY_PATH=$topdir $topdir/python Tools/scripts/pathfix.py -p -i "%{_bindir}/python%{pybasever}" . Tools/scripts/reindent-rst.py

# Rebuild with new python
# We need a link to a versioned python in the build directory
ln -s python python%{pybasever}
LD_LIBRARY_PATH=$topdir PATH=$PATH:$topdir make -s OPT="$CFLAGS -DNDEBUG" %{?_smp_mflags}

%install
[ -d $RPM_BUILD_ROOT ] && rm -fr $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr $RPM_BUILD_ROOT%{_mandir}

# Clean up patched .py files that are saved as .lib64
for f in distutils/command/install distutils/sysconfig; do
    rm -f Lib/$f.py.lib64
done

# create dummy ordereddict file which contains import for OrderedDict
touch Lib/ordereddict.py
echo 'from collections import OrderedDict' > Lib/ordereddict.py

make install DESTDIR=$RPM_BUILD_ROOT
# Fix the interpreter path in binaries installed by distutils 
# (which changes them by itself)
# Make sure we preserve the file permissions
for fixed in $RPM_BUILD_ROOT%{_bindir}/pydoc; do
    sed 's,#!.*/python$,#!%{_bindir}/env python%{pybasever},' $fixed > $fixed- \
        && cat $fixed- > $fixed && rm -f $fixed-
done

# Junk, no point in putting in -test sub-pkg
rm -f $RPM_BUILD_ROOT/%{pylibdir}/idlelib/testcode.py*

# don't include tests that are run at build time in the package
# This is documented, and used: rhbz#387401
if /bin/false; then
 # Move this to -test subpackage.
mkdir save_bits_of_test
for i in test_support.py __init__.py; do
  cp -a $RPM_BUILD_ROOT/%{pylibdir}/test/$i save_bits_of_test
done
rm -rf $RPM_BUILD_ROOT/%{pylibdir}/test
mkdir $RPM_BUILD_ROOT/%{pylibdir}/test
cp -a save_bits_of_test/* $RPM_BUILD_ROOT/%{pylibdir}/test
fi

%if %{main_python}
ln -s python $RPM_BUILD_ROOT%{_bindir}/python2
%else
mv $RPM_BUILD_ROOT%{_bindir}/python $RPM_BUILD_ROOT%{_bindir}/%{python}
mv $RPM_BUILD_ROOT/%{_mandir}/man1/python.1 $RPM_BUILD_ROOT/%{_mandir}/man1/python%{pybasever}.1
%endif

# tools

mkdir -p ${RPM_BUILD_ROOT}%{site_packages}

#modulator
install -p -m755 %{SOURCE6} ${RPM_BUILD_ROOT}%{_bindir}/modulator
cp -rp Tools/modulator \
  ${RPM_BUILD_ROOT}%{site_packages}/

#pynche
install -p -m755 %{SOURCE7} ${RPM_BUILD_ROOT}%{_bindir}/pynche
rm -f Tools/pynche/*.pyw
cp -rp Tools/pynche \
  ${RPM_BUILD_ROOT}%{site_packages}/

mv Tools/modulator/README Tools/modulator/README.modulator
mv Tools/pynche/README Tools/pynche/README.pynche

#gettext
install -p -m755  Tools/i18n/pygettext.py $RPM_BUILD_ROOT%{_bindir}/
install -p -m755  Tools/i18n/msgfmt.py $RPM_BUILD_ROOT%{_bindir}/

# Useful development tools
install -p -m755 -d $RPM_BUILD_ROOT%{tools_dir}/scripts
install Tools/README $RPM_BUILD_ROOT%{tools_dir}/
install -p Tools/scripts/*py $RPM_BUILD_ROOT%{tools_dir}/scripts/

# Documentation tools
install -m755 -d $RPM_BUILD_ROOT%{doc_tools_dir}
#install -m755 Doc/tools/mkhowto $RPM_BUILD_ROOT%{doc_tools_dir}

# Useful demo scripts
install -m755 -d $RPM_BUILD_ROOT%{demo_dir}
cp -ar Demo/* $RPM_BUILD_ROOT%{demo_dir}

# Get rid of crap
find $RPM_BUILD_ROOT/ -name "*~"|xargs rm -f
find $RPM_BUILD_ROOT/ -name ".cvsignore"|xargs rm -f
find $RPM_BUILD_ROOT/ -name "*.bat"|xargs rm -f
find . -name "*~"|xargs rm -f
find . -name ".cvsignore"|xargs rm -f
#zero length
rm -f $RPM_BUILD_ROOT%{site_packages}/modulator/Templates/copyright

rm -f $RPM_BUILD_ROOT%{pylibdir}/LICENSE.txt


#make the binaries install side by side with the main python
%if !%{main_python}
pushd $RPM_BUILD_ROOT%{_bindir}
mv idle idle%{pybasever}
mv modulator modulator%{pybasever}
mv pynche pynche%{pybasever}
mv pygettext.py pygettext%{pybasever}.py
mv msgfmt.py msgfmt%{pybasever}.py
mv smtpd.py smtpd%{pybasever}.py
mv pydoc pydoc%{pybasever}
mv 2to3 2to3-%{pybasever}
rm python-config
popd
%endif

# Remove shebang lines from .py files that aren't executable, and
# remove executability from .py files that don't have a shebang line:
find %{buildroot} -name \*.py \
  \( \( \! -perm /u+x,g+x,o+x -exec sed -e '/^#!/Q 0' -e 'Q 1' {} \; \
  -print -exec sed -i '1d' {} \; \) -o \( \
  -perm /u+x,g+x,o+x ! -exec grep -m 1 -q '^#!' {} \; \
  -exec chmod a-x {} \; \) \)

# Fix for bug #136654
rm -f $RPM_BUILD_ROOT%{pylibdir}/email/test/data/audiotest.au $RPM_BUILD_ROOT%{pylibdir}/test/audiotest.au

# Fix bug #143667: python should own /usr/lib/python2.x on 64-bit machines
%if "%{_lib}" == "lib64"
install -d $RPM_BUILD_ROOT/usr/lib/python%{pybasever}/site-packages
%endif

# Make python-devel multilib-ready (bug #192747, #139911)
%global _pyconfig32_h pyconfig-32.h
%global _pyconfig64_h pyconfig-64.h

%ifarch ppc64 s390x x86_64 ia64 alpha sparc64
%global _pyconfig_h %{_pyconfig64_h}
%else
%global _pyconfig_h %{_pyconfig32_h}
%endif
mv $RPM_BUILD_ROOT%{_includedir}/python%{pybasever}/pyconfig.h \
   $RPM_BUILD_ROOT%{_includedir}/python%{pybasever}/%{_pyconfig_h}
cat > $RPM_BUILD_ROOT%{_includedir}/python%{pybasever}/pyconfig.h << EOF
#include <bits/wordsize.h>

#if __WORDSIZE == 32
#include "%{_pyconfig32_h}"
#elif __WORDSIZE == 64
#include "%{_pyconfig64_h}"
#else
#error "Unknown word size"
#endif
EOF
ln -s ../../libpython%{pybasever}.so $RPM_BUILD_ROOT%{pylibdir}/config/libpython%{pybasever}.so

# Fix for bug 201434: make sure distutils looks at the right pyconfig.h file
sed -i -e "s/'pyconfig.h'/'%{_pyconfig_h}'/" $RPM_BUILD_ROOT%{pylibdir}/distutils/sysconfig.py

# Get rid of egg-info files (core python modules are installed through rpms)
rm $RPM_BUILD_ROOT%{pylibdir}/*.egg-info

# Ensure that the curses module was linked against libncursesw.so, rather than
# libncurses.so (bug 539917)
ldd $RPM_BUILD_ROOT/%{dynload_dir}/_curses*.so \
    | grep curses \
    | grep libncurses.so && (echo "_curses.so linked against libncurses.so" ; exit 1)

# Copy up the gdb hooks into place; the python file will be autoloaded by gdb
# when visiting libpython.so, provided that the python file is installed to the
# same path as the library (or its .debug file) plus a "-gdb.py" suffix, e.g:
#  /usr/lib/debug/usr/lib64/libpython2.6.so.1.0.debug-gdb.py
# (note that the debug path is /usr/lib/debug for both 32/64 bit)
# 
# Initially I tried:
#  /usr/lib/libpython2.6.so.1.0-gdb.py
# but doing so generated noise when ldconfig was rerun (rhbz:562980)
#
%if 0%{?with_gdb_hooks}
%global dir_holding_gdb_py %{_prefix}/lib/debug/%{_libdir}
%global path_of_gdb_py %{dir_holding_gdb_py}/%{py_INSTSONAME}.debug-gdb.py

mkdir -p %{buildroot}%{dir_holding_gdb_py}
cp %{SOURCE1} %{buildroot}%{path_of_gdb_py}

# Manually byte-compile the file, in case find-debuginfo.sh is run before
# brp-python-bytecompile, so that the .pyc/.pyo files are properly listed in
# the debuginfo manifest:
LD_LIBRARY_PATH=. ./python -c "import compileall; import sys; compileall.compile_dir('%{buildroot}%{dir_holding_gdb_py}', ddir='%{dir_holding_gdb_py}')"

LD_LIBRARY_PATH=. ./python -O -c "import compileall; import sys; compileall.compile_dir('%{buildroot}%{dir_holding_gdb_py}', ddir='%{dir_holding_gdb_py}')"
%endif # with_gdb_hooks

#
# Systemtap hooks:
#
%if 0%{?with_systemtap}
# Install a tapset for this libpython into tapsetdir, fixing up the path to the
# library:
mkdir -p %{buildroot}%{tapsetdir}
%ifarch ppc64 s390x x86_64 ia64 alpha sparc64
%global libpython_stp libpython%{pybasever}-64.stp
%else
%global libpython_stp libpython%{pybasever}-32.stp
%endif

sed \
   -e "s|LIBRARY_PATH|%{_libdir}/%{py_INSTSONAME}|" \
   %{SOURCE3} \
   > %{buildroot}%{tapsetdir}/%{libpython_stp}

%endif # with_systemtap

cp %{SOURCE8} %{buildroot}%{site_packages}

#                                                                                                   
# Fix shebangs in files listed in rhbz#521898                                                       
sed -i "s|^#\! */usr/bin.*$|#\!%{_bindir}/%{python}|" \
    %{buildroot}%{_bindir}/pygettext%{pybasever}.py \
    %{buildroot}%{_bindir}/msgfmt%{pybasever}.py \
    %{buildroot}%{_bindir}/smtpd%{pybasever}.py \
    %{buildroot}%{demo_dir}/pdist/rcvs \
    %{buildroot}%{demo_dir}/pdist/rcsbump \
    %{buildroot}%{demo_dir}/pdist/rrcs \
    %{buildroot}%{site_packages}/pynche/pynche

sed -i -e '1i#\! %{__python}' %{buildroot}%{demo_dir}/scripts/find-uname.py

# Do bytecompilation with the newly installed interpreter.
# compile *.pyo
find %{buildroot} -type f -a -name "*.py" -print0 | \
    LD_LIBRARY_PATH="%{buildroot}%{dynload_dir}/:%{buildroot}%{_libdir}" \
    PYTHONPATH="%{buildroot}%{_libdir}/python%{pybasever} %{buildroot}%{_libdir}/python%{pybasever}/site-packages" \
    xargs -0 %{buildroot}%{_bindir}/python%{pybasever} -O -c 'import py_compile, sys; [py_compile.compile(f, dfile=f.partition("%{buildroot}")[2]) for f in sys.argv[1:]]' || :
# compile *.pyc
find %{buildroot} -type f -a -name "*.py" -print0 | \
    LD_LIBRARY_PATH="%{buildroot}%{dynload_dir}/:%{buildroot}%{_libdir}" \
    PYTHONPATH="%{buildroot}%{_libdir}/python%{pybasever} %{buildroot}%{_libdir}/python%{pybasever}/site-packages" \
    xargs -0 %{buildroot}%{_bindir}/python%{pybasever} -c 'import py_compile, sys; [py_compile.compile(f, dfile=f.partition("%{buildroot}")[2]) for f in sys.argv[1:]]' || :

# Make library-files user writable
# rhbz#1046276
/usr/bin/chmod 755 %{buildroot}%{dynload_dir}/*.so
/usr/bin/chmod 755 %{buildroot}%{_libdir}/libpython%{pybasever}.so.1.0

# ===============================
# Running the upstream test suite
# ===============================

%check
%if 0%{run_selftest_suite}
echo STARTING: CHECKING OF PYTHON
EXTRATESTOPTS="--verbose"
EXCLUDED_TESTS=test_dl  # requires sizeof(int) == sizeof(long) == sizeof(char*)
WITHIN_PYTHON_RPM_BUILD= EXTRATESTOPTS="$EXTRATESTOPTS -x $EXCLUDED_TESTS" make test
echo FINISHED: CHECKING OF PYTHON
%endif


%files
%doc LICENSE README
%doc Misc/README.valgrind Misc/valgrind-python.supp Misc/gdbinit
%doc Tools/modulator/README.modulator
%doc Tools/pynche/README.pynche

%{_bindir}/pydoc*
%{_bindir}/%{python}
%if %{main_python}
%{_bindir}/python2
%endif # main_python
%{_bindir}/python%{pybasever}
%if %{main_python}
%{_bindir}/python-config
%endif
%{_bindir}/python%{pybasever}-config
%{_bindir}/smtpd*.py*
%{_bindir}/2to3*
%{_bindir}/idle*
%{_bindir}/modulator*
%{_bindir}/pynche*
%{_bindir}/pygettext*.py*
%{_bindir}/msgfmt*.py*

# https://bugzilla.redhat.com/show_bug.cgi?id=1476593
%exclude /usr/lib/debug%{_libdir}/libpython%{pybasever}.so.1.0.debug-gdb.py*

%{_mandir}/*/*

%{pylibdir}/

%{_includedir}/python%{pybasever}/
%{_libdir}/%{py_INSTSONAME}
%{_libdir}/libpython%{pybasever}.so


%if "%{_lib}" == "lib64"
%attr(0755,root,root) %dir /usr/lib/python%{pybasever}
%attr(0755,root,root) %dir /usr/lib/python%{pybasever}/site-packages
%endif

%if 0%{?with_systemtap}
%{tapsetdir}/%{libpython_stp}
%doc systemtap-example.stp pyfuntop.stp
%endif

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.9-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.9-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.6.9-20
- Rebuild for readline 8.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.9-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Björn Esser <besser82@fedoraproject.org> - 2.6.9-18
- Rebuilt for libcrypt.so.2 (#1666033)

* Mon Sep 24 2018 Miro Hrončok <mhroncok@redhat.com> - 2.6.9-17
- Security fix for CVE-2018-14647 (#1631822)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.9-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 30 2018 Miro Hrončok <mhroncok@redhat.com> - 2.6.9-15
- Fix shebangs

* Tue Mar 27 2018 Miro Hrončok <mhroncok@redhat.com> - 2.6.9-14
- Build the nis module with tirpc

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.9-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 24 2018 Björn Esser <besser82@fedoraproject.org> - 2.6.9-12
- Add patch for libxcrypt
- Disable strict symbol checks in the link editor

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 2.6.9-11
- Rebuilt for switch to libxcrypt

* Tue Dec 05 2017 Charalampos Stratakis <cstratak@redhat.com> - 2.6.9-10
- Fix for CVE-2017-1000158
Resolves: rhbz#1519602

* Tue Nov 07 2017 Charalampos Stratakis <cstratak@redhat.com> - 2.6.9-9
- Exclude gdb.py* files aimed for the debuginfo subpackage

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Feb 16 2017 Charalampos Stratakis <cstratak@redhat.com> - 2.6.9-6
- Fix test_sqlite

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 2.6.9-4
- Rebuild for readline 7.x

* Fri Oct 21 2016 Miro Hrončok <mhroncok@redhat.com> - 2.6.9-3
- Reword the description
- On Fedora 26+, BR compat-openssl10-devel
- Make sure pynche and modulator use the proper version of Python

* Mon Oct 03 2016 Miro Hrončok <mhroncok@redhat.com> - 2.6.9-2
- Do not create /usr/bin/python shebangs

* Tue Sep 06 2016 Miro Hrončok <mhroncok@redhat.com> - 2.6.9-1
- Import from CentOS 6
- Update to 2.6.9

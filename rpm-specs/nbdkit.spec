%global _hardened_build 1

# Broken on {power64} because of
# https://bugzilla.redhat.com/show_bug.cgi?id=1778520
%ifarch aarch64 %{arm} x86_64 ppc
%global have_libguestfs 1
%endif

# We can only compiler the OCaml plugin on platforms which have native
# OCaml support (not bytecode).
%ifarch %{ocaml_native_compiler}
%global have_ocaml 1
%endif

# Architectures where the complete test suite must pass.
#
# On all other architectures, a simpler test suite must pass.  This
# omits any tests that run full qemu, since running qemu under TCG is
# often broken on non-x86_64 arches.
%global complete_test_arches x86_64

# If the test suite is broken on a particular architecture, document
# it as a bug and add it to this list.
#
# aarch64: https://bugzilla.redhat.com/show_bug.cgi?id=1833346
#global broken_test_arches NONE
%global broken_test_arches aarch64

%if 0%{?rhel} == 7
# On RHEL 7, nothing in the virt stack is shipped on aarch64 and
# libguestfs was not shipped on POWER (fixed in 7.5).  We could in
# theory make all of this work by having lots more conditionals, but
# for now limit this package to x86_64 on RHEL.
ExclusiveArch:  x86_64
%endif

# If we should verify tarball signature with GPGv2.
%global verify_tarball_signature 1

# If there are patches which touch autotools files, set this to 1.
%global patches_touch_autotools %{nil}

# The source directory.
%global source_directory 1.21-development

Name:           nbdkit
Version:        1.21.12
Release:        1%{?dist}
Summary:        NBD server

License:        BSD
URL:            https://github.com/libguestfs/nbdkit

Source0:        http://libguestfs.org/download/nbdkit/%{source_directory}/%{name}-%{version}.tar.gz
%if 0%{verify_tarball_signature}
Source1:        http://libguestfs.org/download/nbdkit/%{source_directory}/%{name}-%{version}.tar.gz.sig
# Keyring used to verify tarball signature.
Source2:       libguestfs.keyring
%endif

%if 0%{patches_touch_autotools}
BuildRequires: autoconf, automake, libtool
%endif

%ifnarch %{complete_test_arches}
BuildRequires:  autoconf, automake, libtool
%endif
BuildRequires:  gcc, gcc-c++
BuildRequires:  /usr/bin/pod2man
BuildRequires:  gnutls-devel
BuildRequires:  libselinux-devel
%if 0%{?have_libguestfs}
BuildRequires:  libguestfs-devel
%endif
BuildRequires:  libvirt-devel
BuildRequires:  xz-devel
BuildRequires:  zlib-devel
BuildRequires:  libzstd-devel
BuildRequires:  libcurl-devel
BuildRequires:  libnbd-devel >= 0.9.8
BuildRequires:  libssh-devel
BuildRequires:  e2fsprogs, e2fsprogs-devel
BuildRequires:  genisoimage
BuildRequires:  bash-completion
BuildRequires:  perl-devel
BuildRequires:  perl(ExtUtils::Embed)
BuildRequires:  python3-devel
%if 0%{?have_ocaml}
# Requires OCaml 4.02.2 which contains fix for
# http://caml.inria.fr/mantis/view.php?id=6693
BuildRequires:  ocaml >= 4.02.2
%endif
BuildRequires:  ruby-devel
BuildRequires:  tcl-devel
BuildRequires:  lua-devel
%if 0%{verify_tarball_signature}
BuildRequires:  gnupg2
%endif

# Only for running the test suite:
BuildRequires:  /usr/bin/certtool
BuildRequires:  jq
BuildRequires:  /usr/bin/nbdsh
BuildRequires:  /usr/bin/qemu-img
BuildRequires:  /usr/bin/socat
BuildRequires:  /usr/sbin/ss
BuildRequires:  /usr/bin/ssh-keygen

# nbdkit is a metapackage pulling the server and a useful subset
# of the plugins and filters.
Requires:       nbdkit-server%{?_isa} = %{version}-%{release}
Requires:       nbdkit-basic-plugins%{?_isa} = %{version}-%{release}
Requires:       nbdkit-basic-filters%{?_isa} = %{version}-%{release}


%description
NBD is a protocol for accessing block devices (hard disks and
disk-like things) over the network.

nbdkit is a toolkit for creating NBD servers.

The key features are:

* Multithreaded NBD server written in C with good performance.

* Minimal dependencies for the basic server.

* Liberal license (BSD) allows nbdkit to be linked to proprietary
  libraries or included in proprietary code.

* Well-documented, simple plugin API with a stable ABI guarantee.
  Lets you to export "unconventional" block devices easily.

* You can write plugins in C or many other languages.

* Filters can be stacked in front of plugins to transform the output.

In Fedora, '%{name}' is a meta-package which pulls in the core server
and a useful subset of plugins and filters with minimal dependencies.

If you want just the server, install '%{name}-server'.

To develop plugins, install the '%{name}-devel' package and start by
reading the nbdkit(1) and nbdkit-plugin(3) manual pages.


%package server
Summary:        The %{name} server
License:        BSD


%description server
This package contains the %{name} server with no plugins or filters.


%package basic-plugins
Summary:        Basic plugins for %{name}
License:        BSD

Requires:       %{name}-server%{?_isa} = %{version}-%{release}
Provides:       %{name}-data-plugin = %{version}-%{release}
Provides:       %{name}-eval-plugin = %{version}-%{release}
Provides:       %{name}-file-plugin = %{version}-%{release}
Provides:       %{name}-floppy-plugin = %{version}-%{release}
Provides:       %{name}-full-plugin = %{version}-%{release}
Provides:       %{name}-info-plugin = %{version}-%{release}
Provides:       %{name}-memory-plugin = %{version}-%{release}
Provides:       %{name}-null-plugin = %{version}-%{release}
Provides:       %{name}-pattern-plugin = %{version}-%{release}
Provides:       %{name}-partitioning-plugin = %{version}-%{release}
Provides:       %{name}-random-plugin = %{version}-%{release}
Provides:       %{name}-sh-plugin = %{version}-%{release}
Provides:       %{name}-split-plugin = %{version}-%{release}
Provides:       %{name}-streaming-plugin = %{version}-%{release}
Provides:       %{name}-zero-plugin = %{version}-%{release}


%description basic-plugins
This package contains plugins for %{name} which only depend on simple
C libraries: glibc, gnutls, libzstd.  Other plugins for nbdkit with
more complex dependencies are packaged separately.

nbdkit-data-plugin         Serve small amounts of data from the command line.

nbdkit-eval-plugin         Write a shell script plugin on the command line.

nbdkit-file-plugin         The normal file plugin for serving files.

nbdkit-floppy-plugin       Create a virtual floppy disk from a directory.

nbdkit-full-plugin         A virtual disk that returns ENOSPC errors.

nbdkit-info-plugin         Serve client and server information.

nbdkit-memory-plugin       A virtual memory plugin.

nbdkit-null-plugin         A null (bitbucket) plugin.

nbdkit-pattern-plugin      Fixed test pattern.

nbdkit-partitioning-plugin Create virtual disks from partitions.

nbdkit-random-plugin       Random content plugin for testing.

nbdkit-sh-plugin           Write plugins as shell scripts or executables.

nbdkit-split-plugin        Concatenate one or more files.

nbdkit-streaming-plugin    A streaming file serving plugin.

nbdkit-zero-plugin         Zero-length plugin for testing.


%package example-plugins
Summary:        Example plugins for %{name}
License:        BSD

Requires:       %{name}-server%{?_isa} = %{version}-%{release}
# example4 is written in Perl.
Requires:       %{name}-perl-plugin


%description example-plugins
This package contains example plugins for %{name}.


# The plugins below have non-trivial dependencies are so are
# packaged separately.

%package cc-plugin
Summary:        Write small inline C plugins and scripts for %{name}
License:        BSD

Requires:       %{name}-server%{?_isa} = %{version}-%{release}
Requires:       gcc
Requires:       %{_bindir}/cat


%description cc-plugin
This package contains support for writing inline C plugins and scripts
for %{name}.  NOTE this is NOT the right package for writing plugins
in C, install %{name}-devel for that.


%package curl-plugin
Summary:        HTTP/FTP (cURL) plugin for %{name}
License:        BSD

Requires:       %{name}-server%{?_isa} = %{version}-%{release}


%description curl-plugin
This package contains cURL (HTTP/FTP) support for %{name}.


%if 0%{?have_libguestfs}
%package guestfs-plugin
Summary:        libguestfs plugin for %{name}
License:        BSD

Requires:       %{name}-server%{?_isa} = %{version}-%{release}


%description guestfs-plugin
This package is a libguestfs plugin for %{name}.
%endif


%package gzip-plugin
Summary:        GZip file serving plugin for %{name}
License:        BSD

Requires:       %{name}-server%{?_isa} = %{version}-%{release}


%description gzip-plugin
This package is a gzip file serving plugin for %{name}.


%package iso-plugin
Summary:        Virtual ISO 9660 plugin for %{name}
License:        BSD

Requires:       %{name}-server%{?_isa} = %{version}-%{release}
Requires:       genisoimage


%description iso-plugin
This package is a virtual ISO 9660 (CD-ROM) plugin for %{name}.


%package libvirt-plugin
Summary:        Libvirt plugin for %{name}
License:        BSD

Requires:       %{name}-server%{?_isa} = %{version}-%{release}


%description libvirt-plugin
This package is a libvirt plugin for %{name}.  It lets you access
libvirt guest disks readonly.  It is implemented using the libvirt
virDomainBlockPeek API.


%package linuxdisk-plugin
Summary:        Virtual Linux disk plugin for %{name}
License:        BSD

Requires:       %{name}-server%{?_isa} = %{version}-%{release}
# for mke2fs
Requires:       e2fsprogs


%description linuxdisk-plugin
This package is a virtual Linux disk plugin for %{name}.


%package lua-plugin
Summary:        Lua plugin for %{name}
License:        BSD

Requires:       %{name}-server%{?_isa} = %{version}-%{release}


%description lua-plugin
This package lets you write Lua plugins for %{name}.


%package nbd-plugin
Summary:        NBD passthrough plugin for %{name}
License:        BSD

Requires:       %{name}-server%{?_isa} = %{version}-%{release}


%description nbd-plugin
This package lets you forward NBD connections from %{name}
to another NBD server.


%if 0%{?have_ocaml}
%package ocaml-plugin
Summary:        OCaml plugin for %{name}
License:        BSD

Requires:       %{name}-server%{?_isa} = %{version}-%{release}


%description ocaml-plugin
This package lets you run OCaml plugins for %{name}.

To compile OCaml plugins you will also need to install
%{name}-ocaml-plugin-devel.


%package ocaml-plugin-devel
Summary:        OCaml development environment for %{name}
License:        BSD

Requires:       %{name}-server%{?_isa} = %{version}-%{release}
Requires:       %{name}-ocaml-plugin%{?_isa} = %{version}-%{release}


%description ocaml-plugin-devel
This package lets you write OCaml plugins for %{name}.
%endif


%package perl-plugin
Summary:        Perl plugin for %{name}
License:        BSD

Requires:       %{name}-server%{?_isa} = %{version}-%{release}


%description perl-plugin
This package lets you write Perl plugins for %{name}.


%package python-plugin
Summary:        Python 3 plugin for %{name}
License:        BSD

# Remove in Fedora 33:
Provides:       %{name}-python3-plugin = %{version}-%{release}
Obsoletes:      %{name}-python3-plugin <= %{version}-%{release}
Provides:       %{name}-python-plugin-common = %{version}-%{release}
Obsoletes:      %{name}-python-plugin-common <= %{version}-%{release}

Requires:       %{name}-server%{?_isa} = %{version}-%{release}


%description python-plugin
This package lets you write Python 3 plugins for %{name}.


%package ruby-plugin
Summary:        Ruby plugin for %{name}
License:        BSD

Requires:       %{name}-server%{?_isa} = %{version}-%{release}


%description ruby-plugin
This package lets you write Ruby plugins for %{name}.


%package ssh-plugin
Summary:        SSH plugin for %{name}
License:        BSD

Requires:       %{name}-server%{?_isa} = %{version}-%{release}


%description ssh-plugin
This package contains SSH support for %{name}.


%package tar-plugin
Summary:        Tar archive plugin for %{name}
License:        BSD

Requires:       %{name}-server%{?_isa} = %{version}-%{release}
# XXX These should be autogenerated.
Requires:       %{name}-perl-plugin
Requires:       perl(Cwd)
Requires:       perl(IO::File)


%description tar-plugin
This package is a tar archive plugin for %{name}.


%package tcl-plugin
Summary:        Tcl plugin for %{name}
License:        BSD

Requires:       %{name}-server%{?_isa} = %{version}-%{release}


%description tcl-plugin
This package lets you write Tcl plugins for %{name}.


%package tmpdisk-plugin
Summary:        Remote temporary filesystem disk plugin for %{name}
License:        BSD

Requires:       %{name}-server%{?_isa} = %{version}-%{release}
# For mkfs and mke2fs (defaults).
Requires:       util-linux, e2fsprogs
# For other filesystems.
Suggests:       xfsprogs, ntfsprogs, dosfstools


%description tmpdisk-plugin
This package is a remote temporary filesystem disk plugin for %{name}.


%ifarch x86_64
%package vddk-plugin
Summary:        VMware VDDK plugin for %{name}
License:        BSD

Requires:       %{name}-server%{?_isa} = %{version}-%{release}


%description vddk-plugin
This package is a plugin for %{name} which connects to
VMware VDDK for accessing VMware disks and servers.
%endif


%package basic-filters
Summary:        Basic filters for %{name}
License:        BSD

Requires:       %{name}-server%{?_isa} = %{version}-%{release}
Provides:       %{name}-blocksize-filter = %{version}-%{release}
Provides:       %{name}-cache-filter = %{version}-%{release}
Provides:       %{name}-cacheextents-filter = %{version}-%{release}
Provides:       %{name}-cow-filter = %{version}-%{release}
Provides:       %{name}-ddrescue-filter = %{version}-%{release}
Provides:       %{name}-delay-filter = %{version}-%{release}
Provides:       %{name}-error-filter = %{version}-%{release}
Provides:       %{name}-exitlast-filter = %{version}-%{release}
Provides:       %{name}-extentlist-filter = %{version}-%{release}
Provides:       %{name}-fua-filter = %{version}-%{release}
Provides:       %{name}-ip-filter = %{version}-%{release}
Provides:       %{name}-limit-filter = %{version}-%{release}
Provides:       %{name}-log-filter = %{version}-%{release}
Provides:       %{name}-nocache-filter = %{version}-%{release}
Provides:       %{name}-noextents-filter = %{version}-%{release}
Provides:       %{name}-nofilter-filter = %{version}-%{release}
Provides:       %{name}-noparallel-filter = %{version}-%{release}
Provides:       %{name}-nozero-filter = %{version}-%{release}
Provides:       %{name}-offset-filter = %{version}-%{release}
Provides:       %{name}-partition-filter = %{version}-%{release}
Provides:       %{name}-rate-filter = %{version}-%{release}
Provides:       %{name}-readahead-filter = %{version}-%{release}
Provides:       %{name}-retry-filter = %{version}-%{release}
Provides:       %{name}-stats-filter = %{version}-%{release}
Provides:       %{name}-truncate-filter = %{version}-%{release}


%description basic-filters
This package contains filters for %{name} which only depend on simple
C libraries: glibc, gnutls.  Other filters for nbdkit with more
complex dependencies are packaged separately.

nbdkit-blocksize-filter    Adjust block size of requests sent to plugins.

nbdkit-cache-filter        Server-side cache.

nbdkit-cacheextents-filter Cache extents.

nbdkit-cow-filter          Copy-on-write overlay for read-only plugins.

nbdkit-ddrescue-filter     Filter for serving from ddrescue dump.

nbdkit-delay-filter        Inject read and write delays.

nbdkit-error-filter        Inject errors.

nbdkit-exitlast-filter     Exit on last client connection.

nbdkit-extentlist-filter   Place extent list over a plugin.

nbdkit-fua-filter          Modify flush behaviour in plugins.

nbdkit-ip-filter           Filter clients by IP address.

nbdkit-limit-filter        Limit nr clients that can connect concurrently.

nbdkit-log-filter          Log all transactions to a file.

nbdkit-nocache-filter      Disable cache requests in the underlying plugin.

nbdkit-noextents-filter    Disable extents in the underlying plugin.

nbdkit-nofilter-filter     Passthrough filter.

nbdkit-noparallel-filter   Serialize requests to the underlying plugin.

nbdkit-nozero-filter       Adjust handling of zero requests by plugins.

nbdkit-offset-filter       Serve an offset and range.

nbdkit-partition-filter    Serve a single partition.

nbdkit-rate-filter         Limit bandwidth by connection or server.

nbdkit-readahead-filter    Prefetch data when reading sequentially.

nbdkit-retry-filter        Reopen connection on error.

nbdkit-stats-filter        Display statistics about operations.

nbdkit-truncate-filter     Truncate, expand, round up or round down size.


%package ext2-filter
Summary:        ext2, ext3 and ext4 filesystem support for %{name}
License:        BSD

Requires:       %{name}-server%{?_isa} = %{version}-%{release}

# Remove in Fedora 34:
Provides:       %{name}-ext2-plugin = %{version}-%{release}
Obsoletes:      %{name}-ext2-plugin <= %{version}-%{release}


%description ext2-filter
This package contains ext2, ext3 and ext4 filesystem support for
%{name}.


%package xz-filter
Summary:        XZ filter for %{name}
License:        BSD

Requires:       %{name}-server%{?_isa} = %{version}-%{release}

# Remove in Fedora 33:
Provides:       %{name}-xz-plugin = %{version}-%{release}
Obsoletes:      %{name}-xz-plugin <= %{version}-%{release}


%description xz-filter
This package is the xz filter for %{name}.


%package devel
Summary:        Development files and documentation for %{name}
License:        BSD

Requires:       %{name}-server%{?_isa} = %{version}-%{release}
Requires:       pkgconfig


%description devel
This package contains development files and documentation
for %{name}.  Install this package if you want to develop
plugins for %{name}.


%package bash-completion
Summary:       Bash tab-completion for %{name}
BuildArch:     noarch
Requires:      bash-completion >= 2.0
Requires:      %{name}-server = %{version}-%{release}


%description bash-completion
Install this package if you want intelligent bash tab-completion
for %{name}.


%prep
%if 0%{verify_tarball_signature}
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%endif
%autosetup -p1
%if 0%{patches_touch_autotools}
autoreconf -i
%endif

%ifnarch %{complete_test_arches}
# Simplify the test suite so it doesn't require qemu.
sed -i -e 's/^LIBGUESTFS_TESTS/xLIBGUESTFS_TESTS/' tests/Makefile.am
sed -i -e '/^if HAVE_GUESTFISH/,/^endif HAVE_GUESTFISH/d' tests/Makefile.am
autoreconf -i
%endif


%build
# Golang bindings are not enabled in the Fedora build since they don't
# need to be.  Most people would use them by copying the upstream
# package into their vendor/ directory.
%configure \
    PYTHON=%{_bindir}/python3 \
    --disable-static \
    --disable-golang \
    --disable-rust \
%if 0%{?have_ocaml}
    --enable-ocaml \
%else
    --disable-ocaml \
%endif
%if 0%{?have_libguestfs}
    --with-libguestfs \
%else
    --without-libguestfs \
%endif
    --with-tls-priority=@NBDKIT,SYSTEM

# Verify that it picked the correct version of Python
# to avoid RHBZ#1404631 happening again silently.
grep '^PYTHON_VERSION = 3' Makefile

make %{?_smp_mflags}


%install
%make_install

# Delete libtool crap.
find $RPM_BUILD_ROOT -name '*.la' -delete

# Remove the deprecated ext2 plugin (use ext2 filter instead).
rm $RPM_BUILD_ROOT%{_libdir}/%{name}/plugins/nbdkit-ext2-plugin.so
rm $RPM_BUILD_ROOT%{_mandir}/man1/nbdkit-ext2-plugin.1*


%check
%ifnarch %{broken_test_arches}
# Workaround for broken libvirt (RHBZ#1138604).
mkdir -p $HOME/.cache/libvirt

# tests/test-captive.sh is racy especially on s390x.  We need to
# rethink this test upstream.
truncate -s 0 tests/test-captive.sh

%ifarch s390x
# Temporarily kill tests/test-cache-max-size.sh since it fails
# sometimes on s390x for unclear reasons.
truncate -s 0 tests/test-cache-max-size.sh
%endif

# Temporarily kill test-nbd-tls.sh and test-nbd-tls-psk.sh
# https://www.redhat.com/archives/libguestfs/2020-March/msg00191.html
truncate -s 0 tests/test-nbd-tls.sh tests/test-nbd-tls-psk.sh

# Make sure we can see the debug messages (RHBZ#1230160).
export LIBGUESTFS_DEBUG=1
export LIBGUESTFS_TRACE=1

make %{?_smp_mflags} check || {
    cat tests/test-suite.log
    exit 1
  }
%endif


%if 0%{?have_ocaml}
%ldconfig_scriptlets plugin-ocaml
%endif


%files
# metapackage so empty


%files server
%doc README
%license LICENSE
%{_sbindir}/nbdkit
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%dir %{_libdir}/%{name}/filters
%{_mandir}/man1/nbdkit.1*
%{_mandir}/man1/nbdkit-captive.1*
%{_mandir}/man1/nbdkit-loop.1*
%{_mandir}/man1/nbdkit-probing.1*
%{_mandir}/man1/nbdkit-protocol.1*
%{_mandir}/man1/nbdkit-service.1*
%{_mandir}/man1/nbdkit-security.1*
%{_mandir}/man1/nbdkit-tls.1*


%files basic-plugins
%doc README
%license LICENSE
%{_libdir}/%{name}/plugins/nbdkit-data-plugin.so
%{_libdir}/%{name}/plugins/nbdkit-eval-plugin.so
%{_libdir}/%{name}/plugins/nbdkit-file-plugin.so
%{_libdir}/%{name}/plugins/nbdkit-floppy-plugin.so
%{_libdir}/%{name}/plugins/nbdkit-full-plugin.so
%{_libdir}/%{name}/plugins/nbdkit-info-plugin.so
%{_libdir}/%{name}/plugins/nbdkit-memory-plugin.so
%{_libdir}/%{name}/plugins/nbdkit-null-plugin.so
%{_libdir}/%{name}/plugins/nbdkit-partitioning-plugin.so
%{_libdir}/%{name}/plugins/nbdkit-pattern-plugin.so
%{_libdir}/%{name}/plugins/nbdkit-random-plugin.so
%{_libdir}/%{name}/plugins/nbdkit-sh-plugin.so
%{_libdir}/%{name}/plugins/nbdkit-split-plugin.so
%{_libdir}/%{name}/plugins/nbdkit-streaming-plugin.so
%{_libdir}/%{name}/plugins/nbdkit-zero-plugin.so
%{_mandir}/man1/nbdkit-data-plugin.1*
%{_mandir}/man1/nbdkit-eval-plugin.1*
%{_mandir}/man1/nbdkit-file-plugin.1*
%{_mandir}/man1/nbdkit-floppy-plugin.1*
%{_mandir}/man1/nbdkit-full-plugin.1*
%{_mandir}/man1/nbdkit-info-plugin.1*
%{_mandir}/man1/nbdkit-memory-plugin.1*
%{_mandir}/man1/nbdkit-null-plugin.1*
%{_mandir}/man1/nbdkit-partitioning-plugin.1*
%{_mandir}/man1/nbdkit-pattern-plugin.1*
%{_mandir}/man1/nbdkit-random-plugin.1*
%{_mandir}/man3/nbdkit-sh-plugin.3*
%{_mandir}/man1/nbdkit-split-plugin.1*
%{_mandir}/man1/nbdkit-streaming-plugin.1*
%{_mandir}/man1/nbdkit-zero-plugin.1*


%files example-plugins
%doc README
%license LICENSE
%{_libdir}/%{name}/plugins/nbdkit-example*-plugin.so
%{_libdir}/%{name}/plugins/nbdkit-example4-plugin
%{_mandir}/man1/nbdkit-example*-plugin.1*


%files curl-plugin
%doc README
%license LICENSE
%{_libdir}/%{name}/plugins/nbdkit-curl-plugin.so
%{_mandir}/man1/nbdkit-curl-plugin.1*


%files cc-plugin
%doc README
%license LICENSE
%{_libdir}/%{name}/plugins/nbdkit-cc-plugin.so
%{_mandir}/man3/nbdkit-cc-plugin.3*


%if 0%{?have_libguestfs}
%files guestfs-plugin
%doc README
%license LICENSE
%{_libdir}/%{name}/plugins/nbdkit-guestfs-plugin.so
%{_mandir}/man1/nbdkit-guestfs-plugin.1*
%endif


%files gzip-plugin
%doc README
%license LICENSE
%{_libdir}/%{name}/plugins/nbdkit-gzip-plugin.so
%{_mandir}/man1/nbdkit-gzip-plugin.1*


%files iso-plugin
%doc README
%license LICENSE
%{_libdir}/%{name}/plugins/nbdkit-iso-plugin.so
%{_mandir}/man1/nbdkit-iso-plugin.1*


%files libvirt-plugin
%doc README
%license LICENSE
%{_libdir}/%{name}/plugins/nbdkit-libvirt-plugin.so
%{_mandir}/man1/nbdkit-libvirt-plugin.1*


%files linuxdisk-plugin
%doc README
%license LICENSE
%{_libdir}/%{name}/plugins/nbdkit-linuxdisk-plugin.so
%{_mandir}/man1/nbdkit-linuxdisk-plugin.1*


%files lua-plugin
%doc README
%license LICENSE
%{_libdir}/%{name}/plugins/nbdkit-lua-plugin.so
%{_mandir}/man3/nbdkit-lua-plugin.3*


%files nbd-plugin
%doc README
%license LICENSE
%{_libdir}/%{name}/plugins/nbdkit-nbd-plugin.so
%{_mandir}/man1/nbdkit-nbd-plugin.1*


%if 0%{?have_ocaml}
%files ocaml-plugin
%doc README
%license LICENSE
%{_libdir}/libnbdkitocaml.so.*

%files ocaml-plugin-devel
%{_libdir}/libnbdkitocaml.so
%{_libdir}/ocaml/NBDKit.*
%{_mandir}/man3/nbdkit-ocaml-plugin.3*
%endif


%files perl-plugin
%doc README
%license LICENSE
%{_libdir}/%{name}/plugins/nbdkit-perl-plugin.so
%{_mandir}/man3/nbdkit-perl-plugin.3*


%files python-plugin
%doc README
%license LICENSE
%{_libdir}/%{name}/plugins/nbdkit-python-plugin.so
%{_mandir}/man3/nbdkit-python-plugin.3*


%files ruby-plugin
%doc README
%license LICENSE
%{_libdir}/%{name}/plugins/nbdkit-ruby-plugin.so
%{_mandir}/man3/nbdkit-ruby-plugin.3*


%files ssh-plugin
%doc README
%license LICENSE
%{_libdir}/%{name}/plugins/nbdkit-ssh-plugin.so
%{_mandir}/man1/nbdkit-ssh-plugin.1*


%files tar-plugin
%doc README
%license LICENSE
%{_libdir}/%{name}/plugins/nbdkit-tar-plugin
%{_mandir}/man1/nbdkit-tar-plugin.1*


%files tcl-plugin
%doc README
%license LICENSE
%{_libdir}/%{name}/plugins/nbdkit-tcl-plugin.so
%{_mandir}/man3/nbdkit-tcl-plugin.3*


%files tmpdisk-plugin
%doc README
%license LICENSE
%{_libdir}/%{name}/plugins/nbdkit-tmpdisk-plugin.so
%{_mandir}/man1/nbdkit-tmpdisk-plugin.1*


%ifarch x86_64
%files vddk-plugin
%doc README
%license LICENSE
%{_libdir}/%{name}/plugins/nbdkit-vddk-plugin.so
%{_mandir}/man1/nbdkit-vddk-plugin.1*
%endif


%files basic-filters
%doc README
%license LICENSE
%{_libdir}/%{name}/filters/nbdkit-blocksize-filter.so
%{_libdir}/%{name}/filters/nbdkit-cache-filter.so
%{_libdir}/%{name}/filters/nbdkit-cacheextents-filter.so
%{_libdir}/%{name}/filters/nbdkit-cow-filter.so
%{_libdir}/%{name}/filters/nbdkit-ddrescue-filter.so
%{_libdir}/%{name}/filters/nbdkit-delay-filter.so
%{_libdir}/%{name}/filters/nbdkit-error-filter.so
%{_libdir}/%{name}/filters/nbdkit-exitlast-filter.so
%{_libdir}/%{name}/filters/nbdkit-extentlist-filter.so
%{_libdir}/%{name}/filters/nbdkit-fua-filter.so
%{_libdir}/%{name}/filters/nbdkit-ip-filter.so
%{_libdir}/%{name}/filters/nbdkit-limit-filter.so
%{_libdir}/%{name}/filters/nbdkit-log-filter.so
%{_libdir}/%{name}/filters/nbdkit-nocache-filter.so
%{_libdir}/%{name}/filters/nbdkit-noextents-filter.so
%{_libdir}/%{name}/filters/nbdkit-nofilter-filter.so
%{_libdir}/%{name}/filters/nbdkit-noparallel-filter.so
%{_libdir}/%{name}/filters/nbdkit-nozero-filter.so
%{_libdir}/%{name}/filters/nbdkit-offset-filter.so
%{_libdir}/%{name}/filters/nbdkit-partition-filter.so
%{_libdir}/%{name}/filters/nbdkit-rate-filter.so
%{_libdir}/%{name}/filters/nbdkit-readahead-filter.so
%{_libdir}/%{name}/filters/nbdkit-retry-filter.so
%{_libdir}/%{name}/filters/nbdkit-stats-filter.so
%{_libdir}/%{name}/filters/nbdkit-truncate-filter.so
%{_mandir}/man1/nbdkit-blocksize-filter.1*
%{_mandir}/man1/nbdkit-cache-filter.1*
%{_mandir}/man1/nbdkit-cacheextents-filter.1*
%{_mandir}/man1/nbdkit-cow-filter.1*
%{_mandir}/man1/nbdkit-ddrescue-filter.1*
%{_mandir}/man1/nbdkit-delay-filter.1*
%{_mandir}/man1/nbdkit-error-filter.1*
%{_mandir}/man1/nbdkit-exitlast-filter.1*
%{_mandir}/man1/nbdkit-extentlist-filter.1*
%{_mandir}/man1/nbdkit-fua-filter.1*
%{_mandir}/man1/nbdkit-ip-filter.1*
%{_mandir}/man1/nbdkit-limit-filter.1*
%{_mandir}/man1/nbdkit-log-filter.1*
%{_mandir}/man1/nbdkit-nocache-filter.1*
%{_mandir}/man1/nbdkit-noextents-filter.1*
%{_mandir}/man1/nbdkit-nofilter-filter.1*
%{_mandir}/man1/nbdkit-noparallel-filter.1*
%{_mandir}/man1/nbdkit-nozero-filter.1*
%{_mandir}/man1/nbdkit-offset-filter.1*
%{_mandir}/man1/nbdkit-partition-filter.1*
%{_mandir}/man1/nbdkit-rate-filter.1*
%{_mandir}/man1/nbdkit-readahead-filter.1*
%{_mandir}/man1/nbdkit-retry-filter.1*
%{_mandir}/man1/nbdkit-stats-filter.1*
%{_mandir}/man1/nbdkit-truncate-filter.1*


%files ext2-filter
%doc README
%license LICENSE
%{_libdir}/%{name}/filters/nbdkit-ext2-filter.so
%{_mandir}/man1/nbdkit-ext2-filter.1*


%files xz-filter
%doc README
%license LICENSE
%{_libdir}/%{name}/filters/nbdkit-xz-filter.so
%{_mandir}/man1/nbdkit-xz-filter.1*


%files devel
%doc BENCHMARKING OTHER_PLUGINS README SECURITY TODO
%license LICENSE
# Include the source of the example plugins in the documentation.
%doc plugins/example*/*.c
%doc plugins/example4/nbdkit-example4-plugin
%doc plugins/lua/example.lua
%if 0%{?have_ocaml}
%doc plugins/ocaml/example.ml
%endif
%doc plugins/perl/example.pl
%doc plugins/python/example.py
%doc plugins/ruby/example.rb
%doc plugins/sh/example.sh
%doc plugins/tcl/example.tcl
%{_includedir}/nbdkit-common.h
%{_includedir}/nbdkit-filter.h
%{_includedir}/nbdkit-plugin.h
%{_includedir}/nbdkit-version.h
%{_includedir}/nbd-protocol.h
%{_mandir}/man3/nbdkit-filter.3*
%{_mandir}/man3/nbdkit-plugin.3*
%{_mandir}/man1/nbdkit-release-notes-1.*.1*
%{_libdir}/pkgconfig/nbdkit.pc


%files bash-completion
%license LICENSE
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/nbdkit


%changelog
* Tue Jun 23 2020 Richard W.M. Jones <rjones@redhat.com> - 1.21.12-1
- New upstream development version 1.21.12.
- Use new --disable-rust configure option.

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.21.11-2
- Perl 5.32 rebuild

* Fri Jun 19 2020 Richard W.M. Jones <rjones@redhat.com> - 1.21.11-1
- New upstream development version 1.21.11.

* Mon Jun 15 2020 Richard W.M. Jones <rjones@redhat.com> - 1.21.10-1
- New upstream development version 1.21.10.
- This makes nbdkit-basic-plugins depend on zstd.

* Sun Jun 14 2020 Richard W.M. Jones <rjones@redhat.com> - 1.21.9-1
- New upstream development version 1.21.9.

* Tue Jun  9 2020 Richard W.M. Jones <rjones@redhat.com> - 1.21.8-1
- New upstream development version 1.21.8.
- Remove upstream patches.

* Thu Jun  4 2020 Richard W.M. Jones <rjones@redhat.com> - 1.21.7-1
- New upstream development version 1.21.7.
- New nbdkit-cc-plugin subpackage.

* Tue Jun  2 2020 Richard W.M. Jones <rjones@redhat.com> - 1.21.6-1
- New upstream development version 1.21.6.

* Sat May 30 2020 Richard W.M. Jones <rjones@redhat.com> - 1.21.5-1
- New upstream development version 1.21.5.
- New ddrescue filter.

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.21.4-3
- Rebuilt for Python 3.9

* Wed May 20 2020 Richard W.M. Jones <rjones@redhat.com> - 1.21.4-2
- Add upstream patch to make tests/test-truncate4.sh more stable on s390x.

* Tue May 19 2020 Richard W.M. Jones <rjones@redhat.com> - 1.21.4-1
- New upstream development version 1.21.4.

* Sun May 10 2020 Richard W.M. Jones <rjones@redhat.com> - 1.21.3-1
- New upstream development version 1.21.3.

* Thu May 07 2020 Richard W.M. Jones <rjones@redhat.com> - 1.21.2-1
- New upstream development version 1.21.2.

* Tue May 05 2020 Richard W.M. Jones <rjones@redhat.com> - 1.20.1-2
- Bump and rebuild for OCaml 4.11.0+dev2-2020-04-22 rebuild.

* Mon May  4 2020 Richard W.M. Jones <rjones@redhat.com> - 1.20.1-2
- New upstream version 1.20.1.

* Sat May  2 2020 Richard W.M. Jones <rjones@redhat.com> - 1.20.0-2
- New upstream version 1.20.0.

* Thu Apr 30 2020 Richard W.M. Jones <rjones@redhat.com> - 1.19.12-1
- New upstream version 1.19.12.

* Tue Apr 28 2020 Richard W.M. Jones <rjones@redhat.com> - 1.19.11-1
- New upstream version 1.19.11.

* Fri Apr 24 2020 Richard W.M. Jones <rjones@redhat.com> - 1.19.10-1
- New upstream version 1.19.10.

* Thu Apr 23 2020 Richard W.M. Jones <rjones@redhat.com> - 1.19.9-1
- New upstream version 1.19.9.

* Thu Apr 16 2020 Richard W.M. Jones <rjones@redhat.com> - 1.19.8-1
- New upstream version 1.19.8.

* Wed Apr  8 2020 Richard W.M. Jones <rjones@redhat.com> - 1.19.7-1
- New upstream version 1.19.7.
- Disable VDDK on i386, support for VDDK 5.1.1 was removed upstream.

* Tue Mar 31 2020 Richard W.M. Jones <rjones@redhat.com> - 1.19.6-1
- New upstream version 1.19.6.

* Sat Mar 28 2020 Richard W.M. Jones <rjones@redhat.com> - 1.19.5-1
- New upstream version 1.19.5.

* Fri Mar 20 2020 Richard W.M. Jones <rjones@redhat.com> - 1.19.4-1
- New upstream version 1.19.4.

* Thu Mar 19 2020 Richard W.M. Jones <rjones@redhat.com> - 1.19.3-2
- Kill some upstream tests which are problematic.
- Restore test-shutdown.sh (it was renamed to test-delay-shutdown.sh)

* Tue Mar 17 2020 Richard W.M. Jones <rjones@redhat.com> - 1.19.3-1
- New upstream version 1.19.3.
- New plugin and subpackage: tmpdisk.

* Sat Mar 07 2020 Richard W.M. Jones <rjones@redhat.com> - 1.19.2-1
- New upstream version 1.19.2.
- New filters: exitlast, limit.

* Fri Mar 06 2020 Richard W.M. Jones <rjones@redhat.com> - 1.19.1-1
- New upstream version 1.19.1.

* Thu Feb 27 2020 Richard W.M. Jones <rjones@redhat.com> - 1.18.0-1
- New upstream stable branch version 1.18.0.

* Wed Feb 26 2020 Richard W.M. Jones <rjones@redhat.com> - 1.17.11-2
- OCaml 4.10.0 final.

* Tue Feb 25 2020 Richard W.M. Jones <rjones@redhat.com> - 1.17.11-1
- New upstream development version 1.17.11.

* Wed Feb 19 2020 Richard W.M. Jones <rjones@redhat.com> - 1.17.10-1
- New upstream development version 1.17.10.

* Tue Feb 18 2020 Richard W.M. Jones <rjones@redhat.com> - 1.17.9-1
- New upstream development version 1.17.9.

* Wed Feb 12 2020 Richard W.M. Jones <rjones@redhat.com> - 1.17.8-1
- New upstream development version 1.17.8.
- New filter: ext2.
- Deprecate and remove ext2 plugin.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 25 2020 Richard W.M. Jones <rjones@redhat.com> - 1.17.7-1
- New upstream development version 1.17.7.
- New filter: extentlist.

* Tue Jan 21 2020 Richard W.M. Jones <rjones@redhat.com> - 1.17.6-1
- New upstream development version 1.17.6.

* Sun Dec 15 2019 Richard W.M. Jones <rjones@redhat.com> - 1.17.5-1
- New upstream development version 1.17.5.
- Remove upstream patches.

* Sat Dec 14 2019 Richard W.M. Jones <rjones@redhat.com> - 1.17.4-2
- Improve test times.

* Fri Dec 13 2019 Richard W.M. Jones <rjones@redhat.com> - 1.17.4-1
- New upstream development version 1.17.4.
- New filter: nofilter.
- Remove upstream patches.

* Tue Dec 10 2019 Richard W.M. Jones <rjones@redhat.com> - 1.17.3-2
- New upstream development version 1.17.3.
- Add upstream patch to fix IPv6 support in tests.

* Sat Dec  7 2019 Richard W.M. Jones <rjones@redhat.com> - 1.17.2-2
- Reenable OCaml plugin on riscv64 again, should now work with 4.09.

* Tue Dec  3 2019 Richard W.M. Jones <rjones@redhat.com> - 1.17.2-1
- New upstream development version 1.17.2.
- Enable armv7 again.

* Sun Dec  1 2019 Richard W.M. Jones <rjones@redhat.com> - 1.17.1-1
- New upstream development version 1.17.1.
- Add nbdkit-eval-plugin.
- Add nbdkit-ip-filter.

* Wed Nov 27 2019 Richard W.M. Jones <rjones@redhat.com> - 1.16.0-6
- Use gpgverify macro instead of explicit gpgv2 command.

* Fri Nov 15 2019 Richard W.M. Jones <rjones@redhat.com> - 1.16.0-5
- Enable libvirt plugin on all architectures.
- Disable OCaml plugin on riscv64 temporarily.

* Thu Nov 14 2019 Richard W.M. Jones <rjones@redhat.com> - 1.16.0-1
- New stable release 1.16.0.

* Sat Nov 09 2019 Richard W.M. Jones <rjones@redhat.com> - 1.15.8-1
- New upstream version 1.15.8.
- Add new nbdkit-release-notes-* man pages.

* Wed Nov 06 2019 Richard W.M. Jones <rjones@redhat.com> - 1.15.7-1
- New upstream version 1.15.7.

* Fri Oct 25 2019 Richard W.M. Jones <rjones@redhat.com> - 1.15.6-1
- New upstream version 1.15.6.

* Sat Oct 19 2019 Richard W.M. Jones <rjones@redhat.com> - 1.15.5-1
- New upstream release 1.15.5.

* Tue Oct  1 2019 Richard W.M. Jones <rjones@redhat.com> - 1.15.4-1
- New upstream release 1.15.4.
- New nbdkit-security(1) man page.
- Rename nbdkit-reflection-plugin to nbdkit-info-plugin.

* Wed Sep 25 2019 Richard W.M. Jones <rjones@redhat.com> - 1.15.3-1
- New upstream release 1.15.3.
- Add new header file nbd-protocol.h to devel subpackage.

* Fri Sep 20 2019 Richard W.M. Jones <rjones@redhat.com> - 1.15.2-1
- New upstream version 1.15.2.
- Fixes second Denial of Service attack:
  https://www.redhat.com/archives/libguestfs/2019-September/msg00272.html
- Add new nbdkit-reflection-plugin.
- Add new nbdkit-retry-filter.

* Thu Sep 12 2019 Richard W.M. Jones <rjones@redhat.com> - 1.15.1-1
- New upstream version 1.15.1.
- Fixes Denial of Service / Amplication Attack:
  https://www.redhat.com/archives/libguestfs/2019-September/msg00084.html
- Add nbdsh BR for tests.
- Package <nbdkit-version.h>.

* Thu Aug 29 2019 Richard W.M. Jones <rjones@redhat.com> - 1.14.0-2
- Split out nbdkit-nbd-plugin subpackage.

* Wed Aug 28 2019 Richard W.M. Jones <rjones@redhat.com> - 1.14.0-1
- New upstream version 1.14.0.

* Wed Aug 21 2019 Richard W.M. Jones <rjones@redhat.com> - 1.13.9-3
- Temporarily kill tests/test-shutdown.sh

* Wed Aug 21 2019 Miro Hrončok <mhroncok@redhat.com> - 1.13.9-2
- Rebuilt for Python 3.8

* Wed Aug 21 2019 Richard W.M. Jones <rjones@redhat.com> - 1.13.9-1
- New upstream version 1.13.9.

* Wed Aug 21 2019 Richard W.M. Jones <rjones@redhat.com> - 1.13.8-7
- Add provides for all basic plugins and filters.

* Tue Aug 20 2019 Richard W.M. Jones <rjones@redhat.com> - 1.13.8-5
- BR libnbd 0.9.8.

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.13.8-4
- Rebuilt for Python 3.8

* Mon Aug 19 2019 Richard W.M. Jones <rjones@redhat.com> - 1.13.8-3
- Fix for libnbd 0.9.8.

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.13.8-2
- Rebuilt for Python 3.8

* Fri Aug  2 2019 Richard W.M. Jones <rjones@redhat.com> - 1.13.8-1
- New upstream version 1.13.8.

* Wed Jul 31 2019 Richard W.M. Jones <rjones@redhat.com> - 1.13.7-2
- Add upstream patch to deal with qemu-img 4.1 output change.

* Tue Jul 30 2019 Richard W.M. Jones <rjones@redhat.com> - 1.13.7-1
- New upstream version 1.13.7.

* Fri Jul 26 2019 Richard W.M. Jones <rjones@redhat.com> - 1.13.6-1
- New upstream version 1.13.6.
- Add BR libnbd-devel.
- New filter: cacheextents.
- Disable guestfs plugin on i686.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 10 2019 Richard W.M. Jones <rjones@redhat.com> - 1.13.5-2
- Further fix for Python 3.8 embed brokenness.

* Sun Jun 09 2019 Richard W.M. Jones <rjones@redhat.com> - 1.13.5-1
- New upstream version 1.13.5.

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.13.4-2
- Perl 5.30 rebuild

* Tue May 21 2019 Richard W.M. Jones <rjones@redhat.com> - 1.13.4-1
- New upstream version 1.13.4.
- Add new filters: nocache, noparallel.

* Sat Apr 27 2019 Richard W.M. Jones <rjones@redhat.com> - 1.13.3-1
- New upstream version 1.13.3.
- Add OCaml example to devel subpackage.

* Wed Apr 24 2019 Richard W.M. Jones <rjones@redhat.com> - 1.13.2-1
- New upstream version 1.13.2.

* Tue Apr 23 2019 Richard W.M. Jones <rjones@redhat.com> - 1.13.1-1
- New upstream version 1.13.1.
- Distribute BENCHMARKING and SECURITY files.
- Includes a fix for possible remote memory heap leak with user plugins.

* Sat Apr 13 2019 Richard W.M. Jones <rjones@redhat.com> - 1.13.0-1
- New upstream version 1.13.0.
- Add stats filter.

* Wed Apr 10 2019 Richard W.M. Jones <rjones@redhat.com> - 1.12.0-1
- New upstream version 1.12.0.
- Add noextents filter.

* Mon Apr 08 2019 Richard W.M. Jones <rjones@redhat.com> - 1.11.15-1
- New upstream version 1.11.15.

* Sat Apr 06 2019 Richard W.M. Jones <rjones@redhat.com> - 1.11.14-1
- New upstream version 1.11.14.
- Remove deprecated nbdkit-xz-plugin (replaced by nbdkit-xz-filter).

* Tue Apr 02 2019 Richard W.M. Jones <rjones@redhat.com> - 1.11.13-1
- New upstream version 1.11.13.

* Tue Apr 02 2019 Richard W.M. Jones <rjones@redhat.com> - 1.11.12-1
- New upstream version 1.11.12.
- New nbdkit-readahead-filter.

* Fri Mar 29 2019 Richard W.M. Jones <rjones@redhat.com> - 1.11.11-1
- New upstream version 1.11.11.

* Thu Mar 28 2019 Richard W.M. Jones <rjones@redhat.com> - 1.11.10-1
- New upstream version 1.11.10.

* Sat Mar 23 2019 Richard W.M. Jones <rjones@redhat.com> - 1.11.9-1
- New upstream version 1.11.9.

* Tue Mar 12 2019 Richard W.M. Jones <rjones@redhat.com> - 1.11.8-1
- New upstream version 1.11.8.

* Thu Mar 07 2019 Richard W.M. Jones <rjones@redhat.com> - 1.11.7-3
- Remove Python 2 plugin completely.
  https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Thu Mar 07 2019 Richard W.M. Jones <rjones@redhat.com> - 1.11.7-2
- Remove Provides/Obsoletes in Fedora 31.
- Remove workaround for QEMU bug which is fixed in Fedora 30+.
- Make the tests run in parallel, otherwise they are too slow.

* Thu Mar 07 2019 Richard W.M. Jones <rjones@redhat.com> - 1.11.7-1
- New upstream version 1.11.7.
- Add nbdkit ssh plugin.
- Remove patches already upstream.

* Tue Mar 05 2019 Richard W.M. Jones <rjones@redhat.com> - 1.11.6-2
- Add nbdkit rate filter.

* Fri Mar 01 2019 Richard W.M. Jones <rjones@redhat.com> - 1.11.6-1
- New upstream version 1.11.6.
- Add linuxdisk plugin.
- Remove rust plugin if compiled.

* Tue Feb 05 2019 Richard W.M. Jones <rjones@redhat.com> - 1.11.5-1
- New upstream version 1.11.5.

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 30 2019 Richard W.M. Jones <rjones@redhat.com> - 1.11.4-1
- New upstream version 1.11.4.

* Mon Jan 28 2019 Richard W.M. Jones <rjones@redhat.com> - 1.11.3-1
- New upstream version 1.11.3.

* Thu Jan 24 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.11.2-2
- F-30: rebuild against ruby26

* Thu Jan 24 2019 Richard W.M. Jones <rjones@redhat.com> - 1.11.2-1
- New upstream version 1.11.2.
- Drop patches included in upstream tarball.

* Thu Jan 24 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.11.1-2
- F-30: rebuild again against ruby26

* Tue Jan 22 2019 Richard W.M. Jones <rjones@redhat.com> - 1.11.1-1
- New upstream version 1.11.1.

* Mon Jan 21 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.10.0-2
- F-30: rebuild against ruby26

* Fri Jan 18 2019 Richard W.M. Jones <rjones@redhat.com> - 1.10.0-1
- New upstream version 1.10.0.

* Tue Jan 15 2019 Richard W.M. Jones <rjones@redhat.com> - 1.9.10-1
- New upstream version 1.9.10.

* Mon Jan 14 2019 Björn Esser <besser82@fedoraproject.org> - 1.9.9-2
- Rebuilt for libcrypt.so.2 (#1666033)

* Mon Jan  7 2019 Richard W.M. Jones <rjones@redhat.com> - 1.9.9-1
- New upstream version 1.9.9.

* Tue Jan  1 2019 Richard W.M. Jones <rjones@redhat.com> - 1.9.8-1
- New upstream version 1.9.8.

* Mon Dec 17 2018 Richard W.M. Jones <rjones@redhat.com> - 1.9.7-2
- Remove misguided LDFLAGS hack which removed server hardening.
  https://bugzilla.redhat.com/show_bug.cgi?id=1624149#c6

* Sat Dec 15 2018 Richard W.M. Jones <rjones@redhat.com> - 1.9.7-1
- New upstream version 1.9.7.

* Thu Dec 13 2018 Richard W.M. Jones <rjones@redhat.com> - 1.9.6-1
- New upstream version 1.9.6.
- Add nbdkit-full-plugin.

* Mon Dec 10 2018 Richard W.M. Jones <rjones@redhat.com> - 1.9.5-1
- New upstream version 1.9.5.

* Tue Dec 04 2018 Richard W.M. Jones <rjones@redhat.com> - 1.9.4-1
- New upstream version 1.9.4.
- Fix low priority security issue with TLS:
  https://www.redhat.com/archives/libguestfs/2018-December/msg00047.html
- New man page nbdkit-loop(1).

* Thu Nov 29 2018 Richard W.M. Jones <rjones@redhat.com> - 1.9.3-1
- New upstream version 1.9.3.

* Thu Nov 22 2018 Richard W.M. Jones <rjones@redhat.com> - 1.9.2-1
- New upstream version 1.9.2.
- Add new filter subpackage: nbdkit-xz-filter.
- Deprecate (but do not remove) nbdkit-xz-plugin.

* Sun Nov 18 2018 Richard W.M. Jones <rjones@redhat.com> - 1.9.1-1
- New upstream version 1.9.1.

* Wed Nov 14 2018 Richard W.M. Jones <rjones@redhat.com> - 1.9.0-1
- New upstream version 1.9.0.
- New development branch.

* Mon Nov 12 2018 Richard W.M. Jones <rjones@redhat.com> - 1.8.0-1
- New stable branch version 1.8.0.

* Fri Nov 09 2018 Richard W.M. Jones <rjones@redhat.com> - 1.7.10-1
- New upstream version 1.7.10, possibly final before 1.8.

* Tue Nov 06 2018 Richard W.M. Jones <rjones@redhat.com> - 1.7.9-2
- nbdkit metapackage should depend on versioned -server subpackage etc.

* Tue Nov 06 2018 Richard W.M. Jones <rjones@redhat.com> - 1.7.9-1
- New upstream version 1.7.9.

* Tue Oct 30 2018 Richard W.M. Jones <rjones@redhat.com> - 1.7.8-1
- New upstream version 1.7.8.

* Mon Oct 29 2018 Richard W.M. Jones <rjones@redhat.com> - 1.7.7-1
- New upstream version 1.7.7.
- New nbdkit-floppy-plugin subpackage.

* Wed Oct 17 2018 Richard W.M. Jones <rjones@redhat.com> - 1.7.6-1
- New upstream version 1.7.6.
- New nbdkit-iso-plugin subpackage.

* Tue Oct 16 2018 Richard W.M. Jones <rjones@redhat.com> - 1.7.5-1
- New upstream version 1.7.5.

* Tue Oct  2 2018 Richard W.M. Jones <rjones@redhat.com> - 1.7.4-1
- New upstream version 1.7.4.

* Tue Sep 18 2018 Richard W.M. Jones <rjones@redhat.com> - 1.7.3-1
- New upstream version 1.7.3.
- Add partitioning plugin.

* Thu Sep 13 2018 Richard W.M. Jones <rjones@redhat.com> - 1.7.2-1
- New upstream version 1.7.2.

* Mon Sep 10 2018 Richard W.M. Jones <rjones@redhat.com> - 1.7.1-1
- New upstream version 1.7.1.

* Sat Sep 08 2018 Richard W.M. Jones <rjones@redhat.com> - 1.7.0-1
- New upstream version 1.7.0, development branch.
- Add nbdkit-sh-plugin.

* Tue Aug 28 2018 Richard W.M. Jones <rjones@redhat.com> - 1.6.0-1
- New upstream version 1.6.0, stable branch.

* Mon Aug 27 2018 Richard W.M. Jones <rjones@redhat.com> - 1.5.10-3
- New upstream version 1.5.10.
- Add upstream patches after 1.5.10.

* Sun Aug 26 2018 Richard W.M. Jones <rjones@redhat.com> - 1.5.9-2
- New upstream version 1.5.9.
- Add upstream patches since 1.5.9 was released.

* Tue Aug 21 2018 Richard W.M. Jones <rjones@redhat.com> - 1.5.8-1
- New upstream version 1.5.8.

* Sat Aug 18 2018 Richard W.M. Jones <rjones@redhat.com> - 1.5.7-1
- New upstream version 1.5.7.

* Sat Aug 18 2018 Richard W.M. Jones <rjones@redhat.com> - 1.5.6-2
- Disable libvirt on riscv64.
- Other simplifications to %%configure line.

* Thu Aug 16 2018 Richard W.M. Jones <rjones@redhat.com> - 1.5.6-1
- New upstream version 1.5.6.

* Tue Aug 14 2018 Richard W.M. Jones <rjones@redhat.com> - 1.5.5-2
- Make nbdkit a metapackage.
- Package server in nbdkit-server subpackage.
- Rename all nbdkit-plugin-FOO to nbdkit-FOO-plugin to match upstream.

* Mon Aug 13 2018 Richard W.M. Jones <rjones@redhat.com> - 1.5.5-1
- New upstream version 1.5.5.
- New plugin: data.

* Mon Aug  6 2018 Richard W.M. Jones <rjones@redhat.com> - 1.5.4-1
- New upstream version 1.5.4.
- Add topic man pages.

* Mon Aug  6 2018 Richard W.M. Jones <rjones@redhat.com> - 1.5.3-1
- New upstream version 1.5.3.
- New filter: error.

* Wed Aug  1 2018 Richard W.M. Jones <rjones@redhat.com> - 1.5.2-1
- New upstream version 1.5.2.
- Remove patches which are all upstream.
- New filter: truncate.

* Tue Jul 24 2018 Richard W.M. Jones <rjones@redhat.com> - 1.5.1-2
- Enable VDDK plugin on x86-64 only.

* Fri Jul 20 2018 Richard W.M. Jones <rjones@redhat.com> - 1.5.1-1
- New upstream version 1.5.1.
- Remove patches, all upstream in this version.
- Small refactorings in the spec file.

* Sun Jul 15 2018 Richard W.M. Jones <rjones@redhat.com> - 1.5.0-3
- Add all upstream patches since 1.5.0.
- New pattern plugin.
- Add fixes for 32 bit platforms i686 and armv7.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jul  7 2018 Richard W.M. Jones <rjones@redhat.com> - 1.5.0-1
- New upstream version 1.5.0.
- Add Lua plugin and nbdkit-plugin-lua subpackage.
- Make python-unversioned-command dependent on Fedora >= 29.

* Fri Jul  6 2018 Richard W.M. Jones <rjones@redhat.com> - 1.4.0-1
- New upstream version 1.4.0.
- Add nbdkit-plugin-tcl subpackage.
- +BR python-unversioned-command

* Tue Jul 03 2018 Petr Pisar <ppisar@redhat.com> - 1.3.4-4
- Perl 5.28 rebuild

* Mon Jul 02 2018 Miro Hrončok <mhroncok@redhat.com> - 1.3.4-3
- Rebuilt for Python 3.7

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.3.4-2
- Perl 5.28 rebuild

* Sat Jun 23 2018 Richard W.M. Jones <rjones@redhat.com> - 1.3.4-1
- New upstream version 1.3.4.

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.3.3-2
- Rebuilt for Python 3.7

* Mon Jun 11 2018 Richard W.M. Jones <rjones@redhat.com> - 1.3.3-1
- New upstream version 1.3.3.
- New plugins: nbdkit-zero-plugin, nbdkit-random-plugin.
- Remove upstream patches.

* Sat Jun  9 2018 Richard W.M. Jones <rjones@redhat.com> - 1.3.2-2
- New upstream version 1.3.2.
- Remove patches now upstream.
- New ext2 plugin and subpackage, requires e2fsprogs-devel to build.
- Enable tarball signatures.
- Add upstream patch to fix tests when guestfish not available.
- Enable bash tab completion.

* Wed Jun  6 2018 Richard W.M. Jones <rjones@redhat.com> - 1.3.1-1
- New upstream version 1.3.1.
- Add patch to work around libvirt problem with relative socket paths.
- Add patch to fix the xz plugin test with recent guestfish.

* Fri Apr  6 2018 Richard W.M. Jones <rjones@redhat.com> - 1.3.0-1
- Move to development branch version 1.3.0.
- New filters: blocksize, fua, log, nozero.

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.1.28-5
- Escape macros in %%changelog

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.28-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.1.28-3
- Switch to %%ldconfig_scriptlets

* Fri Jan 26 2018 Richard W.M. Jones <rjones@redhat.com> - 1.1.28-2
- Run a simplified test suite on all arches.

* Mon Jan 22 2018 Richard W.M. Jones <rjones@redhat.com> - 1.1.28-1
- New upstream version 1.1.28.
- Add two new filters to nbdkit-basic-filters.

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 1.1.27-2
- Rebuilt for switch to libxcrypt

* Sat Jan 20 2018 Richard W.M. Jones <rjones@redhat.com> - 1.1.27-1
- New upstream version 1.1.27.
- Add new subpackage nbdkit-basic-filters containing new filters.

* Thu Jan 11 2018 Richard W.M. Jones <rjones@redhat.com> - 1.1.26-2
- Rebuild against updated Ruby.

* Sat Dec 23 2017 Richard W.M. Jones <rjones@redhat.com> - 1.1.26-1
- New upstream version 1.1.26.
- Add new pkg-config file and dependency.

* Wed Dec 06 2017 Richard W.M. Jones <rjones@redhat.com> - 1.1.25-1
- New upstream version 1.1.25.

* Tue Dec 05 2017 Richard W.M. Jones <rjones@redhat.com> - 1.1.24-1
- New upstream version 1.1.24.
- Add tar plugin (new subpackage nbdkit-plugin-tar).

* Tue Dec 05 2017 Richard W.M. Jones <rjones@redhat.com> - 1.1.23-1
- New upstream version 1.1.23.
- Add example4 plugin.
- Python3 tests require libguestfs so disable on s390x.

* Sun Dec 03 2017 Richard W.M. Jones <rjones@redhat.com> - 1.1.22-1
- New upstream version 1.1.22.
- Enable tests on Fedora.

* Sat Dec 02 2017 Richard W.M. Jones <rjones@redhat.com> - 1.1.20-1
- New upstream version 1.1.20.
- Add nbdkit-split-plugin to basic plugins.

* Sat Dec 02 2017 Richard W.M. Jones <rjones@redhat.com> - 1.1.19-2
- OCaml 4.06.0 rebuild.

* Thu Nov 30 2017 Richard W.M. Jones <rjones@redhat.com> - 1.1.19-1
- New upstream version 1.1.19.
- Combine all the simple plugins in %%{name}-basic-plugins.
- Add memory and null plugins.
- Rename the example plugins subpackage.
- Use %%license instead of %%doc for license file.
- Remove patches now upstream.

* Wed Nov 29 2017 Richard W.M. Jones <rjones@redhat.com> - 1.1.18-4
- Fix Python 3 builds / RHEL macros (RHBZ#1404631).

* Tue Nov 21 2017 Richard W.M. Jones <rjones@redhat.com> - 1.1.18-3
- New upstream version 1.1.18.
- Add NBD forwarding plugin.
- Add libselinux-devel so that SELinux support is enabled in the daemon.
- Apply all patches from upstream since 1.1.18.

* Fri Oct 20 2017 Richard W.M. Jones <rjones@redhat.com> - 1.1.16-2
- New upstream version 1.1.16.
- Disable python3 plugin on RHEL/EPEL <= 7.
- Only ship on x86_64 in RHEL/EPEL <= 7.

* Wed Sep 27 2017 Richard W.M. Jones <rjones@redhat.com> - 1.1.15-1
- New upstream version 1.1.15.
- Enable TLS support.

* Fri Sep 01 2017 Richard W.M. Jones <rjones@redhat.com> - 1.1.14-1
- New upstream version 1.1.14.

* Fri Aug 25 2017 Richard W.M. Jones <rjones@redhat.com> - 1.1.13-1
- New upstream version 1.1.13.
- Remove patches which are all upstream.
- Remove grubby hack, should not be needed with modern supermin.

* Sat Aug 19 2017 Richard W.M. Jones <rjones@redhat.com> - 1.1.12-13
- Rebuild for OCaml 4.05.0.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.12-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.12-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 27 2017 Richard W.M. Jones <rjones@redhat.com> - 1.1.12-10
- Rebuild for OCaml 4.04.2.

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.1.12-9
- Perl 5.26 rebuild

* Mon May 15 2017 Richard W.M. Jones <rjones@redhat.com> - 1.1.12-8
- Rebuild for OCaml 4.04.1.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.12-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Vít Ondruch <vondruch@redhat.com> - 1.1.12-6
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.4

* Fri Dec 23 2016 Richard W.M. Jones <rjones@redhat.com> - 1.1.12-5
- Rebuild for Python 3.6 update.

* Wed Dec 14 2016 Richard W.M. Jones <rjones@redhat.com> - 1.1.12-4
- Fix python3 subpackage so it really uses python3 (RHBZ#1404631).

* Sat Nov 05 2016 Richard W.M. Jones <rjones@redhat.com> - 1.1.12-3
- Rebuild for OCaml 4.04.0.

* Mon Oct 03 2016 Richard W.M. Jones <rjones@redhat.com> - 1.1.12-2
- Compile Python 2 and Python 3 versions of the plugin.

* Wed Jun 08 2016 Richard W.M. Jones <rjones@redhat.com> - 1.1.12-1
- New upstream version 1.1.12
- Enable Ruby plugin.
- Disable tests on Rawhide because libvirt is broken again (RHBZ#1344016).

* Wed May 25 2016 Richard W.M. Jones <rjones@redhat.com> - 1.1.11-10
- Add another upstream patch since 1.1.11.

* Mon May 23 2016 Richard W.M. Jones <rjones@redhat.com> - 1.1.11-9
- Add all patches upstream since 1.1.11 (fixes RHBZ#1336758).

* Tue May 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.1.11-7
- Perl 5.24 rebuild

* Wed Mar 09 2016 Richard W.M. Jones <rjones@redhat.com> - 1.1.11-6
- When tests fail, dump out test-suite.log so we can debug it.

* Fri Feb 05 2016 Richard W.M. Jones <rjones@redhat.com> - 1.1.11-5
- Don't run tests on x86, because kernel is broken there
  (https://bugzilla.redhat.com/show_bug.cgi?id=1302071)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 11 2016 Richard W.M. Jones <rjones@redhat.com> - 1.1.11-3
- Add support for newstyle NBD protocol (RHBZ#1297100).

* Sat Oct 31 2015 Richard W.M. Jones <rjones@redhat.com> - 1.1.11-1
- New upstream version 1.1.11.

* Thu Jul 30 2015 Richard W.M. Jones <rjones@redhat.com> - 1.1.10-3
- OCaml 4.02.3 rebuild.

* Sat Jun 20 2015 Richard W.M. Jones <rjones@redhat.com> - 1.1.10-2
- Enable libguestfs plugin on aarch64.

* Fri Jun 19 2015 Richard W.M. Jones <rjones@redhat.com> - 1.1.10-1
- New upstream version.
- Enable now working OCaml plugin (requires OCaml >= 4.02.2).

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 11 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.1.9-5
- Perl 5.22 rebuild

* Wed Jun 10 2015 Richard W.M. Jones <rjones@redhat.com> - 1.1.9-4
- Enable debugging messages when running make check.

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.1.9-3
- Perl 5.22 rebuild

* Tue Oct 14 2014 Richard W.M. Jones <rjones@redhat.com> - 1.1.9-2
- New upstream version 1.1.9.
- Add the streaming plugin.
- Include fix for streaming plugin in 1.1.9.

* Wed Sep 10 2014 Richard W.M. Jones <rjones@redhat.com> - 1.1.8-4
- Rebuild for updated Perl in Rawhide.
- Workaround for broken libvirt (RHBZ#1138604).

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 21 2014 Richard W.M. Jones <rjones@redhat.com> - 1.1.8-1
- New upstream version 1.1.8.
- Add support for cURL, and new nbdkit-plugin-curl package.

* Fri Jun 20 2014 Richard W.M. Jones <rjones@redhat.com> - 1.1.7-1
- New upstream version 1.1.7.
- Remove patches which are now all upstream.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Mar 06 2014 Dan Horák <dan[at]danny.cz> - 1.1.6-4
- libguestfs is available only on selected arches

* Fri Feb 21 2014 Richard W.M. Jones <rjones@redhat.com> - 1.1.6-3
- Backport some upstream patches, fixing a minor bug and adding more tests.
- Enable the tests since kernel bug is fixed.

* Sun Feb 16 2014 Richard W.M. Jones <rjones@redhat.com> - 1.1.6-1
- New upstream version 1.1.6.

* Sat Feb 15 2014 Richard W.M. Jones <rjones@redhat.com> - 1.1.5-2
- New upstream version 1.1.5.
- Enable the new Python plugin.
- Perl plugin man page moved to section 3.
- Perl now requires ExtUtils::Embed.

* Mon Feb 10 2014 Richard W.M. Jones <rjones@redhat.com> - 1.1.4-1
- New upstream version 1.1.4.
- Enable the new Perl plugin.

* Sun Aug  4 2013 Richard W.M. Jones <rjones@redhat.com> - 1.1.3-1
- New upstream version 1.1.3 which fixes some test problems.
- Disable tests because Rawhide kernel is broken (RHBZ#991808).
- Remove a single quote from description which confused emacs.
- Remove patch, now upstream.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 21 2013 Richard W.M. Jones <rjones@redhat.com> - 1.1.2-3
- Fix segfault when IPv6 client is used (RHBZ#986601).

* Tue Jul 16 2013 Richard W.M. Jones <rjones@redhat.com> - 1.1.2-2
- New development version 1.1.2.
- Disable the tests on Fedora <= 18.

* Tue Jun 25 2013 Richard W.M. Jones <rjones@redhat.com> - 1.1.1-1
- New development version 1.1.1.
- Add libguestfs plugin.
- Run the test suite.

* Mon Jun 24 2013 Richard W.M. Jones <rjones@redhat.com> - 1.0.0-4
- Initial release.

# Testsuite is CPU and disk space intensive, partially also just broken
%{!?testsuite: %global testsuite 1}

Summary:        Utility to clone and restore a partition
Name:           partclone
Version:        0.3.12
Release:        5%{?dist}
# Partclone itself is GPLv2+ but uses other source codes, breakdown:
# GPLv3+: fail-mbr/fail-mbr.S
# GPLv2 and GPLv2+: src/btrfs*
# GPL+ and GPLv2 and GPLv2+ and LGPLv2 and LGPLv2+: src/xfs*
# GPLv2 and GPLv2+: src/f2fs*
# GPLv2+: src/{dd,extfs,fat,hfsplus,minix,nilfs,ntfsclone-ng,part}clone*
# GPLv2+: src/{{fuseimg,info,main,ntfsfixboot,readblock}.c,progress*}
# LGPLv2+: src/gettext.h
# Unused source code (= not built): src/{exfat,jfs,reiser,ufs,vmfs}*
License:        GPL+ and GPLv2 and GPLv2+ and GPLv3+ and LGPLv2 and LGPLv2+
URL:            http://partclone.org/
Source0:        https://github.com/Thomas-Tsai/partclone/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         partclone-0.3.12-c99-for-loop.patch
Patch1:         partclone-0.3.12-gcc10.patch
BuildRequires:  gcc
BuildRequires:  libuuid-devel
BuildRequires:  fuse-devel
BuildRequires:  ncurses-devel
BuildRequires:  openssl-devel
BuildRequires:  e2fsprogs-devel
BuildRequires:  ntfs-3g-devel
BuildRequires:  libblkid-devel
%if 0%{?fedora}
BuildRequires:  nilfs-utils-devel
%endif
%if 0%{?testsuite}
BuildRequires:  e2fsprogs
BuildRequires:  ntfsprogs
BuildRequires:  dosfstools
%if 0%{?fedora} || 0%{?rhel} >= 7
# RHEL 6 provides xfsprogs RPM only as part of Resilient Storage Add-On
BuildRequires:  xfsprogs
%endif
%if 0%{?fedora} || 0%{?rhel} == 7
# RHEL 6 provides btrfs-progs RPM only on x86_64 architecture as it seems
# RHEL 8 (including EPEL 8) doesn't provide any btrfs-progs RPM at all
BuildRequires:  btrfs-progs
%endif
%if 0%{?fedora}
BuildRequires:  f2fs-tools
BuildRequires:  hfsplus-tools
%endif
%endif
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gettext-devel

%description
Partclone provides utilities to clone and restore used blocks on a partition
and is designed for higher compatibility of the file system by using existing
libraries, e.g. e2fslibs is used to read and write the ext2 partition.

%prep
%setup -q
%patch0 -p1 -b .c99-for-loop
%patch1 -p1 -b .gcc10
autoreconf -i -f

%build
# /usr/include/asm/types.h:31 and xfs/platform_defs.h:50 try both to define
# umode_t, reported: https://github.com/Thomas-Tsai/partclone/issues/96
%if 0%{?rhel} == 6
%ifarch ppc64
export CFLAGS="$RPM_OPT_FLAGS -DHAVE_UMODE_T"
%endif
%endif

%configure \
  --enable-extfs \
  --enable-xfs \
  --disable-reiserfs \
  --disable-reiser4 \
  --enable-hfsp \
  --enable-fat \
  --disable-exfat \
  --enable-f2fs \
%if 0%{?fedora}
  --enable-nilfs2 \
%else
  --disable-nilfs2 \
%endif
  --enable-ntfs \
  --disable-ufs \
  --disable-vmfs \
  --disable-jfs \
  --enable-btrfs \
  --enable-minix \
  --enable-ncursesw \
  --enable-fs-test
%make_build

%install
%make_install

# Building fail-mbr.bin requires a compiler that can build x86 binaries
%ifnarch %{ix86} x86_64
rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}/
%endif

%find_lang %{name}

%if 0%{?testsuite}
%check
# Patch proposal submitted: https://github.com/Thomas-Tsai/partclone/issues/103
sed -e 's/256/1440/' -i tests/_common

# Tests for Btrfs, XFS and F2FS filesystems are broken on all architectures
sed -e 's/^\(am__append_2 = btrfs.test\)/#\1/' \
    -e 's/^\(am__append_6 = xfs.test\)/#\1/' \
    -e 's/^\(am__append_8 = f2fs.test\)/#\1/' \
    -e 's/^\(am__append_11 = btrfs.test\)/#\1/' \
    -i tests/Makefile

# NILFS2 tests must be run as root (mockbuild is unprivileged)
sed -e 's/^\(am__append_13 = nilfs2.test\)/#\1/' \
    -i tests/Makefile

# Tests for FAT and HFS+ filesystems are broken on ppc64 and s390x
%ifarch ppc64 s390x
sed -e 's/^\(am__append_3 = fat.test\)/#\1/' \
    -e 's/^\(am__append_5 = hfsplus.test\)/#\1/' \
    -i tests/Makefile
%endif

# No f2fs-tools and hfsplus-tools in RHEL or EPEL
%if 0%{?rhel}
sed -e 's/^\(am__append_5 = hfsplus.test\)/#\1/' \
    -e 's/^\(am__append_8 = f2fs.test\)/#\1/' \
    -i tests/Makefile
%endif

make check || (cat tests/test-suite.log; exit 1)
%endif

%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog
%{_sbindir}/%{name}.*
%ifarch %{ix86} x86_64
%{_datadir}/%{name}/
%endif
%{_mandir}/man8/%{name}*.8*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Feb 02 2020 Robert Scheck <robert@fedoraproject.org> 0.3.12-4
- Added patch to declare variables as extern in header files

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 22 2019 Robert Scheck <robert@fedoraproject.org> 0.3.12-1
- Upgrade to 0.3.12

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Oct 30 2017 Robert Scheck <robert@fedoraproject.org> 0.3.11-1
- Upgrade to 0.3.11

* Thu Aug 17 2017 Robert Scheck <robert@fedoraproject.org> 0.3.5a-3
- Added licensing breakdown comment based on components (#1404895)

* Wed Aug 16 2017 Robert Scheck <robert@fedoraproject.org> 0.3.5a-2
- Added improvements suggested by Robert-André Mauchin (#1404895)

* Fri Jan 27 2017 Robert Scheck <robert@fedoraproject.org> 0.3.5a-1
- Upgrade to 0.3.5a (#1404895)
- Initial spec file for Fedora and Red Hat Enterprise Linux

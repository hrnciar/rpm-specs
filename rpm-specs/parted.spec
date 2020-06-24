%define _sbindir /sbin
%define _libdir /%{_lib}

Summary: The GNU disk partition manipulation program
Name:    parted
Version: 3.3
Release: 3%{?dist}
License: GPLv3+
URL:     http://www.gnu.org/software/parted

Source0: https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.xz
Source1: https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.xz.sig
Source2: pubkey.phillip.susi
Source3: pubkey.brian.lane

# Upstream patches since v3.3 release
Patch0001: 0001-Switch-gpt-header-move-and-msdos-overlap-to-python3.patch
Patch0002: 0003-tests-Test-incomplete-resizepart-command.patch
Patch0003: 0004-Fix-end_input-usage-in-do_resizepart.patch
Patch0004: 0005-libparted-Add-ChromeOS-Kernel-partition-flag.patch
Patch0005: 0006-libparted-Add-support-for-MSDOS-partition-type-bls_b.patch
Patch0006: 0007-libparted-Add-support-for-bls_boot-to-GPT-disks.patch

BuildRequires: gcc
BuildRequires: e2fsprogs-devel
BuildRequires: readline-devel
BuildRequires: ncurses-devel
BuildRequires: gettext-devel
BuildRequires: texinfo
BuildRequires: device-mapper-devel
BuildRequires: libselinux-devel
BuildRequires: libuuid-devel
BuildRequires: libblkid-devel >= 2.17
BuildRequires: gnupg2
BuildRequires: git
BuildRequires: autoconf automake
BuildRequires: e2fsprogs
BuildRequires: xfsprogs
BuildRequires: dosfstools
BuildRequires: perl-Digest-CRC
BuildRequires: bc
Buildrequires: python3
BuildRequires: gperf
BuildRequires: make

# bundled gnulib library exception, as per packaging guidelines
# https://fedoraproject.org/wiki/Packaging:No_Bundled_Libraries
Provides: bundled(gnulib)

%description
The GNU Parted program allows you to create, destroy, resize, move,
and copy hard disk partitions. Parted can be used for creating space
for new operating systems, reorganizing disk usage, and copying data
to new hard disks.


%package devel
Summary:  Files for developing apps which will manipulate disk partitions
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig

%description devel
The GNU Parted library is a set of routines for hard disk partition
manipulation. If you want to develop programs that manipulate disk
partitions and filesystems using the routines provided by the GNU
Parted library, you need to install this package.


%prep
%setup -q
gpg2 --import %{SOURCE2} %{SOURCE3}
gpg2 --verify %{SOURCE1} %{SOURCE0}
git init
git config user.email "parted-owner@fedoraproject.org"
git config user.name "Fedora Ninjas"
git add .
git commit -a -q -m "%{version} baseline."
[ -n "%{patches}" ] && git am %{patches}
iconv -f ISO-8859-1 -t UTF8 AUTHORS > tmp; touch -r AUTHORS tmp; mv tmp AUTHORS
git commit -a -m "run iconv"

%build
autoreconf
autoconf
CFLAGS="$RPM_OPT_FLAGS -Wno-unused-but-set-variable"; export CFLAGS
%configure --enable-selinux --disable-static --disable-gcc-warnings
# Don't use rpath!
%{__sed} -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
%{__sed} -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
V=1 %{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}

# Remove components we do not ship
%{__rm} -rf %{buildroot}%{_libdir}/*.la
%{__rm} -rf %{buildroot}%{_infodir}/dir
%{__rm} -rf %{buildroot}%{_bindir}/label
%{__rm} -rf %{buildroot}%{_bindir}/disk

%find_lang %{name}


%check
export LD_LIBRARY_PATH=$(pwd)/libparted/.libs:$(pwd)/libparted/fs/.libs
make check

%files -f %{name}.lang
%doc AUTHORS NEWS README THANKS
%{!?_licensedir:%global license %%doc}
%license COPYING
%{_sbindir}/parted
%{_sbindir}/partprobe
%{_mandir}/man8/parted.8.gz
%{_mandir}/man8/partprobe.8.gz
%{_libdir}/libparted.so.2
%{_libdir}/libparted.so.2.0.2
%{_libdir}/libparted-fs-resize.so.0
%{_libdir}/libparted-fs-resize.so.0.0.2
%{_infodir}/parted.info.*

%files devel
%doc TODO doc/API doc/FAT
%{_includedir}/parted
%{_libdir}/libparted.so
%{_libdir}/libparted-fs-resize.so
%{_libdir}/pkgconfig/libparted.pc
%{_libdir}/pkgconfig/libparted-fs-resize.pc


%changelog
* Fri Mar 06 2020 Brian C. Lane <bcl@redhat.com> - 3.3-3
- Add chromeos_kernel partition flag for gpt disklabels
- Add bls_boot partition flag for msdos and gpt disklabels

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 16 2019 Brian C. Lane <bcl@redhat.com> - 3.3-2
- tests: Test incomplete resizepart command
- Fix end_input usage in do_resizepart
  Resolves: rhbz#1701411

* Fri Oct 11 2019 Brian C. Lane <bcl@redhat.com> - 3.3-1
- New upstream release v3.3
  Includes the DASD virtio-blk fix.
- Dropping pre-3.2 changelog entries

* Wed Oct 02 2019 Brian C. Lane <bcl@redhat.com> - 3.2.153-2
- libparted/s390: Re-enabled virtio-attached DASD heuristics
  Fixes DASD backed virtblk devices

* Mon Aug 12 2019 Brian C. Lane <bcl@redhat.com> - 3.2.153-1
- New upstream ALPHA release v3.2.153
- Includes all patches except the python2 -> python3 change for test helpers

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 24 2019 Björn Esser <besser82@fedoraproject.org> - 3.2-42
- Remove hardcoded gzip suffix from GNU info pages

* Tue Apr 09 2019 Brian C. Lane <bcl@redhat.com> - 3.2-41
- Add fix and tests for nilfs2 sigsegv

* Fri Mar 01 2019 Brian C. Lane <bcl@redhat.com> - 3.2-40
- Run the CI tests using rpmbuild
- t6000-dm: Stop using private lvm root

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.2-39
- Rebuild for readline 8.0

* Thu Jan 31 2019 Brian C. Lane <bcl@redhat.com> - 3.2-38
- Add missing patches from Wang Dong
- fix crash due to improper partition number (dongdwdw)
- fix wrong error label jump in mkpart (dongdwdw)
- clean the disk information when commands fail (dongdwdw)
- Remove PED_ASSERT from ped_partition_set_name (bcl)
- Added support for Windows recovery partition (Hans-Joachim.Baader)

* Tue Oct 16 2018 Brian C. Lane <bcl@redhat.com> - 3.2-37
- Read NVMe model names from sysfs (dann.frazier)
- Fix warnings from GCC 7's -Wimplicit-fallthrough (dann.frazier)
- ped_unit_get_name: Resolve conflicting attributes 'const' and 'pure' (dann.frazier)
- Add udf to t1700-probe-fs and to the manpage (bcl)
- libparted: Add support for MBR id, GPT GUID and detection of UDF filesystem (pali.rohar)
- Fix potential command line buffer overflow (xu.simon)
- t6100-mdraid-partitions: Use v0.90 metadata for the test (bcl)
- parted.c: Make sure dev_name is freed (bcl)
- parted.c: Always free peek_word (bcl)
- Fix the length of several strncpy calls (bcl)

* Thu Jul 19 2018 Brian C. Lane <bcl@redhat.com> - 3.2-36
- drop ldconfig, it no longer needs to be called on un/install (bcl)
- Fix msdos-overlap py3 conversion (bcl)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Brian C. Lane <bcl@redhat.com> - 3.2-34
- Use python3 in buildroot
- Add make to BuildRequires
- Switch gpt-header-move and msdos-overlap to python3 (bcl)
- Modify gpt-header-move and msdos-overlap to work with py2 or py3 (bcl)
- Fix atari label false positives (psusi)
- Lift 512 byte restriction on fat resize (psusi)
- build: Remove unused traces of dynamic loading (cjwatson)
- Fix resizepart iec unit end sector (psusi)
- mkpart: Allow negative start value when FS-TYPE is not given (mail)
- Fix set and disk_set to not crash when no flags are supported (psusi)
- tests: fix t6100-mdraid-partitions (psusi)
- Fix make check (psusi)
- linux: Include <sys/sysmacros.h> for major() macro. (rjones)

* Thu Jun 07 2018 Brian C. Lane <bcl@redhat.com> - 3.2-33
- Use gpg2 for signature checking

* Sat Mar 24 2018 Richard W.M. Jones <rjones@redhat.com> - 3.2-32
- Fix for missing major/minor() macros in glibc 2.27.

* Mon Feb 19 2018 Brian C. Lane <bcl@redhat.com> - 3.2-31
- Add gcc BuildRequires for future minimal buildroot support
- Remove %%clean section

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Dec 19 2017 Brian C. Lane <bcl@redhat.com> - 3.2-29
- Add support for NVDIMM devices (sparschauer)
- libparted/labels: link with libiconv if needed (arnout)

* Mon Jul 31 2017 Brian C. Lane <bcl@redhat.com> - 3.2-28
- atari.c: Drop xlocale.h
  Resloves: rhbz#1476934

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Brian C. Lane <bcl@redhat.com> - 3.2-26
- libparted: Fix udev cookie leak in _dm_resize_partition (bcl)
  Resolves: rhbz#1455564

* Mon May 01 2017 Brian C. Lane <bcl@redhat.com> - 3.2-25
+ Updating to upstream patches
- tests/t1701-rescue-fs wait for the device to appear. (bcl)
- Increase timeout for rmmod scsi_debug and make it a framework failure (bcl)
- libparted/dasd: add test cases for the new fdasd functions (dongdwdw)
- libparted/dasd: add an exception for changing DASD-LDL partition table
  (dongdwdw)
- libpartd/dasd: improve flag processing for DASD-LDL (dongdwdw)
- parted/ui: remove unneccesary information of command line (dongdwdw)
- parted: check the name of partition first when to name a partition (dongdwdw)
- Add support for RAM drives (sparschauer)
- Fix crash when localized (psusi)
- libparted: Fix typo in hfs error message (sebras)
- libparted: Fix MacOS boot support (laurent)
- mac: copy partition type and name correctly (saproj)
- libparted: Add support for atari partition tables (glaubitz)
- libparted:tests: Move get_sector_size() to common.c (glaubitz)
- tests: Update t0220 and t0280 for the swap flag. (bcl)
- libparted: set swap flag on GPT partitions (aschnell)
- libparted/dasd: add test cases for the new fdasd functions (dongdwdw)
- libparted/dasd: add new fdasd functions (dongdwdw)
- libparted/dasd: update and improve fdasd functions (dongdwdw)
- libparted/dasd: unify vtoc handling for cdl/ldl (dongdwdw)
- libparted: Don't warn if no HDIO_GET_IDENTITY ioctl (sparschauer)
- libparted: Fix starting CHS in protective MBR (petr.uzel)
- tests: Stop timing t9040 (#1172675) (bcl)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 3.2-23
- Rebuild for readline 7.x

* Tue Oct 04 2016 Brian C. Lane <bcl@redhat.com> - 3.2-22
- tests: t3310-flags.sh: skip pc98 when sector size != 512 (bcl)
- tests: Set optimal blocks to 64 for scsi_debug devices (bcl)
- tests: t3310-flags.sh: Add tests for remaining table types (mike.fleetwood)
- tests: t3310-flags.sh: Add test for dvh table flags (mike.fleetwood)
- tests: t3310-flags.sh: Add test for mac table flags (mike.fleetwood)
- libparted: Remove commented local variable from bsd_partition_set_flag()
  (mike.fleetwood)
- libparted: Fix to report success when setting lvm flag on bsd table
  (mike.fleetwood)
- tests: t3310-flags.sh: Add test for bsd table flags (mike.fleetwood)
- tests: t3310-flags.sh: Stop excluding certain flags from being tested
  (mike.fleetwood)
- tests: t3310-flags.sh: Query libparted for all flags to be tested
  (mike.fleetwood)
- libparted: only IEC units are treated as exact (petr.uzel)
- docs: Improve partition description in parted.texi (gareth.randall)
- Add support for NVMe devices (petr.uzel)
- libparted/dasd: correct the offset where the first partition begins
  (dongdwdw)

* Wed Jun 15 2016 Brian C. Lane <bcl@redhat.com> - 3.2-21
- Cleanup mkpart manpage entry (#1183077)
- doc: Add information about quoting

* Thu May 26 2016 Brian C. Lane <bcl@redhat.com> - 3.2-20
- libparted: Fix probing AIX disks on other arches
- partprobe: Open the device once for probing

* Tue Apr 12 2016 Brian C. Lane <bcl@redhat.com> 3.2-19
- libparted: Remove fdasd geometry code from alloc_metadata (#1244833) (bcl)
- parted: Display details of partition alignment failure (#726856) (bcl)
- docs: Add list of filesystems for fs-type (#1311596) (bcl)
- Use disk geometry as basis for ext2 sector sizes. (Steven.Lang)
- parted: fix the rescue command (psusi)

* Tue Mar 29 2016 Brian C. Lane <bcl@redhat.com> 3.2-18
- Use BLKSSZGET to get device sector size in _device_probe_geometry()

* Mon Mar 07 2016 Brian C. Lane <bcl@redhat.com> 3.2-17
- lib-fs-resize: Prevent crash resizing FAT with very deep directories
- Add libparted/fs/.libs/ to LD_LIBRARY_PATH during make check

* Mon Feb 29 2016 Brian C. Lane <bcl@redhat.com> 3.2-16
- Cleanup library path usage in specfile
  pkgconfig wasn't finding libparted.pc because it was under /usr/lib64/
- Explicitly reference the library files instead of use wildcards.
- Move libparted-fs-resize.so to the -devel package where it belongs.
- Add a pkgconfig file for the filesystem resize library
- tests: Add udevadm settle to wait_for_ loop
- tests: Add wait to t9042
- tests: Fix t1700 failing on a host with a 4k xfs file

* Tue Feb 09 2016 Brian C. Lane <bcl@redhat.com> 3.2-15
- fdasd.c Safeguard against geometry misprobing.patch (#1305931)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Oct 29 2015 Brian C. Lane <bcl@redhat.com> 3.2-13
- parted: fix build error on s390

* Tue Oct 27 2015 Brian C. Lane <bcl@redhat.com> 3.2-12
- dasd: enhance device probing
- fdasd: geometry handling updated from upstream s390-tools

* Fri Aug 07 2015 Brian C. Lane <bcl@redhat.com> 3.2-11
- tests: Fix patch 0012 test for extended partition length
- UI: Avoid memory leaks
- libparted: Fix memory leaks.patch
- libparted: Fix possible memory leaks.patch
- libparted: Stop converting . in-sys-path-to /
- libparted: Use read-only when probing devices on linux
- tests: Use wait_for_dev_to_ functions

* Mon Jul 13 2015 Brian C. Lane <bcl@redhat.com> 3.2-10
- parted: Fix crash with name command and no disklabel (#1226067)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Brian C. Lane <bcl@redhat.com> 3.2-8
- tests: Make sure the extended partition length is 2 (#1135493)
- libparted: BLKPG_RESIZE_PARTITION uses bytes not sectors (#1135493)

* Tue Apr 28 2015 Brian C. Lane <bcl@redhat.com> 3.2-7
- Add python2 as a BuildRequires, used in some of the tests

* Tue Apr 28 2015 Brian C. Lane <bcl@redhat.com> 3.2-6
- Update manpage NAME so whatis will work (bcl)
- libparted: device mapper uses 512b sectors (bcl)
- tests: Add a test for device-mapper partition sizes (bcl)
- parted: don't crash in disk_set when disk label not found (psusi)

* Fri Nov 07 2014 Brian C. Lane <bcl@redhat.com> 3.2-5
- tests: Change minimum size to 256MiB for t1700-probe-fs

* Fri Oct 31 2014 Brian C. Lane <bcl@redhat.com> 3.2-4
- Update to current master commit ac74b83 to fix fat16 resize (#1159083)
- tests: t3000-resize-fs.sh: Add requirement on mkfs.vfat (mike.fleetwood)
- tests: t3000-resize-fs.sh: Add FAT16 resizing test (mike.fleetwood)
- lib-fs-resize: Prevent crash resizing FAT16 file systems (mike.fleetwood)
- libparted: also link to UUID_LIBS (heirecka)

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Aug 13 2014 Brian C. Lane <bcl@redhat.com> 3.2-2
- Use a better patch to find the UTF8 locale for t0251

* Wed Jul 30 2014 Brian C. Lane <bcl@redhat.com> 3.2-1
- Rebase on upstream stable release v3.2
- Drop upstream patches.
- Patch t0251 to use en_US.UTF-8 if possible. Fedora doesn't have C.UTF-8

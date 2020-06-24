%define _sbindir         /sbin
%define _libdir          /%{_lib}

Name: reiserfs-utils
Version: 3.6.27
Release: 2%{?dist}
Summary: Tools for creating, repairing, and debugging ReiserFS filesystems
URL: http://ftp.kernel.org/pub/linux/utils/fs/reiserfs/
Source0: https://www.kernel.org/pub/linux/kernel/people/jeffm/reiserfsprogs/%{version}/reiserfsprogs-%{version}.tar.xz
Patch0: parse_time_build_fix.patch
License: GPLv2 with exceptions
Epoch: 2
BuildRequires: chrpath
BuildRequires: e2fsprogs-devel
BuildRequires: gcc
BuildRequires: libuuid-devel
BuildRequires: libacl-devel

%description
The reiserfs-utils package contains a number of utilities for
creating, checking, modifying, and correcting any inconsistencies in
ReiserFS filesystems, including reiserfsck (used to repair filesystem
inconsistencies), mkreiserfs (used to initialize a partition to
contain an empty ReiserFS filesystem), debugreiserfs (used to examine
the internal structure of a filesystem, to manually repair a corrupted
filesystem, or to create test cases for reiserfsck), and some other
ReiserFS filesystem utilities.

You should install the reiserfs-utils package if you want to use
ReiserFS on any of your partitions.

%prep
%autosetup -n reiserfsprogs-%{version} -p1
#patch0 -p1


%build
%configure
%make_build

%install
%make_install
chrpath --delete "$RPM_BUILD_ROOT"/%{_sbindir}/*
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man8
install -m644 debugreiserfs/debugreiserfs.8 $RPM_BUILD_ROOT%{_mandir}/man8
install -m644 fsck/reiserfsck.8 $RPM_BUILD_ROOT%{_mandir}/man8
install -m644 mkreiserfs/mkreiserfs.8 $RPM_BUILD_ROOT%{_mandir}/man8
( cd $RPM_BUILD_ROOT/%{_sbindir}
  ln -fs mkreiserfs mkfs.reiserfs
  ln -fs reiserfsck fsck.reiserfs )

%files
%doc ChangeLog CREDITS README
%license COPYING
%{_sbindir}/*reiserfs*
%{_mandir}/*/*
%{_includedir}/reiserfs/
%{_libdir}/libreiserfscore*
%{_libdir}/pkgconfig/reiserfscore.pc

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2:3.6.27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Aug 04 2019 Filipe Rosset <rosset.filipe@gmail.com> - 2:3.6.27-1
- Update to 3.6.27 fixes rhbz#1464287 rhbz#1606106 rhbz#1675882 and rhbz#1736582

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2:3.6.25-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2:3.6.25-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2:3.6.25-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 19 2018 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 2:3.6.25-6
- add gcc into buildrequires

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2:3.6.25-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2:3.6.25-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2:3.6.25-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2:3.6.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Aug 15 2016 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 2:3.6.25-1
- 3.6.25

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2:3.6.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Oct 23 2015 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 2:3.6.24-1
- 3.6.24

* Mon Jul 13 2015 Ralf Corsépius <corsepiu@fedoraproject.org> -  2:3.6.21-13
- Append -std=gnu89 to CFLAGS (Fix F23FTBFS, RHBZ#1239875).
- Modernize spec.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:3.6.21-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:3.6.21-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:3.6.21-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:3.6.21-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:3.6.21-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Aug 16 2012 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 2:3.6.21-7
- add missing libuuid-devel bz# 660285

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:3.6.21-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:3.6.21-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:3.6.21-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Aug 11 2009 Ville Skyttä <ville.skytta@iki.fi> - 2:3.6.21-3
- Use bzipped upstream tarball.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:3.6.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Apr 01 2009 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 2:3.6.21-1
- 3.6.21

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:3.6.19-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Sep  3 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2:3.6.19-4
- fix license tag

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2:3.6.19-3.4.1
- Autorebuild for GCC 4.3

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 2:3.6.19-2.4.1
- rebuild

* Thu Jul  6 2006 David Woodhouse <dwmw2@redhat.com>
- Remove unneeded ExclusiveArch:

* Mon Jun  5 2006 Dave Jones <davej@redhat.com>
- Remove broken asm/unaligned include. (#191889)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 2:3.6.19-2.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Fri Apr 22 2005 Tomas Mraz <tmraz@redhat.com>
- added e2fsprogs-devel to build requires (#134969)

* Sun Jan 23 2005 Florian La Roche <laroche@redhat.com>
- 3.6.19

* Tue Oct 12 2004 Florian La Roche <Florian.LaRoche@redhat.de>
- 3.6.18

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jun 09 2004 Florian La Roche <Florian.LaRoche@redhat.de>
- 3.6.17

* Sat Mar 06 2004 Florian La Roche <Florian.LaRoche@redhat.de>
- Use %%ix86 macro, this got dropped with my previous update

* Thu Mar 04 2004 Florian La Roche <Florian.LaRoche@redhat.de>
- 3.6.13

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu Aug 28 2003 Florian La Roche <Florian.LaRoche@redhat.de>
- update to 3.6.11

* Sat May 31 2003 Florian La Roche <Florian.LaRoche@redhat.de>
- update to 3.6.8

* Wed Apr 30 2003 Elliot Lee <sopwith@redhat.com> 2:3.6.4-6
- Change ExcludeArch to ExclusiveArch to better handle the future of computing

* Thu Feb 06 2003 Phil Knirsch <pknirsch@redhat.com> 2:3.6.4-5
- Bumped release and rebuilt
- Removed s390 and s390x again until i get around fixing the bitops related
  stuff (which is borken on big-endian).

* Wed Jan 22 2003 Tim Powers <timp@redhat.com> 2:3.6.4-4
- rebuilt

* Sun Dec 01 2002 Elliot Lee <sopwith@redhat.com> 2:3.6.4-3
- For real

* Wed Nov 27 2002 Tim Powers <timp@redhat.com> 2:3.6.4-2
- build on all arches

* Mon Nov 11 2002 Florian La Roche <Florian.LaRoche@redhat.de>
- update to 3.6.4

* Fri Jul 19 2002 Florian La Roche <Florian.LaRoche@redhat.de>
- also compile on mainframe
- update epoch

* Mon Jul 15 2002 Florian La Roche <Florian.LaRoche@redhat.de>
- update to version 3.6.2, all additional patches are not needed anymore

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Tue Jan 15 2002 Tim Powers <timp@ragnarok.devel.redhat.com>
- rebuilt with tool toolchain

* Tue Jan 15 2002 Tim Powers <timp@redhat.com>
- rebuilt, for some reason the build date for the binary is not
  matching the build date for the SRPM.

* Wed Apr 25 2001 Bernhard Rosenkraenzer <bero@redhat.com> 3.x.0j-1
- Update to 3.x.0j

* Mon Mar  5 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- Update to 3.x.0f, many important fixes in fsck
- Add missing README (#30556)
- Use -v2 by default in mkreiserfs (#30556)

* Tue Feb 07 2001 Than Ngo <than@redhat.com>
- added Missing symlinks for mkfs and fsck commands (Bug #26359)

* Tue Jan 23 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- initial RPM
- changes from base package:
  - Fix a security problem (yet another tmp file issue)
  - Fix an fd leak
  - Get rid of the config.cache file, it contains broken settings
  - Install man pages
  - Fix locations of binaries, installing this stuff to "bin" is
    not really a good idea
  - Fix build on alpha and ia64

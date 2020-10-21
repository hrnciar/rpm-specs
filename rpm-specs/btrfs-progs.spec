# Local definition of version_no_tilde when it doesn't exist
%{!?version_no_tilde: %define version_no_tilde %{shrink:%(echo '%{version}' | tr '~' '-')}}

# Disable for now until version handling question is dealt with
%bcond_with python

Name:           btrfs-progs
Version:        5.7
Release:        5%{?dist}
Summary:        Userspace programs for btrfs

License:        GPLv2
URL:            https://btrfs.wiki.kernel.org/index.php/Main_Page
Source0:        https://www.kernel.org/pub/linux/kernel/people/kdave/%{name}/%{name}-v%{version_no_tilde}.tar.xz

# Backports from upstream
## Do not use raid0 by default for mkfs multi-disk (#1855174)
Patch0001:      0001-btrfs-progs-mkfs-clean-up-default-profile-settings.patch
Patch0002:      0002-btrfs-progs-mkfs-switch-to-single-as-default-profile.patch
## Fix convert for 64-bit ext4 filesystems (#1851674)
Patch0003:      0001-btrfs-progs-convert-prevent-32bit-overflow-for-cctx-.patch
Patch0004:      0002-btrfs-progs-tests-add-convert-test-case-for-multiply.patch

BuildRequires:  gcc, autoconf, automake
BuildRequires:  e2fsprogs-devel, libuuid-devel, zlib-devel, libzstd-devel
BuildRequires:  libacl-devel, libblkid-devel, lzo-devel
BuildRequires:  asciidoc, xmlto
BuildRequires:  systemd

%if %{with python}
BuildRequires:  python3-devel >= 3.4
%endif

%description
The btrfs-progs package provides all the userspace programs needed to create,
check, modify and correct any inconsistencies in the btrfs filesystem.

%package -n libbtrfs
Summary:        btrfs filesystem-specific runtime libraries
License:        GPLv2
# This was not properly split out before
Conflicts:      %{name} < 4.20.2

%description -n libbtrfs
libbtrfs contains the main library used by btrfs
filesystem-specific programs.

%package -n libbtrfsutil
Summary:        btrfs filesystem-specific runtime utility libraries
License:        LGPLv3
# This was not properly split out before
Conflicts:      %{name}-devel < 4.20.2

%description -n libbtrfsutil
libbtrfsutil contains an alternative utility library used by btrfs
filesystem-specific programs.

%package devel
Summary:        btrfs filesystem-specific libraries and headers
# libbtrfsutil is LGPLv3
License:        GPLv2 and LGPLv3
Requires:       %{name} = %{version}-%{release}
Requires:       libbtrfs%{?_isa} = %{version}-%{release}
Requires:       libbtrfsutil%{?_isa} = %{version}-%{release}

%description devel
btrfs-progs-devel contains the libraries and header files needed to
develop btrfs filesystem-specific programs.

It includes development files for two libraries:
- libbtrfs (GPLv2)
- libbtrfsutil (LGPLv3)

You should install btrfs-progs-devel if you want to develop
btrfs filesystem-specific programs.

%if %{with python}
%package -n python3-btrfsutil
Summary:        Python 3 bindings for libbtrfsutil
License:        LGPLv3
Requires:       libbtrfsutil%{?_isa} = %{version}-%{release}
%{?python_provide:%python_provide python3-btrfsutil}

%description -n python3-btrfsutil
python3-btrfsutil contains Python 3 bindings to the libbtrfsutil library,
which can be used for btrfs filesystem-specific programs in Python.

You should install python3-btrfsutil if you want to use or develop
btrfs filesystem-specific programs in Python.
%endif

%prep
%autosetup -n %{name}-v%{version_no_tilde} -p1

%build
./autogen.sh
%configure CFLAGS="%{optflags} -fno-strict-aliasing" %{!?with_python:--disable-python}
%make_build

%if %{with python}
pushd libbtrfsutil/python
%py3_build
popd
%endif

%install
%make_install mandir=%{_mandir} bindir=%{_sbindir} libdir=%{_libdir} incdir=%{_includedir}
install -Dpm0644 btrfs-completion %{buildroot}%{_datadir}/bash-completion/completions/btrfs
# Nuke the static lib
rm -v %{buildroot}%{_libdir}/*.a

%if %{with python}
pushd libbtrfsutil/python
%py3_install
popd
%endif

%files
%license COPYING
%{_sbindir}/btrfsck
%{_sbindir}/fsck.btrfs
%{_sbindir}/mkfs.btrfs
%{_sbindir}/btrfs-image
%{_sbindir}/btrfs-convert
%{_sbindir}/btrfs-select-super
%{_sbindir}/btrfstune
%{_sbindir}/btrfs
%{_sbindir}/btrfs-map-logical
%{_sbindir}/btrfs-find-root
%{_mandir}/man5/*.gz
%{_mandir}/man8/*.gz
%{_udevrulesdir}/64-btrfs-dm.rules
%{_datadir}/bash-completion/completions/btrfs

%files -n libbtrfs
%license COPYING
%{_libdir}/libbtrfs.so.0*

%files -n libbtrfsutil
%license libbtrfsutil/COPYING*
%{_libdir}/libbtrfsutil.so.1*

%files devel
%{_includedir}/*
%{_libdir}/libbtrfs.so
%{_libdir}/libbtrfsutil.so

%if %{with python}
%files -n python3-btrfsutil
%license libbtrfsutil/COPYING*
%{python3_sitearch}/btrfsutil.*.so
%{python3_sitearch}/btrfsutil-*.egg-info
%endif

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 24 2020 Neal Gompa <ngompa13@gmail.com> - 5.7-4
- Backport fix for converting 64-bit ext4 filesystems (#1851674)

* Tue Jul 21 2020 Neal Gompa <ngompa13@gmail.com> - 5.7-3
- Backport fix to not use raid0 by default for mkfs multi-disk (#1855174)

* Wed Jul 08 2020 Carl George <carl@george.computer> - 5.7-2
- Include bash completion

* Thu Jul 02 2020 Neal Gompa <ngompa13@gmail.com> - 5.7-1
- New upstream release

* Tue Jun 30 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 5.7~rc1-1
- Update to 5.7-rc1

* Mon Jun 15 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 5.6.1-2
- Rebuild

* Mon Jun 08 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 5.6.1-1
- Update to 5.6.1

* Sun Apr 05 2020 Neal Gompa <ngompa13@gmail.com> - 5.6-1
- New upstream release

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 06 2019 Neal Gompa <ngompa13@gmail.com> - 5.4-1
- New upstream release

* Sat Aug 24 2019 Neal Gompa <ngompa13@gmail.com> - 5.2.1-1
- New upstream release

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Neal Gompa <ngompa13@gmail.com> - 5.1-1
- New upstream release

* Sun Mar 10 2019 Neal Gompa <ngompa13@gmail.com> - 4.20.2-1
- New upstream release
- Properly split out libraries into libs subpackages
- Slightly modernize the spec

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.19.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 05 2018 Eric Sandeen <sandeen@redhat.com> 4.19.-1
- New usptream release

* Mon Aug 06 2018 Eric Sandeen <sandeen@redhat.com> 4.17.1-1
- New upstream release

* Mon Jul 23 2018 Eric Sandeen <sandeen@redhat.com> 4.17-1
- New upstream release
- Removes deprecated btrfs-debug-tree, btrfs-zero-log

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 4.16-3
- Rebuilt for Python 3.7

* Sun Apr 08 2018 Eric Sandeen <sandeen@redhat.com> 4.16-2
- Fix up header install paths in devel package (#1564881)

* Fri Apr 06 2018 Eric Sandeen <sandeen@redhat.com> 4.16-1
- New upstream release

* Mon Feb 26 2018 Eric Sandeen <sandeen@redhat.com> 4.15.1-2
- BuildRequires: gcc

* Fri Feb 16 2018 Eric Sandeen <sandeen@redhat.com> 4.15.1-1
- New upstream release

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.14.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 05 2018 Eric Sandeen <sandeen@redhat.com> 4.14.1-1
- New upstream release

* Tue Oct 17 2017 Eric Sandeen <sandeen@redhat.com> 4.13.3-1
- New upstream release

* Fri Oct 06 2017 Eric Sandeen <sandeen@redhat.com> 4.13.2-1
- New upstream release

* Tue Sep 26 2017 Eric Sandeen <sandeen@redhat.com> 4.13.1-1
- New upstream release

* Fri Sep 08 2017 Eric Sandeen <sandeen@redhat.com> 4.13-1
- New upstream release

* Mon Aug 28 2017 Eric Sandeen <sandeen@redhat.com> 4.12.1-1
- New upstream release

* Mon Jul 31 2017 Eric Sandeen <sandeen@redhat.com> 4.12-1
- New upstream release

* Mon Jul 31 2017 Igor Gnatenko <ignatenko@redhat.com> - 4.11.1-3
- Add missing BuildRequires: systemd

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 03 2017 Eric Sandeen <sandeen@redhat.com> 4.11.1-1
- New upstream release

* Thu May 18 2017 Eric Sandeen <sandeen@redhat.com> 4.11-1
- New upstream release

* Wed May 03 2017 Eric Sandeen <sandeen@redhat.com> 4.10.2-1
- New upstream release

* Fri Mar 17 2017 Eric Sandeen <sandeen@redhat.com> 4.10.1-1
- New upstream release

* Wed Mar 8 2017 Eric Sandeen <sandeen@redhat.com> 4.10-1
- New upstream release

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Eric Sandeen <sandeen@redhat.com> 4.9.1-1
- New upstream release

* Wed Jan 25 2017 Eric Sandeen <sandeen@redhat.com> 4.9-2
- Remove unapplied patches

* Fri Dec 23 2016 Eric Sandeen <sandeen@redhat.com> 4.9-1
- New upstream release

* Wed Nov 30 2016 Eric Sandeen <sandeen@redhat.com> 4.8.5-1
- New upstream release

* Fri Nov 25 2016 Eric Sandeen <sandeen@redhat.com> 4.8.4-1
- New upstream release
- btrfs-show-super removed (deprecated upstream)

* Sat Nov 12 2016 Eric Sandeen <sandeen@redhat.com> 4.8.3-1
- New upstream release

* Fri Oct 28 2016 Eric Sandeen <sandeen@redhat.com> 4.8.2-2
- Remove ioctl patch, different fix upstream

* Thu Oct 13 2016 Eric Sandeen <sandeen@redhat.com> 4.8.1-2
- Fix build of apps including ioctl.h (bz#1384413)

* Wed Oct 12 2016 Eric Sandeen <sandeen@redhat.com> 4.8.1-1
- New upstream release

* Wed Oct 12 2016 Eric Sandeen <sandeen@redhat.com> 4.8-1
- New upstream release (FTBFS on 32-bit)

* Wed Sep 21 2016 Eric Sandeen <sandeen@redhat.com> 4.7.3-1
- New upstream release

* Mon Sep 05 2016 Eric Sandeen <sandeen@redhat.com> 4.7.2-1
- New upstream release

* Sat Aug 27 2016 Eric Sandeen <sandeen@redhat.com> 4.7.1-1
- New upstream release

* Mon Aug 01 2016 Eric Sandeen <sandeen@redhat.com> 4.7-1
- New upstream release

* Fri Jun 24 2016 Eric Sandeen <sandeen@redhat.com> 4.6.1-1
- New upstream release

* Wed Jun 15 2016 Eric Sandeen <sandeen@redhat.com> 4.6-1
- New upstream release

* Fri May 13 2016 Eric Sandeen <sandeen@redhat.com> 4.5.3-1
- New upstream release

* Mon May 02 2016 Eric Sandeen <sandeen@redhat.com> 4.5.2-1
- New upstream release

* Thu Mar 31 2016 Eric Sandeen <sandeen@redhat.com> 4.5.1-1
- New upstream release

* Wed Mar 30 2016 Eric Sandeen <sandeen@redhat.com> 4.5-1
- New upstream release

* Fri Feb 26 2016 Eric Sandeen <sandeen@redhat.com> 4.4.1-1
- New upstream release

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 25 2016 Eric Sandeen <sandeen@redhat.com> 4.4-1
- New upstream release

* Wed Nov 18 2015 Eric Sandeen <sandeen@redhat.com> 4.3.1-1
- New upstream release

* Thu Oct 08 2015 Eric Sandeen <sandeen@redhat.com> 4.2.2-1
- New upstream release

* Tue Sep 22 2015 Eric Sandeen <sandeen@redhat.com> 4.2.1-1
- New upstream release

* Thu Sep 03 2015 Eric Sandeen <sandeen@redhat.com> 4.2-1
- New upstream release

* Thu Aug 06 2015 Eric Sandeen <sandeen@redhat.com> 4.1.2-1
- New upstream release
- Fix to reject unknown mkfs options (#1246468)

* Mon Jun 22 2015 Eric Sandeen <sandeen@redhat.com> 4.1-1
- New upstream release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed May 20 2015 Eric Sandeen <sandeen@redhat.com> 4.0.1-1
- New upstream release

* Wed Apr 29 2015 Eric Sandeen <sandeen@redhat.com> 4.0-1
- New upstream release

* Thu Mar 26 2015 Eric Sandeen <sandeen@redhat.com> 3.19.1-1
- New upstream release

* Wed Mar 11 2015 Eric Sandeen <sandeen@redhat.com> 3.19-1
- New upstream release

* Tue Jan 27 2015 Eric Sandeen <sandeen@redhat.com> 3.18.2-1
- New upstream release

* Mon Jan 12 2015 Eric Sandeen <sandeen@redhat.com> 3.18.1-1
- New upstream release

* Fri Jan 02 2015 Eric Sandeen <sandeen@redhat.com> 3.18-1
- New upstream release

* Fri Dec 05 2014 Eric Sandeen <sandeen@redhat.com> 3.17.3-1
- New upstream release

* Fri Nov 21 2014 Eric Sandeen <sandeen@redhat.com> 3.17.2-1
- New upstream release

* Mon Oct 20 2014 Eric Sandeen <sandeen@redhat.com> 3.17-1
- New upstream release

* Fri Oct 03 2014 Eric Sandeen <sandeen@redhat.com> 3.16.2-1
- New upstream release
- Update upstream source location

* Wed Aug 27 2014 Eric Sandeen <sandeen@redhat.com> 3.16-1
- New upstream release

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.14.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jun 16 2014 Eric Sandeen <sandeen@redhat.com> 3.14.2-3
- Support specification of UUID at mkfs time (#1094857)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.14.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 30 2014 Eric Sandeen <sandeen@redhat.com> 3.14.2-1
- New upstream release

* Tue Apr 22 2014 Eric Sandeen <sandeen@redhat.com> 3.14.1-1
- New upstream release

* Wed Apr 16 2014 Eric Sandeen <sandeen@redhat.com> 3.14-1
- New upstream release

* Mon Jan 20 2014 Eric Sandeen <sandeen@redhat.com> 3.12-2
- Add proper Source0 URL, switch to .xz

* Mon Nov 25 2013 Eric Sandeen <sandeen@redhat.com> 3.12-1
- It's a new upstream release!

* Thu Nov 14 2013 Eric Sandeen <sandeen@redhat.com> 0.20.rc1.20131114git9f0c53f-1
- New upstream snapshot

* Tue Sep 17 2013 Eric Sandeen <sandeen@redhat.com> 0.20.rc1.20130917git194aa4a-1
- New upstream snapshot
- Deprecated btrfsctl, btrfs-show, and btrfs-vol; still available in btrfs cmd

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20.rc1.20130501git7854c8b-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon May 13 2013 Richard W.M. Jones <rjones@redhat.com> 0.20.rc1.20130501git7854c8b-3
- Add accepted upstream patch to fix SONAME libbtrfs.so -> libbtrfs.so.0

* Thu May 02 2013 Eric Sandeen <sandeen@redhat.com> 0.20.rc1.20130501git7854c8b-2
- Fix subpackage brokenness

* Wed May 01 2013 Eric Sandeen <sandeen@redhat.com> 0.20.rc1.20130501git7854c8b-1
- New upstream snapshot
- btrfs-progs-devel subpackage

* Fri Mar 08 2013 Eric Sandeen <sandeen@redhat.com> 0.20.rc1.20130308git704a08c-1
- New upstream snapshot
- btrfs-restore is now a command in the btrfs utility

* Wed Feb 13 2013 Richard W.M. Jones <rjones@redhat.com> 0.20.rc1.20121017git91d9eec-3
- Include upstream patch to clear caches as a partial fix for RHBZ#863978.

* Thu Nov  1 2012 Josef Bacik <josef@toxicpanda.com> 0.20.rc1.20121017git91d9eec-2
- fix a bug when mkfs'ing a file (rhbz# 871778)

* Wed Oct 17 2012 Josef Bacik <josef@toxicpanda.com> 0.20.rc1.20121017git91d9eec-1
- update to latest btrfs-progs

* Wed Oct 10 2012 Richard W.M. Jones <rjones@redhat.com> 0.19.20120817git043a639-2
- Add upstream patch to correct uninitialized fsid variable
  (possible fix for RHBZ#863978).

* Fri Aug 17 2012 Josef Bacik <josef@toxicpanda.com> 0.19.20120817git043a639-1
- update to latest btrfs-progs

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.19-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Apr 25 2012 Josef Bacik <josef@toxicpanda.com> 0.19-19
- make btrfs filesystem show <uuid> actually work (rhbz# 816293)

* Wed Apr 11 2012 Josef Bacik <josef@toxicpanda.com> 0.19-18
- updated to latest btrfs-progs

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.19-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Aug 05 2011 Josef Bacik <josef@toxicpanda.com> 0.19-16
- fix build-everything patch to actually build everything

* Fri Aug 05 2011 Josef Bacik <josef@toxicpanda.com> 0.19-15
- actually build btrfs-zero-log

* Thu Aug 04 2011 Josef Bacik <josef@toxicpanda.com> 0.19-14
- bring btrfs-progs uptodate with upstream

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.19-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Aug 20 2010 Adam Tkac <atkac redhat com> 0.19-12
- rebuild to ensure F14 has bigger NVR than F13

* Wed Mar 24 2010 Josef Bacik <josef@toxicpanda.com> 0.19-11
- bring btrfs-progs uptodate with upstream, add btrfs command and other
  features.

* Thu Mar 11 2010 Josef Bacik <josef@toxicpanda.com> 0.19-10
- fix dso linking issue and bring btrfs-progs uptodate with upstream

* Tue Feb 2 2010 Josef Bacik <josef@toxicpanda.com> 0.19-9
- fix btrfsck so it builds on newer glibcs

* Tue Feb 2 2010 Josef Bacik <josef@toxicpanda.com> 0.19-8
- fix btrfsctl to return 0 on success and 1 on failure

* Tue Aug 25 2009 Josef Bacik <josef@toxicpanda.com> 0.19-7
- add btrfs-progs-valgrind.patch to fix memory leaks and segfaults

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.19-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 15 2009 Josef Bacik <josef@toxicpanda.com> 0.19-5
- add e2fsprogs-devel back to BuildRequires since its needed for the converter

* Wed Jul 15 2009 Josef Bacik <josef@toxicpanda.com> 0.19-4
- change BuildRequires for e2fsprogs-devel to libuuid-devel

* Fri Jun 19 2009 Josef Bacik <josef@toxicpanda.com> 0.19-3
- added man pages to the files list and made sure they were installed properly

* Fri Jun 19 2009 Josef Bacik <josef@toxicpanda.com> 0.19-2
- add a patch for the Makefile to make it build everything again

* Fri Jun 19 2009 Josef Bacik <josef@toxicpanda.com> 0.19-1
- update to v0.19 of btrfs-progs for new format

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jan 22 2009 Josef Bacik <josef@toxicpanda.com> 0.18-3
- updated label patch

* Thu Jan 22 2009 Josef Bacik <josef@toxicpanda.com> 0.18-2
- add a patch to handle having /'s in labels

* Sat Jan 17 2009 Josef Bacik <josef@toxicpanda.com> 0.18-1
- updated to 0.18 because of the ioctl change in 2.6.29-rc2

* Fri Jan 16 2009 Marek Mahut <mmahut@fedoraproject.org> 0.17-4
- RHBZ#480219 btrfs-convert is missing

* Mon Jan 12 2009 Josef Bacik <josef@toxicpanda.com> 0.17-2
- fixed wrong sources upload

* Mon Jan 12 2009 Josef Bacik <josef@toxicpanda.com> 0.17
- Upstream release 0.17

* Sat Jan 10 2009 Kyle McMartin <kyle@redhat.com> 0.16.git1-1
- Upstream git sync from -g72359e8 (needed for kernel...)

* Sat Jan 10 2009 Marek Mahut <mmahut@fedoraproject.org> 0.16-1
- Upstream release 0.16

* Wed Jun 25 2008 Josef Bacik <josef@toxicpanda.com> 0.15-4
-use fedoras normal CFLAGS

* Mon Jun 23 2008 Josef Bacik <josef@toxicpanda.com> 0.15-3
-Actually defined _root_sbindir
-Fixed the make install line so it would install to the proper dir

* Mon Jun 23 2008 Josef Bacik <josef@toxicpanda.com> 0.15-2
-Removed a . at the end of the description
-Fixed the copyright to be GPLv2 since GPL doesn't work anymore

* Mon Jun 23 2008 Josef Bacik <josef@toxicpanda.com> 0.15-1
-Initial build

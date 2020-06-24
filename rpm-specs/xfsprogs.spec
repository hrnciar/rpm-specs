Summary:	Utilities for managing the XFS filesystem
Name:		xfsprogs
Version:	5.6.0
Release:	2%{?dist}
License:	GPL+ and LGPLv2+
URL:		https://xfs.wiki.kernel.org
Source0:	http://kernel.org/pub/linux/utils/fs/xfs/xfsprogs/%{name}-%{version}.tar.xz
Requires:	util-linux
BuildRequires:	gcc
BuildRequires:	libtool, gettext, libattr-devel, libuuid-devel
BuildRequires:	readline-devel, libblkid-devel >= 2.17-0.1.git5e51568
Buildrequires:	lvm2-devel, libicu-devel >= 4.6
Provides:	xfs-cmds
Obsoletes:	xfs-cmds <= %{version}
Provides:	xfsprogs-qa-devel
Obsoletes:	xfsprogs-qa-devel <= %{version}
Conflicts:	xfsdump < 3.0.1
Suggests:	xfsprogs-xfs_scrub

%description
A set of commands to use the XFS filesystem, including mkfs.xfs.

XFS is a high performance journaling filesystem which originated
on the SGI IRIX platform.  It is completely multi-threaded, can
support large files and large filesystems, extended attributes,
variable block sizes, is extent based, and makes extensive use of
Btrees (directories, extents, free space) to aid both performance
and scalability.

This implementation is on-disk compatible with the IRIX version
of XFS.

%package devel
Summary: XFS filesystem-specific headers
Requires: xfsprogs = %{version}-%{release}, libuuid-devel

%description devel
xfsprogs-devel contains the header files needed to develop XFS
filesystem-specific programs.

You should install xfsprogs-devel if you want to develop XFS
filesystem-specific programs,  If you install xfsprogs-devel, you'll
also want to install xfsprogs.

%package xfs_scrub
Summary: XFS filesystem online scrubbing utilities
Requires: xfsprogs = %{version}-%{release}, python3

%description xfs_scrub
xfs_scrub attempts to check and repair all metadata in a mounted XFS filesystem.
WARNING!  This program is EXPERIMENTAL, which means that its behavior and
interface could change at any time!

%prep
%setup -q

%build
export tagname=CC

%configure \
        --enable-readline=yes	\
	--enable-blkid=yes	\
	--enable-lto=no

make %{?_smp_mflags}

%install
make DIST_ROOT=$RPM_BUILD_ROOT install install-dev \
	PKG_ROOT_SBIN_DIR=%{_sbindir} PKG_ROOT_LIB_DIR=%{_libdir}

# nuke .la files, etc
rm -f $RPM_BUILD_ROOT/{%{_lib}/*.{la,a,so},%{_libdir}/*.{la,a}}

# remove non-versioned docs location
rm -rf $RPM_BUILD_ROOT/%{_datadir}/doc/xfsprogs/

%find_lang %{name}

%ldconfig_scriptlets

%files -f %{name}.lang
%doc doc/CHANGES README
%{_libdir}/*.so.*
%dir %{_usr}/%{_lib}/xfsprogs
%{_usr}/%{_lib}/xfsprogs/*
%{_mandir}/man5/*
%{_mandir}/man8/*
%{_sbindir}/*
%{_unitdir}/*
%exclude %{_sbindir}/xfs_scrub*
%exclude %{_mandir}/man8/xfs_scrub*
%exclude %{_usr}/%{_lib}/xfsprogs/xfs_scrub*
%exclude %{_mandir}/man8/xfs_scrub_all*
%exclude %{_unitdir}/xfs_scrub*

%files xfs_scrub
%{_sbindir}/xfs_scrub*
%{_mandir}/man8/xfs_scrub*
%{_usr}/%{_lib}/xfsprogs/xfs_scrub*
%{_mandir}/man8/xfs_scrub_all*
%{_unitdir}/xfs_scrub*

%files devel
%{_mandir}/man2/*
%{_mandir}/man3/*
%dir %{_includedir}/xfs
%{_includedir}/xfs/handle.h
%{_includedir}/xfs/jdm.h
%{_includedir}/xfs/linux.h
%{_includedir}/xfs/xfs.h
%{_includedir}/xfs/xfs_arch.h
%{_includedir}/xfs/xfs_fs.h
%{_includedir}/xfs/xfs_types.h
%{_includedir}/xfs/xfs_format.h
%{_includedir}/xfs/xfs_da_format.h
%{_includedir}/xfs/xfs_log_format.h
%{_includedir}/xfs/xqm.h

%{_libdir}/*.so

%changelog
* Sat May 16 2020 Pete Walter <pwalter@fedoraproject.org> - 5.6.0-2
- Rebuild for ICU 67

* Tue Apr 14 2020 Eric Sandeen <sandeen@redhat.com> 5.6.0-1
- New upstream release

* Fri Mar 13 2020 Eric Sandeen <sandeen@redhat.com> 5.5.0-1
- New upstream release

* Fri Jan 31 2020 Eric Sandeen <sandeen@redhat.com> 5.4.0-3
- Fix global redefinitions for gcc10 build

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Eric Sandeen <sandeen@redhat.com> 5.4.0-1
- New upstream release

* Fri Nov 15 2019 Eric Sandeen <sandeen@redhat.com> 5.3.0-1
- New upstream release

* Fri Nov 01 2019 Pete Walter <pwalter@fedoraproject.org> - 5.2.1-2
- Rebuild for ICU 65

* Wed Aug 21 2019 Eric Sandeen <sandeen@redhat.com> 5.2.1-1
- New upstream release

* Fri Aug 16 2019 Eric Sandeen <sandeen@redhat.com> 5.2.0-1
- New upstream release

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 19 2019 Eric Sandeen <sandeen@redhat.com> 5.1.0-1
- New upstream release

* Wed May 08 2019 Eric Sandeen <sandeen@redhat.com> 5.0.0-2
- Create new xfs_scrub subpackage (#1666839)

* Fri May 03 2019 Eric Sandeen <sandeen@redhat.com> 5.0.0-1
- New upstream release

* Fri Feb 22 2019 Eric Sandeen <sandeen@redhat.com> 4.20.0-1
- New upstream release

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 4.19.0-4
- Rebuild for readline 8.0

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.19.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 23 2019 Pete Walter <pwalter@fedoraproject.org> - 4.19.0-2
- Rebuild for ICU 63

* Tue Nov 13 2018 Eric Sandeen <sandeen@redhat.com> 4.19.0-1
- New upstream release

* Fri Aug 24 2018 Eric Sandeen <sandeen@redhat.com> 4.18.0-1
- New upstream release

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.17.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 10 2018 Pete Walter <pwalter@fedoraproject.org> - 4.17.0-2
- Rebuild for ICU 62

* Thu Jun 28 2018 Eric Sandeen <sandeen@redhat.com> 4.17.0-1
- New upstream release

* Mon Apr 30 2018 Pete Walter <pwalter@fedoraproject.org> - 4.16.0-2
- Rebuild for ICU 61.1

* Thu Apr 26 2018 Eric Sandeen <sandeen@redhat.com> 4.16.0-1
- New upstream release
- Clean up specfile

* Mon Feb 26 2018 Eric Sandeen <sandeen@redhat.com> 4.15.1-1
- New upstream release
- Update Polish translation

* Mon Feb 26 2018 Eric Sandeen <sandeen@redhat.com> 4.15.0-2
- BuildRequires: gcc

* Sat Feb 24 2018 Eric Sandeen <sandeen@redhat.com> 4.15.0-1
- New upstream release
- Adds new xfs_scrub utility and services

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Nov 27 2017 Eric Sandeen <sandeen@redhat.com> 4.14.0-1
- New upstream release

* Wed Sep 27 2017 Eric Sandeen <sandeen@redhat.com> 4.13.1-1
- New upstream release
- Trim ancient changelog

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.12.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Sun Jul 30 2017 Florian Weimer <fweimer@redhat.com> - 4.12.0-3
- Rebuild with binutils fix for ppc64le (#1475636)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 24 2017 Eric Sandeen <sandeen@redhat.com> 4.12.0-1
- New upstream release

* Fri May 05 2017 Eric Sandeen <sandeen@redhat.com> 4.11.0-1
- New upstream release

* Sun Feb 26 2017 Eric Sandeen <sandeen@redhat.com> 4.10.0-1
- New upstream release

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 4.9.0-2
- Rebuild for readline 7.x

* Thu Jan 05 2017 Eric Sandeen <sandeen@redhat.com> 4.9.0-1
- New upstream release

* Tue Oct 18 2016 Eric Sandeen <sandeen@redhat.com> 4.8.0-1
- New upstream release

* Tue Sep 06 2016 Eric Sandeen <sandeen@redhat.com> 4.7.0-2
- Add libattr-devel build dependency to fix xfs_fsr

* Sun Sep 04 2016 Eric Sandeen <sandeen@redhat.com> 4.7.0-1
- New upstream release

* Tue Mar 15 2016 Eric Sandeen <sandeen@redhat.com> 4.5.0-1
- New upstream release

* Thu Mar 10 2016 Eric Sandeen <sandeen@redhat.com> 4.3.0-3
- Fix build w/ new kernels which have [sg]etxattr promotion

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov 30 2015 Eric Sandeen <sandeen@redhat.com> 4.3.0-1
- New upstream release

* Wed Sep 09 2015 Eric Sandeen <sandeen@redhat.com> 4.2.0-1
- New upstream release

* Thu Jul 30 2015 Eric Sandeen <sandeen@redhat.com> 3.2.4-1
- New upstream release
- Addresses CVE-2012-2150 for xfs_metadump

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 10 2015 Eric Sandeen <sandeen@redhat.com> 3.2.3-1
- New upstream release

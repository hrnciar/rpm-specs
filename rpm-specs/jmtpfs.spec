Summary:	FUSE and libmtp based filesystem for accessing MTP devices
Name:		jmtpfs
Version:	0.4
Release:	13%{?dist}
License:	GPLv3
URL:		http://research.jacquette.com/jmtpfs-exchanging-files-between-android-devices-and-linux/
Source:		http://research.jacquette.com/wp-content/uploads/2012/05/%{name}-%{version}.tar.gz
Patch0:		jmtpfs-0.4-unistd.patch
Patch1:		jmtpfs-0.4-fuse.patch
Requires:	%{_bindir}/fusermount
BuildRequires:	gcc-c++, fuse-devel >= 2.6, file-devel
%if 0%{?rhel} >= 7 || 0%{?fedora}
BuildRequires:	libmtp-devel >= 1.1.0
%else
BuildRequires:	libmtp11-devel >= 1.1.0
%endif

%description
jmtpfs is a FUSE and libmtp based filesystem for accessing MTP (Media
Transfer Protocol) devices. It was specifically designed for exchanging
files between Linux systems and newer Android devices that support MTP
but not USB Mass Storage.

The goal is to create a well behaved filesystem, allowing tools like
find and rsync to work as expected. MTP file types are set automatically
based on file type detection using libmagic. Setting the file appears to
be necessary for some Android apps, like Gallery, to be able to find and
use the files.

Since it is meant as an Android file transfer utility, the playlists and
other non-file based data are not supported.

%prep
%setup -q
%patch0 -p1 -b .unistd
%patch1 -p1 -b .fuse

%build
%configure
%make_build

%install
%make_install

%files
%license COPYING
%doc AUTHORS README
%{_bindir}/%{name}

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Dec 29 2015 Robert Scheck <robert@fedoraproject.org> 0.4-2
- Use libmtp11 on RHEL 6
- Added patch by Chris Caron to build with fuse on RHEL 6

* Thu Mar 14 2013 Robert Scheck <robert@fedoraproject.org> 0.4-1
- Upgrade to 0.4
- Initial spec file for Fedora and Red Hat Enterprise Linux

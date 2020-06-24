%global _hardened_build 1
%define download_dir 3310

Name:           pmount
Version:        0.9.23
Release:        17%{?dist}
Summary:        Enable normal user mount

# realpath.c is GPLv2+. Others are GPL+;
License:        GPLv2+
URL:            http://pmount.alioth.debian.org/
# BEWARE: The number in the url determines the content, ahs to be updated each time.
Source0:        http://alioth.debian.org/frs/download.php/%{download_dir}/%{name}-%{version}.tar.bz2
# don't set the setuid bits during make install
Patch0:         pmount-0.9.17-nosetuid.patch

BuildRequires:  gcc
BuildRequires:  intltool pkgconfig
BuildRequires:  e2fsprogs-devel
BuildRequires:  libblkid-devel
# ntfs-3g may be used too, it is considered optional, will be used if installed.
Requires:       cryptsetup-luks /bin/mount

%description
pmount  ("policy mount") is a wrapper around the standard mount program
which permits normal users to mount removable devices without a  
matching /etc/fstab entry.

Be warned that pmount is installed setuid root.


%prep
%setup -q
# patching src/Makefile.in; do not run automake:
%patch0 -p1 -b .nosetuid


%build
# mount, umount, cryptsetup and ntfs-3g paths are right and don't use rpm 
# macros, so the corresponding configure options are not used. /media/ is
# also rightly used.
%configure \
  --enable-hal=no \
  --with-lock-dir=%{_localstatedir}/lock/pmount \
  --with-whitelist=%{_sysconfdir}/pmount.allow

make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}

%find_lang %{name}


%files -f %{name}.lang
%doc AUTHORS README.devel COPYING ChangeLog
%config(noreplace) %{_sysconfdir}/pmount.allow
%attr(4755,root,root) %{_bindir}/pmount
%attr(4755,root,root) %{_bindir}/pumount
%{_mandir}/man1/p*mount*.1*


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.23-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.23-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.23-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.23-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.23-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.23-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.23-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.23-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.23-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.23-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.23-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.23-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.23-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue May 21 2013 Richard Shaw <hobbes1069@gmail.com> - 0.9.23-2
- Fix cflags to meet packaging guidelines for packages that contain suid
  binaries. Fixes BZ# 965459.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.23-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 10 2012 Richard Shaw <hobbes1069@gmail.com> - 0.9.23-1
- Update to latest upstream release.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.22-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Apr 21 2011 Vojtech Vitek (V-Teq) <vvitek@redhat.com> - 0.9.22-3
- Drop HAL support (Fedora 15 Features/HalRemoval)
- Remove TODO with obsolete information in favor of README.devel

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri May 28 2010 Jan Zeleny <jzeleny@redhat.com> - 0.9.22-1
- rebased to 0.9.22 (fixed #577614, calling luksClose correctly)

* Wed Sep 23 2009 Stepan Kasal <skasal@redhat.com> - 0.9.20-1
- new upstream version
- adjust BuildRequires

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.17-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Sep 25 2008 Patrice Dumas <pertusus@free.fr> 0.9.17-3
- rediff nosetuid patch

* Sat Mar  1 2008 Patrice Dumas <pertusus@free.fr> 0.9.17-2
- update to 0.9.17
- remove pmount-0.9.13-keeppublic.patch now that dbus connection is private

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.9.13-2
- Autorebuild for GCC 4.3

* Sun Sep 24 2006 Patrice Dumas <pertusus@free.fr> 0.9.13-1
- initial packaging

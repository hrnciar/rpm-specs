%global commit0 bd275a72f85a64eae0f7543603631c5f4891e70a
%global gittag0 v2015.1
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7}) 

Summary: Helper program for calling chroot(2) as non-root
Name: linux-user-chroot
Version: 2015.1
Release: 11%{?dist}
#VCS: git:git://git.gnome.org/linux-user-chroot
# I used "git archive" 
Source0: https://git.gnome.org/browse/linux-user-chroot/snapshot/linux-user-chroot-%{version}.tar.xz
License: GPLv2+
URL: https://git.gnome.org/browse/linux-user-chroot
BuildRequires: autoconf automake libtool
BuildRequires: kernel-headers
BuildRequires: pkgconfig(libseccomp)

%description
A tool made for build systems that run as non-root, offering chroot(2)
and Linux container features to non-root users.
Only install this on systems for which local, authenticated denial of
service attacks are not a serious concern.

%prep
%setup -q

%build
env NOCONFIGURE=1 ./autogen.sh
%configure --enable-documentation
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

%files
%attr(4755,root,root) %{_bindir}/linux-user-chroot
%{_mandir}/man8/*.gz

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2015.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2015.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2015.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2015.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2015.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2015.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2015.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2015.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2015.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2015.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Sep 06 2015 Colin Walters <walters@redhat.com> - 2015.1-1
- New upstream release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2013.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2013.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2013.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2013.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Feb 24 2013 Colin Walters <walters@verbum.org> - 2013.1-1
- New upstream release

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2012.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Aug 13 2012 Colin Walters <walters@verbum.org> - 2012.2-1
- Add changelog


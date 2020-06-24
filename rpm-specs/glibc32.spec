# glibc32 is maintained by the glibc team with support from tools.
%define original_name glibc
%define original_version 2.30
%define original_release 6
%define original_dist .fc31
# Increase build_number in each new build.
# When original version and/or release changes, set it back to 1.
%define build_number 1

%define debug_package %{nil}
Summary: The GNU libc libraries (32-bit)
Name: %{original_name}32
Version: %{original_version}
Release: %{original_release}.%{build_number}%{?dist}.1
License: LGPL
Group: System Environment/Libraries
Source: %{name}-%{original_version}-%{original_release}%{?original_dist}.tar.bz2
ExclusiveArch: x86_64

%description
This package is only used for internal building of multilib aware
packages, like gcc, due to a technical limitation in the distribution
build environment. Any package which needs both 32-bit and 64-bit
runtimes at the same time must install glibc32 (marked as a 64-bit
package) to access the 32-bit development files during a 64-bit build.

This package is not supported or intended for use outside of the
distribution build enviroment. Regular users can install both 32-bit and
64-bit runtimes and development file without any problems.

%prep
%setup -q -n %{name}-%{original_version}-%{original_release}%{?original_dist}

%build
for rpm_file in %{_target_cpu}/*.rpm; do
    rpm2cpio ${rpm_file} | cpio --extract --make-directories
done

%install
rm -rf "$RPM_BUILD_ROOT"
mkdir -p "$RPM_BUILD_ROOT"
mkdir -p "$RPM_BUILD_ROOT/lib"
mkdir -p "$RPM_BUILD_ROOT/usr"
mkdir -p "$RPM_BUILD_ROOT/usr/include/gnu"

cp -a lib "$RPM_BUILD_ROOT"
cp -a usr/lib "$RPM_BUILD_ROOT/usr/"
cp -a usr/include/gnu/stubs-*.h "$RPM_BUILD_ROOT/usr/include/gnu/"
rm -rf "$RPM_BUILD_ROOT"/usr/lib*/locale
rm -rf "$RPM_BUILD_ROOT"/usr/lib*/gconv
rm -rf "$RPM_BUILD_ROOT"/usr/lib*/.build-id

%clean
rm -rf "$RPM_BUILD_ROOT"

%files
%defattr(-,root,root)
/lib/*
/usr/lib/*
/usr/include/*

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.30-6.1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct  8 2019 Florian Weimer <fweimer@redhat.com> - 2.30-6.%{build_number}
- Update to glibc-2.30-6.fc31.
- Drop ppc64 and s390x support.  ppc64 is gone completely, and Fedora
  no longer has a 31-bit userland on s390x.
- Add scripts and instructions from downstream.
  Written by Carlos O'Donell.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.20-7.3.10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.20-7.3.9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.20-7.3.8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.20-7.3.7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 17 2017 Florian Weimer <fweimer@redhat.com> - 2.20-7.3.6
- Revert addition of glibc-static(x86-32) and glibc(x86-32) (#1482267)

* Wed Aug 16 2017 Peter Jones <pjones@redhat.com> - 2.20-7.3.5
- Make glibc32.x86_64 provide glibc-static(x86-32) and glibc(x86-32)

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.20-7.3.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.20-7.3.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed May 03 2017 Dan Horák <dan[at]danny.cz> - 2.20-7.3.2
- rebuilt for new arch (s390x)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.20-7.3.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Nov 30 2016 Petr Šabata <contyk@redhat.com> - 2.20-7.3
- Add the %%dist macro (needed for Modularity & Base Runtime)

* Tue Nov 22 2016 Dan Horák <dan[at]danny.cz> - 2.20-7.2
- rebuilt for new arch (ppc64)
- modernize spec

* Thu Jan 15 2015 Jakub Jelinek <jakub@redhat.com> 2.20-7.1
- add nss-softokn-freebl bits from 3.17.3-1 (i686 and s390) and
  3.16.0-2 (ppc)

* Thu Jan 15 2015 Jakub Jelinek <jakub@redhat.com> 2.20-7
- updated from 2.20-7 (i686 and s390) and 2.19.90-12 (ppc)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.18.90-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Feb 17 2014 Karsten Hopp <karsten@redhat.com> 2.18.90-2
- add libfreebl3.so from nss-softokn-freebl-3.15.4-1

* Sun Feb 16 2014 Karsten Hopp <karsten@redhat.com> 2.18.90-1
- updated from 2.18.90-27
- add some missing changelogs

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.11.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.11.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.11.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.11.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan 28 2010 Jakub Jelinek <jakub@redhat.com>
- updated from glibc-2.11.1-1 and nss-softokn-3.12.4-10.fc12

* Tue Jul 11 2006 Jakub Jelinek <jakub@redhat.com>
- updated from glibc-2.4.90-13

* Sat Feb  4 2006 Jakub Jelinek <jakub@redhat.com>
- updated from glibc-2.3.90-36

* Wed Feb 16 2005 Jakub Jelinek <jakub@redhat.com>
- updated from glibc-2.3.4-10
  - also include /usr/include/gnu/stubs-32.h

* Fri Oct 15 2004 Jakub Jelinek <jakub@redhat.com>
- updated from glibc-2.3.3-68

* Thu Jan 22 2004 Jakub Jelinek <jakub@redhat.com>
- updated from glibc-2.3.3-4

* Tue Apr 15 2003 Elliot Lee <sopwith@redhat.com>
- Update, add ppc64, cleanup install section

* Tue Mar  4 2003 Jakub Jelinek <jakub@redhat.com>
- update

* Sun Nov 10 2002 Jakub Jelinek <jakub@redhat.com>
- temporary package

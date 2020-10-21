%{?mingw_package_header}

Name:           mingw-jasper
Version:        2.0.22
Release:        2%{?dist}
Summary:        MinGW Windows Jasper library

License:        JasPer

URL:            http://www.ece.uvic.ca/~frodo/jasper/
Source0:        https://github.com/mdadams/jasper/archive/version-%{version}/jasper-%{version}.tar.gz

# MinGW-specific patches.
# Version the library
Patch1000:      jasper-libversion.patch
# This patch is a bit of a hack, but it's just there to fix a demo program:
Patch1001:      jasper-1.900.1-sleep.patch
# Add some missing exports, needed by mingw-gdal
Patch1002:      jasper-exports.patch

BuildArch:      noarch

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw64-binutils
BuildRequires:  mingw32-libjpeg
BuildRequires:  mingw64-libjpeg

BuildRequires:  cmake


%description
MinGW Windows Jasper library.


%package -n mingw32-jasper
Summary:        MinGW Windows Jasper library

%description -n mingw32-jasper
MinGW Windows Jasper library.


%package -n mingw32-jasper-static
Summary:        Static version of the MinGW Windows Jasper library
Requires:       mingw32-jasper = %{version}-%{release}

%description -n mingw32-jasper-static
Static version of the MinGW Windows Jasper library.


%package -n mingw64-jasper
Summary:        MinGW Windows Jasper library

%description -n mingw64-jasper
MinGW Windows Jasper library.


%package -n mingw64-jasper-static
Summary:        Static version of the MinGW Windows Jasper library
Requires:       mingw64-jasper = %{version}-%{release}

%description -n mingw64-jasper-static
Static version of the MinGW Windows Jasper library.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n jasper-version-%{version}


%build
jasper_cmake_args="-DJAS_ENABLE_DOC=OFF -DJAS_ENABLE_OPENGL=OFF -DJAS_ENABLE_AUTOMATIC_DEPENDENCIES=OFF"
# Build static
MINGW_BUILDDIR_SUFFIX=-static %mingw_cmake -DJAS_ENABLE_SHARED=OFF $jasper_cmake_args
MINGW_BUILDDIR_SUFFIX=-static %mingw_make_build
# Build shared
MINGW_BUILDDIR_SUFFIX=-shared %mingw_cmake -DJAS_ENABLE_SHARED=ON $jasper_cmake_args
MINGW_BUILDDIR_SUFFIX=-shared %mingw_make_build


%install
MINGW_BUILDDIR_SUFFIX=-static %mingw_make_install
MINGW_BUILDDIR_SUFFIX=-shared %mingw_make_install

# Remove documentation
rm -rf %{buildroot}%{mingw32_mandir}
rm -rf %{buildroot}%{mingw64_mandir}
rm -rf %{buildroot}%{mingw32_docdir}
rm -rf %{buildroot}%{mingw64_docdir}
rmdir %{buildroot}%{mingw32_datadir}
rmdir %{buildroot}%{mingw64_datadir}


%files -n mingw32-jasper
%license COPYRIGHT LICENSE
%{mingw32_bindir}/imgcmp.exe
%{mingw32_bindir}/imginfo.exe
%{mingw32_bindir}/jasper.exe
%{mingw32_bindir}/libjasper-4.dll
%{mingw32_libdir}/libjasper.dll.a
%{mingw32_libdir}/pkgconfig/jasper.pc
%{mingw32_includedir}/jasper/

%files -n mingw32-jasper-static
%{mingw32_libdir}/libjasper.a

%files -n mingw64-jasper
%license COPYRIGHT LICENSE
%{mingw64_bindir}/imgcmp.exe
%{mingw64_bindir}/imginfo.exe
%{mingw64_bindir}/jasper.exe
%{mingw64_bindir}/libjasper-4.dll
%{mingw64_libdir}/libjasper.dll.a
%{mingw64_libdir}/pkgconfig/jasper.pc
%{mingw64_includedir}/jasper/

%files -n mingw64-jasper-static
%{mingw64_libdir}/libjasper.a


%changelog
* Fri Oct 16 2020 Sandro Mani <manisandro@gmail.com> - 2.0.22-2
- Export symbols needed by mingw-gdal

* Wed Oct 07 2020 Sandro Mani <manisandro@gmail.com> - 2.0.22-1
- Update to 2.0.22

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 20 2020 Sandro Mani <manisandro@gmail.com> - 2.0.17-1
- Update to 2.0.17

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.16-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 13 2019 Sandro Mani <manisandro@gmail.com> - 2.0.16-5
- Export even more additional symbols, needed by mingw-gdal

* Wed Nov 13 2019 Sandro Mani <manisandro@gmail.com> - 2.0.16-4
- Export some additional symbols, needed by mingw-gdal

* Wed Oct 09 2019 Sandro Mani <manisandro@gmail.com> - 2.0.16-3
- Export some additional symbols, needed by mingw-gstreamer-plugins-bad-free

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 2.0.16-2
- Rebuild (Changes/Mingw32GccDwarf2)

* Fri Oct 04 2019 Sandro Mani <manisandro@gmail.com> - 2.0.16-1
- Update to 2.0.16

* Wed Aug 28 2019 Sandro Mani <manisandro@gmail.com> - 2.0.14-1
- Update to 2.0.14

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.900.28-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.900.28-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.900.28-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.900.28-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.900.28-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.900.28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Nov 23 2016 Michael Cronenworth <mike@cchtml.com> - 1.900.28-1
- Upstream release.
- Many security fixes:
     CVE-2016-9395, CVE-2016-9262, CVE-2016-8690, CVE-2016-8691,
     CVE-2016-8693, CVE-2016-2089, CVE-2015-5203, CVE-2015-5221, CVE-2016-8692,
     CVE-2016-1867, CVE-2016-1577, CVE-2016-2116

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.900.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.900.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jan 22 2015 Michael Cronenworth <mike@cchtml.com> - 1.900.1-26
- Fixes for CVE-2014-8157 and CVE-2014-8158

* Thu Dec 18 2014 Michael Cronenworth <mike@cchtml.com> - 1.900.1-25
- Fixes for CVE-2014-8137 and CVE-2014-8138

* Sat Dec 13 2014 Michael Cronenworth <mike@cchtml.com> - 1.900.1-24
- Apply all native patches for CVEs

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.900.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.900.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.900.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.900.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Mar 14 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.900.1-19
- Eliminated the libtool hack

* Wed Mar 14 2012 Kalev Lember <kalevlember@gmail.com> - 1.900.1-18
- Build 64 bit Windows binaries

* Fri Mar 09 2012 Kalev Lember <kalevlember@gmail.com> - 1.900.1-17
- Remove .la files

* Tue Mar 06 2012 Kalev Lember <kalevlember@gmail.com> - 1.900.1-16
- Renamed the source package to mingw-jasper (#800426)
- Spec clean up
- Use mingw macros without leading underscore

* Mon Feb 27 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.900.1-15
- Rebuild against the mingw-w64 toolchain

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.900.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 03 2011 Kalev Lember <kalev@smartlink.ee> - 1.900.1-13
- Rebuilt with mingw32-libjpeg-turbo

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.900.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Sep 18 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.900.1-11
- Rebuild because of broken mingw32-gcc/mingw32-binutils

* Thu Aug 27 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.900.1-10
- Rebuild for mingw32-libjpeg 7
- Automatically generate debuginfo subpackage
- Added -static subpackage
- Use %%global instead of %%define

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.900.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Mar  9 2009 Richard W.M. Jones <rjones@redhat.com> - 1.900.1-8
- Fix defattr line.
- Remove the enable-shared patch, and just use --enable-shared on
  the configure line.
- Disable the GL patch since OpenGL is disabled.
- Document what the patches are for in the spec file.
- Only patch Makefile.in so we don't have to rerun autotools, and
  remove autotools dependency.

* Fri Feb 20 2009 Richard W.M. Jones <rjones@redhat.com> - 1.900.1-7
- Rebuild for mingw32-gcc 4.4

* Fri Jan 23 2009 Richard W.M. Jones <rjones@redhat.com> - 1.900.1-6
- Use _smp_mflags.
- Disable static libraries.
- Include documentation.
- Use the same patches as Fedora native package.
- Just run autoconf instead of autoreconf so we don't upgrade libtool.
- +BR mingw32-dlfcn.
- Don't need the manual pages.

* Wed Sep 24 2008 Richard W.M. Jones <rjones@redhat.com> - 1.900.1-5
- Rename mingw -> mingw32.

* Mon Sep 22 2008 Daniel P. Berrange <berrange@redhat.com> - 1.900.1-4
- Add overflow patch from rawhide

* Thu Sep 11 2008 Daniel P. Berrange <berrange@redhat.com> - 1.900.1-3
- Run autoreconf after changing configure.ac script and add BRs for autotools

* Wed Sep 10 2008 Richard W.M. Jones <rjones@redhat.com> - 1.900.1-2
- Enable DLLs.
- Remove static libraries.

* Tue Sep  9 2008 Daniel P. Berrange <berrange@redhat.com> - 1.900.1-1
- Initial RPM release

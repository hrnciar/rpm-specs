Name:    gtkmathview
Version: 0.8.0
Release: 30%{?dist}
Summary: A MathML rendering library
License: LGPLv3+
URL:     http://helm.cs.unibo.it/mml-widget/
Source:  http://helm.cs.unibo.it/mml-widget/sources/gtkmathview-%{version}.tar.gz

Patch00: gtkmathview-0.8.0-gcc43.patch
Patch01: gtkmathview-0.8.0-includes.patch
Patch03: gtkmathview-marshalling-functions-git7d938a.patch
Patch04: gtkmathview-gcc-fixes-git3918e8.patch
Patch05: gtkmathview-fix-ComputerModernShaper-git210206.patch
Patch06: gtkmathview-lowercasegreek-gitb03152.patch
Patch07: gtkmathview-0.8.0-gcc47.patch
Patch08: gtkmathview-0.8.0-t1lib-private.patch
Patch09: gcc-6-build-fixes.patch
Patch10: gcc7-fix.diff
Patch11: fix-cpp-headers.patch
Patch12: missingLib.diff

BuildRequires: gcc-c++
BuildRequires: glib2-devel >= 2.2
BuildRequires: gtk2-devel >= 2.2
BuildRequires: libtool
BuildRequires: libxml2-devel >= 2.6.7
BuildRequires: libxslt >= 1.0.32
BuildRequires: pangox-compat-devel
BuildRequires: pkgconfig
BuildRequires: popt >= 1.7 
BuildRequires: popt-devel >= 1.7 
BuildRequires: t1lib-devel
Requires: lyx-fonts

%description
GtkMathView is a C++ rendering engine for MathML documents. 
It provides an interactive view that can be used for browsing 
and editing MathML markup.

%package  devel
Summary:  Support files necessary to compile applications using gtkmathview
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: glib2-devel >= 2.2.1
Requires: gtk2-devel >= 2.2.1
Requires: libxml2-devel >= 2.6.7
Requires: popt >= 1.7.0 
Requires: pkgconfig

%description devel
Libraries, headers, and support files needed for using gtkmathview.

%prep
%autosetup -p1

%build
# AM_BINRELOC missing, just ignore
echo 'AC_DEFUN([AM_BINRELOC], [])' > acinclude.m4
autoreconf -vif

export CXXFLAGS="%{optflags} -std=gnu++98"
export STDCXXFLAGS="%{optflags} -std=gnu++98"
%configure --disable-static
make %{?_smp_mflags} LIBTOOL=/usr/bin/libtool

%install
make DESTDIR=$RPM_BUILD_ROOT install
rm -f $RPM_BUILD_ROOT/%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/*.a

rm -f $RPM_BUILD_ROOT/%{_mandir}/man1/mathml2ps.1
rm -f $RPM_BUILD_ROOT/%{_mandir}/man1/mathmlviewer.1

%files
%license COPYING LICENSE
%doc README AUTHORS CONTRIBUTORS BUGS
%{_bindir}/*
%{_libdir}/lib*.so.*
%{_sysconfdir}/gtkmathview/
%{_datadir}/gtkmathview/

%files devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/mathview-core.pc
%{_libdir}/pkgconfig/mathview-frontend-libxml2.pc
%{_libdir}/pkgconfig/gtkmathview-custom-reader.pc
%{_libdir}/pkgconfig/gtkmathview-libxml2-reader.pc
%{_libdir}/pkgconfig/gtkmathview-libxml2.pc
%{_libdir}/pkgconfig/mathview-frontend-libxml2-reader.pc
%{_libdir}/pkgconfig/mathview-frontend-custom-reader.pc
%{_libdir}/pkgconfig/mathview-backend-svg.pc
%{_libdir}/pkgconfig/mathview-backend-gtk.pc
%{_libdir}/pkgconfig/mathview-backend-ps.pc
%{_includedir}/gtkmathview

%ldconfig_scriptlets

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 22 2020 Peter Robinson <pbrobinson@fedoraproject.org> 0.8.0-29
- Add isa to devel requires

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun  9 2019 Peter Robinson <pbrobinson@fedoraproject.org> 0.8.0-27
- Fix FTBFS, Build using gnu++98
- Sync patches from Debian
- Package cleanups

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.8.0-18
- Rebuilt for GCC 5 C++11 ABI change

* Sat Feb 21 2015 Till Maas <opensource@till.name> - 0.8.0-17
- Rebuilt for Fedora 23 Change
  https://fedoraproject.org/wiki/Changes/Harden_all_packages_with_position-independent_code

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Adam Jackson <ajax@redhat.com> 0.8.0-14
- Move t1lib from Libs: to Libs.private in pc files, it's an implementation
  detail, consumers (abiword) don't need to link against it themselves.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun May 19 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.8.0-12
- fix FTBFS
- Update SPEC

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Feb 27 2012 Tom Callaway <spot@fedoraproject.org> - 0.8.0-9
- apply fixes from git
- fix build with gcc 4.7

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jan 16 2010 Rex Dieter <rdieter@fedoraproject.org> - 0.8.0-6
- Requires: lyx-fonts

* Tue Aug 04 2009 Rex Dieter <rdieter@fedoraproject.org> - 0.8.0-5
- add lyx-fonts/mathml-fonts dep

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 28 2009 Caolán McNamara <caolanm@redhat.com> - 0.8.0-3
- add stdio.h for snprintf

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jul 29 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.8.0-1
- update to 0.8.0
- fix rpath
- fix gcc43 patch for 0.8.0

* Fri Mar 14 2008 Doug chapman <doug.chapman@hp.com> - 0.7.6-7
- fix GCC 4.3 build errors (BZ 434485)
- require popt-devel for build (BZ 426136)

* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.7.6-6
- Autorebuild for GCC 4.3

* Thu Oct 12 2006 Marc Maurer <uwog@abisource.com> 0.7.6-5.fc6
- Add pkgconfig to the -devel requires (bug 206451)

* Mon Sep 16 2006 Marc Maurer <uwog@abisource.com> 0.7.6-4.fc6
- Rebuild for FC 6

* Thu Feb 16 2006 Marc Maurer <uwog@abisource.com> 0.7.6-3.fc5
- Rebuild for Fedora Extras 5

* Sun Feb 05 2006 Marc Maurer <uwog@abisource.com> - 0.7.6-2.fc5
- Use %%{?dist} in the release name
- Omit static libs (part of bug 171971)
- s/gtkmathview/%%{name} (part of bug 171971)

* Sun Dec 11 2005 Marc Maurer <uwog@abisource.com> - 0.7.6-1
- Update to 0.7.6

* Sun Sep 25 2005 Marc Maurer <uwog@abisource.com> - 0.7.5-1
- Update to 0.7.5

* Mon Sep 12 2005 Marc Maurer <uwog@abisource.com> - 0.7.4-1
- Update to 0.7.4

* Tue Aug 30 2005 Marc Maurer <uwog@abisource.com> - 0.7.3-5
- Drop more unneeded Requires

* Tue Aug 30 2005 Marc Maurer <uwog@abisource.com> - 0.7.3-4
- Drop the explicit Requires

* Mon Aug 29 2005 Marc Maurer <uwog@abisource.com> - 0.7.3-3
- Use smaller lines in the Description field
- Remove the --disable-gmetadom and --without-t1lib flags
- Add a '/' to directories in the files section
- Remove the mathmlviewer man page

* Tue Aug 23 2005 Marc Maurer <uwog@abisource.com> - 0.7.3-2
- Add the proper Requires and Buildrequires
- Make the description field more descriptive
- Add CONTRIBUTORS BUGS LICENSE to the doc section
- Disable gmetadom and t1lib
- Remove the mathml2ps man page

* Sun Aug 14 2005 Marc Maurer <uwog@abisource.com> - 0.7.3-1
- Initial version

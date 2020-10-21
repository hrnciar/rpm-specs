Name: fmt-ptrn
Version: 1.3.22
Release: 17%{?dist}
License: GPLv2+
Source: http://www.flyn.org/projects/%name/%{name}-%{version}.tar.gz
URL: http://www.flyn.org
Summary: A simple template system
Requires: zlib
# No more gcj in Fedora?
#BuildRequires: glib2-devel, zlib-devel, java-1.8.0-gcj-devel, libgcj-devel, junit
BuildRequires:  gcc
BuildRequires: glib2-devel, zlib-devel

%description 
New is a template system, especially useful in conjunction with a 
simple text editor such as vi. The user maintains templates which 
may contain format strings. At run time, nf replaces the format 
strings in a template with appropriate values to create a new file.

For example, given the following template:


//   FILE: %%(FILE)
// AUTHOR: %%(FULLNAME)
//   DATE: %%(DATE)

// Copyright (C) 1999 %%(FULLNAME) %%(EMAIL)
// All rights reserved.
nf will create:


//   FILE: foo.cpp
// AUTHOR: W. Michael Petullo
//   DATE: 11 September 1999

// Copyright (C) 1999 W. Michael Petullo new@flyn.org
// All rights reserved.
on my computer.

The program understands plaintext or gziped template files.

The fmt-ptrn system also provides a shared library which allows a 
programmer access to nf's functionality. The system was developed to 
be light and fast. Its only external dependencies are the C library, 
glib2 and zlib.



%files 
%{_bindir}/*
%{_libdir}/libnewfmt-ptrn.so.1
%{_libdir}/libnewfmt-ptrn.so.%{version}
%{_libdir}/libnewtemplate.so.1
%{_libdir}/libnewtemplate.so.%{version}
%{_datadir}/fmt-ptrn
%{_mandir}/*/*
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README FAQ


%post
/sbin/ldconfig



%postun
/sbin/ldconfig


%package devel
Summary: Files needed to develop applications using fmt-ptrn's libraries
Requires: fmt-ptrn = %{version}-%{release}, glib2-devel, zlib-devel

%description devel
New is a template system, especially useful in conjunction with a 
simple text editor such as vi. The user maintains templates which 
may contain format strings. At run time, nf replaces the format 
strings in a template with appropriate values to create a new file. 
This package provides the libraries, include files, and other 
resources needed for developing applications using fmt-ptrn's API.



%files devel
%{_libdir}/pkgconfig/fmt-ptrn.pc
%{_includedir}/fmt-ptrn
%{_libdir}/libnewfmt-ptrn.so
%{_libdir}/libnewtemplate.so





#%package java
#Summary: Files needed to develop applications using fmt-ptrn's Java classes
#Group: Development/Libraries
#Requires: fmt-ptrn = %{version}-%{release}
#
#%description java
#New is a template system, especially useful in conjunction with a 
#simple text editor such as vi. The user maintains templates which 
#may contain format strings. At run time, nf replaces the format 
#strings in a template with appropriate values to create a new file. 
#This package provides the resources needed for developing applications 
#using fmt-ptrn's Java classes.
#
#
#
#%files java
#%defattr(-, root, root, -)
#%{_libdir}/libnewfmt-ptrnjni.so*
#%{_libdir}/libnewfmt-ptrnjava.so*
#%{_datadir}/java/*
#
#
#%post -n fmt-ptrn-java
#/sbin/ldconfig
#
#
#
#%postun -n fmt-ptrn-java
#/sbin/ldconfig


%prep


%setup -q


%build
 %configure  --disable-static --disable-java
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
rm -f ${RPM_BUILD_ROOT}%{_libdir}/libnewfmt-ptrn.la
rm -f ${RPM_BUILD_ROOT}%{_libdir}/libnewfmt-ptrnjni.la
rm -f ${RPM_BUILD_ROOT}%{_libdir}/libnewfmt-ptrnjava.la
rm -f ${RPM_BUILD_ROOT}%{_libdir}/libnewtemplate.la
# Delete the following 2 lines for building Java:
#rm -f ${RPM_BUILD_ROOT}%{_libdir}/libnewfmt-ptrnjni.*
#rm -f ${RPM_BUILD_ROOT}%{_datadir}/java/libnewfmt-ptrnjava.jar





%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.22-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.22-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.22-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.22-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.22-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.22-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.22-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.22-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.22-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Nov 24 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.22-8
- Move doc statement to files section

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.22-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.22-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.22-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jun 12 2014 W. Michael Petullo <mike@flyn.org> - 1.3.22-4
- Do not build Java stuff; it seems gcj is gone

* Thu Jun 12 2014 W. Michael Petullo <mike@flyn.org> - 1.3.22-3
- Build against Java 1.8

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Mar 20 2014 W. Michael Petullo <mike@flyn.org> - 1.3.22-1
- Updated to fmt-ptrn 1.3.22.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.21-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jan 26 2013 Kevin Fenzi <kevin@scrye.com> - 1.3.21-5
- Rebuild for new libgcj

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.21-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.21-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Feb 14 2010 W. Michael Petullo <mike[@]flyn.org - 1.3.21-1
- Updated to fmt-ptrn 1.3.21.

* Sun Feb 14 2010 W. Michael Petullo <mike[@]flyn.org - 1.3.20-5
- Change PACKAGE_VERSION to version.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.20-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Apr 25 2009 W. Michael Petullo <mike[@]flyn.org> - 1.3.20-3
- Fix ldconfig post for java package.

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild


* Sat Feb 14 2009 W. Michael Petullo <mike[@]flyn.org> - 1.3.20-1
- Updated to fmt-ptrn 1.3.20.

- Integrate stack_t solution upstream, pull previous patch.

* Thu Feb 12 2009 Caolán McNamara <caolanm@redhat.com> - 1.3.17-3
- rebuild for dependencies, rename stack_t to my_stack_t to avoid conflict with /usr/include/bits/sigstack.h's stack_t.

* Sun May 25 2008 W. Michael Petullo <mike[@]flyn.org> - 1.3.17-2
- Fixed placement of %%doc in RPM specification.

* Wed Apr 02 2008 W. Michael Petullo <mike[@]flyn.org> - 1.3.17-1
- Updated to fmt-ptrn 1.3.17.

* Tue Apr 01 2008 W. Michael Petullo <mike[@]flyn.org> - 1.3.16-1
- Updated to fmt-ptrn 1.3.16, should fix ppc64 build.

* Tue Apr 01 2008 W. Michael Petullo <mike[@]flyn.org> - 1.3.15-1
- Updated to fmt-ptrn 1.3.15.

* Tue Feb 12 2008 W. Michael Petullo <mike[@]flyn.org> - 1.3.14-1
- Updated to new 1.3.14.

* Mon Feb 11 2008 W. Michael Petullo <mike[@]flyn.org> - 1.3.13-2
- Update to use java-1.5.0-gcj-devel.

* Sat Dec 22 2007 W. Michael Petullo <mike[@]flyn.org> - 1.3.13-1
- Updated to new 1.3.13.

- License GPLv2+.

- Update make install command.

* Thu Dec 13 2007 W. Michael Petullo <mike[@]flyn.org> - 1.3.12-1
- Updated to new 1.3.12.

- Change package name to fmt-ptrn.

* Mon Oct 02 2007 W. Michael Petullo <mike[@]flyn.org> - 1.3.11-2
- Don't build static libraries.

* Tue Aug 21 2007 W. Michael Petullo <mike[@]flyn.org> - 1.3.11-1
- Updated to fmt-ptrn 1.3.11.

* Sun Aug 19 2007 W. Michael Petullo <mike[@]flyn.org> - 1.3.10-2
- Don't install INSTALL.

- Another %% fix.

- Run ldconfig for java package.

* Sat Aug 18 2007 W. Michael Petullo <mike[@]flyn.org> - 1.3.10-1
- Updated to new 1.3.10.

- Change license to GPLv2.

- Use %% in ChangeLog.

- Don't use %%makeinstall.

- deffattr(-,root,root,-).

- Don't install FmtPtrnTest.

- Don't use SMP build flags for now.

* Tue Aug 14 2007 W. Michael Petullo <mike[@]flyn.org> - 1.3.9-2
- Fix build (junit.o should not be distributed.)

* Sun Jul 29 2007 W. Michael Petullo <mike[@]flyn.org> - 1.3.9-1
- Updated to new 1.3.9.

- Build the Java package.

* Sun Sep 10 2006 W. Michael Petullo <mike[@]flyn.org> - 1.3.8-2
- BuildRequires Java tools.

* Sun Sep 10 2006 W. Michael Petullo <mike[@]flyn.org> - 1.3.8-1
- Updated to new 1.3.8.

- Create new Java package, comment out for now.

* Thu Sep 07 2006 W. Michael Petullo <mike[@]flyn.org> - 1.3.7-4
- Use _libdir macro for rm -rf of .a and .la (fix 64-bit build.)

* Thu Sep 07 2006 W. Michael Petullo <mike[@]flyn.org> - 1.3.7-3
- Rebuild for Fedora Extras 6.

* Fri Feb 17 2006 W. Michael Petullo <mike[@]flyn.org> - 1.3.7-2
- Rebuild for Fedora Extras 5.

* Thu Feb 02 2006 W. Michael Petullo <mike[@]flyn.org> - 1.3.7-1
- Updated to new 1.3.7.

* Wed Feb 01 2006 W. Michael Petullo <mike[@]flyn.org> - 1.3.6-1
- Updated to new 1.3.6.

* Sat Dec 24 2005  <W. Michael Petullo> - 1.3.5-3
- Add %%defattr for %%files devel.

* Tue Dec 13 2005 W. Michael Petullo <mike[@]flyn.org> - 1.3.5-2
- Broke out -devel package.

- Simplifies %%files block.

- Don't use %%doc %%{_mandir}.

- No empty NEWS or FAQ.

* Sun Dec 11 2005 W. Michael Petullo <mike[@]flyn.org> - 1.3.5-1
- Updated to new 1.3.5.

* Sun Dec 11 2005 W. Michael Petullo <mike[@]flyn.org> - 1.3.5-1
- Updated to new 1.3.5.





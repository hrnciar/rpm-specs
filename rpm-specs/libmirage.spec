Summary: A CD-ROM image access library
Name: libmirage
Version: 2.0.0
Release: 18%{?dist}
License: GPLv2+
URL: http://cdemu.sourceforge.net/pkg_libmirage.php
Source: http://downloads.sourceforge.net/cdemu/%{name}-%{version}.tar.bz2
BuildRequires: flex, bison
BuildRequires: libsndfile-devel
BuildRequires: glib2-devel
BuildRequires: gtk-doc
BuildRequires: zlib-devel
BuildRequires: cmake
BuildRequires: bzip2-devel
BuildRequires: gobject-introspection-devel
BuildRequires: xz-devel

%description
This is libMirage library, a CD-ROM image access library, and part of the
userspace-cdemu suite, a free, GPL CD/DVD-ROM device emulator for linux. It is
written in C and based on GLib.

The aim of libMirage is to provide uniform access to the data stored in
different image formats, by creating a representation of disc stored in image
file, which is based on GObjects.

%package devel
Summary: A CD-ROM image access library
Requires: pkgconfig
Requires: %{name} = %{version}-%{release}

%description devel
This is libMirage library, a CD-ROM image access library, and part of the
userspace-cdemu suite, a free, GPL CD/DVD-ROM device emulator for linux. It is
written in C and based on GLib.

This package contains files needed to develop with libMirage.

%prep
%setup -q

%build
%cmake .
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install INSTALL="%{__install} -p" DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/libmirage/*.la

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc AUTHORS COPYING README ChangeLog
%{_libdir}/libmirage.so.*
%{_libdir}/libmirage-2.0/*.so
%{_libdir}/girepository-1.0/*
%{_datadir}/mime/packages/*

%files devel
%{_libdir}/lib*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*
%{_datadir}/gir-1.0/*
%doc %{_datadir}/gtk-doc/html/*

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-18
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Rex Dieter <rdieter@fedoraproject.org> 2.0.0-6
- update mime scriptlets

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 22 2014 Kalev Lember <kalevlember@gmail.com> - 2.0.0-4
- Rebuilt for gobject-introspection 1.41.4

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Feb 18 2013 Jiri Moskovcak <jmoskovc@redhat.com> - 2.0.0-1
- updated to the latest upstream
- removed the gtk-doc requires from -devel package rhbz#604393
- Resolves: #604393

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Aug 25 2008 Jiri Moskovcak <jmoskovc@redhat.com> 1.1.0-3
- fixed post and postun in spec file

* Mon Aug 11 2008 Jiri Moskovcak <jmoskovc@redhat.com> - 1.1.0-2
- more spec file fixes:
    - added "-p" to install to preserve timestamps
    - removed shared-mime-info from Requires since it's not needed
    - added zlib-devel do BuildRequires

* Thu Aug  7 2008 Jiri Moskovcak <jmoskovc@redhat.com> - 1.1.0-1
- updated to latest version
- dropped ppc patch
- spec file cleanups:
    - fixed Source url
    - removed pkgconfig from BuildRequires
    - added shared-mime-info to Requires

* Mon Jul 28 2008 Jiri Moskovcak <jmoskovc@redhat.com> - 1.0.0-3
- spec file cleanups:
    - corrected URL
    - fixed versioned dependecies on pkgconfig
    - removed empty files from rpm
    - added gtk-doc to BuildRequires & Requires
    - license changed to GPLv2+

* Mon Jun 23 2008 Jiri Moskovcak <jmoskovc@redhat.com> - 1.0.0-2
- Initial Fedora release
- fixed issue with compiling on ppc

* Thu Dec 20 2007 Rok Mandeljc <rok.mandeljc@email.si> - 1.0.0-1
- Initial RPM release.

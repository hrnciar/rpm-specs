%{?mingw_package_header}

# first two digits of version
%define release_version %(echo %{version} | awk -F. '{print $1"."$2}')

%define po_package gtksourceview-3.0

Name:           mingw-gtksourceview3
Version:        3.24.11
Release:        5%{?dist}
Summary:        MinGW Windows library for viewing source files

# the library itself is LGPL, some .lang files are GPL
License:        LGPLv2+ and GPLv2+
URL:            http://www.gtk.org
Source0:        http://download.gnome.org/sources/gtksourceview/%{release_version}/gtksourceview-%{version}.tar.xz

BuildArch:      noarch

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw64-binutils
BuildRequires:  mingw32-gettext
BuildRequires:  mingw64-gettext
BuildRequires:  mingw32-gtk3
BuildRequires:  mingw64-gtk3
BuildRequires:  mingw32-libxml2
BuildRequires:  mingw64-libxml2

# Native one for msgfmt
BuildRequires:  gettext
# Native one for glib-genmarshal and glib-mkenums
BuildRequires:  glib2-devel
BuildRequires:  intltool

%description
GtkSourceView is a text widget that extends the standard GTK+
GtkTextView widget. It improves GtkTextView by implementing
syntax highlighting and other features typical of a source code editor.

This package contains the MinGW Windows cross compiled GtkSourceView library,
version 3.


%package -n     mingw32-gtksourceview3
Summary:        MinGW Windows library for viewing source files

%description -n mingw32-gtksourceview3
GtkSourceView is a text widget that extends the standard GTK+
GtkTextView widget. It improves GtkTextView by implementing
syntax highlighting and other features typical of a source code editor.

This package contains the MinGW Windows cross compiled GtkSourceView library,
version 3.


%package -n     mingw64-gtksourceview3
Summary:        MinGW Windows library for viewing source files

%description -n mingw64-gtksourceview3
GtkSourceView is a text widget that extends the standard GTK+
GtkTextView widget. It improves GtkTextView by implementing
syntax highlighting and other features typical of a source code editor.

This package contains the MinGW Windows cross compiled GtkSourceView library,
version 3.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n gtksourceview-%{version}


%build
%mingw_configure \
  --disable-static \
  --disable-gtk-doc \
  --disable-introspection

%mingw_make %{?_smp_mflags} V=1


%install
%mingw_make install DESTDIR=$RPM_BUILD_ROOT

# Remove .la files
rm $RPM_BUILD_ROOT%{mingw32_libdir}/*.la
rm $RPM_BUILD_ROOT%{mingw64_libdir}/*.la

# Remove documentation that duplicates what's in the native package
rm -rf $RPM_BUILD_ROOT%{mingw32_datadir}/gtk-doc
rm -rf $RPM_BUILD_ROOT%{mingw64_datadir}/gtk-doc

%mingw_find_lang %{po_package}


%files -n mingw32-gtksourceview3 -f mingw32-%{po_package}.lang
%license COPYING
%{mingw32_bindir}/libgtksourceview-3.0-1.dll
%{mingw32_includedir}/gtksourceview-3.0/
%{mingw32_libdir}/libgtksourceview-3.0.dll.a
%{mingw32_libdir}/pkgconfig/gtksourceview-3.0.pc
%{mingw32_datadir}/gtksourceview-3.0/

%files -n mingw64-gtksourceview3 -f mingw64-%{po_package}.lang
%license COPYING
%{mingw64_bindir}/libgtksourceview-3.0-1.dll
%{mingw64_includedir}/gtksourceview-3.0/
%{mingw64_libdir}/libgtksourceview-3.0.dll.a
%{mingw64_libdir}/pkgconfig/gtksourceview-3.0.pc
%{mingw64_datadir}/gtksourceview-3.0/


%changelog
* Wed Aug 12 13:39:52 GMT 2020 Sandro Mani <manisandro@gmail.com> - 3.24.11-5
- Rebuild (mingw-gettext)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.24.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 20 2020 Sandro Mani <manisandro@gmail.com> - 3.24.11-3
- Rebuild (gettext)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.24.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Aug 28 2019 Sandro Mani <manisandro@gmail.com> - 3.24.11-1
- Update to 3.24.11

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.24.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.24.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.24.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.24.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.24.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 19 2017 Kalev Lember <klember@redhat.com> - 3.24.3-1
- Update to 3.24.3

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.20.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue May 10 2016 Kalev Lember <klember@redhat.com> - 3.20.3-1
- Update to 3.20.3

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.18.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Oct 16 2015 Kalev Lember <klember@redhat.com> - 3.18.1-1
- Update to 3.18.1

* Fri Sep 25 2015 Kalev Lember <klember@redhat.com> - 3.18.0-1
- Update to 3.18.0

* Sun Aug 23 2015 Kalev Lember <klember@redhat.com> - 3.17.5-1
- Update to 3.17.5

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.16.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Apr 20 2015 Kalev Lember <kalevlember@gmail.com> - 3.16.1-1
- Update to 3.16.1

* Thu Mar 26 2015 Kalev Lember <kalevlember@gmail.com> - 3.16.0-1
- Update to 3.16.0
- Use license macro for the COPYING file

* Sat Nov 15 2014 Kalev Lember <kalevlember@gmail.com> - 3.14.2-1
- Update to 3.14.2

* Tue Oct 14 2014 Kalev Lember <kalevlember@gmail.com> - 3.14.1-1
- Update to 3.14.1

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.12.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 22 2014 Kalev Lember <kalevlember@gmail.com> - 3.12.2-1
- Update to 3.12.2

* Thu Sep 12 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 3.9.91-1
- Update to 3.9.91
- Fixes FTBFS against latest mingw-gtk3

* Sat Aug  3 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 3.8.1-4
- Make sure translations get installed to the correct folder (intltool bug #398571)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jun 16 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 3.8.1-2
- Rebuild to resolve InterlockedCompareExchange regression in mingw32 libraries

* Sun Jun 09 2013 Kalev Lember <kalevlember@gmail.com> - 3.8.1-1
- Update to 3.8.1

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Nov 28 2012 Kalev Lember <kalevlember@gmail.com> - 3.6.1-1
- Update to 3.6.1

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Apr 17 2012 Kalev Lember <kalevlember@gmail.com> - 3.4.1-1
- Update to 3.4.1

* Mon Mar 26 2012 Kalev Lember <kalevlember@gmail.com> - 3.4.0-1
- Update to 3.4.0

* Fri Mar 16 2012 Kalev Lember <kalevlember@gmail.com> - 3.2.0-5
- Build 64 bit Windows binaries

* Tue Feb 28 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 3.2.0-4
- Rebuild against the mingw-w64 toolchain

* Tue Jan 31 2012 Kalev Lember <kalevlember@gmail.com> - 3.2.0-3
- Rebuilt for libpng 1.5
- Remove .la files

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Sep 30 2011 Kalev Lember <kalevlember@gmail.com> - 3.2.0-1
- Update to 3.2.0

* Sat Aug 20 2011 Kalev Lember <kalevlember@gmail.com> - 3.1.4-2
- Explicitly disable introspection (#730781)
- Added comments about native buildrequires

* Mon Aug 15 2011 Kalev Lember <kalevlember@gmail.com> - 3.1.4-1
- Initial RPM release

%{?mingw_package_header}

Name:           mingw-gtkglext
Version:        1.2.0
Release:        23%{?dist}
Summary:        OpenGL Extension to GTK+

License:        LGPLv2
URL:            http://projects.gnome.org/gtkglext/
Source0:        http://downloads.sourceforge.net/sourceforge/gtkglext/gtkglext-%version.tar.bz2

# Patch 1:
#     remove pangox dependency
#
#     use correct glib mkenums patch
#         - https://bugzilla.gnome.org/show_bug.cgi?id=618599
#
#     don't use deprecated functions
#         - https://bugzilla.gnome.org/show_bug.cgi?id=618601
#
#     removed import declarations

Patch1:         gtkglext-1-fixes.patch


# Patch 2:
#    fix out of source tree builds

Patch2:         gtkglext-fix-out-of-source-builds.patch


BuildArch:      noarch

BuildRequires:  autoconf
BuildRequires:  libtool
BuildRequires:  gtk2-devel

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-pkg-config
BuildRequires:  mingw32-freeglut
BuildRequires:  mingw32-gtk2
BuildRequires:  mingw32-pthreads

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-pkg-config
BuildRequires:  mingw64-freeglut
BuildRequires:  mingw64-gtk2
BuildRequires:  mingw64-pthreads

%description
GtkGLExt is an OpenGL extension to GTK+. 
It provides additional GDK objects which support OpenGL rendering
in GTK+ and GtkWidget API add-ons to make GTK+ widgets OpenGL-capable.
This is a MinGW package.

# Win32
%package -n mingw32-gtkglext
Summary:       OpenGL Extension to GTK+ for the Win32 target

%description -n mingw32-gtkglext
GtkGLExt is an OpenGL extension to GTK+. 
It provides additional GDK objects which support OpenGL rendering
in GTK+ and GtkWidget API add-ons to make GTK+ widgets OpenGL-capable. 
Compiled for the Win32 target.

%package -n mingw32-gtkglext-static
Summary:       Static version of gtkglext, OpenGL Extension to GTK+ for the Win32 target
Requires:      mingw32-gtkglext = %{version}-%{release}

%description -n mingw32-gtkglext-static
GtkGLExt is an OpenGL extension to GTK+. 
It provides additional GDK objects which support OpenGL rendering
in GTK+ and GtkWidget API add-ons to make GTK+ widgets OpenGL-capable. 
Static version of gtkglext compiled for the Win32 target.

# Win64
%package -n mingw64-gtkglext
Summary:       OpenGL Extension to GTK+ for the Win64 target

%description -n mingw64-gtkglext
GtkGLExt is an OpenGL extension to GTK+. 
It provides additional GDK objects which support OpenGL rendering
in GTK+ and GtkWidget API add-ons to make GTK+ widgets OpenGL-capable. 
Compiled for the Win64 target.

%package -n mingw64-gtkglext-static
Summary:       Static version of gtkglext, OpenGL Extension to GTK+ for the Win64 target
Requires:      mingw64-gtkglext = %{version}-%{release}

%description -n mingw64-gtkglext-static
GtkGLExt is an OpenGL extension to GTK+. 
It provides additional GDK objects which support OpenGL rendering
in GTK+ and GtkWidget API add-ons to make GTK+ widgets OpenGL-capable. 
Static version of gtkglext compiled for the Win64 target.


%{?mingw_debug_package}


%prep
%setup -q -n gtkglext-%{version}
%patch1 -p1
%patch2 -p0
autoreconf -i --force

%build
%mingw_configure \
    --without-x \
    --with-gdktarget=win32

%mingw_make %{?_smp_mflags}

%install
%mingw_make_install DESTDIR=$RPM_BUILD_ROOT

# delete documentation
rm -rf $RPM_BUILD_ROOT/%{mingw32_datadir}/gtk-doc
rm -rf $RPM_BUILD_ROOT/%{mingw64_datadir}/gtk-doc

find $RPM_BUILD_ROOT -name "*.la" -delete

rm -Rf $RPM_BUILD_ROOT/%{mingw32_datadir}/aclocal
rm -Rf $RPM_BUILD_ROOT/%{mingw64_datadir}/aclocal

# Win32
%files -n mingw32-gtkglext
%{mingw32_bindir}/libgdkglext-win32-1.0-0.dll
%{mingw32_bindir}/libgtkglext-win32-1.0-0.dll
%{mingw32_includedir}/gtkglext-1.0/
%{mingw32_libdir}/libgdkglext-win32-1.0.dll.a
%{mingw32_libdir}/libgtkglext-win32-1.0.dll.a
%{mingw32_libdir}/gtkglext-1.0/
%{mingw32_libdir}/pkgconfig/gdkglext-1.0.pc
%{mingw32_libdir}/pkgconfig/gdkglext-win32-1.0.pc
%{mingw32_libdir}/pkgconfig/gtkglext-1.0.pc
%{mingw32_libdir}/pkgconfig/gtkglext-win32-1.0.pc

%doc COPYING COPYING.LIB

%files -n mingw32-gtkglext-static
%{mingw32_libdir}/libgtkglext-win32-1.0.a
%{mingw32_libdir}/libgdkglext-win32-1.0.a

# Win64
%files -n mingw64-gtkglext
%{mingw64_bindir}/libgdkglext-win32-1.0-0.dll
%{mingw64_bindir}/libgtkglext-win32-1.0-0.dll
%{mingw64_includedir}/gtkglext-1.0/
%{mingw64_libdir}/libgdkglext-win32-1.0.dll.a
%{mingw64_libdir}/libgtkglext-win32-1.0.dll.a
%{mingw64_libdir}/gtkglext-1.0/
%{mingw64_libdir}/pkgconfig/gdkglext-1.0.pc
%{mingw64_libdir}/pkgconfig/gdkglext-win32-1.0.pc
%{mingw64_libdir}/pkgconfig/gtkglext-1.0.pc
%{mingw64_libdir}/pkgconfig/gtkglext-win32-1.0.pc

%doc COPYING COPYING.LIB

%files -n mingw64-gtkglext-static
%{mingw64_libdir}/libgtkglext-win32-1.0.a
%{mingw64_libdir}/libgdkglext-win32-1.0.a


%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-23
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue May 21 2013 Marcel Wysocki <maci@satgnu.net> - 1.2.0-10
- add missing libtool BuildRequire

* Mon May 20 2013 Marcel Wysocki <maci@satgnu.net> - 1.2.0-9
- remove autoconf files
- spec cleanups
- added infos about patches

* Tue Apr 30 2013 Marcel Wysocki <maci@satgnu.net> - 1.2.0-8
- add gtk2-devel BR
- run autoreconf -i --force in prep

* Mon Apr 29 2013 Marcel Wysocki <maci@satgnu.net> - 1.2.0-7
- add gtkglext-fix-out-of-source-builds.patch

* Tue Apr 16 2013 Marcel Wysocki <maci@satgnu.net> - 1.2.0-6
- remove docs, there's already a native gtkglext package in Fedora
- remove mingw_find_lang line
- remove rm RPM_BUILD_ROOT line
- updated main summary

* Thu Jan 17 2013 Marcel Wysocki <maci@satgnu.net> - 1.2.0-5
- add autoconf to BR again, woops

* Thu Jan 17 2013 Marcel Wysocki <maci@satgnu.net> - 1.2.0-4
- add -static packages
- update summary and description
- update buildrequires
- follow https://fedoraproject.org/wiki/Packaging:MinGW

* Mon Jan 14 2013 Marcel Wysocki <maci@satgnu.net> - 1.2.0-3
- use mingw header macro
- build debuginfo packages

* Sun Jan 13 2013 Marcel Wysocki <maci@satgnu.net> - 1.2.0-2
- add autoconf BR

* Sat Jan 12 2013 Marcel Wysocki <maci@satgnu.net> - 1.2.0-1
- initial package



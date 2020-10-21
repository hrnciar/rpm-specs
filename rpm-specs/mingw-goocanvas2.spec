%{?mingw_package_header}

# first two digits of version
%define release_version %(echo %{version} | awk -F. '{print $1"."$2}')

Name:           mingw-goocanvas2
Version:        2.0.4
Release:        4%{?dist}
Summary:        MinGW Windows canvas library for GTK+

License:        LGPLv2+
URL:            https://wiki.gnome.org/Projects/GooCanvas
Source0:        https://download.gnome.org/sources/goocanvas/%{release_version}/goocanvas-%{version}.tar.xz

BuildArch:      noarch

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw64-binutils
BuildRequires:  mingw32-gtk3
BuildRequires:  mingw64-gtk3
# Native one for msgfmt
BuildRequires:  gettext
# Native one for glib-genmarshal and glib-mkenums
BuildRequires:  glib2-devel

%description
GooCanvas is a canvas widget for GTK+ that uses the cairo 2D library for
drawing.

This package contains the MinGW Windows cross compiled GooCanvas 2.0 library.


%package -n mingw32-goocanvas2
Summary:        MinGW Windows canvas library for GTK+

%description -n mingw32-goocanvas2
GooCanvas is a canvas widget for GTK+ that uses the cairo 2D library for
drawing.

This package contains the MinGW Windows cross compiled GooCanvas 2.0 library.


%package -n mingw64-goocanvas2
Summary:        MinGW Windows canvas library for GTK+

%description -n mingw64-goocanvas2
GooCanvas is a canvas widget for GTK+ that uses the cairo 2D library for
drawing.

This package contains the MinGW Windows cross compiled GooCanvas 2.0 library.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n goocanvas-%{version}


%build
export lt_cv_deplibs_check_method="pass_all"
%mingw_configure \
  --disable-static \
  --enable-python=no

%mingw_make %{?_smp_mflags} V=1


%install
%mingw_make install DESTDIR=$RPM_BUILD_ROOT

# Remove .la files
rm $RPM_BUILD_ROOT%{mingw32_libdir}/*.la
rm $RPM_BUILD_ROOT%{mingw64_libdir}/*.la

# Remove documentation which duplicates Fedora native
rm -rf $RPM_BUILD_ROOT%{mingw32_datadir}/gtk-doc
rm -rf $RPM_BUILD_ROOT%{mingw64_datadir}/gtk-doc

%mingw_find_lang goocanvas2


%files -n mingw32-goocanvas2 -f mingw32-goocanvas2.lang
%doc COPYING
%{mingw32_bindir}/libgoocanvas-2.0-9.dll
%{mingw32_includedir}/goocanvas-2.0/
%{mingw32_libdir}/libgoocanvas-2.0.dll.a
%{mingw32_libdir}/pkgconfig/goocanvas-2.0.pc

%files -n mingw64-goocanvas2 -f mingw64-goocanvas2.lang
%doc COPYING
%{mingw64_bindir}/libgoocanvas-2.0-9.dll
%{mingw64_includedir}/goocanvas-2.0/
%{mingw64_libdir}/libgoocanvas-2.0.dll.a
%{mingw64_libdir}/pkgconfig/goocanvas-2.0.pc


%changelog
* Wed Aug 12 13:37:33 GMT 2020 Sandro Mani <manisandro@gmail.com> - 2.0.4-4
- Rebuild (mingw-gettext)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Aug 28 2019 Sandro Mani <manisandro@gmail.com> - 2.0.4-1
- Update to 2.0.4

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Oct 04 2016 Kalev Lember <klember@redhat.com> - 2.0.2-4
- Update project URLs (#1380982)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Nov 15 2014 Kalev Lember <kalevlember@gmail.com> - 2.0.2-1
- Update to 2.0.2

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Mar 16 2012 Kalev Lember <kalevlember@gmail.com> - 2.0.1-4
- Build 64 bit Windows binaries

* Tue Feb 28 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.0.1-3
- Rebuild against the mingw-w64 toolchain

* Tue Jan 31 2012 Kalev Lember <kalevlember@gmail.com> - 2.0.1-2
- Removed .la files

* Fri Jan 27 2012 Kalev Lember <kalevlember@gmail.com> - 2.0.1-1
- Initial RPM release

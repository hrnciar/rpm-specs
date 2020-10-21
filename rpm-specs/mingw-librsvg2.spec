%{?mingw_package_header}

Name:           mingw-librsvg2
Version:        2.40.19
Release:        9%{?dist}
Summary:        SVG library based on cairo for MinGW

License:        LGPLv2+
URL:            https://wiki.gnome.org/Projects/LibRsvg
Source:         https://download.gnome.org/sources/librsvg/2.40/librsvg-%{version}.tar.xz

BuildArch:      noarch
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-gcc
BuildRequires:  mingw32-glib2
BuildRequires:  mingw64-glib2
BuildRequires:  mingw32-libcroco
BuildRequires:  mingw64-libcroco
BuildRequires:  mingw32-gdk-pixbuf
BuildRequires:  mingw64-gdk-pixbuf
BuildRequires:  mingw32-pango
BuildRequires:  mingw64-pango
BuildRequires:  mingw32-gtk3
BuildRequires:  mingw64-gtk3

# we need to call the host gdk-pixbuf-query-loaders executable
BuildRequires:  gdk-pixbuf2
BuildRequires:  perl-File-Temp

%description
An SVG library based on cairo for MinGW.

%package -n mingw32-librsvg2
Summary:        MinGW SVG library based on cairo
Requires:       pkgconfig

%description -n mingw32-librsvg2
This package contains the header files and libraries needed to develop
applications that use librsvg2.

%package -n mingw32-librsvg2-static
Summary:        MinGW SVG static library based on cairo
Requires:       mingw32-librsvg2 = %{version}-%{release}

%description -n mingw32-librsvg2-static
This package contains the static libraries needed to develop
applications that use librsvg2.

%package -n mingw64-librsvg2
Summary:        MinGW SVG library based on cairo
Requires:       pkgconfig

%description -n mingw64-librsvg2
This package contains the header files and libraries needed to develop
applications that use librsvg2.

%package -n mingw64-librsvg2-static
Summary:        MinGW static color daemon
Requires:       mingw64-librsvg2 = %{version}-%{release}

%description -n mingw64-librsvg2-static
This package contains the static libraries needed to develop
applications that use librsvg2.

%{?mingw_debug_package}


%prep
%setup -q -n librsvg-%{version}


%build
%mingw_configure                        \
        --without-pic                   \
        --enable-introspection=no
%mingw_make %{?_smp_mflags} V=1


%install
%mingw_make_install "DESTDIR=$RPM_BUILD_ROOT"


# Libtool files don't need to be bundled
find $RPM_BUILD_ROOT -name "*.la" -delete

# delete things we don't want/need
rm -rf $RPM_BUILD_ROOT%{mingw32_datadir}/man
rm -rf $RPM_BUILD_ROOT%{mingw64_datadir}/man

%files -n mingw32-librsvg2
%doc AUTHORS README NEWS
%license COPYING
%{mingw32_bindir}/librsvg-2-2.dll
%{mingw32_bindir}/rsvg-convert.exe
%{mingw32_bindir}/rsvg-view-3.exe
%{mingw32_includedir}/librsvg-2.0
%{mingw32_libdir}/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-svg.dll
%{mingw32_libdir}/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-svg.dll.a
%{mingw32_libdir}/librsvg-2.dll.a
%{mingw32_libdir}/pkgconfig/*.pc
%dir %{mingw32_datadir}/thumbnailers
%{mingw32_datadir}/thumbnailers/librsvg.thumbnailer

%files -n mingw32-librsvg2-static
%{mingw32_libdir}/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-svg.a
%{mingw32_libdir}/librsvg-2.a

%files -n mingw64-librsvg2
%doc AUTHORS README NEWS
%license COPYING
%{mingw64_bindir}/librsvg-2-2.dll
%{mingw64_bindir}/rsvg-convert.exe
%{mingw64_bindir}/rsvg-view-3.exe
%{mingw64_includedir}/librsvg-2.0
%{mingw64_libdir}/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-svg.dll
%{mingw64_libdir}/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-svg.dll.a
%{mingw64_libdir}/librsvg-2.dll.a
%{mingw64_libdir}/pkgconfig/*.pc
%dir %{mingw64_datadir}/thumbnailers
%{mingw64_datadir}/thumbnailers/librsvg.thumbnailer

%files -n mingw64-librsvg2-static
%{mingw64_libdir}/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-svg.a
%{mingw64_libdir}/librsvg-2.a

%changelog
* Wed Aug 12 13:43:13 GMT 2020 Sandro Mani <manisandro@gmail.com> - 2.40.19-9
- Rebuild (mingw-gettext)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.40.19-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 20 2020 Sandro Mani <manisandro@gmail.com> - 2.40.19-7
- Rebuild (gettext)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.40.19-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.40.19-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.40.19-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.40.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.40.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Oct 15 2017 Kalev Lember <klember@redhat.com> - 2.40.19-1
- Update to 2.40.19

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.40.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 20 2017 Kalev Lember <klember@redhat.com> - 2.40.18-1
- Update to 2.40.18

* Tue Jun 20 2017 Kalev Lember <klember@redhat.com> - 2.40.17-1
- Update to 2.40.17

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.40.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Sep 16 2016 Kalev Lember <klember@redhat.com> - 2.40.16-1
- Update to 2.40.16

* Tue May 03 2016 Kalev Lember <klember@redhat.com> - 2.40.15-1
- Update to 2.40.15

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.40.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Dec 02 2015 David King <amigadave@amigadave.com> - 2.40.12-1
- Update to 2.40.12

* Sat Nov 21 2015 David King <amigadave@amigadave.com> - 2.40.11-1
- Update to 2.40.11

* Sat Aug 29 2015 David King <amigadave@amigadave.com> - 2.40.10-1
- Update to 2.40.10

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.40.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr 21 2015 David King <amigadave@amigadave.com> - 2.40.9-1
- Update to 2.40.9

* Fri Mar 13 2015 David King <amigadave@amigadave.com> - 2.40.8-1
- Update to 2.40.8
- Use license macro for COPYING
- Update URL

* Wed Nov 19 2014 Richard Hughes <richard@hughsie.com> - 2.40.6-1
- Initial packaging attempt

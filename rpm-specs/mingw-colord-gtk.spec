%{?mingw_package_header}

Name:           mingw-colord-gtk
Version:        0.1.26
Release:        13%{?dist}
Summary:        MinGW GTK support library for colord

License:        GPLv2+ and LGPLv2+
URL:            http://www.freedesktop.org/software/colord/
Source0:        http://www.freedesktop.org/software/colord/releases/colord-gtk-%{version}.tar.xz

BuildArch:      noarch
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-gcc
BuildRequires:  mingw32-glib2
BuildRequires:  mingw64-glib2
BuildRequires:  mingw32-colord
BuildRequires:  mingw64-colord
BuildRequires:  mingw32-gtk3
BuildRequires:  mingw64-gtk3
BuildRequires:  intltool

%description
colord-gtk is a support library for colord and provides additional
functionality that requires GTK+.

This is the MinGW version of this library.

%package -n mingw32-colord-gtk
Summary:        MinGW GTK support library for colord
Requires:       pkgconfig

%description -n mingw32-colord-gtk
This package contains the header files and libraries needed to develop
applications that use libcolord.

%package -n mingw32-colord-gtk-static
Summary:        MinGW GTK static library for colord
Requires:       mingw32-colord-gtk = %{version}-%{release}

%description -n mingw32-colord-gtk-static
This package contains the static libraries needed to develop
applications that use libcolord-gtk.

%package -n mingw64-colord-gtk
Summary:        MinGW GTK support library for colord
Requires:       pkgconfig

%description -n mingw64-colord-gtk
This package contains the header files and libraries needed to develop
applications that use libcolord-gtk.

%package -n mingw64-colord-gtk-static
Summary:        MinGW GTK static library for colord
Requires:       mingw64-colord-gtk = %{version}-%{release}

%description -n mingw64-colord-gtk-static
This package contains the static libraries needed to develop
applications that use libcolord-gtk.

%{?mingw_debug_package}


%prep
%setup -q -n colord-gtk-%{version}


%build
%mingw_configure --without-pic
%mingw_make %{?_smp_mflags} V=1


%install
%mingw_make_install "DESTDIR=$RPM_BUILD_ROOT"

%mingw_find_lang colord-gtk

# Libtool files don't need to be bundled
find $RPM_BUILD_ROOT -name "*.la" -delete

# delete things we don't want/need
rm -rf $RPM_BUILD_ROOT%{mingw32_datadir}/man
rm -rf $RPM_BUILD_ROOT%{mingw64_datadir}/man

%files -n mingw32-colord-gtk -f mingw32-colord-gtk.lang
%doc AUTHORS COPYING README NEWS
%{mingw32_bindir}/cd-convert.exe
%{mingw32_bindir}/libcolord-gtk-1.dll
%{mingw32_includedir}/colord-1/colord-gtk
%{mingw32_includedir}/colord-1/*.h
%{mingw32_libdir}/libcolord-gtk.dll.a
%{mingw32_libdir}/pkgconfig/*.pc

%files -n mingw32-colord-gtk-static
%{mingw32_libdir}/libcolord-gtk.a

%files -n mingw64-colord-gtk -f mingw64-colord-gtk.lang
%doc AUTHORS COPYING README NEWS
%{mingw64_bindir}/cd-convert.exe
%{mingw64_bindir}/libcolord-gtk-1.dll
%{mingw64_includedir}/colord-1/colord-gtk
%{mingw64_includedir}/colord-1/*.h
%{mingw64_libdir}/libcolord-gtk.dll.a
%{mingw64_libdir}/pkgconfig/*.pc

%files -n mingw64-colord-gtk-static
%{mingw64_libdir}/libcolord-gtk.a

%changelog
* Wed Aug 12 13:35:26 GMT 2020 Sandro Mani <manisandro@gmail.com> - 0.1.26-13
- Rebuild (mingw-gettext)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.26-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 20 2020 Sandro Mani <manisandro@gmail.com> - 0.1.26-11
- Rebuild (gettext)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.26-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.26-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.26-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.26-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.26-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.26-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.26-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.26-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Nov 19 2014 Richard Hughes <richard@hughsie.com> - 0.1.26-1
- Initial packaging attempt

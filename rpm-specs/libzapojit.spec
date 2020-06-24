%global api 0.0
%global glib2_version 2.28
%global libsoup_version 2.38

Name:           libzapojit
Version:        0.0.3
Release:        17%{?dist}
Summary:        GLib/GObject wrapper for the OneDrive and Hotmail REST APIs

License:        LGPLv2+
URL:            https://wiki.gnome.org/Projects/Zapojit
Source0:        http://download.gnome.org/sources/%{name}/%{api}/%{name}-%{version}.tar.xz

BuildRequires:  gettext
BuildRequires:  pkgconfig(gio-2.0) >= %{glib2_version}
BuildRequires:  pkgconfig(glib-2.0) >= %{glib2_version}
BuildRequires:  pkgconfig(gobject-2.0) >= %{glib2_version}
BuildRequires:  pkgconfig(goa-1.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  gtk-doc
BuildRequires:  intltool
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libsoup-2.4) >= %{libsoup_version}
BuildRequires:  libtool
BuildRequires:  pkgconfig(rest-0.7)
Requires:       gobject-introspection

%description
GLib/GObject wrapper for the OneDrive and Hotmail REST APIs. It supports
OneDrive file and folder objects, and the following OneDrive operations:
  - Deleting a file, folder or photo.
  - Listing the contents of a folder.
  - Reading the properties of a file, folder or photo.
  - Uploading files and photos.

%package        devel
Summary:        Development files for %{name}
Requires:       gobject-introspection-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q


%build
%configure \
  --disable-silent-rules \
  --disable-static \
  --enable-gtk-doc \
  --enable-introspection

# Omit unused direct shared library dependencies.
sed --in-place --expression 's! -shared ! -Wl,--as-needed\0!g' libtool

%make_build


%install
%make_install

find $RPM_BUILD_ROOT -name '*.la' -delete
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/%{name}

%ldconfig_scriptlets


%files
%doc AUTHORS
%doc COPYING
%doc ChangeLog
%doc NEWS
%doc README
%{_libdir}/%{name}-%{api}.so.*

%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/Zpj-%{api}.typelib

%files devel
%{_libdir}/%{name}-%{api}.so
%{_libdir}/pkgconfig/zapojit-%{api}.pc

%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/Zpj-%{api}.gir

%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%doc %{_datadir}/gtk-doc/html/%{name}-%{api}

%dir %{_includedir}/%{name}-%{api}
%{_includedir}/%{name}-%{api}/zpj


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Oct 03 2016 Debarshi Ray <rishi@fedoraproject.org> - 0.0.3-9
- Update URL
- Replace SkyDrive with OneDrive
- Use pkgconfig(...) for BRs
- Use %%make_build and %%make_install macros

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 22 2014 Kalev Lember <kalevlember@gmail.com> - 0.0.3-5
- Rebuilt for gobject-introspection 1.41.4

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Nov 28 2013 Debarshi Ray <rishi@fedoraproject.org> - 0.0.3-3
- Use %%global instead of %%define
- Drop redundant Requires: pkgconfig from devel

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Mar 08 2013 Debarshi Ray <rishi@fedoraproject.org> - 0.0.3-1
- Update to 0.0.3.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 08 2012 Debarshi Ray <rishi@fedoraproject.org> - 0.0.2-2
- Co-own %%{_libdir}/girepository-1.0 and %%{_datadir}/gir-1.0.
- Remove Group tag and %%defattr.

* Wed Jun 06 2012 Debarshi Ray <rishi@fedoraproject.org> - 0.0.2-1
- Update to 0.0.2.

* Wed May 30 2012 Debarshi Ray <rishi@fedoraproject.org> - 0.0.1-1
- Initial spec.

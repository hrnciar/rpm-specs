Name:           gnome-books
Version:        3.34.0
Release:        5%{?dist}
Summary:        E-Book Manager

License:        GPLv2+
URL:            https://wiki.gnome.org/Apps/Books
Source0:        https://download.gnome.org/sources/gnome-books/3.34/gnome-books-%{version}.tar.xz

BuildRequires:  docbook-style-xsl
BuildRequires:  gcc
BuildRequires:  librsvg2
BuildRequires:  meson
BuildRequires:  pkgconfig(evince-document-3.0)
BuildRequires:  pkgconfig(evince-view-3.0)
BuildRequires:  pkgconfig(gjs-1.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gnome-desktop-3.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libgepub-0.6)
BuildRequires:  pkgconfig(tracker-control-2.0)
BuildRequires:  pkgconfig(tracker-sparql-2.0)
BuildRequires:  pkgconfig(webkit2gtk-4.0)
BuildRequires:  /usr/bin/appstream-util
BuildRequires:  /usr/bin/desktop-file-validate

Requires:       gettext%{?isa}
Requires:       gnome-epub-thumbnailer
Requires:       libgepub%{?_isa}

%description
Books is a simple application to access and organize your e-books on GNOME. It
is meant to be a simple and elegant replacement for using a file manager to
deal with e-books.


%prep
%autosetup -p1


%build
%meson
%meson_build


%install
%meson_install

%find_lang gnome-books


%check
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_datadir}/metainfo/org.gnome.Books.appdata.xml
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/org.gnome.Books.desktop


%files -f gnome-books.lang
%license COPYING
%doc README.md
%{_bindir}/gnome-books
%{_libdir}/gnome-books/
%{_datadir}/applications/org.gnome.Books.desktop
%{_datadir}/dbus-1/services/org.gnome.Books.service
%{_datadir}/glib-2.0/schemas/org.gnome.Books.enums.xml
%{_datadir}/glib-2.0/schemas/org.gnome.books.gschema.xml
%{_datadir}/gnome-books/
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Books.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.Books-symbolic.svg
%{_datadir}/metainfo/org.gnome.Books.appdata.xml
%{_mandir}/man1/gnome-books.1*


%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.34.0-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.34.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.34.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 16 2020 Kalev Lember <klember@redhat.com> - 3.34.0-2
- Rebuilt for libgnome-desktop soname bump

* Fri Sep 06 2019 Kalev Lember <klember@redhat.com> - 3.34.0-1
- Update to 3.34.0

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.32.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jul 21 2019 Kalev Lember <klember@redhat.com> - 3.32.0-4
- Rebuilt for libgnome-desktop soname bump

* Tue Apr 16 2019 Adam Williamson <awilliam@redhat.com> - 3.32.0-3
- Rebuild with Meson fix for #1699099

* Wed Apr 10 2019 Kalev Lember <klember@redhat.com> - 3.32.0-2
- Add appdata and desktop file validation (#1698489)

* Wed Apr 10 2019 Kalev Lember <klember@redhat.com> - 3.32.0-1
- Initial Fedora packaging

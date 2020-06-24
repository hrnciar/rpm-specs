%global apiver 5

Name:           tepl
Version:        4.99.2
Release:        1%{?dist}
Summary:        Text editor product line

License:        LGPLv2+
URL:            https://wiki.gnome.org/Projects/Tepl
Source0:        https://download.gnome.org/sources/tepl/4.99/tepl-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:  pkgconfig(amtk-5)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtksourceview-4)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(uchardet)

# the -tests subpackage was removed in F33
Obsoletes:      tepl-tests < 4.99.2

%description
Tepl is a library that eases the development of GtkSourceView-based text
editors and IDEs. Tepl is the acronym for “Text editor product line”.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup


%build
%meson -Dgtk_doc=true
%meson_build


%install
%meson_install

%find_lang tepl-%{apiver}


%files -f tepl-%{apiver}.lang
%license LICENSES/*
%doc AUTHORS NEWS README
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/Tepl-%{apiver}.typelib
%{_libdir}/libtepl-%{apiver}.so.0*

%files devel
%{_includedir}/tepl-%{apiver}/
%{_libdir}/libtepl-%{apiver}.so
%{_libdir}/pkgconfig/tepl-%{apiver}.pc
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/Tepl-%{apiver}.gir
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%{_datadir}/gtk-doc/html/tepl-%{apiver}/


%changelog
* Fri May 29 2020 Kalev Lember <klember@redhat.com> - 4.99.2-1
- Update to 4.99.2
- Switch to the meson build system
- Drop the -tests subpackage (installed tests removed upstream)
- Remove old gtef obsoletes

* Thu Mar 05 2020 Kalev Lember <klember@redhat.com> - 4.4.0-1
- Update to 4.4.0

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 02 2019 Kalev Lember <klember@redhat.com> - 4.3.1-1
- Update to 4.3.1

* Wed Nov 27 2019 Kalev Lember <klember@redhat.com> - 4.2.1-1
- Update to 4.2.1

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 11 2019 Phil Wyett <philwyett@kathenas.org> - 4.2.0-1
- Update to 4.2.0

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Aug 04 2018 Kalev Lember <klember@redhat.com> - 3.0.0-4
- Obsolete gtef (#1612444)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Oct 29 2017 Kalev Lember <klember@redhat.com> - 3.0.0-1
- Initial Fedora packaging

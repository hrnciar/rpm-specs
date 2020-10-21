Name:           libhandy1
Version:        1.0.0
Release:        2%{?dist}
Summary:        Building blocks for modern adaptive GNOME apps

License:        LGPLv2+
URL:            https://gitlab.gnome.org/GNOME/libhandy
Source0:        https://download.gnome.org/sources/libhandy/1.0/libhandy-%{version}.tar.xz

# https://gitlab.gnome.org/GNOME/libhandy/-/merge_requests/607
Patch0:         0001-glade-add-conditional-support-for-gladeui-3.37.patch

BuildRequires:  gcc
BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gladeui-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.24.1

%description
libhandy provides GTK+ widgets and GObjects to ease developing
applications for mobile phones.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n libhandy-%{version} -p1


%build
%meson -Dgtk_doc=true -Dexamples=false
%meson_build


%install
%meson_install

%find_lang libhandy libhandy.lang


%files -f libhandy.lang
%license COPYING
%doc README.md

%{_libdir}/girepository-1.0/
%{_libdir}/libhandy-1.so.0

%files devel
%{_includedir}/libhandy-1/

%{_libdir}/glade/
%{_libdir}/libhandy-1.so
%{_libdir}/pkgconfig/libhandy-1.pc

%{_datadir}/gir-1.0/
%{_datadir}/glade/
%{_datadir}/gtk-doc/
%{_datadir}/vala/


%changelog
* Sun Sep 13 2020 Kalev Lember <klember@redhat.com> - 1.0.0-2
- Rebuilt for libgladeui soname bump

* Tue Sep 08 2020 Kalev Lember <klember@redhat.com> - 1.0.0-1
- Update to 1.0.0

* Fri Sep 04 2020 Kalev Lember <klember@redhat.com> - 0.91.0-1
- Update to 0.91.0

* Thu Sep 03 2020 Fabio Valentini <decathorpe@gmail.com> - 0.90.0-2
- Add patch to support gladeui >= 3.37.

* Fri Aug 07 2020 Fabio Valentini <decathorpe@gmail.com> - 0.90.0-1
- Update to version 0.90.0.

* Fri Jul 31 2020 Kalev Lember <klember@redhat.com> - 0.85.0-1
- Update to 0.85.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.84.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 21 2020 Kalev Lember <klember@redhat.com> - 0.84.0-1
- Update to 0.84.0

* Mon Jun 22 2020 Kalev Lember <klember@redhat.com> - 0.82.0-1
- Update to 0.82.0

* Thu May 28 2020 Fabio Valentini <decathorpe@gmail.com> - 0.80.0-1
- Initial package for libhandy1.

%bcond_with gtk4

Name:           gthree
Version:        0.9.0
Release:        2%{?dist}
Summary:        Gthree is a GObject/Gtk+ port of three.js

License:        MIT
URL:            https://github.com/alexlarsson/gthree
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
ExcludeArch:    i686

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(epoxy) >= 1.4
BuildRequires:  pkgconfig(glib-2.0) >= 2.43.2
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(graphene-1.0) >= 1.10.2
BuildRequires:  pkgconfig(graphene-gobject-1.0) >= 1.10.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22
BuildRequires:  pkgconfig(json-glib-1.0) >= 1.2.0
%if %{with gkt4}
BuildRequires:  pkgconfig(gtk4) >= 3.96
%endif

Recommends:     %{name}-gtk3%{?_isa}
%if %{with gkt4}
Recommends:     %{name}-gtk4%{?_isa}
%endif

Suggests:       %{name}-examples

%description
Gthree is a port of three.js to GObject and Gtk3. The code is a partial copy of
three.js, and the API is very similar, although it only supports OpenGL.

For information about three.js, see: http://threejs.org


# Devel package
%package        devel
Summary:        Devel files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-gtk3%{?_isa} = %{version}-%{release}
%if %{with gkt4}
Requires:       %{name}-gtk4%{?_isa} = %{version}-%{release}
%endif

%description    devel
Devel files for %{name}.


# Examples package
%package        examples
Summary:        Example files for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description    examples
Example files for %{name}.


# GTK3 package
%package        gtk3
Summary:        GTK 3 supprort for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    gtk3
GTK 3 supprort for %{name}.


%if %{with gkt4}
# GTK4 package
%package        gtk4
Summary:        GTK 4 supprort for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    gtk4
GTK 4 supprort for %{name}.
%endif


%prep
%autosetup


%build
%if %{with gkt4}
%meson -Dgtk4=true
%else
%meson
%endif

%meson_build


%install
%meson_install


%files
%license COPYING
%doc README NEWS
%{_libdir}/girepository-1.0/Gthree-1.0.typelib
%{_libdir}/libgthree-1.so.0*

%files devel
%{_datadir}/gir-1.0/Gthree-1.0.gir
%{_datadir}/gir-1.0/GthreeGtk3-1.0.gir
%{_includedir}/%{name}-1.0
%{_includedir}/%{name}-gtk3-1.0/%{name}/gthreearea.h
%{_libdir}/libgthree-1.so
%{_libdir}/libgthree-gtk3-1.so
%{_libdir}/pkgconfig/%{name}-1.0.pc
%{_libdir}/pkgconfig/%{name}-gtk3-1.0.pc

%files gtk3
%{_libdir}/libgthree-gtk3-1.so.0*
%{_libdir}/girepository-1.0/GthreeGtk3-1.0.typelib

%if %{with gkt4}
%files gtk4
# DUMMY
%endif

%files examples
%{_datadir}/%{name}-examples/


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 24 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.9.0-1
- Update to 0.9.0
- No longer exclude 'armv7hl' arch

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Sep 11 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.2.0-2
- Add temporary 'ExcludeArch' for armv7hl and i686

* Mon Sep 09 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.2.0-1
- Update to 0.2.0

* Mon Sep 02 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.1.0-1.20190825git400d8bb
- Update to latest git snapshot

* Wed Jun 05 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0-9.20190808gita38a231
- Initial package

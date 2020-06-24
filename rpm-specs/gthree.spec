# Enable LTO
%global optflags        %{optflags} -flto
%global build_ldflags   %{build_ldflags} -flto

Name:           gthree
Version:        0.2.0
Release:        3%{?dist}
Summary:        Gthree is a GObject/Gtk+ port of three.js

License:        MIT
URL:            https://github.com/alexlarsson/gthree
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
ExcludeArch:    armv7hl i686

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(epoxy) >= 1.4
BuildRequires:  pkgconfig(glib-2.0) >= 2.43.2
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(graphene-1.0)
BuildRequires:  pkgconfig(graphene-gobject-1.0) >= 1.10.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22
BuildRequires:  pkgconfig(json-glib-1.0) >= 1.2.0

%description
Gthree is a port of three.js to GObject and Gtk3. The code is a partial copy of
three.js, and the API is very similar, although it only supports OpenGL.

For information about three.js, see: http://threejs.org


%package        devel

Summary:        Devel files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Devel files for %{name}.


%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install

%files
%license COPYING
%doc README
%{_libdir}/girepository-1.0/Gthree-1.0.typelib
%{_libdir}/libgthree-1.so.0*

%files devel
%{_datadir}/gir-1.0/Gthree-1.0.gir
%{_includedir}/%{name}-1.0
%{_libdir}/libgthree-1.so
%{_libdir}/pkgconfig/%{name}-1.0.pc

%changelog
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

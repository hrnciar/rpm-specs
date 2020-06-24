%global apiver  0

Name:           gtk-layer-shell
Version:        0.1.0
Release:        3%{?dist}
Summary:        Library to create components for Wayland using the Layer Shell

License:        MIT
URL:            https://github.com/wmww/gtk-layer-shell
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-wayland-3.0) >= 3.22.0
BuildRequires:  pkgconfig(wayland-client) >= 1.10.0
BuildRequires:  pkgconfig(wayland-scanner) >= 1.10.0

%description
A library to write GTK applications that use Layer Shell. Layer Shell is a
Wayland protocol for desktop shell components, such as panels, notifications
and wallpapers. You can use it to anchor your windows to a corner or edge of
the output, or stretch them across the entire output. This library only makes
sense on Wayland compositors that support Layer Shell, and will not work on
X11. It supports all Layer Shell features including popups and popovers
(GTK popups Just Work™). Please open issues for any bugs you come across.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files for %{name}.


%prep
%autosetup


%build
%meson
%meson_build


%install
%meson_install


%files
%license COPYING
%doc README.md
%{_libdir}/lib%{name}.so.%{apiver}*
%{_libdir}/girepository-1.0/GtkLayerShell-%{apiver}.?.typelib

%files devel
%{_includedir}/%{name}
%{_libdir}/pkgconfig/*.pc
%{_libdir}/lib%{name}.so
%{_datadir}/gir-1.0/GtkLayerShell-%{apiver}.?.gir


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Sep 26 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.1.0-2
- Cosmetic fixes

* Thu Sep 26 2019 gasinvein <gasinvein@gmail.com>
- Initial package

%global lib_ver     0.14
%global name_ver    0_14-0

%global optflags        %{optflags} -flto
%global build_ldflags   %{build_ldflags} -flto

Name:           retro-gtk
Version:        0.18.1
Release:        2%{?dist}
Summary:        The GTK+ Libretro frontend framework

License:        GPLv3+
URL:            https://gitlab.gnome.org/GNOME/retro-gtk
Source0:        %{url}/-/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(epoxy)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.50
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 0.6.7
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libpulse-simple)
BuildRequires:  pkgconfig(vapigen)

%description
Libretro is a plugin format design to implement video game console emulators,
video games and similar multimedia software. Such plugins are called Libretro
cores.

retro-gtk is a framework easing the usage of Libretro cores in conjunction with
GTK+.


%package     -n libretro-gtk-%{name_ver}
Summary:        The GTK+ Libretro frontend framework

Recommends:     libretro-beetle-ngp%{?_isa}
Recommends:     libretro-beetle-pce-fast%{?_isa}
Recommends:     libretro-beetle-vb%{?_isa}
Recommends:     libretro-beetle-wswan%{?_isa}
Recommends:     libretro-bsnes-mercury%{?_isa}
Recommends:     libretro-desmume2015%{?_isa}
Recommends:     libretro-gambatte%{?_isa}
Recommends:     libretro-handy%{?_isa}
Recommends:     libretro-mgba%{?_isa}
Recommends:     libretro-nestopia%{?_isa}
Recommends:     libretro-pcsx-rearmed%{?_isa}
Recommends:     libretro-prosystem%{?_isa}
Recommends:     libretro-stella2014%{?_isa}

%description -n libretro-gtk-%{name_ver}
Libretro is a plugin format design to implement video game console emulators,
video games and similar multimedia software. Such plugins are called Libretro
cores.

retro-gtk is a framework easing the usage of Libretro cores in conjunction with
GTK+.

(libretro is an API specification implemented by some emulator libraries like
libretro-bsnes).


%package     -n typelib-1_0-Retro-%{name_ver}
Summary:        GObject introspection bindings for libretro-gtk

%description -n typelib-1_0-Retro-%{name_ver}
retro-gtk wraps the libretro API for use in Gtk applications.

This subpackage contains the gobject bindings for the libretro-gtk shared
library.


%package        devel
Summary:        Development files for %{name}
Requires:       libretro-gtk-%{name_ver}%{?_isa} = %{version}
Requires:       typelib-1_0-Retro-%{name_ver}%{?_isa} = %{version}

%description    devel
This subpackage contains the headers to make use of the libretro-gtk library.


%prep
%autosetup


%build
%meson
%meson_build


%install
%meson_install


%files -n libretro-gtk-%{name_ver}
%license COPYING
%doc AUTHORS NEWS README.md
%{_libdir}/libretro-gtk-%{lib_ver}.so.0

%files -n typelib-1_0-Retro-%{name_ver}
%{_libdir}/girepository-1.0/Retro-%{lib_ver}.typelib

%files devel
%{_bindir}/retro-demo
%{_datadir}/gir-1.0/Retro-%{lib_ver}.gir
%{_datadir}/vala/vapi/%{name}-%{lib_ver}*
%{_includedir}/%{name}/
%{_libdir}/libretro-gtk-%{lib_ver}.so
%{_libdir}/pkgconfig/%{name}-%{lib_ver}.pc


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 19 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.18.1-1
- Update to 0.18.1

* Thu Dec 12 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.18.0-3
- Add pcsx-rearmed core

* Wed Oct 09 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.18.0-2
- Add libretro cores as weak deps

* Fri Sep 13 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.18.0-1
- Update to 0.18.0

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 15 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.16.1-2
- Initial package

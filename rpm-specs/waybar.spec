Name:           waybar
Version:        0.9.4
Release:        1%{?dist}
Summary:        Highly customizable Wayland bar for Sway and Wlroots based compositors
# MIT for main package, Boost for bundled clara.hpp
License:        MIT and Boost
URL:            https://github.com/Alexays/Waybar
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  meson >= 0.47.0
BuildRequires:  scdoc
#BuildRequires:  systemd-rpm-macros

BuildRequires:  pkgconfig(date)
BuildRequires:  pkgconfig(dbusmenu-gtk3-0.4)
BuildRequires:  pkgconfig(fmt) >= 5.3.0
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gtk-layer-shell-0)
BuildRequires:  pkgconfig(gtkmm-3.0)
BuildRequires:  pkgconfig(jsoncpp)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(libmpdclient)
BuildRequires:  pkgconfig(libnl-3.0)
BuildRequires:  pkgconfig(libnl-genl-3.0)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(sigc++-2.0)
BuildRequires:  pkgconfig(spdlog) >= 1.3.1
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-protocols)

Enhances:       sway
Recommends:     fontawesome-fonts

%description
%{summary}.

%prep
%autosetup -p1 -n Waybar-%{version}

%build
# FIXME: disable user service until a proper way to start it has been decided
# see rhbz#1798811 for more context
%meson \
    -Dsystemd=disabled
%meson_build

%install
%meson_install


%files
%license LICENSE
%doc README.md
%dir %{_sysconfdir}/xdg/%{name}
%config(noreplace) %{_sysconfdir}/xdg/%{name}/config
%config(noreplace) %{_sysconfdir}/xdg/%{name}/style.css
%{_bindir}/%{name}
%{_mandir}/man5/%{name}*

%changelog
* Mon Sep 21 2020 Aleksei Bavshin <alebastr89@gmail.com> - 0.9.4-1
- Update to 0.9.4

* Sun Sep 20 2020 Aleksei Bavshin <alebastr89@gmail.com> - 0.9.3-2
- Add patch for custom module signal handling regression
- Add patch for network module crash with fmt 7.0
- Add patch for broken updates in mpd and network modules

* Wed Aug 05 2020 Aleksei Bavshin <alebastr89@gmail.com> - 0.9.3-1
- Update to 0.9.3 (closes rhbz#1866571)
- Add patch for wlr/taskbar config strings

* Mon Aug 03 2020 Aleksei Bavshin <alebastr89@gmail.com> - 0.9.2-4
- Rebuild (date)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 30 2020 Björn Esser <besser82@fedoraproject.org> - 0.9.2-2
- Rebuild (jsoncpp)

* Sat Apr 11 2020 Aleksei Bavshin <alebastr89@gmail.com> - 0.9.2-1
- Update to 0.9.2

* Mon Feb 10 2020 Aleksei Bavshin <alebastr89@gmail.com> - 0.9.1-1
- Update to 0.9.1
- Remove upstreamed patch
- Add BuildRequires: pkgconfig(date)

* Sat Feb 08 2020 Aleksei Bavshin <alebastr89@gmail.com> - 0.9.0-1
- Initial import (#1798811)

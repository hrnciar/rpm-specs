# -*-Mode: rpm-spec -*-

Name:     wayvnc
Version:  0.1.2
Release:  3%{?dist}
Summary:  A VNC server for wlroots based Wayland compositors
License:  ISC
URL:      https://github.com/any1/wayvnc
Source:   %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: meson
BuildRequires: pkgconfig(egl)
BuildRequires: pkgconfig(glesv2)
BuildRequires: pkgconfig(gnutls)
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(libuv)
BuildRequires: pkgconfig(neatvnc)
BuildRequires: pkgconfig(pixman-1)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(xkbcommon)

Requires: (sway >= 1.4 if sway)

%description

This is a VNC server for wlroots based Wayland compositors. It
attaches to a running Wayland session, creates virtual input devices
and exposes a single display via the RFB protocol. The Wayland session
may be a headless one, so it is also possible to run wayvnc without a
physical display attached.

%prep
%setup -q

%build
%meson

%meson_build

%install
%meson_install

%files
%{_bindir}/%{name}
%{_datadir}/%{name}/

%doc README.md FAQ.md

%license COPYING

%changelog
* Wed Apr 15 2020 Robert Hepple - 0.1.2-3
- fixes per RHBZ#1823265

* Wed Apr 15 2020 Bob Hepple <bob.hepple@gmail.com> - 0.1.2-2
- fixes per RHBZ#1823265

* Sun Apr 12 2020 Bob Hepple <bob.hepple@gmail.com> - 0.1.2-1
- Initial version of the package

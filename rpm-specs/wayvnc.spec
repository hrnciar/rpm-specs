# -*-Mode: rpm-spec -*-

Name:     wayvnc
Version:  0.3.0
Release:  1%{?dist}
Summary:  A VNC server for wlroots based Wayland compositors
License:  ISC
URL:      https://github.com/any1/wayvnc
Source:   %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:   wayvnc-fix-man-dir.patch

BuildRequires: gcc
BuildRequires: meson
BuildRequires: pkgconfig(aml)
BuildRequires: pkgconfig(egl)
BuildRequires: pkgconfig(glesv2)
BuildRequires: pkgconfig(gnutls)
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(neatvnc) >= 0.3.0
BuildRequires: pkgconfig(pixman-1)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: scdoc

Requires: (sway >= 1.4 if sway)

%description

This is a VNC server for wlroots based Wayland compositors. It
attaches to a running Wayland session, creates virtual input devices
and exposes a single display via the RFB protocol. The Wayland session
may be a headless one, so it is also possible to run wayvnc without a
physical display attached.

%prep
%autosetup

%build
%meson

%meson_build

%install
%meson_install

%files
%{_bindir}/%{name}

%doc README.md FAQ.md
%{_mandir}/man1/%{name}.1.*

%license COPYING

%changelog
* Tue Sep 29 2020 Bob Hepple <bob.hepple@gmail.com> - 0.3.0-1
- new version

* Wed Aug 05 2020 Bob Hepple <bob.hepple@gmail.com> - 0.2.0-1
- new version

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Apr 15 2020 Robert Hepple - 0.1.2-3
- fixes per RHBZ#1823265

* Wed Apr 15 2020 Bob Hepple <bob.hepple@gmail.com> - 0.1.2-2
- fixes per RHBZ#1823265

* Sun Apr 12 2020 Bob Hepple <bob.hepple@gmail.com> - 0.1.2-1
- Initial version of the package

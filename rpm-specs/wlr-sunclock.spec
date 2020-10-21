# -*-Mode: rpm-spec -*-

Name:     wlr-sunclock
Version:  0.1.1
Release:  4%{?dist}
Summary:  Show the sun's shadows on earth

# src/astro.[ch] are by John Walker in 1988 and placed in the Public Domain.
# Otherwise it's LGPLv3.
License:  LGPLv3 and Public Domain

URL:      https://github.com/sentriz/wlr-sunclock
Source:   %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# build fails on aarch64 due to -X option; author suggests removing it:
# https://github.com/sentriz/wlr-sunclock/issues/6
Patch0:  wlr-sunclock-remove-X-linker-option.patch

BuildRequires: gcc
BuildRequires: meson
BuildRequires: wayland-devel
BuildRequires: wayland-protocols-devel
BuildRequires: pkgconfig(gtk+-wayland-3.0)
BuildRequires: pkgconfig(gtk-layer-shell-0)

%description

Wayland desktop widget to show the sun's shadows on earth. Uses
gtk-layer-shell and the layer shell protocol to render on your
desktop, behind your windows.

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install

%files
%{_bindir}/%{name}

%doc README.md

%license LICENCE

%changelog
* Fri Aug 28 2020 Bob Hepple <bob.hepple@gmail.com> - 0.1.1-4
- rebuilt

* Wed Aug 26 2020 Bob Hepple <bob.hepple@gmail.com> - 0.1.1-3
- rebuilt per RHBZ#1867267

* Tue Aug 18 2020 Bob Hepple <bob.hepple@gmail.com> - 0.1.1-2
- rebuilt per RHBZ#1867267


* Sat Aug 08 2020 Bob Hepple <bob.hepple@gmail.com> - 0.1.1-1
- Initial version of the package

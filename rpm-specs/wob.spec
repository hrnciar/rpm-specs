# -*-Mode: rpm-spec-mode; -*-

Name:     wob
Version:  0.8
Release:  4%{?dist}
Summary:  A lightweight overlay volume/backlight/progress/anything bar for Wayland
License:  ISC
URL:      https://github.com/francma/wob

Source0: %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: meson
BuildRequires: scdoc
BuildRequires: wayland-devel
BuildRequires: wayland-protocols-devel

%description
A lightweight overlay volume/backlight/progress/anything bar for
Wayland.

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
%{_mandir}/man1/%{name}.1.*

%license LICENSE

%changelog
* Mon Apr 06 2020 Bob Hepple <bob.hepple@gmail.com> - 0.8-4
- fix license field to ISC

* Mon Apr 06 2020 Bob Hepple <bob.hepple@gmail.com> - 0.8-3
- rebuilt per RHBZ#1819554

* Wed Apr  1 2020 Bob Hepple <bob.hepple@gmail.com> - 0.8-2
- prep for review request

* Mon Mar  2 2020 Bob Hepple <bob.hepple@gmail.com> - 0.8-1
- latest release

* Mon Feb 17 2020 Bob Hepple <bob.hepple@gmail.com> - 0.6-1
- Initial version of the package

Name:           squeekboard
Version:        1.9.2
Release:        1%{?dist}
Summary:        a Wayland virtual keyboard

License:        GPLv3+
URL:            https://source.puri.sm/Librem5/squeekboard
Source0:        https://source.puri.sm/Librem5/squeekboard/-/archive/v%{version}/squeekboard-v%{version}.tar.gz
Source1:        squeekboard.desktop

# temporary until upstreamed
Patch0:         0002-use-latest-compatible-crates.patch

ExclusiveArch:  %{rust_arches}

# Temporary. Breaks on ppc64le
ExcludeArch:    ppc64le

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  rust-packaging
BuildRequires:  pkgconfig(gio-2.0) >= 2.26
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gnome-desktop-3.0) >= 3.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.0
BuildRequires:  pkgconfig(wayland-client) >= 1.14
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.12
BuildRequires:  desktop-file-utils

%description
Squeekboard is a virtual keyboard supporting Wayland, built primarily 
for the Librem 5 phone. It squeaks because some Rust got inside.


%prep
%autosetup -p1 -n squeekboard-v%{version}
%cargo_prep


%generate_buildrequires
%cargo_generate_buildrequires -a


%build
%meson
%meson_build


%install
%meson_install
mkdir -p %{buildroot}/%{_sysconfdir}/xdg/autostart/
cp %{SOURCE1} %{buildroot}/%{_sysconfdir}/xdg/autostart/
chmod +x %{buildroot}/%{_bindir}/squeekboard-entry


%check
%meson_test
desktop-file-validate %{buildroot}/%{_datadir}/applications/sm.puri.Squeekboard.desktop


%files
%{_bindir}/squeekboard
%{_bindir}/squeekboard-entry
%{_bindir}/squeekboard-test-layout
%{_datadir}/applications/sm.puri.Squeekboard.desktop
%{_sysconfdir}/xdg/autostart/squeekboard.desktop
%doc README.md
%license COPYING


%changelog
* Fri Jun 19 2020 Torrey Sorensen <sorensentor@tuta.io> - 1.9.2-1
- Update to 1.9.2, including updated patch file.
- Remove unused libcroco
- Temporarily excluding ppc64le architecture 

* Tue Mar 24 2020 Nikhil Jha <hi@nikhiljha.com> - 1.9.1-1
- Update to 1.9.1

* Tue Mar 24 2020 Nikhil Jha <hi@nikhiljha.com> - 1.9.0-2
- Validate desktop file

* Thu Feb 27 2020 Nikhil Jha <hi@nikhiljha.com> - 1.9.0-1
- Initial packaging

Name:       swaybg
Version:    1.0
Release:    4%{?dist}
Summary:    Wallpaper tool for Wayland compositors

License:    MIT
URL:        https://github.com/swaywm/swaybg
Source0:    %{url}/archive/%{version}/%{name}-%{version}.tar.gz

# Swaybg was part of sway before sway 1.1
Conflicts:  sway < 1.1

BuildRequires:  gcc
BuildRequires:  meson >= 0.48.0
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.14
# Man page compilation
BuildRequires:  scdoc

%description
%{summary}.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%files
%doc README.md
%license LICENSE
%{_bindir}/swaybg
%{_mandir}/man1/swaybg.1*

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 10 2019 Jan StanÄ›k <jstanek@redhat.com> - 1.0-1
- Initial package

Name:           kanshi
Version:        1.1.0
Release:        1%{?dist}
Summary:        Dynamic display configuration for sway

License:        MIT
URL:            https://github.com/emersion/%{name}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  meson >= 0.47

BuildRequires:  pkgconfig(scdoc) >= 1.9.2
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-scanner)

Enhances:       sway
# require sway version with wlr-output-management support
Requires:       (sway >= 1.2 if sway)

%description
kanshi allows you to define output profiles that are automatically enabled
and disabled on hotplug. For instance, this can be used to turn a laptop's
internal screen off when docked.

This is a Wayland equivalent for tools like autorandr. kanshi can be used
on Wayland compositors supporting the wlr-output-management protocol.


%prep
%autosetup


%build
%meson
%meson_build


%install
%meson_install


%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.*
%{_mandir}/man5/%{name}.*


%changelog
* Mon Apr 20 2020 Aleksei Bavshin <alebastr89@gmail.com> - 1.1.0-1
- Initial import (#1825361)

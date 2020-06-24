# Minimal supported version of pipewire;
# 0.3.2 is sufficient for build, but only 0.3.4 has all required runtime fixes
%global pipewire_ver 0.3.4

Name:           xdg-desktop-portal-wlr
Version:        0.1.0
Release:        1%{?dist}
Summary:        xdg-desktop-portal backend for wlroots

License:        MIT
URL:            https://github.com/emersion/%{name}
Source0:        %{url}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{url}/releases/download/v%{version}/%{name}-%{version}.tar.gz.sig
Source2:        https://emersion.fr/.well-known/openpgpkey/hu/dj3498u4hyyarh35rkjfnghbjxug6b19#/gpgkey-0FDE7BE0E88F5E48.gpg

BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  meson
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(libpipewire-0.3) >= %{pipewire_ver}
BuildRequires:  pkgconfig(libspa-0.2)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-scanner)

Requires:       dbus
# required for Screenshot portal implementation
Requires:       grim
# BR does not translate to Requires; specify required version explicitly
Requires:       pipewire-libs%{?_isa} >= %{pipewire_ver}
Requires:       xdg-desktop-portal

Enhances:       sway
Supplements:    (sway and (flatpak or snapd))

%description
%{summary}.
This project seeks to add support for the screenshot, screencast, and possibly
remote-desktop xdg-desktop-portal interfaces for wlroots based compositors.


%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1


%build
%meson
%meson_build


%install
%meson_install


%post
%systemd_user_post %{name}.service

%preun
%systemd_user_preun %{name}.service


%files
%license LICENSE
%doc README.md
%{_libexecdir}/%{name}
%{_datadir}/xdg-desktop-portal/portals/wlr.portal
%{_datadir}/dbus-1/services/*.service
%{_userunitdir}/%{name}.service


%changelog
* Wed May 06 2020 Aleksei Bavshin <alebastr89@gmail.com> - 0.1.0-1
- Initial import (#1831981)

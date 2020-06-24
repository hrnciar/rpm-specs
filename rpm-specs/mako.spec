Name:       mako
Version:    1.4.1
Release:    1%{?dist}
Summary:    Lightweight Wayland notification daemon
Provides:   desktop-notification-daemon

License:    MIT
URL:        https://github.com/emersion/%{name}
Source0:    %{url}/archive/v%{version}.tar.gz
# Add dbus-activated systemd unit as required by the packaging guidelines. To
# be upstreamed as discussed in RHBZ#1689634.
Source1:    %{name}.service

Patch0: add-systemd-service-dbus.patch
Patch1: meson-disable-werror.patch

BuildRequires:  cmake
BuildRequires:  systemd-rpm-macros
BuildRequires:  gcc
BuildRequires:  meson >= 0.43.0
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.14
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  systemd-devel
BuildRequires:  scdoc
Requires:       dbus
Recommends:     jq
%{?systemd_requires}

%description
mako is a lightweight notification daemon for Wayland compositors that support
the layer-shell protocol.

%prep
%autosetup

%build
%meson -Dzsh-completions=true
%meson_build

%install
%meson_install

# Install dbus-activated systemd unit
install -m0644 -Dt %{buildroot}%{_userunitdir}/ %{SOURCE1}

%post
%systemd_user_post %{name}.service

%preun
%systemd_user_preun %{name}.service

%files
%license LICENSE
%doc README.md
%{_bindir}/mako
%{_bindir}/makoctl
%{_mandir}/man1/mako.1*
%{_mandir}/man5/mako.5*
%{_mandir}/man1/makoctl.1*
%{_userunitdir}/%{name}.service
%{_datadir}/dbus-1/services/fr.emersion.mako.service
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_mako*

%changelog
* Tue May 19 2020 Stefano Figura <stefano@figura.im> - 1.4.1-1
- Upstream 1.4.1 release

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 16 2019 Jeff Peeler <jpeeler@redhat.com> - 1.4-1
- Upstream 1.4 release
- Removed D-Bus service file as it is upstream now

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jul 14 2019 Jeff Peeler <jpeeler@redhat.com> - 1.3-1
- Upstream 1.3 release

* Thu Apr 04 2019 Timothée Floure <fnux@fedoraproject.org> - 1.2-2
- Fix location of systemd service file

* Sun Mar 17 2019 Timothée Floure <fnux@fedoraproject.org> - 1.2-1
- Let there be package

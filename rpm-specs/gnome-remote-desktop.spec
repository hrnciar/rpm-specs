%global systemd_unit gnome-remote-desktop.service

Name:           gnome-remote-desktop
Version:        0.1.9
Release:        2%{?dist}
Summary:        GNOME Remote Desktop screen share service

License:        GPLv2+
URL:            https://gitlab.gnome.org/jadahl/gnome-remote-desktop
Source0:        https://download.gnome.org/sources/gnome-remote-desktop/0.1/gnome-remote-desktop-0.1.9.tar.xz

# Avoid race condition on disconnect
Patch0:         0001-vnc-Drop-frames-if-client-is-gone.patch

# Adds encryption support (requires patched LibVNCServer)
Patch1:         gnutls-anontls.patch

# Copy using the right destination stride
Patch2:         0001-vnc-Copy-pixels-using-the-right-destination-stride.patch

BuildRequires:  git
BuildRequires:  gcc
BuildRequires:  meson >= 0.36.0
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.32
BuildRequires:  pkgconfig(libpipewire-0.3) >= 0.3.0
BuildRequires:  pkgconfig(libvncserver) >= 0.9.11-7
BuildRequires:  pkgconfig(freerdp2)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(gnutls)

%{?systemd_requires}
BuildRequires:  systemd

Requires:       pipewire >= 0.3.0

%description
GNOME Remote Desktop is a remote desktop and screen sharing service for the
GNOME desktop environment.


%prep
%autosetup -S git


%build
%meson
%meson_build


%install
%meson_install


%post
%systemd_user_post %{systemd_unit}


%preun
%systemd_user_preun %{systemd_unit}


%postun
%systemd_user_postun_with_restart %{systemd_unit}


%files
%license COPYING
%doc README
%{_libexecdir}/gnome-remote-desktop-daemon
%{_userunitdir}/gnome-remote-desktop.service
%{_datadir}/glib-2.0/schemas/org.gnome.desktop.remote-desktop.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.desktop.remote-desktop.enums.xml


%changelog
* Mon Sep 14 2020 Jonas Ådahl <jadahl@redhat.com> - 0.1.9-2
- Copy using the right destination stride

* Mon Sep 14 2020 Jonas Ådahl <jadahl@redhat.com> - 0.1.9-1
- Update to 0.1.9
- Backport race condition crash fix
- Rebase anon-tls patches

* Thu Aug 27 2020 Ray Strode <rstrode@redhat.com> - 0.1.8-3
- Fix crash
  Related: #1844993

* Mon Jun 1 2020 Felipe Borges <feborges@redhat.com> - 0.1.8-2
- Fix black screen issue in remote connections on Wayland

* Wed Mar 11 2020 Jonas Ådahl <jadahl@redhat.com> - 0.1.8-1
- Update to 0.1.8

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 4 2019 Jonas Ådahl <jadahl@redhat.com> - 0.1.7-1
- Update to 0.1.7

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 2 2018 Jonas Ådahl <jadahl@redhat.com> - 0.1.6-2
- Don't crash when PipeWire disconnects (rhbz#1632781)

* Tue Aug 7 2018 Jonas Ådahl <jadahl@redhat.com> - 0.1.6
- Update to 0.1.6
- Apply ANON-TLS patch
- Depend on pipewire 0.2.2

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 30 2018 Jonas Ådahl <jadahl@redhat.com> - 0.1.4-1
- Update to new version

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.2-5
- Escape macros in %%changelog

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Aug 29 2017 Jonas Ådahl <jadahl@redhat.com> - 0.1.2-3
- Use %%autosetup
- Install licence file

* Tue Aug 22 2017 Jonas Ådahl <jadahl@redhat.com> - 0.1.2-2
- Remove gschema compilation step as that had been deprecated

* Mon Aug 21 2017 Jonas Ådahl <jadahl@redhat.com> - 0.1.2-1
- Update to 0.1.2
- Changed tabs to spaces
- Added systemd user macros
- Install to correct systemd user unit directory
- Compile gsettings schemas after install and uninstall

* Mon Aug 21 2017 Jonas Ådahl <jadahl@redhat.com> - 0.1.1-1
- First packaged version

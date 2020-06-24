%define gnome_online_accounts_version 3.25.3
%define glib2_version 2.56.0
%define gnome_desktop_version 3.35.4
%define gsd_version 3.35.0
%define gsettings_desktop_schemas_version 3.31.0
%define upower_version 0.99.8
%define gtk3_version 3.22.20
%define cheese_version 3.28.0
%define gnome_bluetooth_version 3.18.2

Name:           gnome-control-center
Version:        3.36.3
Release:        1%{?dist}
Summary:        Utilities to configure the GNOME desktop

License:        GPLv2+ and CC-BY-SA
URL:            http://www.gnome.org
Source0:        https://download.gnome.org/sources/gnome-control-center/3.36/gnome-control-center-%{version}.tar.xz

# https://bugzilla.gnome.org/show_bug.cgi?id=695691
Patch0:         distro-logo.patch

# https://teams.fedoraproject.org/project/silverblue/us/127
Patch1:         info-model-for-lenovo.patch

BuildRequires:  chrpath
BuildRequires:  cups-devel
BuildRequires:  desktop-file-utils
BuildRequires:  docbook-style-xsl libxslt
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  git
BuildRequires:  pkgconfig(accountsservice)
BuildRequires:  pkgconfig(cheese) >= %{cheese_version}
BuildRequires:  pkgconfig(cheese-gtk)
BuildRequires:  pkgconfig(clutter-gtk-1.0)
BuildRequires:  pkgconfig(colord)
BuildRequires:  pkgconfig(colord-gtk)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gdk-wayland-3.0)
BuildRequires:  pkgconfig(gio-2.0) >= %{glib2_version}
BuildRequires:  pkgconfig(gnome-desktop-3.0) >= %{gnome_desktop_version}
BuildRequires:  pkgconfig(gnome-settings-daemon) >= %{gsd_version}
BuildRequires:  pkgconfig(goa-1.0) >= %{gnome_online_accounts_version}
BuildRequires:  pkgconfig(goa-backend-1.0)
BuildRequires:  pkgconfig(grilo-0.3)
BuildRequires:  pkgconfig(gsettings-desktop-schemas) >= %{gsettings_desktop_schemas_version}
BuildRequires:  pkgconfig(gsound)
BuildRequires:  pkgconfig(gtk+-3.0) >= %{gtk3_version}
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(ibus-1.0)
BuildRequires:  pkgconfig(libcanberra-gtk3)
BuildRequires:  pkgconfig(libgtop-2.0)
BuildRequires:  pkgconfig(libhandy-0.0)
BuildRequires:  pkgconfig(libnm)
BuildRequires:  pkgconfig(libnma)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libpulse-mainloop-glib)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(mm-glib)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(pwquality)
BuildRequires:  pkgconfig(smbclient)
BuildRequires:  pkgconfig(upower-glib) >= %{upower_version}
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(udisks2)
%ifnarch s390 s390x
BuildRequires:  pkgconfig(gnome-bluetooth-1.0) >= %{gnome_bluetooth_version}
BuildRequires:  pkgconfig(libwacom)
%endif

# Versioned library deps
Requires: cheese-libs%{?_isa} >= %{cheese_version}
Requires: glib2%{?_isa} >= %{glib2_version}
Requires: gnome-desktop3%{?_isa} >= %{gnome_desktop_version}
Requires: gnome-online-accounts%{?_isa} >= %{gnome_online_accounts_version}
Requires: gnome-settings-daemon%{?_isa} >= %{gsd_version}
Requires: gsettings-desktop-schemas%{?_isa} >= %{gsettings_desktop_schemas_version}
Requires: gtk3%{?_isa} >= %{gtk3_version}
Requires: upower%{?_isa} >= %{upower_version}
%ifnarch s390 s390x
Requires: gnome-bluetooth%{?_isa} >= 1:%{gnome_bluetooth_version}
%endif

Requires: %{name}-filesystem = %{version}-%{release}
# For user accounts
Requires: accountsservice
Requires: alsa-lib
# For the thunderbolt panel
Recommends: bolt
# For the color panel
Requires: colord
# For the printers panel
Requires: cups-pk-helper
Requires: dbus
# For the info/details panel
Requires: glx-utils
# For the user languages
Requires: iso-codes
Recommends: NetworkManager-wifi
# For the sharing panel
Recommends: gnome-remote-desktop
%if 0%{?fedora}
Recommends: rygel
%endif
Recommends: vino
# For the info/details panel
Requires: switcheroo-control
# For the keyboard panel
Requires: /usr/bin/gkbd-keyboard-display

# Renamed in F28
Provides: control-center = 1:%{version}-%{release}
Provides: control-center%{?_isa} = 1:%{version}-%{release}
Obsoletes: control-center < 1:%{version}-%{release}

%description
This package contains configuration utilities for the GNOME desktop, which
allow to configure accessibility options, desktop fonts, keyboard and mouse
properties, sound setup, desktop theme and background, user interface
properties, screen resolution, and other settings.

%package filesystem
Summary: GNOME Control Center directories
# NOTE: this is an "inverse dep" subpackage. It gets pulled in
# NOTE: by the main package and MUST not depend on the main package
BuildArch: noarch
# Renamed in F28
Provides: control-center-filesystem = 1:%{version}-%{release}
Obsoletes: control-center-filesystem < 1:%{version}-%{release}

%description filesystem
The GNOME control-center provides a number of extension points
for applications. This package contains directories where applications
can install configuration files that are picked up by the control-center
utilities.

%prep
%autosetup -p1 -S git

%build
%meson -Ddocumentation=true
%meson_build

%install
%meson_install

# We do want this
mkdir -p $RPM_BUILD_ROOT%{_datadir}/gnome/wm-properties

# We don't want these
rm -rf $RPM_BUILD_ROOT%{_datadir}/gnome/autostart
rm -rf $RPM_BUILD_ROOT%{_datadir}/gnome/cursor-fonts

# Remove rpath
chrpath --delete $RPM_BUILD_ROOT%{_bindir}/gnome-control-center

%find_lang %{name} --all-name --with-gnome

%files -f %{name}.lang
%license COPYING
%doc NEWS README.md
%{_bindir}/gnome-control-center
%{_datadir}/applications/*.desktop
%{_datadir}/bash-completion/completions/gnome-control-center
%{_datadir}/dbus-1/services/org.gnome.ControlCenter.SearchProvider.service
%{_datadir}/dbus-1/services/org.gnome.ControlCenter.service
%{_datadir}/gettext/
%{_datadir}/glib-2.0/schemas/org.gnome.ControlCenter.gschema.xml
%{_datadir}/gnome-control-center/keybindings/*.xml
%{_datadir}/gnome-control-center/pixmaps
%{_datadir}/gnome-shell/search-providers/gnome-control-center-search-provider.ini
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/man/man1/gnome-control-center.1*
%{_datadir}/metainfo/gnome-control-center.appdata.xml
%{_datadir}/pixmaps/faces
%{_datadir}/pkgconfig/gnome-keybindings.pc
%{_datadir}/polkit-1/actions/org.gnome.controlcenter.*.policy
%{_datadir}/polkit-1/rules.d/gnome-control-center.rules
%{_datadir}/sounds/gnome/default/*/*.ogg
%{_libexecdir}/cc-remote-login-helper
%{_libexecdir}/gnome-control-center-search-provider
%{_libexecdir}/gnome-control-center-print-renderer

%files filesystem
%dir %{_datadir}/gnome-control-center
%dir %{_datadir}/gnome-control-center/keybindings
%dir %{_datadir}/gnome/wm-properties

%changelog
* Wed Jun 03 2020 Kalev Lember <klember@redhat.com> - 3.36.3-1
- Update to 3.36.3

* Fri May 01 2020 Kalev Lember <klember@redhat.com> - 3.36.2-1
- Update to 3.36.2

* Tue Apr 28 2020 Felipe Borges <feborges@redhat.com> - 3.36.1-2
- Add "Model" row info for Lenovo devices

* Fri Mar 27 2020 Kalev Lember <klember@redhat.com> - 3.36.1-1
- Update to 3.36.1

* Thu Mar 19 2020 Michael Catanzaro <mcatanzaro@redhat.com> - 3.36.0-3
- No changes, bump revision to maintain upgrade path from F32

* Mon Mar 16 2020 Michael Catanzaro <mcatanzaro@redhat.com> - 3.36.0-2
- Update distro-logo.patch to use fedora_vertical version of logo.

* Sat Mar 07 2020 Kalev Lember <klember@redhat.com> - 3.36.0-1
- Update to 3.36.0

* Mon Mar 02 2020 Kalev Lember <klember@redhat.com> - 3.35.92-1
- Update to 3.35.92

* Mon Feb 17 2020 Kalev Lember <klember@redhat.com> - 3.35.91-1
- Update to 3.35.91

* Mon Feb 03 2020 Bastien Nocera <bnocera@redhat.com> - 3.35.90-1
+ gnome-control-center-3.35.90-1
- Update to 3.35.90

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.34.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 16 2020 Kalev Lember <klember@redhat.com> - 3.34.2-3
- Backport a patch to fix the build with latest libgnome-desktop

* Mon Dec 09 2019 Michael Catanzaro <mcatanzaro@gnome.org> - 3.34.2-2
- Drop nm-connection-editor requires, per gnome-control-center#512
- To edit mobile broadband connections, install nm-connection-editor

* Wed Nov 27 2019 Kalev Lember <klember@redhat.com> - 3.34.2-1
- Update to 3.34.2

* Thu Oct 10 2019 Adam Williamson <awilliam@redhat.com> - 3.34.1-4
- Add patch to fix crash when selecting display with no modes (rhbz#1756553)

* Wed Oct 09 2019 Felipe Borges <feborges@redhat.com> - 3.34.1-3
- Add patch to fix parsing of addresses while adding printers (rhbz#1750394)

* Mon Oct 07 2019 Benjamin Berg <bberg@redhat.com> - 3.34.1-2
- Add patch to fix resetting of system wide format locale (rhbz#1759221)

* Mon Oct 07 2019 Kalev Lember <klember@redhat.com> - 3.34.1-1
- Update to 3.34.1

* Sat Oct 05 2019 Michael Catanzaro <mcatanzaro@gnome.org> - 3.34.0.1-3
- Add patch to fix editing wired connection settings (rhbz#1750805)
- Remove broken remote printers patch

* Wed Oct 02 2019 Michael Catanzaro <mcatanzaro@gnome.org> - 3.34.0.1-2
- Add patch to fix crash when configuring remote printers

* Mon Sep 09 2019 Kalev Lember <klember@redhat.com> - 3.34.0.1-1
- Update to 3.34.0.1

* Mon Sep 09 2019 Kalev Lember <klember@redhat.com> - 3.34.0-1
- Update to 3.34.0

* Mon Aug 12 2019 Kalev Lember <klember@redhat.com> - 3.33.90-1
- Update to 3.33.90

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.33.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jul 21 2019 Kalev Lember <klember@redhat.com> - 3.33.3-2
- Remove libXxf86misc-devel BuildRequires as the package no longer exists

* Wed Jun 19 2019 Kalev Lember <klember@redhat.com> - 3.33.3-1
- Update to 3.33.3

* Fri May 24 2019 Kalev Lember <klember@redhat.com> - 3.32.2-1
- Update to 3.32.2

* Tue Apr 16 2019 Adam Williamson <awilliam@redhat.com> - 3.32.1-2
- Rebuild with Meson fix for #1699099

* Fri Mar 29 2019 Kalev Lember <klember@redhat.com> - 3.32.1-1
- Update to 3.32.1

* Mon Mar 11 2019 Kalev Lember <klember@redhat.com> - 3.32.0.1-1
- Update to 3.32.0.1

* Mon Mar 11 2019 Kalev Lember <klember@redhat.com> - 3.32.0-1
- Update to 3.32.0

* Mon Mar 04 2019 Kalev Lember <klember@redhat.com> - 3.31.92-1
- Update to 3.31.92

* Sat Feb 23 2019 Kevin Fenzi <kevin@scrye.com> - 3.31.90-2
- Add https://gitlab.gnome.org/GNOME/gnome-control-center/merge_requests/387.patch 
  to fix udisks crash

* Thu Feb 07 2019 Kalev Lember <klember@redhat.com> - 3.31.90-1
- Update to 3.31.90

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.31.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 09 2019 Kalev Lember <klember@redhat.com> - 3.31.4-1
- Update to 3.31.4

* Tue Nov 20 2018 Pete Walter <pwalter@fedoraproject.org> - 3.30.2-3
- Recommend gnome-remote-desktop for the sharing panel

* Sat Nov 17 2018 Pete Walter <pwalter@fedoraproject.org> - 3.30.2-2
- Change bolt requires to recommends (#1643709)
- Change rygel requires to recommends

* Thu Nov 01 2018 Kalev Lember <klember@redhat.com> - 3.30.2-1
- Update to 3.30.2

* Thu Oct 11 2018 David Herrmann <dh.herrmann@gmail.com> - 3.30.1-4
- Reduce 'dbus-x11' dependency to 'dbus'. The xinit scripts are no longer the
  canonical way to start dbus, but the 'dbus' package is nowadays required to
  provide a user and system bus to its dependents.

* Wed Oct 10 2018 Benjamin Berg <bberg@redhat.com> - 3.30.1-3
- Add patch to improve background loading. The patch is not acceptable
  upstream as is, but is also a good improvement on the current situation
  (#1631002)

* Sun Oct 07 2018 Kalev Lember <klember@redhat.com> - 3.30.1-2
- Backport an upstream fix for a crash in the online accounts panel

* Wed Sep 26 2018 Kalev Lember <klember@redhat.com> - 3.30.1-1
- Update to 3.30.1

* Thu Sep 06 2018 Kalev Lember <klember@redhat.com> - 3.30.0-1
- Update to 3.30.0

* Sun Aug 12 2018 Kalev Lember <klember@redhat.com> - 3.29.90-1
- Update to 3.29.90

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.28.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue May 29 2018 Kalev Lember <klember@redhat.com> - 3.28.2-1
- Update to 3.28.2

* Wed May 23 2018 Pete Walter <pwalter@fedoraproject.org> - 3.28.1-4
- Change NetworkManager-wifi requires to recommends (#1478661)

* Tue May 22 2018 Ray Strode <rstrode@redhat.com> - 3.28.1-3
- Change vino requires to a vino recommends

* Fri Apr 13 2018 Kalev Lember <klember@redhat.com> - 3.28.1-2
- Backport new thunderbolt panel

* Tue Apr 10 2018 Pete Walter <pwalter@fedoraproject.org> - 3.28.1-1
- Rename control-center to gnome-control-center

%global url_ver %%(echo %{version}|cut -d. -f1,2)

Name:       connections
Version:    3.38.1
Release:    1%{?dist}
Summary:    A remote desktop client for the GNOME desktop environment

License:    GPLv3+
URL:        https://gitlab.gnome.org/gnome/connections/-/wikis/home
Source0:    http://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  gcc
BuildRequires:  pkgconfig(freerdp2)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtk-vnc-2.0)

Requires:  adwaita-icon-theme

%description
Connections is a remote desktop client for the GNOME desktop environment

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name} --with-gnome

# Remove unneeded development files
rm -rf %{buildroot}%{_includedir}/connections/

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.Connections.desktop

%files -f %{name}.lang
%license COPYING
%doc README.md NEWS
%{_bindir}/%{name}
%{_libdir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/org.gnome.Connections.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.Connections.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Connections.svg
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Connections.Devel.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.Connections-symbolic.svg
%{_datadir}/appdata/org.gnome.Connections.appdata.xml
%{_datadir}/dbus-1/services/org.gnome.Connections.service
%{_datadir}/mime/packages/org.gnome.Connections.xml

%changelog
* Tue Oct 20 2020 Kalev Lember <klember@redhat.com> - 3.38.1-1
- Update to 3.38.1

* Mon Sep 14 2020 Kalev Lember <klember@redhat.com> - 3.38.0-1
- Update to 3.38.0

* Thu Sep 10 2020 Felipe Borges <feborges@redhat.com> - 3.37.91-1
- Update to 3.37.91

* Mon Aug 10 2020 Felipe Borges <feborges@redhat.com> - 3.37.90-1
- Initial import

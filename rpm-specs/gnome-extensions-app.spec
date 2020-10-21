%global _vpath_srcdir subprojects/extensions-app
%global source_name gnome-shell

Name:          gnome-extensions-app
Version:       3.38.0
Release:       1%{?dist}
Summary:       Manage GNOME Shell extensions

License:       GPLv2+
URL:           https://gitlab.gnome.org/GNOME/%{source_name}
Source0:       https://download.gnome.org/sources/%{source_name}/3.38/%{source_name}-%{version}.tar.xz

Patch0:        0001-extensions-app-Add-compatibility-with-GNOME-3.34.patch

BuildRequires: gcc
BuildRequires: gettext
BuildRequires: meson
BuildRequires: git

BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: gjs
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

Requires:      gjs%{_isa}

%define exec_name gnome-extensions-app
%define bus_name org.gnome.Extensions

%description
GNOME Extensions is an application for configuring and removing
GNOME Shell extensions.


%prep
%setup -q -n %{source_name}-%{version}

%if 0%{?flatpak}
%patch0 -p1
%endif

%{_vpath_srcdir}/generate-translations.sh


%build
%meson
%meson_build

%check
%meson_test
desktop-file-validate %{buildroot}%{_datadir}/applications/%{bus_name}.desktop


%install
%meson_install

%find_lang %{name}

rm -rf %{buildroot}/%{_datadir}/%{name}/gir-1.0

%files -f %{name}.lang
%license COPYING
%{_bindir}/%{exec_name}
%{_datadir}/applications/%{bus_name}.desktop
%{_datadir}/dbus-1/services/%{bus_name}.service
%if 0%{?flatpak}
%{_datadir}/glib-2.0/schemas/%{bus_name}.gschema.xml
%endif
%{_datadir}/metainfo/%{bus_name}.metainfo.xml
%{_datadir}/icons/hicolor/scalable/apps/%{bus_name}.svg
%{_datadir}/icons/hicolor/scalable/apps/%{bus_name}.Devel.svg
%{_datadir}/icons/hicolor/symbolic/apps/%{bus_name}-symbolic.svg
%{_datadir}/%{name}/
%{_libdir}/%{name}/


%changelog
* Tue Sep 15 2020 Florian Müllner <fmuellner@redhat.com> - 3.38.0-1
- Update to 3.38.0

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.37.3-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.37.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 07 2020 Florian Müllner <fmuellner@gnome.org> - 3.37.2-1
- Update to 3.37.3

* Wed Jun 03 2020 Florian Müllner <fmuellner@gnome.org> - 3.37.2-1
- Update to 3.37.2

* Thu Apr 30 2020 Florian Müllner <fmuellner@gnome.org> - 3.37.1-1
- Update to 3.37.1

* Wed Apr 01 2020 Florian Müllner <fmuellner@gnome.org> - 3.36.1-1
- Make flatpak build compatible with F31

* Tue Mar 31 2020 Florian Müllner <fmuellner@gnome.org> - 3.36.1-1
- Build initial version

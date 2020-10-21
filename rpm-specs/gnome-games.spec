%global uuid org.gnome.Games

Name:       gnome-games
Version:    3.38.0
Release:    1%{?dist}
Summary:    Simple game launcher for GNOME

License:    GPLv3+
URL:        https://wiki.gnome.org/Apps/Games
Source0:    https://gitlab.gnome.org/GNOME/gnome-games/-/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: desktop-file-utils
BuildRequires: intltool
BuildRequires: libappstream-glib
BuildRequires: meson >= 0.46.1
BuildRequires: vala
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(glib-2.0) >= 2.38.0
BuildRequires: pkgconfig(grilo-0.3)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(libarchive)
BuildRequires: pkgconfig(libhandy-1) >= 0.90.0
BuildRequires: pkgconfig(librsvg-2.0)
BuildRequires: pkgconfig(libsoup-2.4)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(retro-gtk-1)
BuildRequires: pkgconfig(sqlite3)
BuildRequires: pkgconfig(tracker-sparql-2.0)
%if 0%{?fedora} >= 30
BuildRequires: pkgconfig(manette-0.2) >= 0.2.0
%endif

Requires:   hicolor-icon-theme

Recommends: libretro-beetle-ngp%{?_isa}
Recommends: libretro-beetle-pce-fast%{?_isa}
Recommends: libretro-beetle-vb%{?_isa}
Recommends: libretro-beetle-wswan%{?_isa}
Recommends: libretro-bsnes-mercury%{?_isa}
Recommends: libretro-desmume2015%{?_isa}
Recommends: libretro-gambatte%{?_isa}
Recommends: libretro-handy%{?_isa}
Recommends: libretro-mgba%{?_isa}
Recommends: libretro-nestopia%{?_isa}
Recommends: libretro-pcsx-rearmed%{?_isa}
Recommends: libretro-prosystem%{?_isa}
Recommends: libretro-stella2014%{?_isa}

%description
Games is a GNOME 3 application to browse your video games library and to
easily pick and play a game from it. It aims to do for games what Music
already does for your music library.

You want to install Games if you just want a very simple and comfortable way
to play your games and you don’t need advanced features such as speedrunning
tools or video game development tools.


%prep
%autosetup


%build
%meson
%meson_build


%install
%meson_install
%find_lang %{name}

# Remove executable bit from AUTHORS and COPYING files
find %{buildroot}%{_datadir} -executable -type f -exec chmod -x {} +


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files -f %{name}.lang
%license COPYING
%doc README.md AUTHORS HACKING.md
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/*.desktop
%{_datadir}/dbus-1/services/*.service
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/gnome-shell/search-providers/%{uuid}.SearchProvider.ini
%{_datadir}/icons/hicolor/*/*/*.svg
%{_libdir}/%{name}/
%{_libexecdir}/%{name}-search-provider
%{_metainfodir}/*.xml


%changelog
* Sat Sep 12 17:08:14 EEST 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 3.38.0-1
- Update to 3.38.0

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.36.1-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.36.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Mar 31 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 3.36.1-1
- Update to 3.36.1

* Fri Mar 06 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 3.36.0-1
- Update to 3.36.0

* Fri Feb 28 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 3.35.92-1
- Update to 3.35.92

* Wed Feb 12 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 3.35.90-1
- Update to 3.35.90

* Wed Feb 12 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 3.34.2-1
- Update to 3.34.2

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.34.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Oct 06 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 3.34.1-1
- Update to 3.34.1

* Sat Sep 14 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 3.34.0-1
- Update to 3.34.0

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.32.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 15 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 3.32.1-2
- Initial package

%global srcname music
%global appname io.elementary.music

%global __provides_exclude_from ^%{_libdir}/%{appname}/.*\\.so$

%global common_description %{expand:
Music is a fast and beautiful GTK3 audio player with a focus on music
and libraries. It handles external devices, CDs, and album art. Music
utilizes Granite for a consistent and slick UI.}

Name:           elementary-music
Summary:        Music player and library from elementary
Version:        5.0.5
Release:        2%{?dist}
License:        LGPLv2+

URL:            https://github.com/elementary/%{srcname}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  libappstream-glib
BuildRequires:  vala >= 0.26

BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.40
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(granite) >= 5.2.0
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:  pkgconfig(gstreamer-tag-1.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22
BuildRequires:  pkgconfig(libgda-5.0)
BuildRequires:  pkgconfig(libpeas-1.0)
BuildRequires:  pkgconfig(libpeas-gtk-1.0)
BuildRequires:  pkgconfig(taglib_c)
BuildRequires:  pkgconfig(zeitgeist-2.0)

# dependencies for iPod plugin
BuildRequires:  pkgconfig(libgpod-1.0)

# dependencies for Last.FM plugin
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libaccounts-glib)
BuildRequires:  pkgconfig(libsignon-glib)
BuildRequires:  pkgconfig(libsoup-2.4)

Requires:       hicolor-icon-theme

# elementary-music explicitly requires the sqlite libgda database provider
Requires:       libgda-sqlite%{?_isa}


Provides:       noise = %{version}-%{release}
Obsoletes:      noise < 0.4.2-9.20180822.git67265b0


%description %{common_description}


%package        plugin-ipod
Summary:        The official elementary music player (iPod plugin)
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    plugin-ipod %{common_description}

This package contains the iPod plugin.


%package        plugin-lastfm
Summary:        The official elementary music player (Last.FM plugin)
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    plugin-lastfm %{common_description}

This package contains the Last.FM plugin.


%package        devel
Summary:        The official elementary music player (development headers)
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel %{common_description}

This package contains files needed for developing with Music.


%prep
%autosetup -n %{srcname}-%{version} -p1


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{appname}


%check
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{appname}.desktop

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml


%files -f %{appname}.lang
%doc README.md
%license COPYING

%{_bindir}/%{appname}

%{_libdir}/lib%{appname}-core.so.0
%{_libdir}/lib%{appname}-core.so.0.1

%dir %{_libdir}/%{appname}
%dir %{_libdir}/%{appname}/plugins

%{_libdir}/%{appname}/plugins/cdrom-device.plugin
%{_libdir}/%{appname}/plugins/libcdrom-device.so
%{_libdir}/%{appname}/plugins/audioplayer-device.plugin
%{_libdir}/%{appname}/plugins/libaudioplayer-device.so

%{_datadir}/applications/%{appname}.desktop
%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/multimedia-audio-player.svg
%{_datadir}/metainfo/%{appname}.appdata.xml


%files plugin-ipod
%{_libdir}/%{appname}/plugins/ipod-device.plugin
%{_libdir}/%{appname}/plugins/libipod-device.so


%files plugin-lastfm
%{_libdir}/%{appname}/plugins/lastfm.plugin
%{_libdir}/%{appname}/plugins/liblastfm.so
%{_datadir}/accounts/applications/noise-lastfm.application


%files devel
%{_libdir}/lib%%{appname}-core.so
%{_libdir}/pkgconfig/%{appname}-core.pc

%{_includedir}/%{appname}-core.h

%{_datadir}/vala/vapi/%{appname}-core.deps
%{_datadir}/vala/vapi/%{appname}-core.vapi


%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Mar 06 2020 Fabio Valentini <decathorpe@gmail.com> - 5.0.5-1
- Update to version 5.0.5.

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Apr 18 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.4-1
- Update to version 5.0.4.

* Tue Apr 16 2019 Adam Williamson <awilliam@redhat.com> - 5.0.3-3
- Rebuild with Meson fix for #1699099

* Sat Mar 16 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.3-2
- Enable Last.FM plugin.
- Split off plugins with extra dependencies into optional sub-packages.

* Thu Feb 28 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.3-1
- Update to version 5.0.3.

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 25 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.2-3
- Include upstream patch to fix issue spotted by vala 0.43.4+.

* Fri Jan 25 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.2-2
- Include upstream patch to fix valac target GLib check.

* Tue Dec 18 2018 Fabio Valentini <decathorpe@gmail.com> - 5.0.2-1
- Update to version 5.0.2.

* Sun Dec 16 2018 Fabio Valentini <decathorpe@gmail.com> - 5.0.1-1
- Update to version 5.0.1.

* Thu Oct 18 2018 Fabio Valentini <decathorpe@gmail.com> - 5.0-1
- Update to version 5.0.
- Disable LastFM plugin.

* Tue Aug 28 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2-9.20180822.git67265b0
- Initial package renamed from noise.


%global srcname photos
%global appname io.elementary.%{srcname}

%global __provides_exclude_from ^%{_libdir}/%{appname}/.*\\.so$

Name:           elementary-photos
Summary:        Photo manager and viewer from elementary
Version:        2.7.0
Release:        3%{?dist}
License:        LGPLv2+

URL:            https://github.com/elementary/%{srcname}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson >= 0.46.0
BuildRequires:  vala

BuildRequires:  pkgconfig(gee-0.8) >= 0.8.5
BuildRequires:  pkgconfig(geocode-glib-1.0)
BuildRequires:  pkgconfig(gexiv2) >= 0.4.90
BuildRequires:  pkgconfig(gio-2.0) >= 2.20
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.20
BuildRequires:  pkgconfig(glib-2.0) >= 2.30.0
BuildRequires:  pkgconfig(gmodule-2.0) >= 2.24.0
BuildRequires:  pkgconfig(granite) >= 5.2.0
BuildRequires:  pkgconfig(gstreamer-1.0) >= 1.0.0
BuildRequires:  pkgconfig(gstreamer-base-1.0) >= 1.0.0
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0) >= 1.0.0
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0) >= 1.0.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.6.0
BuildRequires:  pkgconfig(gudev-1.0) >= 145
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libexif) >= 0.6.16
BuildRequires:  pkgconfig(libgphoto2) >= 2.4.2
BuildRequires:  pkgconfig(libraw) >= 0.13.2
BuildRequires:  pkgconfig(libsoup-2.4) >= 2.26.0
BuildRequires:  pkgconfig(libwebp) >= 0.4.4
BuildRequires:  pkgconfig(libxml-2.0) >= 2.6.32
BuildRequires:  pkgconfig(rest-0.7) >= 0.7
BuildRequires:  pkgconfig(sqlite3) >= 3.5.9
BuildRequires:  pkgconfig(webkit2gtk-4.0) >= 2.0.0

Requires:       hicolor-icon-theme

Obsoletes:      pantheon-photos < 0.2.4-7
Provides:       pantheon-photos = %{version}-%{release}


%description
The elementary continuation of Shotwell, originally written by Yorba
Foundation.


%prep
%autosetup -n %{srcname}-%{version} -p1


%build
%meson -Dlibunity=false
%meson_build


%install
%meson_install

%find_lang %{appname}


%check
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{appname}.desktop

desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{appname}-viewer.desktop

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml


%files -f %{appname}.lang
%doc README.md
%license COPYING

%{_bindir}/%{appname}

%{_libdir}/%{appname}/

%{_libexecdir}/%{appname}/

%{_datadir}/applications/%{appname}.desktop
%{_datadir}/applications/%{appname}-viewer.desktop
%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/glib-2.0/schemas/%{appname}-extras.gschema.xml
%{_datadir}/metainfo/%{appname}.appdata.xml


%changelog
* Tue Jun 02 2020 Fabio Valentini <decathorpe@gmail.com> - 2.7.0-3
- Drop useless dependency on libunity.

* Mon May 11 2020 Gwyn Ciesla <gwync@protonmail.com> - 2.7.0-2
- Rebuild for new LibRaw

* Wed Apr 08 2020 Fabio Valentini <decathorpe@gmail.com> - 2.7.0-1
- Update to version 2.7.0.

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Nov 16 2019 Fabio Valentini <decathorpe@gmail.com> - 2.6.5-1
- Update to version 2.6.5.

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 17 2019 Fabio Valentini <decathorpe@gmail.com> - 2.6.4-1
- Update to version 2.6.4.

* Tue Apr 16 2019 Adam Williamson <awilliam@redhat.com> - 2.6.3-2
- Rebuild with Meson fix for #1699099

* Tue Apr 16 2019 Fabio Valentini <decathorpe@gmail.com> - 2.6.3-1
- Update to version 2.6.3.

* Mon Mar 18 2019 Fabio Valentini <decathorpe@gmail.com> - 2.6.2-3
- Add backported upstream patch to fix building with gexiv2 >= 0.11.

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 28 2019 Fabio Valentini <decathorpe@gmail.com> - 2.6.2-1
- Update to version 2.6.2.

* Mon Oct 29 2018 Fabio Valentini <decathorpe@gmail.com> - 2.6.1-1
- Update to version 2.6.1.
- Remove upstreamed patch.

* Fri Oct 19 2018 Fabio Valentini <decathorpe@gmail.com> - 2.6.0-1
- Update to version 2.6.0.
- Add patch to fix appdata markup.

* Mon Aug 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5-5
- Fix FTBFS issue with vala 0.42.

* Thu Jul 19 2018 Adam Williamson <awilliam@redhat.com> - 0.2.5-4
- Rebuild for new libraw

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5-2
- Add missing BR: gcc, gcc-c++.

* Fri Jul 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.5-1
- Initial package renamed from pantheon-photos.


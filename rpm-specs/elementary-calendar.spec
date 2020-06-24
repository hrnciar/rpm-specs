%global __provides_exclude_from ^%{_libdir}/%{appname}/.*\\.so$

%global srcname calendar
%global appname io.elementary.calendar

Name:           elementary-calendar
Summary:        Desktop calendar app designed for elementary
Version:        5.0.5
Release:        1%{?dist}
License:        GPLv3+

URL:            https://github.com/elementary/%{srcname}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(champlain-0.12)
BuildRequires:  pkgconfig(champlain-gtk-0.12)
BuildRequires:  pkgconfig(clutter-1.0)
BuildRequires:  pkgconfig(clutter-gtk-1.0)
BuildRequires:  pkgconfig(folks)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(geocode-glib-1.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(granite) >= 5.2.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22
BuildRequires:  pkgconfig(libecal-2.0)
BuildRequires:  pkgconfig(libgeoclue-2.0)
BuildRequires:  pkgconfig(libical-glib)
BuildRequires:  pkgconfig(libsoup-2.4)

# elementary-calendar also provides a generic symbolic icon (actions/calendar-go-today)
Requires:       hicolor-icon-theme

Provides:       maya-calendar = %{version}-%{release}
Obsoletes:      maya-calendar < 0.4.1-6


%description
A slim, lightweight calendar app that syncs and manages multiple
calendars in one place, like Google Calendar, Outlook and CalDAV.


%package        devel
Summary:        The official elementary calendar (devel files)
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
A slim, lightweight calendar app that syncs and manages multiple
calendars in one place, like Google Calendar, Outlook and CalDAV.

This package contains the development files.


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
    %{buildroot}/%{_sysconfdir}/xdg/autostart/%{appname}-daemon.desktop
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{appname}.desktop

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml


%files -f %{appname}.lang
%doc README.md
%license COPYING

%config(noreplace) %{_sysconfdir}/xdg/autostart/%{appname}-daemon.desktop

%{_bindir}/%{appname}
%{_libexecdir}/%{appname}-daemon

%{_libdir}/lib%{name}.so.0*
%{_libdir}/%{appname}/

%{_datadir}/applications/%{appname}.desktop
%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/metainfo/%{appname}.appdata.xml


%files devel
%{_includedir}/%{name}/

%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%{_datadir}/vala/vapi/%{name}.deps
%{_datadir}/vala/vapi/%{name}.vapi


%changelog
* Tue Jun 02 2020 Fabio Valentini <decathorpe@gmail.com> - 5.0.5-1
- Update to version 5.0.5.

* Fri Apr 03 2020 Fabio Valentini <decathorpe@gmail.com> - 5.0.4-1
- Update to version 5.0.4.

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 27 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.3-1
- Update to version 5.0.3.

* Wed Nov 27 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.2-1
- Update to version 5.0.2.

* Tue Nov 26 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.1-1
- Update to version 5.0.1.

* Fri Sep 13 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0-3.20190913.git26275ba
- Add proposed changes for compatibility with libecal-2.0.

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Mar 01 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0-1
- Update to version 5.0.

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 14 2018 Fabio Valentini <decathorpe@gmail.com> - 4.2.3-2
- Rebuild for libedataserver soname bump.

* Tue Oct 16 2018 Fabio Valentini <decathorpe@gmail.com> - 4.2.3-1
- Update to version 4.2.3.

* Wed Oct 03 2018 Fabio Valentini <decathorpe@gmail.com> - 4.2.2-1
- Update to version 4.2.2.

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jul 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2.1-1
- Update to version 0.4.2.1.

* Wed Jun 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2-2
- Rebuild for granite5 soname bump.

* Wed Jun 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.4.2-1
- Initial package renamed from maya-calendar.


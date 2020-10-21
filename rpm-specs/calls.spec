Name:       calls
Version:    0.1.8
Release:    1%{?dist}
Summary:    A phone dialer and call handler

License:        GPLv3+ and MIT
URL:            https://source.puri.sm/Librem5/calls
Source0:        https://source.puri.sm/Librem5/calls/-/archive/v%{version}/%{name}-v%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  cmake

BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.50.0
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libhandy-0.0) >= 0.0.12
BuildRequires:  pkgconfig(gsound)
BuildRequires:  pkgconfig(libpeas-1.0)
BuildRequires:  pkgconfig(gom-1.0)
BuildRequires:  pkgconfig(libebook-contacts-1.2)
BuildRequires:  pkgconfig(folks)
BuildRequires:  pkgconfig(mm-glib)
BuildRequires:  pkgconfig(libfeedback-0.0)

BuildRequires:  desktop-file-utils
BuildRequires:  /usr/bin/xvfb-run
BuildRequires:  /usr/bin/xauth
BuildRequires: libappstream-glib

Requires: hicolor-icon-theme


%description
A phone dialer and call handler.


%prep
%setup -q -n %{name}-v%{version}


%build
%meson
%meson_build


%install
%meson_install
%find_lang %{name}

%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/sm.puri.Calls.metainfo.xml

desktop-file-validate %{buildroot}/%{_datadir}/applications/sm.puri.Calls.desktop

LC_ALL=C.UTF-8 xvfb-run sh <<'SH'
%meson_test
SH


%files -f %{name}.lang
%{_sysconfdir}/xdg/autostart/sm.puri.Calls.desktop
%{_bindir}/%{name}

%dir %{_libdir}/calls
%dir %{_libdir}/calls/plugins
%dir %{_libdir}/calls/plugins/mm
%dir %{_libdir}/calls/plugins/dummy

%{_libdir}/calls/plugins/mm/libmm.so
%{_libdir}/calls/plugins/mm/mm.plugin
%{_libdir}/calls/plugins/dummy/dummy.plugin
%{_libdir}/calls/plugins/dummy/libdummy.so

# ofono is retired so we exclude the plugins 4/24/2020
%exclude %{_libdir}/calls/plugins/ofono/libofono.so
%exclude %{_libdir}/calls/plugins/ofono/ofono.plugin

%{_datadir}/applications/sm.puri.Calls.desktop
%{_datadir}/icons/hicolor/scalable/apps/sm.puri.Calls.svg
%{_datadir}/icons/hicolor/symbolic/apps/sm.puri.Calls-symbolic.svg
%{_datadir}/metainfo/sm.puri.Calls.metainfo.xml

%doc README.md
%license COPYING

%changelog
* Fri Sep 18 2020 Torrey Sorensen <sorensentor@tuta.io> - 0.1.8-1
- Update version 0.1.8

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 14 2020 Torrey Sorensen <sorensentor@tuta.io> - 0.1.7-1
- Update version 0.1.7

* Wed Jun 24 2020 Torrey Sorensen <sorensentor@tuta.io> - 0.1.6-2
- Rebuild for broken libebook-contacts

* Fri Jun 12 2020 Torrey Sorensen <sorensentor@tuta.io> - 0.1.6-1
- Update version 0.1.6

* Mon May 18 2020 Torrey sorensen <sorensentor@tuta.io> - 0.1.5-1
- Owning the directories for calls, plugins, and mm.
- Update version 0.1.5.
- Adding MIT to License
- Upstream changed "appdata" to "metainfo"

* Fri Apr 24 2020 Torrey Sorensen <sorensentor@tuta.io> - 0.1.4-1
- Updating version 0.1.4. Fixing comments from review regarding ofono and appdata.

* Fri Mar 27 2020 Torrey Sorensen <sorensentor@tuta.io> - 0.1.3-1 
- Updating version 0.1.3. Adding tests

* Wed Mar 25 2020 Torrey Sorensen <sorensentor@tuta.io> - 0.1.2-2
- Adding license and meson_test. Remove buildid

* Sun Mar 08 2020 Torrey Sorensen <sorensentor@tuta.io> - 0.1.2-1
- Initial packaging

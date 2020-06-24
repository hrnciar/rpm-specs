%global libical_version 3.0.5
%global gsettings_desktop_schemas_version 3.21.2
%global edataserver_version 3.33.2
%global glib2_version 2.58.0
%global gtk3_version 3.22.20

Name:           gnome-calendar
Version:        3.36.2
Release:        1%{?dist}
Summary:        Simple and beautiful calendar application designed to fit GNOME 3

License:        GPLv3+
URL:            https://wiki.gnome.org/Apps/Calendar
Source0:        https://download.gnome.org/sources/%{name}/3.36/%{name}-%{version}.tar.xz

# These are all backports of crasher fix PRs by mcatanzaro
Patch2:         84.patch

BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:  pkgconfig(geocode-glib-1.0)
BuildRequires:  pkgconfig(gio-2.0) >= %{glib2_version}
BuildRequires:  pkgconfig(glib-2.0) >= %{glib2_version}
BuildRequires:  pkgconfig(gsettings-desktop-schemas) >= %{gsettings_desktop_schemas_version}
BuildRequires:  pkgconfig(gtk+-3.0) >= %{gtk3_version}
BuildRequires:  pkgconfig(gweather-3.0)
BuildRequires:  pkgconfig(libdazzle-1.0)
BuildRequires:  pkgconfig(libecal-2.0) >= %{edataserver_version}
BuildRequires:  pkgconfig(libedataserver-1.2) >= %{edataserver_version}
BuildRequires:  pkgconfig(libgeoclue-2.0)
BuildRequires:  pkgconfig(libhandy-0.0)
BuildRequires:  pkgconfig(libical) >= %{libical_version}
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  /usr/bin/appstream-util
BuildRequires:  desktop-file-utils

Requires:       evolution-data-server%{?_isa} >= %{edataserver_version}
Requires:       glib2%{?_isa} >= %{glib2_version}
Requires:       gsettings-desktop-schemas%{?_isa} >= %{gsettings_desktop_schemas_version}
Requires:       gtk3%{?_isa} >= %{gtk3_version}
Requires:       libical%{?_isa} >= %{libical_version}

%description
Calendar is a simple and beautiful calendar application designed to fit
GNOME 3.
Features:
* Week, month and year views
* Basic editing of events
* Evolution Data Server integration
* Search support

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
%{find_lang} %{name}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.Calendar.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/org.gnome.Calendar.appdata.xml

%files -f %{name}.lang
%doc NEWS README.md
%license COPYING
%{_bindir}/gnome-calendar
%{_datadir}/applications/org.gnome.Calendar.desktop
%{_datadir}/dbus-1/services/org.gnome.Calendar.service
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Calendar*.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.Calendar*-symbolic.svg
%{_datadir}/metainfo/org.gnome.Calendar.appdata.xml
%{_datadir}/glib-2.0/schemas/org.gnome.calendar.enums.xml
%{_datadir}/glib-2.0/schemas/org.gnome.calendar.gschema.xml
# co-own these directories
%dir %{_datadir}/gnome-shell
%dir %{_datadir}/gnome-shell/search-providers
%{_datadir}/gnome-shell/search-providers/org.gnome.Calendar.search-provider.ini

%changelog
* Mon Jun 22 2020 Kalev Lember <klember@redhat.com> - 3.36.2-1
- Update to 3.36.2

* Mon Apr 20 2020 Kalev Lember <klember@redhat.com> - 3.36.1-1
- Update to 3.36.1

* Sat Mar 07 2020 Kalev Lember <klember@redhat.com> - 3.36.0-1
- Update to 3.36.0

* Mon Mar 02 2020 Kalev Lember <klember@redhat.com> - 3.35.92-1
- Update to 3.35.92

* Tue Feb 18 2020 Kalev Lember <klember@redhat.com> - 3.35.2-1
- Update to 3.35.2

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.34.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 10 2019 Kalev Lember <klember@redhat.com> - 3.34.2-1
- Update to 3.34.2

* Mon Oct 07 2019 Kalev Lember <klember@redhat.com> - 3.34.1-1
- Update to 3.34.1

* Sat Sep 21 2019 Michael Catanzaro <mcatanzaro@gnome.org> - 3.34.0-2
- Add patch to fix rhbz#1753558

* Mon Sep 09 2019 Kalev Lember <klember@redhat.com> - 3.34.0-1
- Update to 3.34.0

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.33.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 19 2019 Kalev Lember <klember@redhat.com> - 3.33.4-1
- Update to 3.33.4

* Wed Jul 17 2019 Michael Catanzaro <mcatanzaro@gnome.org> - 3.33.1-5
- Add another patch to fix another use-after-free vulnerability

* Wed Jul 17 2019 Michael Catanzaro <mcatanzaro@gnome.org> - 3.33.1-4
- Add patch to fix a use-after-free vulnerability

* Mon Jul 08 2019 Kalev Lember <klember@redhat.com> - 3.33.1-3
- Rebuilt for libgweather soname bump

* Thu Jul 04 2019 Adam Williamson <awilliam@redhat.com> - 3.33.1-2
- Backport a whole series of crasher fix PRs by mcatanzaro

* Fri Jun 21 2019 Kalev Lember <klember@redhat.com> - 3.33.1-1
- Update to 3.33.1

* Tue May 21 2019 Milan Crha <mcrha@redhat.com> - 3.32.2-2
- Add patch to build against newer evolution-data-server (libecal-2.0)

* Fri May 10 2019 Kalev Lember <klember@redhat.com> - 3.32.2-1
- Update to 3.32.2

* Mon May 06 2019 Kalev Lember <klember@redhat.com> - 3.32.1-1
- Update to 3.32.1

* Mon Mar 11 2019 Kalev Lember <klember@redhat.com> - 3.32.0-1
- Update to 3.32.0

* Thu Feb 07 2019 Kalev Lember <klember@redhat.com> - 3.31.90-1
- Update to 3.31.90

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.30.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 12 2018 Milan Crha <mcrha@redhat.com> - 3.30.1-2
- Rebuilt for evolution-data-server soname bump

* Sat Nov 03 2018 Kalev Lember <klember@redhat.com> - 3.30.1-1
- Update to 3.30.1

* Thu Sep 06 2018 Kalev Lember <klember@redhat.com> - 3.30.0-1
- Update to 3.30.0

* Mon Aug 13 2018 Kalev Lember <klember@redhat.com> - 3.29.90-1
- Update to 3.29.90

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.28.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 02 2018 Kalev Lember <klember@redhat.com> - 3.28.2-1
- Update to 3.28.2

* Tue Apr 10 2018 Kalev Lember <klember@redhat.com> - 3.28.1-1
- Update to 3.28.1

* Mon Mar 12 2018 Kalev Lember <klember@redhat.com> - 3.28.0-1
- Update to 3.28.0

* Mon Mar 05 2018 Kalev Lember <klember@redhat.com> - 3.27.92-1
- Update to 3.27.92

* Wed Feb 07 2018 Kalev Lember <klember@redhat.com> - 3.26.3-2
- Rebuilt for evolution-data-server soname bump

* Wed Jan 17 2018 Kalev Lember <klember@redhat.com> - 3.26.3-1
- Update to 3.26.3

* Fri Jan 05 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.26.2-3
- Remove obsolete scriptlets

* Wed Nov 08 2017 Milan Crha <mcrha@redhat.com> - 3.26.2-2
- Rebuild for newer libical

* Sun Oct 08 2017 Kalev Lember <klember@redhat.com> - 3.26.2-1
- Update to 3.26.2

* Thu Sep 21 2017 Kalev Lember <klember@redhat.com> - 3.26.1-1
- Update to 3.26.1

* Wed Sep 13 2017 Kalev Lember <klember@redhat.com> - 3.26.0-1
- Update to 3.26.0

* Sat Aug 12 2017 David King <amigadave@amigadave.com> - 3.25.90-1
- Update to 3.25.90

* Tue Aug 01 2017 Kalev Lember <klember@redhat.com> - 3.25.3-1
- Update to 3.25.3

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.24.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 12 2017 Kalev Lember <klember@redhat.com> - 3.24.3-1
- Update to 3.24.3

* Wed May 10 2017 Kalev Lember <klember@redhat.com> - 3.24.2-1
- Update to 3.24.2

* Tue Apr 25 2017 Kalev Lember <klember@redhat.com> - 3.24.1-1
- Update to 3.24.1

* Tue Mar 21 2017 Kalev Lember <klember@redhat.com> - 3.24.0-1
- Update to 3.24.0

* Fri Mar 17 2017 Kalev Lember <klember@redhat.com> - 3.23.92-1
- Update to 3.23.92

* Mon Mar 06 2017 Kalev Lember <klember@redhat.com> - 3.23.91.1-1
- Update to 3.23.91.1

* Wed Feb 15 2017 Richard Hughes <rhughes@redhat.com> - 3.23.90-1
- Update to 3.23.90

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Kalev Lember <klember@redhat.com> - 3.22.2-1
- Update to 3.22.2

* Sun Oct 02 2016 David King <amigadave@amigadave.com> - 3.22.1-1
- Update to 3.22.1

* Tue Sep 20 2016 Kalev Lember <klember@redhat.com> - 3.22.0-1
- Update to 3.22.0

* Fri Sep 16 2016 Kalev Lember <klember@redhat.com> - 3.21.92-1
- Update to 3.21.92

* Wed Aug 31 2016 David King <amigadave@amigadave.com> - 3.21.91-1
- Update to 3.21.91

* Tue Jul 26 2016 Kalev Lember <klember@redhat.com> - 3.21.4-1
- Update to 3.21.4

* Mon Jul 18 2016 Milan Crha <mcrha@redhat.com> - 3.21.2-2
- Rebuild for newer evolution-data-server

* Wed Jun 22 2016 Richard Hughes <rhughes@redhat.com> - 3.21.2-1
- Update to 3.21.2

* Tue Jun 21 2016 Milan Crha <mcrha@redhat.com> - 3.20.2-2
- Rebuild for newer evolution-data-server

* Mon May 09 2016 Kalev Lember <klember@redhat.com> - 3.20.2-1
- Update to 3.20.2

* Fri Apr 15 2016 David Tardon <dtardon@redhat.com> - 3.20.1-2
- rebuild for ICU 57.1

* Thu Apr 14 2016 Kalev Lember <klember@redhat.com> - 3.20.1-1
- Update to 3.20.1
- Set minimum required gtk3 version

* Tue Mar 22 2016 Kalev Lember <klember@redhat.com> - 3.20.0-1
- Update to 3.20.0

* Tue Mar 15 2016 David King <amigadave@amigadave.com> - 3.19.92-1
- Update to 3.19.92

* Thu Mar 03 2016 David King <amigadave@amigadave.com> - 3.19.91-1
- Update to 3.19.91

* Tue Feb 16 2016 David King <amigadave@amigadave.com> - 3.19.90-1
- Update to 3.19.90

* Tue Feb 16 2016 Milan Crha <mcrha@redhat.com> - 3.19.4-3
- Rebuild for newer evolution-data-server

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.19.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 20 2016 Kalev Lember <klember@redhat.com> - 3.19.4-1
- Update to 3.19.4

* Mon Jan 18 2016 David Tardon <dtardon@redhat.com> - 3.19.3-2
- rebuild for libical 2.0.0

* Wed Dec 16 2015 Kalev Lember <klember@redhat.com> - 3.19.3-1
- Update to 3.19.3

* Sat Oct 17 2015 Kalev Lember <klember@redhat.com> - 3.18.1-1
- Update to 3.18.1

* Mon Sep 21 2015 Kalev Lember <klember@redhat.com> - 3.18.0-1
- Update to 3.18.0

* Mon Sep 14 2015 Kalev Lember <klember@redhat.com> - 3.17.92-1
- Update to 3.17.92

* Wed Aug 19 2015 Kalev Lember <klember@redhat.com> - 3.17.90-1
- Update to 3.17.90

* Mon Jul 20 2015 David King <amigadave@amigadave.com> - 3.17.4-1
- Update to 3.17.4

* Tue Jun 23 2015 David King <amigadave@amigadave.com> - 3.17.3-1
- Update to 3.17.3
- Use pkgconfig for BuildRequires

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.17.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun May 31 2015 Kalev Lember <kalevlember@gmail.com> - 3.17.2-1
- Update to 3.17.2

* Tue May 12 2015 Kalev Lember <kalevlember@gmail.com> - 3.16.2-1
- Update to 3.16.2

* Tue Apr 28 2015 Milan Crha <mcrha@redhat.com> - 3.16.1-2
- Rebuild for newer evolution-data-server

* Thu Apr 16 2015 Kalev Lember <kalevlember@gmail.com> - 3.16.1-1
- Update to 3.16.1

* Fri Mar 20 2015 Kalev Lember <kalevlember@gmail.com> - 3.16.0-1
- Update to 3.16.0

* Tue Mar 17 2015 Kalev Lember <kalevlember@gmail.com> - 3.15.92-1
- Update to 3.15.92

* Tue Mar 03 2015 Kalev Lember <kalevlember@gmail.com> - 3.15.91-1
- Update to 3.15.91
- Drop large ChangeLog file from docs

* Tue Feb 17 2015 David King <amigadave@amigadave.com> - 3.15.90-2
- Add missing colon after glib-compile-schemas

* Tue Feb 17 2015 David King <amigadave@amigadave.com> - 3.15.90-1
- Update to 3.15.90
- Use license macro for COPYING

* Sun Jan 25 2015 Igor Gnatenko <ignatenko@src.gnome.org> - 3.15.4.1-2
- Add check section
- Add hook for mime entry

* Sat Jan 24 2015 Igor Gnatenko <ignatenko@src.gnome.org> - 3.15.4.1-1
- 3.15.4.1

* Wed Jan 21 2015 Igor Gnatenko <ignatenko@src.gnome.org> - 3.15.4-1
- 3.15.4

* Fri Jan 02 2015 Igor Gnatenko <ignatenko@src.gnome.org> - 3.15.3.1-1
- Initial package

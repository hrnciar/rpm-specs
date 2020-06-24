%global libgweather_version 3.32.0

Name:           gnome-clocks
Version:        3.36.2
Release:        1%{?dist}
Summary:        Clock application designed for GNOME 3

License:        GPLv2+
URL:            https://wiki.gnome.org/Apps/Clocks
Source0:        https://download.gnome.org/sources/gnome-clocks/3.36/%{name}-%{version}.tar.xz

BuildRequires:  meson
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  itstool
BuildRequires:  libappstream-glib
BuildRequires:  vala

BuildRequires:  pkgconfig(gtk+-3.0) >= 3.20
BuildRequires:  pkgconfig(gweather-3.0) >= %{libgweather_version}
BuildRequires:  pkgconfig(gnome-desktop-3.0) >= 3.8
BuildRequires:  pkgconfig(glib-2.0) >= 2.44
BuildRequires:  pkgconfig(gobject-2.0) >= 2.44
BuildRequires:  pkgconfig(libgeoclue-2.0) >= 2.4
BuildRequires:  pkgconfig(libhandy-0.0)
BuildRequires:  pkgconfig(geocode-glib-1.0) >= 1.0
BuildRequires:  pkgconfig(gsound) >= 0.98

Requires:       libgweather%{?_isa} >= %{libgweather_version}

%description
Clock application designed for GNOME 3

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
%find_lang gnome-clocks --with-gnome

%check
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/org.gnome.clocks.desktop

%files -f gnome-clocks.lang
%doc AUTHORS.md NEWS.md README.md
%license LICENSE.md
%{_bindir}/gnome-clocks
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.clocks.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.clocks-symbolic.svg
%{_datadir}/applications/org.gnome.clocks.desktop
%{_datadir}/dbus-1/services/org.gnome.clocks.service
%{_datadir}/glib-2.0/schemas/org.gnome.clocks.gschema.xml
%dir %{_datadir}/gnome-shell/
%dir %{_datadir}/gnome-shell/search-providers/
%{_datadir}/gnome-shell/search-providers/org.gnome.clocks.search-provider.ini
%{_datadir}/metainfo/org.gnome.clocks.metainfo.xml

%changelog
* Sun May 10 2020 Kalev Lember <klember@redhat.com> - 3.36.2-1
- Update to 3.36.2

* Tue Apr 14 2020 Michael Catanzaro <mcatanzaro@gnome.org> - 3.36.0-2
- Fix crashes when sunrise/sunset calculation goes badly

* Thu Mar 05 2020 Kalev Lember <klember@redhat.com> - 3.36.0-1
- Update to 3.36.0

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.34.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 16 2020 Kalev Lember <klember@redhat.com> - 3.34.0-2
- Rebuilt for libgnome-desktop soname bump

* Mon Sep 09 2019 Kalev Lember <klember@redhat.com> - 3.34.0-1
- Update to 3.34.0

* Mon Aug 12 2019 Kalev Lember <klember@redhat.com> - 3.33.1-1
- Update to 3.33.1

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.32.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jul 21 2019 Yanko Kaneti <yaneti@declera.com> - 3.32.0-3
- Rebuilt for gnome-desktop3 soname bump

* Mon Jul 08 2019 Kalev Lember <klember@redhat.com> - 3.32.0-2
- Rebuilt for libgweather soname bump

* Mon Mar 11 2019 Kalev Lember <klember@redhat.com> - 3.32.0-1
- Update to 3.32.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.31.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jan 06 2019 Kalev Lember <klember@redhat.com> - 3.31.2-1
- Update to 3.31.2

* Mon Nov 12 2018 Yanko Kaneti <yaneti@declera.com> - 3.31.1-1
- Update to 3.31.1. Drop upstreamed patch

* Mon Oct 22 2018 Kalev Lember <klember@redhat.com> - 3.30.1-1
- Update to 3.30.1

* Tue Sep 18 2018 Yanko Kaneti <yaneti@declera.com> - 3.30.0-3
- Fix timer visual glitch. Bug #1630248

* Sun Sep  9 2018 Yanko Kaneti <yaneti@declera.com> - 3.30.0-2
- Rebuild

* Sat Sep  1 2018 Yanko Kaneti <yaneti@declera.com> - 3.30.0-1
- Update to 3.30.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.28.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Mar 10 2018 Yanko Kaneti <yaneti@declera.com> - 3.28.0-1
- Update to 3.28.0. Drop upstreamed patch

* Wed Feb 21 2018 Yanko Kaneti <yaneti@declera.com> - 3.27.1-4
- Add workaround for frequent crashes in the shell search provider

* Mon Feb 12 2018 Yanko Kaneti <yaneti@declera.com> - 3.27.1-3
- Rebuild for gnome-desktop3 soname bump

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.27.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Feb 05 2018 Kalev Lember <klember@redhat.com> - 3.27.1-1
- Update to 3.27.1

* Fri Jan 05 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.26.1-2
- Remove obsolete scriptlets

* Sun Oct 15 2017 Kalev Lember <klember@redhat.com> - 3.26.1-1
- Update to 3.26.1

* Sun Sep 10 2017 Yanko Kaneti <yaneti@declera.com> - 3.26.0-1
- Update to 3.26.0

* Sun Aug 20 2017 Yanko Kaneti <yaneti@declera.com> - 3.25.90-1
- Update to 3.25.90
- Drop symlink patch, meson 0.43 does it by default

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.25.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.25.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jul  1 2017 Yanko Kaneti <yaneti@declera.com> - 3.25.2-1
- Update to 3.25.2
- Drop appdata modification, fixed upstream
- Update meson patch

* Tue May 23 2017 Yanko Kaneti <yaneti@declera.com> - 3.25.1-1
- Update to 3.25.1. Meson. BR reshuffle

* Mon Mar 20 2017 Yanko Kaneti <yaneti@declera.com> - 3.24.0-1
- Update to 3.24.0

* Tue Feb 14 2017 Richard Hughes <rhughes@redhat.com> - 3.23.90-1
- Update to 3.23.90

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Oct 10 2016 Yanko Kaneti <yaneti@declera.com> - 3.22.1-1
- Update to 3.22.1

* Thu Sep 22 2016 Kalev Lember <klember@redhat.com> - 3.22.0-2
- BR vala instead of obsolete vala-tools subpackage

* Mon Sep 19 2016 Kalev Lember <klember@redhat.com> - 3.22.0-1
- Update to 3.22.0
- Use make_install macro

* Mon Aug 29 2016 Kalev Lember <klember@redhat.com> - 3.21.2-1
- Update to 3.21.2

* Thu Aug 18 2016 Kalev Lember <klember@redhat.com> - 3.21.1-1
- Update to 3.21.1
- Update project URLs
- Move desktop file validation to the check section

* Sun May  8 2016 Yanko Kaneti <yaneti@declera.com> - 3.20.1-1
- Update to 3.20.1

* Sun Mar 20 2016 Yanko Kaneti <yaneti@declera.com> - 3.20.0-1
- Update to 3.20.0

* Sun Feb 21 2016 Yanko Kaneti <yaneti@declera.com> - 3.19.2-1
- Update to 3.19.2

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.19.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Dec 14 2015 Yanko Kaneti <yaneti@declera.com> - 3.19.1-1
- First development release

* Mon Sep 21 2015 Yanko Kaneti <yaneti@declera.com> - 3.18.0-1
- Update to 3.18.0

* Mon Sep 14 2015 Kalev Lember <klember@redhat.com> - 3.16.2-1
- Update to 3.16.2

* Mon Aug  3 2015 Yanko Kaneti <yaneti@declera.com> - 3.16.1-4
- Fix stopwatch redraw. #1249376.

* Wed Jul 22 2015 Yanko Kaneti <yaneti@declera.com> - 3.16.1-3
- Bump for gnome-desktop3 soname change

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.16.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Apr 13 2015 Yanko Kaneti <yaneti@declera.com> - 3.16.1-1
- Update to 3.16.1
- No more HighContrast specific icons

* Mon Mar 30 2015 Richard Hughes <rhughes@redhat.com> - 3.16.0-2
- Use better AppData screenshots

* Mon Mar 23 2015 Yanko Kaneti <yaneti@declera.com> - 3.16.0-1
- Update to 3.16.0
- Use license macro

* Sat Mar 14 2015 Yanko Kaneti <yaneti@declera.com> - 3.15.92-1
- Update to 3.15.92

* Thu Feb 19 2015 Yanko Kaneti <yaneti@declera.com> - 3.15.90-1
- Update to 3.15.90. BR intltool >= 0.50.1

* Mon Dec  1 2014 Yanko Kaneti <yaneti@declera.com> - 3.15.1-1
- First development release from the 3.16 cycle.
- Depends on gsound

* Fri Nov 14 2014 Florian Müllner <fmuellner@redhat.com> - 3.14.1-2
- Remove libnotify dependency

* Mon Oct 13 2014 Yanko Kaneti <yaneti@declera.com> - 3.14.1-1
- Update to 3.14.1

* Mon Sep 22 2014 Yanko Kaneti <yaneti@declera.com> - 3.14.0-1
- Update to 3.14.0

* Wed Sep 17 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.92-1
- Update to 3.13.92

* Tue Sep  2 2014 Yanko Kaneti <yaneti@declera.com> - 3.13.91-1
- Update to 3.13.91

* Tue Aug 19 2014 Yanko Kaneti <yaneti@declera.com> - 3.13.2-1
- Update to 3.13.2

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.13.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 22 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.1-1
- Update to 3.13.1

* Thu Jun 12 2014 Yanko Kaneti <yaneti@declera.com> - 3.12.0-3
- Upstream patch to fix empty window with latest gtk+

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Mar 24 2014 Yanko Kaneti <yaneti@declera.com> - 3.12.0-1
- Update to 3.12.0

* Wed Mar 19 2014 Yanko Kaneti <yaneti@declera.com> - 3.11.92-1
- Update to 3.11.92

* Wed Feb 19 2014 Richard Hughes <rhughes@redhat.com> - 3.11.90-3
- Rebuilt for gnome-desktop soname bump

* Wed Feb 19 2014 Yanko Kaneti <yaneti@declera.com> - 3.11.90-2
- Rebuilt for gnome-desktop soname bump

* Tue Feb 18 2014 Yanko Kaneti <yaneti@declera.com> - 3.11.90-1
- Update to 3.11.90

* Tue Nov 19 2013 Yanko Kaneti <yaneti@declera.com> - 3.11.1-1
- First release from the 3.11 development series.

* Mon Oct 14 2013 Yanko Kaneti <yaneti@declera.com> - 3.10.1-1
- Update to 3.10.1

* Mon Sep 23 2013 Yanko Kaneti <yaneti@declera.com> - 3.10.0-1
- Update to 3.10.0

* Tue Sep 17 2013 Yanko Kaneti <yaneti@declera.com> - 3.9.92-1
- Update to 3.9.92. Geolocation support
- New BRs: itstool geoclue2-devel geocode-glib-devel
- Add help

* Tue Sep 03 2013 Kalev Lember <kalevlember@gmail.com> - 3.9.91-1
- Update to 3.9.91

* Mon Aug 19 2013 Yanko Kaneti <yaneti@declera.com> - 3.9.90-1
- Update to 3.9.90

* Sun Aug  4 2013 Yanko Kaneti <yaneti@declera.com> - 3.9.3-2
- Bump for libgweather soname change

* Sun Aug  4 2013 Yanko Kaneti <yaneti@declera.com> - 3.9.3-1
- Update to 3.9.3

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 21 2013 Kalev Lember <kalevlember@gmail.com> - 3.9.2-1
- Update to 3.9.2

* Tue Jun 11 2013 Yanko Kaneti <yaneti@declera.com> - 3.9.1-1
- Update to 3.9.1

* Tue May 14 2013 Richard Hughes <rhughes@redhat.com> - 3.8.2-1
- Update to 3.8.2

* Mon Apr 15 2013 Kalev Lember <kalevlember@gmail.com> - 3.8.1-1
- Update to 3.8.1

* Tue Mar 26 2013 Yanko Kaneti <yaneti@declera.com> - 3.8.0-1
- Update to 3.7.92

* Mon Mar 18 2013 Yanko Kaneti <yaneti@declera.com> - 3.7.92-1
- New upstream release - 3.7.92

* Wed Mar  6 2013 Yanko Kaneti <yaneti@declera.com> - 3.7.91-1
- New upstream release - 3.7.91

* Wed Feb 20 2013 Yanko Kaneti <yaneti@declera.com> - 3.7.90-1
- New upstream release - 3.7.90. Moving to vala.

* Wed Feb  6 2013 Yanko Kaneti <yaneti@declera.com> - 0.1.6-3
- Use python3-canberra

* Wed Feb  6 2013 Yanko Kaneti <yaneti@declera.com> - 0.1.6-2
- pycairo is python3-cairo in python3 land.

* Wed Feb  6 2013 Yanko Kaneti <yaneti@declera.com> - 0.1.6-1
- Update to 0.1.6. Handle the move to autotools.

* Tue Dec  4 2012 Yanko Kaneti <yaneti@declera.com> - 0.1.5-1
- Update to 0.1.5.
- Additionaly require gnome-desktop3 and libnotify

* Tue Oct 16 2012 Yanko Kaneti <yaneti@declera.com> - 0.1.4-1
- Update to 0.1.4

* Mon Oct  1 2012 Yanko Kaneti <yaneti@declera.com> - 0.1.3-2
- Add packaging snippets to update the icon cache

* Thu Sep 27 2012 Yanko Kaneti <yaneti@declera.com> - 0.1.3-1
- Update to 0.1.3

* Wed Sep 26 2012 Yanko Kaneti <yaneti@declera.com> - 0.1.2-3
- Actually update the License tag

* Wed Sep 26 2012 Yanko Kaneti <yaneti@declera.com> - 0.1.2-2
- Use packaged pycanberra

* Wed Sep 26 2012 Yanko Kaneti <yaneti@declera.com> - 0.1.2-1
- Latest from upstream - 0.1.2

* Sat Sep 15 2012 Yanko Kaneti <yaneti@declera.com> - 0.1.1-2
- Address review issues. Separate bundled pycanberra licensing

* Thu Sep 13 2012 Yanko Kaneti <yaneti@declera.com> - 0.1.1-1
- Package for review

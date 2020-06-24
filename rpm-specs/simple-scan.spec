Name:           simple-scan
Version:        3.37.2
Release:        1%{?dist}
Summary:        Simple scanning utility

License:        GPLv3+
URL:            https://launchpad.net/%{name}
Source0:        https://download.gnome.org/sources/%{name}/3.37/%{name}-%{version}.tar.xz

BuildRequires:  meson
BuildRequires:  sane-backends-devel
BuildRequires:  gettext
BuildRequires:  itstool
BuildRequires:  /usr/bin/appstream-util
BuildRequires:  /usr/bin/desktop-file-validate
BuildRequires:  /usr/bin/valac
BuildRequires:  pkgconfig(colord)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(libwebpmux)
BuildRequires:  pkgconfig(packagekit-glib2) >= 1.1.5
BuildRequires:  pkgconfig(zlib)

Requires:       xdg-utils

%description
Simple Scan is an easy-to-use application, designed to let users connect their
scanner and quickly have the image/document in an appropriate format.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name} --with-man --with-gnome

%check
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/%{name}.appdata.xml
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop

%files -f %{name}.lang
%doc NEWS README.md
%license COPYING
%{_mandir}/man1/%{name}.1*
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.SimpleScan.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.SimpleScan-symbolic.svg
%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.SimpleScan.gschema.xml

%changelog
* Thu Jun 04 2020 Kalev Lember <klember@redhat.com> - 3.37.2-1
- Update to 3.37.2

* Tue May 05 2020 Kalev Lember <klember@redhat.com> - 3.37.1-1
- Update to 3.37.1

* Wed Apr 29 2020 Kalev Lember <klember@redhat.com> - 3.36.2-1
- Update to 3.36.2

* Fri Mar 27 2020 Kalev Lember <klember@redhat.com> - 3.36.1-1
- Update to 3.36.1

* Fri Mar 06 2020 Kalev Lember <klember@redhat.com> - 3.36.0-1
- Update to 3.36.0

* Mon Mar 02 2020 Kalev Lember <klember@redhat.com> - 3.35.92-1
- Update to 3.35.92

* Mon Feb 17 2020 Kalev Lember <klember@redhat.com> - 3.35.91-1
- Update to 3.35.91

* Sun Feb 02 2020 Kalev Lember <klember@redhat.com> - 3.35.90-1
- Update to 3.35.90

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.35.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 10 2020 Kalev Lember <klember@redhat.com> - 3.35.3-1
- Update to 3.35.3

* Mon Dec 02 2019 Kalev Lember <klember@redhat.com> - 3.35.2-1
- Update to 3.35.2

* Wed Nov 27 2019 Kalev Lember <klember@redhat.com> - 3.34.2-1
- Update to 3.34.2

* Mon Oct 07 2019 Kalev Lember <klember@redhat.com> - 3.34.1-1
- Update to 3.34.1

* Mon Sep 09 2019 Kalev Lember <klember@redhat.com> - 3.34.0-1
- Update to 3.34.0

* Tue Sep 03 2019 Kalev Lember <klember@redhat.com> - 3.33.92-1
- Update to 3.33.92

* Wed Aug 21 2019 Kalev Lember <klember@redhat.com> - 3.33.91-1
- Update to 3.33.91

* Mon Aug 05 2019 David King <amigadave@amigadave.com> - 3.33.90-1
- Update to 3.33.90

* Tue Jul 23 2019 David King <amigadave@amigadave.com> - 3.33.4-1
- Update to 3.33.4

* Tue Jun 18 2019 Kalev Lember <klember@redhat.com> - 3.33.3-1
- Update to 3.33.3

* Thu May 09 2019 Kalev Lember <klember@redhat.com> - 3.33.1-1
- Update to 3.33.1

* Mon May 06 2019 Kalev Lember <klember@redhat.com> - 3.32.2.1-1
- Update to 3.32.2.1

* Tue Apr 16 2019 Adam Williamson <awilliam@redhat.com> - 3.32.2-2
- Rebuild with Meson fix for #1699099

* Wed Apr 10 2019 Kalev Lember <klember@redhat.com> - 3.32.2-1
- Update to 3.32.2

* Tue Apr 09 2019 Kalev Lember <klember@redhat.com> - 3.32.1-1
- Update to 3.32.1

* Mon Mar 11 2019 Kalev Lember <klember@redhat.com> - 3.32.0-1
- Update to 3.32.0

* Mon Mar 04 2019 Kalev Lember <klember@redhat.com> - 3.31.92-1
- Update to 3.31.92

* Tue Feb 19 2019 Kalev Lember <klember@redhat.com> - 3.31.91-2
- Rebuilt against fixed atk (#1626575)

* Tue Feb 19 2019 Kalev Lember <klember@redhat.com> - 3.31.91-1
- Update to 3.31.91

* Sun Feb 10 2019 Kalev Lember <klember@redhat.com> - 3.31.90.1-1
- Update to 3.31.90.1

* Mon Feb 04 2019 Kalev Lember <klember@redhat.com> - 3.31.90-1
- Update to 3.31.90

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.31.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 08 2019 Kalev Lember <klember@redhat.com> - 3.31.4-1
- Update to 3.31.4
- Don't recommend yelp

* Fri Oct 26 2018 Kalev Lember <klember@redhat.com> - 3.30.2-1
- Update to 3.30.2

* Fri Sep 28 2018 Kalev Lember <klember@redhat.com> - 3.30.1.1-1
- Update to 3.30.1.1

* Wed Sep 26 2018 Kalev Lember <klember@redhat.com> - 3.30.1-1
- Update to 3.30.1

* Thu Sep 06 2018 Kalev Lember <klember@redhat.com> - 3.30.0-1
- Update to 3.30.0

* Mon Aug 13 2018 Kalev Lember <klember@redhat.com> - 3.29.91-1
- Update to 3.29.91

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.28.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 09 2018 Kalev Lember <klember@redhat.com> - 3.28.1-1
- Update to 3.28.1

* Mon Mar 12 2018 Kalev Lember <klember@redhat.com> - 3.28.0-1
- Update to 3.28.0

* Tue Mar 06 2018 Kalev Lember <klember@redhat.com> - 3.27.92-1
- Update to 3.27.92

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.27.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Feb 05 2018 Kalev Lember <klember@redhat.com> - 3.27.90-1
- Update to 3.27.90

* Sat Jan 06 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.27.3-2
- Remove obsolete scriptlets

* Thu Dec 14 2017 David King <amigadave@amigadave.com> - 3.27.3-1
- Update to 3.27.3

* Mon Nov 13 2017 David King <amigadave@amigadave.com> - 3.27.2-1
- Update to 3.27.2

* Mon Oct 30 2017 David King <amigadave@amigadave.com> - 3.27.1-1
- Update to 3.27.1

* Mon Oct 09 2017 Kalev Lember <klember@redhat.com> - 3.26.1-1
- Update to 3.26.1

* Mon Sep 11 2017 Kalev Lember <klember@redhat.com> - 3.26.0-1
- Update to 3.26.0

* Thu Sep 07 2017 David King <amigadave@amigadave.com> - 3.25.92-1
- Update to 3.25.92

* Mon Aug 21 2017 David King <amigadave@amigadave.com> - 3.25.91-1
- Update to 3.25.91

* Mon Aug 07 2017 Kalev Lember <klember@redhat.com> - 3.25.90-1
- Update to 3.25.90

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.25.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.25.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 18 2017 David King <amigadave@amigadave.com> - 3.25.4-1
- Update to 3.25.4

* Fri Jun 23 2017 David King <amigadave@amigadave.com> - 3.25.3-1
- Update to 3.25.3

* Tue May 23 2017 David King <amigadave@amigadave.com> - 3.25.2-1
- Update to 3.25.2

* Tue Apr 25 2017 David King <amigadave@amigadave.com> - 3.25.1-1
- Update to 3.25.1

* Mon Mar 20 2017 David King <amigadave@amigadave.com> - 3.24.0-1
- Update to 3.24.0

* Mon Feb 13 2017 David King <amigadave@amigadave.com> - 3.23.90-1
- Update to 3.23.90

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.23.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 12 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 3.23.3-1
- Update to 3.23.3

* Wed Nov 30 2016 David King <amigadave@amigadave.com> - 3.23.2-1
- Update to 3.23.2

* Tue Sep 20 2016 David King <amigadave@amigadave.com> - 3.22.0.1-1
- Update to 3.22.0.1
- Use gettext instead of intltool

* Sat Sep 03 2016 Kalev Lember <klember@redhat.com> - 3.21.90-1
- Update to 3.21.90

* Tue Apr 26 2016 David King <amigadave@amigadave.com> - 3.21.1-1
- Update to 3.21.1

* Mon Mar 21 2016 David King <amigadave@amigadave.com> - 3.20.0-1
- Update to 3.20.0

* Mon Mar 14 2016 David King <amigadave@amigadave.com> - 3.19.92-1
- Update to 3.19.92

* Sun Feb 28 2016 David King <amigadave@amigadave.com> - 3.19.91-1
- Update to 3.19.91

* Mon Feb 15 2016 David King <amigadave@amigadave.com> - 3.19.90-1
- Update to 3.19.90

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.19.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 18 2016 David King <amigadave@amigadave.com> - 3.19.4-1
- Update to 3.19.4

* Mon Dec 14 2015 David King <amigadave@amigadave.com> - 3.19.3-1
- Update to 3.19.3

* Mon Nov 23 2015 David King <amigadave@amigadave.com> - 3.19.2-1
- Update to 3.19.2

* Tue Oct 27 2015 David King <amigadave@amigadave.com> - 3.19.1-1
- Update to 3.19.1

* Mon Oct 12 2015 David King <amigadave@amigadave.com> - 3.18.1-1
- Update to 3.18.1

* Mon Sep 21 2015 David King <amigadave@amigadave.com> - 3.18.0-1
- Update to 3.18.0

* Mon Sep 14 2015 David King <amigadave@amigadave.com> - 3.17.92-1
- Update to 3.17.92

* Thu Sep 03 2015 Kalev Lember <klember@redhat.com> - 3.17.91-1
- Update to 3.17.91

* Wed Aug 19 2015 Kalev Lember <klember@redhat.com> - 3.17.90-1
- Update to 3.17.90
- Use make_install macro

* Sun Jul 19 2015 David King <amigadave@amigadave.com> - 3.17.4-1
- Update to 3.17.4

* Mon Jun 22 2015 David King <amigadave@amigadave.com> - 3.17.3-1
- Update to 3.17.3

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.17.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 25 2015 David King <amigadave@amigadave.com> - 3.17.2-1
- Update to 3.17.2

* Wed May 20 2015 David King <amigadave@amigadave.com> - 3.17.1.1-1
- Update to 3.17.1.1

* Tue Apr 28 2015 David King <amigadave@amigadave.com> - 3.17.1-1
- Update to 3.17.1

* Tue Apr 14 2015 David King <amigadave@amigadave.com> - 3.16.1.1-1
- Update to 3.16.1.1

* Mon Apr 13 2015 David King <amigadave@amigadave.com> - 3.16.1-1
- Update to 3.16.1

* Tue Mar 24 2015 David King <amigadave@amigadave.com> - 3.16.0.1-1
- Update to 3.16.0.1

* Mon Mar 16 2015 David King <amigadave@amigadave.com> - 3.15.92-1
- Update to 3.15.92

* Mon Mar 02 2015 David King <amigadave@amigadave.com> - 3.15.91-1
- Update to 3.15.91
- Validate AppData and desktop file during check

* Mon Feb 16 2015 David King <amigadave@amigadave.com> - 3.15.90-1
- Update to 3.15.90
- Use license macro for COPYING

* Mon Jan 19 2015 David King <amigadave@amigadave.com> - 3.15.4-1
- Update to 3.15.4

* Thu Jan 08 2015 David King <amigadave@amigadave.com> - 3.15.3-2
- Update man page glob in files section

* Mon Dec 15 2014 David King <amigadave@amigadave.com> - 3.15.3-1
- Update to 3.15.3

* Mon Nov 24 2014 David King <amigadave@amigadave.com> - 3.15.2-1
- Update to 3.15.2

* Mon Oct 27 2014 David King <amigadave@amigadave.com> - 3.15.1-1
- Update to 3.15.1

* Mon Sep 22 2014 David King <amigadave@amigadave.com> - 3.14.0-1
- Update to 3.14.0
- Do not own the appdata directory

* Tue Sep 16 2014 David King <amigadave@amigadave.com> - 3.13.92-1
- Update to 3.13.92

* Fri Aug 29 2014 David King <amigadave@amigadave.com> - 3.13.91-1
- Update to 3.13.91

* Mon Aug 18 2014 David King <amigadave@amigadave.com> - 3.13.90-1
- Update to 3.13.90

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.13.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 22 2014 David King <amigadave@amigadave.com> - 3.13.4.2-1
- Update to 3.13.4.2

* Mon Jul 21 2014 David King <amigadave@amigadave.com> - 3.13.4-1
- Update to 3.13.4

* Mon Jun 23 2014 David King <amigadave@amigadave.com> - 3.13.3-1
- Update to 3.13.3

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.13.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 07 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.1-2
- Drop gnome-icon-theme dependency

* Tue Apr 29 2014 David King <amigadave@amigadave.com> - 3.13.1-1
- Update to 3.13.1

* Mon Mar 24 2014 David King <amigadave@amigadave.com> - 3.12.0-1
- Update to 3.12.0

* Mon Mar 17 2014 David King <amigadave@amigadave.com> - 3.11.92-1
- Update to 3.11.92

* Mon Mar 10 2014 David King <amigadave@amigadave.com> - 3.11.91-2
- Drop unnecessary sqlite3 BuildRequires

* Sun Mar 09 2014 David King <amigadave@amigadave.com> - 3.11.91-1
- Update to 3.11.91

* Sun Mar 09 2014 David King <amigadave@amigadave.com> - 3.10.2-1
- Update to 3.10.2

* Wed Sep 25 2013 Kalev Lember <kalevlember@gmail.com> - 3.10.0-1
- Update to 3.10.0
- Include the appdata file

* Sun Aug 25 2013 Kalev Lember <kalevlember@gmail.com> - 3.9.90-1
- Update to 3.9.90

* Tue Jul 30 2013 Richard Hughes <rhughes@redhat.com> - 3.8.0-2
- Rebuild for colord soname bump

* Wed Mar 27 2013 Kalev Lember <kalevlember@gmail.com> - 3.8.0-1
- Update to 3.8.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 21 2013 Adam Tkac <atkac redhat com> - 3.6.0-3
- rebuild due to "jpeg8-ABI" feature drop

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 3.6.0-2
- rebuild against new libjpeg

* Wed Sep 26 2012 Matthias Clasen <mclasen@redhat.com> - 3.6.0-1
- Update to 3.6.0

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri May 11 2012 Matthias Clasen <mclasen@redhat.com> - 3.4.1-1
- Update to 3.4.1
- Fixes 820971

* Wed Mar 28 2012 Richard Hughes <rhughes@redhat.com> - 3.4.0-1
- Update to 3.4.0

* Wed Mar 21 2012 Richard Hughes <rhughes@redhat.com> - 3.3.92-1
- Update to 3.3.92

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Nov 24 2011 Tomas Bzatek <tbzatek@redhat.com> - 3.2.1-1
- Update to 3.2.1

* Fri Sep 30 2011 Kalev Lember <kalevlember@gmail.com> - 3.2.0-2
- Fix postun scriplet syntax error

* Wed Sep 28 2011 Ray <rstrode@redhat.com> - 3.2.0-1
- Update to 3.2.0

* Tue Sep 20 2011 Matthias Clasen <mclasen@redhat.com> - 3.1.91-1
- Update to 3.1.91

* Mon Jul 25 2011 Matthias Clasen <mclasen@redhat.com> - 3.1.3-1
- Update to 3.1.3

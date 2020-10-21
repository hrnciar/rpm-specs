%global _changelog_trimtime %(date +%s -d "1 year ago")

%define gtk3_version 3.22.0
%define glib2_version 2.53.4
%define gnome_desktop_version 2.91.2
%define libexif_version 0.6.14

Name:    eog
Version: 3.38.0
Release: 1%{?dist}
Summary: Eye of GNOME image viewer

# The GFDL has an "or later version" clause embedded inside the license.
# There is no need to add the + here.
License: GPLv2+ and GFDL
URL:     https://wiki.gnome.org/Apps/EyeOfGnome
Source0: https://download.gnome.org/sources/%{name}/3.38/%{name}-%{version}.tar.xz

BuildRequires: pkgconfig(exempi-2.0)
BuildRequires: pkgconfig(gdk-pixbuf-2.0)
BuildRequires: pkgconfig(glib-2.0) >= %{glib2_version}
BuildRequires: pkgconfig(gnome-desktop-3.0) >= %{gnome_desktop_version}
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: pkgconfig(gsettings-desktop-schemas)
BuildRequires: pkgconfig(gtk+-3.0) >= %{gtk3_version}
BuildRequires: pkgconfig(lcms2)
BuildRequires: pkgconfig(libexif) >= %{libexif_version}
BuildRequires: pkgconfig(libpeas-1.0) >= 0.7.4
BuildRequires: pkgconfig(libpeas-gtk-1.0) >= 0.7.4
BuildRequires: pkgconfig(libportal)
BuildRequires: pkgconfig(librsvg-2.0)
BuildRequires: pkgconfig(shared-mime-info)
BuildRequires: pkgconfig(x11)
BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: gtk-doc
BuildRequires: itstool
BuildRequires: libjpeg-devel
BuildRequires: meson
BuildRequires: zlib-devel
BuildRequires: /usr/bin/appstream-util

Requires:      gsettings-desktop-schemas
Requires:      glib2%{?_isa} >= %{glib2_version}
Requires:      gtk3%{?_isa} >= %{gtk3_version}

%description
The Eye of GNOME image viewer (eog) is the official image viewer for the
GNOME desktop. It can view single image files in a variety of formats, as
well as large image collections.

eog is extensible through a plugin system.

%package devel
Summary: Support for developing plugins for the eog image viewer
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The Eye of GNOME image viewer (eog) is the official image viewer for the
GNOME desktop. This package allows you to develop plugins that add new
functionality to eog.

%package  tests
Summary:  Tests for the %{name} package
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: python3-behave
Requires: python3-dogtail

%description tests
The %{name}-tests package contains tests that can be used to verify
the functionality of the installed %{name} package.

%prep
%setup -q

%build
%meson -Dgtk_doc=true -Dinstalled_tests=true
%meson_build

%install
%meson_install

%find_lang %{name} --with-gnome

%check
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/*.appdata.xml
desktop-file-validate %{buildroot}/%{_datadir}/applications/org.gnome.eog.desktop

%files -f %{name}.lang
%doc AUTHORS NEWS README
%license COPYING
%{_datadir}/eog
%{_datadir}/applications/org.gnome.eog.desktop
%{_datadir}/icons/hicolor/*/apps/*
%{_bindir}/*
%{_libdir}/eog
%{_datadir}/GConf/gsettings/eog.convert
%{_datadir}/glib-2.0/schemas/org.gnome.eog.enums.xml
%{_datadir}/glib-2.0/schemas/org.gnome.eog.gschema.xml
%{_datadir}/metainfo/eog.appdata.xml

%files devel
%{_includedir}/eog-3.0
%{_libdir}/pkgconfig/eog.pc
%{_datadir}/gtk-doc/

%files tests
%dir %{_libexecdir}/eog
%{_libexecdir}/eog/installed-tests/
%{_datadir}/installed-tests/

%changelog
* Sat Sep 12 2020 Kalev Lember <klember@redhat.com> - 3.38.0-1
- Update to 3.38.0

* Sun Sep 06 2020 Kalev Lember <klember@redhat.com> - 3.37.92-1
- Update to 3.37.92

* Mon Aug 17 2020 Kalev Lember <klember@redhat.com> - 3.37.90-1
- Update to 3.37.90

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.37.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Apr 30 2020 Kalev Lember <klember@redhat.com> - 3.37.1-1
- Update to 3.37.1

* Sat Apr 25 2020 Kalev Lember <klember@redhat.com> - 3.36.2-1
- Update to 3.36.2

* Tue Apr 14 2020 Felipe Borges <feborges@redhat.com> - 3.36.1-3
- Also use Portals for the right-click "Open with" option

* Fri Apr 03 2020 Felipe Borges <feborges@redhat.com> - 3.36.1-2
- Use Portals for "open with"

* Sun Mar 29 2020 Kalev Lember <klember@redhat.com> - 3.36.1-1
- Update to 3.36.1

* Sun Mar 08 2020 Kalev Lember <klember@redhat.com> - 3.36.0-1
- Update to 3.36.0

* Mon Mar 02 2020 Kalev Lember <klember@redhat.com> - 3.35.92-1
- Update to 3.35.92

* Mon Feb 17 2020 Kalev Lember <klember@redhat.com> - 3.35.91-1
- Update to 3.35.91

* Sun Feb 02 2020 Kalev Lember <klember@redhat.com> - 3.35.3-1
- Update to 3.35.3

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.35.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 20 2020 Kalev Lember <klember@redhat.com> - 3.35.2-1
- Update to 3.35.2

* Thu Jan 16 2020 Kalev Lember <klember@redhat.com> - 3.35.1-2
- Rebuilt for libgnome-desktop soname bump

* Mon Dec 02 2019 Kalev Lember <klember@redhat.com> - 3.35.1-1
- Update to 3.35.1

* Mon Oct 07 2019 Kalev Lember <klember@redhat.com> - 3.34.1-1
- Update to 3.34.1

* Wed Sep 11 2019 Kalev Lember <klember@redhat.com> - 3.34.0-2
- Change -tests subpackage to depend on python3 instead of python2

* Mon Sep 09 2019 Kalev Lember <klember@redhat.com> - 3.34.0-1
- Update to 3.34.0

* Fri Sep 06 2019 Nikola Forró <nforro@redhat.com> - 3.33.91-3
- Rebuilt for exempi 2.5.1

* Tue Aug 20 2019 Kalev Lember <klember@redhat.com> - 3.33.91-2
- Rebuild

* Tue Aug 20 2019 Kalev Lember <klember@redhat.com> - 3.33.91-1
- Update to 3.33.91

* Tue Aug 06 2019 Phil Wyett <philwyett@kathenas.org> - 3.33.90-1
- Update to 3.33.90.

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.33.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jul 21 2019 Kalev Lember <klember@redhat.com> - 3.33.3-2
- Rebuilt for libgnome-desktop soname bump

* Mon Jul 15 2019 Kalev Lember <klember@redhat.com> - 3.33.3-1
- Update to 3.33.3

* Tue Jun 18 2019 Kalev Lember <klember@redhat.com> - 3.33.2-1
- Update to 3.33.2

* Tue May 21 2019 Kalev Lember <klember@redhat.com> - 3.33.1-1
- Update to 3.33.1

* Tue May 21 2019 Kalev Lember <klember@redhat.com> - 3.32.2-1
- Update to 3.32.2

* Tue Apr 16 2019 Adam Williamson <awilliam@redhat.com> - 3.32.1-2
- Rebuild with Meson fix for #1699099

* Mon Apr 08 2019 Kalev Lember <klember@redhat.com> - 3.32.1-1
- Update to 3.32.1

* Mon Mar 11 2019 Kalev Lember <klember@redhat.com> - 3.32.0-1
- Update to 3.32.0

* Mon Mar 04 2019 Kalev Lember <klember@redhat.com> - 3.31.91-1
- Update to 3.31.91

* Mon Feb 04 2019 Phil Wyett <philwyett@kathenas.org> - 3.31.90-1
- Update to 3.31.90

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.31.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 07 2019 Kalev Lember <klember@redhat.com> - 3.31.3-1
- Update to 3.31.3

* Wed Sep 26 2018 Kalev Lember <klember@redhat.com> - 3.28.4-1
- Update to 3.28.4

* Wed Jul 25 2018 Kalev Lember <klember@redhat.com> - 3.28.3-1
- Update to 3.28.3

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.28.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue May 08 2018 Kalev Lember <klember@redhat.com> - 3.28.2-1
- Update to 3.28.2

* Fri Apr 13 2018 Kalev Lember <klember@redhat.com> - 3.28.1-2
- Fix -test subpackage deps

* Mon Apr 09 2018 Kalev Lember <klember@redhat.com> - 3.28.1-1
- Update to 3.28.1

* Mon Mar 12 2018 Kalev Lember <klember@redhat.com> - 3.28.0-1
- Update to 3.28.0

* Mon Mar 05 2018 Kalev Lember <klember@redhat.com> - 3.27.91-1
- Update to 3.27.91
- Switch to the meson build system

* Tue Feb 13 2018 Björn Esser <besser82@fedoraproject.org> - 3.26.2-4
- Rebuild against newer gnome-desktop3 package

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.26.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 05 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.26.2-2
- Remove obsolete scriptlets

* Thu Nov 09 2017 Kalev Lember <klember@redhat.com> - 3.26.2-1
- Update to 3.26.2

* Sun Oct 08 2017 Kalev Lember <klember@redhat.com> - 3.26.1-1
- Update to 3.26.1

* Wed Sep 13 2017 Kalev Lember <klember@redhat.com> - 3.26.0-1
- Update to 3.26.0

* Thu Sep 07 2017 Kalev Lember <klember@redhat.com> - 3.25.92-1
- Update to 3.25.92

* Tue Aug 15 2017 Kalev Lember <klember@redhat.com> - 3.25.90-1
- Update to 3.25.90

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.25.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.25.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 25 2017 Kalev Lember <klember@redhat.com> - 3.25.1-1
- Update to 3.25.1

* Tue Apr 11 2017 Kalev Lember <klember@redhat.com> - 3.24.1-1
- Update to 3.24.1

* Tue Mar 21 2017 Kalev Lember <klember@redhat.com> - 3.24.0-1
- Update to 3.24.0

* Thu Mar 16 2017 Kalev Lember <klember@redhat.com> - 3.23.92-1
- Update to 3.23.92

* Tue Feb 28 2017 Richard Hughes <rhughes@redhat.com> - 3.23.91-1
- Update to 3.23.91

* Tue Feb 14 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.23.90-1
- Update to 3.23.90

* Mon Feb 13 2017 Richard Hughes <rhughes@redhat.com> - 3.23.1-1
- Update to 3.23.1

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.20.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Oct 12 2016 Kalev Lember <klember@redhat.com> - 3.20.5-1
- Update to 3.20.5
- Don't set group tags
- Use upstream screenshots for appdata

* Sun Aug 21 2016 Kalev Lember <klember@redhat.com> - 3.20.4-1
- Update to 3.20.4

* Tue Jun 21 2016 David King <amigadave@amigadave.com> - 3.20.3-1
- Update to 3.20.3

* Tue May 10 2016 Kalev Lember <klember@redhat.com> - 3.20.2-1
- Update to 3.20.2

* Wed Apr 13 2016 Kalev Lember <klember@redhat.com> - 3.20.1-1
- Update to 3.20.1

* Fri Apr 08 2016 Debarshi Ray <rishi@fedoraproject.org> - 3.20.0-2
- Prevent a crash when queueing a new draw (GNOME #665897)

* Tue Mar 22 2016 Kalev Lember <klember@redhat.com> - 3.20.0-1
- Update to 3.20.0

* Tue Mar 15 2016 Richard Hughes <rhughes@redhat.com> - 3.19.92-1
- Update to 3.19.92

* Tue Mar 01 2016 Richard Hughes <rhughes@redhat.com> - 3.19.91-1
- Update to 3.19.91

* Tue Feb 16 2016 David King <amigadave@amigadave.com> - 3.19.90-1
- Update to 3.19.90

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.19.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 19 2016 David King <amigadave@amigadave.com> - 3.19.4-1
- Update to 3.19.4

* Mon Dec 14 2015 Kalev Lember <klember@redhat.com> - 3.19.3-1
- Update to 3.19.3

* Tue Nov 24 2015 Kalev Lember <klember@redhat.com> - 3.19.2-1
- Update to 3.19.2

* Tue Nov 10 2015 Kalev Lember <klember@redhat.com> - 3.18.1-1
- Update to 3.18.1

* Mon Sep 28 2015 Kalev Lember <klember@redhat.com> - 3.18.0-1
- Update to 3.18.0

* Mon Sep 14 2015 Kalev Lember <klember@redhat.com> - 3.17.92-1
- Update to 3.17.92

* Mon Aug 31 2015 Kalev Lember <klember@redhat.com> - 3.17.91-1
- Update to 3.17.91

* Mon Aug 17 2015 Kalev Lember <klember@redhat.com> - 3.17.90-1
- Update to 3.17.90
- Use make_install macro

* Tue Jul 21 2015 David King <amigadave@amigadave.com> - 3.17.3-2
- Bump for new gnome-desktop3

* Mon Jul 20 2015 David King <amigadave@amigadave.com> - 3.17.3-1
- Update to 3.17.3
- Preserve timestamps during install

* Mon Jun 22 2015 David King <amigadave@amigadave.com> - 3.17.2-1
- Update to 3.17.2

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.17.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue May 26 2015 David King <amigadave@amigadave.com> - 3.17.1-1
- Update to 3.17.1

* Wed May 13 2015 Kalev Lember <kalevlember@gmail.com> - 3.16.2-1
- Update to 3.16.2

* Tue May 12 2015 Michael Catanzaro <mcatanzaro@gnome.org> - 3.16.1-2
- Add symbolic icon

* Tue Apr 14 2015 Kalev Lember <kalevlember@gmail.com> - 3.16.1-1
- Update to 3.16.1

* Mon Mar 30 2015 Richard Hughes <rhughes@redhat.com> - 3.16.0-2
- Use better AppData screenshots

* Mon Mar 23 2015 Kalev Lember <kalevlember@gmail.com> - 3.16.0-1
- Update to 3.16.0

* Tue Mar 17 2015 Kalev Lember <kalevlember@gmail.com> - 3.15.92-1
- Update to 3.15.92

* Tue Feb 17 2015 David King <amigadave@amigadave.com> - 3.15.90-1
- Update to 3.15.90

* Mon Feb 02 2015 David King <amigadave@amigadave.com> - 3.15.1-1
- Update to 3.15.1
- Use pkgconfig for BuildRequires
- Update desktop file validation checks
- Use license macro for COPYING
- Update URL
- Validate AppData in check

* Thu Nov 20 2014 Kalev Lember <kalevlember@gmail.com> - 3.14.3-1
- Update to 3.14.3

* Wed Nov 12 2014 Vadim Rutkovsky <vrutkovs@redhat.com> - 3.14.2-2
- Build installed tests

* Mon Nov 10 2014 Kalev Lember <kalevlember@gmail.com> - 3.14.2-1
- Update to 3.14.2

* Mon Oct 13 2014 Kalev Lember <kalevlember@gmail.com> - 3.14.1-1
- Update to 3.14.1

* Mon Sep 22 2014 Kalev Lember <kalevlember@gmail.com> - 3.14.0-1
- Update to 3.14.0

* Tue Sep 16 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.92-1
- Update to 3.13.92
- Tighten -devel subpackage deps

* Tue Aug 19 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.90-1
- Update to 3.13.90

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.13.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 22 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.3-2
- Rebuilt for gobject-introspection 1.41.4

* Tue Jul 22 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.3-1
- Update to 3.13.3

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.13.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.2-1
- Update to 3.13.2

* Tue Apr 29 2014 Richard Hughes <rhughes@redhat.com> - 3.13.1-1
- Update to 3.13.1

* Tue Apr 15 2014 Kalev Lember <kalevlember@gmail.com> - 3.12.1-1
- Update to 3.12.1

* Mon Mar 24 2014 Kalev Lember <kalevlember@gmail.com> - 3.12.0-1
- Update to 3.12.0

* Tue Mar 18 2014 Richard Hughes <rhughes@redhat.com> - 3.11.92-1
- Update to 3.11.92

* Wed Mar 05 2014 Richard Hughes <rhughes@redhat.com> - 3.11.91-1
- Update to 3.11.91

* Wed Feb 19 2014 Richard Hughes <rhughes@redhat.com> - 3.11.90-2
- Rebuilt for gnome-desktop soname bump

* Tue Feb 18 2014 Richard Hughes <rhughes@redhat.com> - 3.11.90-1
- Update to 3.11.90

* Tue Jan 14 2014 Richard Hughes <rhughes@redhat.com> - 3.11.4-1
- Update to 3.11.4

* Tue Dec 17 2013 Richard Hughes <rhughes@redhat.com> - 3.11.3-1
- Update to 3.11.3

* Tue Nov 19 2013 Richard Hughes <rhughes@redhat.com> - 3.11.2-1
- Update to 3.11.2

* Wed Oct 30 2013 Richard Hughes <rhughes@redhat.com> - 3.11.1-1
- Update to 3.11.1

* Mon Oct 28 2013 Richard Hughes <rhughes@redhat.com> - 3.10.1-1
- Update to 3.10.1

* Wed Sep 25 2013 Kalev Lember <kalevlember@gmail.com> - 3.10.0-1
- Update to 3.10.0

* Wed Sep 18 2013 Kalev Lember <kalevlember@gmail.com> - 3.9.92-1
- Update to 3.9.92

* Tue Sep 03 2013 Kalev Lember <kalevlember@gmail.com> - 3.9.91-2
- Rebuilt for libgnome-desktop soname bump

* Tue Sep 03 2013 Kalev Lember <kalevlember@gmail.com> - 3.9.91-1
- Update to 3.9.91

* Sat Aug 10 2013 Kalev Lember <kalevlember@gmail.com> - 3.9.5-1
- Update to 3.9.5

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jun 22 2013 Matthias Clasen <mclasen@redhat.com> - 3.9.1-2
- Trim %%changelog

* Thu Jun 20 2013 Kalev Lember <kalevlember@gmail.com> - 3.9.1-1
- Update to 3.9.1
- Adapt for gnome-icon-theme packaging changes

* Tue May 14 2013 Richard Hughes <rhughes@redhat.com> - 3.8.2-1
- Update to 3.8.2

* Tue Mar 26 2013 Kalev Lember <kalevlember@gmail.com> - 3.8.0-1
- Update to 3.8.0

* Wed Mar 20 2013 Richard Hughes <rhughes@redhat.com> - 3.7.92-1
- Update to 3.7.92

* Fri Mar  8 2013 Matthias Clasen <mclasen@redhat.com> - 3.7.91-1
- Update to 3.7.91

* Thu Feb 21 2013 Kalev Lember <kalevlember@gmail.com> - 3.7.4-5
- Drop the desktop file vendor prefix

* Wed Feb 20 2013 Kalev Lember <kalevlember@gmail.com> - 3.7.4-4
- Rebuilt for libgnome-desktop soname bump

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 18 2013 Adam Tkac <atkac redhat com> - 3.7.4-2
- rebuild due to "jpeg8-ABI" feature drop

* Wed Jan 16 2013 Richard Hughes <hughsient@gmail.com> - 3.7.4-1
- Update to 3.7.4

* Fri Dec 21 2012 Kalev Lember <kalevlember@gmail.com> - 3.7.2-2
- Rebuilt for libgnome-desktop-3 3.7.3 soname bump

* Wed Nov 21 2012 Richard Hughes <hughsient@gmail.com> - 3.7.2-1
- Update to 3.7.2

* Fri Nov 09 2012 Kalev Lember <kalevlember@gmail.com> - 3.7.1-1
- Update to 3.7.1

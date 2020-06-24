Name:           gnome-dictionary
Version:        3.26.1
Release:        6%{?dist}
Summary:        A dictionary application for GNOME

License:        GPLv3+ and LGPLv2+ and GFDL
URL:            https://wiki.gnome.org/Apps/Dictionary
Source0:        https://download.gnome.org/sources/%{name}/3.26/%{name}-%{version}.tar.xz

BuildRequires:  desktop-file-utils
BuildRequires:  docbook-style-xsl
BuildRequires:  gettext
BuildRequires:  itstool
BuildRequires:  meson
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  /usr/bin/appstream-util
BuildRequires:  /usr/bin/xsltproc

Obsoletes: gnome-utils <= 1:3.3
Obsoletes: gnome-utils-libs <= 1:3.3
Obsoletes: gnome-utils-devel <= 1:3.3
# Removed in F27
Obsoletes: gnome-dictionary-devel < 3.26.0
Obsoletes: gnome-dictionary-libs < 3.26.0

%description
gnome-dictionary lets you look up words in dictionary sources.

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name} --with-gnome

%check
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_datadir}/appdata/*.appdata.xml
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/*.desktop

%files -f %{name}.lang
%doc NEWS README.md
%license COPYING COPYING.docs COPYING.libs
%{_bindir}/gnome-dictionary
%{_datadir}/appdata/org.gnome.Dictionary.appdata.xml
%{_datadir}/applications/org.gnome.Dictionary.desktop
%{_datadir}/dbus-1/services/org.gnome.Dictionary.service
%{_datadir}/gdict-1.0/
%{_datadir}/glib-2.0/schemas/org.gnome.dictionary.gschema.xml
%{_mandir}/man1/gnome-dictionary.1*

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.26.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.26.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.26.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.26.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.26.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Oct 08 2017 Kalev Lember <klember@redhat.com> - 3.26.1-1
- Update to 3.26.1

* Thu Sep 14 2017 Kalev Lember <klember@redhat.com> - 3.26.0-1
- Update to 3.26.0
- Switch to the meson build system
- Drop -libs and -devel subpackages now that the shared lib is gone

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.24.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.24.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Mar 21 2017 Kalev Lember <klember@redhat.com> - 3.24.0-1
- Update to 3.24.0

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.20.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Mar 22 2016 Kalev Lember <klember@redhat.com> - 3.20.0-1
- Update to 3.20.0

* Wed Mar 02 2016 Richard Hughes <rhughes@redhat.com> - 3.19.91-1
- Update to 3.19.91

* Tue Feb 16 2016 Richard Hughes <rhughes@redhat.com> - 3.19.90-1
- Update to 3.19.90

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.19.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 25 2016 Kalev Lember <klember@redhat.com> - 3.19.0-1
- Update to 3.19.0

* Wed Jan 20 2016 Kalev Lember <klember@redhat.com> - 3.18.1-1
- Update to 3.18.1

* Mon Sep 21 2015 Kalev Lember <klember@redhat.com> - 3.18.0-1
- Update to 3.18.0

* Thu Aug 20 2015 Kalev Lember <klember@redhat.com> - 3.17.90-2
- Split out -libs subpackage

* Tue Aug 18 2015 Kalev Lember <klember@redhat.com> - 3.17.90-1
- Update to 3.17.90
- Use make_install macro

* Mon Jul 20 2015 David King <amigadave@amigadave.com> - 3.17.4-1
- Update to 3.17.4

* Wed Jun 24 2015 David King <amigadave@amigadave.com> - 3.17.3-1
- Update to 3.17.3
- Update URL
- Preserve timestamps during install

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.17.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun May 31 2015 Kalev Lember <kalevlember@gmail.com> - 3.17.2-1
- Update to 3.17.2

* Fri May 01 2015 Kalev Lember <kalevlember@gmail.com> - 3.17.1-1
- Update to 3.17.1

* Tue Apr 14 2015 Kalev Lember <kalevlember@gmail.com> - 3.16.1-1
- Update to 3.16.1

* Mon Mar 23 2015 Kalev Lember <kalevlember@gmail.com> - 3.16.0-1
- Update to 3.16.0

* Sun Mar 15 2015 Kalev Lember <kalevlember@gmail.com> - 3.15.92-1
- Update to 3.15.92

* Tue Mar 03 2015 Kalev Lember <kalevlember@gmail.com> - 3.15.91-1
- Update to 3.15.91

* Tue Feb 17 2015 David King <amigadave@amigadave.com> - 3.15.90-1
- Update to 3.15.90
- Use license macro for COPYING, COPYING.docs and COPYING.libs
- Update man page glob in files section
- Use pkgconfig for BuildRequires
- Validate AppData in check

* Mon Nov 10 2014 Kalev Lember <kalevlember@gmail.com> - 3.14.2-1
- Update to 3.14.2

* Mon Oct 13 2014 Kalev Lember <kalevlember@gmail.com> - 3.14.1-1
- Update to 3.14.1

* Tue Sep 23 2014 Kalev Lember <kalevlember@gmail.com> - 3.14.0-1
- Update to 3.14.0

* Thu Sep 18 2014 Richard Hughes <rhughes@redhat.com> - 3.13.92-1
- Update to 3.13.92

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Oct 28 2013 Richard Hughes <rhughes@redhat.com> - 3.10.0-1
- Update to 3.10.0

* Thu Aug 22 2013 Kalev Lember <kalevlember@gmail.com> - 3.9.0-1
- Update to 3.9.0

* Sat Aug 10 2013 Kalev Lember <kalevlember@gmail.com> - 3.8.0-1
- Update to 3.8.0

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Sep 25 2012 Richard Hughes <hughsient@gmail.com> - 3.6.0-1
- Update to 3.6.0

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 07 2012 Richard Hughes <hughsient@gmail.com> - 3.5.2-1
- Update to 3.5.2

* Tue Apr 24 2012 Kalev Lember <kalevlember@gmail.com> - 3.4.0-2
- Silence rpm scriptlet output

* Tue Mar 27 2012 Kalev Lember <kalevlember@gmail.com> - 3.4.0-1
- Update to 3.4.0

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Nov 10 2011 Matthias Clasen <mclasen@redhat.com> - 3.3.2-2
- Obsolete all gnome-utils subpackages, and handle the epoch

* Thu Nov 10 2011 Matthias Clasen <mclasen@redhat.com> - 3.3.2-1
- Initial packaging

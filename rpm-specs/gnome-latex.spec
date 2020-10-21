Name:           gnome-latex
Version:        3.38.0
Release:        1%{?dist}
Summary:        Integrated LaTeX Environment for the GNOME desktop

License:        GPLv3+
URL:            https://wiki.gnome.org/Apps/GNOME-LaTeX
Source0:        https://download.gnome.org/sources/%{name}/3.38/%{name}-%{version}.tar.xz

BuildRequires:  amtk-devel
BuildRequires:  dconf-devel
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  glib2-devel
BuildRequires:  gsettings-desktop-schemas-devel
BuildRequires:  gspell-devel
BuildRequires:  gtk3-devel
BuildRequires:  gtksourceview4-devel
BuildRequires:  intltool
BuildRequires:  itstool
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  tepl-devel
BuildRequires:  vala
BuildRequires:  /usr/bin/appstream-util
BuildRequires:  /usr/bin/desktop-file-validate

Requires:       gsettings-desktop-schemas
Requires:       hicolor-icon-theme
Requires:       latexmk

# Renamed in Fedora 30
Obsoletes:      latexila < 3.28
Provides:       latexila = %{version}-%{release}

%description
GNOME LaTeX is a LaTeX editor for the GNOME desktop, previously named
LaTeXila. GNOME LaTeX permits to concentrate on the content and the
structure of the document instead of being distracted by its
presentation.

To help the writing of the LaTeX markup, auto-completion is available as
well as menus and toolbars with the principal commands. New documents are
created from templates. There are buttons to compile, convert and view a
document in one click. And projects containing several .tex files are
managed easily.

A side panel contains three components: the document structure to easily
navigate in it; lists of symbols to insert them in a document; and a file
browser.

GNOME LaTeX has also other features like the spell-checking, or jumping
to the associated position between the .tex file and the PDF.

%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
# Renamed in Fedora 30
Obsoletes:      latexila-doc < 3.28

%description    doc
This package contains documentation for %{name}.

%prep
%autosetup -p1

%build
%configure
%make_build V=1

%install
%make_install
%find_lang %{name} --with-gnome

%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/org.gnome.gnome-latex.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.gnome-latex.desktop

%files -f %{name}.lang
%license COPYING
%doc AUTHORS README NEWS HACKING
%{_bindir}/gnome-latex
%{_datadir}/applications/org.gnome.gnome-latex.desktop
%{_datadir}/dbus-1/services/org.gnome.gnome-latex.service
%{_datadir}/glib-2.0/schemas/org.gnome.gnome-latex.gschema.xml
%{_datadir}/gnome-latex/
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.gnome-latex.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.gnome-latex-symbolic.svg
%{_datadir}/metainfo/org.gnome.gnome-latex.appdata.xml
%{_mandir}/man1/gnome-latex.1*

%files doc
%{_datadir}/gtk-doc/

%changelog
* Fri Sep 11 2020 Kalev Lember <klember@redhat.com> - 3.38.0-1
- Update to 3.38.0

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.37.2-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.37.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 29 2020 Kalev Lember <klember@redhat.com> - 3.37.2-1
- Update to 3.37.2

* Tue Mar 31 2020 Kalev Lember <klember@redhat.com> - 3.36.0-1
- Update to 3.36.0

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.32.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.32.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Mar 14 2019 Pete Walter <pwalter@fedoraproject.org> - 3.32.0-2
- Validate appstream data
- Add missing dconf-devel BuildRequires

* Wed Mar 13 2019 Pete Walter <pwalter@fedoraproject.org> - 3.32.0-1
- Update the packaging for latexila to gnome-latex rename (#1688309)

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.26.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.26.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Mar 11 2018 Kalev Lember <klember@redhat.com> - 3.26.1-4
- Rebuilt for gspell 1.8

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.26.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 05 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.26.1-2
- Remove obsolete scriptlets

* Tue Oct 31 2017 Kalev Lember <klember@redhat.com> - 3.26.1-1
- Update to 3.26.1

* Mon Aug 21 2017 Kalev Lember <klember@redhat.com> - 3.24.3-1
- Update to 3.24.3

* Fri Aug 11 2017 Kalev Lember <klember@redhat.com> - 3.24.2-1
- Update to 3.24.2

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.23.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.23.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Mar 17 2017 Richard Hughes <rhughes@redhat.com> - 3.23.2-1
- Update to 3.23.2

* Mon Feb 13 2017 Richard Hughes <rhughes@redhat.com> - 3.23.1-1
- Update to 3.23.1

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Dec 18 2016 Kalev Lember <klember@redhat.com> - 3.22.1-1
- Update to 3.22.1
- Use https source URL

* Mon Sep 19 2016 Kalev Lember <klember@redhat.com> - 3.22.0-1
- Update to 3.22.0
- Don't set group tags

* Mon Aug 01 2016 Kalev Lember <klember@redhat.com> - 3.20.1-1
- Update to 3.20.1

* Sun Mar 20 2016 Kalev Lember <klember@redhat.com> - 3.20.0-1
- Update to 3.20.0

* Mon Mar 14 2016 Kalev Lember <klember@redhat.com> - 3.19.5-1
- Update to 3.19.5

* Tue Feb 16 2016 Richard Hughes <rhughes@redhat.com> - 3.19.4-1
- Update to 3.19.4

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.19.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 20 2016 Kalev Lember <klember@redhat.com> - 3.19.3-1
- Update to 3.19.3

* Mon Dec 14 2015 Kalev Lember <klember@redhat.com> - 3.19.2-1
- Update to 3.19.2

* Mon Dec 07 2015 Kalev Lember <klember@redhat.com> - 3.19.1-1
- Update to 3.19.1

* Wed Aug 19 2015 Kalev Lember <klember@redhat.com> - 3.17.0-1
- Update to 3.17.0

* Tue Aug 18 2015 Kalev Lember <klember@redhat.com> - 3.16.2-1
- Update to 3.16.2
- Use make_install macro

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.16.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Apr 19 2015 Kalev Lember <kalevlember@gmail.com> - 3.16.1-1
- Update to 3.16.1
- Use license macro for the COPYING file

* Sun Feb 22 2015 Kalev Lember <kalevlember@gmail.com> - 3.15.2-1
- Update to 3.15.2
- Add -doc subpackage

* Wed Oct 01 2014 Kalev Lember <kalevlember@gmail.com> - 3.14.1-1
- Update to 3.14.1

* Mon Sep 22 2014 Kalev Lember <kalevlember@gmail.com> - 3.14.0-1
- Update to 3.14.0

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.12.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun May 11 2014 Kalev Lember <kalevlember@gmail.com> - 2.12.1-1
- Update to 2.12.1

* Mon Nov 25 2013 Kalev Lember <kalevlember@gmail.com> - 2.10.0-1
- Update to 2.10.0

* Wed Sep 04 2013 Kalev Lember <kalevlember@gmail.com> - 2.8.3-1
- Update to 2.8.3

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 07 2013 Kalev Lember <kalevlember@gmail.com> - 2.8.2-1
- Update to 2.8.2

* Mon May 13 2013 Kalev Lember <kalevlember@gmail.com> - 2.8.1-1
- Update to 2.8.1

* Thu Mar 28 2013 Kalev Lember <kalevlember@gmail.com> - 2.8.0-1
- Update to 2.8.0

* Tue Mar 26 2013 Kalev Lember <kalevlember@gmail.com> - 2.6.2-3
- Rebuilt for gtksourceview3 soname bump

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Nov 24 2012 Kalev Lember <kalevlember@gmail.com> - 2.6.2-1
- Update to 2.6.2

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Apr 8 2012 Thibault North <tnorth@fedoraproject.org> - 2.4.0-1
- Update to 2.4.0

* Wed Mar 28 2012 Thibault North <tnorth@fedoraproject.org> - 2.3.1-2
- Fix libgee require

* Mon Mar 5 2012 Thibault North <tnorth@fedoraproject.org> - 2.3.1-1
- Update to 2.3.1

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jan 3 2012 Thibault North <tnorth@fedoraproject.org> - 2.3.0-1
- Update to 2.3.0

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 2.2.2-2
- Rebuild for new libpng

* Sat Oct 15 2011 Thibault North <tnorth@fedoraproject.org> - 2.2.2-1
- Update to 2.2.2

* Sat Aug 27 2011 Thibault North <tnorth@fedoraproject.org> - 2.2.0-1
- Update to 2.2.0

* Tue Jul 12 2011 Thibault North <tnorth@fedoraproject.org> - 2.0.8-1
- Update to 2.0.8

* Thu Apr 7 2011 Thibault North <tnorth@fedoraproject.org> - 2.0.7-1
- Update to 2.0.7

* Sun Mar 20 2011 Thibault North <tnorth@fedoraproject.org> - 2.0.6-1
- Update to 2.0.6

* Tue Feb 15 2011 Thibault North <tnorth@fedoraproject.org> - 2.0.5-1
- Update to 2.0.5, thanks Sébastien Wilmet

* Thu Nov 25 2010 Thibault North <tnorth@fedoraproject.org> - 2.0.1-4
- A few more fixes

* Mon Nov 22 2010 Thibault North <tnorth@fedoraproject.org> - 2.0.1-3
- Use %%find_lang, fixes by Mohamed El Morabity

* Sun Nov 21 2010 Thibault North <tnorth@fedoraproject.org> - 2.0.1-2
- Small fixes

* Sun Nov 21 2010 Sébastien Wilmet <sebastien.wilmet@gmail.com> - 2.0.1-1
- Release 2.0.1

* Sun Nov 14 2010 Thibault North <tnorth@fedoraproject.org> - 2.0.0-1
- Release 2.0

* Mon Mar 1 2010 Sébastien Wilmet <sebastien.wilmet@gmail.com> - 0.2-1
- New upstream release
- Icons support

* Fri Dec 25 2009 Sébastien Wilmet <sebastien.wilmet@gmail.com> - 0.1-1
- Initial package for Fedora

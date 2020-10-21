%{?!_icondir:%define _icondir   %{_datadir}/icons}

Name:       electronics-menu
Version:    1.0
Release:    24%{?dist}
Summary:    Electronics Menu for the Desktop
Summary(fr): Menu « Électronique » pour le bureau

License:    GPLv2

URL:        http://geda.seul.org/
Source0:    http://geda.seul.org/dist/%{name}-%{version}.tar.gz
# Created by Chitlesh
Source1:    electronics-menu-1.0-submenu.tar.bz2

Patch0:     electronics-menu-1.0-submenus.patch
Patch1:     electronics-menu-1.0-makefile.patch
Patch2:     electronics-menu-1.0-typo.patch
Patch3:     electronics-menu-1.0-submenus-fr.patch
Patch4:     electronics-menu-1.0-submenus-qucs.patch


Requires(pre): gtk2

BuildArchitectures: noarch

%description
The programs from the category Electronics are normally located
in the Edutainment directory.
This Package adds a Electronics menu to the xdg menu structure.

%{name} is listed among Fedora Electronic Lab (FEL) packages.

%description -l fr
Les programmes de la catégorie Électronique sont normalement situés
dans la catégorie Éducation.
Ce paquetage ajoute le menu Électronique à la structure de menus xdg.

%{name} fait partie des paquetages de Fedora Electronic Lab (FEL).

%prep
%setup -q -a 1

%patch0 -p0 -b .submenus
%patch1 -p0 -b .submenus
%patch2 -p0 -b .typo
%patch3 -p0 -b .french
%patch4 -p0 -b .qucs

# allowing timestamps
sed -i 's|install|install -p|g' Makefile

# Fedora Specific Vendor
sed -i 's|<Filename>fedora-|<Filename>|' electronics.menu


%build


%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}

%files
%doc COPYING README
%{_icondir}/hicolor/??x??/categories/applications-electronics*.png
%{_icondir}/hicolor/scalable/categories/applications-electronics*.svg
%config(noreplace) %{_sysconfdir}/xdg/menus/applications-merged/electronics.menu
%{_datadir}/desktop-directories/*.directory



%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Apr  8 2013 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> - 1.0-12
- Fix a typo in menu french translation
- Frenchify submenus
- Add eeschema & pcbnew (kicad), pikdev and qucs menu entries

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-11.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-10.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-9.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-8.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Sep 29 2009 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 1.0-7
- Improved submenus structure for F-12

* Sat Aug 28 2009 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 1.0-6
- Improved submenus structure for F-12

* Wed Jul 08 2009 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 1.0-4
- patched for submenus
- added extra icons and directory desktop files to support the submenus feature

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Jul 06 2008 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 1.0-2
- Corrected yum install with requires(pre)

* Fri Feb 01 2008 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 1.0-1
- Initial package for Fedora

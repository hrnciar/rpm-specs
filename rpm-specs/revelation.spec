%global gettext_package revelation
%global glib2_version 2.52.0
%global gtk3_version 3.22

Name:           revelation
Version:        0.5.4
Release:        2%{?dist}
Summary:        A password manager for the GNOME desktop
# The entire source code is GPLv2 except src/lib/PBKDF2.py which is MIT
License:        GPLv2
URL:            https://revelation.olasagasti.info
Source0:        https://github.com/mikelolasagasti/%{name}/releases/download/%{name}-%{version}/%{name}-%{version}.tar.xz
Patch0:         0001-Change-mime-icon-path.patch
BuildArch:      noarch

BuildRequires:  meson
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-gobject-devel
BuildRequires:  gettext-devel
BuildRequires:  glib2-devel >= %{glib2_version}
BuildRequires:  gtk3-devel >= %{gtk3_version}
BuildRequires:  dconf-devel
BuildRequires:  gsettings-desktop-schemas-devel
BuildRequires:  python3-pycryptodomex
BuildRequires:  python3-pwquality
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
Requires:       python3-gobject
Requires:       python3-pycryptodomex
Requires:       python3-pwquality
Requires:       dbus
Requires:       glib2%{?_isa} >= %{glib2_version}
Requires:       gsettings-desktop-schemas
Requires:       gtk3%{?_isa} >= %{gtk3_version}
Requires:       hicolor-icon-theme

%description
Revelation is a password manager for the GNOME desktop, released under the GNU
GPL license. It stores all your accounts and passwords in a single, secure
place, and gives you access to it through a user-friendly graphical interface. 

%prep
%autosetup -p1

%build
%meson
%define __ninja_common_opts -v
%meson_build

%install
%meson_install
%find_lang %{gettext_package}

%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/info.olasagasti.revelation.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/info.olasagasti.revelation.desktop

%files -f %{name}.lang
%license COPYING
%doc AUTHORS NEWS README.md TODO
%{_bindir}/*
%{_metainfodir}/*.appdata.xml
%{_datadir}/applications/*.desktop
%{_datadir}/%{name}/
%{_datadir}/icons/hicolor/??x??/mimetypes/gnome-mime-application-x-revelation.png
%{_datadir}/icons/hicolor/*/apps/info.olasagasti.%{name}*.*
%{python3_sitelib}/%{name}/
%{_datadir}/mime/packages/*
%{_datadir}/glib-2.0/schemas/info.olasagasti.revelation.gschema.xml

%changelog
* Sun Oct 4 2020 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 0.5.4-2
- Fix doc

* Sun Oct 4 2020 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 0.5.4-1
- Version bump
- Remove MIT licensed PBKDF2 implementation

* Sun Sep 13 2020 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 0.5.3-1
- Version bump
- Changed dep from python3-crypto to python3-cryptodomex

* Fri Sep 11 2020 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 0.5.2-3
- Changes from review #bz1877702

* Thu Sep 10 2020 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 0.5.2-2
- Changes from review #bz1877702
- Add builddeps on desktop-file-utils and libappstream-glib
- Add check section for desktop and appdata

* Fri Sep 04 2020 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 0.5.2-1
- Version bump

* Sun Aug 30 2020 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 0.5.1-1
- Version bump

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.14-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.14-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.14-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.4.14-19
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.14-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.14-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.14-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Mar 14 2017 Pete Walter <pwalter@fedoraproject.org> - 0.4.14-15
- Disable GNOME 2 panel applet

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.14-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.14-13
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.14-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Sep 11 2015 Pete Walter <pwalter@fedoraproject.org> - 0.4.14-11
- Spec clean up
- Validate appdata and desktop files
- Don't create empty debuginfo subpackage (#832752)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.14-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 0.4.14-9
- Add an AppData file for the software center

* Thu Oct 02 2014 Rex Dieter <rdieter@fedoraproject.org> 0.4.14-8
- update desktop/icon/mime scriptlets

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.14-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed May 01 2013 Jon Ciesla <limburgher@gmail.com> - 0.4.14-4
- Drop desktop vendor tag.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 01 2012 Jef Spaleta <jspaleta@fedoraproject.org> - 0.4.14-1
- New Upstream release which addresses weak encryption format. 

* Sun Jun 24 2012 Jef Spaleta <jspaleta@fedoraproject.org> - 0.4.13-3
- Upstream pre-release which addresses weak encryption format. 
- This version will detect old encryption format and will prompt you to 
  re-save in new format.

* Fri Jun 15 2012 Jef Spaleta <jspaleta@fedoraproject.org> - 0.4.13-2
- dep fix up for rawhide building 

* Fri Jun 15 2012 Jef Spaleta <jspaleta@fedoraproject.org> - 0.4.13-1
- New upstream development location and new release 

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.11-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Sep 15 2011 Jef Spaleta <jspaleta@fedoraproject.org> - 0.4.11-17
- still actually requires gnome-python2-gnome without the applet

* Wed Aug 03 2011 Adam Williamson <awilliam@redhat.com> - 0.4.11-16
- still actually requires gnome-python2-bonobo without the applet

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.11-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Feb 02 2011 Adam Williamson <awilliam@redhat.com> - 0.4.11-14
- drop the manual gnome-python2-applet require

* Wed Feb 02 2011 Adam Williamson <awilliam@redhat.com> - 0.4.11-13
- obsolete the applet schema

* Wed Feb 02 2011 Adam Williamson <awilliam@redhat.com> - 0.4.11-12
- ditch the applet, we're not supporting them any more in GNOME 3
- drop some now useless deps, add a BR on intltool
- gcc.patch: fix incorrect use of --export-dynamic parameter
- add the dist tag to the EVR

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.4.11-11
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Mon May 24 2010 Jef Spaleta <jspaleta@fedoraproject.org> - 0.4.11-10
- UI patch update to fix broken icons. 

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.11-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Dec  5 2008 Jeremy Katz <katzj@redhat.com> - 0.4.11-7
- rebuild for python 2.6 harder

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.4.11-6.1
- Rebuild for Python 2.6

* Fri Oct 03 2008 Jef Spaleta <jspaleta@fedoraproject.org> - 0.4.11-5.1
- Depchain fix.

* Fri Oct 03 2008 Jef Spaleta <jspaleta@fedoraproject.org> - 0.4.11-5
- Minor patch to ui.py to fix broken menu generation.

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.4.11-4.1
- Autorebuild for GCC 4.3

* Tue Aug 21 2007 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 0.4.11-3.1
- Remove version key from desktop file

* Fri Aug 03 2007 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info>
- Update License field due to the "Licensing guidelines changes"

* Mon Jun 04 2007 Thorsten Leemhuis <fedora at leemhuis dot info> 0.4.11-3
- Rebuild to build for ppc64 as well

* Wed Feb 07 2007 Thorsten Leemhuis <fedora at leemhuis dot info> 0.4.11-2
- use RPM_OPT_FLAGS during build (patch from Ville, #226680)

* Thu Jan 11 2007 Thorsten Leemhuis <fedora at leemhuis dot info> 0.4.11-1
- update to 0.4.11 (fixes revelation-applet, upstream #202)
- run gconftool-2 for applet stuff, too

* Thu Jan 11 2007 Thorsten Leemhuis <fedora at leemhuis dot info> 0.4.9-1
- update to 0.4.9
- Remove 0.4.8-specific workaround 
- Remove manual python-abi requires

* Sun Dec 31 2006 Thorsten Leemhuis <fedora at leemhuis dot info> 0.4.8-2
- BR gnome-python2-applet

* Sun Dec 31 2006 Thorsten Leemhuis <fedora at leemhuis dot info> 0.4.8-1
- update to 0.4.8
- ships locales now; use find_lang, BR gettext, perl(XML::Parser)

* Sat Dec 09 2006 Thorsten Leemhuis <fedora[AT]leemhuis.info> - 0.4.7-7
- Rebuild for python 2.5

* Thu Oct 31 2006 Thorsten Leemhuis <fedora[AT]leemhuis.info> - 0.4.7-6
- track rawhide and BR gnome-python2-devel and cracklib-devel

* Thu Sep 07 2006 Thorsten Leemhuis <fedora[AT]leemhuis.info> - 0.4.7-5
- Don't ghost pyo files (#205432)

* Tue Aug 29 2006 Thorsten Leemhuis <fedora[AT]leemhuis.info> - 0.4.7-4
- Rebuild for Fedora Extras 6

* Mon Feb 15 2006 Thorsten Leemhuis <fedora[AT]leemhuis.info>  0.4.7-3
- BR gnome-python2-desktop now needed

* Mon Feb 13 2006 Thorsten Leemhuis <fedora[AT]leemhuis.info>
- Rebuild for Fedora Extras 5

* Mon Feb 06 2006 Thorsten Leemhuis <fedora at leemhuis dot info> 0.4.7-1
- update to 0.4.7

* Fri Oct 14 2005 Thorsten Leemhuis <fedora at leemhuis dot info> 0.4.5-3
- use cracklib-dicts correctly (#170742)
- don't ship revelation dicts

* Mon Aug 27 2005 Thorsten Leemhuis <fedora at leemhuis dot info> 0.4.5-2
- Require gnome-python2-applet (#166987)

* Mon Aug 27 2005 Thorsten Leemhuis <fedora at leemhuis dot info> 0.4.5-1
- Update to 0.4.5
- add patch revelation-dont_check_everything.patch

* Fri Aug 19 2005 Thorsten Leemhuis <fedora at leemhuis dot info> 0.4.4-2
- rebuild

* Mon Aug 08 2005 Thorsten Leemhuis <fedora at leemhuis dot info> 0.4.4-1
- Update to 0.4.4
- Use dist-macro
- New BR gnome-panel-devel  gnome-python2-extras

* Fri May 06 2005 Thorsten Leemhuis <fedora at leemhuis dot info> 0.4.3-3
- Update the GTK+ theme icon cache on (un)install

* Sat Apr 02 2005 Thorsten Leemhuis <fedora at leemhuis dot info> 0:0.4.3-2
- Devel rebuild

* Sat Apr 02 2005 Thorsten Leemhuis <fedora at leemhuis dot info> 0:0.4.3-1
- Update to 0.4.3
- BR words, cracklib, Req words
- Use configure para -with-cracklib-dict=/usr/share/dict/

* Wed Mar 30 2005 Thorsten Leemhuis <fedora at leemhuis dot info> 0:0.4.2-1
- Update to 0.4.2

* Tue Mar 01 2005 Thorsten Leemhuis <fedora at leemhuis dot info> 0:0.4.0-1
- Update to 0.4.0 - depends on gtk 2.4 now
- Uses configure now
- add BR pygtk2-devel gnome-keyring-devel
- use shared-mime-info and desktop-file-utils
- Remove unneeded explicit Requires
- not a noarch package anymore
- on x86_64 it currently installs and needs authmanager.so in %%{python_sitelib}
  will report upstream

* Wed Sep 29 2004 Thorsten Leemhuis <fedora at leemhuis dot info> 0:0.3.4-0.fdr.1
- Update to 0.3.4

* Tue Aug 31 2004 Thorsten Leemhuis <fedora at leemhuis dot info> 0:0.3.3-0.fdr.1
- Update to 0.3.3

* Thu Aug 11 2004 Thorsten Leemhuis <fedora at leemhuis dot info> 0:0.3.2-0.fdr.2
- Own python_sitelib/revelation/

* Wed Aug 11 2004 Thorsten Leemhuis <fedora at leemhuis dot info> 0:0.3.2-0.fdr.1
- Update to 0.3.2
- convert package to noarch
- convert parts to match python spec-file template

* Sat Jul 17 2004 Thorsten Leemhuis <fedora at leemhuis dot info> 0:0.3.0-0.fdr.1
- New Spec File based on Matthew Hall and Dags SPEC Files -- Thanks to them
- Fix Gconf handling

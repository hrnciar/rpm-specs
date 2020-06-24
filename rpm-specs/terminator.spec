Name:           terminator
Version:        1.92
Release:        4%{?dist}
Summary:        Store and run multiple GNOME terminals in one window

License:        GPLv2
URL:            https://github.com/gnome-terminator
Source0:        https://github.com/gnome-terminator/terminator/releases/download/v1.92/terminator-1.92.tar.gz

BuildArch:      noarch

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  gtk-update-icon-cache
BuildRequires:  intltool
BuildRequires:  python3-devel

Requires:       keybinder3
Requires:       python3-configobj
Requires:       python3-gobject
Requires:       python3-psutil
Requires:       vte291

Patch0:         0000-terminator-fix-desktop-file.patch
Patch1:         0001-Disable-special-logic-for-pasting-on-Wayland.patch

%description
Multiple GNOME terminals in one window.  This is a project to produce
an efficient way of filling a large area of screen space with
terminals. This is done by splitting the window into a resizeable
grid of terminals. As such, you can  produce a very flexible
arrangements of terminals for different tasks.


%prep
%setup -q -n terminator-%{version}

%patch0 -p0
%patch1 -p1


%build
%{__python3} setup.py build


%install
rm -rf %{buildroot}
%{__python3} setup.py install -O1 --skip-build --root %{buildroot}
%find_lang %{name}
rm -f %{buildroot}/%{_datadir}/icons/hicolor/icon-theme.cache
rm -f %{buildroot}/%{_datadir}/applications/%{name}.desktop
desktop-file-install --dir=${RPM_BUILD_ROOT}%{_datadir}/applications data/%{name}.desktop


%files -f %{name}.lang
%doc COPYING
%{_mandir}/man1/%{name}.*
%{_mandir}/man5/%{name}_config.*
%{_bindir}/%{name}*
%{_bindir}/remotinator
%{python3_sitelib}/*
%{_datadir}/%{name}/terminatorlib/themes/*/gtk-3.0/apps/*.css
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/HighContrast/*/*/%{name}*.png
%{_datadir}/icons/HighContrast/*/*/%{name}*.svg
%{_datadir}/icons/HighContrast/16x16/status/terminal-bell.png
%{_datadir}/icons/hicolor/*/*/%{name}*.png
%{_datadir}/icons/hicolor/*/*/%{name}*.svg
%{_datadir}/icons/hicolor/16x16/status/terminal-bell.png
%{_datadir}/pixmaps/%{name}.png

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.92-4
- Rebuilt for Python 3.9

* Mon May 18 2020 Dominic Hopf <dmaphy@fedoraproject.org> - 1.92-3
- Backport upstream patch for middle click issues on Wayland (RHBZ#1836812)

* Wed May 06 2020 Dominic Hopf <dmaphy@fedoraproject.org> - 1.92-2
- Improve requirement listings
- Fix requirement for python3-psutil on EPEL8
- Add missing requirement for gtk-update-icon-cache

* Sat Apr 18 2020 Dominic Hopf <dmaphy@fedoraproject.org> - 1.92-1
- New upstream release: 1.92

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.91-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 20 2019 Matt Rose <mattrose@folkwolf.net> - 1.91-14
- fix bug 1573927
* Tue Dec 17 2019 Matt Rose <mattrose@folkwolf.net> - 1.91-12
- Fix url Drag and Drop.  Thanks to Egmont Koblinger

* Mon Dec 16 2019 Matt Rose <mattrose@folkwolf.net> - 1.91-11
- Patched with python3 support, with thanks from Egmont Koblinger and Roman Kovtyukh

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.91-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.91-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 24 2018 Miro Hrončok <mhroncok@redhat.com> - 1.91-8
- Update Python macros to new packaging standards
  (See https://fedoraproject.org/wiki/Changes/Move_usr_bin_python_into_separate_package)

* Sat Jul 21 2018 Dominic Hopf <dmaphy@fedoraproject.org> - 1.91-7
- RHBZ#1606509: Fix FTBFS issue, explicitly use python2

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.91-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 21 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.91-5
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.91-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.91-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb 27 2017 Dominic Hopf <dmaphy@fedoraproject.org> - 1.91-1
- New Upstream Release: Terminator 1.91

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.90-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Nov 30 2016 Matt Rose <mattrose@folkwolf.net> - 1.90-4
- add keybinder3 to requires

* Tue Nov 29 2016 Matt Rose <mattrose@folkwolf.net> - 1.90-3
- adjust requires for vte

* Thu Nov 24 2016 Dominic Hopf <dmaphy@fedoraproject.org> - 1.90-2
- Adjust requires for python(2)-psutil for EPEL

* Wed Nov 23 2016 Dominic Hopf <dmaphy@fedoraproject.org> - 1.90-1
- New Upstream Release: Terminator 1.90

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.98-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.98-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Oct 10 2015 Marco Driusso <marcodriusso@gmail.com> - 0.98-2
- apply patch from upstream for fixing RHBZ#1268289 and add dependency to
  python-psutils

* Tue Sep 08 2015 Dominic Hopf <dmaphy@fedoraproject.org> - 0.98-1
- New Upstream Release: Terminator 0.98

* Thu Jun 25 2015 Dominic Hopf <dmaphy@fedoraproject.org> - 0.97-8
- add dependency to python-keybinder (RHBZ#1234627)

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.97-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.97-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Jan 05 2014 Dominic Hopf <dmaphy@fedoraproject.org> - 0.97-5
- fix the new URL for the website

* Sun Jan 05 2014 Dominic Hopf <dmaphy@fedoraproject.org> - 0.97-4
- update upstream URL to new website (RHBZ#1048553)
- fix bogus date in changelog-warnings

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.97-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 28 2013 Dominic Hopf <dmaphy@fedoraproject.org> - 0.97-2
- fix an issue when inactive colour is set to 1.0 (RHBZ#968379)

* Fri May 17 2013 Dominic Hopf <dmaphy@fedoraproject.org> - 0.97-1
- New upstream release: Terminator 0.97

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.96-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.96-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.96-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Sep 24 2011 Dominic Hopf <dmaphy@fedoraproject.org> - 0.96-1
- New upstream release: Terminator 0.96

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.95-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Oct 01 2010 Dominic Hopf <dmaphy@fedoraproject.org> - 0.95-2
- readd dependency for gnome-python2-bonobo

* Wed Aug 25 2010 Dominic Hopf <dmaphy@fedoraproject.org> - 0.95-1
- New upstream release: Terminator 0.95

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.94-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Mon Jul 19 2010 Dominic Hopf <dmaphy@fedoraproject.org> - 0.94-1
- New upstream release: Terminator 0.94

* Thu Apr 15 2010 Dominic Hopf <dmaphy@fedoraproject.org> - 0.93-1
- New upstream release: Terminator 0.93

* Fri Apr 09 2010 Dominic Hopf <dmaphy@fedoraproject.org> - 0.92-1
- New upstream release: Terminator 0.92

* Mon Apr 05 2010 Dominic Hopf <dmaphy@fedoraproject.org> - 0.91-1
- New upstream release: Terminator 0.91

* Wed Mar 10 2010 Steven Fernandez <lonetwin@fedoraproject.org> 0.14-3
- Added patch to fix the traceback reported in bug 567861

* Wed Mar 3 2010 Steven Fernandez <lonetwin@fedoraproject.org> - 0.14-2
- Added dependency for deskbar-applets and gnome-python2-{bonobo,canvas}
  packages (bug 540551 and bug 509461)

* Thu Jan 14 2010 Dominic Hopf <dmaphy@fedoraproject.org> - 0.14-1
- New terminator version 0.14

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jul  7 2009 Ian Weller <ian@ianweller.org> - 0.13-2
- BuildRequires: intltool

* Thu Jul  2 2009 Ian Weller <ian@ianweller.org> - 0.13-1
- New upstream release

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jan 20 2009 Ian Weller <ianweller@gmail.com> 0.12-1
- New upstream release
- Upstream fixed desktop file, removing patch0

* Mon Dec 08 2008 Ian Weller <ianweller@gmail.com> 0.11-3
- Patch version in terminatorlib/verison.py to the one we think it is
- Fix License tag
- Update post and postun scripts with one line

* Mon Dec 01 2008 Ian Weller <ianweller@gmail.com> 0.11-2
- Add BuildRequires: gettext
- Fix installation of .desktop file
- terminator-0.11-desktop.patch:
    Remove useless things
    Move to same category as gnome-terminal
- Uses spaces instead of tabs in the specfile because I can't stand tabs

* Mon Dec 01 2008 Ian Weller <ianweller@gmail.com> 0.11-1
- Update upstream
- Fix description to something useful
- Fix group
- Fix some specfile oddities
- Complete/restandardize file list
- Get rid of she-bangs in python_sitelib

* Sat Sep 13 2008 Max Spevack <mspevack AT redhat DOT com> 0.10
- New upstream release.
- Tried to make sure the spec file matches guidelines on Fedora wiki.

* Tue Jul 08 2008 chantra AatT rpm-based DdOoTt org 0.9.fc9.rb
- New upstream release

* Sat May 17 2008 chantra AatT rpm-based DdOoTt org 0.8.1.fc9.rb
- Initial release for Fedora 9.

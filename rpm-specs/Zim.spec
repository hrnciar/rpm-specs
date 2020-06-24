Name:           Zim
Version:        0.73.0
Release:        1%{?dist}
Summary:        Desktop wiki & notekeeper

# The entire source code is GPLv2+ except
# ./zim/plugins/pageindex/generictreemodel,.py which is LGPLv2+
License:        GPLv2+ and LGPLv2+
URL:            http://zim-wiki.org/
Source0:        http://www.zim-wiki.org/downloads/zim-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  desktop-file-utils
BuildRequires:  python3-devel
BuildRequires:  python3-gobject
BuildRequires:  gtk3, python3-pyxdg
# for tests
#BuildRequires:  /usr/bin/xvfb-run

Requires:       python3-gobject
Requires:       gtk3, python3-pyxdg
Recommends:     libappindicator-gtk3

%description
Zim is a WYSIWYG text editor written in Python which aims to bring the
concept of a wiki to your desktop. Every page is saved as a text file with
wiki markup. Pages can contain links to other pages, and are saved
automatically. Creating a new page is as easy as linking to a non-existing
page. Pages are ordered in a hierarchical structure that gives it the look
and feel of an outliner. This tool is intended to keep track of TODO lists
or to serve as a personal scratch book.

%prep
%setup -q -n zim-%{version}
# https://github.com/zim-desktop-wiki/zim-desktop-wiki/issues/1114
sed -i 's/cElementTree/ElementTree/' zim/parser.py

%build
./setup.py build

%install
rm -rf %{buildroot}
./setup.py install --root=%{buildroot} --skip-build

%find_lang zim

desktop-file-validate %{buildroot}%{_datadir}/applications/zim.desktop

%check
# Tests do not pass
# https://github.com/zim-desktop-wiki/zim-desktop-wiki/issues/814
#xvfb-run ./test.py

%if 0%{?rhel} && 0%{?rhel} <= 7
%post
update-desktop-database &> /dev/null || :
touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :
touch --no-create %{_datadir}/mime/packages &> /dev/null || :

%postun
update-desktop-database &> /dev/null || :
if [ $1 -eq 0 ] ; then
    touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :
    gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
    touch --no-create %{_datadir}/mime/packages &> /dev/null || :
    update-mime-database %{?fedora:-n} %{_datadir}/mime &> /dev/null || :
fi

%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
update-mime-database %{?fedora:-n} %{_datadir}/mime &> /dev/null || :
%endif

%files -f zim.lang
%license LICENSE
%doc *.md contrib/
%{_mandir}/man[13]/*.[13]*
%{_bindir}/*
%{_datadir}/zim/
%{_datadir}/pixmaps/*
%{_datadir}/applications/*
%{_datadir}/mime/packages/zim.xml
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/icons/hicolor/*/mimetypes/*
# No package in Fedora provides such directories
%{_datadir}/icons/ubuntu-mono-*/
%{python3_sitelib}/zim-*.egg-info
%{python3_sitelib}/zim/
%{_datadir}/metainfo/*

%changelog
* Tue Jun  9 2020 Robin Lee <cheeselee@fedoraproject.org> - 0.73.0-1
- Update to 0.73.0

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.72.1-2
- Rebuilt for Python 3.9

* Sun Mar 29 2020 Robin Lee <cheeselee@fedoraproject.org> - 0.72.1-1
- Update to 0.72.1

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.72.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Sep  1 2019 Robin Lee <cheeselee@fedoraproject.org> - 0.72.0-1
- Release 0.72.0
- Add launchable entry to metainfo (RHBZ#1729275)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.71.1-3
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.71.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 24 2019 Robin Lee <cheeselee@fedoraproject.org> - 0.71.1-1
- Update to 0.71.1
- Disable tests

* Mon Apr  1 2019 Robin Lee <cheeselee@fedoraproject.org> - 0.70-1
- new release
- Recommends appindicator to keep compatible with previous version
- Enable tests

* Tue Feb 19 2019 Robin Lee <cheeselee@fedoraproject.org> - 0.70-0.3.rc3
- Update to 0.70-rc3

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.70-0.2.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 22 2019 Robin Lee <cheeselee@fedoraproject.org> - 0.70-0.1.rc1
- Update to 0.70-rc1, which switched to Python3 and Gtk+3

* Mon Dec 17 2018 Robin Lee <cheeselee@fedoraproject.org> - 0.69-1
- Update to 0.69
- Fix Requires on Fedora <= 28

* Mon Oct 22 2018 Robin Lee <cheeselee@fedoraproject.org> - 0.68-4
- Fix for epel7

* Thu Jul 19 2018 Robin Lee <cheeselee@fedoraproject.org> - 0.68-3
- Use python2_sitelib macro (BZ#1603334)

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.68-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Apr 26 2018 Iryna Shcherbina <shcherbina.iryna@gmail.com> - 0.68-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Mon Apr  2 2018 Robin Lee <cheeselee@fedoraproject.org> - 0.68-1
- Update to 0.68

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.67-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 30 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.67-3
- Remove obsolete scriptlets

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.67-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 11 2017 Robin Lee <cheeselee@fedoraproject.org> - 0.67-1
- Update to 0.67

* Wed Jun 14 2017 Robin Lee <cheeselee@fedoraproject.org> - 0.67-0.rc2.1
- Update to 0.67-rc2

* Wed Jun 07 2017 Oliver Haessler <oliver@redhat.com> - 0.66-2
- added patch for "Fix for logger missing in newfs" to allow build of 0.66 on
  Fedora/RHEL (will be fixed in 0.67)

* Tue Jun 06 2017 Oliver Haessler <oliver@redhat.com> - 0.66-1
- Update to 0.66

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.65-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.65-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.65-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov  2 2015 Robin Lee <lirb@winhong.com> - 0.65-1
- Update to 0.65

* Wed Oct 28 2015 Robin Lee <cheeselee@fedoraproject.org> - 0.64-1
- Update to 0.64 (BZ#1275861)

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.63-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 15 2015 Robin Lee <cheeselee@fedoraproject.org> - 0.63-1
- Update to 0.63
- Requires python-appindicator to fix trayicon on Plasma 5
- Drop applied 755_754.diff

* Sun Nov 16 2014 Robin Lee <cheeselee@fedoraproject.org> - 0.62-2
- Backport upstream bzr755 to fix mis-matched gtk and pygtk in Fedora/RHEL

* Fri Oct  3 2014 Robin Lee <cheeselee@fedoraproject.org> - 0.62-1
- Update to 0.62

* Thu Oct 02 2014 Rex Dieter <rdieter@fedoraproject.org> 0.61-2
- update mime scriptlets

* Sat Aug  2 2014 Robin Lee <cheeselee@fedoraproject.org> - 0.61-1
- Update to 0.61

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.60-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.60-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed May  1 2013 Robin Lee <cheeselee@fedoraproject.org> - 0.60-1
- Update to 0.60

* Thu Jan 24 2013 Robin Lee <cheeselee@fedoraproject.org> - 0.59-1
- Update to 0.59 (#903621, #841803, #857820, #858250, #871030, #875776)

* Mon Dec 17 2012 Robin Lee <cheeselee@fedoraproject.org> - 0.58-1
- Update to 0.58

* Mon Nov 19 2012 Robin Lee <cheeselee@fedoraproject.org> - 0.57-2
- Backport fix for #865078, #865079

* Tue Oct  9 2012 Robin Lee <cheeselee@fedoraproject.org> - 0.57-1
- Update to 0.57 (#807149, #826886)

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.56-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun May 27 2012 Robin Lee <cheeselee@fedoraproject.org> - 0.56-3
- bug #802750

* Thu May 24 2012 Robin Lee <cheeselee@fedoraproject.org> - 0.56-2
- BZ#822454

* Wed Apr  4 2012 Robin Lee <cheeselee@fedoraproject.org> - 0.56-1
- Update to 0.56

* Wed Feb 29 2012 Robin Lee <cheeselee@fedoraproject.org> - 0.55-1
- Update to 0.55

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.54-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Dec 23 2011 Robin Lee <cheeselee@fedoraproject.org> - 0.54-2
- Just use %%{_datadir}

* Fri Dec 23 2011 Robin Lee <cheeselee@fedoraproject.org> - 0.54-1
- Update to 0.54 (#740211)

* Tue Sep 20 2011 Robin Lee <cheeselee@fedoraproject.org> - 0.53-1
- Update to 0.53 (#702811, #708471, #719889, #720434, #727804)

* Fri Apr 29 2011 Robin Lee <cheeselee@fedoraproject.org> - 0.52-1
- Update to 0.52 (#700001)

* Wed Apr 20 2011 Robin Lee <cheeselee@fedoraproject.org> - 0.51-1
- Update to 0.51 (#683469)

* Sun Mar  6 2011 Robin Lee <cheeselee@fedoraproject.org> - 0.50-2
- Fix quicknote problem (#680057)

* Wed Feb 16 2011 Robin Lee <cheeselee@fedoraproject.org> - 0.50-1
- 0.50 (#654373, #657928)
- Remove redundant python sitelib definition

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.49-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Nov  3 2010 Robin Lee <cheeselee@fedoraproject.org> - 0.49-1
- Update to 0.49
- Check desktop entry file in %%check section

* Mon Aug 30 2010 Robin Lee <robinlee.sysu@gmail.com> - 0.48-2
- Move building command to %%build section

* Sat Aug 28 2010 Robin Lee <robinlee.sysu@gmail.com> - 0.48-1
- update to 0.48
- include more icons

* Sat Jul 31 2010 Thomas Spura <tomspur@fedoraproject.org> - 0.47-2
- Rebuild for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Mon Jun 14 2010 Robin Lee <robinlee.sysu@gmail.com> - 0.47-1
- update to 0.47, upstream reimplementation with PyGTK
- remove vendor from the desktop entry file name
- License changed to 'GPLv2+ and LGPLv3+'
- remove BuildRoot tag
- clean some whitespaces

* Wed Jun 02 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.29-2
- Mass rebuild with perl-5.12.0

* Tue Feb 09 2010 Chris Weyl <cweyl@alumni.drew.edu>
- update to 0.29
- add perl_default_filter

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 0.28-3
- rebuild against perl 5.10.1

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Mar 16 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.28-1
- update to 0.28

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Nov 21 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.27-1
- update to 0.27

* Thu Sep 25 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.26-1
- update to 0.26

* Tue Aug 05 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.25-2
- drop tests entirely for the moment.

* Sun Aug 03 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.25-1
- update to 0.25
- note we nuke t/71_gui_daemon.t -- it fails under perl 5.10; per
  upstream it's '...not a problem during normal usage of the program.'

* Thu Mar 06 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.23-2
Rebuild for new perl

* Thu Nov 22 2007 Chris Weyl <cweyl@alumni.drew.edu> 0.23-1
- update to 0.23

* Wed Oct 03 2007 Chris Weyl <cweyl@alumni.drew.edu> 0.21-1
- update to 0.21
- add contrib/, TRepository.PL to doc
- update license tag: GPL -> GPL+
- add a requires on scrot, for the InsertScreenshot plugin

* Wed May 30 2007 Chris Weyl <cweyl@alumni.drew.edu> 0.19-2
- add a require on Gtk2::TrayIcon; not picked up automatically
- some BR refactoring given perl splittage

* Thu Mar 22 2007 Chris Weyl <cweyl@alumni.drew.edu> 0.19-1
- and hot on the heels of 0.18 is 0.19! :)

* Sat Mar 17 2007 Chris Weyl <cweyl@alumni.drew.edu> 0.18-1
- update to 0.18
- fix homepage/download links
- drop dep on shared-mime-info as bz#215972 has been resolved

* Tue Nov 21 2006 Chris Weyl <cweyl@alumni.drew.edu> 0.17-3
- bump

* Thu Nov 16 2006 Chris Weyl <cweyl@alumni.drew.edu> 0.17-2
- add requires on shared-mime-info

* Wed Nov 15 2006 Chris Weyl <cweyl@alumni.drew.edu> 0.17-1
- initial packaging.

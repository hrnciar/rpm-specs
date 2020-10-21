%undefine __cmake_in_source_build

%global gitcommit_full 93726f3d4e177816337beaf5c8872859ef33e9d8
%global gitcommit %(c=%{gitcommit_full}; echo ${c:0:7})

Name:           krename
Version:        5.0.60
Release:        8%{?dist}
Summary:        Powerful batch file renamer
License:        GPLv2
URL:            https://github.com/KDE/krename
Source0:        %{url}/tarball/%{gitcommit_full}


BuildRequires:  gcc-c++
BuildRequires:  extra-cmake-modules
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(KF5Archive)
BuildRequires:  cmake(KF5Completion)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5ItemViews)
BuildRequires:  cmake(KF5JobWidgets)
BuildRequires:  cmake(KF5JS)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Service)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  taglib-devel
BuildRequires:  exiv2-devel
BuildRequires:  podofo-devel
BuildRequires:  freetype-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

%description
KRename is a very powerfull batch file renamer by KDE. It allows you to easily
rename hundreds or even more files in one go. The filenames can be created by
parts of the original filename, numbering the files or accessing hundreds of
informations about the file, like creation date or Exif informations of an
image.


%prep
%autosetup -n KDE-%{name}-%{gitcommit}


%build
%{cmake_kf5}
%cmake_build


%install
%cmake_install


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.kde.%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.appdata.xml


%files
%license COPYING COPYING-CMAKE-SCRIPTS
%doc AUTHORS README.md TODO
%{_bindir}/%{name}
%{_datadir}/metainfo/org.kde.%{name}.appdata.xml
%{_datadir}/applications/org.kde.%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/icons/locolor/*/apps/*.png
%{_datadir}/kservices5/ServiceMenus/%{name}*.desktop


%changelog
* Tue Aug 04 2020 Vasiliy Glazov Vasiliy N. Glazov <vascom2@gmail.com> 5.0.60-8
- Update to latest git

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.60-7
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.60-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.60-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.60-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.60-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 30 2019 Rex Dieter <rdieter@fedoraproject.org> - 5.0.60-2
- rebuild (exiv2)

* Thu Dec 27 2018 Vasiliy Glazov Vasiliy N. Glazov <vascom2@gmail.com> 5.0.60-1
- Initial release with KF5

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.9-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Sandro Mani <manisandro@gmail.com> - 4.0.9-26
- Rebuild (podofo)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.9-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 4.0.9-24
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.9-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.9-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 02 2017 Rex Dieter <rdieter@fedoraproject.org> - 4.0.9-21
- rebuild (exiv2)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.9-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 02 2017 Sandro Mani <manisandro@gmail.com> - 4.0.9-19
- Rebuild (podofo)

* Thu Dec 08 2016 Radek Novacek <rad.n@centrum.cz> - 4.0.9-18
- fix FTBFS

* Thu Nov 24 2016 Radek Novacek <rnovacek@redhat.com> - 4.0.9-18
- podofo rebuild.

* Fri Sep 23 2016 Jon Ciesla <limburgher@gmail.com> - 4.0.9-17
- podofo rebuild.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.9-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 24 2015 Rex Dieter <rdieter@fedoraproject.org> - 4.0.9-15
- rebuild (exiv2)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.9-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 4.0.9-13
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.9-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.9-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Dec 03 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.0.9-10
- rebuild (exiv2)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Mar 21 2013 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.9-8
- apply upstream fix for FindLIBPODOFO.cmake

* Thu Mar 21 2013 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.9-7
- BR: podofo-devel (for PDF support)
- clean up specfile further (remove more deprecated stuff)

* Mon Mar 18 2013 Radek Novacek <rnovacek@redhat.com> 4.0.9-6
- Fix FTBFS because of freetype includes
- Get rid of deprecated Buildroot and Group tags in spec
- Add BR: freetype-devel

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed May 02 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.0.9-3
- rebuild (exiv2)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jan 02 2012 Radek Novacek <rnovacek@redhat.com> 4.0.9-1
- Update to 4.0.9
- Drop patch for static init crash

* Fri Oct 14 2011 Rex Dieter <rdieter@fedoraproject.org> - 4.0.7-3
- rebuild (exiv2)

* Wed Mar 16 2011 Radek Novacek <rnovacek@redhat.com> - 4.0.7-2
- Fixed crash on static initialization
- Resolves: #684908

* Fri Feb 25 2011 Radek Novacek <rnovacek@redhat.com> - 4.0.7-1
- Update to 4.0.7

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 31 2011 Radek Novacek <rnovacek@redhat.com> - 4.0.6-1
- Update to 4.0.6

* Sun Jan 02 2011 Rex Dieter <rdieter@fedoraproject.org> - 4.0.5-2
- rebuild (exiv2)

* Thu Sep 30 2010 Radek Novacek <rnovacek@redhat.com> 4.0.5-1
- Update to 4.0.5

* Wed Sep 29 2010 jkeating - 4.0.4-2
- Rebuilt for gcc bug 634757

* Mon Sep 13 2010 Radek Novacek <rnovacek@redhat.com> - 4.0.4-1
- Update to 4.0.4

* Mon May 31 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.0.1-3
- rebuild (exiv2)

* Mon Jan 03 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.0.1-2 
- rebuild (exiv2)
- drop extraneous Req: hicolor-icon-theme
- update icon scriptlets

* Mon Oct 5 2009 Ben Boeckel <MathStuf@gmail.com> - 4.0.1-1
- Update to 4.0.1

* Tue Sep 29 2009 Ben Boeckel <MathStuf@gmail.com> - 4.0.0-1
- Update to KDE4 version

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 22 2008 Michał Bentkowski <mr.ecik at gmail.com> - 3.0.14-4
- Fix BR

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 3.0.14-3
- Autorebuild for GCC 4.3

* Fri Aug 24 2007 Michał Bentkowski <mr.ecik at gmail.com> - 3.0.14-2
- BuildID rebuild
- License tag fix

* Sat Apr 28 2007 Michał Bentkowski <mr.ecik at gmail.com> - 3.0.14-1
- Update to 3.0.14

* Thu Dec 21 2006 Michał Bentkowski <mr.ecik at gmail.com> - 3.0.13-2
- Fix encoding of ChangeLog and TODO files
- Fix desktop file issue
- Add %%post and %%postun sections
- Make %%{_datadir}/apps/konqueror owned by this package

* Tue Dec 19 2006 Michał Bentkowski <mr.ecik at gmail.com> - 3.0.13-1
- Initial package

%undefine __cmake_in_source_build

Name:           yarock
Version:        1.4.0
Release:        10%{?dist}
Summary:        Lightweight, beautiful music player
# Main license is GPLv2+ in sources,
# but GPLv3+ in README.md and BSD (3 clause) for widgets/flowlayout
License:        GPLv3+ and BSD
URL:            https://launchpad.net/%{name}
Source0:        %{url}/1.x/%{version}/+download/Yarock_%{version}_Sources.tar.gz
Patch0:         %{name}-%{version}-appdata.patch

BuildRequires:  cmake
BuildRequires:  taglib-devel
BuildRequires:  qt5-qtbase-private-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  qt5-linguist
BuildRequires:  phonon-qt5-devel
BuildRequires:  sqlite-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  htmlcxx-devel

Requires:       hicolor-icon-theme

%description
Yarock is a music player designed to provide a clean,
simple and beautiful music collection based on album cover-art.


%prep
%setup -q -n Yarock_%{version}_Sources
%patch0 -p1
# Fix the incorrect PHONON include directory for QT5
sed -i 's/PHONON_INCLUDE_DIR/PHONON4QT5_INCLUDE_DIR/g' src/core/player/phonon/CMakeLists.txt
# remove empty dir src3party
rm -rfv src3party

%build
%cmake \
  -DENABLE_PHONON:BOOL=ON \
  -DENABLE_VLC:BOOL=OFF
%cmake_build

%install
install -D -m0644 data/org.%{name}.desktop %{buildroot}%{_datadir}/applications/org.%{name}.desktop
install -D -m0644 data/org.%{name}.appdata.xml %{buildroot}%{_datadir}/appdata/org.%{name}.appdata.xml
%cmake_install
%find_lang %{name} --all-name --with-qt
desktop-file-install \
  --remove-key=Version \
  %{buildroot}%{_datadir}/applications/org.%{name}.desktop

%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/org.%{name}.appdata.xml

%files -f %{name}.lang
%license COPYING
%doc *.md
%{_bindir}/%{name}
%{_libdir}/%{name}/
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/pixmaps/application-x-%{name}.png
%{_datadir}/applications/org.%{name}.desktop
%{_datadir}/appdata/org.%{name}.appdata.xml
%dir %{_datadir}/%{name}/
%dir %{_datadir}/%{name}/translations/

%changelog
* Fri Sep 11 2020 Jan Grulich <jgrulich@redhat.com> - 1.4.0-10
- rebuild (qt5)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 06 2020 Rex Dieter <rdieter@fedoraproject.org> - 1.4.0-8
- rebuild (qt5)

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 09 2019 Jan Grulich <jgrulich@redhat.com> - 1.4.0-6
- rebuild (qt5)

* Wed Sep 25 2019 Jan Grulich <jgrulich@redhat.com> - 1.4.0-5
- rebuild (qt5)

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 17 2019 Jan Grulich <jgrulich@redhat.com> - 1.4.0-3
- rebuild (qt5)

* Thu Apr 11 2019 Pete Walter <pwalter@fedoraproject.org> - 1.4.0-2
- rebuild (qt5)

* Thu Mar 28 2019 Martin Gansser <martinkg@fedoraproject.org> - 1.4.0-1
- Update to 1.4.0
- Add %%{name}-%%{version}-appdata.patch

* Sun Mar 03 2019 Rex Dieter <rdieter@fedoraproject.org> - 1.3.1-8
- rebuild (qt5)

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec 13 2018 Rex Dieter <rdieter@fedoraproject.org> - 1.3.1-6
- rebuild (qt5)

* Fri Sep 21 2018 Jan Grulich <jgrulich@redhat.com> - 1.3.1-5
- rebuild (qt5)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 21 2018 Rex Dieter <rdieter@fedoraproject.org> - 1.3.1-3
- rebuild (qt5)

* Sun May 27 2018 Rex Dieter <rdieter@fedoraproject.org> - 1.3.1-2
- rebuild (qt5)

* Sun Mar 04 2018 Martin Gansser <martinkg@fedoraproject.org> - 1.3.1-1
- Update to 1.3.1
- Remove ldconfig scriptlets

* Wed Feb 14 2018 Jan Grulich <jgrulich@redhat.com> - 1.3.0-4
- rebuild (qt5)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.3.0-2
- Remove obsolete scriptlets

* Wed Jan 10 2018 Martin Gansser <martinkg@fedoraproject.org> - 1.3.0-1
- Update to 1.3.0

* Wed Dec 20 2017 Jan Grulich <jgrulich@redhat.com> - 1.2.0-2
- rebuild (qt5)

* Sun Dec 03 2017 Raphael Groner <projects.rg@smart.ms> - 1.2.0-1
- new version

* Tue Oct 10 2017 Rex Dieter <rdieter@fedoraproject.org> - 1.1.6-7
- rebuild (qt5)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Rex Dieter <rdieter@fedoraproject.org> - 1.1.6-4
- rebuild (qt5)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 15 2016 Rex Dieter <rdieter@fedoraproject.org> - 1.1.6-2
- bump release

* Mon Nov 21 2016 Rex Dieter <rdieter@fedoraproject.org> - 1.1.6-1.1
- branch rebuild (qt5)

* Sat Oct 01 2016 Builder <projects.rg@smart.ms> - 1.1.6-1
- new version

* Thu Jun 09 2016 Rex Dieter <rdieter@fedoraproject.org> - 1.1.5-5
- rebuild (qtbase)

* Sat May 07 2016 Raphael Groner <projects.rg@smart.ms> - 1.1.5-4
- remove dependency to qjson, get rid of Qt4 headers
- add BR: qt5-qtbase-private-devel, tracking needed rebuilds

* Mon Feb 08 2016 Raphael Groner <projects.rg@smart.ms> - 1.1.5-3
- unretire
- add license breakdown
- add calls to ldconfig
- cleanup

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 07 2016 Parag Nemade <pnemade AT redhat DOT com> - 1.1.5-1
- Update to 1.1.5
- Drop upstream committed patch
- This package is now started using only QT5 libraries

* Wed Dec 16 2015 Parag Nemade <pnemade AT redhat DOT com> - 1.1.4-1
- Update to 1.1.4

* Wed Dec 02 2015 Parag Nemade <pnemade AT redhat DOT com> - 1.1.2-1
- Update 1.1.2
- Thanks to Rex for the unbundling patches

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.67-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.9.67-4
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.67-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.67-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May 10 2014 James Abtahi <jam3s@fedoraproject.com> 0.9.67-1
- update for the latest version
- the patch .system_libs by Rex Dieter was applied to upstream
- the patch .installationpath was replaced by .translation_path

* Wed Dec 04 2013 James Abtahi <jamescategory@gmail.com> 0.9.64-3
- install translation files in {_datadir}/{name}/translations

* Sun Dec 01 2013 James Abtahi <jamescategory@gmail.com> 0.9.64-2
- fixed a typo in description
- added {_datadir}/locale/{name}/
- added comments to patches

* Sat Nov 30 2013 James Abtahi <jamescategory@gmail.com> 0.9.64-2
- revert to {_datadir}/icons/hicolor/*/*/*

* Sat Nov 23 2013 James Abtahi <jamescategory@gmail.com> 0.9.64-2
- fixed a typo and added qtsinglecoreapplication-devel dependency
- added desktop-file-validate

* Fri Nov 22 2013 Rex Dieter <rdieter@fedoraproject.org> 0.9.64-2
- use system qtsingleapplication, qxt libraries
- use %%cmake macro

* Fri Nov 22 2013 James Abtahi <jamescategory@gmail.com> 0.9.64-1
- Added hicolor-icon-theme requirement and icon scriplets
- Added {_prefix} macro to cmake
- Removed redundant requirements
- Added VERBOSE to make
- Adding {optflags}

* Wed Nov 20 2013 James Abtahi <jamescategory@gmail.com> 0.9.64-1
- Removed extra empty lines
- Some editing in Summary and Description
- Removed rm -rf in install section
- Removed clean section
- More specific file listing for {_datadir}/icons/hicolor/*/*/*

* Sat Nov 16 2013 James Abtahi <jamescategory@gmail.com> 0.9.64-1
- Initial Build

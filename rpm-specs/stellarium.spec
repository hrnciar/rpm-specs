Name:           stellarium
Version:        0.20.2
Release:        1%{?dist}
Summary:        Photo-realistic nightsky renderer

License:        GPLv2+
URL:            http://www.stellarium.org
Source0:        https://github.com/Stellarium/stellarium/releases/download/v%{version}/stellarium-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  mesa-libGLU-devel
BuildRequires:  ImageMagick
BuildRequires:	cmake
BuildRequires:	qt5-qtbase-devel
BuildRequires:  qt5-qtdeclarative-devel
BuildRequires:	qt5-qtlocation-devel
BuildRequires:	qt5-qttools-devel
BuildRequires:	qt5-qtscript-devel
BuildRequires:	qt5-qtserialport-devel
BuildRequires:	qt5-qtmultimedia-devel
BuildRequires:	gettext-devel
BuildRequires:	boost-devel
BuildRequires:	glib2-devel
BuildRequires:	perl-podlators
BuildRequires:  libappstream-glib

%description
Stellarium is a real-time 3D photo-realistic nightsky renderer. It can
generate images of the sky as seen through the Earth's atmosphere with
more than one hundred thousand stars from the Hipparcos Catalogue,
constellations, planets, major satellites and nebulas.

%prep
%setup -q

%build
export CFLAGS="$RPM_OPT_FLAGS -fPIC"
export CXXFLAGS="$RPM_OPT_FLAGS -fPIC"
%{cmake} -DCMAKE_BUILD_TYPE=Release -DQT5_LIBS=%{_libdir}/qt5
make VERBOSE=1 %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="%{_bindir}/install -c -p"
mkdir -p $RPM_BUILD_ROOT%{_libdir}
for i in `find . -type f -name '*.so'`; do
	install -c -p $i $RPM_BUILD_ROOT%{_libdir}
done

# Remove unwanted files
rm -f $RPM_BUILD_ROOT%{_datadir}/stellarium/data/*.ttf
rm -f $RPM_BUILD_ROOT%{_datadir}/pixmaps/stellarium.xpm
rm -f $RPM_BUILD_ROOT%{_datadir}/stellarium/data/stellarium.ico

%check
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_datadir}/metainfo/stellarium.appdata.xml
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/stellarium.desktop

%files 
%license COPYING
%doc ChangeLog CREDITS.md README.md
%{_bindir}/stellarium
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/metainfo/stellarium.appdata.xml
%{_datadir}/icons/hicolor/*/apps/stellarium.png
%{_mandir}/man1/stellarium.1*
%{_datadir}/mime/packages/stellarium.xml

%ldconfig_scriptlets

%changelog
* Tue Jun 23 2020 Kalev Lember <klember@redhat.com> - 0.20.2-1
- Update to 0.20.2

* Mon Apr 20 2020 Gwyn Ciesla <gwync@protonmail.com> - 0.20.1-1
- 0.20.1

* Mon Mar 30 2020 Kalev Lember <klember@redhat.com> - 0.20.0-1
- 0.20.0
- Drop old, unused buildrequires

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Dec 22 2019 Kalev Lember <klember@redhat.com> - 0.19.3-1
- 0.19.3
- Don't replace upstream screenshots in appdata
- Use desktop-file-validate rather than desktop-file-install
- Validate appdata

* Sun Sep 29 2019 Kalev Lember <klember@redhat.com> - 0.19.2-1
- 0.19.2

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 24 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.19.1-1
- 0.19.1

* Mon Mar 25 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.19.0-1
- 0.19.0

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 15 2019 fedora-toolbox <otaylor@redhat.com> - 0.18.3-2
- Handle both compressed and uncompressed manual pages

* Wed Dec 26 2018 Gwyn Ciesla <limburgher@gmail.com> - 0.18.3-1
- 0.18.3

* Wed Aug 15 2018 Gwyn Ciesla <limburgher@gmail.com> - 0.18.2-1
- 0.18.2

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 02 2018 Gwyn Ciesla <limburgher@gmail.com> - 0.18.1-1
- 0.18.1

* Mon Mar 26 2018 Gwyn Ciesla <limburgher@gmail.com> - 0.18.0-1
- 0.18.0

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Feb 01 2018 Gwyn Ciesla <limburgher@gmail.com> - 0.17.0-2
- Fix lunar eclipse crash.

* Thu Dec 21 2017 Gwyn Ciesla <limburgher@gmail.com> - 0.17.0-1
- 0.17.0

* Mon Sep 25 2017 Gwyn Ciesla <limburgher@gmail.com> - 0.16.1-1
- 0.16.1.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 22 2017 Gwyn Ciesla <limburgher@gmail.com> - 0.16.0-1
- 0.16.0.

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Tue Mar 21 2017 Gwyn Ciesla <limburgher@gmail.com> - 0.15.2-1
- 0.15.2.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 27 2016 Jon Ciesla <limburgher@gmail.com> - 0.15.1-1
- 0.15.1.

* Mon Aug 01 2016 Jon Ciesla <limburgher@gmail.com> - 0.15.0-1
- 0.15.0.

* Sun May 22 2016 Jon Ciesla <limburgher@gmail.com> - 0.14.3-1
- 0.14.3.

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Dec 16 2015 Jon Ciesla <limburgher@gmail.com> - 0.14.1-2
- BR fix.

* Wed Dec  2 2015 Jochen Schmitt <Jochen herr-schmitt de> - 0.14.1-1
- New minor upstream update release

* Mon Nov 02 2015 Jon Ciesla <limburgher@gmail.com> - 0.14.0-1
- Latest upstream, BZ 1274980.
- Changelog date fix.
- Qt 5.5 patch upstreamed.

* Thu Oct 15 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.13.3-5
- Fix build with Qt 5.5

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13.3-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 0.13.3-3
- rebuild for Boost 1.58

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun May  3 2015 Jochen Schmitt <Jochen herr-schmitt de> - 0.13.3-1
- Ne upstream release

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.13.2-4
- Rebuilt for GCC 5 C++11 ABI change

* Mon Mar 30 2015 Richard Hughes <rhughes@redhat.com> - 0.13.2-3
- Use better AppData screenshots

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 0.13.2-2
- Rebuild for boost 1.57.0

* Thu Jan 22 2015 Jochen Schmitt <Jochen herr-schmitt de> - 0.13.2-1
- New monor bug-fixing release from upstream

* Tue Oct 21 2014 Jochen Schmitt <Jochen herr-schmitt de> - 0.13.1-1
- New upstream release
- Remove ms-no-bitfields patch

* Wed Sep 24 2014 Dan Horák <dan[at]danny.cz> - 0.13.0-3
- fix build on non-x86 arches, patch taken from Debian

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 29 2014 Jochen Schmitt <Jochen herr-schmitt de> - 0.13.0-1
- New upstream release
- Add AppData support
- Exclude armv7hl due an unsupported compiler option

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 22 2014 Petr Machata <pmachata@redhat.com> - 0.12.4-2
- Rebuild for boost 1.55.0

* Sun Sep 29 2013 Jochen Schmitt <Jochen herr-schmitt de> - 0.12.4-1
- New upstream release

* Sun Sep 15 2013 Jochen Schmitt <Jochen herr-schmitt de> - 0.12.3-1
- New upstream release
- Remove subpackage with obsoltete program documentation
- Correcting the project home page

* Sun Aug  4 2013 Jochen Schmitt <Jochen herr-schmitt de> - 0.12.2-1
- New upstream release
- Add phonon-devel as a BR

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 30 2013 Petr Machata <pmachata@redhat.com> - 0.12.1-2
- Rebuild for boost 1.54.0
- Add patch from upstream to solve a issue with pod2man

* Mon Apr 22 2013 Jochen Schmitt <Jochen herr-schmitt de> - 0.12.1-1
- New upstream release

* Tue Feb 12 2013 Jochen Schmitt <Jochen herr-schmitt de> - 0.12.0-4
- Use upstream stellarium.desktop file

* Tue Feb 12 2013 Jochen Schmitt <Jochen herr-schmitt de> - 0.12.0-3
- Remove opengl-games-utils wrapper (#910402)
- Make BR to perl-podlators conditional

* Tue Feb 12 2013 Jon Ciesla <limburgher@gmail.com> - 0.12.0-2
- Drop desktop vendor tag.

* Sun Feb  3 2013 Jochen Schmitt <Jochen herr-schmitt de> - 0.12.0-1
- New upstream release
- Clean up SPEC file
- Add perl-podlators as a BR to access pod2man

* Mon Aug 27 2012 Jochen Schmitt <JOchen her-schmitt de> - 0.11.4a-1
- New upstream release

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun  8 2012 Jochen Schmitt <s4504kr@omega.in.herr-schmitt.de> - 0.11.3-2
- Remove duplicate desktop file

* Mon Jun  4 2012 Jochen Schmitt <Jochen herr-schmitt de> 0.11.3-1
- New upstream release

* Tue Mar 13 2012 Jochen Schmitt <Jochen herr-schmitt de> 0.11.2-1
- New upstream release

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.1-3
- Rebuilt for c++ ABI breakage

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Nov  8 2011 Jochen Schmitt <Jochen herr-schmitt de> 0.11.1-1
- New upstream release

* Tue Jul  5 2011 Jochen Schmitt <Jochen herr-schmitt de> 0.11.0-1
- New upstream release

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec  6 2010 Jochen Schmitt <Jochen herr-schmitt de> 0.10.6-1
- New upstream release

* Thu Jun  3 2010 Jochen Schmitt <Jochen herr-schmitt de> 0.10.5-1
- Nrw upstream release

* Sun Mar 14 2010 Jochen Schmitt <Jochen herr-schmitt de> 0.10.4-4
- Set StartupNotify=true in desktop file

* Wed Feb 24 2010 Jochen Schmitt <Jochen herr-schmitt de> 0.10.4-3
- Remove font files

* Tue Feb 23 2010 Jochen Schmitt <Jochen herr-schmitt de> 0.10.4-2
- Fix uploaded sources

* Tue Feb 23 2010 Jochen Schmitt <Jochen herr-schmitt de> 0.10.4-1
- New upstream release

* Sun Jan 31 2010 Jochen Schmitt <Jochen herr-schmitt de> 0.10.3-1
- New upstream release (#559929)

* Wed Nov 25 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> 0.10.2-7
- Rebuild for Qt 4.6.0 RC1 in F13 (was built against Beta 1 with unstable ABI)

* Sun Nov  1 2009 Jochen Schmitt <Jochen herr-schmitt de> 0.10.2-6
- Remove symlink to font files

* Thu Sep 24 2009 Jochen Schmitt <Jochen herr-schmitt de> 0.10.2-5
- Updated program documentation (#525302)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jul  2 2009 Jochen Schmitt <Jochen herr-schmitt de> 0.10.2-3
- Rebuild for new boost release

* Tue Mar 24 2009 Jochen Schmitt <Jochen herr-schmitt de> 0.10.2-2
- Changed desktop file (#491922)

* Thu Mar 12 2009 Jochen Schmitt <Jochen herr-schmitt de> 0.10.2-1
- New upstream release

* Thu Mar  5 2009 Jochen Schmitt <Jochen herr-schmitt de> 0.10.1-4
- Support noarch subpackates

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Feb  8 2009 Jochen Schmitt <Jochen herr-schmitt de> 0.10.1-2
- New upstream release

* Sun Jan 18 2009 Jochen Schmitt <Jochen herr-schmitt de> 0.10.0-3
- Change Req. to fonts pakcage because fonts package renaming (#480474)

* Sun Jan  4 2009 Jochen Schmitt <Jochen herr-schmitt de> 0.10.0-2
- Create symlinks to DejaVu fonts (#477460)

* Wed Sep 24 2008 Jochen Schmitt <Jochen herr-schmitt de> 0.10.0-1
- New upstream release

* Sat Sep  6 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.9.1-7
- fix license tag

*  Mon Feb 11 2008 Jochen Schmitt <Jochen herr-schmitt de> 0.9.1-6
- Fix gcc-4.3 related issues

* Tue Jan 22 2008 Jochen Schmitt <Jochen herr-schmitt de> 0.9.1-1
- New upstream release

* Tue Oct 23 2007 Will Woods <wwoods@redhat.com> 0.9.0-6
- Fix opengl-game-wrapper.sh usage

* Wed Sep 26 2007 Jochen Schmitt <Jochen herr-schmitt de> 0.9.0-5
- Add usage of opengl-game-wrapper (BZ #304851)

* Thu Aug  9 2007 Jochen Schmitt <Jochen herr-schmitt de> 0.9.0-4
- Rebuild

* Tue Aug  7 2007 Jochen Schmitt <Jochen herr-schmitt de> 0.9.0-3
- Solve weakday displaying issue (#250621)

* Wed Jun 27 2007 Jochen Schmitt <Jochen herr-schmitt de> 0.9.0-2
- Change category of the desktop entry (#241440)

* Tue Jun 12 2007 Jochen Schmitt <Jochen herr-schmitt de> 0.9.0-1
- New upstream release

* Sun Dec 17 2006 Jochen Schmitt <Jochen herr-schmitt de> 0.8.2-5
- Resize icon to 32x32

* Tue Nov 14 2006 Jochen Schmitt <Jochen herr-schmitt de> 0.8.2-3
- Try to fix AMD64 problem (#210525)

* Thu Oct 19 2006 Jochen Schmitt <Jochen herr-schmitt de> 0.8.2-2
- Fix segfault on x64 systems (#210525)

* Tue Oct 10 2006 Jochen Schmitt <Jochen herr-schmitt de> 0.8.2-1
- New upstream release

* Tue Jul  4 2006 Jochen Schmitt <Jochen herr-schmitt de> 0.8.1-1
- New upstream release
- Fix demaged PDF (#197301)

* Wed May 31 2006 Jochen Schmitt <Jochen herr-schmitt de> 0.8.0-4
- Update user guide
- change dl.sf.net to prdownloads.sf.net

* Sun May  7 2006 Jochen Schmitt <Jochen herr-schmitt de> 0.8.0-3
- New upstream release

* Tue Feb 14 2006 Jochen Schmitt <Jochen herr-schmitt de> 0.7.1-7
- Add stellarium user guide as doc subpackage
- Add gcc41 patch from Diego Petteno

* Mon Feb 13 2006 Jochen Schmitt <Jochen herr-schmitt de> 0.7.1-4
- Add SDL_mixer-devel as BuildRequires:

* Sun Feb 12 2006 Jochen Schmitt <Jochen herr-schmitt de> 0.7.1-3
- Rebuilt for FC5

* Mon Oct 10 2005 Jochen Schmitt <Jochen herr-schmitt de> 0.7.1-2
- use of %%find_lang

* Sun Oct  9 2005 Jochen Schmitt <Jochen herr-schmitt de> 0.7.1-1
- New upstream release

* Thu Aug 11 2005 Jochen Schmitt <Jochen herr-schmitt de> 0.6.2-6
- Add %%{?dist} to release.

* Wed Aug 10 2005 Jochen Schmitt <Jochen herr-schmitt de> 0.6.2-5
- Fix build for GCC4.

* Thu Apr 14 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 0.6.2-4
- Fix build for GCC4.
- Fix desktop icon installation.

* Fri Apr  8 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Sun Jan 23 2005 Marius L. Jøhndal <mariuslj at ifi.uio.no> - 0:0.6.2-2
- Fixed broken patch.

* Sun Jan 16 2005 Marius L. Jøhndal <mariuslj at ifi.uio.no> - 0:0.6.2-0.fdr.1
- Updated to 0.6.2.

* Sun Oct 17 2004 Marius L. Jøhndal <mariuslj at ifi.uio.no> - 0:0.6.1-0.fdr.1
- Updated to 0.6.1.

* Sat Aug 21 2004 Marius L. Jøhndal <mariuslj at ifi.uio.no> - 0:0.6.0-0.fdr.2
- Patched to honour optflags.
- Added nvidia specific patch.

* Sat Jul 17 2004 Marius L. Jøhndal <mariuslj at ifi.uio.no> - 0:0.6.0-0.fdr.1
- Initial RPM release.

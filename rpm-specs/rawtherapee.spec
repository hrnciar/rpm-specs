%global link_tcmalloc 1

Name:           rawtherapee
Version:        5.8
Release:        2%{?dist}
Summary:        Raw image processing software

License:        GPLv3 and MIT and IJG
URL:            http://www.rawtherapee.com/
Source0:        https://github.com/Beep6581/RawTherapee/releases/download/%{version}/%{name}-%{version}.tar.xz

# Fix linking against system's KLT
# Upstream PR https://github.com/Beep6581/RawTherapee/pull/5539
Patch0:         RT_5.8_system_klt.patch

# Backport patch for fixing rhbz#1820907
Patch1:         RT_5.8_fix_crop.patch


BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  klt-devel
BuildRequires:  libappstream-glib
BuildRequires:  libatomic

BuildRequires:  pkgconfig(exiv2)
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(fftw3f)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(glibmm-2.4)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtkmm-3.0)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(lensfun)
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(libiptcdata)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(librsvg-2.0)
%if 0%{?link_tcmalloc}
BuildRequires:  pkgconfig(libtcmalloc)
%endif
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(sigc++-2.0)
BuildRequires:  pkgconfig(zlib)

Requires:       hicolor-icon-theme

# https://fedorahosted.org/fpc/ticket/530
# to find: `grep DCRAW_VERSION: rawtherapee-*/rtengine/dcraw.c`
Provides:       bundled(dcraw) = 9.27


%description
Rawtherapee is a RAW image processing software. It gives full control over
many parameters to enhance the raw picture before finally exporting it
to some common image format.

%prep
%autosetup -p1 -n %{name}-%{version}

# fix wrong line endings
sed -i "s|\r||g" LICENSE.txt

# remove bundled KLT, so we're sure to use system provided KLT
rm -rf rtengine/klt/

%build
# do not build shared libs
# https://github.com/Beep6581/RawTherapee/pull/5479
%{cmake} %{?BUILD_TESTS} \
        -DCMAKE_INSTALL_PREFIX=%{_prefix} \
        -DLIBDIR=%{_libdir} \
        -DCMAKE_BUILD_TYPE=release \
        -DBUILD_SHARED_LIBS:BOOL=OFF \
        -DAUTOMATED_BUILD_SYSTEM:BOOL=ON \
        -DCACHE_NAME_SUFFIX="" \
        -DCMAKE_CXX_FLAGS="$RPM_OPT_FLAGS" \
        -DCMAKE_C_FLAGS="$RPM_OPT_FLAGS" \
%if 0%{?link_tcmalloc}
        -DENABLE_TCMALLOC=ON \
%endif
        -DWITH_SYSTEM_KLT=ON .
        
make VERBOSE=1 %{?_smp_mflags} 


%install
make install DESTDIR=%{buildroot}


# These file are taken from the root already
rm -rf %{buildroot}/%{_datadir}/doc 


%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/com.%{name}.RawTherapee.appdata.xml


%files
%doc AUTHORS.txt LICENSE.txt RELEASE_NOTES.txt
%{_mandir}/man1/%{name}.1.gz
%{_bindir}/%{name}
%{_bindir}/%{name}-cli
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/metainfo/com.%{name}.RawTherapee.appdata.xml
%{_datadir}/icons/hicolor/*/apps/%{name}.png


%changelog
* Mon Apr 06 2020 Mattia Verga <mattia.verga@protonmail.com> - 5.8-2
- Backport patch for fixing rhbz#1820907

* Wed Feb 05 2020 Mattia Verga <mattia.verga@protonmail.com> - 5.8-1
- Release 5.8 stable
- Fix linking to system's KLT lib
- Use static libraries
- Enable linking to tcmalloc

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Sep 11 2019 Mattia Verga <mattia.verga@protonmail.com> - 5.7-1
- Release 5.7 stable
- Add forgotten klt-devel as BR

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Apr 25 2019 Mattia Verga <mattia.verga@protonmail.com> - 5.6-2
- Backport patch to fix appdata validation

* Wed Apr 24 2019 Mattia Verga <mattia.verga@protonmail.com> - 5.6-1
- Release 5.6 stable

* Sat Apr 13 2019 Mattia Verga <mattia.verga@protonmail.com> - 5.6-0.1.rc1
- Update to 5.6RC1
- Added librsvg-2.0 to BuildRequires
- Changed appdata filename

* Sat Apr 06 2019 Mattia Verga <mattia.verga@protonmail.com> - 5.5-4
- Backport patch to fix Histogram Matching (RHBZ #1692572)

* Sat Feb 16 2019 Mattia Verga <mattia.verga@protonmail.com> - 5.5-3
- Backport patch to fix build with GCC9

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Dec 21 2018 Mattia Verga <mattia.verga@protonmail.com> - 5.5-1
- Release 5.5 stable
- Add libatomic to BRs to fix x64 builds

* Tue Sep 18 2018 Owen Taylor <otaylor@redhat.com> - 5.4-3
- Don't explicitly require fftw - this pulls in unnecessary library subpackages
  and binaries; just count on RPM's standard library autodependencies.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 22 2018 Mattia Verga <mattia.verga@email.it> - 5.4-1
- Release 5.4 stable

* Wed Mar 14 2018 Mattia Verga <mattia.verga@email.it> - 5.4-0.2.rc3
- Update to 5.4RC3

* Sun Mar 04 2018 Mattia Verga <mattia.verga@email.it> - 5.4-0.1.rc2
- Update to 5.4RC2
- Report correct dcraw version in bundled statement
- Remove obsolete ld scriptlets

* Mon Feb 19 2018 Mattia Verga <mattia.verga@email.it> - 5.3-4
- Add gcc-c++ to BuildRequires

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org>
- Remove obsolete scriptlets

* Mon Oct  2 2017 Matthew Miller <mattdm@fedoraproject.org> - 5.3-1
- update to 5.3 final

* Mon Sep 25 2017 Matthew Miller <mattdm@fedoraproject.org> - 5.3-0.1
- upstream 5.3 rc1 for rawhide
- includes fix for CVE-2017-13735
- lensfun is now required (enabling new lens correction feature)
- appdata -> metainfo dir

* Sun Sep 10 2017 Mattia Verga <mattia.verga@email.it> - 5.2-2
- Backport upstream patch for fixing CVE-2017-13735

* Mon Jul 31 2017 Mattia Verga <mattia.verga@email.it> - 5.2-1
- Upgrade to 5.2
- Use system KLT library instead of bundled one
- No further requires bzip2 as BR

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu May 18 2017 Matthew Miller <mattdm@fedoraproject.org> - 5.1-1
- 5.1 final is out

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1-0.2.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Sun May 14 2017 Mattia Verga <mattia.verga@email.it> - 5.1-0.1.rc1
- Upgrade to 5.1-rc1
- New command line binary
- Removed support for gtk2

* Sat Feb 18 2017 Mattia Verga <mattia.verga@tiscali.it> - 5.0-3.r1
- Upgrade to 5.0-r1
- Fix build error with GCC7

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 23 2017 Mattia Verga <mattia.verga@tiscali.it> - 5.0-1
- Upgrade to stable 5.0-gtk3

* Sat Nov 05 2016 Mattia Verga <mattia.verga@tiscali.it> - 4.2.1234-2.20161105gitb766110
- Upgrade svn version
- Add provides klt

* Sun Oct 09 2016 Mattia Verga <mattia.verga@tiscali.it> - 4.2.1234-1.20161009gitd16d244
- Upgrade to svn version
- GTK3 is now default
- Remove unneeded patches

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed May 13 2015 Matthew Miller <mattdm@fedoraproject.org> - 4.2-10
- note dcraw bundling (see https://fedorahosted.org/fpc/ticket/530)

* Wed May 13 2015 Matthew Miller <mattdm@fedoraproject.org> - 4.2-9
- same thing, format patch correctly

* Wed May 13 2015 Matthew Miller <mattdm@fedoraproject.org> - 4.2-8
- Security fix for CVE-2015-3885 (dcraw input sanitization), bz #1221257

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 4.2-7
- Rebuilt for GCC 5 C++11 ABI change

* Tue Mar 24 2015 Matthew Miller <mattdm@fedoraproject.org> - 4.2-6
- ooh, fixed it. (insufficiently strict html in description. will
  submit bug upstream -- thanks Kalev for the fix!)

* Tue Mar 24 2015 Matthew Miller <mattdm@fedoraproject.org> - 4.2-5
- appstream validation currently failing on f22 and f23. temporarily
  disabling

* Tue Mar 24 2015 Matthew Miller <mattdm@fedoraproject.org> - 4.2-4
- oh look! fix some invalid dates in changelog including the previous entry
- move appdata validation next to desktop file validation

* Tue Mar 24 2015 Matthew Miller <mattdm@fedoraproject.org> - 4.2-3
- package appdata
- fix some invalid dates in changelog

* Tue Mar 24 2015 Matthew Miller <mattdm@fedoraproject.org> - 4.2-2
- a few config changes to match upstream rpm

* Sat Nov 08 2014 Matthew Miller <mattdm@fedoraproject.org> - 4.2-1
- update to new upstream stable release
- set cache and config dir to be unversioned by upstream request
  (see http://rawtherapee.com/blog/4.2-pre-release-announcement)
  Note that this will cause config from 4.1 to be ignored, and 
  possibly even older config to be used instead.

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Matthew Miller <mattdm@fedoraproject.org> - 4.1-1
- update to new upstream stable release (first officially-stable release
  since 3.1)
- see changelog at http://rawtherapee.com/blog/rawtherapee-4.1-is-out
- drop documentation subpackage, because upstream does not yet have a pdf
  for 4.1; see docs online at http://rawtherapee.com/blog/documentation and
  http://rawpedia.rawtherapee.com/
- no need to include COMPILE.txt in binary package, but do incliude 
  RELEASE_NOTES.txt

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jun 29 2013 Thibault North <tnorth@fedoraproject.org> - 4.0.11-1
- Update to 4.0.11

* Sun Apr 7 2013 Thibault North <tnorth@fedoraproject.org> - 4.0.10-1
- Update to 4.0.10

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 21 2013 Adam Tkac <atkac redhat com> - 4.0.9-4
- rebuild due to "jpeg8-ABI" feature drop

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 4.0.9-3
- rebuild against new libjpeg

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 22 2012 Thibault North <tnorth@fedoraproject.org> - 4.0.9-1
- Update to 4.0.9

* Sat Apr 7 2012 Thibault North <tnorth@fedoraproject.org> - 4.0.8-1
- Update to 4.0.8
- Spec cleanup
- Rebase on the online source archive

* Sun Feb 12 2012  Thibault North <tnorth@fedoraproject.org> - 4.0.7-2
- Fix faulty MIME directive

* Sat Feb 11 2012  Thibault North <tnorth@fedoraproject.org> - 4.0.7-1
- Update to 4.0.7

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Nov 27 2011  Thibault North <tnorth@fedoraproject.org> - 4.0.5-2
- Now require lcms2

* Sun Nov 27 2011  Thibault North <tnorth@fedoraproject.org> - 4.0.5-1
- Upgrade to release 4.0.5

* Thu Aug 18 2011 Thibault North <tnorth@fedoraproject.org> - 3.0.0-1
- Upgrade to stable release 3.0.0

* Tue Jul 12 2011 Thibault North <tnorth@fedoraproject.org> - 3.0-0.31.a1
- Fix .desktop file to properly run rawtherapee

* Sun Jul 10 2011 Thibault North <tnorth@fedoraproject.org> - 3.0-0.30.a1
- Sync with upstream for many fixes and improvements
- Executable is now rawtherapee instead of rt (see BZ#715390)

* Mon Jun 6 2011  Thibault North <tnorth@fedoraproject.org> - 3.0-0.29.a1
- Sync with upstream
- Versioning now needs to be included in version.h 

* Sun Mar 20 2011 Thibault North <tnorth@fedoraproject.org> - 3.0-0.28.a1
- Updated to 3.0A2, distance 13 for many fixes
- Updated spec file thanks to upstream fixes

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-0.28.a1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 3 2011 Thibault North <tnorth@fedoraproject.org> - 3.0-0.27.a1
- Sync with upstream for various bugfixes and enhancements

* Sun Dec 19 2010 Thibault North <tnorth@fedoraproject.org> - 3.0-0.26.a1
- Sync with branch_3.0 upstream: rawtherapee has a stable branch now.

* Sat Nov 6 2010 Dan Horák <dan[at]danny.cz> - 3.0-0.25.a1
- Fix libdir for 64-bit architectures
- Fix ownership of the /usr/share/rawtherapee directory

* Mon Oct 25 2010 Thibault North <tnorth@fedoraproject.org> - 3.0-0.24.a1
- Sync with upstream for many enhancements and fixes

* Thu Sep 9 2010 Thibault North <tnorth@fedoraproject.org> - 3.0-0.23.a1
- Sync with upstream back to the official repository
- Various fixes and enhancements

* Thu May 27 2010 Thibault North <tnorth@fedoraproject.org> - 3.0-0.22.a1
- Sync upstream for OpenMP support

* Tue May 11 2010 Thibault North <tnorth@fedoraproject.org> - 3.0-0.21.a1
- Sync with upstream rev ccc12f4a03
- Segfault fix
- Various fixes/enhancements

* Tue Apr 27 2010 Thibault North <tnorth@fedoraproject.org> - 3.0-0.20.a1
- Fix compilation for 64 bits OSes

* Tue Apr 27 2010 Thibault North <tnorth@fedoraproject.org> - 3.0-0.19.a1
- Switch back to Rawtherapee original release
- Bug fixes
- Translations and themes now have a licence and can be used
- Hide information on pictures by default

* Fri Apr 16 2010 Thibault North <tnorth@fedoraproject.org> - 3.0-0.18.a1
- New release including curves (exposure and luminance)

* Fri Apr 16 2010 Thibault North <tnorth@fedoraproject.org> - 3.0-0.17.a1
- Sync with upstream: multiple fixes

* Mon Apr 12 2010 Thibault North <tnorth@fedoraproject.org> - 3.0-0.16.a1
- Sync with upstream for new resizing algorithms
- File renames

* Thu Apr 8 2010 Thibault North <tnorth@fedoraproject.org> - 3.0-0.15.a1
- Sync with upstream for new demosaicing algorithms
- Fix segfault

* Tue Mar 23 2010 Thibault North <tnorth@fedoraproject.org> - 3.0-0.14.a1
- Remove sed liners which have been pushed upstream

* Tue Mar 23 2010 Thibault North <tnorth@fedoraproject.org> - 3.0-0.13.a1
- Fix CMakeLists to build without extra languages and themes
- Remove PDF docs : development-related or outdated

* Tue Mar 23 2010 Thibault North <tnorth@fedoraproject.org> - 3.0-0.12.a1
- Now rely on RawTherapee-Fork, new upstream

* Sat Mar 20 2010 Sebastian Dziallas <sebastian@when.com> - 3.0-0.11.a1
- Correct path in .desktop file

* Wed Mar 17 2010 Thibault North <tnorth@fedoraproject.org> - 3.0-0.10.a1
- Run ldconfig at post/postun

* Mon Mar 15 2010 Thibault North <tnorth@fedoraproject.org> - 3.0-0.9.a1
- Use proper license tag
- Remove some files with different licensing

* Wed Mar 3 2010 Thibault North <tnorth@fedoraproject.org> - 3.0-0.8.a1
- Various fixes related to review request.

* Sun Feb 28 2010 Thibault North <tnorth@fedoraproject.org> - 3.0-0.7.a1
- Update icon database on install/removal
- Fix many files permissions (thanks Sebastian Dziallas)

* Sun Feb 28 2010 Thibault North <tnorth@fedoraproject.org> - 3.0-0.6.a1
- Set icons for desktop file
- Remove rawzor from SRPM

* Sun Feb 28 2010 Thibault North <tnorth@fedoraproject.org> - 3.0-0.5.a1
- More fixes and added desktop file

* Wed Feb 24 2010 Sebastian Dziallas <sebastian@when.com> - 3.0-0.4.a1
- Smaller modifications and changes

* Sun Jan 24 2010 Sebastian Dziallas <sebastian@when.com> - 3.0-0.3.a1
- Switch to a1 SVN checkout

* Sun Jan 24 2010 Thibault North <tnorth@fedoraproject.org> - 3.0-0.2.a1
- Various Fixes

* Fri Jan 22 2010 Thibault North <tnorth@fedoraproject.org> - 3.0-0.1.a1
- Initial package

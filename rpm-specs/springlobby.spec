# Colorize terminal output. Helps to find problems during build process.
%global optflags %{optflags} -fdiagnostics-color=always

Name:           springlobby
Version:        0.269
Release:        1%{?dist}
Summary:        Free cross-platform lobby client for the Spring RTS project

# License clarification: http://springlobby.info/issues/show/810
License:        GPLv2
URL:            https://springlobby.springrts.com/
Source0:        https://springlobby.springrts.com/dl/stable/springlobby-%{version}.tar.bz2
ExclusiveArch:  %{ix86} x86_64

# Build fails with new GCC 10
# * https://github.com/springlobby/springlobby/issues/951
Patch0:         https://github.com/springlobby/springlobby/pull/958.patch#/gcc10.patch

BuildRequires:  alure-devel
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  dumb-devel
BuildRequires:  gcc-c++ >= 8
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  libcurl-devel
BuildRequires:  libnotify-devel
BuildRequires:  minizip-compat-devel
BuildRequires:  ninja-build
BuildRequires:  openal-devel
BuildRequires:  rb_libtorrent-devel
BuildRequires:  SDL_mixer-devel
BuildRequires:  SDL_sound-devel
BuildRequires:  SDL-devel
BuildRequires:  wxGTK3-devel

# https://github.com/springlobby/springlobby/issues/709
BuildRequires:  jsoncpp-devel

Requires:       hicolor-icon-theme
Requires:       mesa-libGLU%{?_isa}

Recommends:     fluidsynth-libs%{?_isa}
Recommends:     spring%{?_isa}

# There are other "lobbies" for spring, make a virtual-provides
Provides:       spring-lobby = %{version}-%{release}

%description
SpringLobby is a free cross-platform lobby client for the Spring RTS project.


%prep
%autosetup -p1
mkdir -p %{_target_platform}

# Unbunle libs
rm -rf \
    src/downloader/lib/src/lib/minizip


%build
pushd %{_target_platform}
%cmake \
    -G Ninja \
    ..
popd
%ninja_build -C %{_target_platform}


%install
%ninja_install -C %{_target_platform}
%find_lang %{name}
rm -rf %{buildroot}%{_docdir}/%{name}/COPYING


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files -f %{name}.lang
%license COPYING
%doc ChangeLog
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/scalable/apps/*.svg
%{_docdir}/%{name}/
%{_metainfodir}/*.xml


%changelog
* Wed Jun 03 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.269-1
- Update to 0.269
- Fix compilation with GCC 10 | GH-951
- Unbundle 'minizip'
- Add new BR: jsoncpp-devel, libnotify-devel, minizip-compat-devel, ninja-build
- Add new weak dep: fluidsynth-libs
- Add AppStream data and desktop file validation
- Update URL and sources link, now using HTTPS
- Replace tabs with spaces
- Switch to Ninja build
- SPEC file optimizations

* Fri May 29 2020 Jonathan Wakely <jwakely@redhat.com> - 0.267-7
- Rebuilt for Boost 1.73

* Tue Apr 07 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.267-6
- Add dependency 'mesa-libGLU'

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.267-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 14 2019 Jeff Law <law@redhat.com> - 0.267-4
- Fix missing #include for gcc-10

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.267-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.267-2
- Update to 0.267
- Spec file update and fixes

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.195-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 29 2018 Scott Talbert <swt@techie.net> - 0.195-17
- Rebuild with wxWidgets 3.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.195-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.195-15
- Escape macros in %%changelog

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.195-14
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.195-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.195-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 21 2017 Kalev Lember <klember@redhat.com> - 0.195-11
- Rebuilt for Boost 1.64

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.195-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.195-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 19 2016 Jonathan Wakely <jwakely@redhat.com> - 0.195-8
- Rebuilt for Boost 1.60

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 0.195-7
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.195-6
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 0.195-5
- rebuild for Boost 1.58

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.195-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.195-3
- Rebuilt for GCC 5 C++11 ABI change

* Wed Apr 08 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.195-2
- Update to 0.195 (Merger from f20).
- Fix FTBFS.
- spec-file cleanup.
- Drop springlobby-dso.patch, springlobby-gtkfix.patch.

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 0.169-12
- Add an AppData file for the software center

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.169-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.169-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 David Tardon <dtardon@redhat.com> - 0.169-9
- rebuild for boost 1.55.0

* Wed Dec 04 2013 Gilboa Davara <gilboad [AT] gmail [DOT] com> - 0.169-8
- ExclusiveArch should use %%ix86 x86_64 instead of i386 x86_64 (#1036567).

* Wed Nov 20 2013 Gilboa Davara <gilboad [AT] gmail [DOT] com> - 0.169-7
- Switch to ExclusiveArch.

* Mon Nov 18 2013 Gilboa Davara <gilboad [AT] gmail [DOT] com> - 0.169-6
- Exclude ARM.
- Missing dependencies added (#1000755).
- Changelog date cleanup.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.169-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 28 2013 Petr Machata <pmachata@redhat.com> - 0.169-4
- Rebuild for boost 1.54.0

* Thu Apr 25 2013 Gilboa Davara <gilboad [AT] gmail [DOT] com> - 0.169-3
- Fix package breakage due to %%libdir pulling debug symbols.

* Sat Apr 06 2013 Gilboa Davara <gilboad [AT] gmail [DOT] com> - 0.169-2
- Fix missing libraries.

* Mon Apr 01 2013 Gilboa Davara <gilboad [AT] gmail [DOT] com> - 0.169-1
- Version 0.169, major spring/springlobby upstream release.
- Fix #921690.
- GTK2 patch dropped.

* Sun Feb 24 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 0.147-4
- Rebuild for rb_libtorrent soname bump
- Clean up spec to follow current guidelines

* Sat Feb 09 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 0.147-3
- Rebuild for Boost-1.53.0

* Sun Feb 03 2013 Kevin Fenzi <kevin@scrye.com> - 0.147-2
- Rebuild for broken deps in rawhide

* Fri Jun 15 2012 Gilboa Davara <gilboad [AT] gmail [DOT] com> - 0.147-1
- Version 0.147 (Large number of fixes).

* Fri Mar 16 2012 Gilboa Davara <gilboad [AT] gmail [DOT] com> - 0.144-1
- Version 0.144 (Large number of fixes).

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.139-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Nov 07 2011 Gilboa Davara <gilboad [AT] gmail [DOT] com> - 0.139-1
- Version 0.139 (Large number of fixes).

* Mon Aug 22 2011 Gilboa Davara <gilboad [AT] gmail [DOT] com> - 0.136-1
- Version 0.136 (Large number of fixes).

* Wed May 18 2011 Gilboa Davara <gilboad [AT] gmail [DOT] com> - 0.131-1
- Version 0.131 (Large number of fixes).

* Thu Mar 31 2011 Gilboa Davara <gilboad [AT] gmail [DOT] com> - 0.128-1
- Version 0.128 (Large number of fixes).
- libnotify patched dropped, handled up-stream.

* Thu Mar 10 2011 Gilboa Davara <gilboad [AT] gmail [DOT] com> - 0.124-1
- Version 0.124 (Large number of fixes).

* Mon Feb 14 2011 Leigh Scott <leigh123linux@googlemail.com> - 0.120-3
- specify boost_filesystem version
- patch for libnotify changes

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.120-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jan 11 2011 Gilboa Davara <gilboad [at] gmail [dot] com> - 0.120-1
- BT download broken by new spring release.

* Fri Dec 17 2010 Gilboa Davara <gilboad [at] gmail [dot] com> - 0.118-1
- version 0.118 (w/ GTK fix)
- BT download should work now.

* Thu Nov 18 2010 Gilboa Davara <gilboad [at] gmail [dot] com> - 0.116-1
- version 0.116 (w/ GTK fix)

* Wed Sep 29 2010 jkeating - 0.101-2
- Rebuilt for gcc bug 634757

* Wed Sep 15 2010 Aurelien Bompard <abompard@fedoraproject.org> - 0.101-1
- version 0.101

* Mon Aug 16 2010 Aurelien Bompard <abompard@fedoraproject.org> - 0.80-2
- version 0.95

* Wed Jul 14 2010 Dan Horák <dan@danny.cz> - 0.80-2
- rebuilt against wxGTK-2.8.11-2

* Mon May 10 2010 Aurelien Bompard <abompard@fedoraproject.org> - 0.80-1
- version 0.80

* Tue May 04 2010 Aurelien Bompard <abompard@fedoraproject.org> - 0.79-1
- version 0.79
- add patch to fix DSO linking
    (http://fedoraproject.org/wiki/UnderstandingDSOLinkChange)

* Sun May 02 2010 Aurelien Bompard <abompard@fedoraproject.org> - 0.78-1
- version 0.78

* Sun Mar 21 2010 Aurelien Bompard <abompard@fedoraproject.org> - 0.63-1
- version 0.63

* Sun Jan 31 2010 Aurelien Bompard <abompard@fedoraproject.org> - 0.61-2
- missing BR: openal-devel

* Sun Jan 31 2010 Aurelien Bompard <abompard@fedoraproject.org> - 0.61-1
- version 0.61

* Sat Jan 23 2010 Caolán McNamara <caolanm@redhat.com> - 0.40-2
- rebuild for boost

* Sun Dec 06 2009 Aurelien Bompard <abompard@fedoraproject.org> - 0.40-1
- version 0.40

* Mon Nov 09 2009 Aurelien Bompard <abompard@fedoraproject.org> - 0.35-1
- version 0.35

* Sun Oct 11 2009 Aurelien Bompard <abompard@fedoraproject.org> - 0.27-1
- version 0.27

* Mon Sep 14 2009 Aurelien Bompard <abompard@fedoraproject.org> - 0.23-1
- version 0.23

* Wed Sep 09 2009 Aurelien Bompard <abompard@fedoraproject.org> - 0.22-1
- version 0.22

* Thu Aug 27 2009 Tomas Mraz <tmraz@redhat.com> - 0.19-2
- rebuilt with new openssl

* Sun Aug 23 2009 Aurelien Bompard <abompard@fedoraproject.org> - 0.19-1
- version 0.19

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jul 18 2009 Aurelien Bompard <abompard@fedoraproject.org> 0.3
- version 0.3

* Fri May 22 2009 Aurelien Bompard <abompard@fedoraproject.org> 0.0.1.10461-1
- version 10461
- drop patch0 (merged upstream)

* Sun May 10 2009 Aurelien Bompard <abompard@fedoraproject.org> 0.0.1.10425-5
- rebuild

* Tue Apr 28 2009 Aurelien Bompard <abompard@fedoraproject.org> 0.0.1.10425-4
- rebuild

* Sun Mar 29 2009 Aurelien Bompard <abompard@fedoraproject.org> 0.0.1.10425-3
- add patch for gcc 4.4

* Sat Mar 28 2009 Aurelien Bompard <abompard@fedoraproject.org> 0.0.1.10425-2
- rebuild

* Sun Mar 22 2009 Aurelien Bompard <abompard@fedoraproject.org> 0.0.1.10425-1
- revert to 10425

* Mon Mar 16 2009 Aurelien Bompard <abompard@fedoraproject.org> 0.0.1.10429-4
- fix license tag

* Mon Mar 16 2009 Aurelien Bompard <abompard@fedoraproject.org> 0.0.1.10429-3
- new scriptlets for the icon cache
- require hicolor-icon-theme

* Sun Mar 15 2009 Aurelien Bompard <abompard@fedoraproject.org> 0.0.1.10429-2
- drop the version in the buildrequires
- don't package ChangeLog as %%doc

* Sun Mar 15 2009 Aurelien Bompard <abompard@fedoraproject.org> 0.0.1.10429-1
- version 10429

* Wed Feb 25 2009 Aurelien Bompard <abompard@fedoraproject.org> 0.0.1.10425-1
- version 10425
- drop both patches (merged upstream)

* Tue Feb 03 2009 Aurelien Bompard <abompard@fedoraproject.org> 0.0.1.10393-1
- version 10393
- add patch to detect libunitsync.so properly
- drop workaround for rhbz#478589
- require spring
- add patch to fix gettext detection on x86_64

* Sat Jan 17 2009 Aurelien Bompard <abompard@fedoraproject.org> 0.0.1.10387-1
- version 10387
- remove vendor from the desktop file

* Thu Jan 01 2009 Aurelien Bompard <abompard@fedoraproject.org> 0.0.1.10372-1
- initial package

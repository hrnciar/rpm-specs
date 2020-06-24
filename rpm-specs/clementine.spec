%global commit          edb8c3b4ed8f976c62f4b182f8f77a4d23bf9d33
%global snapshotdate    20200617
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           clementine
Version:        1.4.0
Release:        1.rc1.%{snapshotdate}git%{shortcommit}%{?dist}.1
Summary:        A music player and library organizer

License:        GPLv3+ and GPLv2+
URL:            https://www.clementine-player.org/
Source0:        https://github.com/clementine-player/Clementine/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

Patch4:         clementine-udisks-headers.patch
# Workaround for crash RHBZ#1566807
# Upstream: https://github.com/clementine-player/Clementine/issues/6042
# until we have a better fix...
Patch5:         clementine-lastscope-size.patch
# fix compiler flag handling in gst/moodbar, upstreamable --rex
Patch6:         clementine-moodbar_flags.patch
# Use qt5 libraries (qtiocompressor)
Patch11:        clementine-qt5-libraries.patch
# Remove default shortcuts because of it steals focus when using GNOME
# https://github.com/clementine-player/Clementine/issues/6191
# https://bugzilla.redhat.com/show_bug.cgi?id=1643937
Patch13:        0001-Remove-default-shortcuts.patch

BuildConflicts: pkgconfig(gmock) >= 1.6
BuildConflicts: pkgconfig(gtest)
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  liblastfm-qt5-devel
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(cryptopp)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-app-1.0)
BuildRequires:  pkgconfig(gstreamer-audio-1.0)
BuildRequires:  pkgconfig(gstreamer-base-1.0)
BuildRequires:  pkgconfig(gstreamer-tag-1.0)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(libcdio)
BuildRequires:  pkgconfig(libchromaprint)
BuildRequires:  pkgconfig(libmtp)
BuildRequires:  pkgconfig(libmygpo-qt5)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libplist-2.0)
BuildRequires:  pkgconfig(libprojectM) >= 2.0.1-7
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libsparsehash)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(protobuf)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(QxtCore-qt5)
BuildRequires:  pkgconfig(sqlite3) >= 3.7
BuildRequires:  pkgconfig(taglib) >= 1.11
BuildRequires:  pkgconfig(udisks)
BuildRequires:  qt5-linguist
BuildRequires:  qtiocompressor-devel
BuildRequires:  qtsingleapplication-qt5-devel >= 2.6.1-2
BuildRequires:  qtsinglecoreapplication-qt5-devel
BuildRequires:  sha2-devel
%ifnarch s390 s390x
BuildRequires:  pkgconfig(libgpod-1.0)
BuildRequires:  pkgconfig(libimobiledevice-1.0)
%endif

Requires:       gstreamer1-plugins-good
Requires:       hicolor-icon-theme
Requires:       qtiocompressor >= 2.3.1-17

%description
Clementine is a multi-platform music player. It is inspired by Amarok 1.4,
focusing on a fast and easy-to-use interface for searching and playing your
music.


%prep
%autosetup -p1 -n Clementine-%{commit}

# Remove most 3rdparty libraries
# Unbundle taglib next release:
# https://github.com/taglib/taglib/issues/837#issuecomment-428389347
mv 3rdparty/{gmock,qocoa,qsqlite,taglib,utf8-cpp}/ .
rm -fr 3rdparty/*
mv {gmock,qocoa,qsqlite,taglib,utf8-cpp}/ 3rdparty/


%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake} \
  -DBUILD_WERROR:BOOL=OFF \
  -DCMAKE_BUILD_TYPE:STRING=Release \
  -DUSE_SYSTEM_QTSINGLEAPPLICATION=1 \
  -DUSE_SYSTEM_PROJECTM=1 \
  -DUSE_SYSTEM_QXT=1 \
  ..
popd

%make_build -C %{_target_platform}


%install
make install DESTDIR=%{buildroot} -C %{_target_platform}


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/clementine.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/clementine.appdata.xml


%files
%license COPYING
%doc Changelog
%{_bindir}/clementine
%{_bindir}/clementine-tagreader
%{_metainfodir}/clementine.appdata.xml
%{_datadir}/applications/clementine.desktop
%{_datadir}/icons/hicolor/*/apps/clementine.*
%{_datadir}/kservices5/clementine-*.protocol


%changelog
* Sun Jun 21 2020 Adrian Reber <adrian@lisas.de> - 1.4.0-1.rc1.20200617gitedb8c3b.1
- Rebuilt for protobuf 3.12

* Wed Jun 17 15:33:41 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.4.0-1.rc1.20200717gitedb8c3b
- Update to 1.4.0 rc1, commit edb8c3b4ed8f976c62f4b182f8f77a4d23bf9d33

* Mon Mar 30 2020 Adrian Reber <adrian@lisas.de> - 1.3.1-41.20181130gitd260c8b
- Rebuilt for libcdio-2.1.0

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-40.20181130gitd260c8b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 19 2019 Orion Poplawski <orion@nwra.com> - 1.3.1-39.20181130gitd260c8b
- Rebuild for protobuf 3.11

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-38.20181130gitd260c8b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 03 23:14:14 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.3.1-37.20181130gitd260c8b
- Rebuilt for new gstreamer

* Tue Mar 26 19:42:01 CET 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.3.1-36.20181130gitd260c8b
- Rebuilt for new projectM

* Thu Feb 28 2019 Nicolas Chauvet <kwizart@gmail.com> - 1.3.1-35.20181130gitd260c8b
- Rebuilt for cryptopp

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-34.20181130gitd260c8b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Nov 30 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.3.1-33.20181130gitd260c8b
- Bump to qt5 branch. commit d260c8b6d8c876280f8ac883870916bdf4b64df5

* Wed Nov 21 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.3.1-32.20181116gitb8eea8c
- Rebuild for protobuf 3.6

* Fri Nov 16 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.3.1-30.20181116gitb8eea8c
- Bump to qt5 branch. commit b8eea8ccc116388b67e4b042a5b81e87bf7a24e5

* Sat Oct 20 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.3.1-30.20181020gitfb00835
- Bump to qt5 branch. commit fb00835468295925a6945a286406a2eec6bdb67a

* Thu Oct 18 2018 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 1.3.1-29
- Fix a crash on a system that doesn't define XDG_CURRENT_DESKTOP. RHBZ#1639901

* Sat Sep 29 2018 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 1.3.1-28
- Disable systray on Gnome. RHBZ#1517748

* Thu Sep 06 2018 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 1.3.1-27
- Improvement on the previous patch. Fixes RHBZ#1624618

* Mon Aug 13 2018 Nicolas Chauvet <kwizart@gmail.com> - 1.3.1-26
- Rebuilt for cryptopp 7.0.0

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun May 13 2018 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 1.3.1-24
- Workaround for the analyzer crash RHBZ#1566807 until we have a better fix

* Tue Apr 10 2018 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 1.3.1-23
- Backported cryptopp >= 6.0.0 build fix

* Tue Apr 10 2018 Rex Dieter <rdieter@fedoraproject.org> 1.3.1-22
- rebuild (cryptopp)
- use %%make_build, workaround FTBFS on f28+

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Feb 01 2018 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 1.3.1-20
- fix crash on exit RHBZ#1533019

* Wed Jan 31 2018 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 1.3-1.19
- Backported fix for crash on search in spotify library tab RHBZ#1540663

* Thu Jan 25 2018 Adrian Reber <adrian@lisas.de> - 1.3-1.18
- Rebuilt for libcdio-2.0.0

* Sat Jan 20 2018 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 1.3-1.17
- support for chromaprint-1.4+

* Sun Jan 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.3.1-16
- Remove obsolete scriptlets

* Tue Jan 02 2018 Jan Grulich <jgrulich@redhat.com> - 1.3.1-15
- Reduce some CPU load

* Wed Nov 29 2017 Igor Gnatenko <ignatenko@redhat.com> - 1.3.1-14
- Rebuild for protobuf 3.5

* Mon Nov 13 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.3.1-13
- Rebuild for protobuf 3.4

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 03 2017 Jonathan Wakely <jwakely@redhat.com> - 1.3.1-10
- Rebuilt for Boost 1.64

* Tue Jun 13 2017 Orion Poplawski <orion@cora.nwra.com> - 1.3.1-9
- Rebuild for protobuf 3.3.1

* Fri Feb 17 2017 Jonathan Wakely <jwakely@redhat.com> - 1.3.1-8
- Add patch to fix build with GCC 7

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 1.3.1-7
- Rebuilt for Boost 1.63

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 1.3.1-6
- Rebuilt for Boost 1.63

* Mon Jan 23 2017 Orion Poplawski <orion@cora.nwra.com> - 1.3.1-5
- Rebuild for protobuf 3.2.0

* Sat Nov 19 2016 Orion Poplawski <orion@cora.nwra.com> - 1.3.1-4
- Fix URL, Source URL
- Use %%license

* Sat Nov 19 2016 Orion Poplawski <orion@cora.nwra.com> - 1.3.1-4
- Rebuild for protobuf 3.1.0

* Mon Nov 14 2016 Adrian Reber <adrian@lisas.de> 1.3.1-3
- rebuild (libcdio)

* Tue May 31 2016 Jan Grulich <jgrulich@redhat.com> - 1.3.1-2
- Enable fts3 tokinizers at runtime
  Resolves: bz#1323540

* Wed Apr 20 2016 Jan Grulich <jgrulich@redhat.com> - 1.3.1-1
- Update to 1.3.1

* Mon Mar 21 2016 Jan Grulich <jgrulich@redhat.com> - 1.3.0-0.4.rc1
- Rebuild for libprojectM

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-0.3.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 14 2016 Jonathan Wakely <jwakely@redhat.com> - 1.3.0-0.2.rc1
- Rebuilt for Boost 1.60

* Thu Jan 07 2016 Jan Grulich <jgrulich@redhat.com> - 1.3.0-0.1rc1
- Update to 1.3.0rc1

* Tue Dec 01 2015 Jan Grulich <jgrulich@redhat.com> - 1.2.3-14
- Requires: gstreamer-plugins-good

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 1.2.3-13
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-12
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 1.2.3-11
- rebuild for Boost 1.58

* Wed Jul 15 2015 Jan Grulich <jgrulich@redhat.com> - 1.2.3-10
- Rebuild (qtsingleapplication, qtsinglecoreapplication)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 04 2015 Rex Dieter <rdieter@fedoraproject.org> 1.2.3-8
- fix gst/moodbar compiler flags, simplify qca2 build dep

* Wed Apr 29 2015 Kalev Lember <kalevlember@gmail.com> - 1.2.3-7
- Rebuilt for protobuf soname bump

* Mon Apr 27 2015 Jan Grulich <jgrulich@redhat.com> - 1.2.3-6
- Rebuild for protobuf 2.6.1

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 1.2.3-5
- Rebuild for boost 1.57.0

* Tue Nov 18 2014 Rex Dieter <rdieter@fedoraproject.org> 1.2.3-4
- rebuild (libechonest)

* Wed Nov 12 2014 Adrian Reber <adrian@lisas.de> 1.2.3-3
- rebuild (libcdio)

* Wed Nov 05 2014 Rex Dieter <rdieter@fedoraproject.org> 1.2.3-2
- rebuild (libechonest)

* Mon Sep 22 2014 Jan Grulich <jgrulich@redhat.com> - 1.2.3-1
- 1.2.3

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jun 09 2014 Jan Grulich <jgrulich@redhat.com> - 1.2.1-4
- Do not generate namespace headers for udisks

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 22 2014 Petr Machata <pmachata@redhat.com> - 1.2.1-2
- Rebuild for boost 1.55.0

* Fri Jan 03 2014 Rex Dieter <rdieter@fedoraproject.org> 1.2.1-1
- 1.2.1

* Tue Dec 17 2013 Adrian Reber <adrian@lisas.de> 1.1.1-10
- rebuild (libcdio)

* Wed Sep 04 2013 Rex Dieter <rdieter@fedoraproject.org> 1.1.1-9
- fix .desktop categories (+Audio)
- clementine - excessive debug output (#1001595)
- drop Requires: libtaginfo (not needed or used afaict)
- drop Requires: libprojectM, qtsingleapplication
- allow bundled gmock(1.5), not compat with 1.6 (yet)
- restore parallel builds

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 30 2013 Petr Machata <pmachata@redhat.com> - 1.1.1-7
- Rebuild for boost 1.54.0

* Tue Jun 11 2013 Rex Dieter <rdieter@fedoraproject.org> 1.1.1-6
- BR: taglib-devel >= 1.8

* Wed May 29 2013 Luis Bazan <lbazan@fedoraproject.org> 1.1.1-5
- rebuild (libtaginfo)

* Wed May 22 2013 Rex Dieter <rdieter@fedoraproject.org> 1.1.1-4
- rebuild (libechonest)

* Tue Apr 23 2013 Tom Callaway <spot@fedoraproject.org> - 1.1.1-3
- fix compile against new libimobiledevice

* Wed Mar 20 2013 Peter Robinson <pbrobinson@fedoraproject.org> 1.1.1-2
- Rebuild for new libimobiledevice

* Sun Feb 24 2013 Orion Poplawski <orion@cora.nwra.com> - 1.1.1-1
- Update to 1.1.1
- Rebase desktop patch
- Drop system-sha2, fresh-start, fix-albumcoverfetch-crash, imobiledevice, and
  liblastfm1-compatibility patches fixed upstream
- Add mygpo patch to use system mygpo-qt library
- Use bundled qocoa library for now
- Add BR on fftw-devel and sparsehash-devel
- Drop BR on notification-daemon, not used and being dropped from Fedora

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jan 13 2013 Rex Dieter <rdieter@fedoraproject.org> 1.0.1-15
- -DBUILD_WERROR=OFF

* Mon Jan 07 2013 Adrian Reber <adrian@lisas.de> 1.0.1-14
- rebuild (libcdio)

* Sat Nov 24 2012 Rex Dieter <rdieter@fedoraproject.org> 1.0.1-13
- rebuild (qjson)

* Sat Jul 28 2012 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 1.0.1-12
- Rebuild on F-18 against new boost

* Thu Jul 26 2012 Rex Dieter <rdieter@fedoraproject.org> 1.0.1-11
- rebuild (libechonest)

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jul 08 2012 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 1.0.1-9
- Disable plasmarunner plugin as it was unstable. Upstream removed it from trunk

* Tue Jul 03 2012 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 1.0.1-8
- liblastfm1 compatibility fix

* Tue Jul 03 2012 Rex Dieter <rdieter@fedoraproject.org> 1.0.1-7
- rebuild (liblastfm)

* Tue Jun 05 2012 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 1.0.1-6
- Add Requires: qca-ossl RHBZ#826723

* Sat Apr 21 2012 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 1.0.1-5
- Rebuild for new libimobiledevice and usbmuxd one more time on F-18

* Thu Apr 12 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 1.0.1-4
- Rebuild for new libimobiledevice and usbmuxd

* Sun Feb 26 2012 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 1.0.1-3
- Fix a possible crash when an album cover search times out RHBZ#797451

* Tue Feb 07 2012 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 1.0.1-2
- Re-add the fresh start patch. Looks like it didn't make it to 1.0.1
- Include plasma addon only in F-17+

* Thu Feb 02 2012 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 1.0.1-1
- New upstream release RHBZ#772175

* Thu Jan 12 2012 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 0.7.1-6
- Fix startup on a fresh install RHBZ#773547
- Some specfile clean-ups

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jan 10 2012 Rex Dieter <rdieter@fedoraproject.org> 0.7.1-4.1
- rebuild (libechonest)

* Tue Nov 29 2011 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 0.7.1-4
- Lastfm login fix RHBZ#757280
- Patches for building against newer glibmm24 and glib2

* Mon Oct 10 2011 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 0.7.1-3
- Rebuild for libechonest soname bump.

* Sat Jun 11 2011 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 0.7.1-2
- Rebuild due to libmtp soname bump. Was this announced?

* Thu Mar 31 2011 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 0.7.1-1
- New upstream release
- Drop upstreamed patch

* Thu Mar 31 2011 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 0.7-2
- gcc-4.6 fix

* Wed Mar 30 2011 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 0.7-1
- New upstream version
- Drop all upstreamed patches

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 27 2010 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 0.6-2
- Rebuilt against new libimobiledevice on F-15

* Thu Dec 23 2010 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 0.6-1
- New upstream version

* Thu Oct 14 2010 Dan Horák <dan[at]danny.cz> - 0.5.3-2
- Update BRs for s390(x)

* Wed Sep 29 2010 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 0.5.3-1
- New upstream version

* Sun Sep 26 2010 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 0.5.2-1
- New upstream version

* Wed Sep 22 2010 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 0.5.1-1
- New upstream version
- Drop all upstreamed patches

* Sun Aug 08 2010 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 0.4.2-9
- Only create the OpenGL graphics context when you first open the visualisations
  window. Fixes RHBZ#621913

* Fri Aug 06 2010 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 0.4.2-8
- Enforce Fedora compilation flags

* Thu Aug 05 2010 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 0.4.2-7
- Fix crash on lastfm tree RHBZ#618474

* Tue Jul 27 2010 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 0.4.2-6
- Rebuild against new boost on F-14

* Fri Jul 23 2010 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 0.4.2-5
- Add missing scriptlets

* Wed Jul 21 2010 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 0.4.2-4
- Use: make VERBOSE=1
- License is GPLv3+ and GPLv2+
- Put BRs in alphabetical order
- Remove redundant BRs: glew-devel, xine-lib-devel, and
  the extra libprojectM-devel
- Add R: hicolor-icon-theme

* Sun Jul 18 2010 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 0.4.2-3
- Better qxt split patch

* Sat Jul 17 2010 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 0.4.2-2
- Fix font paths issue, which caused a segfault on visualizations

* Sat Jul 17 2010 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 0.4.2-1
- Version 0.4.2

* Fri May 07 2010 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 0.3-1
- Version 0.3

* Sat Apr 17 2010 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 0.2-2
- Patch out the external libraries
- Build the libclementine_lib into the final executable

* Sat Mar 27 2010 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 0.2-1
- Fedorized the upstream specfile

* Mon Mar 22 2010 David Sansome <me@davidsansome.com> - 0.2
- Version 0.2

* Sun Feb 21 2010 David Sansome <me@davidsansome.com> - 0.1-5
- Various last-minute bugfixes

* Sun Jan 17 2010 David Sansome <me@davidsansome.com> - 0.1-1
- Initial package

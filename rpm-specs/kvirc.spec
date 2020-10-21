Name:             kvirc
Version:          5.0.0
Release:          10%{?dist}
Summary:          Free portable IRC client
License:          GPLv2+ with exceptions
URL:              http://kvirc.net/
Source0:          ftp://ftp.kvirc.net/pub/kvirc/%{version}/source/KVIrc-%{version}.tar.bz2
# https://fedoraproject.org/wiki/Packaging:CryptoPolicies
Patch0:           kvirc-5.0.0_enforce_system_crypto.patch

BuildRequires:    enchant2-devel
BuildRequires:    audiofile-devel
BuildRequires:    glib2-devel
BuildRequires:    perl-devel
BuildRequires:    perl-ExtUtils-Embed
BuildRequires:    dbus-devel
BuildRequires:    cmake3
BuildRequires:    ninja-build
BuildRequires:    extra-cmake-modules
BuildRequires:    desktop-file-utils
BuildRequires:    gettext
BuildRequires:    doxygen
BuildRequires:    graphviz
BuildRequires:    libtheora-devel
BuildRequires:    libvorbis-devel
BuildRequires:    zlib-devel
BuildRequires:    openssl-devel
BuildRequires:    qt5-qtwebkit-devel
BuildRequires:    qt5-qtsvg-devel
BuildRequires:    qt5-qtmultimedia-devel
BuildRequires:    qt5-qtx11extras-devel
BuildRequires:    phonon-qt5-devel
BuildRequires:    kf5-ki18n-devel
BuildRequires:    kf5-kxmlgui-devel
BuildRequires:    kf5-kwindowsystem-devel
BuildRequires:    kf5-knotifications-devel
BuildRequires:    kf5-kservice-devel

%description
KVIrc is a free portable IRC client based on the excellent
Qt GUI toolkit. KVirc is being written by Szymon Stefanek
and the KVIrc Development Team with the contribution of
many IRC addicted developers around the world.

%prep
%autosetup -p1 -n KVIrc-%{version}

%build
%{cmake3}  \
-GNinja \
-DCMAKE_SKIP_RPATH=ON \
-DWANT_ENV_FLAGS=ON \
-DWANT_DCC_VIDEO=ON \
-DWANT_OGG_THEORA=ON \
-DWANT_GTKSTYLE=ON \
-DADDITIONAL_LINK_FLAGS='-Wl,--as-needed' \
%{nil}


%cmake_build

%install
%cmake_install

desktop-file-install \
    --dir %{buildroot}%{_datadir}/applications/ \
    %{buildroot}%{_datadir}/applications/%{name}.desktop

ln -sf ../../%{name}/5.0/license/COPYING COPYING

# Delete zero length file
rm %{buildroot}%{_datadir}/kvirc/5.0/help/en/_db_widget.idx

rm %{buildroot}%{_bindir}/kvirc-config
rm %{buildroot}%{_libdir}/libkvilib.so

%find_lang %{name} --all-name

%ldconfig_scriptlets

%files -f %{name}.lang
%license COPYING
%doc RELEASES
%{_bindir}/%{name}
%{_libdir}/libkvilib.so.5*
%{_datadir}/applications/%{name}.desktop
%{_libdir}/%{name}/
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/5.0
%dir %{_datadir}/%{name}/5.0/locale
%{_datadir}/%{name}/5.0/audio/
%{_datadir}/%{name}/5.0/config/
%{_datadir}/%{name}/5.0/defscript/
%{_datadir}/%{name}/5.0/help/
%{_datadir}/%{name}/5.0/modules/
%{_datadir}/%{name}/5.0/msgcolors/
%{_datadir}/%{name}/5.0/pics/
%{_datadir}/%{name}/5.0/themes/
%{_datadir}/%{name}/5.0/license/
%{_datadir}/icons/hicolor/*/apps/kvirc.*
%{_datadir}/icons/hicolor/*/mimetypes/application-x-kva.*
%{_datadir}/icons/hicolor/*/mimetypes/application-x-kvt.*
%{_datadir}/icons/hicolor/*/mimetypes/text-x-kvc.*
%{_datadir}/icons/hicolor/*/mimetypes/text-x-kvs.*
%{_datadir}/pixmaps/%{name}.png
%{_mandir}/man1/%{name}.1.gz

# Translation files
%lang(de) %{_mandir}/de/man1/%{name}.1.gz
%lang(fr) %{_mandir}/fr/man1/%{name}.1.gz
%lang(it) %{_mandir}/it/man1/%{name}.1.gz
%lang(pt) %{_mandir}/pt/man1/%{name}.1.gz
%lang(uk) %{_mandir}/uk/man1/%{name}.1.gz

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 5.0.0-9
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Aug 13 2019 Alexey Kurov <nucleo@fedoraproject.org> - 5.0.0-7
- rebuild

* Tue Aug 13 2019 Alexey Kurov <nucleo@fedoraproject.org> - 5.0.0-6
- Disable python support [Bug 1738031]

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 5.0.0-4
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 23 2019 Björn Esser <besser82@fedoraproject.org> - 5.0.0-2
- Append curdir to CMake invokation. (#1668512)

* Wed Jan 02 2019 Alexey Kurov <nucleo@fedoraproject.org> - 5.0.0-1
- KVIrc 5.0.0
- Switch to BuildRequires: enchant2-devel

* Wed Aug 01 2018 Leigh Scott <leigh123linux@googlemail.com> - 5.0.0-0.16.beta1
- Switch to BuildRequires: openssl-devel
- Fix disconnection issue with openssl-devel

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-0.15.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 5.0.0-0.14.beta1
- Perl 5.28 rebuild

* Sun Feb 25 2018 Leigh Scott <leigh123linux@googlemail.com> - 5.0.0-0.13.beta1
- Install lang files properly
- Fix scriptlets
- Use ninja to build

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-0.12.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 09 2018 Leigh Scott <leigh123linux@googlemail.com> - 5.0.0-0.11.beta1
- Fix some rpmlint warnings/errors

* Tue Jan 09 2018 Leigh Scott <leigh123linux@googlemail.com> - 5.0.0-0.10.beta1
- KVIrc 5.0.0 beta1

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-0.9.alpha2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-0.8.alpha2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 12 2017 Leigh Scott <leigh123linux@googlemail.com> - 5.0.0-0.7.alpha2
- Switch to compat-openssl10-devel
- Fix FTBFS (rhbz 1423830)

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 5.0.0-0.6.alpha2
- Perl 5.26 rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-0.5.alpha2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 5.0.0-0.4.alpha2
- Perl 5.24 rebuild

* Sun Mar 20 2016 Alexey Kurov <nucleo@fedoraproject.org> - 5.0.0-0.3.alpha2
- KVIrc 5.0.0 alpha2

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-0.2.alpha1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan  3 2016 Alexey Kurov <nucleo@fedoraproject.org> - 5.0.0-0.1.alpha1
- KVIrc 4.9.1
- switch to Qt5 and KF5

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 4.2.0-15
- Perl 5.22 rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 4.2.0-14
- Rebuilt for GCC 5 C++11 ABI change

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 4.2.0-13
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Aug 12 2014 Rex Dieter <rdieter@fedoraproject.org> 4.2.0-11
- add mime scriptlet

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Apr 24 2013 Alexey Kurov <nucleo@fedoraproject.org> - 4.2.0-8
- fix deprecated v4l interfaces in 3.9 kernel

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Oct 11 2012 Alexey Kurov <nucleo@fedoraproject.org> - 4.2.0-5
- rebuild for audiofile-0.3.4

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul  2 2012 Alexey Kurov <nucleo@fedoraproject.org> - 4.2.0-3
- fix epel build

* Mon Jul  2 2012 Alexey Kurov <nucleo@fedoraproject.org> - 4.2.0-2
- new tarball

* Sun Jul  1 2012 Alexey Kurov <nucleo@fedoraproject.org> - 4.2.0-1
- KVIrc 4.2.0
- drop BR: cryptopp-devel, esound-devel

* Thu Jan  5 2012 Alexey Kurov <nucleo@fedoraproject.org> - 4.0.4-3
- fix build with gcc-4.7.0

* Tue Jul 12 2011 Alexey Kurov <nucleo@fedoraproject.org> - 4.0.4-2
- BR: qt-webkit-devel

* Sun Mar 20 2011 Alexey Kurov <nucleo@fedoraproject.org> - 4.0.4-1
- KVIrc 4.0.4

* Thu Feb 10 2011 Alexey Kurov <nucleo@fedoraproject.org> - 4.0.2-8
- V4L1 disabled only for F15+

* Thu Feb 10 2011 Alexey Kurov <nucleo@fedoraproject.org> - 4.0.2-7
- disabled V4L1 support

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Alexey Kurov <nucleo@fedoraproject.org> - 4.0.2-5
- fix the color issues with recent gtk packages kvirc#1010

* Thu Nov 25 2010 Alexey Kurov <nucleo@fedoraproject.org> - 4.0.2-4
- depends on kdelibs version used at build time

* Tue Nov 23 2010 Alexey Kurov <nucleo@fedoraproject.org> - 4.0.2-3
- fix join channel crash #656251, kvirc#1024

* Mon Aug  2 2010 Alexey Kurov <nucleo@fedoraproject.org> - 4.0.2-2
- fix tray issue kvirc#872

* Mon Aug  2 2010 Alexey Kurov <nucleo@fedoraproject.org> - 4.0.2-1
- KVIrc 4.0.2

* Tue Jul 27 2010 Alexey Kurov <nucleo@fedoraproject.org> - 4.0.0-3
- fix for kvirc#858

* Tue Jul 27 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.0.0-2
- rebuild (python27)

* Mon Jun 28 2010 Alexey Kurov <nucleo@fedoraproject.org> - 4.0.0-1
- KVIrc 4.0

* Sun Apr 18 2010 Alexey Kurov <nucleo@fedoraproject.org> - 4.0.0-0.27.rc3
- fix in help borwser (r4258)

* Sat Apr 17 2010 Alexey Kurov <nucleo@fedoraproject.org> - 4.0.0-0.26.rc3
- update to 4.0 rc3

* Fri Feb 26 2010 Alexey Kurov <nucleo@fedoraproject.org> - 4.0.0-0.25.20100226svn4030
- svn snapshot 4030
- added -DCMAKE_SKIP_RPATH=ON to fix F13+ rpath issue

* Sun Feb 21 2010 Alexey Kurov <nucleo@fedoraproject.org> - 4.0.0-0.24.20100221svn4000
- svn 4000 (SASL support implemented)

* Fri Feb 12 2010 Alexey Kurov <nucleo@fedoraproject.org> - 4.0.0-0.23.20100212svn3956
- svn 3956 (should fix irc7 Excess Flood issue)

* Tue Dec 29 2009 Alexey Kurov <nucleo@fedoraproject.org> - 4.0.0-0.21.rc2
- fix log files date format from svn 3762

* Sat Dec 19 2009 Alexey Kurov <nucleo@fedoraproject.org> - 4.0.0-0.20.rc2
- KVIrc 4.0 release candidate 2
- added BR cryptopp-devel and -DWANT_NO_EMBEDDED_CODE=ON
- re-enabled pyhton module -DWITHOUT_PYTHON=OFF
- added BR python-devel

* Wed Sep  9 2009 Alexey Kurov <nucleo@fedoraproject.org> - 4.0.0-0.17.rc1
- disabled pyhton module, added -DWITHOUT_PYTHON=ON
- removed BR python-devel

* Tue Sep  8 2009 Alexey Kurov <nucleo@fedoraproject.org> - 4.0.0-0.16.rc1
- KVIrc 4.0 release candidate 1

* Mon Aug 31 2009 Alexey Kurov <nucleo@fedoraproject.org> - 4.0.0-0.15.20090831svn3442
- svn snapshot 3442 that includes option for using environment variables
- Added -DUSE_ENV_FLAGS=ON for using default compiler flags

* Sat Aug 29 2009 Alexey Kurov <nucleo@fedoraproject.org> - 4.0.0-0.13.20090827svn3429
- rebuilt with new openssl

* Thu Aug 27 2009 Alexey Kurov <nucleo@fedoraproject.org> - 4.0.0-0.11.20090827svn3429
- svn snapshot 3429 that includes patch for openssl >=1.0

* Thu Aug 27 2009 Tomas Mraz <tmraz@redhat.com> - 4.0.0-0.10.20090826svn3426
- rebuilt with new openssl

* Wed Aug 26 2009 Alexey Kurov <nucleo@fedoraproject.org> - 4.0.0-0.9.20090826svn3426
- svn snapshot 3426
- Added -DWANT_COEXISTENCE=OFF, binary name changed to kvirc
- Added -DWITH_ix86_ASM and -DMANUAL_REVISION
- Added BR: esound-devel

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.0-0.7.20090409svn3173
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Apr  9 2009 Alexey Kurov <nucleo@fedoraproject.org> - 4.0.0-0.6.20090409svn3173
- svn snapshot 3173
- Summary changed to Free portable IRC client

* Mon Apr  6 2009 Alexey Kurov <nucleo@fedoraproject.org> - 4.0.0-0.5.20090404svn3172
- patch for using standard compiler flags

* Sun Apr  5 2009 Alexey Kurov <nucleo@fedoraproject.org> - 4.0.0-0.4.20090404svn3172
- symlink to COPYING

* Sat Apr  4 2009 Alexey Kurov <nucleo@fedoraproject.org> - 4.0.0-0.3.20090404svn3172
- Exclude duplicate files
- svn snapshot 3172
- BR dbus-devel

* Sat Mar 28 2009 Alexey Kurov <nucleo@fedoraproject.org> - 4.0.0-0.2.20090328svn3168
- Fixed owner of /usr/share/kvirc
- Changed release tag and license field
- Fixed owner of /usr/share/kvirc/4.0 and /usr/share/kvirc/4.0/locale
- caps dir included in package

* Sat Mar 28 2009 Alexey Kurov <nucleo@fedoraproject.org> - 4.0-0.5.svn3168
- Use update-desktop-database and gtk-update-icon-cache instead of xdg-utils

* Fri Mar 20 2009 Alexey Kurov <nucleo@fedoraproject.org> - 4.0-0.4.svn3151
- Initial RPM release

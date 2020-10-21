%if 0%{?fedora} < 26 && 0%{?rhel} <= 7
%bcond_with kf5
%else
%bcond_without kf5
%endif
# keep this in sync with phonon-backend-gstreamer
%global gstversion 1.0

Name:           kid3
Version:        3.8.4
Release:        1%{?dist}
Summary:        Efficient KDE ID3 tag editor

License:        GPLv2+
URL:            http://kid3.sourceforge.net/
Source0:        http://download.kde.org/stable/%{name}/%{version}/%{name}-%{version}.tar.xz

%if %{with kf5}
BuildRequires:  kf5-kio-devel
BuildRequires:  kf5-kdelibs4support
BuildRequires:  kf5-kdoctools-devel
BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  qt5-qtmultimedia-devel
%else
BuildRequires:  kdelibs4-devel
%endif
BuildRequires:  cmake
BuildRequires:  id3lib-devel
BuildRequires:  taglib-devel >= 1.4
BuildRequires:  flac-devel
BuildRequires:  libvorbis-devel
BuildRequires:  libchromaprint-devel
BuildRequires:  pkgconfig(gstreamer-%{gstversion})
BuildRequires:  readline-devel
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  gcc-c++
Requires:       %{name}-common = %{version}-%{release}

%description
If you want to easily tag multiple MP3, Ogg/Vorbis, FLAC, MPC,
MP4/AAC, MP2, Speex, TrueAudio, WavPack, WMA, WAV, and AIFF files
(e.g. full albums) without typing the same information again and again
and have control over both ID3v1 and ID3v2 tags, then Kid3 is the
program you are looking for.

%package        common
Summary:        Efficient command line ID3 tag editor
Recommends:     xdg-utils

%description    common
If you want to easily tag multiple MP3, Ogg/Vorbis, FLAC, MPC,
MP4/AAC, MP2, Speex, TrueAudio, WavPack, WMA, WAV, and AIFF files
(e.g. full albums) without typing the same information again and again
and have control over both ID3v1 and ID3v2 tags, then Kid3 is the
program you are looking for.  The %{name}-common package provides Kid3
command line tool and files shared between all Kid3 variants.


%package        qt
Summary:        Efficient Qt ID3 tag editor
Requires:       %{name}-common = %{version}-%{release}

%description    qt
If you want to easily tag multiple MP3, Ogg/Vorbis, FLAC, MPC,
MP4/AAC, MP2, Speex, TrueAudio, WavPack, WMA, WAV, and AIFF files
(e.g. full albums) without typing the same information again and again
and have control over both ID3v1 and ID3v2 tags, then Kid3 is the
program you are looking for.  The %{name}-qt package provides Kid3
built without KDE dependencies.


%prep
%autosetup -p1


%build
%if %{with kf5}
# lib64 stuff: //bugzilla.redhat.com/show_bug.cgi?id=1425064
%cmake_kf5 \
%if "%{?_lib}" == "lib64"
    %{?_cmake_lib_suffix64} \
%endif
%else
%cmake_kde4 \
%endif
    -DWITH_GSTREAMER_VERSION=%{gstversion} \
    -DWITH_NO_MANCOMPRESS=ON \
    .
%cmake_build


%install

%cmake_install

install -dm 755 $RPM_BUILD_ROOT%{_pkgdocdir}
install -pm 644 AUTHORS ChangeLog README $RPM_BUILD_ROOT%{_pkgdocdir}

%find_lang %{name} --with-kde --with-man
mv %{name}.lang %{name}-kde.lang
%find_lang %{name}-qt --with-man
%find_lang %{name}-cli --with-man
%find_lang %{name} --with-qt
cat %{name}.lang >> %{name}-cli.lang
cat <<EOF >> %{name}-cli.lang
%%dir %%{_datadir}/kid3/
%%dir %%{_datadir}/kid3/translations/
EOF


%check
appstream-util validate-relax --nonet \
    $RPM_BUILD_ROOT%{_datadir}/metainfo/*.appdata.xml

%files -f %{name}-kde.lang
%{_bindir}/kid3
%{_datadir}/metainfo/org.kde.kid3.appdata.xml
%{_datadir}/icons/hicolor/*x*/apps/kid3.png
%{_datadir}/icons/hicolor/scalable/apps/kid3.svgz
%if %{with kf5}
%{_datadir}/applications/org.kde.kid3.desktop
%{_datadir}/kxmlgui5/%{name}
%else
%{_datadir}/applications/kde4/kid3.desktop
%{_kde4_appsdir}/kid3/
%endif

%files common -f %{name}-cli.lang
%{_bindir}/kid3-cli
%{_libdir}/kid3/
%{_datadir}/dbus-1/interfaces/*.xml
%{_datadir}/kid3/qml/
%{_mandir}/man1/kid3.1*
%{_mandir}/man1/kid3-cli.1*
%license COPYING LICENSE
%{_pkgdocdir}/

%files qt -f %{name}-qt.lang
%{_bindir}/kid3-qt
%{_datadir}/metainfo/org.kde.kid3-qt.appdata.xml
%{_datadir}/applications/org.kde.kid3-qt.desktop
%{_datadir}/icons/hicolor/*x*/apps/kid3-qt.png
%{_datadir}/icons/hicolor/scalable/apps/kid3-qt.svg
%dir %{_docdir}/kid3-qt/
%lang(de) %{_docdir}/kid3-qt/kid3_de.html
%lang(en) %{_docdir}/kid3-qt/kid3_en.html
%lang(pt) %{_docdir}/kid3-qt/kid3_pt.html
%lang(ca) %{_docdir}/kid3-qt/kid3_ca.html
%lang(it) %{_docdir}/kid3-qt/kid3_it.html
%lang(nl) %{_docdir}/kid3-qt/kid3_nl.html
%lang(sv) %{_docdir}/kid3-qt/kid3_sv.html
%lang(uk) %{_docdir}/kid3-qt/kid3_uk.html
%{_mandir}/man1/kid3-qt.1*


%changelog
* Sun Oct 04 2020 Marie Loise Nolden <loise@kde.org> - 3.8.4-1
- fix build with cmake, update to 3.8.4

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.2-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 08 2020 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 3.8.2-1
- Update to latest upstream version: 3.8.2 with new features and bugfixes

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.7.0-3
- Rebuild for readline 8.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 09 2019 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 3.7.0-1
- New upstream version

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 28 2018 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 3.6.0-1
- Update to 3.6.0

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.5.1-3
- Remove obsolete scriptlets

* Sun Jan 07 2018 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 3.5.1-2
- Rebuild because of updated dependency

* Thu Nov 02 2017 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 3.5.1-1
- Update to new upstream version: 3.5.1

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 21 2017 Ville Skyttä <ville.skytta@iki.fi> - 3.5.0-1
- Update to 3.5.0

* Mon Feb 20 2017 Ville Skyttä <ville.skytta@iki.fi> - 3.4.5-2
- Fix KF5/Qt5 build and reversed conditional build logic

* Sun Feb 19 2017 Ville Skyttä <ville.skytta@iki.fi> - 3.4.5-1
- Update to 3.4.5

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 3.4.4-2
- Rebuild for readline 7.x

* Sun Jan  1 2017 Ville Skyttä <ville.skytta@iki.fi> - 3.4.4-1
- Update to 3.4.4
- Build with KF5/Qt5 on F-26+

* Tue Nov  1 2016 Ville Skyttä <ville.skytta@iki.fi> - 3.4.3-1
- Update to 3.4.3

* Wed Aug 24 2016 Ville Skyttä <ville.skytta@iki.fi> - 3.4.2-1
- Update to 3.4.2
- Skip update-desktop-database in F-25+ scriptlets (handled by file triggers)

* Sat Jun 25 2016 Ville Skyttä <ville.skytta@iki.fi> - 3.4.1-1
- Update to 3.4.1

* Thu Jun  2 2016 Ville Skyttä <ville.skytta@iki.fi> - 3.4.0-1
- Update to 3.4.0
- Specfile cleanups

* Tue Mar 15 2016 Ville Skyttä <ville.skytta@iki.fi> - 3.3.2-1
- Update to 3.3.2

* Sat Feb  6 2016 Ville Skyttä <ville.skytta@iki.fi> - 3.3.0-3
- Use appstream-util instead of appdata-validate

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Sep 30 2015 Ville Skyttä <ville.skytta@iki.fi> - 3.3.0-1
- Update to 3.3.0

* Wed Jul 15 2015 Ville Skyttä <ville.skytta@iki.fi> - 3.2.1-4
- Soften xdg-utils dependency to recommendation

* Tue Jun 30 2015 Ville Skyttä <ville.skytta@iki.fi> - 3.2.1-3
- Move kid3(1) manpage to -common, others are symlinks to it

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed May 13 2015 Ville Skyttä <ville.skytta@iki.fi> - 3.2.1-1
- Update to 3.2.1

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 3.2.0-2
- Rebuilt for GCC 5 C++11 ABI change

* Wed Mar 18 2015 Ville Skyttä <ville.skytta@iki.fi> - 3.2.0-1
- Update to 3.2.0

* Sat Nov 15 2014 Ville Skyttä <ville.skytta@iki.fi> - 3.1.2-1
- Update to 3.1.2

* Fri Aug 29 2014 Ville Skyttä <ville.skytta@iki.fi> - 3.1.1-2
- Apply upstream appdata fix

* Tue Aug 26 2014 Ville Skyttä <ville.skytta@iki.fi> - 3.1.1-1
- Update to 3.1.1
- Build with gstreamer 1 for F-21+ and EL > 7
- Mark license files as %%license where applicable

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Apr 25 2014 Ville Skyttä <ville.skytta@iki.fi> - 3.1-1
- Update to 3.1

* Sun Dec  1 2013 Ville Skyttä <ville.skytta@iki.fi> - 3.0.2-1
- Update to 3.0.2.

* Tue Oct 29 2013 Ville Skyttä <ville.skytta@iki.fi> - 3.0.1-1
- Update to 3.0.1.
- Move translations to -common.

* Fri Oct 25 2013 Ville Skyttä <ville.skytta@iki.fi> - 3.0-1
- Update to 3.0.

* Fri Jul 26 2013 Ville Skyttä <ville.skytta@iki.fi> - 2.3-2
- Install -qt docs to unversioned dir if %%{_docdir_fmt} is defined.

* Thu Mar 14 2013 Ville Skyttä <ville.skytta@iki.fi> - 2.3-1
- Update to 2.3.
- Patch to fix XM support.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Feb 12 2013 Ville Skyttä <ville.skytta@iki.fi> - 2.2.1-2
- Remove "fedora" vendor prefix from desktop entry file names.
- Fix bogus dates in %%changelog.

* Tue Dec  4 2012 Ville Skyttä <ville.skytta@iki.fi> - 2.2.1-1
- Update to 2.2.1.

* Sat Oct 27 2012 Ville Skyttä <ville.skytta@iki.fi> - 2.2-1
- Update to 2.2.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat May 12 2012 Ville Skyttä <ville.skytta@iki.fi> - 2.1-1
- Update to 2.1.

* Wed Jan  4 2012 Ville Skyttä <ville.skytta@iki.fi> - 2.0.1-2
- Fix build with g++ 4.7.0.

* Fri Nov  4 2011 Ville Skyttä <ville.skytta@iki.fi> - 2.0.1-1
- Update to 2.0.1.

* Thu Sep  8 2011 Ville Skyttä <ville.skytta@iki.fi> - 2.0-1
- Update to 2.0.
- Clean up no longer needed specfile parts.
- Do icon dir timestamp update in %%post with lua.

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Feb  5 2011 Ville Skyttä <ville.skytta@iki.fi> - 1.6-2
- Add -qt subpackage containing a version without KDE dependencies.

* Sat Feb  5 2011 Ville Skyttä <ville.skytta@iki.fi> - 1.6-1
- Update to 1.6.

* Sat Sep 25 2010 Ville Skyttä <ville.skytta@iki.fi> - 1.5-1
- Update to 1.5, patches applied upstream.

* Mon May 31 2010 Ville Skyttä <ville.skytta@iki.fi> - 1.4-2
- Patch to fix build with KDE 4.5 (DocBook 4.2).
- Patch to improve desktop entry (MIME types, startup).

* Sat Mar  6 2010 Ville Skyttä <ville.skytta@iki.fi> - 1.4-1
- Update to 1.4.

* Wed Nov 25 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.3-2
- Rebuild for Qt 4.6.0 RC1 in F13 (was built against Beta 1 with unstable ABI)

* Sun Nov  8 2009 Ville Skyttä <ville.skytta@iki.fi> - 1.3-1
- Update to 1.3.

* Wed Sep 23 2009 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 1.2-3
- Update desktop file according to F-12 FedoraStudio feature

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Apr 30 2009 Ville Skyttä <ville.skytta@iki.fi> - 1.2-1
- Update to 1.2, discogs.com patch applied upstream.
- Use %%find_lang --with-kde.

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 18 2009 Ville Skyttä <ville.skytta@iki.fi> - 1.1-2
- Apply upstream patch to fix discogs.com import.
- Update desktop database when appropriate.
- Improve icon cache refresh scriptlets.
- Do not convert doc symlinks to relative.
- Drop support for building for KDE 3.

* Sat Oct 25 2008 Ville Skyttä <ville.skytta@iki.fi> - 1.1-1
- 1.1.

* Thu Apr  3 2008 Ville Skyttä <ville.skytta@iki.fi> - 1.0-1
- 1.0, all patches applied upstream.

* Thu Jan  3 2008 Ville Skyttä <ville.skytta@iki.fi> - 0.10-3
- Fix build with gcc 4.3's cleaned up C++ headers.

* Mon Dec  3 2007 Ville Skyttä <ville.skytta@iki.fi> - 0.10-2
- Use xdg-open as the default browser.

* Sun Dec  2 2007 Ville Skyttä <ville.skytta@iki.fi> - 0.10-1
- 0.10, desktop entry patch applied upstream.
- Build for KDE4 in F9+, KDE3 in earlier.

* Sun Dec  2 2007 Ville Skyttä <ville.skytta@iki.fi> - 0.9-3
- BuildRequire libvorbis-devel, and kdelibs3-devel instead of kdelibs-devel.

* Thu Aug 16 2007 Ville Skyttä <ville.skytta@iki.fi> - 0.9-2
- Remove Application Category and deprecated items from desktop entry.
- License: GPLv2+

* Wed Jun 13 2007 Ville Skyttä <ville.skytta@iki.fi> - 0.9-1
- 0.9.

* Wed Feb 14 2007 Ville Skyttä <ville.skytta@iki.fi> - 0.8.1-2
- Rebuild, drop workaround for #216783.

* Wed Nov 22 2006 Ville Skyttä <ville.skytta@iki.fi> - 0.8.1-1
- 0.8.1, desktop entry fixes applied upstream.
- Re-enable musicbrainz support.

* Mon Oct  2 2006 Ville Skyttä <ville.skytta@iki.fi> - 0.7-4
- Rebuild.

* Wed Sep 27 2006 Ville Skyttä <ville.skytta@iki.fi> - 0.7-3
- Disable musicbrainz support by default, not ready for tunepimp 0.5 yet.

* Wed Aug 30 2006 Ville Skyttä <ville.skytta@iki.fi> - 0.7-2
- Rebuild.

* Thu Jun 29 2006 Ville Skyttä <ville.skytta@iki.fi> - 0.7-1
- 0.7, build with libtunepimp.
- Patch to register as a handler for more media types.
- Update desktop database at post(un)install time.
- Make symlinks relative.

* Wed Feb 15 2006 Ville Skyttä <ville.skytta@iki.fi> - 0.6-2
- Explicitly disable musicbrainz support for now, needs older libtunepimp
  than what's available in FE.
- Apply Debian's 0.6-2 patch, includes ogg tagging fix.
- Install man page.

* Mon Oct 31 2005 Ville Skyttä <ville.skytta@iki.fi> - 0.6-1
- 0.6, patches applied upstream.
- Clean up build dependencies.
- Improve summary and description.

* Thu May 19 2005 Ville Skyttä <ville.skytta@iki.fi> - 0.5-4
- Update GTK icon cache at (un)install time.

* Wed Apr  6 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 0.5-3
- rebuilt

* Sun Dec 19 2004 Ville Skyttä <ville.skytta@iki.fi> - 0:0.5-2
- Apply patch for better non-latin1 filename support.
- Build with dependency tracking disabled.
- Trim dir ownership for FC3.

* Sat Jul 31 2004 Ville Skyttä <ville.skytta@iki.fi> - 0:0.5-0.fdr.1
- Update to 0.5.

* Mon Feb  9 2004 Ville Skyttä <ville.skytta@iki.fi> - 0:0.4-0.fdr.1
- Update to 0.4.

* Sat Nov  1 2003 Ville Skyttä <ville.skytta@iki.fi> - 0:0.3-0.fdr.1
- First build.

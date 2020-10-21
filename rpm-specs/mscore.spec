%global fontfamilyname %{name}
%global shortver 3.5

Name:          mscore
Summary:       Music Composition & Notation Software
Version:       %{shortver}.2
Release:       1%{?dist}
# rtf2html is LGPLv2+
# paper4.png paper5.png are LGPLv3
# the rest is GPLv2
# Soundfont is MIT
License:       GPLv2 and LGPLv2+ and LGPLv3 and MIT
URL:           https://musescore.org/
Source0:       https://github.com/musescore/MuseScore/archive/v%{version}/MuseScore-%{version}.tar.gz
# For mime types
Source1:       %{name}.xml
# Add metainfo file for font to show in gnome-software
Source2:       %{fontfamilyname}.metainfo.xml
# We don't build the common files (font files, wallpapers, demo song, instrument
# list) into the binary executable to reduce its size. This is also useful to
# inform the users about the existence of different choices for common files.
# The font files need to be separated due to the font packaging guidelines.
Patch0:        mscore-3.4.2-separate-commonfiles.patch
# Ensure CMake will use qmake-qt5
Patch1:        mscore-3.5.1-fix-qmake-path.patch
# Unbundle gnu-free-{sans,serif}-fonts, kqoauth, QtSingleApplication, and
# steinberg-bravura{,-text}-fonts
Patch2:        mscore-3.4.2-unbundle.patch
# Fix some glitches in the aeolus code
Patch3:        mscore-3.5.0-aeolus.patch
# Fix some glitches in the OMR code
Patch4:        mscore-3.5.0-omr.patch

BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: fontforge
BuildRequires: fontpackages-devel
BuildRequires: gcc-c++
BuildRequires: gnu-free-sans-fonts
BuildRequires: gnu-free-serif-fonts
BuildRequires: lame-devel
BuildRequires: perl(Pod::Usage)
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(jack)
BuildRequires: pkgconfig(libpulse)
BuildRequires: pkgconfig(poppler-qt5)
BuildRequires: pkgconfig(portaudiocpp)
BuildRequires: pkgconfig(Qt5)
BuildRequires: pkgconfig(Qt5Designer)
BuildRequires: pkgconfig(Qt5Qml)
BuildRequires: pkgconfig(Qt5QuickControls2)
BuildRequires: pkgconfig(Qt5Script)
BuildRequires: pkgconfig(Qt5Svg)
BuildRequires: pkgconfig(Qt5UiTools)
%ifarch %{qt5_qtwebengine_arches}
BuildRequires: pkgconfig(Qt5WebEngine)
%endif
BuildRequires: pkgconfig(Qt5WebKit)
BuildRequires: pkgconfig(Qt5XmlPatterns)
BuildRequires: pkgconfig(sndfile)
BuildRequires: pkgconfig(vorbis)
BuildRequires: portmidi-devel
BuildRequires: qt5-qtbase-private-devel
BuildRequires: qtsingleapplication-qt5-devel
BuildRequires: steinberg-bravura-fonts-all

Requires:      %{name}-fonts = %{version}-%{release}
Requires:      gnu-free-sans-fonts
Requires:      gnu-free-serif-fonts
Requires:      hicolor-icon-theme
Requires:      soundfont2
Requires:      soundfont2-default
Requires:      steinberg-bravura-fonts-all
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}
# For scripting
Requires:      qt5-qtquickcontrols%{?_isa} = %{_qt5_version}
Requires:      qt5-qtquickcontrols2%{?_isa} = %{_qt5_version}

# Doxygen documentation is huge and it is for musescore development only.
# Hence we don't build it for now. Otherwise it needs:
# BuildRequires: graphviz doxygen texlive-latex texlive-dvips

Provides:      musescore = %{version}-%{release}
Provides:      bundled(beatroot-vamp) = 1.0
Provides:      bundled(intervaltree)
Provides:      bundled(rtf2html) = 0.2.0

%description
MuseScore is a free cross platform WYSIWYG music notation program. Some
highlights:

    * WYSIWYG, notes are entered on a "virtual note sheet"
    * Unlimited number of staves
    * Up to four voices per staff
    * Easy and fast note entry with mouse, keyboard or MIDI
    * Integrated sequencer and FluidSynth software synthesizer
    * Import and export of MusicXML and Standard MIDI Files (SMF)
    * Translated in 26 languages

%package       doc
Summary:       MuseScore documentation
License:       CC-BY
Requires:      %{name} = %{version}-%{release}
BuildArch:     noarch

%description   doc
MuseScore is a free cross platform WYSIWYG music notation program.

This package contains the user manual of MuseScore in different languages.

%package       fonts
Summary:       MuseScore fonts
License:       GPL+ with exceptions and OFL
Requires:      fontpackages-filesystem
BuildArch:     noarch

%description   fonts
MuseScore is a free cross platform WYSIWYG music notation program.

This package contains the musical notation fonts for use of MuseScore.

%prep
%autosetup -p1 -n MuseScore-%{version}

# Remove bundled stuff
rm -rf thirdparty/{freetype,openssl,poppler,portmidi,singleapp}
rm -rf fonts/{bravura,FreeS*}
rm -rf cmake

# Force Fedora specific flags:
find . -name CMakeLists.txt -exec sed -i -e 's|-O3|%{optflags}|' {} \+

# Fix EOL encoding
for fil in thirdparty/rtf2html/README{,.ru}; do
  sed -i.orig 's|\r||' $fil
  touch -r $fil.orig $fil
  rm $fil.orig
done

%build
# Build the actual program
mkdir -p build
pushd build
   %cmake -B . \
          -DCMAKE_BUILD_TYPE=RELEASE         \
          -DCMAKE_CXX_FLAGS="%{optflags} -fsigned-char"    \
          -DCMAKE_CXX_FLAGS_RELEASE="%{optflags} -std=gnu++11 -fPIC -DNDEBUG -DQT_NO_DEBUG -fsigned-char" \
          -DAEOLUS=ON \
%if 0%{?__isa_bits} == 32
          -DBUILD_64=OFF \
%endif
%ifnarch %{qt5_qtwebengine_arches}
          -DBUILD_WEBENGINE=OFF \
%endif
          -DDOWNLOAD_SOUNDFONT=OFF \
          -DOMR=ON \
          -DUSE_PATH_WITH_EXPLICIT_QT_VERSION=ON \
          -DUSE_SYSTEM_FREETYPE=ON \
          -DUSE_SYSTEM_POPPLER=ON \
          -DUSE_SYSTEM_QTSINGLEAPPLICATION=ON \
          ..
   %make_build lrelease PREFIX=%{_prefix}
   %make_build manpages PREFIX=%{_prefix}
   %make_build PREFIX=%{_prefix} VERBOSE=1
   make -C rdoc referenceDocumentation PREFIX=%{_prefix}
popd

%install
make -C build install PREFIX=%{_prefix} DESTDIR=%{buildroot}
make -C build/rdoc install PREFIX=%{_prefix} DESTDIR=%{buildroot}

mkdir -p %{buildroot}/%{_datadir}/applications
cp -a build/mscore.desktop %{buildroot}/%{_datadir}/applications

# Install fonts
mkdir -p %{buildroot}/%{_fontdir}
mkdir -p %{buildroot}/%{_fontdir}/bravura
mkdir -p %{buildroot}/%{_fontdir}/campania
mkdir -p %{buildroot}/%{_fontdir}/gootville
mkdir -p %{buildroot}/%{_fontdir}/musejazz
cp -a fonts/smufl %{buildroot}%{_fontdir}
install -pm 644 fonts/*.{sfd,ttf} %{buildroot}/%{_fontdir}
install -pm 644 fonts/campania/*.otf %{buildroot}/%{_fontdir}/campania/
install -pm 644 fonts/gootville/*.otf %{buildroot}/%{_fontdir}
install -pm 644 fonts/gootville/*.json %{buildroot}/%{_fontdir}/gootville/
install -pm 644 fonts/mscore/*.{sfd,ttf} %{buildroot}/%{_fontdir}
install -pm 644 fonts/mscore/*.json %{buildroot}/%{_fontdir}
install -pm 644 fonts/musejazz/*.otf %{buildroot}/%{_fontdir}
install -pm 644 fonts/musejazz/*.json %{buildroot}/%{_fontdir}/musejazz
install -pm 644 fonts/*.xml %{buildroot}/%{_fontdir}

# mscz
install -pm 0644 share/templates/*.mscz %{buildroot}/%{_datadir}/%{name}-%{shortver}/demos/
# symlinks to be safe
pushd %{buildroot}/%{_datadir}/%{name}-%{shortver}/demos/
for i in *.mscz; do
  ln -s %{_datadir}/%{name}-%{shortver}/demos/$i ../templates/$i
done
popd

pushd %{buildroot}/%{_fontdir}
cd gootville
ln -s ../Gootville.otf .
ln -s ../GootvilleText.otf .
cd ../musejazz
ln -s ../MuseJazz.otf .
ln -s ../MuseJazzText.otf .
cd ..
popd

# Mime type
mkdir -p %{buildroot}/%{_datadir}/mime/packages
install -pm 644 %{SOURCE1} %{buildroot}/%{_datadir}/mime/packages/

# Desktop file
desktop-file-install \
   --dir=%{buildroot}/%{_datadir}/applications \
   --add-category="X-Notation" \
   --remove-category="Sequencer" \
   --remove-category="AudioVideoEditing" \
   --add-mime-type="audio/midi" \
   --add-mime-type="application/xml" \
   %{buildroot}/%{_datadir}/applications/%{name}.desktop

# Move images to the freedesktop location
for sz in 16 24 32 48 64 96 128 512; do
  mkdir -p %{buildroot}/%{_datadir}/icons/hicolor/${sz}x${sz}/{apps,mimetypes}
  install -pm 644 assets/musescore-icon-round-${sz}.png \
    %{buildroot}/%{_datadir}/icons/hicolor/${sz}x${sz}/apps/mscore.png
  install -pm 644 assets/musescore-icon-round-${sz}.png \
    %{buildroot}/%{_datadir}/icons/hicolor/${sz}x${sz}/mimetypes/mscore.png
done
mkdir -p %{buildroot}/%{_datadir}/icons/hicolor/scalable/{apps,mimetypes}
install -pm 644 assets/musescore-icon-round.svg \
  %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps/mscore.svg
install -pm 644 assets/musescore-icon-round.svg \
  %{buildroot}/%{_datadir}/icons/hicolor/scalable/mimetypes/mscore.svg

# Manpage
mkdir -p %{buildroot}/%{_mandir}/man1
install -pm 644 build/%{name}.1 %{buildroot}/%{_mandir}/man1/

# There are many doc files spread around the tarball. Let's collect them
mv thirdparty/rtf2html/ChangeLog        ChangeLog.rtf2html
mv thirdparty/rtf2html/COPYING.LESSER   COPYING.LESSER.rtf2html
mv thirdparty/rtf2html/README           README.rtf2html
mv thirdparty/rtf2html/README.mscore    README.mscore.rtf2html
mv thirdparty/rtf2html/README.ru        README.ru.rtf2html
mv share/wallpaper/COPYRIGHT            COPYING.wallpaper
mv %{buildroot}%{_datadir}/%{name}-%{shortver}/sound/MuseScore_General_License.md \
   COPYING.MuseScore_General
mv fonts/campania/LICENSE               COPYING.OFL

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE2} \
        %{buildroot}%{_datadir}/appdata/%{fontfamilyname}.metainfo.xml

# Do not duplicate files from qt5-qtwebengine
rm -f %{buildroot}%{_bindir}/QtWebEngineProcess
rm -fr %{buildroot}%{_prefix}/lib

# Move the soundfonts to where the rest of the system expects them to be
mv %{buildroot}%{_datadir}/%{name}-%{shortver}/sound \
   %{buildroot}%{_datadir}/soundfonts
ln -s ../soundfonts %{buildroot}%{_datadir}/%{name}-%{shortver}/sound

%check
# iotest seems outdated. Skipping.
# reftest needs the X server. Skipping.

%files
%doc README*
%license LICENSE.GPL COPYING*
%{_bindir}/mscore
%{_bindir}/musescore
%{_datadir}/%{name}-%{shortver}/
%exclude %{_datadir}/%{name}-%{shortver}/manual/
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/metainfo/*.appdata.xml
%exclude %{_datadir}/mime/packages/musescore.xml
%{_datadir}/mime/packages/mscore.xml
%{_mandir}/man1/*
%{_datadir}/soundfonts/aeolus/
%{_datadir}/soundfonts/MuseScore_General.sf3

%files doc
%doc %{_datadir}/%{name}-%{shortver}/manual/

%_font_pkg %{fontfamilyname}*.ttf MScoreText.ttf *.otf
%{_fontdir}/campania/
%{_fontdir}/gootville/
%{_fontdir}/musejazz/
%{_fontdir}/smufl/
%{_fontdir}/*.json
%{_fontdir}/*.sfd
%{_fontdir}/*.xml
%{_datadir}/appdata/%{fontfamilyname}.metainfo.xml

%changelog
* Mon Oct 19 2020 Jerry James <loganjerry@gmail.com> - 3.5.2-1
- Version 3.5.2

* Tue Oct  6 2020 Jerry James <loganjerry@gmail.com> - 3.5.1-1
- Version 3.5.1

* Fri Sep 11 2020 Jan Grulich <jgrulich@redhat.com> - 3.5.0-2
- rebuild (qt5)

* Fri Aug  7 2020 Jerry James <loganjerry@gmail.com> - 3.5.0-1
- Version 3.5.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 06 2020 Rex Dieter <rdieter@fedoraproject.org> - 3.4.2-4
- rebuild (qt5)

* Sat Apr  4 2020 Jerry James <loganjerry@gmail.com> - 3.4.2-3
- Rebuild for updated Bravura fonts

* Wed Mar 18 2020 Jerry James <loganjerry@gmail.com> - 3.4.2-2
- Desktop file should not claim LilyPond support (bz 1813797)

* Mon Feb 17 2020 Jerry James <loganjerry@gmail.com> - 3.4.2-1
- Version 3.4.2
- Drop the -user-default-soundfont patch; use a symlink instead
- R both qt5-qtquickcontrols and qt5-qtquickcontrols2; both seem to be used
- kQOAuth is no longer used, so drop unbundling

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Marek Kasik <mkasik@redhat.com> - 3.3.4-4
- Rebuild for poppler-0.84.0

* Sat Dec 14 2019 Jerry James <loganjerry@gmail.com> - 3.3.4-3
- Require QtQuick.Controls version 2

* Mon Dec 09 2019 Jan Grulich <jgrulich@redhat.com> - 3.3.4-2
- rebuild (qt5)

* Wed Dec  4 2019 Jerry James <loganjerry@gmail.com> - 3.3.4-1
- Version 3.3.4

* Tue Nov 26 2019 Jerry James <loganjerry@gmail.com> - 3.3.3-1
- Version 3.3.3

* Fri Nov 22 2019 Jerry James <loganjerry@gmail.com> - 3.3.2-2
- Fix segfault in the aeolus destructor

* Thu Nov 14 2019 Jerry James <loganjerry@gmail.com> - 3.3.2-1
- Version 3.3.2

* Wed Nov 13 2019 Jerry James <loganjerry@gmail.com> - 3.3.1-1
- Version 3.3.1

* Fri Nov  1 2019 Jerry James <loganjerry@gmail.com> - 3.3.0-1
- Version 3.3.0
- Unbundle the bravura fonts

* Wed Sep 25 2019 Jan Grulich <jgrulich@redhat.com> - 3.2.3-3
- rebuild (qt5)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 18 2019 Jerry James <loganjerry@gmail.com> - 3.2.3-1
- Version 3.2.3
- Update URLs
- Drop upstreamed patches: -fix-files-for-precompiled-header,
  -fix-desktop-file, -fix-fonts_tablature, -missing-includes
- Unbundle gnu-free-{sans,serif}-fonts, kqoauth, and QtSingleApplication
- Remove "and OFL" from main package License; fonts are in -fonts subpackage
- Remove "and CC-BY" from main package License; applies to -doc subpackage

* Mon Jun 17 2019 Jan Grulich <jgrulich@redhat.com> - 2.2.1-11
- rebuild (qt5)

* Wed Jun 05 2019 Jan Grulich <jgrulich@redhat.com> - 2.2.1-10
- rebuild (qt5)

* Thu Apr 25 2019 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.2.1-9
- Fix build (#1702062)

* Mon Mar 04 2019 Rex Dieter <rdieter@fedoraproject.org> - 2.2.1-9
- rebuild (qt5)

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec 13 2018 Rex Dieter <rdieter@fedoraproject.org> - 2.2.1-7
- rebuild (qt5)

* Fri Sep 21 2018 Jan Grulich <jgrulich@redhat.com> - 2.2.1-6
- rebuild (qt5)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 21 2018 Rex Dieter <rdieter@fedoraproject.org> - 2.2.1-4
- rebuild (qt5)

* Thu May 31 2018 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 2.2.1-3
- Fix missing include for qt >= 5.11 (RHBZ#1584834)

* Sun May 27 2018 Rex Dieter <rdieter@fedoraproject.org> - 2.2.1-2
- rebuild (qt5)

* Wed Apr 04 2018 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 2.2.1-1
- Update to 2.2.1

* Wed Feb 14 2018 Jan Grulich <jgrulich@redhat.com> - 2.1.0-12
- rebuild (qt5)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 05 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.1.0-10
- Remove (hopefully) last dependency on qt4

* Fri Jan 05 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.1.0-9
- Remove obsolete scriptlets

* Mon Jan 01 2018 Rex Dieter <rdieter@fedoraproject.org> - 2.1.0-8
- rebuild (qt5)

* Mon Dec 25 2017 Brendan Jones <brendan.jones.it@gmail.com> - 2.1.0-7
- Link against full template path

* Mon Dec 25 2017 Brendan Jones <brendan.jones.it@gmail.com> - 2.1.0-6
- Correct mscz link

* Mon Nov 27 2017 Rex Dieter <rdieter@fedoraproject.org> - 2.1.0-5
- rebuild (qt5)

* Mon Nov 20 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.1.0-4
- Use proper qtsingleapplication (qt5)

* Sun Oct 29 2017 Brendan Jones <brendan.jones.it@gmail.com> - 2.1.0-3
- Use system libs

* Sat Oct 21 2017 Brendan Jones <brendan.jones.it@gmail.com> - 2.1.0-2
- Remove non-free scores
- Fix pch project depends
- Reorder patches

* Tue Oct 17 2017 Brendan Jones <brendan.jones.it@gmail.com> - 2.1.0-1
- Update to 2.1

* Wed Oct 11 2017 Rex Dieter <rdieter@fedoraproject.org> - 2.0.3-10
- BR: qt5-qtbase-private-devel

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 18 2017 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 2.0.3-7
- Removed BR: qt5-qtquick1-devel as it is no longer in Fedora

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Nov 19 2016 Peter Robinson <pbrobinson@fedoraproject.org> 2.0.3-4
- Rebuild (Power64)

* Mon May 09 2016 Brendan Jones <brendan.jones.it@gmail.com> 2.0.3-3
- Font locations

* Fri May 06 2016 Brendan Jones <brendan.jones.it@gmail.com> 2.0.3-2
- correct load and font errors

* Sun Apr 24 2016 Brendan Jones <brendan.jones.it@gmail.com> 2.0.3-1
- Update to 2.0.3
- fix make job flags
- rename modified patches

* Sat Feb 27 2016 Brendan Jones <brendan.jones.it@gmail.com> 2.0.2-1
- Update to 2.0.2

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Nov 19 2015 Brendan Jones <brendan.jones.it@gmail.com> 2.0.1-6
- Fix fonts_tabulature.xml location bug rhbz#1236965 rhbz#1262528

* Wed Sep 16 2015 Marcin Juszkiewicz <mjuszkiewicz@redhat.com> - 2.0.1-5
- added backport fixing compilation with Qt5.5 - rhbz#1263806

* Tue Jul 14 2015 Brendan Jones <brendan.jones.it@gmail.com> 2.0.1-4
- Rebuilt

* Tue Jun 30 2015 Brendan Jones <brendan.jones.it@gmail.com> 2.0.1-3
- Fix font locations

* Tue Jun 23 2015 Brendan Jones <bsjones@fedoraproject.org> - 2.0.1-2
- Clean up change log

* Tue Jun 23 2015 Brendan Jones <bsjones@fedoraproject.org> - 2.0.1-1
- Update to 2.0.1 - patches provided by Bodhi Zazen

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr 29 2015 Tom Callaway <spot@fedoraproject.org> - 2.0.0-3
- do not strip bits when installing (bz 1215956)

* Sat Apr 25 2015 Tom Callaway <spot@fedoraproject.org> - 2.0.0-2
- add BR: doxygen
- add -fsigned-char for ARM

* Sat Apr 25 2015 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.0.0-1
- Remove mp3 support to fix FTBFS
- Add pulseaudio-libs-devel to BR

* Tue Nov 18 2014 Parag Nemade <pnemade AT redhat DOT com> - 1.3-8
- Add metainfo file to show mscore-MuseJazz font in gnome-software

* Thu Oct 02 2014 Rex Dieter <rdieter@fedoraproject.org> 1.3-7
- update mime scriptlet

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Feb 26 2014 Dan Horák <dan[at]danny.cz> - 1.3-4
- fix FTBFS (#992300)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Apr 12 2013 Tom Callaway <spot@fedoraproject.org> - 1.3-2
- perl(Pod::Usage) needed for font generation

* Fri Apr 12 2013 Tom Callaway <spot@fedoraproject.org> - 1.3-1
- update to 1.3
- remove mscore/demos/prelude.mscx from source tarball (it is non-free, see bz951379)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Mar 13 2012 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 1.2-1
- Update to 1.2.

* Sat Mar 03 2012 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 1.1-4
- Fix accidontals crash RHBZ#738044

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-3
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jul 28 2011 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 1.1-1
- Update to 1.1.

* Tue Feb 08 2011 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 1.0-1
- Update to 1.0.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Sep 26 2010 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 0.9.6.3-1
- Update to 0.9.6.3

* Thu Aug 19 2010 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 0.9.6.2-1
- Update to 0.9.6.2

* Tue Jul 20 2010 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 0.9.6.1-1
- Update to 0.9.6.1

* Mon Jun 14 2010 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 0.9.6-1
- Update to 0.9.6
- Split documentation into its own package
- Move some gcc warning fixes into a patch

* Tue Dec 22 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 0.9.5-3
- Fix build flags on F-11

* Tue Dec 22 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 0.9.5-2
- Add default soundfont support for exported audio files
- Rebuild against new libsndfile for additional functionality
- Drop F-10 related bits from specfile
- Make fonts subpackage noarch
- Fix build failure on arm architecture

* Fri Aug 21 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 0.9.5-1
- Update to 0.9.5

* Wed Aug 05 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 0.9.4-6
- Update the .desktop file

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jun 11 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 0.9.4-4
- Font package cleanup for F-12 (RHBZ#493463)
- One specfile for all releases

* Mon Mar 23 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 0.9.4-3.fc10.1
- Add BR: tetex-font-cm-lgc for Fedora < 11

* Mon Mar 23 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 0.9.4-3
- Add Provides: musescore = %%{name}-%%{version}
- Replace "fluid-soundfont" requirement with "soundfont2-default"

* Fri Mar 06 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 0.9.4-2
- Add extra BR:tex-cm-lgc for F-11+. This is necessary to build the fonts from source
- Update icon scriptlets according to the new guidelines

* Sat Feb 21 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 0.9.4-1
- Initial Fedora build

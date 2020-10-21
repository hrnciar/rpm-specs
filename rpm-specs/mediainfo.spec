%global libzen_version  0.4.38

Name:           mediainfo
Version:        20.08
Release:        1%{?dist}
Summary:        Supplies technical and tag information about a video or audio file (CLI)
Summary(ru):    Предоставляет полную информацию о медиа файле (CLI)

License:        BSD
URL:            http://mediaarea.net/MediaInfo
Source0:        http://mediaarea.net/download/source/%{name}/%{version}/%{name}_%{version}.tar.xz
Source1:        mediainfo-qt.desktop
Source2:        mediainfo-qt.kde4.desktop

BuildRequires:  pkgconfig(libmediainfo) >= %{version}
BuildRequires:  pkgconfig(libzen) >= %{libzen_version}
BuildRequires:  wxGTK3-devel
BuildRequires:  pkgconfig(zlib)
BuildRequires:  libtool
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  desktop-file-utils
BuildRequires:  ImageMagick
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  libappstream-glib

%description
MediaInfo CLI (Command Line Interface).

What information can I get from MediaInfo?
* General: title, author, director, album, track number, date, duration...
* Video: codec, aspect, fps, bitrate...
* Audio: codec, sample rate, channels, language, bitrate...
* Text: language of subtitle
* Chapters: number of chapters, list of chapters

DivX, XviD, H263, H.263, H264, x264, ASP, AVC, iTunes, MPEG-1,
MPEG1, MPEG-2, MPEG2, MPEG-4, MPEG4, MP4, M4A, M4V, QuickTime,
RealVideo, RealAudio, RA, RM, MSMPEG4v1, MSMPEG4v2, MSMPEG4v3,
VOB, DVD, WMA, VMW, ASF, 3GP, 3GPP, 3GP2

What format (container) does MediaInfo support?
* Video: MKV, OGM, AVI, DivX, WMV, QuickTime, Real, MPEG-1,
  MPEG-2, MPEG-4, DVD (VOB) (Codecs: DivX, XviD, MSMPEG4, ASP,
  H.264, AVC...)
* Audio: OGG, MP3, WAV, RA, AC3, DTS, AAC, M4A, AU, AIFF
* Subtitles: SRT, SSA, ASS, S-MI

%description -l ru
MediaInfo CLI (интерфейс командной строки).

Какая информация может быть получена MediaInfo?
* Общее: title, author, director, album, track number, date, duration...
* Видео: codec, aspect, fps, bitrate...
* Аудио: codec, sample rate, channels, language, bitrate...
* Текст: язык субтитров
* Части: число частей, список частей

DivX, XviD, H263, H.263, H264, x264, ASP, AVC, iTunes, MPEG-1,
MPEG1, MPEG-2, MPEG2, MPEG-4, MPEG4, MP4, M4A, M4V, QuickTime,
RealVideo, RealAudio, RA, RM, MSMPEG4v1, MSMPEG4v2, MSMPEG4v3,
VOB, DVD, WMA, VMW, ASF, 3GP, 3GPP, 3GP2

Какой формат (контейнер) поддерживает MediaInfo?
* Видео: MKV, OGM, AVI, DivX, WMV, QuickTime, Real, MPEG-1,
  MPEG-2, MPEG-4, DVD (VOB) (Codecs: DivX, XviD, MSMPEG4, ASP,
  H.264, AVC...)
* Аудио: OGG, MP3, WAV, RA, AC3, DTS, AAC, M4A, AU, AIFF
* Субтитры: SRT, SSA, ASS, SAMI

%package gui
Summary:    Supplies technical and tag information about a video or audio file (GUI)
Summary(ru):Предоставляет полную информацию о медиа файле (GUI)
Requires:   libzen%{?_isa} >= %{libzen_version}
Requires:   libmediainfo%{?_isa} >= %{version}
Requires:   hicolor-icon-theme

%description gui
MediaInfo (Graphical User Interface).

What information can I get from MediaInfo?
* General: title, author, director, album, track number, date, duration...
* Video: codec, aspect, fps, bitrate...
* Audio: codec, sample rate, channels, language, bitrate...
* Text: language of subtitle
* Chapters: number of chapters, list of chapters

DivX, XviD, H263, H.263, H264, x264, ASP, AVC, iTunes, MPEG-1,
MPEG1, MPEG-2, MPEG2, MPEG-4, MPEG4, MP4, M4A, M4V, QuickTime,
RealVideo, RealAudio, RA, RM, MSMPEG4v1, MSMPEG4v2, MSMPEG4v3,
VOB, DVD, WMA, VMW, ASF, 3GP, 3GPP, 3GP2

What format (container) does MediaInfo support?
* Video: MKV, OGM, AVI, DivX, WMV, QuickTime, Real, MPEG-1,
  MPEG-2, MPEG-4, DVD (VOB) (Codecs: DivX, XviD, MSMPEG4, ASP,
  H.264, AVC...)
* Audio: OGG, MP3, WAV, RA, AC3, DTS, AAC, M4A, AU, AIFF
* Subtitles: SRT, SSA, ASS, SAMI

%description gui -l ru
MediaInfo (графический интерфейс пользователя).

Какая информация может быть получена MediaInfo?
* Общее: title, author, director, album, track number, date, duration...
* Видео: codec, aspect, fps, bitrate...
* Аудио: codec, sample rate, channels, language, bitrate...
* Текст: язык субтитров
* Части: число частей, список частей

DivX, XviD, H263, H.263, H264, x264, ASP, AVC, iTunes, MPEG-1,
MPEG1, MPEG-2, MPEG2, MPEG-4, MPEG4, MP4, M4A, M4V, QuickTime,
RealVideo, RealAudio, RA, RM, MSMPEG4v1, MSMPEG4v2, MSMPEG4v3,
VOB, DVD, WMA, VMW, ASF, 3GP, 3GPP, 3GP2

Какой формат (контейнер) поддерживает MediaInfo?
* Видео: MKV, OGM, AVI, DivX, WMV, QuickTime, Real, MPEG-1,
  MPEG-2, MPEG-4, DVD (VOB) (Codecs: DivX, XviD, MSMPEG4, ASP,
  H.264, AVC...)
* Аудио: OGG, MP3, WAV, RA, AC3, DTS, AAC, M4A, AU, AIFF
* Субтитры: SRT, SSA, ASS, SAMI

%package qt
Summary:    Supplies technical and tag information about a video or audio file (Qt GUI)
Summary(ru):Предоставляет полную информацию о медиа файле (Qt GUI)
Requires:   libzen%{?_isa} >= %{libzen_version}
Requires:   libmediainfo%{?_isa} >= %{version}

%description qt
MediaInfo (Graphical User Interface).

What information can I get from MediaInfo?
* General: title, author, director, album, track number, date, duration...
* Video: codec, aspect, fps, bitrate...
* Audio: codec, sample rate, channels, language, bitrate...
* Text: language of subtitle
* Chapters: number of chapters, list of chapters

DivX, XviD, H263, H.263, H264, x264, ASP, AVC, iTunes, MPEG-1,
MPEG1, MPEG-2, MPEG2, MPEG-4, MPEG4, MP4, M4A, M4V, QuickTime,
RealVideo, RealAudio, RA, RM, MSMPEG4v1, MSMPEG4v2, MSMPEG4v3,
VOB, DVD, WMA, VMW, ASF, 3GP, 3GPP, 3GP2

What format (container) does MediaInfo support?
* Video: MKV, OGM, AVI, DivX, WMV, QuickTime, Real, MPEG-1,
  MPEG-2, MPEG-4, DVD (VOB) (Codecs: DivX, XviD, MSMPEG4, ASP,
  H.264, AVC...)
* Audio: OGG, MP3, WAV, RA, AC3, DTS, AAC, M4A, AU, AIFF
* Subtitles: SRT, SSA, ASS, SAMI

%prep
%autosetup -n MediaInfo

sed -i 's/.$//' *.txt *.html Release/*.txt

find Source -type f -exec chmod 644 {} ';'
chmod 644 *.html *.txt Release/*.txt

#https://fedorahosted.org/FedoraReview/wiki/AutoTools
sed -i 's/AC_PROG_LIBTOOL/LT_INIT/' Project/GNU/*/configure.ac

pushd Project/GNU/CLI
    autoreconf -fiv
    sed -i 's/enable_unicode="$(pkg-config --variable=Unicode libzen)"/enable_unicode=yes/' configure
popd

pushd Project/GNU/GUI
    autoreconf -fiv
    sed -i 's/enable_unicode="$(pkg-config --variable=Unicode libzen)"/enable_unicode=yes/' configure
popd

sed -i 's|TARGET = "mediainfo-gui"|TARGET = "mediainfo-qt"|' Project/QMake/GUI/MediaInfoQt.pro
sed -i 's|-ldl|-ldl -lmediainfo -lzen|' Project/QMake/GUI/MediaInfoQt.pro

%build
# build CLI
pushd Project/GNU/CLI
    %configure --enable-static=no
    %make_build
popd

# now build GUI
pushd Project/GNU/GUI
    %configure --enable-static=no
    %make_build
popd

# now build Qt GUI
pushd Project/QMake/GUI
    %{qmake_qt5}
    %make_build
popd

%install
pushd Project/GNU/CLI
    %make_install
popd

pushd Project/GNU/GUI
    %make_install
popd

pushd Project/QMake/GUI
#     make install INSTALL_ROOT=%{buildroot}
    install -m 755 %{name}-qt %{buildroot}%{_bindir}
popd

# icon
install -dm 755 %{buildroot}%{_datadir}/pixmaps
install -m 644 -p Source/Resource/Image/MediaInfo.png \
    %{buildroot}%{_datadir}/pixmaps/%{name}.png

# menu-entry
install -dm 755 %{buildroot}%{_datadir}/applications
desktop-file-install --dir="%{buildroot}%{_datadir}/applications" \
Project/GNU/GUI/%{name}-gui.desktop
desktop-file-install --dir="%{buildroot}%{_datadir}/applications" %{SOURCE1}
install -m 644 -p %{SOURCE2} %{buildroot}%{_datadir}/kservices5/ServiceMenus/%{name}-qt.desktop
rm -rf %{buildroot}%{_datadir}/kde4
rm %{buildroot}%{_datadir}/kservices5/ServiceMenus/%{name}-gui.desktop

mkdir %{buildroot}%{_datadir}/appdata
mv %{buildroot}%{_datadir}/metainfo/%{name}-gui.metainfo.xml %{buildroot}%{_datadir}/appdata/%{name}-gui.appdata.xml
rm -rf %{buildroot}%{_datadir}/metainfo

%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/*.appdata.xml

%files
%doc Release/ReadMe_CLI_Linux.txt History_CLI.txt
%license License.html
%{_bindir}/%{name}

%files gui
%doc Release/ReadMe_GUI_Linux.txt History_GUI.txt
%{_bindir}/%{name}-gui
%{_datadir}/applications/%{name}-gui.desktop
%{_datadir}/pixmaps/*.png
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/pixmaps/%{name}.xpm
%{_datadir}/apps/konqueror/servicemenus/%{name}-gui.desktop
%{_datadir}/appdata/%{name}-gui.appdata.xml

%files qt
%doc Release/ReadMe_GUI_Linux.txt History_GUI.txt
%{_bindir}/%{name}-qt
%{_datadir}/applications/%{name}-qt.desktop
%{_datadir}/pixmaps/*.png
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/kservices5/ServiceMenus/%{name}-qt.desktop


%changelog
* Thu Aug 13 2020 Vasiliy N. Glazov <vascom2@gmail.com> - 20.08-1
- Update to 20.08

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20.03-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20.03-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Apr 03 2020 Vasiliy N. Glazov <vascom2@gmail.com> - 20.03-1
- Update to 20.03

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 19.09-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 13 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 19.09-1
- Update to 19.09

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 19.07-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 17 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 19.07-1
- Update to 19.07

* Wed Apr 24 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 19.04-1
- Update to 19.04

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 18.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec 13 2018 Vasiliy N. Glazov <vascom2@gmail.com> - 18.12-1
- Update to 18.12

* Tue Sep 11 2018 Vasiliy N. Glazov <vascom2@gmail.com> - 18.08.1-1
- Update to 18.08.1

* Mon Sep 03 2018 Vasiliy N. Glazov <vascom2@gmail.com> - 18.08-1
- Update to 18.08

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 18.05-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 10 2018 Scott Talbert <swt@techie.net> - 18.05-2
- Rebuild with wxWidgets 3.0

* Thu May 10 2018 Vasiliy N. Glazov <vascom2@gmail.com> - 18.05-1
- Update to 18.05

* Tue Mar 20 2018 Vasiliy N. Glazov <vascom2@gmail.com> - 18.03-1
- Update to 18.03

* Thu Mar 08 2018 Rex Dieter <rdieter@fedoraproject.org> - 17.12-3
- Better Qt dep

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 17.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Dec 22 2017 Vasiliy N. Glazov <vascom2@gmail.com> - 17.12-1
- Update to 17.12

* Mon Dec 04 2017 Vasiliy N. Glazov <vascom2@gmail.com> - 17.10-3
- Bump release

* Fri Dec 01 2017 Vasiliy N. Glazov <vascom2@gmail.com> - 17.10-2
- Rebuild due to .so version change

* Thu Nov 09 2017 Vasiliy N. Glazov <vascom2@gmail.com> - 17.10-1
- Update to 17.10
- New versioning scheme

* Wed Sep 13 2017 Vasiliy N. Glazov <vascom2@gmail.com> - 0.7.99-1
- Update to 0.7.99

* Tue Aug 15 2017 Vasiliy N. Glazov <vascom2@gmail.com> - 0.7.98-1
- Update to 0.7.98

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.97-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.97-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 10 2017 Vasiliy N. Glazov <vascom2@gmail.com> - 0.7.97-1
- Update to 0.7.97

* Mon Jun 19 2017 Vasiliy N. Glazov <vascom2@gmail.com> - 0.7.96-1
- Update to 0.7.96

* Wed May 10 2017 Vasiliy N. Glazov <vascom2@gmail.com> - 0.7.95-1
- Update to 0.7.95

* Thu Apr 06 2017 Vasiliy N. Glazov <vascom2@gmail.com> - 0.7.94-1
- Update to 0.7.94

* Mon Mar 06 2017 Vasiliy N. Glazov <vascom2@gmail.com> - 0.7.93-1
- Update to 0.7.93

* Mon Feb 06 2017 Vasiliy N. Glazov <vascom2@gmail.com> - 0.7.92.1-1
- Update to 0.7.92.1

* Mon Dec 05 2016 Vasiliy N. Glazov <vascom2@gmail.com> - 0.7.91-1
- Update to 0.7.91

* Fri Nov 11 2016 Vasiliy N. Glazov <vascom2@gmail.com> - 0.7.90-1
- Update to 0.7.90

* Tue Oct 04 2016 Vasiliy N. Glazov <vascom2@gmail.com> - 0.7.89-1
- Update to 0.7.89

* Thu Sep 15 2016 Vasiliy N. Glazov <vascom2@gmail.com> - 0.7.88-1
- Update to 0.7.88

* Wed Jul 06 2016 Vasiliy N. Glazov <vascom2@gmail.com> - 0.7.87-1
- Update to 0.7.87

* Wed Jun 01 2016 Vasiliy N. Glazov <vascom2@gmail.com> - 0.7.86-1
- Update to 0.7.86

* Thu May 05 2016 Vasiliy N. Glazov <vascom2@gmail.com> - 0.7.85-1
- Update to 0.7.85
- Add validate appdata XML

* Fri Apr 01 2016 Vasiliy N. Glazov <vascom2@gmail.com> - 0.7.84-1
- Update to 0.7.84

* Wed Mar 02 2016 Vasiliy N. Glazov <vascom2@gmail.com> - 0.7.83-1
- Update to 0.7.83

* Mon Feb 08 2016 Vasiliy N. Glazov <vascom2@gmail.com> 0.7.82-1
- Update to 0.7.82

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.81-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Feb 02 2016 Rex Dieter <rdieter@fedoraproject.org> - 0.7.81-2
- use %%qmake_qt4 macro to ensure proper build flags

* Wed Jan 20 2016 Vasiliy N. Glazov <vascom2@gmail.com> 0.7.81-1
- Update to 0.7.81

* Thu Dec 03 2015 Vasiliy N. Glazov <vascom2@gmail.com> 0.7.80-1
- Update to 0.7.80

* Fri Aug 14 2015 Vasiliy N. Glazov <vascom2@gmail.com> 0.7.76-1
- Update to 0.7.76

* Fri Jul 17 2015 Vasiliy N. Glazov <vascom2@gmail.com> 0.7.75-1
- Update to 0.7.75

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.74-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed May 27 2015 Vasiliy N. Glazov <vascom2@gmail.com> 0.7.74-1
- Update to 0.7.74

* Wed Apr 22 2015 Vasiliy N. Glazov <vascom2@gmail.com> - 0.7.73-2
- Rebuild with updated libmediainfo

* Fri Apr 10 2015 Vasiliy N. Glazov <vascom2@gmail.com> 0.7.73-1
- Update to 0.7.73

* Wed Jan 14 2015 Vasiliy N. Glazov <vascom2@gmail.com> 0.7.72-1
- Update to 0.7.72

* Wed Nov 12 2014 Vasiliy N. Glazov <vascom2@gmail.com> 0.7.71-1
- Update to 0.7.71

* Thu Sep 25 2014 Vasiliy N. Glazov <vascom2@gmail.com> 0.7.70-1
- Update to 0.7.69

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.69-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.69-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jun 05 2014 Vasiliy N. Glazov <vascom2@gmail.com> 0.7.69-2
- Add qt GUI subpackage

* Tue Jun 03 2014 Vasiliy N. Glazov <vascom2@gmail.com> 0.7.69-1
- Update to 0.7.69

* Tue Apr 08 2014 Vasiliy N. Glazov <vascom2@gmail.com> 0.7.68-1
- Update to 0.7.68

* Thu Feb 27 2014 Vasiliy N. Glazov <vascom2@gmail.com> 0.7.67-3
- Added resized icons and scriptlets

* Mon Feb 24 2014 Vasiliy N. Glazov <vascom2@gmail.com> 0.7.67-2
- Corrected obsolete m4 macros
- Corrected URL

* Fri Feb 21 2014 Vasiliy N. Glazov <vascom2@gmail.com> 0.7.67-1
- Update to 0.7.67

* Thu Dec 12 2013 Vasiliy N. Glazov <vascom2@gmail.com> 0.7.65-1
- Update to 0.7.65

* Wed Jul 31 2013 Vasiliy N. Glazov <vascom2@gmail.com> 0.7.64-3
- Corrected make flags and use install macros

* Tue Jul 30 2013 Vasiliy N. Glazov <vascom2@gmail.com> 0.7.64-2
- just rebuild

* Fri Jul 12 2013 Vasiliy N. Glazov <vascom2@gmail.com> 0.7.64-1
- update to 0.7.64

* Fri May 31 2013 Vasiliy N. Glazov <vascom2@gmail.com> 0.7.63-1
- update to 0.7.63

* Tue Apr 23 2013 Vasiliy N. Glazov <vascom2@gmail.com> 0.7.62-2
- Removed dos2unix from BR
- Correcting encoding for all files
- Corrected config and build

* Wed Mar 20 2013 Vasiliy N. Glazov <vascom2@gmail.com> 0.7.62-1
- update to 0.7.62

* Tue Oct 23 2012 Vasiliy N. Glazov <vascom2@gmail.com> 0.7.61-1
- Update to 0.7.61

* Mon Sep 03 2012 Vasiliy N. Glazov <vascom2@gmail.com> 0.7.60-1
- Update to 0.7.60

* Tue Jun 05 2012 Vasiliy N. Glazov <vascom2@gmail.com> 0.7.58-1
- Update to 0.7.58

* Fri May 04 2012 Vasiliy N. Glazov <vascom2@gmail.com> 0.7.57-2
- Clean spec

* Fri May 04 2012 Vasiliy N. Glazov <vascom2@gmail.com> 0.7.57-1
- Update to 0.7.57

* Wed Apr 11 2012 Vasiliy N. Glazov <vascom2@gmail.com> 0.7.56-1
- Update to 0.7.56

* Tue Mar 20 2012 Vasiliy N. Glazov <vascom2@gmail.com> 0.7.54-1
- Update to 0.7.54

* Thu Feb 09 2012 Vasiliy N. Glazov <vascom2@gmail.com> 0.7.53-1
- Update to 0.7.53

* Thu Dec 22 2011 Vasiliy N. Glazov <vascom2@gmail.com> 0.7.52-1
- Update to 0.7.52

* Tue Nov 22 2011 Vasiliy N. Glazov <vascom2@gmail.com> 0.7.51-2
- Added description in russian language

* Mon Nov 14 2011 Vasiliy N. Glazov <vascom2@gmail.com> 0.7.51-1
- Update to 0.7.51

* Tue Sep 27 2011 Vasiliy N. Glazov <vascom2@gmail.com> 0.7.50-1
- Update to 0.7.50

* Mon Sep 19 2011 Vasiliy N. Glazov <vascom2@gmail.com> 0.7.49-1
- Update to 0.7.49

* Fri Aug 19 2011 Vasiliy N. Glazov <vascom2@gmail.com> 0.7.48-1
- Update to 0.7.48

* Tue Aug 09 2011 Vasiliy N. Glazov <vascom2@gmail.com> 0.7.47-2
- Removed 0 from name

* Fri Aug 05 2011 Vasiliy N. Glazov <vascom2@gmail.com> 0.7.47-1
- Initial release

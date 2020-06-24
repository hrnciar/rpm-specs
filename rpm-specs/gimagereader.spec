Name:          gimagereader
Version:       3.3.1
Release:       4%{?dist}
Summary:       A front-end to tesseract-ocr

License:       GPLv3+
URL:           https://github.com/manisandro/gimagereader
Source0:       https://github.com/manisandro/gimagereader/releases/download/v%{version}/%{name}-%{version}.tar.xz

BuildRequires: desktop-file-utils
BuildRequires: djvulibre-devel
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: intltool
BuildRequires: make
BuildRequires: podofo-devel
BuildRequires: sane-backends-devel
BuildRequires: tesseract-devel

BuildRequires: cairomm-devel
BuildRequires: libappstream-glib
BuildRequires: libjpeg-turbo-devel
%if 0%{fedora} > 26
BuildRequires: libxml++30-devel
%else
BuildRequires: libxml++-devel
%endif
BuildRequires: libuuid-devel
BuildRequires: libzip-devel
BuildRequires: gtkmm30-devel
BuildRequires: gtksourceviewmm3-devel
BuildRequires: gtkspellmm30-devel
BuildRequires: json-glib-devel
BuildRequires: poppler-glib-devel
BuildRequires: python3-gobject

BuildRequires: poppler-qt5-devel
BuildRequires: qt5-qtbase-devel
BuildRequires: qtspell-qt5-devel
BuildRequires: quazip-qt5-devel

Requires:      hicolor-icon-theme
Requires:      gvfs

%description
gImageReader is a simple front-end to tesseract. Features include:
 - Import PDF documents and images from disk, scanning devices, clipboard and screenshots
 - Process multiple images and documents in one go
 - Manual or automatic recognition area definition
 - Recognize to plain text or to hOCR documents
 - Recognized text displayed directly next to the image
 - Post-process the recognized text, including spellchecking
 - Generate PDF documents from hOCR documents


%package gtk
Summary:       A Gtk+ front-end to tesseract-ocr
Requires:      %{name}-common = %{version}-%{release}
Obsoletes:     %{name} < 2.94-1

%description gtk
gImageReader is a simple front-end to tesseract. Features include:
 - Import PDF documents and images from disk, scanning devices, clipboard and screenshots
 - Process multiple images and documents in one go
 - Manual or automatic recognition area definition
 - Recognize to plain text or to hOCR documents
 - Recognized text displayed directly next to the image
 - Post-process the recognized text, including spellchecking
 - Generate PDF documents from hOCR documents
This package contains the Gtk+ front-end.


%package qt
Summary:       A Qt front-end to tesseract-ocr
Requires:      %{name}-common = %{version}-%{release}

%description qt
gImageReader is a simple front-end to tesseract. Features include:
 - Import PDF documents and images from disk, scanning devices, clipboard and screenshots
 - Process multiple images and documents in one go
 - Manual or automatic recognition area definition
 - Recognize to plain text or to hOCR documents
 - Recognized text displayed directly next to the image
 - Post-process the recognized text, including spellchecking
 - Generate PDF documents from hOCR documents
This package contains the Qt front-end.

%package common
Summary:       Common files for %{name}
BuildArch:     noarch

%description common
Common files for %{name}.


%prep
%autosetup -p1


%build
mkdir build_gtk
(
cd build_gtk
%cmake -DINTERFACE_TYPE=gtk -DENABLE_VERSIONCHECK=0 -DMANUAL_DIR="%{_defaultdocdir}/%{name}-common" ..
%make_build
)
mkdir build_qt
(
cd build_qt
%cmake -DINTERFACE_TYPE=qt5 -DENABLE_VERSIONCHECK=0 -DMANUAL_DIR="%{_defaultdocdir}/%{name}-common" ..
%make_build
)


%install
%make_install -C build_gtk
%make_install -C build_qt
%{_bindir}/desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}-gtk.desktop
%{_bindir}/desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}-qt5.desktop
%{_bindir}/appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/%{name}-gtk.appdata.xml
%{_bindir}/appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/%{name}-qt5.appdata.xml

%find_lang %{name}


%files common -f %{name}.lang
%license COPYING
%doc AUTHORS NEWS README.md
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
%{_datadir}/icons/hicolor/256x256/apps/%{name}.png
%doc %{_defaultdocdir}/%{name}-common/manual*.html

%files gtk
%{_bindir}/%{name}-gtk
%{_datadir}/metainfo/%{name}-gtk.appdata.xml
%{_datadir}/applications/%{name}-gtk.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.%{name}.gschema.xml

%files qt
%{_bindir}/%{name}-qt5
%{_datadir}/metainfo/%{name}-qt5.appdata.xml
%{_datadir}/applications/%{name}-qt5.desktop

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Marek Kasik <mkasik@redhat.com> - 3.3.1-3
- Rebuild for poppler-0.84.0

* Sat Dec 28 2019 Sandro Mani <manisandro@gmail.com> - 3.3.1-2
- Rebuild (tesseract)

* Sun Jul 28 2019 Sandro Mani <manisandro@gmail.com> - 3.3.1-1
- Update to 3.3.1

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 01 2019 Sandro Mani <manisandro@gmail.com> - 3.3.0-4
- Fix crash when opening language manager
- Add requires: gvfs

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 14 2018 Sandro Mani <manisandro@gmail.com> - 3.3.0-2
- Rebuild (tesseract)

* Wed Sep 26 2018 Sandro Mani <manisandro@gmail.com> - 3.3.0-1
- Update to 3.3.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.99-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Sandro Mani <manisandro@gmail.com> - 3.2.99-3
- Rebuild (podofo)

* Fri Mar 23 2018 Marek Kasik <mkasik@redhat.com> - 3.2.99-2
- Rebuild for poppler-0.63.0

* Sun Feb 25 2018 Sandro Mani <manisandro@gmail.com> - 3.2.99-1
- Update to 3.2.99

* Sun Feb 18 2018 Sandro Mani <manisandro@gmail.com> - 3.2.3-6
- Add missing BR: gcc-c++, make

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.2.3-4
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jul 01 2017 Sandro Mani <manisandro@gmail.com> - 3.2.3-1
- Update to 3.2.3

* Fri Jun 30 2017 Sandro Mani <manisandro@gmail.com> - 3.2.2-1
- Update to 3.2.2

* Wed May 17 2017 Sandro Mani <manisandro@gmail.com> - 3.2.1-4
- Backport patch to fix some icons missing in Gtk interface (#1451357)

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Tue Feb 21 2017 Sandro Mani <manisandro@gmail.com> - 3.2.1-2
- Rebuild (tesseract)

* Fri Feb 10 2017 Sandro Mani <manisandro@gmail.com> - 3.2.1-1
- Update to 3.2.1

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 03 2017 Sandro Mani <manisandro@gmail.com> - 3.2.0-2
- Rebuild (podofo)

* Wed Nov 23 2016 Sandro Mani <manisandro@gmail.com> - 3.2.0-1
- Update to 3.2.0

* Fri Oct 14 2016 Sandro Mani <manisandro@gmail.com> - 3.1.99-1
- Update to 3.1.99

* Tue May 03 2016 Sandro Mani <manisandro@gmail.com> - 3.1.91-1
- Update to 3.1.91

* Thu Apr 28 2016 Sandro Mani <manisandro@gmail.com> - 3.1.90-1
- Update to 3.1.90

* Thu Feb 04 2016 Sandro Mani <manisandro@gmail.com> - 3.1.2-5
- Add patch to fix FTBFS

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Oct 16 2015 Sandro Mani <manisandro@gmail.com> - 3.1.2-3
- Rebuild (tesseract)

* Wed Oct 14 2015 Sandro Mani <manisandro@gmail.com> - 3.1.2-2
- Rebuild (tesseract)

* Tue Jun 30 2015 Sandro Mani <manisandro@gmail.com> - 3.1.2-1
- Update to 3.1.2

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 11 2015 Sandro Mani <manisandro@gmail.com> - 3.1.1-1
- Update to 3.1.1

* Fri May 01 2015 Sandro Mani <manisandro@gmail.com> - 3.1-1
- Update to 3.1

* Sun Jan 04 2015 Sandro Mani <manisandro@gmail.com> - 3.0.1-1
- Update to 3.0.1.

* Mon Dec 15 2014 Sandro Mani <manisandro@gmail.com> - 3.0-1
- Update to 3.0.

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.93-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Aug 13 2014 Sandro Mani <manisandro@gmail.com> - 2.93-4
- Rebuild (tesseract)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.93-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun May 04 2014 Sandro Mani <manisandro@gmail.com> - 2.93-2
- Workaround rhbz #1065695

* Wed Apr 30 2014 Sandro Mani <manisandro@gmail.com> - 2.93-1
- Update to 2.93

* Wed Mar 19 2014 Sandro Mani <manisandro@gmail.com> - 2.92-1
- Update to 2.92

* Thu Feb 20 2014 Sandro Mani <manisandro@gmail.com> - 2.91-1
- Update to 2.91

* Sat Feb 15 2014 Sandro Mani <manisandro@gmail.com> - 2.91-0.2git20140216
- Update to newer 2.91 pre, work around crash at exit

* Thu Feb 13 2014 Sandro Mani <manisandro@gmail.com> - 2.91-0.1
- Update to 2.91 pre

* Thu Feb 13 2014 Sandro Mani <manisandro@gmail.com> - 2.90-3
- Require hicolor-icon-theme
- Add missing icon theme scriptlets

* Wed Feb 12 2014 Sandro Mani <manisandro@gmail.com> - 2.90-2
- Add appdata file

* Tue Feb 11 2014 Sandro Mani <manisandro@gmail.com> - 2.90-1
- Initial package.

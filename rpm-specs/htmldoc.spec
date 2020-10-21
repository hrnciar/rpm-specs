Name:		htmldoc
Version:	1.9.7
Release:	3%{?dist}
Summary:	Converter from HTML into indexed HTML, PostScript, or PDF

# GPLv2 with OpenSSL exception
License:	GPLv2 with exceptions
URL:		https://michaelrsweet.github.io/htmldoc
Source0:  	https://github.com/michaelrsweet/htmldoc/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

## upstream patches
# fix for  CVE-2019-19630 (#1783940)
Patch10: 0010-Fix-a-buffer-underflow-issue-with-GCC-on-Linux-Issue.patch

# NEEDSWORK: use Fedora system fonts
Patch200:  	htmldoc-1.9.1-system_fonts.patch

Patch100: htmldoc-1.9.1-Makedefs.patch

%global urw_fonts urw-base35-fonts
%if 0%{?fedora} < 27
%global urw_fonts urw-fonts
%endif

# uses clang (in preference to gcc) if present
BuildConflicts: clang

BuildRequires: desktop-file-utils

BuildRequires: fontpackages-devel
BuildRequires: gcc-c++
BuildRequires: gnutls-devel
BuildRequires: libjpeg-devel
BuildRequires: libpng-devel
BuildRequires: libXpm-devel
BuildRequires: fltk-devel
BuildRequires: zlib-devel

# fonts.  not used, yet.  see system_fonts
BuildRequires: dejavu-sans-fonts dejavu-sans-mono-fonts dejavu-serif-fonts
BuildRequires: %{urw_fonts}
BuildRequires: ttf2pt1 t1utils

Requires: dejavu-sans-fonts dejavu-sans-mono-fonts dejavu-serif-fonts
Requires: %{urw_fonts}
Requires: ttf2pt1 t1utils


%description
HTMLDOC converts HTML source files into indexed HTML, PostScript, or
Portable Document Format (PDF) files that can be viewed online or
printed. With no options a HTML document is produced on stdout.

The second form of HTMLDOC reads HTML source from stdin, which allows
you to use HTMLDOC as a filter.

The third form of HTMLDOC launches a graphical interface that allows
you to change options and generate documents interactively.


%prep
%setup -q

%patch10 -p1 -b 0010

%patch100 -p1 -b .Makedefs

%if 0%{?system_fonts}
%patch200 -p1 -b .system_fonts
pushd fonts
rm -f *.pfa *.afm
ln -s %{_fontbasedir}/default/Type1/n022003l.afm Courier.afm
ln -s %{_fontbasedir}/default/Type1/n022004l.afm Courier-Bold.afm
ln -s %{_fontbasedir}/default/Type1/n022024l.afm Courier-BoldOblique.afm
ln -s %{_fontbasedir}/default/Type1/n022024l.pfb Courier-BoldOblique.pfb
ln -s %{_fontbasedir}/default/Type1/n022004l.pfb Courier-Bold.pfb
ln -s %{_fontbasedir}/default/Type1/n022023l.afm Courier-Oblique.afm
ln -s %{_fontbasedir}/default/Type1/n022023l.pfb Courier-Oblique.pfb
ln -s %{_fontbasedir}/default/Type1/n022003l.pfb Courier.pfb
ln -s %{_fontbasedir}/default/Type1/d050000l.afm Dingbats.afm
ln -s %{_fontbasedir}/default/Type1/d050000l.pfb Dingbats.pfb
ln -s %{_fontbasedir}/default/Type1/n019003l.afm Helvetica.afm
ln -s %{_fontbasedir}/default/Type1/n019004l.afm Helvetica-Bold.afm
ln -s %{_fontbasedir}/default/Type1/n019024l.afm Helvetica-BoldOblique.afm
ln -s %{_fontbasedir}/default/Type1/n019024l.pfb Helvetica-BoldOblique.pfb
ln -s %{_fontbasedir}/default/Type1/n019004l.pfb Helvetica-Bold.pfb
ln -s %{_fontbasedir}/default/Type1/n019023l.afm Helvetica-Oblique.afm
ln -s %{_fontbasedir}/default/Type1/n019023l.pfb Helvetica-Oblique.pfb
ln -s %{_fontbasedir}/default/Type1/n019003l.pfb Helvetica.pfb
ln -s %{_fontbasedir}/default/Type1/s050000l.afm Symbol.afm
ln -s %{_fontbasedir}/default/Type1/s050000l.pfb Symbol.pfb
ln -s %{_fontbasedir}/default/Type1/n021004l.afm Times-Bold.afm
ln -s %{_fontbasedir}/default/Type1/n021024l.afm Times-BoldItalic.afm
ln -s %{_fontbasedir}/default/Type1/n021024l.pfb Times-BoldItalic.pfb
ln -s %{_fontbasedir}/default/Type1/n021004l.pfb Times-Bold.pfb
ln -s %{_fontbasedir}/default/Type1/n021023l.afm Times-Italic.afm
ln -s %{_fontbasedir}/default/Type1/n021023l.pfb Times-Italic.pfb
ln -s %{_fontbasedir}/default/Type1/n021003l.afm Times-Roman.afm
ln -s %{_fontbasedir}/default/Type1/n021003l.pfb Times-Roman.pfb
ln -s %{_fontbasedir}/dejavu/DejaVuSans-BoldOblique.ttf
ln -s %{_fontbasedir}/dejavu/DejaVuSans-Bold.ttf
ln -s %{_fontbasedir}/dejavu/DejaVuSansMono-BoldOblique.ttf
ln -s %{_fontbasedir}/dejavu/DejaVuSansMono-Bold.ttf
ln -s %{_fontbasedir}/dejavu/DejaVuSansMono-Oblique.ttf
ln -s %{_fontbasedir}/dejavu/DejaVuSansMono.ttf
ln -s %{_fontbasedir}/dejavu/DejaVuSans-Oblique.ttf
ln -s %{_fontbasedir}/dejavu/DejaVuSans.ttf
ln -s %{_fontbasedir}/dejavu/DejaVuSerif-BoldItalic.ttf
ln -s %{_fontbasedir}/dejavu/DejaVuSerif-Bold.ttf
ln -s %{_fontbasedir}/dejavu/DejaVuSerif-Italic.ttf
ln -s %{_fontbasedir}/dejavu/DejaVuSerif.ttf
popd
%endif


%build
%configure \
 --enable-gnutls=yes

make %{?_smp_mflags} VERBOSE=1


%install
make install \
  BUILDROOT=%{buildroot} \
  VERBOSE=1

# install icons
for s in 32 128; do
  install -p -m644 -D desktop/htmldoc-$s.png \
    %{buildroot}%{_datadir}/icons/hicolor/${s}x${s}/apps/htmldoc.png;
done

# desktop file
desktop-file-edit \
  --remove-category=X-Red-Hat-Base \
  --add-mime-type=application/vnd.htmldoc-book \
  %{buildroot}%{_datadir}/applications/htmldoc.desktop

## unpackaged files
rm -rf %{buildroot}%{_datadir}/pixmaps/
rm -fv %{buildroot}%{_pkgdocdir}/htmldoc/*

%files
#doc doc/intro.html doc/c-relnotes.html
%doc doc/htmldoc.{html,pdf} doc/help.html
%doc README.md
%license COPYING
%{_bindir}/htmldoc
%{_datadir}/htmldoc/
%{_datadir}/applications/htmldoc.desktop
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/mime/packages/htmldoc.xml
%{_mandir}/man1/htmldoc.1*


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Dec 17 2019 Rex Dieter <rdieter@fedoraproject.org> - 1.9.7-1
- 1.9.7
- fix for  CVE-2019-19630 (#1783940)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Feb 20 2018 Rex Dieter <rdieter@fedoraproject.org> - 1.9.1-2
- BR: gcc-c++

* Mon Feb 12 2018 Rex Dieter <rdieter@fedoraproject.org> - 1.9.1-1
- htmldoc-1.9.1
- s/urw-fonts/urw-base35-fonts/ (f27+)
- .spec cosmetics

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.28-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.28-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.28-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.28-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.28-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.28-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.8.28-7
- Rebuilt for GCC 5 C++11 ABI change

* Thu Feb 19 2015 Rex Dieter <rdieter@fedoraproject.org> 1.8.28-6
- rebuild (fltk)

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.28-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Aug 09 2014 Rex Dieter <rdieter@fedoraproject.org> 1.8.28-4
- fixdso.patch no longer needed

* Sat Aug 09 2014 Rex Dieter <rdieter@fedoraproject.org> 1.8.28-3
- optimize/update scriptlets

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 14 2014 Rex Dieter <rdieter@fedoraproject.org> 1.8.28-1
- htmldoc-1.8.28

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.27-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Apr 24 2013 Jon Ciesla <limburgher@gmail.com> - 1.8.27-24
- Drop desktop vendor tag.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.27-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 18 2013 Adam Tkac <atkac redhat com> - 1.8.27-22
- rebuild due to "jpeg8-ABI" feature drop

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 1.8.27-21
- rebuild against new libjpeg

* Sat Sep  1 2012 Daniel Drake <dsd@laptop.org> - 1.8.27-20
- fix libpng-1.5 patch to not corrupt images

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.27-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Rex Dieter <rdieter@fedoraproject.org> 1.8.27-18
- fix build against libpng-1.5

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.27-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 1.8.27-16
- Rebuild for new libpng

* Tue Jun 14 2011 Peter Robinson <pbrobinson@gmail.com> - 1.8.27-15
- Fix DSO linking so htmldoc actually compiles and works - RHBZ 631135 and others

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.27-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 1.8.27-13
- rebuilt with new openssl

* Thu Aug 13 2009 Adam Goode <adam@spicenitz.org> - 1.8.27-12
- Fix limitation of -D_FORTIFY_SOURCE=2 (#511520)
- Fix scanf overflows (#512513)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.27-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.27-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 10 2009 Adam Goode <adam@spicenitz.org> - 1.8.27-9
- Patch to specify Dingbats as a standard PS and PDF font
- Use system fonts to conform to new font guidelines (#477397)

* Fri Jan 16 2009 Tomas Mraz <tmraz@redhat.com> - 1.8.27-8
- rebuild with new openssl

* Sat Aug 30 2008 Adam Goode <adam@spicenitz.org> - 1.8.27-7
- RPM 4.6 fix for patch tag

* Sat Feb  9 2008 Adam Goode <adam@spicenitz.org> - 1.8.27-6
- GCC 4.3 mass rebuild

* Wed Dec  5 2007 Adam Goode <adam@spicenitz.org> - 1.8.27-5
- Fix desktop file validation

* Wed Dec 05 2007 Release Engineering <rel-eng at fedoraproject dot org> - 1.8.27-4
 - Rebuild for deps

* Wed Aug 22 2007 Adam Goode <adam@spicenitz.org> - 1.8.27-3
- Update license tag
- Rebuild for buildid

* Sat May  5 2007 Adam Goode <adam@spicenitz.org> - 1.8.27-2
- Remove X-Fedora

* Thu Aug 31 2006 Adam Goode <adam@spicenitz.org> - 1.8.27-1.1
- Mass rebuild

* Wed Aug  2 2006 Adam Goode <adam@spicenitz.org> - 1.8.27-1
- New upstream release

* Wed May 31 2006 Adam Goode <adam@spicenitz.org> - 1.8.26-4
- Fix hardcoded documentation path in configure
- Add help.html to documentation

* Mon May 29 2006 Adam Goode <adam@spicenitz.org> - 1.8.26-3
- Use upstream desktop file
- Install icons
- Install mime XML file
- Eliminate strange spaces in description

* Sat May 27 2006 Adam Goode <adam@spicenitz.org> - 1.8.26-2
- Add downloadable source

* Thu May 25 2006 Adam Goode <adam@spicenitz.org> - 1.8.26-1
- New upstream release
- Rebuild for FC5

* Mon Oct 24 2005 Thomas Chung <tchung@fedoranews.org> 1.8.24-1
- Rebuild for FC4

* Tue Feb 22 2005 Thomas Chung <tchung@fedoranews.org> 1.8.24-0
- Initial RPM build for FC3

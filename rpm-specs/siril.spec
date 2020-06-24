%global _default_patch_fuzz 2

Name:           siril
Version:        0.9.12
Release:        7%{?dist}
Summary:        Astronomical image processing software

License:        GPLv3+
URL:            http://free-astro.org/index.php/Siril
Source0:        https://free-astro.org/download/%{name}-%{version}.tar.bz2
# Upstream patch https://gitlab.com/free-astro/siril/issues/424
Patch0:         fixing-gcc10-compilation-and-some-warnings-fixes-424.patch

# Notes on dependencies:
# No ffmpeg and ffms support 

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  curl-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(cfitsio)
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(gsl)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libconfig)
%if %{?fedora} > 27
BuildRequires:  giflib-devel
%endif
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libraw)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(opencv) 

%description
Siril is an image processing tool specially tailored for noise reduction and
improving the signal/noise ratio of an image from multiple captures, as
required in astronomy. Siril can align automatically or manually, stack and
enhance pictures from various file formats, even images sequences (movies and
SER files)

Note: This version is built without ffmpeg support due to Fedora software 
      guidelines.


%prep
%autosetup -p1

%build
intltoolize -f -c
autoreconf -fi -Wno-portability
%configure
%make_build


%install
%make_install

desktop-file-install						\
	--dir=%{buildroot}%{_datadir}/applications		\
	platform-specific/linux/org.free_astro.siril.desktop

%find_lang %{name}


%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/org.free_astro.siril.appdata.xml

%files -f %{name}.lang
%license LICENSE.md
%doc AUTHORS ChangeLog NEWS README.md
%{_bindir}/%{name}
%{_datadir}/applications/org.free_astro.siril.desktop
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/mimetypes/text-x-seq.svg
%{_datadir}/metainfo/org.free_astro.siril.appdata.xml
%{_datadir}/%{name}/
%{_mandir}/man1/%{name}.1.gz
# license is packaged with %%license
%exclude %{_pkgdocdir}/LICENSE.md

%changelog
* Thu Jun 04 2020 Nicolas Chauvet <kwizart@gmail.com> - 0.9.12-7
- Rebuilt for OpenCV 4.3

* Mon May 11 2020 Gwyn Ciesla <gwync@protonmail.com> - 0.9.12-6
- Rebuild for new LibRaw

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 29 2020 Nicolas Chauvet <kwizart@gmail.com> - 0.9.12-4
- Add upstream patch to fix compilation

* Tue Jan 28 2020 Nicolas Chauvet <kwizart@gmail.com> - 0.9.12-3
- Rebuild for OpenCV 4.2

* Sun Dec 29 2019 Nicolas Chauvet <kwizart@gmail.com> - 0.9.12-2
- Rebuilt for opencv4

* Wed Nov 06 2019 Christian Dersch <lupinix@fedoraproject.org> - 0.9.12-1
- new version

* Tue Aug 20 2019 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.9.11-3
- Rebuilt for GSL 2.6.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 08 2019 Christian Dersch <lupinix@fedoraproject.org> - 0.9.11-1
- new version

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 24 2019 Christian Dersch - 0.9.10-1
- new version

* Tue Jul 24 2018 Adam Williamson <awilliam@redhat.com> - 0.9.9-6
- Rebuild for new libconfig

* Thu Jul 19 2018 Christian Dersch <lupinix@fedoraproject.org> - 0.9.9-5
- Rebuilt for LibRaw soname bump

* Tue Jul 17 2018 Christian Dersch <lupinix@fedoraproject.org> - 0.9.9-4
- BuildRequires: gcc-c++

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 03 2018 Christian Dersch <lupinix.fedora@gmail.com> - 0.9.9-2
- Fix #1588442 with siril-0.9.9-fix-build-glibc2.28.patch

* Fri Jun 15 2018 Christian Dersch <lupinix.fedora@gmail.com> - 0.9.9-1
- new version

* Sat May 26 2018 Christian Dersch <lupinix@mailbox.org> - 0.9.8.3-4
- rebuilt for cfitsio 3.450

* Sun Mar 04 2018 Christian Dersch <lupinix@mailbox.org> - 0.9.8.3-3
- new dependency: curl-devel/curl

* Fri Mar 02 2018 Christian Dersch <lupinix@mailbox.org> - 0.9.8.3-2
- rebuild for opencv 3.4.1

* Fri Feb 23 2018 Christian Dersch <lupinix@mailbox.org> - 0.9.8.3-1
- new version

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Christian Dersch <lupinix@mailbox.org> - 0.9.8-1
- new version

* Mon Dec 25 2017 Christian Dersch <lupinix@fedoraproject.org> - 0.9.7-2
- rebuilt (opencv)

* Thu Sep 21 2017 Christian Dersch <lupinix@mailbox.org> - 0.9.7-1
- new version

* Sat Aug 05 2017 Christian Dersch <lupinix@mailbox.org> - 0.9.6-4
- Rebuild (gsl)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 23 2017 Christian Dersch <lupinix@mailbox.org> - 0.9.6-1
- new version

* Thu Mar 02 2017 Christian Dersch <lupinix@mailbox.org> - 0.9.5-4
- rebuilt for opencv-3.2.0

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Dec 28 2016 Jon Ciesla <limburgher@gmail.com> - 0.9.5-2
- Rebuild for new LibRaw.

* Tue Nov 29 2016 Christian Dersch <lupinix@mailbox.org> - 0.9.5-1
- new version

* Fri Oct 14 2016 Christian Dersch <lupinix@mailbox.org> - 0.9.4-3
- Rebuilt

* Fri Oct 14 2016 Christian Dersch <lupinix@mailbox.org> - 0.9.4-2
- fix scriptlets, use update-desktop-database only for Fedora < 25

* Fri Oct 14 2016 Christian Dersch <lupinix@mailbox.org> - 0.9.4-1
- update to version 0.9.4
- complete rework of the package

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Lubomir Rintel <lkundrak@v3.sk> - 0.8-17
- Fix format string security error
- Deal with the compile warnings
- Actually rebuild for the new cfitsio

* Fri Jan 10 2014 Orion Poplawski <orion@cora.nwra.com> - 0.8-16
- Rebuild for cfitsio 3.360

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Mar 30 2013 Kevin Fenzi <kevin@scrye.com> - 0.8-14
- Rebuild for broken deps in rawhide

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Aug 3 2009 Lubomir Rintel <lkundrak@v3.sk> - 0.8-9
- Fix build
- Fix out of string bound writes (#494536)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Apr 4 2009 Lubomir Rintel <lkundrak@v3.sk> - 0.8-7
- Fix crash on incorrectly loaded pictures (#494536)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Aug 29 2008 Michael Schwendt <mschwendt@fedoraproject.org> - 0.8-5
- Include unowned directories

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.8-4
- Autorebuild for GCC 4.3

* Sat Nov 24 2007 Marek Mahut <mmahut@fedoraproject.org> - 0.8-3
- Initial build.

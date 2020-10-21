%global github_owner    nomacs
# https://github.com/nomacs/nomacs/issues/530
%global git_build    224

Name:		nomacs
Summary:	Lightweight image viewer
Version:	3.16
Release:	1%{?dist}
License:	GPLv3+ and CC-BY
Url:		http://nomacs.org
Source0:	https://github.com/%{github_owner}/%{name}/archive/%{version}.%{build}.tar.gz/%{name}-%{version}.%{git_build}.tar.gz
Source1:	https://github.com/%{github_owner}/%{name}-plugins/archive/%{version}.tar.gz/%{name}-plugins-%{version}.tar.gz
# desktop entries rename (https://github.com/nomacs/nomacs/issues/528)
Patch0:		%{name}-%{version}.%{git_build}-desktop.diff
# plugins search path (https://github.com/nomacs/nomacs/issues/531)
Patch1:		%{name}-%{version}.%{git_build}-pluginspath.diff
# plugins install path (https://github.com/nomacs/nomacs-plugins/issues/34)
Patch2:		%{name}-plugins-%{version}-instpath.diff
BuildRequires:	gcc-c++
BuildRequires:	cmake
BuildRequires:	desktop-file-utils
BuildRequires:	qt5-linguist
BuildRequires:	cmake(Qt5Gui)
# qt5-qtsvg-devel
BuildRequires:	cmake(Qt5Svg)
# exiv2-devel
BuildRequires:	pkgconfig(exiv2) >= 0.20
# opencv-devel
BuildRequires:	pkgconfig(opencv) >= 2.1.0
# LibRaw-devel
BuildRequires:	pkgconfig(libraw) >= 0.12.0
# libtiff-devel
BuildRequires:	pkgconfig(libtiff-4)
# libwebp-devel >= 0.3.1
BuildRequires:	pkgconfig(libwebp)
# quazip-qt5-devel >= 0.7
BuildRequires:	quazip-qt5-devel
# libheif-devel (rpmfusion-free)
# BuildRequires:	pkgconfig(libheif)
BuildRequires:	lcov

%description
nomacs is image viewer based on Qt5 library.
nomacs is small, fast and able to handle the most common image formats.
Additionally it is possible to synchronize multiple viewers
running on the same computer or via LAN is possible.
It allows to compare images and spot the differences
e.g. schemes of architects to show the progress).

%package	plugins
Summary:	Plugins for nomacs image viewer.
Requires:	%{name} = %{version}-%{release}

%description	plugins
Some usefull plugins for nomacs:
- Affine transformations
- RGB image from greyscales
- Fake miniature filter
- Page extractions
- Painting


%prep
%setup -n %{name}-%{version}.%{git_build}
%patch0
%patch1
%setup -T -D -a 1 -n %{name}-%{version}.%{git_build}
# plug them in
mv nomacs-plugins-%{version}/* ImageLounge/plugins/
%patch2
# Be sure
rmdir {3rd-party/*,3rd-party}
# wrong lang code (https://github.com/nomacs/nomacs/issues/529)
rm -fv ImageLounge/translations/nomacs_als.ts


%build
%cmake ImageLounge \
  -DCMAKE_BUILD_TYPE=Release\
  -DENABLE_RAW=1 \
  -DUSE_SYSTEM_WEBP=ON \
  -DUSE_SYSTEM_QUAZIP=ON \
  -DENABLE_TRANSLATIONS=ON
#  -DENABLE_HEIF=1
%{cmake_build}


%install
%{cmake_install}
%find_lang %{name} --with-qt --without-mo
# workaround errors wrt to spaces
sed -i -e 's|Image Lounge|Image?Lounge|g' %{name}.lang


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop


%files -f %{name}.lang
%license ImageLounge/license/*
%doc README.md
%{_bindir}/%{name}
%{_libdir}/libnomacsCore.so*
%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/Image?Lounge/themes/
%dir %{_datadir}/%{name}/Image?Lounge/
%dir %{_datadir}/%{name}/Image?Lounge/translations/
%{_metainfodir}/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_mandir}/man1/%{name}.*

%files	plugins
%license ImageLounge/license/*
%{_libdir}/nomacs-plugins/


%changelog
* Fri Aug 07 2020 TI_Eugene <ti.eugene@gmail.com> 3.16-1
- Version bump
- Plugins added
- Spec fixes against F33

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.14.2-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.14.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 04 2020 Nicolas Chauvet <kwizart@gmail.com> - 3.14.2-3
- Rebuilt for OpenCV 4.3

* Mon May 11 2020 Gwyn Ciesla <gwync@protonmail.com> - 3.14.2-2
- Rebuild for new LibRaw

* Thu Apr 23 2020 TI_Eugene <ti.eugene@gmail.com> 3.14.2-1
- Version bump

* Sat Mar 14 2020 TI_Eugene <ti.eugene@gmail.com> 3.14-1
- Version bump
- All patches removed
- lena.jpg workaround removed

* Fri Mar 06 2020 Nicolas Chauvet <kwizart@gmail.com> - 3.12-7
- Rebuilt for opencv-4.2

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 28 2020 Nicolas Chauvet <kwizart@gmail.com> - 3.12-5
- Rebuild for OpenCV 4.2

* Mon Jan 27 2020 Nicolas Chauvet <kwizart@gmail.com> - 3.12-4
- Add patch for OpenCV 4.2

* Sun Dec 29 2019 Nicolas Chauvet <kwizart@gmail.com> - 3.12-3
- Rebuilt for opencv4

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 22 2019 Rex Dieter <rdieter@fedoraproject.org> - 3.12-1
- nomacs-3.12 (#1597451)
- fixes FTBFS issues (#1671159, #1675548)

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.1-0.5.20180223git9b305e2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 30 2019 Rex Dieter <rdieter@fedoraproject.org> - 3.8.1-0.4.20180223git9b305e2
- rebuild (exiv2)

* Thu Jul 19 2018 Adam Williamson <awilliam@redhat.com> - 3.8.1-0.3.20180223git9b305e2
- Rebuild for new libraw

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.1-0.2.20180223git9b305e2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 05 2018 Adam Williamson <awilliam@redhat.com> - 3.8.1-0.1.20180223git9b305e2
- Update to latest git for bug and compile fixes
- Use a cleaned tarball again, add script for producing cleaned tarball

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 07 2018 TI_Eugene <ti.eugene@gmail.com> 3.8.0-1
- Version bump
- lcov dependency added

* Sun Jan 07 2018 Sérgio Basto <sergio@serjux.com> - 3.6.1-6
- Rebuild (opencv-3.3.1)

* Thu Nov 30 2017 Pete Walter <pwalter@fedoraproject.org> - 3.6.1-5
- Rebuild for ICU 60.1

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 02 2017 Rex Dieter <rdieter@fedoraproject.org> - 3.6.1-2
- rebuild (exiv2)

* Sat Mar 25 2017 TI_Eugene <ti.eugene@gmail.com> 3.6.1-1
- Version bump

* Mon Mar 20 2017 Tom Callaway <spot@fedoraproject.org> - 3.4-4
- replace non-free lena files with CC-BY licensed image

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 27 2016 Jon Ciesla <limburgher@gmail.com> 3.4.0-2
- Rebuild for new LibRaw.

* Mon Jul 25 2016 TI_Eugene <ti.eugene@gmail.com> 3.4.0-1
- Version bump

* Sat May 21 2016 TI_Eugene <ti.eugene@gmail.com> 3.2.0-2
- Rawhide patch

* Thu Apr 28 2016 TI_Eugene <ti.eugene@gmail.com> 3.2.0-1
- Version bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 07 2016 TI_Eugene <ti.eugene@gmail.com> 3.0.0-3
- "Requires" added (qt5-qtsvg, libicu)

* Tue Dec 29 2015 Kalev Lember <klember@redhat.com> - 3.0.0-2
- Rebuilt for libwebp soname bump

* Fri Dec 18 2015 TI_Eugene <ti.eugene@gmail.com> 3.0.0-1
- Version bump

* Thu Aug 20 2015 Jon Ciesla <limburgher@gmail.com> - 2.6.4-2
- Rebuild for new LibRaw.

* Thu Aug 20 2015 TI_Eugene <ti.eugene@gmail.com> 2.6.4-1
- Version bump

* Wed Jun 24 2015 Rex Dieter <rdieter@fedoraproject.org> - 2.4.4-3
- rebuild (exiv2)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr 15 2015 TI_Eugene <ti.eugene@gmail.com> 2.4.4-1
- Version bump

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 2.4.2-3
- Add an AppData file for the software center

* Tue Mar 03 2015 TI_Eugene <ti.eugene@gmail.com> 2.4.2-2
- Version bump.

* Sun Nov 16 2014 TI_Eugene <ti.eugene@gmail.com> 2.2.0-2
- Use system libwebp and quazip.

* Thu Nov 13 2014 TI_Eugene <ti.eugene@gmail.com> 2.2.0-1
- Version bump.

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jul 31 2014 TI_Eugene <ti.eugene@gmail.com> 2.0.2-1
- Version bump.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Feb 21 2014 TI_Eugene <ti.eugene@gmail.com> 1.6.4-1
- Version bump.

* Wed Jan 22 2014 Jon Ciesla <limburgher@gmail.com> 1.6.2-2
- Rebuild for new LibRaw.

* Fri Dec 20 2013 TI_Eugene <ti.eugene@gmail.com> 1.6.2-1
- Version bump.

* Tue Dec 03 2013 Rex Dieter <rdieter@fedoraproject.org> - 1.6.0.2-2
- rebuild (exiv2)

* Wed Oct 23 2013 TI_Eugene <ti.eugene@gmail.com> 1.6.0.2-1
- Version bump (hotfix).

* Wed Oct 16 2013 TI_Eugene <ti.eugene@gmail.com> 1.6.0-1
- Version bump.

* Mon Jul 15 2013 TI_Eugene <ti.eugene@gmail.com> 1.4.0-1
- Version bump.
- BR libtiff-devel added

* Sat Jun 15 2013 TI_Eugene <ti.eugene@gmail.com> 1.2.0-1
- Version bump.
- %%find_lang macro added
- _als translation removed

* Fri May 31 2013 Jon Ciesla <limburgher@gmail.com> 1.0.2-4
- Rebuild for new LibRaw.

* Tue Apr 09 2013 TI_Eugene <ti.eugene@gmail.com> 1.0.2-3
- CXX flags - -O3 only

* Tue Apr 09 2013 TI_Eugene <ti.eugene@gmail.com> 1.0.2-2
- CXX flags added to %%cmake macro

* Sun Apr 07 2013 TI_Eugene <ti.eugene@gmail.com> 1.0.2-1
- next version
- source url fixed
- description update (removed "free", "windows", licensing)
- update-desktop-database added

* Fri Mar 29 2013 TI_Eugene <ti.eugene@gmail.com> 1.0.0-3
- BuildRequires libraries versions defined

* Fri Mar 29 2013 TI_Eugene <ti.eugene@gmail.com> 1.0.0-2
- disabled EL6/CentOS6 build (due qt < 4.7)

* Fri Mar 29 2013 TI_Eugene <ti.eugene@gmail.com> 1.0.0-1
- initial packaging for Fedora

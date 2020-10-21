%define __cmake_in_source_build 1

Name:           sir
Version:        2.5.1
Release:        24%{?dist}
Summary:        A simple application for resizing images

License:        GPLv2+
URL:            http://sir.projet-libre.org 
Source0:        http://sir.googlecode.com/files/%{name}_%{version}.tar.gz
Patch0:         sir_service.desktop.patch

BuildRequires:  qt4-devel,desktop-file-utils,exiv2-devel,cmake
   

%description
A simple application for resizing images,inspired by GTPY - ImageResizer
But uses C++/QT and QImage class to convert the images.

%prep
%setup -q -n %{name}
%patch0 -p0

%build
%cmake . -Dmetadata=ON
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT
desktop-file-install --dir=$RPM_BUILD_ROOT%{_datadir}/applications %{name}.desktop
desktop-file-install --dir=$RPM_BUILD_ROOT%{_datadir}/applications %{name}_service.desktop

# Register as an application to be visible in the software center
#
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Ryan Lerch <rlerch@redhat.com> -->
<!--
BugReportURL: https://code.google.com/p/sir/issues/detail?id=6
SentUpstream: 2014-09-17
-->
<application>
  <id type="desktop">sir.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>Resize images in batches</summary>
  <description>
    <p>
      Sir (Simple Image Resizer) is a utility to resize one or many images at a time.
      Sir allows you to select a number of images (or a whole directory), to import
      then once you have chosen the size that you want to export to, will export them
      in one action.
      Sir also has the ability to resize while preserving the aspect  ratio,
      and do simple transforms like rotation.
      Sir supports over 30 different image formats for import and output,
      including PNG, JPG, BMP, SVG and TIFF.
    </p>
  </description>
  <url type="homepage">https://code.google.com/p/sir/</url>
  <screenshots>
    <screenshot type="default">https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/sir/a.png</screenshot>
  </screenshots>
</application>
EOF

%files
%{_bindir}/%{name}
%{_datadir}/pixmaps/*.png
%{_datadir}/appdata/*.appdata.xml
%{_datadir}/applications/*.desktop
%{_datadir}/%{name}/
%doc LICENSE

%changelog
* Tue Sep 22 2020 Jeff Law  <law@redhat.com> - 2.5.1-24
- Use cmake_in_source_build to fix FTBFS due to recent cmake macro changes

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-23
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 30 2019 Rex Dieter <rdieter@fedoraproject.org> - 2.5.1-18
- rebuild (exiv2)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 02 2017 Rex Dieter <rdieter@fedoraproject.org> - 2.5.1-13
- rebuild (exiv2)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 24 2015 Rex Dieter <rdieter@fedoraproject.org> - 2.5.1-10
- rebuild (exiv2)

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.5.1-8
- Rebuilt for GCC 5 C++11 ABI change

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 2.5.1-7
- Add an AppData file for the software center

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Dec 04 2013 Rex Dieter <rdieter@fedoraproject.org> - 2.5.1-4
- BR: qt4-devel exiv2-devel
- rebuild (exiv2)
- fix %%_datadir/%%name/ subdir ownership

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 11 2013 François Cami <fcami@fedoraproject.org> - 2.5.1-1
- New upstream release
- Switch build system to CMake

* Mon Aug 1 2012 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> 2.4-1
- New version

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Mar 19 2011 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> 2.1.1-3
- Fix pixmaps problems
- Fix install section problem

* Fri Mar 18 2011 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> 2.1.1-2
- Fix license,desktop file problems
- Remove INSTALL and TODO from doc section

* Wed Mar 16 2011 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> 2.1.1-1
- Initial Build

Name:           openalchemist
Version:        0.4
Release:        31%{?dist}
Summary:        Reflection game
License:        GPLv2+ and CC-BY-SA
URL:            http://www.openalchemist.com

#Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}-src.tar.gz
# There's no tarball for version 0.4, it is only tagged in the repository
# svn export https://openalchemist.svn.sourceforge.net/svnroot/openalchemist/tags/0.4 openalchemist-0.4-src
Source0:        %{name}-%{version}-src.tar.gz
Patch0:         openalchemist-0.4-cl23.patch
Patch1:         openalchemist-0.4-title-xml.patch
Patch2:         openalchemist-0.4-py3_gtk3.patch

BuildRequires:  ClanLib-devel >= 2.3
BuildRequires:  desktop-file-utils
BuildRequires:  fontconfig-devel
BuildRequires:  freetype-devel
BuildRequires:  gcc-c++
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libtool
BuildRequires:  zip
BuildRequires:  zlib-devel
Requires:       hicolor-icon-theme
Requires:       python3-gobject-base


%description
OpenAlchemist is a new reflection game which looks like classic falling block
games but where you can take your time. Be a crazy alchemist and try to make
new objects from those you get from the sky.


%prep
%setup -q -n openalchemist-%{version}-src
%patch0 -p1 -z .cl23
%patch1 -p1
%patch2 -p0
autoreconf -f -i


%build
%configure
%make_build V=1


%install
%make_install

rm -f %{buildroot}%{_datadir}/openalchemist/{CODE-LICENSE,GRAPHICS-LICENSE}

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/apps
install -p -m 644 data/logo_svg.svg \
    %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/openalchemist.svg
mv .desktop openalchemist.desktop
desktop-file-install --dir=%{buildroot}%{_datadir}/applications openalchemist.desktop

# Register as an application to be visible in the software center
#
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
mkdir -p %{buildroot}%{_datadir}/appdata
cat > %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Eduardo Mayorga <e@mayorgalinux.com> -->
<!--
EmailAddress: contact@openalchemist.com
SentUpstream: 2014-09-24
-->
<application>
  <id type="desktop">openalchemist.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>Puzzle game featuring chemicals</summary>
  <description>
    <p>
      OpenAlchemist is a tile-matching puzzle game in which appear the chemical elements.
      OpenAlchemist is an easy-to-play game suitable for children and young people.
      It aims for reflection, adventure and suspense.
    </p>
  </description>
  <url type="homepage">http://www.openalchemist.com</url>
  <screenshots>
    <screenshot type="default">http://www.openalchemist.com/img/aqua.png</screenshot>
  </screenshots>
</application>
EOF

%files
%doc AUTHORS ChangeLog README TODO
%license CODE-LICENSE GRAPHICS-LICENSE
%{_bindir}/openalchemist
%{_bindir}/openalchemist-config
%{_datadir}/openalchemist
%{_datadir}/icons/hicolor/scalable/apps/openalchemist.svg
%{_datadir}/appdata/*%{name}.appdata.xml
%{_datadir}/applications/*openalchemist.desktop


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Aug 08 2019 Xavier Bachelot <xavier@bachelot.org> 0.4-30
- Add patch to port openalchemist-config to python3 and GTK3.
  Fixes RHBZ#1738939.

* Tue Jul 30 2019 Xavier Bachelot <xavier@bachelot.org> 0.4-29
- Modernize spec.
- Make python shebang explicit in openalchemist-config.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 26 2018 Xavier Bachelot <xavier@bachelot.org> 0.4-25
- Add BR: gcc-c++.

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4-23
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.4-17
- Rebuilt for GCC 5 C++11 ABI change

* Thu Mar 26 2015 Xavier Bachelot <xavier@bachelot.org> 0.4-16
- Fix startup (RHBZ#1049583).

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 0.4-15
- Add an AppData file for the software center

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Apr 30 2013 Jon Ciesla <limburgher@gmail.com> - 0.4-11
- Drop desktop vendor tag.

* Sun Mar 31 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.4-10
- ClanLib is now available on secondary arches

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 21 2013 Adam Tkac <atkac redhat com> - 0.4-8
- rebuild due to "jpeg8-ABI" feature drop

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 0.4-7
- rebuild against new libjpeg

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-5
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Dec 11 2011 Hans de Goede <hdegoede@redhat.com> 0.4-4
- Rebuild for ClanLib-2.3.4
- Better (high res) icon

* Thu Jun 09 2011 Karsten Hopp <karsten@redhat.com> 0.4-3
- exclusivearch x86 x86_64, requirement clanGDI not available on other archs

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun May 23 2010 Xavier Bachelot <xavier@bachelot.org> 0.4-1
- Update to 0.4 :
  - Use ClanLib 2.
  - Add music and sounds.
  - New menus system, more extensible.
  - New menus (more options available from within the game).
  - Fix score calculation.
  - Fix numerous memory leaks.
  - Redefine new and delete operators, to trace memory allocations.
  - Change Coding Style.
  - Add loading screen.
  - Add a desktop file.
  - Split Board::detect_to_destroy() fonction.
  - Better synchronisation (game runs at the same speed everywhere).

* Thu Nov 19 2009 Xavier Bachelot <xavier@bachelot.org> 0.3-8
- BR: ClanLib1-devel instead of ClanLib-devel (RHBZ#538870).

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon May 18 2009 Xavier Bachelot <xavier@bachelot.org> 0.3-6
- Rebuild for ClanLib 1.0.

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Oct 23 2008 Xavier Bachelot <xavier@bachelot.org> 0.3-4
- Modify Description: tag.
- Modify Summary: tag again.

* Thu Oct 16 2008 Xavier Bachelot <xavier@bachelot.org> 0.3-3
- Modify Summary: tag.
- Add graphics license to License: tag.
- Add Requires: pygtk2.
- Update desktop file.
- Remove duplicate license files.

* Tue Oct 14 2008 Xavier Bachelot <xavier@bachelot.org> 0.3-2
- Add a desktop file and icon.

* Mon Oct 13 2008 Xavier Bachelot <xavier@bachelot.org> 0.3-1
- Initial build.

# Copyright (c) 2007 oc2pus <toni@links2linux.de>
# Copyright (c) 2007-2015 Hans de Goede <hdegoede@redhat.com>
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# Please submit bugfixes or comments to us at the above email addresses

Name:           freecol
Version:        0.11.6
Release:        13%{?dist}
Summary:        Turn-based multi-player strategy game
License:        GPL+
URL:            http://www.freecol.org/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}-src.zip
Source1:        %{name}.sh
Source2:        %{name}.desktop
Source3:        freecol.appdata.xml
Source4:        %{name}-imperator.metainfo.xml
# From freecol 0.11.5, upstream freecol is no longer using this,
# we keep it around for non freecol users
Source5:        Imperator.ttf
# manpage courtesy of Debian
Source6:        %{name}.6
Patch0:         freecol-no-classpath-in-MF.patch
# texlive makeindex disallows absolute paths, and file= gets turned into one
Patch1:         freecol-fix-makeindex-invocation.patch
Patch2:         freecol-source-encoding.patch
# rhbz#1271823, patch from Debian, forward ported to 0.11.6
Patch3:         commons-cli-1.3.patch
BuildRequires:  ant xml-commons-apis xml-commons-resolver
BuildRequires:  tex(tex4ht.sty) desktop-file-utils fontpackages-devel
BuildRequires:  apache-commons-cli cortado jorbis miglayout >= 4.2
BuildRequires:  tex(latex)
BuildRequires:  java-devel >= 1:1.8.0
BuildArch:      noarch
Requires:       java >= 1:1.8.0 jpackage-utils hicolor-icon-theme
Requires:       apache-commons-cli cortado jorbis miglayout >= 4.2
Requires:       %{name}-shadowedblack-fonts

%description
FreeCol is a turn-based, multi-player, X based strategy game. FreeCol
has compatible rules with the Colonization game.


%package manual
Summary:        User Documentation for freecol
Requires:       %{name} = %{version}-%{release}

%description manual
User Documentation for freecol.


%package shadowedblack-fonts
Summary:        Gothic font with drop shadows
License:        GPLv2+
Requires:       fontpackages-filesystem

%description shadowedblack-fonts
A gothic font with drop shadows originally created by Paul Lloyd in 2002,
extended by the freecol project to include most accented latin characters.


%package imperator-fonts
Summary:        Gothic font
License:        GPLv2+
Requires:       fontpackages-filesystem

%description imperator-fonts
A gothic font originally created by Paul Lloyd in 2002, extended by the freecol
project to include most accented latin characters.


%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
# freecol normally builds against copies shipped with the source. Remove these
# and symlink to the system versions of these.
rm jars/*
ln -s %{_javadir}/commons-cli.jar jars/commons-cli-1.1.jar
ln -s %{_javadir}/cortado.jar jars/cortado-0.6.0.jar
ln -s %{_javadir}/jogg.jar jars/jogg-0.0.17.jar
ln -s %{_javadir}/jorbis.jar jars/jorbis-0.0.17.jar
ln -s %{_javadir}/miglayout-core.jar jars/miglayout-core-4.2.jar
ln -s %{_javadir}/miglayout-swing.jar jars/miglayout-swing-4.2.jar


%build
ant clean package manual


%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_javadir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man6
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/apps
mkdir -p $RPM_BUILD_ROOT%{_fontdir}

install -p -m 644 FreeCol.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
install -p -m 755 %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/%{name}
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE2}
install -p -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/appdata
install -p -m 644 %{SOURCE4} $RPM_BUILD_ROOT%{_datadir}/appdata
install -p -m 644 %{SOURCE5} $RPM_BUILD_ROOT%{_fontdir}
install -p -m 644 %{SOURCE6} $RPM_BUILD_ROOT%{_mandir}/man6

cp -a data $RPM_BUILD_ROOT%{_datadir}/%{name}

mv $RPM_BUILD_ROOT%{_datadir}/%{name}/data/base/resources/fonts/ShadowedBlack.ttf \
  $RPM_BUILD_ROOT%{_fontdir}
ln -s ../../../../../fonts/freecol/ShadowedBlack.ttf \
  $RPM_BUILD_ROOT%{_datadir}/%{name}/data/base/resources/fonts/ShadowedBlack.ttf

install -p -m 644 packaging/common/freecol.svg \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/apps



%files
%doc README COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_javadir}/%{name}.jar
%{_mandir}/man6/%{name}.6.gz
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

%files manual
%doc doc/FreeCol.pdf doc/FreeCol.html doc/FreeCol.css doc/images

%_font_pkg -n shadowedblack ShadowedBlack.ttf
%doc COPYING data/base/resources/fonts/README
%dir %{_fontdir}

%_font_pkg -n imperator Imperator.ttf
%{_datadir}/appdata/%{name}-imperator.metainfo.xml
%doc COPYING data/base/resources/fonts/README
%dir %{_fontdir}


%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 0.11.6-12
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 16 2018 Vojtech Trefny <vtrefny@redhat.com> - 0.11.6-8
- Fix dependency on tex4ht

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.11.6-5
- Remove obsolete scriptlets

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Oct 17 2015 Hans de Goede <hdegoede@redhat.com> - 0.11.6-1
- New upstream release 0.11.6 (#1272625)
- Fix crash with commons-cli >= 1.3 (#1271823)

* Tue Aug  4 2015 Hans de Goede <hdegoede@redhat.com> - 0.11.5-1
- New upstream release 0.11.5 (#1249256)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Mar 18 2015 Hans de Goede <hdegoede@redhat.com> - 0.11.3-1
- New upstream release 0.11.3 (#1199758)

* Thu Jan 15 2015 Hans de Goede <hdegoede@redhat.com> - 0.11.2-1
- New upstream release 0.11.2 (#1178747)

* Mon Nov 24 2014 Hans de Goede <hdegoede@redhat.com> - 0.11.1-1
- New upstream release 0.11.1 (#1166347)

* Wed Oct 22 2014 Hans de Goede <hdegoede@redhat.com> - 0.11.0-1
- New upstream release 0.11.0 (#1154287)

* Fri Oct 17 2014 Richard Hughes <richard@hughsie.com> - 0.10.7-5
- Add a MetaInfo file for the software center; this is a font we want to show.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Nov 18 2013 Hans de Goede <hdegoede@redhat.com> - 0.10.7-3
- Add a patch from upstream fixing crash on intro vid (rhbz#1031621)
- Add an appdata file (rhbz#1031611)

* Sat Aug 10 2013 Hans de Goede <hdegoede@redhat.com> - 0.10.7-2
- Drop vorbisspi and tritonus Requires, since 0.10.7 freecol no longer needs
  these
- Re-add html version to -manual sub-package

* Tue Jul 30 2013 Hans de Goede <hdegoede@redhat.com> - 0.10.7-1
- New upstream release 0.10.7 (#889436)
- Temporary drop html version from -manual sub-package as it fails to
  build due to a texlive bug (#959696)

* Fri Mar 15 2013 Jon Ciesla <limburgher@gmail.com> - 0.10.5-5
- Drop desktop vendor tag.

* Sat Mar 02 2013 Bruno Wolff III <bruno@wolff.to> - 0.10.5-4
- Adjust buildrequires for new texlive

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Feb 26 2012 Bruno Wolff III <bruno@wolff.to> - 0.10.5-1
- Update to upstream 0.10.5 (#789676)
- 0.10.5 release announcement: http://www.freecol.org/index2.php?option=com_content&task=view&id=113&pop=1&page=0&Itemid=40
- 0.10.4 release announcement: http://www.freecol.org/index2.php?option=com_content&task=view&id=112&pop=1&page=0&Itemid=40
- 0.10.4 changelog document: http://www.freecol.org/docs/freecol-changelog-version-0.10.4.pdf

* Fri Feb 17 2012 Deepak Bhole <dbhole@redhat.com> - 0.10.3-3
- Resolves rhbz#791366
- Patch from Omair Majid <omajid@redhat.com> to remove explicit Java 6 req.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Oct 16 2011 Hans de Goede <hdegoede@redhat.com> 0.10.3-1
- New upstream release 0.10.3 (#711737)
- upstream sources are now clean, use them directly instead of generating
  a -clean.tar.gz file
- vorbisspi is now packaged, use it instead of converting all the .ogg files
  to .wav files

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Nov 17 2010 Hans de Goede <hdegoede@redhat.com> 0.9.5-1
- New upstream release 0.9.5 (#579520)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue May 12 2009 Hans de Goede <hdegoede@redhat.com> 0.8.3-1
- New upstream release 0.8.3

* Mon May  4 2009 Hans de Goede <hdegoede@redhat.com> 0.8.2-1
- New upstream release 0.8.2

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Feb 22 2009 Hans de Goede <hdegoede@redhat.com> 0.8.1-1
- New upstream release 0.8.1

* Thu Jan 15 2009 Hans de Goede <hdegoede@redhat.com> 0.8.0-2
- Update description for new trademark guidelines

* Thu Jan 15 2009 Hans de Goede <hdegoede@redhat.com> 0.8.0-1
- New upstream release 0.8.0

* Sat Dec 27 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.7.4-4
- Drop unclearly licensed Plakat-Fraktur font (and stop using it)
- Put ShadowedBlack font in its own shadowedblack-fonts subpackage (rh 477388)

* Mon Nov 24 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.7.4-3
- Fixup Summary

* Thu Sep 11 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.7.4-2
- use tetex-tex4ht instead of latex2html

* Mon Jun 16 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.7.4-1
- New upstream release 0.7.4

* Fri Mar 14 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.7.3-2
- Adapt launch script and (Build)Requires for icedtea -> openjdk rename

* Sat Feb  9 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.7.3-1
- New upstream release 0.7.3
- Drop ExcludeArch ppc ppc64 now that icedtea is available for ppc too

* Wed Oct  3 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.7.2-3
- Remove wstx classpath lookup from the startup script, as we no longer
  require wstx
- .desktop file cleanups

* Tue Oct  2 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.7.2-2
- Add BuildRequires: xorg-x11-server-utils, to fix generating of images in
  the manual package, see bz 313301
- Drop requires on wstx, it isn't strictly needed, but does speed up things
  significantly, so the Requires will return when wstx hits the repo
- Really remove classpath entry from the manifest

* Sun Sep 23 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.7.2-1
- Adapted Packman spec file for Fedora

* Thu Sep 20 2007 Toni Graffy <toni@links2linux.de> - 0.7.2-0.pm.1
- update to 0.7.2

* Fri Aug 31 2007 Toni Graffy <toni@links2linux.de> - 0.7.1-0.pm.2
- build openSUSE-10.3, corrected BuildRequires

* Mon Aug 13 2007 Toni Graffy <toni@links2linux.de> - 0.7.1-0.pm.1
- update to 0.7.1

* Fri Jul 13 2007 Toni Graffy <toni@links2linux.de> - 0.7.0-0.pm.1
- update to 0.7.0

* Sun May 06 2007 Toni Graffy <toni@links2linux.de> - 0.6.1-0.pm.1
- First packaged release 0.6.1

Name:           dosbox
# https://fedoraproject.org/wiki/Packaging:Versioning#More_complex_versioning
# actual version is 0.74-3 which uses invalid characters
# 0.74-3 (upstream) becomes 0.74.2 (fedora)
%define shortver     0.74
%define upstreamrel  3
%define upstreamver  %{shortver}-%{upstreamrel}
Version:        %{shortver}.%{upstreamrel}
Release:        5%{?dist}

Summary:        x86/DOS emulator with sound and graphics

License:        GPLv2+
URL:            http://www.dosbox.com
Source0:        http://dl.sourceforge.net/%{name}/%{name}-%{upstreamver}.tar.gz
Source1:        dosbox.desktop
# From https://commons.wikimedia.org/wiki/File:DOSBox_icon.png
Source2:        dosbox.png
Source3:        dosbox.appdata.xml
# add translations {da,de,es,fr,it,ko,pt,ru} rhbz#752307
Source10:       DOSBox-0.74-DK.zip
Source11:       DOSBox-german-lang-0.74.zip
Source12:       DOSBox-spanish-074.zip
Source13:       DOSBox-0.74-lang-french.zip
Source14:       DOSBox-ita-lang-0.74.zip
Source15:       DOSBox-Kor-Lang-0.74.zip
Source16:       DOSBox-portuguese-br-lang-074.zip
Source17:       DOSBox-russian-lang-074.zip

BuildRequires:  gcc-c++
BuildRequires:  gcc
BuildRequires:  libpng-devel
BuildRequires:  SDL-devel
BuildRequires:  SDL_net-devel
BuildRequires:  SDL_sound-devel
BuildRequires:  desktop-file-utils
BuildRequires:  alsa-lib-devel
BuildRequireS:  libGLU-devel

Requires: hicolor-icon-theme

%description

DOSBox is a DOS-emulator using SDL for easy portability to different
platforms. DOSBox has already been ported to several different platforms,
such as Windows, BeOS, Linux, Mac OS X...
DOSBox emulates a 286/386 realmode CPU, Directory FileSystem/XMS/EMS,
a SoundBlaster card for excellent sound compatibility with older games...
You can "re-live" the good old days with the help of DOSBox, it can run plenty
of the old classics that don't run on your new computer!


%prep
%setup -q -n %{name}-%{upstreamver}


%build
%configure --enable-core-inline
%{__make} %{_smp_mflags}


%check
%{__make} check


%install
make install DESTDIR=%{buildroot}

desktop-file-install \
%if 0%{?fedora} && 0%{?fedora} < 19
  --vendor fedora            \
%endif
  --dir=%{buildroot}%{_datadir}/applications \
  %{SOURCE1}

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/256x256/apps
install -p -m 0644 %SOURCE2 %{buildroot}%{_datadir}/icons/hicolor/256x256/apps
mkdir -p %{buildroot}%{_datadir}/metainfo
install -p -m 0644 %SOURCE3 %{buildroot}%{_datadir}/metainfo

mkdir -p %{buildroot}%{_datadir}/dosbox/translations/{da,de,es,fr,it,ko,pt,ru}
pushd %{buildroot}%{_datadir}/dosbox/translations/da
unzip -j %{SOURCE10}
popd
pushd %{buildroot}%{_datadir}/dosbox/translations/de
unzip %{SOURCE11}
popd
pushd %{buildroot}%{_datadir}/dosbox/translations/es
unzip %{SOURCE12}
popd
pushd %{buildroot}%{_datadir}/dosbox/translations/fr
unzip %{SOURCE13}
popd
pushd %{buildroot}%{_datadir}/dosbox/translations/it
unzip -j %{SOURCE14}
popd
pushd %{buildroot}%{_datadir}/dosbox/translations/ko
unzip %{SOURCE15}
popd
pushd %{buildroot}%{_datadir}/dosbox/translations/pt
unzip %{SOURCE16}
popd
pushd %{buildroot}%{_datadir}/dosbox/translations/ru
unzip %{SOURCE17}
popd

%files
%doc AUTHORS ChangeLog COPYING NEWS README THANKS
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/*/apps/dosbox.png
%{_datadir}/metainfo/*
%{_datadir}/dosbox


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.74.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Nov 16 2019 Kalev Lember <klember@redhat.com> - 0.74.3-4
- Install the icon into hicolor icon theme

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.74.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 04 2019 François Cami <fcami@redhat.com> - 0.74.3-2
- Update sources

* Thu Jul 04 2019 François Cami <fcami@redhat.com> - 0.74.3-1
- Update to latest upstream (0.74-3) (rhbz#1725365).
- Fixes CVE-2019-12594 and CVE-2019-7165

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.74.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 01 2019 François Cami <fcami@redhat.com> - 0.74.2-2
- Include upstream input focus gain/loss fix for Xorg 1.20

* Tue Jan 01 2019 François Cami <fcami@redhat.com> - 0.74.2-1
- Update to latest upstream (0.74-2).
- Remove all upstreamed patches.

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.74-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Apr 15 2018 Kalev Lember <klember@redhat.com> - 0.74-25
- Add new 256x256 px icon

* Fri Feb 23 2018 Kalev Lember <klember@redhat.com> - 0.74-24
- Add appdata file (#1442849)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.74-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.74-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.74-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.74-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

 Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.74-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.74-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 06 2016 Adam Williamson <awilliam@redhat.com> - 0.74-17
- backport upstream patch to fix crashes when built with GCC 5 (SF #413)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.74-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.74-15
- Rebuilt for GCC 5 C++11 ABI change

* Mon Jan 05 2015 Andreas Bierfert <andreas.bierfert@lowlatency.de>
- 0.74-14
- add 0.74 translations (rhbz#752307)
- cleanup spec

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.74-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.74-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Dec 18 2013 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 0.74-11
- fix format security (rhbz#1037041)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.74-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri May 10 2013 Hans de Goede <hdegoede@redhat.com> - 0.74-9
- Fix crash on startup when compiled with gcc-4.8

* Tue Feb 12 2013 Jon Ciesla <limburgher@gmail.com> - 0.74-8
- Drop desktop vendor tag.

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.74-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.74-6
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.74-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.74-4
- Rebuild for new libpng

* Thu Jun 30 2011 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.74-3
- Adopt openSUSE's gcc46.patch (Fix FTBFS BZ#715677).

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.74-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon May 24 2010 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 0.74-1
- version upgrade (#592894)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.73-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat May 30 2009 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 0.73-1
- version upgrade

* Sun Mar 08 2009 Lubomir Rintel <lkundrak@v3.sk> - 0.72-7
- Fix build with GCC 4.4
- Fix key mapping with evdev driver (#473875)

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.72-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Sep 21 2008 Ville Skyttä <ville.skytta at iki.fi> - 0.72-5
- Fix Patch0:/%%patch mismatch.

* Fri Feb 22 2008 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 0.72-4
- fix gcc43 build (#433990) with patch from Erik van Pienbroek
- add BR SDL_sound-devel

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.72-3
- Autorebuild for GCC 4.3

* Mon Feb 11 2008 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de> - 0.72-2
- Rebuilt for gcc43

* Mon Aug 27 2007 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 0.72-1
- version upgrade

* Wed Aug 22 2007 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0.71-2
- new license tag
- rebuild for buildid

* Thu Aug 09 2007 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0.71-1
- version upgrade (#250149)
- new version has x86_64 dynamic core support (#247791)

* Fri Apr 27 2007 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0.70-3
- proper fix for #230902
- require hicolor-icon-theme
- drop X-Fedora category

* Wed Apr 25 2007 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0.70-2
- fix #230902

* Sun Mar 04 2007 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0.70-1
- version upgrade (#230768)

* Tue Sep 12 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0.65-3
- FE6 rebuild

* Mon Jul 10 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0.65-2
- add ipx support (#198057)

* Thu Mar 30 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0.65-1
- version upgrade

* Tue Feb 14 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0.63-9
- Rebuild for Fedora Extras 5

* Wed Jan 25 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0.63-8
- apply upstream patch
- fix typos

* Sun Jan 22 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0.63-7
- add dist
- rebuild
- add gcc4.1 patch

* Mon May 30 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0.63-6
- add a x86_64 bugfix from upstream 

* Mon May 30 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0.63-5
- more build fixes and cleanups...

* Mon May 30 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- more x86_64 build fixes...

* Mon May 23 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0.63-3
- fix x86_64 build (#158446)

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Thu Nov 25 2004 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0:0.63-1
- new version
- added missing BuildRequires
- merged with preextras spec

* Wed Nov 10 2004 Michael Schwendt <mschwendt[AT]users.sf.net>
- Add a desktop file icon from upstream package (fixes fedora.us #1144).

* Mon May 31 2004 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0:0.61-0.fdr.1
- new version

* Mon Dec 22 2003 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0:0.60-0.fdr.1
- new version
- closed bug #1144
* Sun Jul 27 2003 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0:0.58-0.fdr.3
- Fixed minor stuff from #442 #3

* Sun Jul 13 2003 Andreas Bierfert (awjb) <andreas.bierfert[AT]awbsworld.de>
0:0.58-0.fdr.2
- Added desktop entry
- Fixed minor stuff

* Mon Jun 30 2003 Andreas Bierfert (awjb) <andreas.bierfert[AT]awbsworld.de>
0:0.58-0.fdr.1
- Initial RPM release.

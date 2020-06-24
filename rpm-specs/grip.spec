Summary: Front-end for CD rippers and Ogg Vorbis encoders
Name: grip
Version: 4.1.1
Release: 1%{?dist}
Epoch: 1
License: GPLv2+
Source0: http://downloads.sourceforge.net/grip/grip-%{version}.tar.gz
# This fixes code which is not used right now; still keeping it
Patch0: grip-64bit-fix.patch
URL: https://sourceforge.net/projects/grip/
Requires: vorbis-tools
%if 0%{?fedora}
Recommends: lame
%endif
BuildRequires: gcc gcc-c++
BuildRequires: cdparanoia-devel
BuildRequires: libgnomeui-devel curl-devel
BuildRequires: gettext id3lib-devel
BuildRequires: desktop-file-utils

%description
Grip is a GTK+ based front-end for CD rippers (such as cdparanoia and
cdda2wav) and Ogg Vorbis encoders. Grip allows you to rip entire tracks or
just a section of a track. Grip supports the CDDB protocol for
accessing track information on disc database servers.

%prep
%setup -q
%patch0 -p1

%build

pushd po
iconv -f koi8-r -t utf-8 ru.po > ru.po.tmp
mv ru.po.tmp ru.po

sed -i 's/Content-Type: text\/plain; charset=koi8-r\\n/Content-Type: text\/plain; charset=utf-8\\n/' ru.po
popd

%configure
%make_build

%install
make DESTDIR=$RPM_BUILD_ROOT install

cat >> %{buildroot}%{_datadir}/applications/grip.desktop << EOF
StartupWMClass=Grip
EOF

desktop-file-install \
	--dir $RPM_BUILD_ROOT/%{_datadir}/applications \
	--delete-original \
	--add-category X-AudioVideoImport \
	--add-category AudioVideo \
	$RPM_BUILD_ROOT%{_datadir}/applications/grip.desktop

# I think this is a KDE specific path; delete for now - until understood
rm -rf $RPM_BUILD_ROOT%{_datadir}/apps/

%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc README ChangeLog CREDITS AUTHORS TODO
%{_bindir}/grip
%{_datadir}/pixmaps/grip.png
%{_datadir}/pixmaps/griptray.png
%{_datadir}/gnome/help/grip
%{_datadir}/applications/*
%{_datadir}/solid/actions/grip-audiocd.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_mandir}/man1/*

%changelog
* Sun Apr 12 2020 Adrian Reber <adrian@lisas.de> - 1:4.1.1-1
- Updated to 4.1.1 (#1778979)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Dec 03 2019 Adrian Reber <adrian@lisas.de> - 1:4.0.1-1
- Updated to 4.0.1 (#1778979)

* Sat Oct 05 2019 Adrian Reber <adrian@lisas.de> - 1:4.0.0-1
- Updated to 4.0.0
- Removed vte dependency (upstream dropped the corresponding code)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 23 2019 Adrian Reber <adrian@lisas.de> - 1:3.10.0-1
- Updated to 3.10.0
- Added patch to build with gcc-9

* Mon Jul 16 2018 Adrian Reber <adrian@lisas.de> - 1:3.9.0-1
- Updated to 3.9.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 02 2018 Adrian Reber <adrian@lisas.de> - 1:3.8.1-1
- Updated to 3.8.1
- Removed upstreamed patches

* Thu Apr 26 2018 Adrian Reber <adrian@lisas.de> - 1:3.7.1-1
- Updated to 3.7.1

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Adrian Reber <adrian@lisas.de> - 1:3.6.3-1
- Updated to 3.6.3
- Remove icon scriptlets

* Sat Oct 28 2017 Adrian Reber <adrian@lisas.de> - 1:3.6.1-2
- Updated to 3.6.1 (#1504330)

* Tue Aug 08 2017 Adrian Reber <adrian@lisas.de> - 1:3.5.2-1
- Updated to 3.5.2

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Sun Jul 30 2017 Adrian Reber <adrian@lisas.de> - 1:3.5.0-1
- Updated to 3.5.0
- Removed upstreamed patches
- Update icon cache for newly available icons

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 24 2017 Adrian Reber <adrian@lisas.de> - 1:3.4.3-2
- Added patch to fix broken non-MP3-tagging (#1474010)

* Sat Jul 08 2017 Gwyn Ciesla <limburgher@gmail.com> - 1:3.4.3-1
- 3.4.3.

* Wed Jun 28 2017 Adrian Reber <adrian@lisas.de> - 1:3.4.2-2
- Updated to 3.4.2 (thanks to Orion Poplawski) (#1455353)
- Removed all upstreamed patches

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.2.0-51
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.2.0-50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.2.0-49
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1:3.2.0-48
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.2.0-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.2.0-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Dec 04 2013 Adrian Reber <adrian@lisas.de> - 1:3.2.0-45
- fixed "grip FTBFS if "-Werror=format-security" flag is used" (#1037105)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.2.0-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Apr 12 2013 Jon Ciesla <limburgher@gmail.com> - 1:3.2.0-43
- Drop desktop vendor tag.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.2.0-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Sep 15 2012 Adrian Reber <adrian@lisas.de> - 1:3.2.0-41
- fixed "Proxy settings don't work in Grip" (#857633) (David Waring)

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.2.0-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Apr 03 2012 Adrian Reber <adrian@lisas.de> - 1:3.2.0-39
- first try to fix the many resize errors

* Wed Mar 28 2012 Adrian Reber <adrian@lisas.de> - 1:3.2.0-38
- fixed "IA__gdk_window_set_icon_name: Process /usr/bin/grip was killed by signal 11" (#737792)

* Tue Mar 27 2012 Adrian Reber <adrian@lisas.de> - 1:3.2.0-37
- fixed "_IO_fwrite: Process /usr/bin/grip was killed by signal 11" (#653609)

* Tue Mar 27 2012 Adrian Reber <adrian@lisas.de> - 1:3.2.0-36
- fixed "no rip speed is indicated in the application" (#804180)
- removed a few warnings
- fixed a segfault

* Mon Mar 26 2012 Adrian Reber <adrian@lisas.de> - 1:3.2.0-35
- fixed "GripUpdate: Process /usr/bin/grip was killed by signal 11" (#728254)

* Mon Mar 26 2012 Adrian Reber <adrian@lisas.de> - 1:3.2.0-34
- fixed "Spurious output when editing disc info" (#736391)
- removed buildroot and clean section

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.2.0-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 1:3.2.0-32
- Rebuild for new libpng

* Thu Jun 23 2011 Adrian Reber <adrian@lisas.de> - 1:3.2.0-31
- fixed id3lib detection (FTBFS)

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.2.0-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Nov 19 2009 Adrian Reber <adrian@lisas.de> - 1:3.2.0-29
- fixed " Charset conversion for Russian translation is broken by .spec file"
  (#477920); applied patch from Andrew Martynov

* Wed Sep 23 2009 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 1:3.2.0-28
- Update desktop file according to F-12 FedoraStudio feature

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.2.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.2.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Nov 10 2008 Adrian Reber <adrian@lisas.de> - 1:3.2.0-25
- fixed "grip breaks utf-8 sequences up when writing xmcd CD database file"
  (#466656)

* Sun Nov 09 2008 Adrian Reber <adrian@lisas.de> - 1:3.2.0-24
- fixed "buffer overflow caused by large amount of CDDB replies" (#470552)
  (CVE-2005-0706)

* Thu Oct 02 2008 Adrian Reber <adrian@lisas.de> - 1:3.2.0-23
- fixed "German Umlauts are shown incorrectly" (#459394)
  (not converting de.po and fr.po to UTF-8 anymore)

* Sat Aug 23 2008 Adrian Reber <adrian@lisas.de> - 1:3.2.0-22
- updated to better "execute command after encode" patch from Stefan Becker

* Sun Aug 10 2008 Adrian Reber <adrian@lisas.de> - 1:3.2.0-21
- added "execute command after encode" patch (#457186)

* Sat Jul 26 2008 Adrian Reber <adrian@lisas.de> - 1:3.2.0-20
- fixed "Grip silently crahses on F8" (#456721)
  (converted non UTF-8 .po files to UTF-8)

* Tue Jun 10 2008 Adrian Reber <adrian@lisas.de> - 1:3.2.0-19
- removed now unnecessary cell-renderer patch
- fixed "default config creates ogg files with .mp3 extension" (#427017)

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1:3.2.0-18
- Autorebuild for GCC 4.3

* Mon Sep 03 2007 Adrian Reber <adrian@lisas.de> - 1:3.2.0-17
- search for ripper and encoder executables in path (#249150)
- updated License:

* Wed Jan 17 2007 Adrian Reber <adrian@lisas.de> - 1:3.2.0-16
- fixes for #220777, #222574, #232755

* Wed Jan 03 2007 Adrian Reber <adrian@lisas.de> - 1:3.2.0-15
- changed default file extension (#220777)

* Tue Oct 31 2006 Adrian Reber <adrian@lisas.de> - 1:3.2.0-14
- rebuilt for new curl

* Sat Sep 09 2006 Adrian Reber <adrian@lisas.de> - 1:3.2.0-13
- rebuilt

* Fri Jun 23 2006 Adrian Reber <adrian@lisas.de> - 1:3.2.0-12
- updated with patch from novell to fix crashes when calling
  external programs (#184542)

* Fri May 12 2006 Adrian Reber <adrian@lisas.de> - 1:3.2.0-11
- rebuilt for new vte

* Mon Feb 13 2006 Adrian Reber <adrian@lisas.de> - 1:3.2.0-10
- rebuilt

* Tue Nov 15 2005 Adrian Reber <adrian@lisas.de> - 1:3.2.0-9
- rebuilt

* Wed Sep 14 2005 Adrian Reber <adrian@lisas.de> - 1:3.2.0-8
- added .desktop patch from Chong Kai Xiong (#167989)

* Sat Aug 20 2005 Adrian Reber <adrian@lisas.de> - 1:3.2.0-7
- rebuilt

* Thu Aug 04 2005 Adrian Reber <adrian@lisas.de> - 1:3.2.0-6
- added patch for buffer overflow in id3.c (#160671)

* Thu Jul 07 2005 Adrian Reber <adrian@lisas.de> - 1:3.2.0-5
- added patch to fix cell renderer problem (BZ #162324)
- wrote and added a man page

* Wed Mar 02 2005 Adrian Reber <adrian@lisas.de> - 1:3.2.0-4
- s/Copyright/License/
- s/Serial/Epoch/
- cosmetic changes to quiet rpmlint
- removed grip.png and grip.desktop (Source1 and Source2) as
  it is already included in the tarball
- removed unused patches
- removed ExcludeArch: s390 s390x
- renamed BuildPrereq to BuildRequires
- added id3lib-devel to BuildRequires
- use %%{_smp_mflags}
- changed .desktop file creation and installation
- removed INSTALL and NEWS from %%doc
- deleted changelog entries older than 2004
- changed Source line to be valid

* Fri Oct  8 2004 Bill Nottingham <notting@redhat.com> 3.2.0-3
- add a passel of buildreqs (#135045)

* Wed Jul 28 2004 Adrian Havill <havill@redhat.com> 3.2.0-2
- rebuilt
- add vte-devel to BuildRequires

* Sun Jun 20 2004 Karsten Hopp <karsten@redhat.de> 3.2.0-1
- update to latest stable version
- remove obsolete locking and cdparanoia patches

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

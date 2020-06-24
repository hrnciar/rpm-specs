Name: cylindrix
Version:  1.0
Release: 32%{?dist}
Summary: A 3 degrees of freedom combat game

License: LGPLv2        
URL: http://www.hardgeus.com/cylindrix/
Source0: http://www.hardgeus.com/cylindrix/cylindrix-1.0.tar.bz2
Source1: cylindrix.desktop
Source2: cylindrix.png
Source3: cylindrix.sh
Source4: cylindrix-level10.dat
Patch0: cylindrix-1.0-fix-packing.patch
Patch1: cylindrix-1.0-arch-independ-file-read.patch
Patch2: cylindrix-1.0-use-int-not-long.patch
Patch3: cylindrix-1.0-arch-independ-file-write.patch
Patch4: cylindrix-1.0-object-fopen.patch
Requires: hicolor-icon-theme
BuildRequires:  gcc-c++
BuildRequires: allegro-devel, desktop-file-utils

%description
Cylindrix is a 3-on-3 combat game with 360 degrees of freedom that is
similar to Spectre VR but with a wider variety of ships, as well as the
addition of drivers. Attack and be attacked from all angles as you battle
in huge orbiting arenas that are each unique in physics, atmospheric
conditions, and configuration. You must build your team from 37 warriors
from 10 alien races and select from 8 vehicles, each with unique 
maneuverability, speed, and firepower. The graphics are good, although
structure and ship graphics are a little too monotonous. Gameplay is fast
and furious... so furious, in fact, that it is difficult to differentiate
between friend and foe in the thick of battle. For those who are confident
of their reflexes or have beaten Spectre and Battlezone, though, this game
is worth a try.

%prep
%setup -q

%patch0 -p0
%patch1 -p0
%patch2 -p0
%patch3 -p0
%patch4 -p0

%build

%configure
make CFLAGS="$RPM_OPT_FLAGS -Wno-pointer-sign -fcommon" LIBS="-lm"

%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 %{SOURCE3} %{buildroot}%{_bindir}/cylindrix
install -m 755 cylindrix %{buildroot}%{_bindir}/cylindrix-bin

mkdir -p %{buildroot}%{_datadir}/cylindrix

cp -pr 3d_data %{buildroot}%{_datadir}/cylindrix
cp -pr anything.mod %{buildroot}%{_datadir}/cylindrix
cp -pr cylindrx.fli %{buildroot}%{_datadir}/cylindrix
cp -pr gamedata %{buildroot}%{_datadir}/cylindrix
cp -pr pcx_data %{buildroot}%{_datadir}/cylindrix
cp -pr people.dat %{buildroot}%{_datadir}/cylindrix
cp -pr stats %{buildroot}%{_datadir}/cylindrix
cp -pr wav_data %{buildroot}%{_datadir}/cylindrix

#replace broken data file
rm -f %{buildroot}%{_datadir}/cylindrix/gamedata/level10.dat
install -m 644 %{SOURCE4} %{buildroot}%{_datadir}/cylindrix/gamedata/level10.dat

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install            \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE1}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps
install -p -m 644 %{SOURCE2} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps


%files
%{_bindir}/cylindrix*
%{_datadir}/cylindrix/
%license COPYING
%doc AUTHORS
%{_datadir}/applications/cylindrix.desktop
%{_datadir}/icons/hicolor/64x64/apps/cylindrix.png


%changelog
* Thu Feb 06 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.0-32
- Fix FTBFS.

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0-26
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Feb 11 2013 Jon Ciesla <limburgher@gmail.com> - 1.0-17
- Drop desktop vendor tag.

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jul 15 2011 Jon Ciesla <limb@jcomserv.net> - 1.0-14
- Bump and rebuild for new Allegro.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jun 28 2010 Jon Ciesla <limb@jcomserv.net> - 1.0-12
- FTBFS fix, BZ 600019.

* Mon Aug 10 2009 Ville Skyttä <ville.skytta@iki.fi> - 1.0-11
- Use bzipped upstream tarball.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 13 2009 Jon Ciesla <limb@jcomserv.net> - 1.0-8
- Replace broken data file, BZ 452190.

* Wed Nov 26 2008 Jon Ciesla <limb@jcomserv.net> - 1.0-7
- Fix fopen, BZ 452190.

* Mon Nov 24 2008 Jon Ciesla <limb@jcomserv.net> - 1.0-6
- Shorten summary.

* Fri Jun 20 2008 Jon Ciesla <limb@jcomserv.net> - 1.0-5
- Set terminal to false in .desktop, BZ 452155.

* Mon Jun 16 2008 Jon Ciesla <limb@jcomserv.net> - 1.0-4
- Fixed launcher script, data locations.
- Added Hans's newest review patch.

* Mon Jun 16 2008 Jon Ciesla <limb@jcomserv.net> - 1.0-3
- Dropped VS files.
- Dropped icon extension.
- Added CFLAG.

* Mon Jun 16 2008 Jon Ciesla <limb@jcomserv.net> - 1.0-2
- Added allegro-devel, desktop-file-utils BRs.
- Added Hans's review patches.
- Corrected data installation method for shared and mutable data.

* Sat Sep 08 2007 Jon Ciesla <limb@jcomserv.net> - 1.0-1
- Added h-i-theme requires, xparentfied icon.
- create.

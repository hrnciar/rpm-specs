Name:           nogravity
Version:        2.00
Release:        34%{?dist}
Summary:        Space shooter in 3D
License:        GPLv2+
URL:            http://www.realtech-vr.com/nogravity/
Source0:        http://downloads.sourceforge.net/%{name}/rt-%{name}-src.zip
Source2:        %{name}.desktop
Source3:        %{name}.png
Source4:        nogravity--Makefile.am
Source5:        nogravity--bootstrap
Source6:        nogravity--configure.in
Source7:        nogravity.sh
Source8:        %{name}.appdata.xml
Patch0:         nogravity--snd_sdlmixer_c-powerpc-fix.diff
Patch1:         nogravity--fullscreen_as_option.patch
Patch2:         nogravity--fixed_path_to_game_data.diff
Patch3:         nogravity--64-bit.patch
Patch4:         nogravity--cvs.patch
Patch5:         nogravity--openal.patch
# See: https://www.redhat.com/archives/fedora-games-list/2007-June/msg00000.html
Patch6:         nogravity--README.patch
Patch7:         nogravity--bufer-overflows.patch
Patch8:         nogravity--strcpy-abuse.patch
Patch9:         nogravity-2.00-rhbz699274.patch
Patch10:        nogravity-2.00-libpng15.patch
Patch11:        0001-v3xscene-Remove-some-unused-code.patch
Patch12:        0002-rlx32-Stop-using-MaxExtentableObjet.patch
Patch13:        nogravity-2.00-stdint_h.patch
Patch14:        nogravity--gcc6.patch
Requires:       %{name}-data = %{version}
BuildRequires:  gcc-c++
BuildRequires:  SDL_mixer-devel openal-soft-devel libpng-devel libvorbis-devel
BuildRequires:  automake desktop-file-utils libappstream-glib
Requires:       hicolor-icon-theme glx-utils

%description
No Gravity is a fantastic and futuristic universe made of five
intergalactic worlds. An arcade type game with great playability,
where it is easy to plunge into space battles against spacefighters,
space stations and more!


%prep
%setup -q -c
cp %{SOURCE4} ./src/Linux/Makefile.am
cp %{SOURCE5} ./src/Linux/bootstrap
cp %{SOURCE6} ./src/Linux/configure.in
%patch0 -b .snd_sdlmixer_c-powerpc-fix
%patch1 -b .fullscreen_as_option 
%patch2 -b .fixed_path_to_game_data
%patch3 -p1 -b .64-bit
%patch4 -p1 -b .cvs
%patch5 -p1 -b .openal
%patch6 -p1 -b .license
%patch7 -p1 -b .buf-oflow
%patch8 -p1 -b .strcpy
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
sed -i 's/\r//g' GNU.TXT README.TXT
pushd src/Linux
sh bootstrap
popd


%build
pushd src/Linux

%configure --enable-sound=sdl_mixer --disable-opengl
make %{?_smp_mflags} LDADD=-lz
mv %{name} %{name}-software

make distclean

%configure --enable-sound=openal --enable-opengl
make %{?_smp_mflags} LDADD=-lz
mv %{name} %{name}-opengl

popd


%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
install -m 755 src/Linux/%{name}-software $RPM_BUILD_ROOT%{_bindir}
install -m 755 src/Linux/%{name}-opengl   $RPM_BUILD_ROOT%{_bindir}
install -p -m 755 %{SOURCE7} $RPM_BUILD_ROOT%{_bindir}/%{name}
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE2}
install -p -m 644 %{SOURCE3} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
install -p -m 644 %{SOURCE8} $RPM_BUILD_ROOT%{_datadir}/appdata
appstream-util validate-relax --nonet \
  $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml

%files
%doc GNU.TXT README.TXT
%{_bindir}/%{name}*
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.00-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.00-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.00-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.00-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.00-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.00-29
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.00-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.00-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.00-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Feb 20 2016 Hans de Goede <hdegoede@redhat.com> - 2.00-25
- Fix FTBFS (rhbz#1307807)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.00-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Hans de Goede <hdegoede@redhat.com> - 2.00-24
- Fix FTBFS
- Add an appdata file

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.00-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.00-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.00-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.00-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Apr 29 2013 Jon Ciesla <limburgher@gmail.com> - 2.00-19
- Drop desktop vendor tag.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.00-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.00-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Apr 11 2012 Hans de Goede <hdegoede@redhat.com> - 2.00-16
- Fix crash when loading level 5 (rhbz#768754)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.00-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Hans de Goede <hdegoede@redhat.com> - 2.00-14
- Take a stab at fixing the crash reported in rhbz#699274
  (race condition, cannot reproduce)
- Fix building with libpng-1.5

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 2.00-13
- Rebuild for new libpng

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.00-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Feb 15 2010 Hans de Goede <hdegoede@redhat.com> 2.00-11
- Fix FTBFS (#564637)

* Sat Nov  7 2009 Hans de Goede <hdegoede@redhat.com> 2.00-10
- Fix crash on startup on Intel 64 bit CPU's (strcpy abuse)

* Sun Aug 16 2009 Hans de Goede <hdegoede@redhat.com> 2.00-9
- Switch to openal-soft

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.00-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.00-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.00-6
- Autorebuild for GCC 4.3

* Fri Jan 11 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 2.00-5
- Fix wrapper script to work with duel head configurations

* Sun Dec 30 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 2.00-4
- Activate my 64 bit patch
- Add icon cache scriplets
- Use sed rather then dos2unix
- Build both a software rendering version and an opengl version, add a wrapper
  script which chooses which one to use based on the availabiliy of DRI
- Patch README to reflect that the data is GPL licensed too now
- Move datafile from /usr/games/nogravity to /usr/share/nogravity
- Make nogravity startup fullscreen by default
- Fix openal sound effects volume control and some other minor openal issues
- Fix several wrong memory uses and non 0 terminated strings, strncpy is evil!
  This fixes saving modified keybindings and hopefully also the odd segfault

* Sat Dec 29 2007 Rahul Sundaram <sundaram@fedoraproject.org> 2.00-3
- Split engine and data. List patch from Hans

* Mon Nov 26 2007 Peter Lemenkov <lemenkov@gmail.com> 2.00-2
- Various fixes according to https://bugzilla.redhat.com/show_bug.cgi?id=366841#c2

* Thu Oct  4 2007 Peter Lemenkov <lemenkov@gmail.com> 2.00-1
- Fixed download paths
- Fixed license as required

* Sun Oct  1 2006 Peter Lemenkov <lemenkov@gmail.com> 2.00-0.lvn.2
- Clean up BuildRequires
- Added patch for enabling/disabling fullscreen-mode (via config-file)
- Added patch for proper path to resource-file
- Dropped startup script (no longer necessary)
- Fixed audio at PowerPC-arch
- Disabled OpenGL (seems to be broken)

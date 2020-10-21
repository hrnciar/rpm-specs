# src/types.h is set to issue error on i386 and warning on other architectures
# when trying to enable position-independent code. It is not recommended for
# performance reasons
%undefine _hardened_build

Name:           mednafen
Version:        1.25.0
Release:        0.2.UNSTABLE%{?dist}
Summary:        A multi-system emulator utilizing OpenGL and SDL
#mednafen incorporates several emulators hence the colourful licensing
License:        GPLv2+ and BSD and ISC and LGPLv2+ and MIT and zlib 
URL:            https://mednafen.github.io/
Source0:        https://mednafen.github.io/releases/files/%{name}-%{version}-UNSTABLE.tar.xz
BuildRequires:  gcc-c++
BuildRequires:  gettext
#1.3.0 is required
#BuildRequires:  libmpcdec-devel
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(jack) => 1.0.2
#2.09 is required
%if 0%{?fedora} >= 32
BuildRequires:  pkgconfig(lzo2)
%endif
BuildRequires:  pkgconfig(sdl2) => 2.0.5
BuildRequires:  pkgconfig(sndfile) => 1.0.2
BuildRequires:  pkgconfig(zlib)

%description
A portable, utilizing OpenGL and SDL, argument(command-line)-driven multi-system
emulator. Mednafen has the ability to remap hotkey functions and virtual system
inputs to a keyboard, a joystick, or both simultaneously. Save states are
supported, as is real-time game rewinding. Screen snapshots may be taken, in the
PNG file format, at the press of a button. Mednafen can record audiovisual
movies in the QuickTime file format, with several different lossless codecs
supported.

The following systems are supported(refer to the emulation module documentation
for more details):

* Apple II/II+
* Atari Lynx
* Neo Geo Pocket (Color)
* WonderSwan
* GameBoy (Color)
* GameBoy Advance
* Nintendo Entertainment System
* Super Nintendo Entertainment System/Super Famicom
* Virtual Boy
* PC Engine/TurboGrafx 16 (CD)
* SuperGrafx
* PC-FX
* Sega Game Gear
* Sega Genesis/Megadrive
* Sega Master System
* Sega Saturn (experimental, x86_64 only)
* Sony PlayStation

Due to the threaded model of emulation used in Mednafen, and limitations of SDL,
a joystick is preferred over a keyboard to play games, as the joystick will have
slightly less latency, although the latency differences may not be perceptible
to most people. 


%prep
%autosetup -p1 -n %{name}

# Permission cleanup
find \( -name \*.c\* -or -name \*.h\* -or -name \*.inc \) -exec chmod -x {} \;


%build
# This package has a configure test which uses ASMs, but does not link the
# resultant .o files.  As such the ASM test is always successful in pure
# LTO mode.  We can use -ffat-lto-objects to force code generation.
#
# -ffat-lto-objects is the default for F33, but is expected to be removed
# in F34.  So we list it explicitly here.
%define _lto_cflags -flto=auto -ffat-lto-objects

CFLAGS="$RPM_OPT_FLAGS -Wl,-z,relro -Wl,-z,now"
CXXFLAGS="$RPM_OPT_FLAGS -Wl,-z,relro -Wl,-z,now"

export CFLAGS
export CXXFLAGS

%configure --disable-rpath \
%if 0%{?fedora} >= 32
    --with-external-lzo
%endif

#to be added once dependencies become available
#    --with-external-mpcdec
#    --with-external-tremor
#    --with-external-trio
%make_build


%install
%make_install

# Documentation cleanup
rm -rf Documentation/*.def Documentation/*.php Documentation/generate.sh \
    Documentation/Makefile.* Documentation/docgen.inc

%find_lang %{name}


%files -f %{name}.lang
%license COPYING
%doc ChangeLog TODO Documentation/*
%{_bindir}/%{name}


%changelog
* Thu Aug 20 2020 Jeff Law <law@redhat.com> - 1.25.0-0.2.UNSTABLE
- Re-enable LTO

* Tue Jul 28 2020 Julian Sikorski <belegdol@fedoraproject.org> - 1.25.0-0.1.UNSTABLE
- Update to 1.25.0-UNSTABLE

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.24.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 14 2020 Jeff Law <law@redhat.com> - 1.24.3-2
- Disable LTO

* Mon May 04 2020 Julian Sikorski <belegdol@fedoraproject.org> - 1.24.3-1
- Update to 1.24.3

* Sun May 03 2020 Julian Sikorski <belegdol@fedoraproject.org> - 1.24.2-1
- Update to 1.24.2

* Wed Mar 18 2020 Julian Sikorski <belegdol@fedoraproject.org> - 1.24.1-1
- Update to 1.24.1
- Drop ppc detection fix patch
- Enable system lzo on f32 and later

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.24.0-0.2.UNSTABLE
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 27 2019 Julian Sikorski <belegdol@fedoraproject.org> - 1.24.0-0.1.UNSTABLE
- Update to 1.24.0-UNSTABLE
- Dropped included patch
- Fix ppc detection on ppc64le

* Thu Sep 05 2019 Julian Sikorski <belegdol@fedoraproject.org> - 1.23.0-0.1.UNSTABLE
- Update to 1.23.0-UNSTABLE
- Work around gcc compiler bug 91678

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 24 2019 Julian Sikorski <belegdol@fedoraproject.org> - 1.22.2-1
- Update to 1.22.2

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 29 2019 Julian Sikorski <belegdol@fedoraproject.org> - 1.22.1-1
- Update to 1.22.1

* Mon Dec 24 2018 Julian Sikorski <belegdol@fedoraproject.org> - 1.22.0-0.1.UNSTABLE
- Update to 1.22.0-UNSTABLE

* Fri Jul 20 2018 Julian Sikorski <belegdol@fedoraproject.org> - 1.21.3-4
- Fixed FTBFS: BR gcc-c++, gcc is not enough

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.21.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon May 14 2018 Julian Sikorski <belegdol@fedoraproject.org> - 1.21.3-2
- Added an explanation why hardened build is disabled
- Bumped release so that the Fedora package is newer than RPM Fusion one

* Tue May 01 2018 Julian Sikorski <belegdol@fedoraproject.org> - 1.21.3-1
- Updated to 1.21.3

* Mon Apr 23 2018 Julian Sikorski <belegdol@fedoraproject.org> - 1.21.2-2
- Added pkgconfig(alsa) to BuildRequires as it is no longer pulled implicitly

* Sun Apr 15 2018 Julian Sikorski <belegdol@fedoraproject.org> - 1.21.2-1
- Updated to 1.21.2
- Switched to SDL2
- Added placeholders for system libs to be enabled once dependencies become available

* Fri Mar 02 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 0.9.48-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Oct 07 2017 Julian Sikorski <belegdol@fedoraproject.org> - 0.9.48-1
- Updated to 0.9.48

* Thu Sep 07 2017 Julian Sikorski <belegdol@fedoraproject.org> - 0.9.47-1
- Updated to 0.9.47

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 0.9.43-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Apr 02 2017 Julian Sikorski <belegdol@fedoraproject.org> - 0.9.43-1
- Updated to 0.9.43

* Sun Mar 26 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 0.9.39.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Oct 29 2016 Julian Sikorski <belegdol@fedoraproject.org> - 0.9.39.2-1
- Updated to 0.9.39.2
- Updated %%description
- Dropped gcc-6 fix
- Cleaned up the .spec file
- Disabled hardened build, see types.h

* Mon Jul 04 2016 Sérgio Basto <sergio@serjux.com> - 0.9.38.7-2
- Fix error compiling with GCC 6.x on Fedora 24

* Thu Dec 31 2015 Julian Sikorski <belegdol@fedoraproject.org> - 0.9.38.7-1
- Updated to 0.9.38.7

* Sun Sep 27 2015 Julian Sikorski <belegdol@fedoraproject.org> - 0.9.38.6-1
- Updated to 0.9.38.6

* Tue Jul 14 2015 Julian Sikorski <belegdol@fedoraproject.org> - 0.9.38.5-1
- Updated to 0.9.38.5

* Mon Sep 01 2014 Sérgio Basto <sergio@serjux.com> - 0.9.33.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Apr 29 2014 Julian Sikorski <belegdol@fedoraproject.org> - 0.9.33.3-1
- Updated to 0.9.33.3
- Updared the Source URL

* Sun Nov 10 2013 Julian Sikorski <belegdol@fedoraproject.org> - 0.9.32-0.1
- Updated to 0.9.32-WIP

* Tue May 14 2013 Julian Sikorski <belegdol@fedoraproject.org> - 0.9.28-0.1
- Updated to 0.9.28-WIP

* Mon Apr 29 2013 Nicolas Chauvet <kwizart@gmail.com> - 0.9.25-0.3
- https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Dec 09 2012 Julian Sikorski <belegdol@fedoraproject.org> - 0.9.25-0.1
- Updated to 0.9.25-WIP

* Sat Aug 25 2012 Julian Sikorski <belegdol@fedoraproject.org> - 0.9.24-0.1
- Updated to 0.9.24-WIP

* Mon Jul 02 2012 Julian Sikorski <belegdol@fedoraproject.org> - 0.9.22-0.1
- Updated to 0.9.22-WIP

* Wed May 02 2012 Julian Sikorski <belegdol@fedoraproject.org> - 0.9.21-0.1
- Updated to 0.9.21-WIP
- Dropped upstreamed gcc-47 patch

* Fri Feb 10 2012 Julian Sikorski <belegdol@fedoraproject.org> - 0.9.19-0.1
- Updated to 0.9.19-WIP
- Dropped obsolete Group, Buildroot, %%clean and %%defattr
- Updated %%description

* Thu Feb 09 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.9.18-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Nov 27 2011 Julian Sikorski <belegdol@fedoraproject.org> - 0.9.18-0.1
- Updated to 0.9.18-WIP
- Dropped the NES sound patch

* Sat Aug 27 2011 Julian Weissgerber <sloevenh1@googlemail.com> - 0.9.17-0.2
- Patch to fix segfault when NES sound is enabled

* Wed Jun 15 2011 Julian Sikorski <belegdol@fedoraproject.org> - 0.9.17-0.1
- Updated to 0.9.17-WIP
- Updated the License tag

* Thu Apr 29 2010 Julian Sikorski <belegdol@fedoraproject.org> - 0.8.12-2.0.8.C
- Rebuilt for new libcdio

* Thu Jul 09 2009 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.8.12-1.0.8.C
- Updated to 0.8.C
- Dropped the upstreamed gcc44 patch

* Sun Mar 29 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 0.8.11-2.0.8.B
- rebuild for new F11 features

* Sun Mar 08 2009 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.8.11-1.0.8.B
- Updated to 0.8.B
- ExcludeArch: ppc64 on Fedora 11+

* Thu Nov  6 2008 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.8.10-2.0.8.A
- Rebuilt. Something has mangled the x86_64 rpm

* Sun Nov  2 2008 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.8.10-1.0.8.A
- Updated to 0.8.A

* Sat Sep 20 2008 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.8.9-1
- Updated to 0.8.9
- Dropped the rpath patch, does not seem to be necessary

* Tue Jan 08 2008 Ian Chapman <packages[AT]amiga-hardware.com> 0.8.7-1
- Upgrade to 0.8.7

* Sun Nov 25 2007 Ian Chapman <packages[AT]amiga-hardware.com> 0.8.5-1
- Upgrade to 0.8.5

* Sun Nov 18 2007 Ian Chapman <packages[AT]amiga-hardware.com> 0.8.4-1
- Upgrade to 0.8.4
- Removed several patches which have been applied upstream
- License change due to new guidelines
- New URL as project homepage has changed

* Sat Apr 28 2007 Ian Chapman <packages[AT]amiga-hardware.com> 0.8.1-2
- Added patch to fix crashes with wonderswan roms
- Added patch to fix compilation on ppc

* Thu Apr 26 2007 Ian Chapman <packages[AT]amiga-hardware.com> 0.8.1-1
- Upgrade to 0.8.1

* Tue Feb 13 2007 Ian Chapman <packages[AT]amiga-hardware.com> 0.7.2-1
- Upgrade to 0.7.2

* Wed Jan 03 2007 Ian Chapman <packages[AT]amiga-hardware.com> 0.7.1-1
- Upgrade to 0.7.1
- Updated rpath patch
- Added support for jack

* Fri Oct 06 2006 Ian Chapman <packages[AT]amiga-hardware.ocm> 0.6.5-2
- Rebuild for new version of libcdio in fc6

* Thu Sep 07 2006 Ian Chapman <packages[AT]amiga-hardware.com> 0.6.5-1
- Upgrade to 0.6.5

* Wed Aug 23 2006 Ian Chapman <packages[AT]amiga-hardware.com> 0.6.4-1
- Upgrade to 0.6.4
- Minor alteration to RPM description due to new features

* Sat Aug 12 2006 Ian Chapman <packages[AT]amiga-hardware.com> 0.6.3-1
- Upgrade to 0.6.3
- Drop the libtool buildrequire and use the patch for fixing rpath

* Mon Jun 19 2006 Ian Chapman <packages[AT]amiga-hardware.com> 0.6.2-1
- Upgrade to 0.6.2

* Sun Jun 04 2006 Ian Chapman <packages[AT]amiga-hardware.com> 0.6.1-2
- Removed gawk buildrequire. Doesn't seem to be needed.
- Removed bison buildrequire. Doesn't seem to be needed.
- Replaced xorg-x11-devel with libGLU-devel for compatibility reasons with
  modular and non modular X
- Removed SDL-devel buildrequire, implied by SDL_net-devel

* Tue May 23 2006 Ian Chapman <packages[AT]amiga-hardware.com> 0.6.1-1.iss
- Initial Release

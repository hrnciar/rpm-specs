%{?mingw_package_header}

Name:           mingw-SDL
Version:        1.2.15
Release:        16%{?dist}
Summary:        MinGW Windows port of SDL cross-platform multimedia library

URL:        https://www.libsdl.org/
# The license of the file src/video/fbcon/riva_mmio.h is bad, but the contents
# of the file has been relicensed to MIT in 2008 by Nvidia for the
# xf86_video-nv driver, therefore it can be considered ok.
# The license in the file src/stdlib/SDL_qsort.c is bad, but author relicensed
# it to zlib on 2016-02-21,
# <https://www.mccaughan.org.uk/software/qsort.c-1.14>, bug #1381888.
License:    LGPLv2+
# Source: %%{url}/release/%%{name}-%%{version}.tar.gz
# To create the repackaged archive use ./repackage.sh %%{version}
Source0:    SDL-%{version}_repackaged.tar.gz
Source1:    %{url}/release/SDL-%{version}.tar.gz.sig
Source2:    https://slouken.libsdl.org/slouken-pubkey.asc
#Source3:    SDL_config.h
Source4:    repackage.sh
Patch0:     SDL-1.2.12-multilib.patch
# Rejected by upstream as sdl1155, rh480065
Patch1:     SDL-1.2.10-GrabNotViewable.patch
# Proposded to upstream as sdl1769
Patch2:     SDL-1.2.15-const_XData32.patch
# sdl-config(1) manual from Debian, rh948864
Patch3:     SDL-1.2.15-add_sdl_config_man.patch
# Upstream fix for sdl1486, rh990677
Patch4:     SDL-1.2.15-ignore_insane_joystick_axis.patch
# Do not use backing store by default, sdl2383, rh1073057, rejected by
# upstream
Patch5:     SDL-1.2.15-no-default-backing-store.patch
# Fix processing keyboard events if SDL_EnableUNICODE() is enabled, sdl2325,
# rh1126136, in upstream after 1.2.15
Patch6:     SDL-1.2.15-SDL_EnableUNICODE_drops_keyboard_events.patch
# Fix vec_perm() usage on little-endian 64-bit PowerPC, bug #1392465
Patch7:     SDL-1.2.15-vec_perm-ppc64le.patch
# Use system glext.h to prevent from clashing on a GL_GLEXT_VERSION definition,
# rh1662778
Patch8:     SDL-1.2.15-Use-system-glext.h.patch
# Fix CVE-2019-7577 (a buffer overread in MS_ADPCM_decode), bug #1676510,
# upstream bug #4492, in upstream after 1.2.15
Patch9:     SDL-1.2.15-CVE-2019-7577-Fix-a-buffer-overread-in-MS_ADPCM_deco.patch
# Fix CVE-2019-7575 (a buffer overwrite in MS_ADPCM_decode), bug #1676744,
# upstream bug #4493, in upstream after 1.2.15
Patch10:    SDL-1.2.15-CVE-2019-7575-Fix-a-buffer-overwrite-in-MS_ADPCM_dec.patch
# Fix CVE-2019-7574 (a buffer overread in IMA_ADPCM_decode), bug #1676750,
# upstream bug #4496, in upstream after 1.2.15
Patch11:    SDL-1.2.15-CVE-2019-7574-Fix-a-buffer-overread-in-IMA_ADPCM_dec.patch
# Fix CVE-2019-7572 (a buffer overread in IMA_ADPCM_nibble), bug #1676754,
# upstream bug #4495, in upstream after 1.2.15
Patch12:    SDL-1.2.15-CVE-2019-7572-Fix-a-buffer-overread-in-IMA_ADPCM_nib.patch
# Fix CVE-2019-7572 (a buffer overwrite in IMA_ADPCM_nibble), bug #1676754,
# upstream bug #4495, in upstream after 1.2.15
Patch13:    SDL-1.2.15-CVE-2019-7572-Fix-a-buffer-overwrite-in-IMA_ADPCM_de.patch
# Fix CVE-2019-7573, CVE-2019-7576 (buffer overreads in InitMS_ADPCM),
# bugs #1676752, #1676756, upstream bugs #4491, #4490,
# in upstream after 1.2.15
Patch14:    SDL-1.2.15-CVE-2019-7573-CVE-2019-7576-Fix-buffer-overreads-in-.patch
# Fix CVE-2019-7578, (a buffer overread in InitIMA_ADPCM), bug #1676782,
# upstream bug #4491, in upstream after 1.2.15
Patch15:    SDL-1.2.15-CVE-2019-7578-Fix-a-buffer-overread-in-InitIMA_ADPCM.patch
# Fix CVE-2019-7638, CVE-2019-7636 (buffer overflows when processing BMP
# images with too high number of colors), bugs #1677144, #1677157,
# upstream bugs #4500, #4499, in upstream after 1.2.15
Patch16:    SDL-1.2.15-CVE-2019-7638-CVE-2019-7636-Refuse-loading-BMP-image.patch
# Fix CVE-2019-7637 (an integer overflow in SDL_CalculatePitch), bug #1677152,
# upstream bug #4497, in upstream after 1.2.15
Patch17:    SDL-1.2.15-CVE-2019-7637-Fix-in-integer-overflow-in-SDL_Calcula.patch
# Fix CVE-2019-7635 (a buffer overread when blitting a BMP image with pixel
# colors out the palette), bug #1677159, upstream bug #4498,
# in upstream after 1.2.15
Patch18:    SDL-1.2.15-CVE-2019-7635-Reject-BMP-images-with-pixel-colors-ou.patch
# Reject 2, 3, 5, 6, 7-bpp BMP images (related to CVE-2019-7635),
# bug #1677159, upstream bug #4498, in upstream after 1.2.15
Patch19:    SDL-1.2.15-Reject-2-3-5-6-7-bpp-BMP-images.patch
# Fix CVE-2019-7577 (Fix a buffer overread in MS_ADPCM_nibble and
# MS_ADPCM_decode on an invalid predictor), bug #1676510, upstream bug #4492,
# in upstream after 1.2.15
Patch20:    SDL-1.2.15-CVE-2019-7577-Fix-a-buffer-overread-in-MS_ADPCM_nibb.patch
# Fix retrieving an error code after stopping and resuming a CD-ROM playback,
# upstream bug #4108, in upstream after 1.2.15
Patch21:    SDL-1.2.15-Fixed-bug-4108-Missing-break-statements-in-SDL_CDRes.patch
# Fix SDL_Surface reference counter initialization and a possible crash when
# opening a mouse device when using a framebuffer video output, bug #1602687
Patch22:    SDL-1.2.15-fix-small-errors-detected-by-coverity.patch
# Fix Windows drivers broken with a patch for CVE-2019-7637, bug #1677152,
# upstream bug #4497, in upstream after 1.2.15
Patch23:    SDL-1.2.15-fix_copy_paste_mistakes_in_commit_9b0e5c555c0f.patch
# Fix CVE-2019-13616 (a heap buffer over-read in BlitNtoN), bug #1747237,
# upstream bug #4538, in upstream after 1.2.15
Patch24:    SDL-1.2.15-CVE-2019-13616-validate_image_size_when_loading_BMP_files.patch

BuildArch:      noarch

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-win-iconv

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-win-iconv

# Not required at the moment, but SDL does contain plenty of C++ code,
# I just haven't worked out how to enable it.
#BuildRequires:  mingw32-gcc-c++

%ifarch %{ix86}
BuildRequires: nasm
%endif


%description
Simple DirectMedia Layer (SDL) is a cross-platform multimedia library
designed to provide fast access to the graphics frame buffer and audio
device.


# Win32
%package -n mingw32-SDL
Summary:        MinGW Windows port of SDL cross-platform multimedia library
Requires:       pkgconfig
# kraxel pointed out that the headers need <iconv.h>, hence:
Requires:       mingw32-win-iconv

%description -n mingw32-SDL
Simple DirectMedia Layer (SDL) is a cross-platform multimedia library
designed to provide fast access to the graphics frame buffer and audio
device.

# Win32
%package -n mingw64-SDL
Summary:        MinGW Windows port of SDL cross-platform multimedia library
Requires:       pkgconfig
# kraxel pointed out that the headers need <iconv.h>, hence:
Requires:       mingw64-win-iconv

%description -n mingw64-SDL
Simple DirectMedia Layer (SDL) is a cross-platform multimedia library
designed to provide fast access to the graphics frame buffer and audio
device.


%?mingw_debug_package


%prep
%setup -q -b0 -n SDL-%{version}
%patch0 -p1
%patch1 -p0
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
for F in CREDITS; do
    iconv -f iso8859-1 -t utf-8 < "$F" > "${F}.utf"
    touch --reference "$F" "${F}.utf"
    mv "${F}.utf" "$F"
done


%build
%mingw_configure
%mingw_make %{?_smp_mflags}


%install
%mingw_make DESTDIR=$RPM_BUILD_ROOT install

# Remove static libraries but DON'T remove *.dll.a files.
rm $RPM_BUILD_ROOT%{mingw32_libdir}/libSDL.a
rm $RPM_BUILD_ROOT%{mingw64_libdir}/libSDL.a

# Actually libSDLmain.a seems to be required.  It just contains
# a single object file called SDL_win32_main.o.
#rm $RPM_BUILD_ROOT%{mingw32_libdir}/libSDLmain.a
#rm $RPM_BUILD_ROOT%{mingw64_libdir}/libSDLmain.a

# Delete man pages since they duplicate what is already available
# in base Fedora package.
rm $RPM_BUILD_ROOT%{mingw32_mandir}/man1/*.1*
rm $RPM_BUILD_ROOT%{mingw64_mandir}/man1/*.1*
rm $RPM_BUILD_ROOT%{mingw32_mandir}/man3/*.3*
rm $RPM_BUILD_ROOT%{mingw64_mandir}/man3/*.3*

# Drop all .la files
find $RPM_BUILD_ROOT -name "*.la" -delete


# Win32
%files -n mingw32-SDL
%doc COPYING
%{mingw32_bindir}/SDL.dll
%{mingw32_bindir}/sdl-config
%{mingw32_libdir}/libSDL.dll.a
%{mingw32_libdir}/libSDLmain.a
%{mingw32_libdir}/pkgconfig/sdl.pc
%{mingw32_datadir}/aclocal/sdl.m4
%{mingw32_includedir}/SDL

# Win64
%files -n mingw64-SDL
%doc COPYING
%{mingw64_bindir}/SDL.dll
%{mingw64_bindir}/sdl-config
%{mingw64_libdir}/libSDL.dll.a
%{mingw64_libdir}/libSDLmain.a
%{mingw64_libdir}/pkgconfig/sdl.pc
%{mingw64_datadir}/aclocal/sdl.m4
%{mingw64_includedir}/SDL


%changelog
* Thu Feb 13 2020 Daniel P. Berrangé <berrange@redhat.com> - 1.2.15-16
- Sync sources/patches with native package
- Fixes CVE-2019-13616, CVE-2019-7572, CVE-2019-7572, CVE-2019-7573
  CVE-2019-7576, CVE-2019-7574, CVE-2019-7575, CVE-2019-7577,
  CVE-2019-7577, CVE-2019-7578, CVE-2019-7635, CVE-2019-7637,
  CVE-2019-7638, CVE-2019-7636

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.15-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 1.2.15-14
- Rebuild (Changes/Mingw32GccDwarf2)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.15-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.15-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.15-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.15-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.15-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.15-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.15-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.15-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jun 02 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.2.15-1
- Update to 1.2.15
- Dropped upstreamed patches
- Dropped all configure arguments which aren't relevant for the win32/win64 targets
- Add BR: nasm

* Sat Apr 14 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.2.13-15
- Added win64 support
- Automatically generate debuginfo package
- Use parallel make
- Dropped unneeded BR: mingw32-dlfcn

* Fri Mar 09 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.2.13-14
- Dropped .la files

* Wed Mar 07 2012 Kalev Lember <kalevlember@gmail.com> - 1.2.13-13
- Renamed the source package to mingw-SDL (#801028)
- Modernize the spec file
- Use mingw macros without leading underscore

* Mon Feb 27 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.2.13-12
- Rebuild against the mingw-w64 toolchain
- Build without directx support as it isn't ready yet for the mingw-w64 toolchain

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.13-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jul 06 2011 Kalev Lember <kalevlember@gmail.com> - 1.2.13-10
- Rebuilt against win-iconv

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.13-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.13-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Apr 29 2009 Richard W.M. Jones <rjones@redhat.com> - 1.2.13-7
- Add runtime Requires mingw32-iconv (kraxel).

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 20 2009 Richard W.M. Jones <rjones@redhat.com> - 1.2.13-5
- Rebuild for mingw32-gcc 4.4

* Tue Jan 13 2009 Richard W.M. Jones <rjones@redhat.com> - 1.2.13-4
- Verify we are still up to date with Fedora release.
- Include COPYING in documentation.
- Build with dlfcn.
- List all BRs.
- No need to package the man pages, don't duplicate what's in the
  base Fedora package already.
- Requires pkgconfig.

* Fri Oct 24 2008 Richard W.M. Jones <rjones@redhat.com> - 1.2.13-2
- Initial RPM release.

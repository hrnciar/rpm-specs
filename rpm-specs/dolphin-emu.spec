%undefine _hardened_build
#I think one of the bundled libraries needs to be static.
#Static libraries are fine as all of the libraries included are bundled.
%undefine _cmake_shared_libs

#Dolphin now uses gitsnapshots for it's versions.
#See upstream release notes for this snapshot:
#https://dolphin-emu.org/download/dev/$commit
%global commit 8d4e8314a3dcd8680ae81d91fb7e076b4496b43b
%global snapnumber 11991

Name:           dolphin-emu
Version:        5.0.%{snapnumber}
Release:        1%{?dist}
Summary:        GameCube / Wii / Triforce Emulator

Url:            https://dolphin-emu.org/
##The project is licensed under GPLv2+ with some notable exceptions
#Source/Core/Common/GL/GLExtensions/* is MIT
#Source/Core/Core/HW/Sram.h is zlib
#Source/Core/Common/GekkoDisassembler.* is BSD (2 clause)
##The following is BSD (3 clause):
#dolphin-5.0/Source/Core/Common/SDCardUtil.cpp
#dolphin-5.0/Source/Core/Common/BitField.h
#dolphin-5.0/Source/Core/Core/IPC_HLE/l2cap.h
#dolphin-5.0/Source/Core/Core/IPC_HLE/hci.h
#dolphin-5.0/Source/Core/VideoBackends/Software/Clipper.cpp
#dolphin-5.0/Source/Core/AudioCommon/aldlist.cpp
##Any code in Externals has a license break down in Externals/licenses.md
License:        GPLv2+ and BSD and MIT and zlib
Source0:        https://github.com/%{name}/dolphin/archive/%{commit}/%{name}-%{version}.tar.gz
Source1:        %{name}.appdata.xml
#Can't be upstreamed as-is, needs rework:
Patch1:         0001-Use-system-headers-for-Vulkan.patch
#Update soundtouch:
#https://github.com/dolphin-emu/dolphin/pull/8725
Patch2:         0001-soundtounch-update-to-2.1.2.patch
Patch3:         0002-soundtouch-Use-shorts-instead-of-floats-for-samples.patch
Patch4:         0003-soundtounch-disable-exceptions.patch
#This needs to be fixed, I've reverted the patch that breaks minizip
Patch5:         0001-Revert-Externals-Update-minizip-search-path.patch

##Bundled code ahoy
#The following isn't in Fedora yet:
Provides:       bundled(FreeSurround)
Provides:       bundled(imgui) = 1.70
Provides:       bundled(cpp-argparse)
#soundtouch cannot be unbundled easily, as it requires compile time changes:
Provides:       bundled(soundtouch) = 2.1.2

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  alsa-lib-devel
BuildRequires:  bluez-libs-devel
%ifarch x86_64
BuildRequires:  bochs-devel
%endif
BuildRequires:  cmake
BuildRequires:  cubeb-devel
BuildRequires:  enet-devel
BuildRequires:  fmt-devel >= 6.0.0
BuildRequires:  glslang-devel
BuildRequires:  hidapi-devel
BuildRequires:  libao-devel
BuildRequires:  libcurl-devel
BuildRequires:  libevdev-devel
BuildRequires:  libpng-devel
BuildRequires:  libusb-devel
BuildRequires:  libXi-devel
BuildRequires:  libXrandr-devel
BuildRequires:  lzo-devel
BuildRequires:  mbedtls-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  minizip-devel
BuildRequires:  miniupnpc-devel
BuildRequires:  openal-soft-devel
BuildRequires:  picojson-devel
BuildRequires:  pugixml-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  portaudio-devel
BuildRequires:  SDL2-devel
BuildRequires:  SFML-devel
BuildRequires:  spirv-headers-devel
BuildRequires:  spirv-tools
BuildRequires:  spirv-tools-devel
BuildRequires:  systemd-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  vulkan-headers
BuildRequires:  xxhash-devel
BuildRequires:  zlib-devel
BuildRequires:  xz-devel

BuildRequires:  gettext
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  hicolor-icon-theme
BuildRequires:  /usr/bin/env

#Only the following architectures are supported:
ExclusiveArch:  x86_64 aarch64

Requires:       hicolor-icon-theme
Requires:       %{name}-data = %{version}-%{release}

#Most of below is taken bundled spec file in source#
%description
Dolphin is a Gamecube, Wii and Triforce (the arcade machine based on the
Gamecube) emulator, which supports full HD video with several enhancements such
as compatibility with all PC controllers, turbo speed, networked multiplayer,
and more.
Most games run perfectly or with minor bugs.

%package nogui
Summary:        Dolphin Emulator without a graphical user interface
Requires:       %{name}-data = %{version}-%{release}

%description nogui
Dolphin Emulator without a graphical user interface.

%package data
Summary:        Dolphin Emulator data files
BuildArch:      noarch

%description data
This package provides the data files for dolphin-emu.

####################################################

%prep
%autosetup -p1 -n dolphin-%{commit}

#Allow building with cmake macro
sed -i '/CMAKE_C.*_FLAGS/d' CMakeLists.txt

#Font license, drop the install directory into thie file
echo "%{_datadir}/%{name}/Sys/GC:" > font-licenses.txt
cat Data/Sys/GC/font-licenses.txt >> font-licenses.txt

###Remove Bundled:
cd Externals
#Keep what we need...
rm -rf `ls | grep -v 'Bochs' | grep -v 'FreeSurround' | grep -v 'imgui' | grep -v 'cpp-optparse' | grep -v 'soundtouch' | grep -v 'picojson'`
#Remove Bundled Bochs source and replace with links (for x86 only):
%ifarch x86_64
pushd Bochs_disasm
rm -rf `ls | grep -v 'stdafx' | grep -v 'CMakeLists.txt'`
ln -s %{_includedir}/bochs/* ./
ln -s %{_includedir}/bochs/disasm/* ./
popd
%else
rm -rf Bochs_disasm
%endif
#Replace bundled picojson with a modified system copy (remove use of throw)
pushd picojson
rm picojson.h
#In master, picojson has build option "PICOJSON_NOEXCEPT", but for now:
sed "s/throw std::.*;/std::abort();/g" /usr/include/picojson.h > picojson.h
popd

%build
#Script to find xxhash is not implemented, just tell cmake it was found
#Note some items are disabled to avoid bundling
%cmake . \
       -DXXHASH_FOUND=ON \
       -DUSE_SHARED_ENET=ON \
       -DENABLE_TESTS=OFF \
       -DENABLE_ANALYTICS=OFF \
       -DENCODE_FRAMEDUMPS=OFF \
       -DUSE_DISCORD_PRESENCE=OFF \
       -DDOLPHIN_WC_DESCRIBE=5.0-%{snapnumber} \
       -DDOLPHIN_WC_REVISION=%{commit} \
       -DDOLPHIN_WC_BRANCH="beta"
%make_build

%install
%make_install

#Install udev rules
mkdir -p %{buildroot}%{_udevrulesdir}
install -m 0644 Data/51-usb-device.rules %{buildroot}%{_udevrulesdir}/51-dolphin-usb-device.rules

#Create shell wrapper; dolphin doesn't work on wayland yet, but the QT GUI
#tries to use it. For now, force xwayland. Also fixes bodhi test warning
mv %{buildroot}/%{_bindir}/%{name} %{buildroot}/%{_bindir}/%{name}-x11
echo -e '#!/usr/bin/bash\nQT_QPA_PLATFORM=xcb %{name}-x11 "$@"' \
  > %{buildroot}/%{_bindir}/%{name}
#Remove workaround in desktop:
sed -i "s/^Exec=.*/Exec=dolphin-emu/g" \
  %{buildroot}/%{_datadir}/applications/%{name}.desktop
#Symlink manpage
ln -s %{name}.6 %{buildroot}/%{_mandir}/man6/%{name}-x11.6

#Install appdata.xml
install -p -D -m 0644 %{SOURCE1} \
  %{buildroot}/%{_datadir}/appdata/%{name}.appdata.xml
%find_lang %{name}

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet \
  %{buildroot}/%{_datadir}/appdata/*.appdata.xml

%files -f %{name}.lang
%doc Readme.md
%license license.txt
%attr(755, root, root) %{_bindir}/%{name}
%{_bindir}/%{name}-x11
%{_mandir}/man6/%{name}.*
%{_mandir}/man6/%{name}-x11.*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/%{name}/sys/Resources/
%{_datadir}/%{name}/sys/Themes/
%{_datadir}/appdata/*.appdata.xml

%files nogui
%doc Readme.md
%license license.txt
%{_bindir}/%{name}-nogui
%{_mandir}/man6/%{name}-nogui.*

%files data
%doc Readme.md docs/gc-font-tool.cpp
%license license.txt font-licenses.txt
#For the gui package:
%exclude %{_datadir}/%{name}/sys/Resources/
%exclude %{_datadir}/%{name}/sys/Themes/
#Already packaged:
%exclude %{_datadir}/%{name}/sys/GC/font-licenses.txt
%{_datadir}/%{name}
%{_udevrulesdir}/51-dolphin-usb-device.rules

%changelog
* Tue May 05 2020 Jeremy Newton <alexjnewt at hotmail dot com> - 5.0.11991-1
- Update to latest beta version

* Wed Apr 29 2020 Jeremy Newton <alexjnewt at hotmail dot com> - 5.0.11824-1
- Unbundle cubeb
- Update to latest beta version

* Mon Apr 13 2020 Jeremy Newton <alexjnewt at hotmail dot com> - 5.0.11819-5
- Forgot shebang in wrapper
- Symlink manpage for dolphin-emu-x11

* Mon Apr 13 2020 Jeremy Newton <alexjnewt at hotmail dot com> - 5.0.11819-4
- Fix permissions of wrapper script

* Mon Apr 13 2020 Jeremy Newton <alexjnewt at hotmail dot com> - 5.0.11819-3
- Add wrapper script for xwayland, fixes RH#1823234

* Sun Apr 05 2020 Jeremy Newton <alexjnewt at hotmail dot com> - 5.0.11819-2
- Update bundled soundtouch to 2.1.2

* Fri Mar 27 2020 Jeremy Newton <alexjnewt at hotmail dot com> - 5.0.11819-1
- Update to 5.0-11819

* Wed Mar 25 2020 Jeremy Newton <alexjnewt at hotmail dot com> - 5.0.11817-1
- Update to 5.0-11817

* Wed Mar 18 2020 Jeremy Newton <alexjnewt at hotmail dot com> - 5.0.11782-1
- Update to 5.0-11782

* Wed Mar 18 2020 Jeremy Newton <alexjnewt at hotmail dot com> - 5.0.11713-3
- Unbundle glslang

* Thu Mar 12 2020 Jeremy Newton <alexjnewt at hotmail dot com> - 5.0.11713-2
- Unbundle picojson

* Wed Mar 11 2020 Jeremy Newton <alexjnewt at hotmail dot com> - 5.0.11713-1
- Update to 5.0-11713

* Wed Mar 11 2020 Jeremy Newton <alexjnewt at hotmail dot com> - 5.0.10474-1
- Update to 5.0-10474

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 10 2019 Kalev Lember <klember@redhat.com> - 5.0-27
- Rebuilt for miniupnpc soname bump

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Sep 27 2018 Morten Stevens <mstevens@fedoraproject.org> - 5.0-25
- Rebuilt for mbed TLS 2.13.0

* Mon Aug 20 2018 Jeremy Newton <alexjnewt at hotmail dot com> - 5.0-24
- Fix for soundtouch 2.0.0-5 onwards

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon May 21 2018 Robert Scheck <robert@fedoraproject.org> - 5.0-22
- Rebuilt for mbed TLS 2.9.0 (libmbedcrypto.so.2)

* Wed Mar 07 2018 Jeremy Newton <alexjnewt at hotmail dot com> - 5.0-21
- Unbundle xxhash

* Mon Feb 19 2018 Robert Scheck <robert@fedoraproject.org> - 5.0-20
- Rebuilt for mbed TLS 2.7.0

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 5.0-18
- Remove obsolete scriptlets

* Sun Oct 15 2017 Jeremy Newton <alexjnewt at hotmail dot com> - 5.0-17
- Rebuild with gtk2, since it's been merged into wxGTK3
- Cleanup unnecessary walyand script due to gtk2, closer to upstream now

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 8 2017 Jeremy Newton <alexjnewt at hotmail dot com> - 5.0-14
- Rework and rebuild for bochs 2.6.9

* Sun May 7 2017 Jeremy Newton <alexjnewt at hotmail dot com> - 5.0-13
- Fix launcher script issues

* Wed Feb 15 2017 Jeremy Newton <alexjnewt at hotmail dot com> - 5.0-12
- Rebuilt SFML 2.4

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 4 2017 Jeremy Newton <alexjnewt at hotmail dot com> - 5.0-10
- Add launch scripts for seemless xwayland support
- Revert workaround in desktop file
- Use check macro
- Enable LTO

* Tue Jan 3 2017 Jeremy Newton <alexjnewt at hotmail dot com> - 5.0-9
- Workaround for wayland (force x11 for GUI)

* Thu Dec 22 2016 Jeremy Newton <alexjnewt at hotmail dot com> - 5.0-8
- Appdata fixes

* Fri Dec 9 2016 Jeremy Newton <alexjnewt at hotmail dot com> - 5.0-7
- Add appdata

* Tue Dec 6 2016 Jeremy Newton <alexjnewt at hotmail dot com> - 5.0-6
- License fixes with added breakdown
- Split out common data into data subpackage

* Mon Dec 5 2016 Jeremy Newton <alexjnewt at hotmail dot com> - 5.0-5
- Revert patch for curl 7.50
- Spec cleanup and fixes
- Add a patch for f26+

* Mon Jul 25 2016 Jeremy Newton <alexjnewt at hotmail dot com> - 5.0-4
- Patch for curl 7.50

* Mon Jul 25 2016 Jeremy Newton <alexjnewt at hotmail dot com> - 5.0-3
- Added systemd-devel as build require
- Rebuild for miniupnpc-2.0

* Thu Jul 7 2016 Jeremy Newton <alexjnewt at hotmail dot com> - 5.0-2
- Added patch for building with mbedtls 2.3+

* Fri Jun 24 2016 Jeremy Newton <alexjnewt at hotmail dot com> - 5.0-1
- Update to 5.0

* Thu Mar 24 2016 Jeremy Newton <alexjnewt at hotmail dot com> - 5.0-0.2rc
- Update manpages to upstream
- Disable hardened build (breaks dolphin)

* Thu Mar 3 2016 Jeremy Newton <alexjnewt at hotmail dot com> - 5.0-0.1rc
- Update to 5.0rc
- Updated manpage

* Thu Nov 12 2015 Jeremy Newton <alexjnewt at hotmail dot com> - 4.0-10
- Patch for mbedtls updated for 2.0+ (f23+)

* Thu Nov 12 2015 Jeremy Newton <alexjnewt at hotmail dot com> - 4.0-9
- Patch for X11 for f22+
- Patch for mbedtls (used to be polarssl, fixes check)
- Changed the source download link (migrated to github)

* Mon Jul 20 2015 Jeremy Newton <alexjnewt at hotmail dot com> - 4.0-8
- Disabling polarssl check, as its not working on buildsys

* Sun Jun 14 2015 Jeremy Newton <alexjnewt at hotmail dot com> - 4.0-7
- Patching for the rename of polarssl

* Tue Dec 9 2014 Jeremy Newton <alexjnewt at hotmail dot com> - 4.0-6
- Patching for GCC 4.9

* Sat Dec 6 2014 Jeremy Newton <alexjnewt at hotmail dot com> - 4.0-5
- Line got deleted by accident, build fails

* Mon Oct 27 2014 Jeremy Newton <alexjnewt at hotmail dot com> - 4.0-4
- Change in wxGTK3-devel file
- Remove unnecessary CG requirement

* Thu Oct 2 2014 Jeremy Newton <alexjnewt at hotmail dot com> - 4.0-3
- Use polarssl 1.3 (fedora 21+) to avoid bundling
- patch to use entropy functionality in SSL instead of havege

* Thu Oct 2 2014 Jeremy Newton <alexjnewt at hotmail dot com> - 4.0-2
- Bundle polarssl (temporary fix, only for F19/20)

* Mon Mar 3 2014 Jeremy Newton <alexjnewt at hotmail dot com> - 4.0-1
- Update to dolphin 4.0.2
- Removed any unnecessary patches
- Added new and updated some old patches
- Removed exclusive arch, now builds on arm

* Wed Jan 1 2014 Jeremy Newton <alexjnewt at hotmail dot com> - 3.5-6
- Build for SDL2 (Adds vibration support)

* Mon Nov 18 2013 Jeremy Newton <alexjnewt at hotmail dot com> - 3.5-5
- Added patch for SFML, thanks to Hans de Goede

* Sat Jul 27 2013 Jeremy Newton <alexjnewt at hotmail dot com> - 3.5-4
- Updated for SFML compat

* Fri Jul 26 2013 Jeremy Newton <alexjnewt at hotmail dot com> - 3.5-3
- GCC 4.8 Fix (Fedora 19 and onwards)

* Tue Feb 19 2013 Jeremy Newton <alexjnewt at hotmail dot com> - 3.5-2
- Fixed date typos in SPEC

* Tue Feb 19 2013 Jeremy Newton <alexjnewt at hotmail dot com> - 3.5-1
- Updated to latest stable: removed GCC patch, updated CLRun patch
- Added patch to build on wxwidgets 2.8 (temporary workaround)

* Sat Feb 16 2013 Jeremy Newton <alexjnewt at hotmail dot com> - 3.0-12
- Removed patch for libav and disabled ffmpeg, caused rendering issues
- Minor consistency fixes to SPEC file

* Fri Dec 14 2012 Jeremy Newton <alexjnewt at hotmail dot com> - 3.0-11
- Added patch for recent libav api change in fc18, credit to Xiao-Long Chen
- Renamed patch 1 for consistency

* Mon Jun 25 2012 Jeremy Newton <alexjnewt at hotmail dot com> - 3.0-10
- Changed CLRun buildrequire package name
- Renamed GCC 4.7 patch to suit fedora standards
- Added missing hicolor-icon-theme require

* Sat Jun 02 2012 Xiao-Long Chen <chenxiaolong@cxl.epac.to> - 3.0-9
- Add patch to fix build with gcc 4.7.0 in fc17

* Thu Apr 5 2012 Jeremy Newton <alexjnewt at hotmail dot com> - 3.0-8
- Removed bundled CLRun

* Tue Mar 13 2012 Jeremy Newton <alexjnewt at hotmail dot com> - 3.0-7
- Removed bundled bochs
- Fixed get-source-from-git.sh: missing checkout 3.0

* Fri Feb 24 2012 Jeremy Newton <alexjnewt at hotmail dot com> - 3.0-6
- Removed purposeless zerolength file
Lots of clean up and additions, thanks to Xiao-Long Chen:
- Added man page
- Added script to grab source
- Added copyright file
- Added ExclusiveArch
- Added Some missing dependencies

* Thu Feb 23 2012 Jeremy Newton <alexjnewt at hotmail dot com> - 3.0-5
- Fixed Licensing
- Split sources and fixed source grab commands

* Fri Jan 27 2012 Jeremy Newton <alexjnewt at hotmail dot com> - 3.0-4
- Tweaked to now be able to encode frame dumps

* Sun Jan 22 2012 Jeremy Newton <alexjnewt at hotmail dot com> - 3.0-3
- Building now uses cmake macro
- Turned off building shared libs
- Removed unnecessary lines
- Fixed debuginfo-without-sources issue
- Reorganization of the SPEC for readability

* Thu Jan 12 2012 Jeremy Newton <alexjnewt at hotmail dot com> - 3.0-2
- Fixed up spec to Fedora Guidelines
- Fixed various trivial mistakes
- Added SOIL and SFML to dependancies
- Removed bundled SOIL and SFML from source spin

* Sun Dec 18 2011 Jeremy Newton <alexjnewt at hotmail dot com> - 3.0-1
- Initial package SPEC created

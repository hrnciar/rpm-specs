Name: easyrpg-player
Summary: Game interpreter for RPG Maker 2000/2003 and EasyRPG games
URL: https://easyrpg.org

# EasyRPG Player itself is GPLv3+.
# It bundles several libraries: FMMidi, PicoJSON and Dirent.
#
# FMMidi files - licensed under the 3-clause BSD license:
# - src/midisequencer.cpp
# - src/midisequencer.h
# - src/midisynth.cpp
# - src/midisynth.h
#
# PicoJSON is used only for Emscripten builds (and unbundled before build).
# Dirent is used only for MS Windows builds (and unbundled before build).
License: GPLv3+ and BSD

Version: 0.6.2.1
Release: 4%{?dist}

%global repo_owner EasyRPG
%global repo_name Player
Source0: https://github.com/%{repo_owner}/%{repo_name}/archive/%{version}/%{repo_name}-%{version}.tar.gz

# Unbundle libraries
Patch0: %{name}--unbundle-picojson.patch
Patch1: %{name}--unbundle-dirent.patch

# Upstream CMake Modules have a circular dependency between Freetype and HarfBuzz.
# This patch makes the "find Freetype" and "find Harfbuzz" modules less likely
# to engage in nested searches of each other, which causes the builds to fail.
Patch2: %{name}--fix-harfbuzz-freetype-circular-dependency.patch

# Upstream CMakeLists do not work fully with out-of-source builds
Patch3: %{name}--fix-man-page-install.patch

# The way upstream CMakeLists work is that they build a dynamic library containing most of the logic,
# with the "easyrpg-player" executable and any test runners being just minimal wrappers around the library.
#
# We modify the CMakeLists to create a static library, instead. This allows us to:
# a) build the executable and the test runners without any further changes to the CMakeLists;
# b) avoid shipping an unversioned .so file that's used by just one executable.
Patch4: %{name}--no-shared-library.patch

BuildRequires: asciidoc
BuildRequires: cmake >= 3.7
BuildRequires: gcc-c++
BuildRequires: make

BuildRequires: pkgconfig(fmt)
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(harfbuzz)
BuildRequires: pkgconfig(liblcf)
BuildRequires: pkgconfig(libmpg123)
BuildRequires: pkgconfig(libpng)
BuildRequires: pkgconfig(libxmp)
BuildRequires: pkgconfig(opusfile)
BuildRequires: pkgconfig(pixman-1)
BuildRequires: pkgconfig(sdl2) >= 2.0.5
BuildRequires: pkgconfig(SDL2_mixer)
BuildRequires: pkgconfig(sndfile)
BuildRequires: pkgconfig(speexdsp)
BuildRequires: pkgconfig(vorbis)
BuildRequires: pkgconfig(wildmidi)
BuildRequires: pkgconfig(zlib)


%description
EasyRPG Player is a game interpreter for RPG Maker 2000/2003 and EasyRPG games.

To play a game, run the "%{name}" executable inside
a RPG Maker 2000/2003 game project folder (same place as RPG_RT.exe).


%prep
%setup -q -n %{repo_name}-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1


%build
%cmake \
	-DCMAKE_BUILD_TYPE=Release \
	-DPLAYER_AUDIO_BACKEND=SDL2_mixer \
	-DPLAYER_BUILD_EXECUTABLE=ON \
	-DPLAYER_BUILD_LIBLCF=OFF \
	-DPLAYER_ENABLE_TESTS=ON \
	-DPLAYER_TARGET_PLATFORM=SDL2 \
	./
%cmake_build


%install
%cmake_install


%check
%cmake_build --target check


%files
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man6/%{name}.6*


%changelog
* Sun Aug 09 2020 Artur Iwicki <fedora@svgames.pl> - 0.6.2.1-4
- Add missing (optional) build-time dependency on HarfBuzz

* Fri Aug 07 2020 Artur Iwicki <fedora@svgames.pl> - 0.6.2.1-3
- Add a patch to avoid creating libEasyRPG_Player.so
- Switch to BuildRequiring all libraries via pkgconfig()

* Mon Aug 03 2020 Artur Iwicki <fedora@svgames.pl> - 0.6.2.1-2
- Add missing BuildRequires on asciidoc (needed for man pages)
- Unbundle PicoJSON and Dirent before build
- Fix building and running tests during %%check

* Fri Jul 31 2020 Artur Iwicki <fedora@svgames.pl> - 0.6.2.1-1
- Initial packaging

Name: opensurge
Summary: 2D retro platformer inspired by Sonic games
License: GPLv3

Version: 0.5.1.2
Release: 6%{?dist}

URL: https://opensurge2d.org
Source0: https://github.com/alemart/opensurge/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: allegro5-devel
BuildRequires: allegro5-addon-acodec-devel
BuildRequires: allegro5-addon-audio-devel
BuildRequires: allegro5-addon-dialog-devel
BuildRequires: allegro5-addon-image-devel
BuildRequires: allegro5-addon-ttf-devel
BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: libappstream-glib
BuildRequires: surgescript-devel

%global fontlist font(roboto) font(gothica1)
BuildRequires: fontconfig
BuildRequires: %{fontlist}

Requires: %{name}-data = %{version}-%{release}

%description
Open Surge is a fun 2D retro platformer inspired by Sonic games,
and a game creation system that lets you unleash your creativity!

Open Surge is two projects in one: a game
and a game creation system (game engine).


%package data
Summary: Data files for opensurge
BuildArch: noarch

Requires: %{fontlist}

# Most of the game's assets are licensed under CC-BY 3.0.
# Some individual files are licensed under CC-BY-SA 3.0 / Public Domain.
#
# There also bundled fonts (Google Roboto and HanYang Gothic A1),
# but we un-bundle them, so they don't apply to the License tag here.
#
# For a detailed list, consult src/misc/credits.c inside the source archive.
License: CC-BY and CC-BY-SA and CC0 and Public Domain

%description data
Data files (graphics, music, sounds) required by Open Surge.


%prep
%setup -q


%build
mkdir build && cd build
%cmake \
	-DCMAKE_BUILD_TYPE=Release  \
	-DUSE_A5=ON  \
	-DALLEGRO_STATIC=OFF  \
	-DALLEGRO_MONOLITH=OFF  \
	"-DGAME_DATADIR=%{_datadir}/%{name}"  \
	-DDESKTOP_INSTALL=ON  \
	"-DDESKTOP_ENTRY_PATH=%{_datadir}/applications"  \
	"-DDESKTOP_ICON_PATH=%{_datadir}/pixmaps"  \
	"-DDESKTOP_METAINFO_PATH=%{_metainfodir}"  \
	..
%make_build


%install
cd build/
%make_install

# The install section of CMakeLists.txt just plops the executable inside /usr/
# We need to move it to /usr/bin/
install -m 755 -d %{buildroot}%{_bindir}
mv %{buildroot}%{_prefix}/%{name} %{buildroot}%{_bindir}/%{name}

# Remove bundled fonts and replace them with symlinks
for GOTHIC in Bold Medium; do
	ln -sf  \
		"$(fc-match -f '%%{file}' "Gothic A1:${GOTHIC}")"  \
		"%{buildroot}/%{_datadir}/%{name}/fonts/GothicA1-${GOTHIC}.ttf"
done
for ROBOTO in Black Bold Medium; do
	ln -sf  \
		"$(fc-match -f '%%{file}' "Roboto:${ROBOTO}")"  \
		"%{buildroot}/%{_datadir}/%{name}/fonts/Roboto-${ROBOTO}.ttf"
done

# The licenses are not readable inside the game,
# and since we un-bundle this font, we might as well remove its license
rm %{buildroot}%{_datadir}/%{name}/licenses/LICENSE-GothicA1.ttf.txt


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/%{name}.appdata.xml


%files
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/pixmaps/%{name}.png


%files data
%license licenses/CC-BY-3.0-legalcode.txt
%{_datadir}/%{name}/


%changelog
* Fri Jun 05 2020 Artur Iwicki <fedora@svgames.pl> - 0.5.1.2-6
- Move the Requires: on fonts from main package to -data subpackage
- Use different %%license files for the main package and -data subpackage

* Tue May 26 2020 Artur Iwicki <fedora@svgames.pl> - 0.5.1.2-5
- Unbundle HanYang Gothic A1 fonts
- Use fc-match to find font files instead of relying on hard-coded paths
- Wrap description to 80 chars per line

* Mon Apr 13 2020 Artur Iwicki <fedora@svgames.pl> - 0.5.1.2-4
- Unbundle surgescript
- Drop Source1 (updated CMakeLists.txt) - not needed since
  we no longer link surgescript statically
- Once again correct the License: tag on the -data subpackage
  and add a comment explaining the licensing breakdown
- Add a Provides: bundled() for the HanYang fonts

* Sun Apr 12 2020 Artur Iwicki <fedora@svgames.pl> - 0.5.1.2-2
- Correct the License: tag on the -data subpackage
- Unbundle Roboto fonts

* Sat Apr 11 2020 Artur Iwicki <fedora@svgames.pl> - 0.5.1.2-1
- Initial packaging

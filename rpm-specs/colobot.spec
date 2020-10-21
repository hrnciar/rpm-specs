Name: colobot
%global orgname info.colobot.Colobot

Version: 0.1.12
Release: 10%{?dist}
Summary: A video game that teaches programming in a fun way

License: GPLv3
URL: https://colobot.info

%global giturl https://github.com/colobot
%global gittag colobot-gold-%{version}-alpha
Source0: %{giturl}/colobot/archive/%{gittag}/colobot-%{gittag}.tar.gz
Source1: %{giturl}/colobot-data/archive/%{gittag}/colobot-data-%{gittag}.tar.gz

# Music files are licensed under GPLv3, like the rest of the game.
# They are not kept in the colobot-data repo, and by default are downloaded during the build.
# Since Fedora builders have net-access disabled, we need to download them beforehand.
%global musicurl https://colobot.info/files/music
Source100: %{musicurl}/Intro1.ogg
Source101: %{musicurl}/Intro2.ogg
Source102: %{musicurl}/music002.ogg
Source103: %{musicurl}/music003.ogg
Source104: %{musicurl}/music004.ogg
Source105: %{musicurl}/music005.ogg
Source106: %{musicurl}/music006.ogg
Source107: %{musicurl}/music007.ogg
Source108: %{musicurl}/music008.ogg
Source109: %{musicurl}/music009.ogg
Source110: %{musicurl}/music010.ogg
Source111: %{musicurl}/music011.ogg
Source112: %{musicurl}/music012.ogg
Source113: %{musicurl}/music013.ogg
Source114: %{musicurl}/Constructive.ogg
Source115: %{musicurl}/Humanitarian.ogg
Source116: %{musicurl}/Hv2.ogg
Source117: %{musicurl}/Quite.ogg
Source118: %{musicurl}/Infinite.ogg
Source119: %{musicurl}/Proton.ogg
Source120: %{musicurl}/Prototype.ogg


# The game uses the translated string "Player" as the default player name
# yet it does not properly handle UTF-8 in player names,
# so non-English speakers may have the game always crash when putting in the player name.
#
# See: https://github.com/colobot/colobot/issues/1268 
Patch0: colobot--do-not-translate-default-player-name.patch

# GCC10 complains about unknown identifiers
Patch1: colobot--missing-includes.patch

# GCC11 complains about potential NULL from dynamic cast, fix them
Patch2: colobot-gcc11.patch

BuildRequires: boost-devel >= 1.51
BuildRequires: boost-filesystem >= 1.51
BuildRequires: boost-regex >= 1.51
BuildRequires: cmake >= 2.8
BuildRequires: desktop-file-utils
BuildRequires: gcc-c++
BuildRequires: gettext-devel >= 0.18
BuildRequires: glew-devel >= 1.8.0
BuildRequires: libappstream-glib
BuildRequires: libogg-devel >= 1.3.0
BuildRequires: libpng-devel >= 1.2
BuildRequires: libsndfile-devel >= 1.0.25
BuildRequires: libvorbis >= 1.3.2
BuildRequires: openal-soft-devel >= 1.13
BuildRequires: po4a
BuildRequires: physfs-devel
BuildRequires: python3-devel
BuildRequires: SDL2-devel SDL2_image-devel SDL2_ttf-devel
BuildRequires: xmlstarlet
BuildRequires: %{_bindir}/pod2man
BuildRequires: %{_bindir}/rsvg-convert

Requires: colobot-data = %{version}-%{release}
Requires: colobot-music = %{version}-%{release}
Requires: hicolor-icon-theme

%description
Colobot: Gold Edition is a real-time strategy game, where you can program
your units (bots) in a language called CBOT, which is similar to C++ and Java.
Your mission is to find a new planet to live and survive.
You can save the humanity and get programming skills!


%package data
Summary: Data files for Colobot: Gold Edition
BuildArch: noarch

%description data
Data files (graphics, sounds, levels) required to run Colobot Gold.


%package music
Summary: Music for Colobot: Gold Edition
BuildArch: noarch

%description music
Music files used by Colobot Gold.


%prep
%setup -q -n colobot-%{gittag}
%patch0 -p1
%patch1 -p1
%patch2 -p1

rm -rf ./data
cp %{SOURCE1} ./data.tgz
tar xzf ./data.tgz
rm ./data.tgz
mv ./colobot-data-%{gittag} ./data

cp -a %{SOURCE100} data/music/
cp -a %{SOURCE101} data/music/
cp -a %{SOURCE102} data/music/
cp -a %{SOURCE103} data/music/
cp -a %{SOURCE104} data/music/
cp -a %{SOURCE105} data/music/
cp -a %{SOURCE106} data/music/
cp -a %{SOURCE107} data/music/
cp -a %{SOURCE108} data/music/
cp -a %{SOURCE109} data/music/
cp -a %{SOURCE110} data/music/
cp -a %{SOURCE111} data/music/
cp -a %{SOURCE112} data/music/
cp -a %{SOURCE113} data/music/
cp -a %{SOURCE114} data/music/
cp -a %{SOURCE115} data/music/
cp -a %{SOURCE116} data/music/
cp -a %{SOURCE117} data/music/
cp -a %{SOURCE118} data/music/
cp -a %{SOURCE119} data/music/
cp -a %{SOURCE120} data/music/

sed \
  -e 's|set(COLOBOT_INSTALL_BIN_DIR ${CMAKE_INSTALL_PREFIX}/games |set(COLOBOT_INSTALL_BIN_DIR %{_bindir}/ |' \
  -e 's|set(COLOBOT_INSTALL_LIB_DIR ${CMAKE_INSTALL_PREFIX}/lib/colobot |set(COLOBOT_INSTALL_LIB_DIR %{_libdir}/colobot |' \
  -e 's|set(COLOBOT_INSTALL_DATA_DIR ${CMAKE_INSTALL_PREFIX}/share/games/colobot |set(COLOBOT_INSTALL_DATA_DIR %{_datadir}/colobot |' \
  -e 's|set(COLOBOT_INSTALL_I18N_DIR ${CMAKE_INSTALL_PREFIX}/share/locale |set(COLOBOT_INSTALL_I18N_DIR %{_datadir}/locale |' \
  -e 's|set(COLOBOT_INSTALL_DOC_DIR ${CMAKE_INSTALL_PREFIX}/share/doc/colobot |set(COLOBOT_INSTALL_DOC_DIR %{_datadir}/doc/colobot |' \
  -i CMakeLists.txt


%build
%cmake -DCMAKE_BUILD_TYPE=Release -DPYTHON_EXECUTABLE=%{__python3} ./
%cmake_build


%install
%cmake_install

# Change the .desktop file name to match the .appdata.xml file name
mv %{buildroot}%{_datadir}/applications/%{name}.desktop %{buildroot}%{_datadir}/applications/%{orgname}.desktop
sed -e 's|%{name}.desktop|%{orgname}.desktop|' -i %{buildroot}%{_metainfodir}/%{orgname}.appdata.xml

%find_lang %{name} --with-man


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{orgname}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{orgname}.appdata.xml


%files -f %{name}.lang
%license LICENSE.txt
%{_bindir}/%{name}
%{_libdir}/%{name}/

%{_datadir}/applications/%{orgname}.desktop
%{_metainfodir}/%{orgname}.appdata.xml

%{_datadir}/icons/hicolor/**/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_mandir}/man6/%{name}.6*


%files data
%license LICENSE.txt
%{_datadir}/%{name}/
%exclude %{_datadir}/%{name}/music


%files music
%license LICENSE.txt
%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/music/


%changelog
* Thu Sep 03 2020 Jeff Law <law@redhat.com> - 0.1.12-10
- Fix dynamic casts to avoid gcc-11 diagnostics

* Tue Jul 28 2020 Artur Iwicki <fedora@svgames.pl> - 0.1.12-9
- Update spec to use the new cmake_build and cmake_install macros

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.12-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Artur Iwicki <fedora@svgames.pl> - 0.1.12-7
- Edit Patch1 (missing includes) - fix build failures on Rawhide

* Fri Feb 07 2020 Artur Iwicki <fedora@svgames.pl> - 0.1.12-6
- Add a patch to fix build failures in Rawhide

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Oct 07 2019 Artur Iwicki <fedora@svgames.pl> - 0.1.12-4
- Make the game always use "Player" as the default player name
  (fixes the game crashing under certain system locale settings)
- Rename the .desktop file to match the .appdata.xml file name

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 24 2019 Artur Iwicki <fedora@svgames.pl> - 0.1.12-2
- Replace python3 BR with python3-devel
- Move music files to the fepdkg lookaside cache

* Sun Feb 24 2019 Artur Iwicki <fedora@svgames.pl> - 0.1.12-1
- Update to newest upstream release
- Drop Patch0 (appdata.xml file) - merged upstream
- Drop Patch1 (use snprintf() instead of sprintf()) - issue fixed upstream
- Drop Patch2 (strncpy() fix) - merged upstream

* Sat Feb 02 2019 Artur Iwicki <fedora@svgames.pl> - 0.1.11.1-8
- Add a patch for strncpy() usages

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.11.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 19 2018 Miro Hrončok <miro@hroncok.cz> - 0.1.11.1-7
- Use python3 during build instead of python2

* Tue Nov 13 2018 Artur Iwicki <fedora@svgames.pl> - 0.1.11.1-6
- Use %%find_lang for .mo files and man pages

* Thu Nov 08 2018 Artur Iwicki <fedora@svgames.pl> - 0.1.11.1-5
- Change the Summary: to something more descriptive
- Add a comment on music files
- Preserve timestamps on music files

* Thu Nov 08 2018 Artur Iwicki <fedora@svgames.pl> - 0.1.11.1-4
- Add a Requires: for hicolor-icon-theme
- Validate the desktop and appdata file

* Sun Nov 04 2018 Artur Iwicki <fedora@svgames.pl> - 0.1.11.1-3
- Fix build failures on F28 and later

* Mon Oct 29 2018 Artur Iwicki <fedora@svgames.pl> - 0.1.11.1-2
- Add an Appdata XML file
- Move music into a separate subpackage

* Tue Oct 16 2018 Artur Iwicki <fedora@svgames.pl> - 0.1.11.1-1
- Initial packaging

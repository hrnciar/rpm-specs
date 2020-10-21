%global shortname flare
Name:       flare-engine
Version:    1.07
Release:    6%{?dist}
Summary:    A single player, 2D-isometric, action Role-Playing Engine
License:    GPLv3+
URL:        http://www.flarerpg.org
Source0:    http://downloads.sourceforge.net/project/flare-game/Linux/%{name}-v%{version}.tar.gz

Requires:   liberation-sans-fonts
Requires:   unifont-fonts

BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: SDL2_gfx-devel
BuildRequires: SDL2_image-devel
BuildRequires: SDL2_mixer-devel
BuildRequires: SDL2_ttf-devel
BuildRequires: desktop-file-utils

%description
Flare (Free Libre Action Roleplaying Engine) is a simple game engine built to
handle a very specific kind of game: single-player 2D action RPGs. Flare is not 
a re-implementation of an existing game or engine. It is a tribute to and 
exploration of the action RPG genre.

Rather than building a very abstract, robust game engine, the goal of this
project is to build several real games and harvest an engine from the common,
reusable code. The first game, in progress, is a fantasy dungeon crawl.

Flare uses simple file formats (INI style config files) for most of the game
data, allowing anyone to easily modify game contents. Open formats are
preferred (png, ogg). The game code is C++.

This package contains the engine only.


%prep
%setup -q -n %{name}-v%{version}


%build
%cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} -DBINDIR="bin" -DDATADIR="share/%{shortname}/" .
%cmake_build


%install
%cmake_install

# Use system fonts
find %{buildroot}%{_datadir}/%{shortname}/ -name "*.ttf" -delete -print
ln -s %{_datadir}/fonts/liberation/LiberationSans-Regular.ttf %{buildroot}%{_datadir}/%{shortname}/mods/default/fonts/LiberationSans-Regular.ttf
# slightly wrong version number, but should be fine, past releases shipped without it at all
ln -s %{_datadir}/fonts/unifont/unifont.ttf %{buildroot}%{_datadir}/%{shortname}/mods/default/fonts/unifont-10.0.06.ttf

# Validate desktop file
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{shortname}.desktop


%files
%doc COPYING README.engine.md CREDITS.engine.txt RELEASE_NOTES.txt
%{_bindir}/%{shortname}
%{_datadir}/%{shortname}/
%{_datadir}/applications/%{shortname}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{shortname}.svg
%{_mandir}/man6/%{shortname}.6*


%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Sep 09 2018 Erik Schilling <ablu.erikschilling@googlemail.com> - 1.07-1
- Updated to 1.07

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.19-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.19-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.19-4
- Rebuilt for GCC 5 C++11 ABI change

* Wed Aug 06 2014 Erik Schilling <ablu.erikschilling@googlemail.com> - 0.19-3
- Added -print to find call

* Wed Jul 30 2014 Erik Schilling <ablu.erikschilling@googlemail.com> - 0.19-2
- Actually apply system gfx patch
- Disallow the project to override environment compiler flags
- Delete bundeled ttf and use symlink
- Added missing mail address to changelog

* Sat Mar 01 2014 Erik Schilling <ablu.erikschilling@googlemail.com> - 0.19-1
- Seperated out engine into a seperate package like upstream did
- Previously this engine was part of the flare package

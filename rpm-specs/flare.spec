Name:       flare
Version:    1.07
Release:    7%{?dist}
Summary:    A single player, 2D-isometric, action Role-Playing Game
License:    CC-BY-SA and CC-BY and CC0 and Public Domain
URL:        http://www.flarerpg.org
Source0:    http://downloads.sourceforge.net/project/%{name}-game/Linux/%{name}-game-v%{version}.tar.gz
# https://github.com/clintbellanger/flare-game/pull/774
Patch0:     %{name}-appdata-location-fix.patch

Requires:   %{name}-engine%{?_isa} = %{version}
Requires:   liberation-sans-fonts

Obsoletes:   %{name}-data <= 0.18

BuildRequires: cmake
BuildRequires: libappstream-glib
BuildRequires: gcc
BuildRequires: gcc-c++

BuildArch: noarch


%description
Flare (Free Libre Action Roleplaying Engine) is a simple game engine built to
handle a very specific kind of game: single-player 2D action RPGs. Flare is not
a re-implementation of an existing game or engine. It is a tribute to and
exploration of the action RPG genre.

Rather than building a very abstract, robust game engine, the goal of this
project is to build several real games and harvest an engine from the common,
reusable code. The first game, in progress, is a fantasy dungeon crawl.

Flare uses simple file formats (INI style configuration files) for most of
the game data, allowing anyone to easily modify game contents. Open formats are
preferred (png, ogg). The game code is C++.

%prep
%setup -q -n %{name}-game-v%{version}
%patch0 -p1


%build
# Do not use /usr/games or /usr/share/games/
%cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} -DBINDIR="bin" -DDATADIR="share/%{name}/" .
%cmake_build


%install
%cmake_install

# Use system font
find %{buildroot}%{_datadir}/%{name}/ -name "*.ttf" -delete -print
ln -s %{_datadir}/fonts/liberation/LiberationSans-Bold.ttf %{buildroot}%{_datadir}/%{name}/mods/fantasycore/fonts/LiberationSans-Bold.ttf
ln -s %{_datadir}/fonts/liberation/LiberationSans-Italic.ttf %{buildroot}%{_datadir}/%{name}/mods/fantasycore/fonts/LiberationSans-Italic.ttf
ln -s %{_datadir}/fonts/liberation/LiberationSans-Regular.ttf %{buildroot}%{_datadir}/%{name}/mods/fantasycore/fonts/LiberationSans-Regular.ttf

# Validate appdata
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml


%files
%doc README LICENSE.txt CREDITS.txt

%{_metainfodir}/*.appdata.xml
%{_datadir}/%{name}/mods/*/
%exclude %{_datadir}/%{name}/mods/*/languages/
%dir %{_datadir}/%{name}/mods/*/languages/
# info files about locales (but not the .po files!)
%{_datadir}/%{name}/mods/*/languages/*[!o]

# LOCALES:
# For updating (replace %% with single one):
# find -name "*.po" | sed 's/^.\/\(.*[a-z]\+\.\)\(.\+\)\.po/%%lang(\2) %%{_datadir}\/%%{name}\/\1\2.po/' | sort
%lang(be) %{_datadir}/%{name}/mods/empyrean_campaign/languages/data.be.po
%lang(be) %{_datadir}/%{name}/mods/fantasycore/languages/data.be.po
%lang(bg) %{_datadir}/%{name}/mods/empyrean_campaign/languages/data.bg.po
%lang(bg) %{_datadir}/%{name}/mods/fantasycore/languages/data.bg.po
%lang(cs) %{_datadir}/%{name}/mods/empyrean_campaign/languages/data.cs.po
%lang(cs) %{_datadir}/%{name}/mods/fantasycore/languages/data.cs.po
%lang(de) %{_datadir}/%{name}/mods/empyrean_campaign/languages/data.de.po
%lang(de) %{_datadir}/%{name}/mods/fantasycore/languages/data.de.po
%lang(el) %{_datadir}/%{name}/mods/empyrean_campaign/languages/data.el.po
%lang(el) %{_datadir}/%{name}/mods/fantasycore/languages/data.el.po
%lang(es) %{_datadir}/%{name}/mods/empyrean_campaign/languages/data.es.po
%lang(es) %{_datadir}/%{name}/mods/fantasycore/languages/data.es.po
%lang(fi) %{_datadir}/%{name}/mods/empyrean_campaign/languages/data.fi.po
%lang(fi) %{_datadir}/%{name}/mods/fantasycore/languages/data.fi.po
%lang(fr) %{_datadir}/%{name}/mods/empyrean_campaign/languages/data.fr.po
%lang(fr) %{_datadir}/%{name}/mods/fantasycore/languages/data.fr.po
%lang(gd) %{_datadir}/%{name}/mods/empyrean_campaign/languages/data.gd.po
%lang(gd) %{_datadir}/%{name}/mods/fantasycore/languages/data.gd.po
%lang(gl) %{_datadir}/%{name}/mods/empyrean_campaign/languages/data.gl.po
%lang(gl) %{_datadir}/%{name}/mods/fantasycore/languages/data.gl.po
%lang(he) %{_datadir}/%{name}/mods/empyrean_campaign/languages/data.he.po
%lang(he) %{_datadir}/%{name}/mods/fantasycore/languages/data.he.po
%lang(it) %{_datadir}/%{name}/mods/empyrean_campaign/languages/data.it.po
%lang(it) %{_datadir}/%{name}/mods/fantasycore/languages/data.it.po
%lang(ja) %{_datadir}/%{name}/mods/empyrean_campaign/languages/data.ja.po
%lang(ja) %{_datadir}/%{name}/mods/fantasycore/languages/data.ja.po
%lang(nb) %{_datadir}/%{name}/mods/empyrean_campaign/languages/data.nb.po
%lang(nb) %{_datadir}/%{name}/mods/fantasycore/languages/data.nb.po
%lang(nl) %{_datadir}/%{name}/mods/empyrean_campaign/languages/data.nl.po
%lang(nl) %{_datadir}/%{name}/mods/fantasycore/languages/data.nl.po
%lang(pl) %{_datadir}/%{name}/mods/empyrean_campaign/languages/data.pl.po
%lang(pl) %{_datadir}/%{name}/mods/fantasycore/languages/data.pl.po
%lang(pt_BR) %{_datadir}/%{name}/mods/empyrean_campaign/languages/data.pt_BR.po
%lang(pt_BR) %{_datadir}/%{name}/mods/fantasycore/languages/data.pt_BR.po
%lang(pt) %{_datadir}/%{name}/mods/empyrean_campaign/languages/data.pt.po
%lang(pt) %{_datadir}/%{name}/mods/fantasycore/languages/data.pt.po
%lang(ru) %{_datadir}/%{name}/mods/empyrean_campaign/languages/data.ru.po
%lang(ru) %{_datadir}/%{name}/mods/fantasycore/languages/data.ru.po
%lang(sk) %{_datadir}/%{name}/mods/empyrean_campaign/languages/data.sk.po
%lang(sk) %{_datadir}/%{name}/mods/fantasycore/languages/data.sk.po
%lang(sv) %{_datadir}/%{name}/mods/empyrean_campaign/languages/data.sv.po
%lang(sv) %{_datadir}/%{name}/mods/fantasycore/languages/data.sv.po
%lang(uk) %{_datadir}/%{name}/mods/empyrean_campaign/languages/data.uk.po
%lang(uk) %{_datadir}/%{name}/mods/fantasycore/languages/data.uk.po
%lang(zh) %{_datadir}/%{name}/mods/empyrean_campaign/languages/data.zh.po
%lang(zh) %{_datadir}/%{name}/mods/fantasycore/languages/data.zh.po


%changelog
* Wed Oct 07 2020 Erik Schilling <git@ablu.org> - 1.07-7
- Fixes for
  https://fedoraproject.org/wiki/Changes/CMake_to_do_out-of-source_builds#Migration

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

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.19-9
- Remove obsolete scriptlets

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.19-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 0.19-4
- Add an AppData file for the software center

* Tue Sep 2 2014 Marcos Paulo de Souza <marcos.souza.org@gmail.com> - 0.19-3
- Fixed desktop file by removing TryExec args

* Wed Aug 20 2014 Erik Schilling <ablu.erikschilling@googlemail.com> - 0.19-2
- Fixed cmake dependency

* Tue Aug 19 2014 Erik Schilling <ablu.erikschilling@googlemail.com> 0.19-1
- New release
- Splitted out engine code into flare-engine package

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 13 2014 Hans de Goede <hdegoede@redhat.com> - 0.18-5
- Rebuild for new SDL_gfx

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Apr 1 2013 Erik Schilling <ablu.erikschilling@googlemail.com> 0.18-2
- Adapted to the newly updated release tar
- Since the old one was kind of broken and incomplete a new one was generated

* Mon Apr 1 2013 Erik Schilling <ablu.erikschilling@googlemail.com> 0.18-1
- New upstream release
- Breaks compatibillity with old save files

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Nov 13 2012 Erik Schilling <ablu.erikschilling@googlemail.com> 0.17.1-8
- Simplified directiory permissions

* Mon Nov 12 2012 Erik Schilling <ablu.erikschilling@googlemail.com> 0.17.1-7
- Fixed directory ownership

* Sun Nov 11 2012 Erik Schilling <ablu.erikschilling@googlemail.com> 0.17.1-6
- Spell-fix: reimplementation --> re-implementation
- Mark translation files with %%lang

* Fri Nov 02 2012 Erik Schilling <ablu.erikschilling@googlemail.com> 0.17.1-5
- Dropped / between path makros
- Made use of %%{name} makro in Source1
- Made sure that the binary links against system SDL_gfx parts
- Replaced unifont use with dejavu since the font was not packaged

* Thu Oct 25 2012 Erik Schilling <ablu.erikschilling@googlemail.com> 0.17.1-4
- Fixed require of binaries in -data package
- Fixed update icon cache
- Fixed trailing slash of url
- Fixed license from GPLv3 to GPLv3+

* Sat Oct 6 2012 Erik Schilling <ablu.erikschilling@googlemail.com> 0.17.1-3
- Do not install to /usr/share/games but /usr/share (https://fedoraproject.org/wiki/SIGs/Games/Packaging)

* Sat Oct 6 2012 Erik Schilling <ablu.erikschilling@googlemail.com> 0.17.1-2
- Added BuildArch: noarch for data package

* Fri Oct 5 2012 Erik Schilling <ablu.erikschilling@googlemail.com> 0.17.1-1
- Initial packaging

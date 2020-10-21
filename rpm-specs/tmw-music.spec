%global project themanaworld
%global commit0 0fe3e2164dc75117af1f3c96aeb7599ba3495f71
%global date0   20151005

Name:           tmw-music
# we do not know any newer version, latest from obsolete Sourceforge is 0.3
Version:        0.3.0.1
Release:        0.9.%{date0}git%(c=%{commit0}; echo ${c:0:7})%{?dist}
Summary:        Music files for The Mana World

# generally license is GPLv2, most ogg files with CC-BY-SA,
# but CC0 for ride-of-the-valkyries.ogg (see music-license.md)
License:        GPLv2 and CC-BY-SA and CC0
URL:            https://www.%{project}.org
Source0:        https://github.com/%{project}/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{commit0}.tar.gz
BuildArch:      noarch

# let people find us via project name
Provides:       %{project}-music

Obsoletes:      manaworld-music <= 0.3-4
Provides:       manaworld-music = %{version}-%{release}

Requires:       tmw

%description
This package contains the optional music files for The Mana World (TMW). 
TMW is an innovative, free and open source MMORPG.
Besides the official game server, this client can connect to multiple
community-grown servers, which provide varied environments and further
challenge. In TMW, the players solve quests, fight monsters, practice skills
and study magic. Social activities include parties, trading and limited PvP in
designated areas. While there are no limits to solo play, collaborative
behavior such as healing others, fighting together and banding up against
tougher monsters are rewarded in the game. The Mana World graphics have been
inspired by 2D pixel art at its prime of the late 1990s, when many RPG
classics, such as Secret of Mana for the Super Nintendo Entertainment System,
were released.


%prep
%setup -q -n %{name}-%{commit0}


%build
# nothing to build


%install
mkdir -p %{buildroot}%{_datadir}/tmw/data/music
cp -p *.ogg %{buildroot}%{_datadir}/tmw/data/music


%files
%license COPYING music-license.md
%doc README.md
# just in case, we're not absolutely sure what folders are owned already
%dir %{_datadir}/tmw
%dir %{_datadir}/tmw/data
%dir %{_datadir}/tmw/data/music
%{_datadir}/tmw/data/music/*.ogg


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0.1-0.9.20151005git0fe3e21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0.1-0.8.20151005git0fe3e21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0.1-0.7.20151005git0fe3e21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0.1-0.6.20151005git0fe3e21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0.1-0.5.20151005git0fe3e21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0.1-0.4.20151005git0fe3e21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0.1-0.3.20151005git0fe3e21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0.1-0.2.20151005git0fe3e21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Feb 28 2016 Raphael Groner <projects.rg@smart.ms> - 0.3.0.1-0.1.20151005git0fe3e21
- upstream moved to GitHub
- use license macro, mention CC-BY-SA and CC0 for individual ogg files
- add virtual Provides

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Sep 25 2012 Martin Gieseking <martin.gieseking@uos.de> 0.3-5
- initial package (replaces manaworld-music)


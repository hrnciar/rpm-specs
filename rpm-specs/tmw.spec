%global srcname themanaworld

Name:           tmw
Version:        20130201
Release:        14%{?dist}
Summary:        The Mana World is a 2D MMORPG

License:        GPLv2
URL:            https://www.%{srcname}.org
Source0:        https://github.com/%{srcname}/%{name}-branding/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:      noarch

# let people find us via real name
Provides:       %{srcname}
Provides:       %{srcname}-branding
Suggests:       %{name}-music

Obsoletes:      manaworld <= 0.5.2
Provides:       manaworld

BuildRequires:  desktop-file-utils
Requires:       manaplus

%description
The Mana World (TMW for short) is an innovative, free and open source MMORPG.
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
%setup -q -n %{name}-branding-%{version}
rm -f data/icons/*.{icns,ico}


%build
# nothing to build


%install
install -D -p -m 755 %{name} %{buildroot}%{_bindir}/%{name}
install -D -p -m 644 data/icons/%{name}.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
install -D -p -m 644 %{name}.mana %{buildroot}%{_datadir}/%{name}/%{name}.mana
mv data/ %{buildroot}%{_datadir}/%{name}/
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{name}.desktop


%files
%license COPYING 
%doc README
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20130201-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20130201-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20130201-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20130201-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20130201-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20130201-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20130201-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20130201-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Feb 28 2016 Raphael Groner <projects.rg@smart.ms> - 20130201-6
- upstream moved to GitHub, rebuild with new tarball
- use license macro
- enable package alias (virtual Provides)
- suggest music package

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20130201-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20130201-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20130201-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20130201-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Mar 20 2013 Martin Gieseking <martin.gieseking@uos.de> 20130201-1
- updated to new release 20130201
- replaced Requires: mana by manaplus

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20110911-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Oct 02 2012 Martin Gieseking <martin.gieseking@uos.de> 20110911-2
- added explicit version to Obsolotes: manaworld

* Tue Sep 25 2012 Martin Gieseking <martin.gieseking@uos.de> 20110911-1
- initial package


%global vergit  20200710
%global tname   Flat-Remix

Name:           flat-remix-icon-theme
Version:        0.0.%{vergit}
Release:        2%{?dist}
Summary:        Icon theme inspired on material design

# The entire source code is GPLv3+ except:
# GPLv3:        Numix icon theme
#               Papirus icon theme
# CC-BY-SA:     EvoPop icon theme
#               Flattr icon theme
#               Paper icon theme
License:        GPLv3+ and CC-BY-SA
URL:            https://github.com/daniruiz/flat-remix
Source0:        %{url}/archive/%{vergit}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  fdupes

Requires:       adwaita-icon-theme
Requires:       gnome-icon-theme
Requires:       hicolor-icon-theme

Recommends:     flat-remix-gtk2-theme
Recommends:     flat-remix-gtk3-theme

Suggests:       flat-remix-theme
Suggests:       gnome-shell-theme-flat-remix

%description
Flat Remix icon theme is a pretty simple Linux icon theme inspired on material
design. It is mostly flat with some shadows, highlights and gradients for some
depth, and uses a colorful palette with nice contrasts.


%prep
%autosetup -n flat-remix-%{vergit}


%build
%make_build


%install
%make_install
%fdupes -s %{buildroot}%{_datadir}

touch %{buildroot}%{_datadir}/icons/%{tname}-Blue/icon-theme.cache
touch %{buildroot}%{_datadir}/icons/%{tname}-Blue-Dark/icon-theme.cache
touch %{buildroot}%{_datadir}/icons/%{tname}-Blue-Light/icon-theme.cache
touch %{buildroot}%{_datadir}/icons/%{tname}-Green/icon-theme.cache
touch %{buildroot}%{_datadir}/icons/%{tname}-Green-Dark/icon-theme.cache
touch %{buildroot}%{_datadir}/icons/%{tname}-Green-Light/icon-theme.cache
touch %{buildroot}%{_datadir}/icons/%{tname}-Red/icon-theme.cache
touch %{buildroot}%{_datadir}/icons/%{tname}-Red-Dark/icon-theme.cache
touch %{buildroot}%{_datadir}/icons/%{tname}-Red-Light/icon-theme.cache
touch %{buildroot}%{_datadir}/icons/%{tname}-Yellow/icon-theme.cache
touch %{buildroot}%{_datadir}/icons/%{tname}-Yellow-Dark/icon-theme.cache
touch %{buildroot}%{_datadir}/icons/%{tname}-Yellow-Light/icon-theme.cache

%transfiletriggerin -- %{_datadir}/icons/%{tname}-Blue
gtk-update-icon-cache --force %{_datadir}/icons/%{tname}-Blue &>/dev/null || :

%transfiletriggerin -- %{_datadir}/icons/%{tname}-Blue-Dark
gtk-update-icon-cache --force %{_datadir}/icons/%{tname}-Blue-Dark &>/dev/null || :

%transfiletriggerin -- %{_datadir}/icons/%{tname}-Blue-Light
gtk-update-icon-cache --force %{_datadir}/icons/%{tname}-Blue-Light &>/dev/null || :

%transfiletriggerin -- %{_datadir}/icons/%{tname}-Green
gtk-update-icon-cache --force %{_datadir}/icons/%{tname}-Green &>/dev/null || :

%transfiletriggerin -- %{_datadir}/icons/%{tname}-Green-Dark
gtk-update-icon-cache --force %{_datadir}/icons/%{tname}-Green-Dark &>/dev/null || :

%transfiletriggerin -- %{_datadir}/icons/%{tname}-Green-Light
gtk-update-icon-cache --force %{_datadir}/icons/%{tname}-Green-Light &>/dev/null || :

%transfiletriggerin -- %{_datadir}/icons/%{tname}-Yellow
gtk-update-icon-cache --force %{_datadir}/icons/%{tname}-Yellow &>/dev/null || :

%transfiletriggerin -- %{_datadir}/icons/%{tname}-Yellow-Dark
gtk-update-icon-cache --force %{_datadir}/icons/%{tname}-Yellow-Dark &>/dev/null || :

%transfiletriggerin -- %{_datadir}/icons/%{tname}-Yellow-Light
gtk-update-icon-cache --force %{_datadir}/icons/%{tname}-Yellow-Light &>/dev/null || :

# ---

%transfiletriggerpostun -- %{_datadir}/icons/%{tname}-Blue
gtk-update-icon-cache --force %{_datadir}/icons/%{tname}-Blue &>/dev/null || :

%transfiletriggerpostun -- %{_datadir}/icons/%{tname}-Blue-Dark
gtk-update-icon-cache --force %{_datadir}/icons/%{tname}-Blue-Dark &>/dev/null || :

%transfiletriggerpostun -- %{_datadir}/icons/%{tname}-Blue-Light
gtk-update-icon-cache --force %{_datadir}/icons/%{tname}-Blue-Light &>/dev/null || :

%transfiletriggerpostun -- %{_datadir}/icons/%{tname}-Green
gtk-update-icon-cache --force %{_datadir}/icons/%{tname}-Green &>/dev/null || :

%transfiletriggerpostun -- %{_datadir}/icons/%{tname}-Green-Dark
gtk-update-icon-cache --force %{_datadir}/icons/%{tname}-Green-Dark &>/dev/null || :

%transfiletriggerpostun -- %{_datadir}/icons/%{tname}-Red
gtk-update-icon-cache --force %{_datadir}/icons/%{tname}-Red &>/dev/null || :

%transfiletriggerpostun -- %{_datadir}/icons/%{tname}-Red-Dark
gtk-update-icon-cache --force %{_datadir}/icons/%{tname}-Red-Dark &>/dev/null || :

%transfiletriggerpostun -- %{_datadir}/icons/%{tname}-Red-Light
gtk-update-icon-cache --force %{_datadir}/icons/%{tname}-Red-Light &>/dev/null || :

%transfiletriggerpostun -- %{_datadir}/icons/%{tname}-Yellow
gtk-update-icon-cache --force %{_datadir}/icons/%{tname}-Yellow &>/dev/null || :

%transfiletriggerpostun -- %{_datadir}/icons/%{tname}-Yellow-Dark
gtk-update-icon-cache --force %{_datadir}/icons/%{tname}-Yellow-Dark &>/dev/null || :

%transfiletriggerpostun -- %{_datadir}/icons/%{tname}-Yellow-Light
gtk-update-icon-cache --force %{_datadir}/icons/%{tname}-Yellow-Light &>/dev/null || :


%files
%license LICENSE
%doc README.md AUTHORS
%dir %{_datadir}/icons/%{tname}-*/
%{_datadir}/icons/%{tname}-*/{actions/,animations/,apps/,categories/,devices/,emblems/,emotes/,mimetypes/,panel/,places/,status/,index.theme}
%ghost %{_datadir}/icons/%{tname}-*/icon-theme.cache


%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.20200710-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 23 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.0.20200710-1
- Update to 20200710

* Mon May 25 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.0.20200511-1
- Update to 20200511

* Fri Mar 27 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.0.20200116-1
- Update to 20200116

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.20191223-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 03 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.0.20191223-1
- Update to 20191223

* Fri Sep 13 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.0.20190908-3
- Update to 20190908
- Add recommended optional packages for complete theme

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.20190413-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Apr 21 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.0.20190413-1
- Initial package

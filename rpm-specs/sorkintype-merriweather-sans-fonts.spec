# SPDX-License-Identifier: MIT
%global forgeurl    https://github.com/SorkinType/Merriweather-Sans
%global commit      f36d6e1eb17fd4eead50c320fc8313f5353c9f5f
%forgemeta

Version: 1.008
Release: 3%{?dist}
URL:     %{forgeurl}

%global foundry           SorkinType
%global fontlicense       OFL
%global fontlicenses      OFL.txt
%global fontdocs          *txt *md
%global fontdocsex        %{fontlicenses}

%global fontfamily        Merriweather Sans
%global fontsummary       Merriweather Sans, a low-contrast semi-condensed sans-serif font family
%global fonts             fonts/ttfs/*ttf fonts/variable/*.ttf
%global fontconfngs       %{SOURCE10}
%global fontdescription   %{expand:
Merriweather Sans is a low-contrast semi-condensed sans-serif font family
designed to be readable at very small sizes. Merriweather Sans is traditional
in feeling despite the modern shapes it has adopted for screens. It is a
companion to the serif font family Merriweather.}

Source0:  %{forgesource}
Source10: 57-%{fontpkgname}.xml

%fontpkg

%prep
%forgesetup

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.008-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Feb 22 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 1.008-2
✅ Rebuild with fonts-rpm-macros 2.0.2

* Sat Feb 15 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 1.008-1.20191208gitf36d6e1
✅ Initial packaging

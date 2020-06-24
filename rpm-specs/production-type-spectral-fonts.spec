# SPDX-License-Identifier: MIT
%global forgeurl    https://github.com/productiontype/Spectral
%global commit      748733e3761fc7985ca9c473996ed121954debf8
%forgemeta

Version: 2.003
Release: 2%{?dist}
URL:     %{forgeurl}

%global foundry           Production Type
%global fontlicense       OFL
%global fontlicenses      OFL.txt
%global fontdocs          *txt *md
%global fontdocsex        %{fontlicenses}

%global fontfamily        Spectral
%global fontsummary       Spectral, an efficient and versatile serif font family
%global fonts             fonts/desktop_otf/*otf
%global fontconfngs       %{SOURCE10}
%global fontdescription   %{expand:
Spectral is a versatile serif font family available in seven weights of roman
and italic, with small caps. Spectral offers an efficient, beautiful design
that’s intended primarily for text-rich, screen-first environments and
long-form reading.}

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
* Sat Feb 22 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 2.003-2
✅ Rebuild with fonts-rpm-macros 2.0.2

* Sat Feb 15 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 2.003-1.1.20191208git748733e
✅ Initial packaging

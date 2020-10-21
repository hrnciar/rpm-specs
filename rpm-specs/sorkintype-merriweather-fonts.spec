# SPDX-License-Identifier: MIT
%global forgeurl    https://github.com/SorkinType/Merriweather
%global commit      fad21f97f3525af393d7a1d6c2995cbaf4b0cd7b
%forgemeta

Version: 2.008
Release: 3%{?dist}
URL:     %{forgeurl}

%global foundry           SorkinType
%global fontlicense       OFL
%global fontlicenses      OFL.txt
%global fontdocs          *txt *md
%global fontdocsex        %{fontlicenses}

%global fontfamily        Merriweather
%global fontsummary       Merriweather, a warm space-saving serif font family
%global fonts             fonts/ttfs/*ttf fonts/variable/*ttf
%global fontsex           fonts/variable/*WO7*ttf fonts/ttfs/Merriweather35*ttf
%global fontconfngs       %{SOURCE10}
%global fontdescription   %{expand:
Merriweather offers a Renaissance warmth while using proportions which are
space-saving. It is suitable for editorial design, news and other kinds of
space sensitive typography.

Merriweather was designed to be a text face that is pleasant to read on
screens. It features a very large x height, slightly condensed letter-forms, a
mild diagonal stress, sturdy serifs and open forms}

Source0:  %{forgesource}
Source10: 57-%{fontpkgname}.xml

%fontpkg

%package   doc
Summary:   Optional documentation files of %{name}
BuildArch: noarch
%description doc
This package provides optional documentation files shipped with
%{name}.

%prep
%forgesetup

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%files doc
%defattr(644, root, root, 0755)
%license OFL.txt
%doc documents/*

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.008-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Feb 22 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 2.008-2
✅ Rebuild with fonts-rpm-macros 2.0.2

* Sat Feb 15 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 2.008-1.0.20200111gitfad21f9
✅ Initial packaging

# SPDX-License-Identifier: MIT
%global forgeurl    https://github.com/ossobuffo/jura
%global commit      6e2614af65721fe74167b1f74b90e7bf5c0d0260
%forgemeta

Version: 5.103
Release: 4%{?dist}
URL:     %{forgeurl}

%global foundry           ossobuffo
%global fontlicense       OFL
%global fontlicenses      OFL.txt
%global fontdocs          *txt *html *md
%global fontdocsex        %{fontlicenses}

%global fontfamily        Jura
%global fontsummary       Jura, a sans-serif font family in the Eurostile vein
%global fonts             fonts/otf/*otf
%global fontconfngs       %{SOURCE10}
%global fontdescription   %{expand:
Jura is a sans-serif font family in the Eurostile vein.}

Source0:  %{forgesource}
Source10: 60-%{fontpkgname}.xml

%fontpkg

%package   doc
Summary:   Optional documentation files of %{name}
BuildArch: noarch
%description doc
This package provides optional documentation files shipped with
%{name}.

%prep
%forgesetup
%linuxtext %{fontdocs} %{fontlicenses}
chmod 644 %{fontdocs} %{fontlicenses}

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
%doc documentation/*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.103-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Feb 22 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 5.103-3
✅ Rebuild with fonts-rpm-macros 2.0.2

* Sat Feb 15 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 5.103-1.20191208git6d8a4e1
✅ Initial packaging

# SPDX-License-Identifier: MIT
%global forgeurl  https://github.com/googlefonts/literata/
%global tag       %{version}
%forgemeta

Version: 2.200

Release: 2%{?dist}
URL:     %{forgeurl}

%global foundry           TypeTogether
%global fontlicense       OFL
%global fontlicenses      OFL.txt
%global fontdocs          *txt *html *md
%global fontdocsex        %{fontlicenses}

%global fontfamily        Literata
%global fontsummary       Literata, a contemporary serif font family for long-form reading
%global fonts             *ttf
%global fontconfngs       %{SOURCE10}
%global fontdescription   %{expand:
Literata is one of the most distinct free font families for digital books. It
was commissioned as the default font family for all Google Play Books in 2014,
balancing a brand-able look with the strict needs of a comfortable reading
experience on a wide range of devices with varying screen resolutions and
rendering technologies — not an easy task.

TypeTogether solved these problems by designing a familiar roman style (varied
texture, slanted stress, and less mechanic structure) paired with an uncommon
upright italic that accounts for the inherent limitations of the square pixel
grid.

It was released under the SIL Open Font License in January 2019.}

Source0:  %{forgesource}
Source1:  %{forgeurl}/releases/download/%{version}/%{fontfamily}-v%{version}.zip
Source10: 57-%{fontpkgname}.xml

%fontpkg

%prep
%forgesetup
unzip -j -q  %{SOURCE1}

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
* Sat Feb 22 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 2.200-2
✅ Rebuild with fonts-rpm-macros 2.0.2

* Sat Feb 15 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 2.200-1
✅ Initial packaging

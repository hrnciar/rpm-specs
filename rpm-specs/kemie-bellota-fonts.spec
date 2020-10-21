# SPDX-License-Identifier: MIT
%global forgeurl    https://github.com/kemie/Bellota-Font/
Version:            4.1
%forgemeta

Release: 5%{?dist}
URL:     %{forgeurl}

%global foundry           kemie
%global fontlicense       OFL
%global fontlicenses      OFL.txt
%global fontdocs          *txt *TXT *md
%global fontdocsex        %{fontlicenses}

%global common_description %{expand:
The Bellota font families are ornamented, low contrast sans-serifs with text
and swash alternates. They’re just cute enough! They include stylistic
alternates (for swash and non-ornamented characters) and ligatures available
through OpenType features.}

%global fontfamily0       Bellota
%global fontsummary0      An ornamented, cute, low contrast sans-serif font family
%global fonts0            ttf/*ttf
%global fontsex0          %{fonts1}
%global fontconfngs0      %{SOURCE10}
%global fontdescription0  %{expand:
%{common_description}

Bellota, is the most exuberant variation published by the project.}

%global fontfamily1       Bellota Text
%global fontsummary1      An ornamented, slightly demure, cute, low contrast sans-serif font family
%global fontpkgheader1    %{expand:
Suggests: font(bellota)
}
%global fonts1            ttf/BellotaText*ttf
%global fontconfngs1      %{SOURCE11}
%global fontdescription1  %{expand:
%{common_description}

Bellota Text is slightly more demure than Bellota itself.}

%fontmeta

%global source_files %{expand:
Source0:  %{forgesource}
Source10: 60-%{fontpkgname0}.xml
Source11: 60-%{fontpkgname1}.xml
}

%fontpkg

%fontmetapkg

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
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 27 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 4.1-4
🐞 Workaround Fedora problems created by rpm commit 93604e2

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 4.1-3
💥 Actually rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are
  valid

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 4.1-2
👻 Rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are valid

* Thu Mar 26 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 4.1-1
✅ Initial packaging

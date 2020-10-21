# SPDX-License-Identifier: MIT
%global forgeurl    https://github.com/uswds/public-sans/
Version:            1.008
%forgemeta

Release: 7%{?dist}
URL:     https://public-sans.digital.gov/

%global foundry           USWDS
%global fontlicense       OFL
%global fontlicenses      LICENSE.md
%global fontdocs          *txt *md
%global fontdocsex        %{fontlicenses}

%global fontfamily        Public Sans
%global fontsummary       A strong, neutral, principles-driven, sans-serif Latin font family
%global fonts             binaries/otf/*otf binaries/variable/*ttf
%global fontconfngs       %{SOURCE10}
%global fontdescription   %{expand:
Public Sans is a fork of the Libre Franklin font family. Libre Franklin is a
reinterpretation and expansion of the 1912 Morris Fuller Benton’s classic.
Public Sans has many similarities with its parent, but diverges enough in its
particulars that its effect is distinct.

Overall, Public Sans differs from Libre Franklin in its focus on long form
reading and neutral UI applicability. It takes inspiration from geometric sans
faces of the 20th century, as well as the original Franklins of the 19th,
resulting in something of a mongrel face that retains its American origin.

Public Sans is designed to work well with Apple and Google system fonts as the
base in its font stack. It’s designed to have metrics most similar to SF Pro
Text (the Apple system font) and to fall somewhere between SF Pro Text and
Roboto (the Google system font) in its overall size and appearance.}

%fontmeta

%global source_files %{expand:
Source0:  %{forgesource}
Source10: 58-%{fontpkgname}.xml
}

%fontpkg

%prep
%forgesetup
chmod 644 %{fontdocs} %{fontlicenses}

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 27 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 1.008-6
🐞 Workaround Fedora problems created by rpm commit 93604e2

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 1.008-5
💥 Actually rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are
  valid

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 1.008-4
👻 Rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are valid

* Sat Feb 22 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 1.008-3
✅ Rebuild with fonts-rpm-macros 2.0.2

* Sat Feb 15 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 1.008-1
✅ Initial packaging

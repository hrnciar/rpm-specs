# SPDX-License-Identifier: MIT
%global forgeurl    https://github.com/huertatipografica/Alegreya-Sans
Version: 2.008
%forgemeta

Release: 8%{?dist}
URL:     https://www.huertatipografica.com/en/fonts/alegreya-sans-ht

%global foundry           HT
%global fontlicense       OFL
%global fontlicenses      OFL.txt
%global fontdocs          *txt *md
%global fontdocsex        %{fontlicenses}

%global fontfamily        Alegreya Sans
%global fontsummary       Alegreya Sans, a humanist sans serif font family with a calligraphic feeling
%global fonts             fonts/otf/*otf
%global fontsex           fonts/otf/*SC*otf
%global fontconfngs       %{SOURCE10}
%global fontdescription   %{expand:
Alegreya Sans is a humanist sans serif font family with a calligraphic feeling
that conveys a dynamic and varied rhythm. This gives a pleasant feeling to
readers of long texts.

The family follows humanist proportions and principles, just like the serif
version of the family, Alegreya. It achieves a playful and harmonious paragraph
through elements carefully designed in an atmosphere of diversity.}

%fontmeta

%global source_files %{expand:
Source0:  %{forgesource}
Source10: 58-%{fontpkgname}.xml
}

%fontpkg

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

%changelog
* Mon Apr 27 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 7.100-6
🐞 Workaround Fedora problems created by rpm commit 93604e2

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 2.008-7
💥 Actually rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are
  valid

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 2.008-6
👻 Rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are valid

* Mon Mar 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 2.008-5
✅ Lint, lint, lint and lint again

* Thu Feb 27 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 2.008-4
✅ Fix license processing

* Sat Feb 22 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 2.008-3
✅ Rebuild with fonts-rpm-macros 2.0.2

* Sat Feb 15 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 2.008-1
✅ Initial packaging

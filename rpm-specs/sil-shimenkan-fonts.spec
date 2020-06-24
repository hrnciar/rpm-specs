# SPDX-License-Identifier: MIT
Version: 1.000
Release: 6%{?dist}

%global foundry           SIL
%global fontlicense       OFL
%global fontlicenses      OFL.txt
%global fontdocs          *.txt
%global fontdocsex        %{fontlicenses}

%global fontfamily        Shimenkan
%global fontsummary       Shimenkan, a Miao (Pollard) script font family
%global projectname       %{lua:t=string.gsub(rpm.expand("%{fontfamily}"), " SIL$", ""); t=string.gsub(t, "[%p%s]+", ""); print(string.lower(t))}
%global archivename       %{lua:t=string.gsub(rpm.expand("%{fontfamily}"), "[%p%s]+", ""); print(t)}-%{version}
URL:                      https://software.sil.org/%{projectname}/
%global fontpkgheader     %{expand:
Recommends: font(sourcesanspro)
}
%global fonts             *.ttf
%global fontconfngs       %{SOURCE10}
%global fontdescription   %{expand:
The Shimenkan font family supports the broad variety of writing systems that
use the Miao (Pollard) script. It leverages OpenType features to provide the
correct alternates and positioning for each language. Therefore, making use of
this font requires good OpenType support in applications.

The Latin glyphs are based on the OFL-licensed Source Sans Pro fonts. The Miao
glyphs are designed to harmonize with the Latin, but remain true to the unique
characteristics of Miao writing systems. The project is inspired by, but not
based on, the Miao Unicode project.

Languages that use the Miao script have different positioning and glyphs
shaping conventions. Accessing the correct alternates and positioning for a
given language requires application support for the corresponding OpenType
feature.}

%fontmeta

%global source_files %{expand:
Source0:  https://github.com/silnrsi/font-%{projectname}/releases/download/v%{version}/%{archivename}.tar.xz
Source10: 65-%{fontpkgname}.xml
}

%fontpkg

%prep
%setup -q -n %{archivename}
%linuxtext *.txt

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
* Mon Apr 27 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 1.000-6
🐞 Workaround Fedora problems created by rpm commit 93604e2

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 1.000-5
💥 Actually rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are
  valid

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 1.000-4
👻 Rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are valid

* Sat Feb 22 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 1.000-3
✅ Rebuild with fonts-rpm-macros 2.0.2

* Sat Feb 15 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 1.000-1
✅ Initial packaging

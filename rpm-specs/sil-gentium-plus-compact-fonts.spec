# SPDX-License-Identifier: MIT
Version: 5.000
Release: 6%{?dist}

%global foundry           SIL
%global fontlicense       OFL
%global fontlicenses      OFL.txt
%global fontdocs          *.txt documentation/*.txt documentation/*.odt
%global fontdocsex        %{fontlicenses}

%global fontfamily        Gentium Plus Compact
%global fontsummary       Gentium Plus Compact, a Latin/Greek/Cyrillic font family
%global projectname       gentium
%global archivename       %{lua:t=string.gsub(rpm.expand("%{fontfamily}"), "[%p%s]+", ""); print(t)}-%{version}
URL:                      https://software.sil.org/%{projectname}/
%global fontpkgheader     %{expand:
Suggests: font(gentium)
}
%global fonts             *.ttf
%global fontconfngs       %{SOURCE10}
%global fontdescription   %{expand:
Gentium is a font family designed to enable the diverse ethnic groups around
the world who use the Latin, Cyrillic and Greek scripts to produce readable,
high-quality publications.

Gentium was a winner of the TDC2003 Type Design Competition and was exhibited
as part of the bukva:raz! exhibit at the UN Headquarters Main Lobby, 17 Jan –
13 Feb, 2002.

The Gentium Plus Compact font family was derived from Gentium Plus using SIL
TypeTuner, by setting the “Line spacing” feature to “Tight”, and it cannot be
TypeTuned again. It may exhibit some diacritics clipping on screen (but should
print fine).}

%fontmeta

%global source_files %{expand:
Source0:  https://software.sil.org/downloads/r/%{projectname}/%{archivename}.zip
Source10: 61-%{fontpkgname}.xml
}

%fontpkg

%prep
%setup -q -n %{archivename}
%linuxtext *.txt documentation/*.txt

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
* Mon Apr 27 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 5.000-6
🐞 Workaround Fedora problems created by rpm commit 93604e2

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 5.000-5
💥 Actually rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are
  valid

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 5.000-4
👻 Rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are valid

* Sat Feb 22 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 5.000-3
✅ Rebuild with fonts-rpm-macros 2.0.2

* Sat Feb 15 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 5.000-1
✅ Initial packaging

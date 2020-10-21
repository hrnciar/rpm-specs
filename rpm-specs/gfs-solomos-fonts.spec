# SPDX-License-Identifier: MIT
Version: 20071114
Release: 34%{?dist}
URL:     http://www.greekfontsociety-gfs.gr/typefaces/19th_century

%global foundry           GFS
%global fontlicense       OFL
%global fontlicenses      OFL.txt
%global fontdocs          *.txt
%global fontdocsex        %{fontlicenses}

%global fontfamily        Solomos
%global fontsummary       GFS Solomos, a 19th century italic Greek font family
%global fonts             *.otf
%global fontconfngs       %{SOURCE10}
%global fontdescription   %{expand:
From the middle of the 19th century an italic font with many calligraphic
overtones was introduced into Greek printing. Its source is unknown, but it
almost certainly was the product of a German or Italian foundry. In the first
type specimen printed in Greece by the type cutter K. Miliadis (1850), the font
was listed anonymously along others of 11pts and in the Gr. Doumas’ undated
specimen appeared as “11pt Greek inclined”. For most of the second half of the
century the type was used extensively as an italic for emphasis in words,
sentences or excerpts. In 1889, the folio size Type Specimen of Anestis
Konstantinidis’ publishing, printing and type founding establishment also
included the type as “Greek inclined [9 & 12 pt]”.

Nevertheless, the excessively calligraphic style of the characters, combined
with the steep and uncomfortable obliqueness of the capitals, was out of
favor in the 20th century and the type did not survive the conformity of the
mechanical type cutting and casting.

The font has been digitally revived, as part of our typographic tradition, by
George D. Matthiopoulos and is part of GFS’ type library under the name GFS
Solomos, in commemoration of the great Greek poet of the 19th century,
Dionisios Solomos.}

%global archivename %{lua:t=string.gsub(rpm.expand("%{foundry} %{fontfamily}"), "[%p%s]+", "_");print(t)}

%fontmeta

%global source_files %{expand:
Source0:  http://www.greekfontsociety-gfs.gr/_assets/fonts/%{archivename}.zip
Source10: 61-%{fontpkgname}.xml
}

%fontpkg

%new_package doc
Summary:   Optional documentation files of %{source_name}
BuildArch: noarch
%description doc
This package provides optional documentation files shipped with
%{source_name}.

%prep
%setup -q -c -T
unzip -j -q  %{SOURCE0}
%linuxtext *.txt

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
%doc *.pdf

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 27 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 20071114-33
🐞 Workaround Fedora problems created by rpm commit 93604e2

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 20071114-32
💥 Actually rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are
  valid

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 20071114-31
👻 Rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are valid

* Mon Mar 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 20071114-30
✅ Lint, lint, lint and lint again

* Sat Feb 22 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 20071114-29
✅ Rebuild with fonts-rpm-macros 2.0.2

* Sat Feb 15 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 20071114-28
✅ Convert to fonts-rpm-macros use

* Sun Nov 25 2007 Nicolas Mailhot <nim@fedoraproject.org>
- 20071114-1
✅ Initial packaging

# SPDX-License-Identifier: MIT
Version: 20090902
Release: 23%{?dist}
URL:     http://www.greekfontsociety-gfs.gr/typefaces/19th_century

%global foundry           GFS
%global fontlicense       OFL
%global fontlicenses      OFL.txt
%global fontdocs          *.txt
%global fontdocsex        %{fontlicenses}

%global fontfamily        Philostratos
%global fontsummary       GFS Philostratos, a 19th century Greek revival of Griechische Antiqua
%global fonts             *.otf
%global fontconfngs       %{SOURCE10}
%global fontdescription   %{expand:
Griechische Antiqua was one of the historical Greek typefaces of the late 19th
and early 20th century. It was designed by Μaurice Εduard Pinder, a German
erudite artist and a member of the Academy of Science in Berlin. This is the
most popular version which has appeared from 1870 to 1940 in the German
speaking philological literature and in many classical and Byzantine editions
by publishers like Teubner (in Leipzig) and Weidmann (in Berlin) such as:
Anthology of Byzantine Melos by Wilhelm von Christ and Matthaios
Paranikas (Leipzig 1871), Epicurea, by Heinrich Usener (Leipzig 1887),
Mitrodorous by Alfred Koerte (Leipzig 1890), Pindar by Otto Schroeder (Leipzig
1908), του Aeschylus by U. von Wilamowitz-Moellendorff (Berlin 1910, 1915),
Bachylides by Bruno Snell (Leipzig, 1934),  The Vulgata by Alfred Rahlfs
(Stuttgart 1935), Suidas Lexicon by Ada Adler (Leipzig 1928-1938) etc.

E.J. Kenney lamented the abandonment of the type after the 2nd World War as a
great loss for Greek typography (“From Script to Print”, Greek Scripts: An
illustrated Introduction, Society for the Promotion of Hellenic Studies, 2001,
p. 69).

GFS Philostratos was digitized by George D. Matthiopoulos.}

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
* Mon Apr 27 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 20090902-23
🐞 Workaround Fedora problems created by rpm commit 93604e2

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 20090902-22
💥 Actually rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are
  valid

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 20090902-21
👻 Rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are valid

* Mon Mar 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 20090902-20
✅ Lint, lint, lint and lint again

* Sat Feb 22 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 20090902-19
✅ Rebuild with fonts-rpm-macros 2.0.2

* Sat Feb 15 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 20090902-18
✅ Convert to fonts-rpm-macros use

* Sun Sep  6 2009 Nicolas Mailhot <nim@fedoraproject.org>
- 20090902-1
✅ Initial packaging

# SPDX-License-Identifier: MIT
Version: 20090918
Release: 24%{?dist}
URL:     http://www.greekfontsociety-gfs.gr/typefaces/20th_21st_century

%global foundry           GFS
%global fontlicense       OFL
%global fontlicenses      OFL.txt
%global fontdocs          *.txt
%global fontdocsex        %{fontlicenses}

%global fontfamily        NeoHellenic
%global fontsummary       GFS NeoHellenic, a 20th century round Greek font family
%global fonts             *.otf
%global fontconfngs       %{SOURCE10}
%global fontdescription   %{expand:
The design of new Greek typefaces always followed the growing needs of the
Classical Studies in the major European Universities. Furthermore, by the end
of the 19th century bibliology had become an established section of Historical
Studies, and, as John Bowman commented, the prevailing attitude was that Greek
types should adhere to a lost idealized, yet undefined, Greekness of yore.
Especially in Great Britain this tendency remained unchallenged in the first
decades of the 20th century, both by Richard Proctor, curator of the incunabula
section in the British Museum Library and his successor Victor Scholderer.

In 1927, Scholderer, on behalf of the Society for the Promotion of Greek
Studies, got involved in choosing and consulting the design and production of a
Greek type called New Hellenic cut by the Lanston Monotype Corporation. He
chose the revival of a round, and almost mono-line type which had first appeared
in 1492 in the edition of Macrobius, ascribable to the printing shop of
Giovanni Rosso (Joannes Rubeus) in Venice. New Hellenic was the only successful
typeface in Great Britain after the introduction of Porson Greek well over a
century before. The type, since to 1930’s, was also well received in Greece,
albeit with a different design for Ksi and Omega.

GFS digitized the typeface (1993-1994) funded by the Athens Archeological
Society with the addition of a new set of epigraphical symbols. Later (2000)
more weights were added (italic, bold and bold italic) as well as a Latin
version.}

%global archivename %{lua:t=string.gsub(rpm.expand("%{foundry} %{fontfamily}"), "[%p%s]+", "_");print(t)}

%fontmeta

%global source_files %{expand:
Source0:  http://www.greekfontsociety-gfs.gr/_assets/fonts/%{archivename}.zip
Source10: 60-%{fontpkgname}.xml
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
- 20090918-23
🐞 Workaround Fedora problems created by rpm commit 93604e2

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 20090918-22
💥 Actually rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are
  valid

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 20090918-21
👻 Rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are valid

* Mon Mar 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 20090918-20
✅ Lint, lint, lint and lint again

* Sat Feb 22 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 20090918-19
✅ Rebuild with fonts-rpm-macros 2.0.2

* Sat Feb 15 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 20090918-18
✅ Convert to fonts-rpm-macros use

* Sun Nov 25 2007 Nicolas Mailhot <nim@fedoraproject.org>
- 20070415-1
✅ Initial packaging

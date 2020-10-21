# SPDX-License-Identifier: MIT
Version: 20070415
Release: 38%{?dist}
URL:     http://www.greekfontsociety-gfs.gr/typefaces/20th_21st_century

%global foundry           GFS
%global fontlicense       OFL
%global fontlicenses      OFL.txt
%global fontdocs          *.txt
%global fontdocsex        %{fontlicenses}

%global fontfamily        Theokritos
%global fontsummary       GFS Theokritos, a 20th century decorative Greek font family
%global fonts             *.otf
%global fontconfngs       %{SOURCE10}
%global fontdescription   %{expand:
Yannis Kefallinos (1894–1958) was one of the most innovative engravers of his
generation and the first who researched methodically the aesthetics of book and
typographic design in Greece. He taught at the Fine Arts School of Athens and
established the first book design workshop from which many practicing artists
of the 60’s and 70’s had graduated.

In the late 50’s Kefallinos designed and published an exquisite book with
engraved illustrations of the ancient white funerary pottery in Attica in
collaboration with Varlamos, Montesanto, Damianakis. For the text of
Kefallinos’ Δέκα λευκαί λήκυθοι (1956) the artist used a typeface which he
himself had designed a few years before for an unrealized edition of
Theocritos’ Idyls. Its complex and heavily decorative design does point to
aesthetic codes which preoccupied his artistic expression and, although
impractical for contemporary text setting, it remains an original display
face, or it can be used as initials.

The book design workshop of the Fine Arts School of Athens has been recently
reorganized, under the direction of professor Leoni Vidali, and with her
collaboration George D. Matthiopoulos has redesigned digitally this historical
font which is now available as GFS Theokritos.}

%global archivename %{lua:t=string.gsub(rpm.expand("%{foundry} %{fontfamily}"), "[%p%s]+", "_");print(t)}

%fontmeta

%global source_files %{expand:
Source0:  http://www.greekfontsociety-gfs.gr/_assets/fonts/%{archivename}.zip
Source10: 65-%{fontpkgname}.xml
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
- 20070415-37
🐞 Workaround Fedora problems created by rpm commit 93604e2

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 20070415-36
💥 Actually rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are
  valid

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 20070415-35
👻 Rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are valid

* Mon Mar 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 20070415-34
✅ Lint, lint, lint and lint again

* Sat Feb 22 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 20070415-33
✅ Rebuild with fonts-rpm-macros 2.0.2

* Sat Feb 15 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 20070415-32
✅ Convert to fonts-rpm-macros use

* Sun Nov 25 2007 Nicolas Mailhot <nim@fedoraproject.org>
- 20070415-1
✅ Initial packaging

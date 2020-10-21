# SPDX-License-Identifier: MIT
Version: 20180227
Release: 6%{?dist}
URL:     https://www.greekfontsociety-gfs.gr/typefaces/Math

%global foundry           GFS
%global fontlicense       OFL
# GFS already forgot about providing clean licensing texts
%global fontlicenses      README
%global fontdocs          README

%global fontfamily        NeoHellenic Math
%global fontsummary       GFS NeoHellenic Math, an almost Sans Serif Math font family
%global fontpkgheader     %{expand:
Requires:    gfs-neohellenic-fonts
Supplements: gfs-neohellenic-fonts
}
%global fonts             *.otf
%global fontconfngs       %{SOURCE10}
%global fontdescription   %{expand:
GFS NeoHellenic Math is an almost Sans Serif font family. One of its main uses
is for presentations, an area where (we believe) a commercial grade sans math
font was not available up to now.

The font family contains an extended glyph set including more than the standard
math symbols such as vertically extended integrals, chess symbols, etc.

It was commissioned to the Greek Font Society (GFS) by the Graduate Studies
program “Studies in Mathematics” of the Department of Mathematics of the
University of the Aegean, located on the Samos island, Greece.

The design copyright belongs to the main designer of GFS, George Matthiopoulos.
The OpenType Math Table embedded in the font was developed by the Mathematics
Professor Antonis Tsolomitis.}

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
%linuxtext README

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%files doc
%defattr(644, root, root, 0755)
%license README
%doc *.pdf *.sty

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 27 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 20180227-5
🐞 Workaround Fedora problems created by rpm commit 93604e2

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 20180227-4
💥 Actually rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are
  valid

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 20180227-3
👻 Rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are valid

* Sat Feb 22 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 20180227-2
✅ Rebuild with fonts-rpm-macros 2.0.2

* Sat Feb 15 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 20180227-1
✅ Initial packaging

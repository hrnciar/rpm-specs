# SPDX-License-Identifier: MIT
Version: 20070415
Release: 35%{?dist}
URL:     http://www.greekfontsociety-gfs.gr/typefaces/18th_century

%global foundry           GFS
%global fontlicense       OFL
%global fontlicenses      OFL.txt
%global fontdocs          *.txt
%global fontdocsex        %{fontlicenses}

%global fontfamily        Bodoni Classic
%global fontsummary       GFS Bodoni Classic, an 18th century oblique Greek font family
%global fontpkgheader     %{expand:
Suggests: font(gfsbodoni)
}
%global fonts             *.otf
%global fontconfngs       %{SOURCE10}
%global fontdescription   %{expand:
Giambattista Bodoni was the most prolific Italian type cutter of the 18th
century. While he worked in the Vatican Press he was involved in the
type cutting of “exotic” languages for which catholic literature was printed.
When he established his own press in Parma he did publish many books of the
classics with his own Greek typefaces in the last quarter of the 18th century.
He was among the first European type cutters to move away from the byzantine
cursive tradition with the numerous ligatures which was the norm until then.
His Greek types influenced many subsequent designers, yet they fell in disuse
by the middle of the 19th century.

GFS presented Bodoni’s original Greek typeface in the commemorative edition of
Pindar’s Olympian Odes (2004), in digital version by George D. Matthiopoulos,
and is now available as free ware for the general public. In the OpenType
features, under ligatures, one may alternately use diphthongs with the accents
placed in between the characters, as Giambattista Bodoni did when setting
Greek texts.
}

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
- 20070415-34
🐞 Workaround Fedora problems created by rpm commit 93604e2

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 20070415-33
💥 Actually rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are
  valid

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 20070415-32
👻 Rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are valid

* Mon Mar 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 20070415-31
✅ Lint, lint, lint and lint again

* Sat Feb 22 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 20070415-30
✅ Rebuild with fonts-rpm-macros 2.0.2

* Sat Feb 15 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 20070415-29
✅ Convert to fonts-rpm-macros use

* Sun Nov 25 2007 Nicolas Mailhot <nim@fedoraproject.org>
- 20070415-1
✅ Initial packaging

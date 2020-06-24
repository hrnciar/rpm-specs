# SPDX-License-Identifier: MIT
Version: 2.000
Release: 5%{?dist}

%global foundry           SIL
%global fontlicense       OFL
%global fontlicenses      OFL.txt
%global fontdocs          *.txt documentation/*.txt documentation/*.odt
%global fontdocsex        %{fontlicenses}

%global fontfamily        Awami Nastaliq
%global fontsummary       Awami Nastaliq, a Nastaliq-style Arabic script font family
%global projectname       awami
%global archivename       %{lua:t=string.gsub(rpm.expand("%{fontfamily}"), "[%p%s]+", ""); print(t)}-%{version}
URL:                      https://software.sil.org/%{projectname}/
%global fontpkgheader     %{expand:
Recommends: font(charissil)
}
%global fonts             *.ttf
%global fontconfngs       %{SOURCE10}
%global fontdescription   %{expand:
Awami Nastaliq is a Nastaliq-style Arabic script font family supporting a wide
variety of languages of southwest Asia, including but not limited to Urdu. This
font is aimed at minority language support. This makes it unique among Nastaliq
fonts.

Nastaliq, based on a centuries-old calligraphic tradition, is considered one of
the most beautiful scripts on the planet. Nastaliq has been called “the bride
of calligraphy” but its complexity also makes it one of the most difficult
scripts to render using a computer font. Its right-to-left direction, vertical
nature, and context-specific shaping provide a challenge to any font rendering
engine and make it much more difficult to render than the flat (Naskh) Arabic
script that it is based on. As a result, font developers have long struggled to
produce a font with the correct shaping but at the same time avoid overlapping
of dots and diacritics. In order to account for the seemingly infinite
variations, the Graphite rendering engine has been extended just to handle
these complexities properly.}

%fontmeta

%global source_files %{expand:
Source0:  https://github.com/silnrsi/font-%{projectname}/releases/download/v%{version}/%{archivename}.tar.xz
Source10: 65-%{fontpkgname}.xml
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
- 2.000-5
🐞 Workaround Fedora problems created by rpm commit 93604e2

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 2.000-4
💥 Actually rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are
  valid

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 2.000-3
👻 Rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are valid

* Sat Feb 22 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 2.000-2
✅ Rebuild with fonts-rpm-macros 2.0.2

* Sat Feb 15 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 2.000-1
✅ Initial packaging

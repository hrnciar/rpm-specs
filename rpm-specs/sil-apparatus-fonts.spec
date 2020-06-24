# SPDX-License-Identifier: MIT
Version: 1.0
Release: 6%{?dist}

%global foundry           SIL
%global fontlicense       OFL
%global fontlicenses      OFL.txt
%global fontdocs          *.txt
%global fontdocsex        %{fontlicenses}

%global fontfamily        Apparatus SIL
%global fontsummary       Apparatus SIL, a font family for rendering Greek & Hebrew biblical texts
%global archivename       %{lua:t=string.gsub(rpm.expand("%{fontfamily}"), "[%p%s]+", "");print(t)}
%global projectname       %{archivename}
URL:                      https://scripts.sil.org/ApparatusSIL
%global fonts             *.ttf *.TTF
%global fontconfngs       %{SOURCE10}
%global fontdescription   %{expand:
The Apparatus SIL font family was designed to provide most of the symbols
needed to reproduce the textual apparatus found in major editions of Greek &
Hebrew biblical texts. It is based on SIL Charis, a font family designed for
optimum clarity and compactness when printed at small point sizes. This assures
that both Charis SIL and Apparatus SIL can be used together in documents with a
consistency of style.

Most lines of text in the apparatus can be reproduced by combining the Greek
and Hebrew fonts, transliteration (using a font such as Charis SIL), and the
Apparatus SIL font.}

%fontmeta

%global source_files %{expand:
Source0:  https://scripts.sil.org/cms/scripts/render_download.php?format=file&media_id=AppSIL%{version}.zip&filename=%{archivename}.zip#/%{archivename}.zip
Source10: 60-%{fontpkgname}.xml
}

%fontpkg

%prep
%setup -q -c -T
unzip -j -q %{SOURCE0}
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
- 1.0-6
🐞 Workaround Fedora problems created by rpm commit 93604e2

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 1.0-5
💥 Actually rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are
  valid

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 1.0-4
👻 Rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are valid

* Sun Feb 23 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 1.0-3
✅ Fix source URL

* Sat Feb 22 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 1.0-2
✅ Rebuild with fonts-rpm-macros 2.0.2

* Sat Feb 15 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 1.0-1
✅ Initial packaging

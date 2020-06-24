# SPDX-License-Identifier: MIT
%global forgeurl    https://github.com/googlefonts/GreatVibesFont
%global commit      a82e16d27e13b0d1337abeab05fdfd99a51d044c
%forgemeta

Version: 1.101
Release: 5%{?dist}
URL:     %{forgeurl}

%global foundry           TypeSETit
%global fontlicense       OFL
%global fontlicenses      OFL.txt
%global fontdocs          *.txt *.md
%global fontdocsex        %{fontlicenses}

%global fontfamily        Great Vibes
%global fontsummary       Great Vibes, a beautifully flowing cursive font family
%global fonts             fonts/*ttf
%global fontconfngs       %{SOURCE10}
%global fontdescription   %{expand:
Great Vibes is a beautifully flowing connecting cursive font family. It has
cleanly looping ascenders and descenders as well as elegant uppercase forms.}

%fontmeta

%global source_files %{expand:
Source0:  %{forgesource}
Source10: 57-%{fontpkgname}.xml
}

%fontpkg

%prep
%forgesetup

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
* Mon Apr 27 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 1.101-5.20200215gita82e16d
🐞 Workaround Fedora problems created by rpm commit 93604e2

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 1.101-4.20200215gita82e16d
💥 Actually rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are
  valid

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 1.101-3.20200215gita82e16d
👻 Rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are valid

* Sat Feb 22 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 1.101-2
✅ Rebuild with fonts-rpm-macros 2.0.2

* Sat Feb 15 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 1.101-1.20191208gita82e16d
✅ Initial packaging

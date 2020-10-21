# SPDX-License-Identifier: MIT
Version: 20200215
Release: 7%{?dist}
URL:     https://fonts.google.com/specimen/Patrick+Hand

%global foundry           Wagesreiter
%global fontlicense       OFL
%global fontlicenses      OFL.txt
%global fontdocs          *.pb *.html

%global fontfamily        Patrick Hand
%global fontsummary       Patrick Hand, an handwriting font family
%global fonts             *ttf
%global fontconfngs       %{SOURCE10}
%global fontdescription   %{expand:
Patrick Hand is a font family based on the designer’s own handwriting. It is
developed to bring an impressive and useful handwriting effect to your
texts.

It has all the basic Latin characters as well as most of the Latin extended
ones. It also includes some fancy glyphs like heavy quotation marks and the
floral heart! Ligatures, small caps and old style numbers are available as
OpenType features.}

%fontmeta

%global source_files %{expand:
Source0:  %{source_name}-%{version}.tar.xz
# Not available outside the huge Google fonts repository
Source1:  getfiles.sh
Source10: 60-%{fontpkgname}.xml
}

%fontpkg

%prep
%setup -q

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 27 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 20200215-6
🐞 Workaround Fedora problems created by rpm commit 93604e2

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 20200215-5
💥 Actually rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are
  valid

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 20200215-4
👻 Rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are valid

* Sat Feb 22 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 20200215-3
✅ Rebuild with fonts-rpm-macros 2.0.2

* Sat Feb 15 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 20191208-1
✅ Initial packaging

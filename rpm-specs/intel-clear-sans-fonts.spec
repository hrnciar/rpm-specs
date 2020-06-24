# SPDX-License-Identifier: MIT
Version: 1.00
Release: 7%{?dist}
%global  projectname clear-sans
URL:     https://01.org/%{projectname}

%global foundry           Intel
%global fontlicense       ASL 2.0
%global fontlicenses      LICENSE-2.0.txt

%global fontfamily        Clear Sans
%global fontsummary       Clear Sans, a versatile font family for screen, print, and Web
%global fonts             TTF/*.ttf
%global fontconfngs       %{SOURCE10}
%global fontdescription  %{expand:
Clear Sans has been recognized as a versatile font for screen, print, and Web.
Its minimized, unambiguous characters and slightly narrow proportions, make it
ideal for UI design.

Clear Sans was designed with on-screen legibility in mind. It strikes a balance
between contemporary, professional, and stylish expression and thoroughly
functional purpose. It has a sophisticated and elegant personality at all
sizes, and its thoughtful design becomes even more evident at the thin weight.}

%fontmeta

%global source_files %{expand:
Source0:  https://01.org/sites/default/files/downloads/%{projectname}/clearsans-%{version}.zip
Source10: 60-%{fontpkgname}.xml
}

%fontpkg

%prep
%setup -q -c

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
* Mon Apr 27 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 1.00-7
🐞 Workaround Fedora problems created by rpm commit 93604e2

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 1.00-6
💥 Actually rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are
  valid

* Sat Mar  7 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 1.00-3
✅ Initial packaging

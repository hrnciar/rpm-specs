# SPDX-License-Identifier: MIT
%global forgeurl    https://github.com/googlefonts/nunito
%global commit      6d8a4e1c00df8b361e59656eee7c2b458d663191
%forgemeta

Version: 3.504
Release: 8%{?dist}
URL:     %{forgeurl}

%global foundry           vernnobile
%global fontlicense       OFL
%global fontlicenses      OFL.txt
%global fontdocs          *txt *html *md
%global fontdocsex        %{fontlicenses}

%global fontfamily        Nunito
%global fontsummary       Nunito, a sans serif font family with rounded terminals
%global fonts             fonts/TTF-unhinted/*otf
%global fontconfngs       %{SOURCE10}
%global fontdescription   %{expand:
Nunito is a well balanced sans serif with rounded terminals. Nunito has been
designed mainly to be used as a display font but is usable as a text font too.
Nunito has been designed to be used freely across the internet by web browsers
on desktop computers, laptops and mobile devices.}

%fontmeta

%global source_files %{expand:
Source0:  %{forgesource}
Source10: 58-%{fontpkgname}.xml
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
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 27 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 3.504-7.20200215git6d8a4e1
🐞 Workaround Fedora problems created by rpm commit 93604e2

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 3.504-6.20200215git6d8a4e1
💥 Actually rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are
  valid

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 3.504-5.20200215git6d8a4e1
👻 Rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are valid

* Wed Mar 11 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 3.504-4
✅ Rebuild to workaround broken F31 build

* Thu Feb 27 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 3.504-3
✅ Fix license processing

* Sat Feb 22 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 3.504-2
✅ Rebuild with fonts-rpm-macros 2.0.2

* Sat Feb 15 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 3.504-1.20191208git6d8a4e1
✅ Initial packaging

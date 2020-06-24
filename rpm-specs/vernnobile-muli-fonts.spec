# SPDX-License-Identifier: MIT
%global forgeurl    https://github.com/googlefonts/MuliFont
%global commit      580b05e1f2ad319cd98a8de03fd2da7b36677954
%forgemeta

Version: 2.001
Release: 7%{?dist}
URL:     %{forgeurl}

%global foundry           vernnobile
%global fontlicense       OFL
%global fontlicenses      OFL.txt
%global fontdocs          *txt *md
%global fontdocsex        %{fontlicenses}

%global fontfamily        Muli
%global fontsummary       Muli, a minimalist sans serif font family
%global fonts             fonts/*ttf
%global fontconfngs       %{SOURCE10}
%global fontdescription   %{expand:
Muli is a minimalist sans serif font family, designed for both display and text
typography.}

%fontmeta

%global source_files %{expand:
Source0:  %{forgesource}
Source10: 60-%{fontpkgname}.xml
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
- 2.001-7.20200215git580b05e
🐞 Workaround Fedora problems created by rpm commit 93604e2

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 2.001-6.20200215git580b05e
💥 Actually rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are
  valid

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 2.001-5.20200215git580b05e
👻 Rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are valid

 Wed Mar 11 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 2.001-4
✅ Rebuild to workaround broken F31 build

* Thu Feb 27 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 2.001-3
✅ Fix license processing

* Sat Feb 22 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 2.001-2
✅ Rebuild with fonts-rpm-macros 2.0.2

* Sat Feb 15 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 2.001-1.20191208git580b05e
✅ Initial packaging

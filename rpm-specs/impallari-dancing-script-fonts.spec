# SPDX-License-Identifier: MIT
%global forgeurl    https://github.com/impallari/DancingScript
%global commit      f7f54bc1b8836601dae8696666bfacd306f77e34
%forgemeta

Version: 2.000
Release: 10%{?dist}
URL:     %{forgeurl}

%global foundry           Impallari
%global fontlicense       OFL
%global fontlicenses      OFL.txt
%global fontdocs          *.txt *.md *.html
%global fontdocsex        %{fontlicenses}

%global fontfamily        Dancing Script
%global fontsummary       Dancing Script, a friendly, informal and spontaneous cursive font family
%global fonts             fonts/otf/*otf
%global fontconfngs       %{SOURCE10}
%global fontdescription   %{expand:
Dancing Script is a lively casual script where the letters bounce and change
size slightly. Caps are big, and goes below the baseline.

Dancing Script references popular scripts typefaces from the 50’s. It relates
to Murray Hill (Emil Klumpp. 1956) in his weight distribution, and to Mistral
(Roger Excoffon. 1953) in his lively bouncing effect.

Use it when you want a friendly, informal and spontaneous look.}

%fontmeta

%global source_files %{expand:
Source0:  %{forgesource}
Source10: 57-%{fontpkgname}.xml
}

%fontpkg

%prep
%forgesetup
%linuxtext %{fontdocs}
chmod 644 %{fontdocs} %{fontlicenses}

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 27 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 2.000-9.20200215gitf7f54bc
🐞 Workaround Fedora problems created by rpm commit 93604e2

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 2.000-8.20200215gitf7f54bc
💥 Actually rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are
  valid

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 2.000-7.20200215gitf7f54bc
👻 Rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are valid

* Wed Mar 11 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 2.000-6
✅ Rebuild to workaround broken F31 build

* Mon Mar 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 2.000-5
✅ Lint, lint, lint and lint again

* Thu Feb 27 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 2.000-4
✅ Fix license processing

* Sat Feb 22 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 2.000-3
✅ Rebuild with fonts-rpm-macros 2.0.2

* Sat Feb 15 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 2.000-1.20191208gitf7f54bc
✅ Initial packaging

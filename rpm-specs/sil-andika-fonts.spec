# SPDX-License-Identifier: MIT
Version: 5.000
Release: 7%{?dist}

%global foundry           SIL
%global fontlicense       OFL
%global fontlicenses      OFL.txt
%global fontdocs          *.txt
%global fontdocsex        %{fontlicenses}

%global fontfamily        Andika
%global fontsummary       SIL Andika, a font family for literacy and beginning readers
%global projectname       %{lua:t=string.gsub(rpm.expand("%{fontfamily}"), " SIL$", ""); t=string.gsub(t, "[%p%s]+", ""); print(string.lower(t))}
%global archivename       %{lua:t=string.gsub(rpm.expand("%{fontfamily}"), "[%p%s]+", ""); print(t)}-%{version}
URL:                      https://software.sil.org/%{projectname}/
%global fontpkgheader     %{expand:
Suggests: font(andikanewbasic)
}
%global fonts             *.ttf
%global fontconfngs       %{SOURCE10}
%global fontdescription   %{expand:
Andika is a sans serif, Unicode-compliant font family designed especially for
literacy use, taking into account the needs of beginning readers. The focus is
on clear, easy-to-perceive letter-forms that will not be readily confused with
one another.

A sans serif font is preferred by some literacy personnel for teaching people
to read. Its forms are simpler and less cluttered than those of most serif
fonts. For years, literacy workers have had to make do with fonts that were
not really suitable for beginning readers and writers. In some cases, literacy
specialists have had to tediously assemble letters from a variety of fonts in
order to get all of the characters they need for their particular language
project, resulting in confusing and unattractive publications. Andika
addresses those issues.}

%fontmeta

%global source_files %{expand:
Source0:  https://software.sil.org/downloads/r/%{projectname}/%{archivename}.zip
Source10: 61-%{fontpkgname}.xml
}

%fontpkg

%prep
%setup -q -n %{archivename}
%linuxtext *.txt

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
- 5.000-6
🐞 Workaround Fedora problems created by rpm commit 93604e2

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 5.000-5
💥 Actually rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are
  valid

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 5.000-4
👻 Rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are valid

* Mon Mar 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 5.000-3
✅ Lint, lint, lint and lint again

* Sat Feb 22 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 5.000-2
✅ Rebuild with fonts-rpm-macros 2.0.2

* Sat Feb 15 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 5.000-1
✅ Convert to fonts-rpm-macros use

* Tue Jun 24 2008 Nicolas Mailhot <nim@fedoraproject.org>
- 1.0-1
✅ Initial packaging

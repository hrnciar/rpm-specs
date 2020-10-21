# SPDX-License-Identifier: MIT
Version: 1.004
Release: 7%{?dist}

%global foundry           SIL
%global fontlicense       OFL
%global fontlicenses      OFL.txt
%global fontdocs          *.txt
%global fontdocsex        %{fontlicenses}

%global fontfamily        Namdhinggo SIL
%global fontsummary       Namdhinggo SIL, a font family for the Limbu writing system of Nepal
%global projectname       %{lua:t=string.gsub(rpm.expand("%{fontfamily}"), " SIL$", ""); t=string.gsub(t, "[%p%s]+", ""); print(string.lower(t))}
%global archivename       %{lua:t=string.gsub(rpm.expand("%{fontfamily}"), "[%p%s]+", ""); print(t)}-%{version}
URL:                      https://software.sil.org/%{projectname}/
%global fonts             *.ttf
%global fontconfngs       %{SOURCE10}
%global fontdescription   %{expand:
Namdhinggo provides glyphs for all Limbu characters and some Latin.

The Limbu, or Kirat Sirijonga, script is used by around 400 000 people in Nepal
and India. This Unicode-encoded font has been designed to support literacy and
materials development in the Limbu language.

According to traditional histories the Limbu script was developed by King
Sirijonga in the 9th Century. It then fell out of use before being reintroduced
in the 18th century by Teongsi Sirijonga (1704-1741) whom many felt to be the
reincarnation of the first Sirijonga. The modern Sirijonga was apparently
martyred in 1741 for the sake of this script by lamas in Sikkim. The script was
named ‘Sirijonga’ in his honor by the Limbu scholar Iman Singh Chemjong.}

%fontmeta

%global source_files %{expand:
Source0:  https://software.sil.org/downloads/r/%{projectname}/%{archivename}.zip
Source10: 66-%{fontpkgname}.xml
}

%fontpkg

%prep
%setup -q -n NamdhinggoSIL
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
- 1.004-6
🐞 Workaround Fedora problems created by rpm commit 93604e2

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 1.004-5
💥 Actually rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are
  valid

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 1.004-4
👻 Rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are valid

* Sat Feb 22 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 1.004-3
✅ Rebuild with fonts-rpm-macros 2.0.2

* Sat Feb 15 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 1.004-1
✅ Initial packaging

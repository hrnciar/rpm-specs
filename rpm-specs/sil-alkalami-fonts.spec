# SPDX-License-Identifier: MIT
Version: 1.200
Release: 8%{?dist}

%global foundry           SIL
%global fontlicense       OFL
%global fontlicenses      OFL.txt
%global fontdocs          *.txt documentation/*.txt
%global fontdocsex        %{fontlicenses}

%global fontfamily        Alkalami
%global fontsummary       A font family for the Arabic scripts of the Kano region of Nigeria and Niger
%global projectname       %{lua:t=string.gsub(rpm.expand("%{fontfamily}"), " SIL$", ""); t=string.gsub(t, "[%p%s]+", ""); print(string.lower(t))}
%global archivename       %{lua:t=string.gsub(rpm.expand("%{fontfamily}"), "[%p%s]+", ""); print(t)}-%{version}
URL:                      https://software.sil.org/%{projectname}/
%global fonts             *.ttf
%global fontconfngs       %{SOURCE10}
%global fontdescription   %{expand:
Alkalami is a font family for Arabic-based writing systems in the Kano region
of Nigeria and in Niger. This style of writing African Ajami has sometimes been
called Sudani Kufi or Rubutun Kano.

Alkǎlami (pronounced al-KA-la-mi) is the local word for the Arabic “qalam”, a
type of sharpened stick used for writing on wooden boards in the Kano region of
Nigeria and in Niger, and what gives the style its distinct appearance. The
baseline stroke is very thick and solid. The ascenders and other vertical
strokes including the teeth are very narrow when compared to the baseline. A
generous line height is necessary to allow for deep swashes and descenders, and
the overall look of the page is a very black, solid rectangle. Diacritics are
much smaller in scale, with very little distance from the main letters.

The Alkalami font supports the characters known to be used by languages written
with the Kano style of Arabic script, but may not have the characters needed
for other languages.}

%fontmeta

%global source_files %{expand:
Source0:  https://github.com/silnrsi/font-%{projectname}/releases/download/v%{version}/%{archivename}.tar.xz
Source10: 66-%{fontpkgname}.xml
}

%fontpkg

%new_package doc
Summary:   Optional documentation files of %{source_name}
BuildArch: noarch
%description doc
This package provides optional documentation files shipped with
%{source_name}.

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

%files doc
%license OFL.txt
%doc documentation/*.pdf

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 27 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 1.200-7
🐞 Workaround Fedora problems created by rpm commit 93604e2

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 1.200-6
💥 Actually rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are
  valid

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 1.200-5
👻 Rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are valid

* Mon Mar 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 1.200-4
✅ Lint, lint, lint and lint again

* Sat Feb 22 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 1.200-3
✅ Rebuild with fonts-rpm-macros 2.0.2

* Sat Feb 15 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 1.200-1
✅ Initial packaging

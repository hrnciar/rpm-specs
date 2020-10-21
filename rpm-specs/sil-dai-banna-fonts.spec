# SPDX-License-Identifier: MIT
Version: 2.200
Release: 7%{?dist}

%global foundry           SIL
%global fontlicense       OFL
%global fontlicenses      OFL.txt
%global fontdocs          *.txt
%global fontdocsex        %{fontlicenses}

%global fontfamily        Dai Banna SIL
%global fontsummary       Dai Banna SIL, a font family for rendering New Tai Lue (Xishuangbanna Dai)
%global projectname       %{lua:t=string.gsub(rpm.expand("%{fontfamily}"), " SIL$", ""); t=string.gsub(t, "[%p%s]+", ""); print(string.lower(t))}
%global archivename       %{lua:t=string.gsub(rpm.expand("%{fontfamily}"), " SIL$", ""); t=string.gsub(t, "[%p%s]+", ""); print(t)}-%{version}
URL:                      https://software.sil.org/%{projectname}/
%global fonts             *.ttf
%global fontconfngs       %{SOURCE10}
%global fontdescription   %{expand:
Dai Banna includes a complete set of New Tai Lue (Xishuangbanna Dai)
consonants, vowels, tones, and digits, along with punctuation and other useful
symbols. A basic set of Latin glyphs, including Arabic numerals, is also
provided.

The New Tai Lue script is used by approximately 300 000 people who speak the
Xishuangbanna Dai language in Yunnan, China.  It is a simplification of the Tai
Tham (Old Tai Lue) script as used for this language for hundreds of years.

The Dai News Department of Xishuangbanna Daily provided valuable advice during
the development of this font family. Xishuangbanna Daily, established in 1957,
is the largest newspaper company in Yunnan, China that publishes in the New Tai
Lue script.}

%fontmeta

%global source_files %{expand:
Source0:  https://software.sil.org/downloads/r/%{projectname}/%{archivename}.zip
Source10: 65-%{fontpkgname}.xml
}

%fontpkg

%new_package doc
Summary:   Optional documentation files of %{source_name}
BuildArch: noarch
%description doc
This package provides optional documentation files shipped with
%{source_name}.

%prep
%setup -q -n dai-banna-%{version}
%linuxtext *.txt doc/*.txt

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%files doc
%defattr(644, root, root, 0755)
%license OFL.txt
%doc doc/*.pdf doc/*.txt

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 27 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 2.200-6
🐞 Workaround Fedora problems created by rpm commit 93604e2

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 2.200-5
💥 Actually rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are
  valid

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 2.200-4
👻 Rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are valid

* Sat Feb 22 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 2.200-3
✅ Rebuild with fonts-rpm-macros 2.0.2

* Sat Feb 15 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 2.200-1
✅ Initial packaging

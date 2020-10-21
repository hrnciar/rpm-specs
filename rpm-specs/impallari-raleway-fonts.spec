# SPDX-License-Identifier: MIT
%global forgeurl    https://github.com/alexeiva/Raleway
%global commit      98add575720aa077b7d253477e26c463a55e71da
%forgemeta

Version: 4.025
Release: 5%{?dist}
URL:     %{forgeurl}

%global foundry           Impallari
%global fontlicense       OFL
%global fontlicenses      OFL.txt
%global fontdocs          *.txt *.md
%global fontdocsex        %{fontlicenses}

%global fontfamily        Raleway
%global fontsummary       Raleway, an elegant sans-serif font family
%global fonts             fonts/TTF/*ttf
%global fontconfngs       %{SOURCE10}
%global fontdescription   %{expand:
Raleway is an elegant sans-serif font family intended for headings and other
large size usage.

It features both old style and lining numerals, standard and discretionary
ligatures, a pretty complete set of diacritics, as well as a stylistic
alternate inspired by more geometric sans-serif typefaces than its
neo-grotesque inspired default character set.}

%fontmeta

%global source_files %{expand:
Source0:  %{forgesource}
Source10: 58-%{fontpkgname}.xml
}

%fontpkg

%new_package doc
Summary:   Optional documentation files of %{source_name}
BuildArch: noarch
%description doc
This package provides optional documentation files shipped with
%{source_name}.

%prep
%forgesetup
%linuxtext %{fontdocs} %{fontlicenses}

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
%doc documents/*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 27 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 4.025-4.20200310git98add57
🐞 Workaround Fedora problems created by rpm commit 93604e2

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 4.025-3.20200310git98add57
💥 Actually rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are
  valid

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 4.025-2.20200310git98add57
👻 Rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are valid

* Tue Mar 10 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 4.025-1.20200310git98add57.fc33
✅ Convert to fonts-rpm-macros use

* Sun Mar 12 2017 Fabio Valentini <decathorpe@gmail.com> - 3.0-1.git20161116.6c67ab1
- Initial package.

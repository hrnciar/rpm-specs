Version:        0.5.2
Release:        3%{?dist}
URL:            https://launchpad.net/newscycle

%global foundry           glyphography
%global fontlicense       OFL
%global fontlicenses      OFL.txt
%global fontdocs          *.txt
%global fontdocsex        %{fontlicenses}

%global fontfamily        newscycle
%global fontsummary       A realist sans-serif font family based on News Gothic

%global fonts             *.ttf
%global fontconfs         %{SOURCE10}

%global fontdescription   %{expand:
Inspired by the original News Gothic, which found an eminently useful
life in print media news coverage, the goal of this project is to design
a highly readable open font suitable for large bodies of text, even at
small sizes, and that is available at multiple weights. In addition to
the readability and weight, however, the project is extending News
Gothic's glyph coverage to alphabets derived from Latin, Cyrillic, and
Greek, including the accent marks and diacritics required by languages
outside of Western Europe.
}

Source0:        %{url}/trunk/%{version}/+download/%{fontfamily}-%{version}.zip
Source10:       61-%{fontpkgname}.conf

%fontpkg

%prep
%setup -n %{fontfamily}-%{version}
rm -f *~ *.svg

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
* Wed Feb 26 2020 Iñaki Úcar <iucar@fedoraproject.org> - 0.5.2-3
- Add "glyphography" as foundry name, rename package

* Wed Feb 26 2020 Iñaki Úcar <iucar@fedoraproject.org> - 0.5.2-2
- Adapt to the new guidelines https://pagure.io/packaging-committee/issue/935

* Tue Feb 25 2020 Iñaki Úcar <iucar@fedoraproject.org> - 0.5.2-1
- Initial packaging for Fedora

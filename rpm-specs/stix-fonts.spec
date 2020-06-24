# SPDX-License-Identifier: MIT
%global forgeurl https://github.com/stipub/stixfonts/
Version: 2.0.2
%forgemeta

Release: 6%{?dist}
URL:     http://www.stixfonts.org/

%global foundry           STIX
%global fontlicense       OFL
%global fontlicenses      docs/STIX_%{version}_license.pdf
%global fontdocs          *.md docs/*.txt
%global fontdocsex        %{fontlicenses}

%global fontfamily        STIX
%global fontsummary       STIX, a scientific and engineering font family
%global fontpkgheader     %{expand:
Obsoletes: stix-math-fonts < %{version}-%{release}
}
%global fonts             OTF/STIX2Text*otf OTF/STIX2Math*otf
%global fontconfngs       %{SOURCE10}
%global fontdescription   %{expand:
The mission of the Scientific and Technical Information Exchange (STIX) font
creation project is the preparation of a comprehensive set of fonts that serve
the scientific and engineering community in the process from manuscript
creation through final publication, both in electronic and print formats.
}

%fontmeta

%global source_files %{expand:
Source0:  %{forgesource0}
Source10: 65-%{fontpkgname0}.xml
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

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%files doc
%license docs/STIX_%{version}_license.pdf
%doc docs/charts/*pdf

%changelog
* Mon Apr 27 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 2.0.2-6
🐞 Workaround Fedora problems created by rpm commit 93604e2

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 2.0.2-5
💥 Actually rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are
  valid

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 2.0.2-4
👻 Rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are valid

* Mon Mar 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 2.0.2-3
✅ Lint, lint, lint and lint again

* Sat Feb 22 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 2.0.2-2
✅ Rebuild with fonts-rpm-macros 2.0.2

* Sat Feb 15 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 2.0.2-1
✅ Convert to fonts-rpm-macros use

* Thu Nov 1 2007 Nicolas Mailhot <nim@fedoraproject.org>
- 0.9-4
✅ Initial packaging

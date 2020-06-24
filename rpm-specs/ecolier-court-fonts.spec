# SPDX-License-Identifier: MIT
Version: 20070702
Release: 35%{?dist}
# This used to be published here, copies are all over the web now
#URL:     http://perso.orange.fr/jm.douteau/page_ecolier.htm

%global fontlicense       OFL
%global fontlicenses      lisez_moi.txt
%global fontdocs          README-Fedora.txt

%global common_description %{expand:
The Écolier court font families were created by Jean-Marie Douteau to mimic the
traditional cursive writing French children are taught in school.

He kindly released two of them under the OFL, which are redistributed in this
package.}

%global fontfamily0       Ecolier Court
%global fontsummary0      Écolier Court, a schoolchildren cursive Latin font family
%global fontpkgheader0    %{expand:
Obsoletes: ecolier-court-fonts-common < %{version}-%{release}
}
%global fonts0            %{SOURCE10}
%global fontconfngs0      %{SOURCE20}
%global fontdescription0  %{expand:
%{common_description}}

%global fontfamily1       Ecolier Lignes Court
%global fontsummary1      Écolier Lignes Court, a schoolchildren cursive Latin font family with lines
%global fontpkgheader1    %{expand:
Obsoletes: ecolier-court-lignes-fonts < %{version}-%{release}
}
%global fonts1            %{SOURCE11}
%global fontconfngs1      %{SOURCE21}

%global fontdescription1  %{expand:
%{common_description}

The « lignes » (lines) Écolier Court font variant includes the Seyes lining
commonly used on schoolchildren notepads.}

%fontmeta

%global source_files %{expand:
Source0:  lisez_moi.txt
Source1:  README-Fedora.txt
Source10: ec_cour.ttf
Source11: ecl_cour.ttf
Source20: 61-%{fontpkgname}.xml
Source21: 61-%{fontpkgname1}.xml
}

%fontpkg

%fontmetapkg

%prep
%setup -q -c -T
install -m 0644 -p %{SOURCE0} %{SOURCE1} .
%linuxtext *.txt

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
 Wed Apr 22 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 20070702-35
🐞 Workaround Fedora problems created by rpm commit 93604e2

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 20070702-34
💥 Actually rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are
  valid

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 20070702-33
👻 Rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are valid

* Mon Mar 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 20070702-32
✅ Lint, lint, lint and lint again

* Sat Feb 22 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 20070702-31
✅ Rebuild with fonts-rpm-macros 2.0.2

* Sat Feb 15 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 20070702-29
✅ Convert to fonts-rpm-macros use

* Sat Jul 19 2008 Nicolas Mailhot <nim@fedoraproject.org>
- 20070702-1
✅ Initial packaging

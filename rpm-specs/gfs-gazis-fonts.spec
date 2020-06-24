# SPDX-License-Identifier: MIT
Version: 20091008
Release: 22%{?dist}
URL:     http://www.greekfontsociety-gfs.gr/typefaces/18th_century

%global foundry           GFS
%global fontlicense       OFL
%global fontlicenses      OFL.txt
%global fontdocs          *.txt
%global fontdocsex        %{fontlicenses}

%global fontfamily        Gazis
%global fontsummary       GFS Gazis, an 18th century oblique Greek font family
%global fonts             *.otf
%global fontconfngs       %{SOURCE10}
%global fontdescription   %{expand:
During the whole of the 18th century the old tradition of using Greek types
designed to conform to the Byzantine cursive hand with many ligatures and
abbreviations — as it was originated by Aldus Manutius in Venice and
consolidated by Claude Garamont (Grecs du Roy) — was still much in practice,
although clearly on the wane.

GFS Gazis is a typical German example of this practice as it appeared at the
end of that era in the 1790’s. Its name pays tribute to Anthimos Gazis
(1758-1828), one of the most prolific Greek thinkers of the period, who was
responsible for writing, translating and editing numerous books, including the
editorship of the important Greek periodical Ερμής ο Λόγιος (Litterary Hermes)
in Wien.

GFS Gazis has been digitally designed by George D. Matthiopoulos.}

%global archivename %{lua:t=string.gsub(rpm.expand("%{foundry} %{fontfamily}"), "[%p%s]+", "_");print(t)}

%fontmeta

%global source_files %{expand:
Source0:  http://www.greekfontsociety-gfs.gr/_assets/fonts/%{archivename}.zip
Source10: 61-%{fontpkgname}.xml
}

%fontpkg

%new_package doc
Summary:   Optional documentation files of %{source_name}
BuildArch: noarch
%description doc
This package provides optional documentation files shipped with
%{source_name}.

%prep
%setup -q -c -T
unzip -j -q  %{SOURCE0}
%linuxtext *.txt

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
%doc *.pdf

%changelog
* Mon Apr 27 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 20091008-22
🐞 Workaround Fedora problems created by rpm commit 93604e2

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 20091008-21
💥 Actually rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are
  valid

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 20091008-20
👻 Rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are valid

* Sat Feb 22 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 20091008-19
✅ Rebuild with fonts-rpm-macros 2.0.2

* Sat Feb 15 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 20091008-18
✅ Convert to fonts-rpm-macros use

* Sun Nov 25 2007 Nicolas Mailhot <nim@fedoraproject.org>
- 20070417-1
✅ Initial packaging

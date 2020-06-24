# SPDX-License-Identifier: MIT
Version: 20100203
Release: 22%{?dist}
URL:     http://www.greekfontsociety-gfs.gr/typefaces/19th_century

%global foundry           GFS
%global fontlicense       OFL
%global fontlicenses      OFL.txt
%global fontdocs          *.txt
%global fontdocsex        %{fontlicenses}

%global fontfamily        Goschen
%global fontsummary       GFS Göschen, a 19th century neoclassical cursive Greek font family
%global fonts             *.otf
%global fontconfngs       %{SOURCE10}
%global fontdescription   %{expand:
Georg Joachim Göschen founded in 1782 the publishing house of G.J.
Göschensche Verlagsbuchhandlung in Leipzig and was one of the most active
publishers of the period in Germany. Göschen was very interested in
typography, influenced by the fame and quality of the editions of G. Bodoni
and F. Didot.

In 1797, he collaborated with the leading scholar of the period, Johann Jakob
Griesbach, to edit and publish the New Testament in Greek for which he formed
a committee of scholars to decide the new Greek type which were eventually
cut by Johann Prillwitz. The book appeared in 1803 and the types show many
influences from the Greek types of Bodoni. Their characteristic was the
neoclassical form of marked contrast between thick and thin strokes, the
cursive style and the large size of the font.

The design was too cumbersome to allow general use and can be considered
successful only for its indirect influence on the later cut Greek Leipzig
type. It is, however, part of the greater heritage of Greek type design and
therefore the type has been digitized by George D. Matthiopoulos in 2009 and
is part of GFS’ type library under the name GFS Göschen cursive, in
commemoration of the great German publisher.}

%global archivename %{lua:t=string.gsub(rpm.expand("%{foundry} %{fontfamily}"), "[%p%s]+", "_");print(t)}

%fontmeta

%global source_files %{expand:
Source0:  http://www.greekfontsociety-gfs.gr/_assets/fonts/%{archivename}.zip
Source10: 64-%{fontpkgname}.xml
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
- 20100203-22
🐞 Workaround Fedora problems created by rpm commit 93604e2

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 20100203-21
💥 Actually rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are
  valid

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 20100203-20
👻 Rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are valid

* Sat Feb 22 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 20100203-19
✅ Rebuild with fonts-rpm-macros 2.0.2

* Sat Feb 15 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 20100203-18
✅ Convert to fonts-rpm-macros use

* Sat Feb 13 2010 Nicolas Mailhot <nim@fedoraproject.org>
- 20100203-1
✅ Initial packaging

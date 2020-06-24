# SPDX-License-Identifier: MIT
Version: 20191205
Release: 5%{?dist}
URL:     http://www.greekfontsociety-gfs.gr/typefaces/20th_21st_century

%global foundry           GFS
%global fontlicense       OFL
%global fontlicenses      OFL.txt
%global fontdocs          *.txt
%global fontdocsex        %{fontlicenses}

%global fontfamily        Galatea
%global fontsummary       GFS Galatea, a 20th century Greek font family
%global fonts             *.otf
%global fontconfngs       %{SOURCE10}
%global fontdescription   %{expand:
GFS Galatea Bold revives in digital form an older hot metal typeface from the
1920’s, which can be found in older Greek type specimens named simply as FAT
type. The font was used as a bold companion of Didot Greek (Apla/Monotype 92).
It has many similarities with Didot Greek (Απλά) in design, but it differs in
its reduced stroke contrast, the use of a lunar lower case epsilon (reminiscent
of the similar epsilon in Porson Greek) and in sturdier stems and slab serifs.
An experimental projection of these characteristics to a lighter version has
led to the introduction of GFS Galatea Regular. The name Galatea is a tribute
to the author and feminist Galatea Kazantzakis (1881–1962) as samples of the
typeface were found in several of her books.

Both typefaces were designed by George Triantafyllakos and are freely available
for use.}

%global archivename %{lua:t=string.gsub(rpm.expand("%{foundry} %{fontfamily}"), "[%p%s]+", "_");print(t)}

%fontmeta

%global source_files %{expand:
Source0:  http://www.greekfontsociety-gfs.gr/_assets/fonts/%{archivename}.zip
Source10: 60-%{fontpkgname}.xml
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
- 20191205-5
🐞 Workaround Fedora problems created by rpm commit 93604e2

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 20191205-4
💥 Actually rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are
  valid

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 20191205-3
👻 Rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are valid

* Sat Feb 22 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 20191205-2
✅ Rebuild with fonts-rpm-macros 2.0.2

* Sat Feb 15 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 20191205-1
✅ Initial packaging

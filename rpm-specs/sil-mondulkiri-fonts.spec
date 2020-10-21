# SPDX-License-Identifier: MIT
Version: 7.100
Release: 7%{?dist}
URL:     https://scripts.sil.org/Mondulkiri

%global foundry           SIL
%global fontlicense       OFL
%global fontlicenses      OFL.txt
%global fontdocs          *.txt
%global fontdocsex        %{fontlicenses}

%global fontfamily0       Mondulkiri
%global fontsummary0      Khmer Mondulkiri, a Khmer script font family suited for very small print
%global fonts0            Mondulkiri*.ttf
%global fontconfngs0      %{SOURCE10}
%global fontdescription0  %{expand:
The Khmer Mondulkiri font family provides Unicode support for the Khmer script.
It is very light and well suited for very small print.}

%global fontfamily1       Busra
%global fontsummary1      Khmer Busra, a Khmer script font family suited for normal text
%global fonts1            Busra*.ttf
%global fontconfngs1      %{SOURCE11}
%global fontdescription1  %{expand:
The Khmer Busra font family provides Unicode support for the Khmer script. It
is probably the best SIL font family for Khmer normal text. The regular font
was formerly named “Khmer Mondulkiri Book” and the bold font was named “Khmer
Mondulkiri SemiBold”.}

%global archivename %{lua:t=string.gsub(rpm.expand("%{fontfamily0}"), "[%p%s]+", "");print(t)}-%{version}

%fontmeta

%global source_files %{expand:
Source0:  https://scripts.sil.org/cms/scripts/render_download.php?format=file&media_id=%{archivename}&filename=%{archivename}.zip#/%{archivename}.zip
Source10: 65-%{fontpkgname0}.xml
Source11: 65-%{fontpkgname1}.xml
}

%fontpkg

%fontmetapkg

%new_package doc
Summary:   Optional documentation files of %{source_name}
BuildArch: noarch
%description doc
This package provides optional documentation files shipped with
%{source_name}.

%prep
%setup -q -n %{archivename}
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
%doc documentation/*pdf

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 27 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 7.100-6
🐞 Workaround Fedora problems created by rpm commit 93604e2

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 7.100-5
💥 Actually rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are
  valid

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 7.100-4
👻 Rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are valid

* Sat Feb 22 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 7.100-3
✅ Rebuild with fonts-rpm-macros 2.0.2

* Sat Feb 15 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 7.100-1
✅ Initial packaging

Version:        0.954
Release:        13%{?dist}
## Note that upstream is dead and there is no download link available at this minute
## so please don't report FTBFS bugs for this package.
URL:            http://www.ctan.org/tex-archive/fonts/Asana-Math/

%global foundry           oflb
%global fontlicense       OFL
%global fontlicenses      License.txt
%global fontdocs          *.txt README.license
%global fontdocsex        %{fontlicenses}

%global fontfamily        Asana Math
%global fontsummary       An OpenType font with a MATH table
%global fonts             Asana-Math.otf
%global fontconfs         %{SOURCE1}
%global fontdescription   %{expand:
An OpenType font with a MATH table that can be used with XeTeX to typeset math
content.}

Source0:        http://mirrors.ctan.org/fonts/Asana-Math/Asana-Math.otf
Source1:        63-%{fontpkgname}.conf
Source2:        README.license
#license text extracted from font file
Source3:        License.txt

%fontpkg

%prep
%setup -q -c -T
cp -p %{SOURCE0} %{SOURCE1} %{SOURCE2} %{SOURCE3} .

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.954-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 24 2020 Parag Nemade <pnemade AT redhat DOT com> - 0.954-12
- Update fontconfig DTD id in conf file

* Fri Mar 06 2020 Parag Nemade <pnemade AT redhat DOT com> - 0.954-11
- Convert to new fonts packaging guidelines
- Drop Obsoletes: and Provides: on asana-math-fonts (Added in F14)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.954-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.954-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.954-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.954-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.954-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.954-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.954-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.954-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.954-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Nov 05 2014 Parag Nemade <pnemade AT redha DOT com> - 0.954-1
- update to 954 update

* Thu Oct 16 2014 Parag Nemade <pnemade AT redhat.com> - 0.952-2
- Add metainfo file to show this font in gnome-software

* Tue Sep 30 2014 Parag Nemade <pnemade AT redha DOT com> - 0.952-1
- update to 952 update

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.930-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.930-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.930-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.930-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.930-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Aug 25 2011 Parag Nemade <pnemade AT redha DOT com> - 0.930-1
- Update to next upstream release

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.914-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jul 13 2010 Parag Nemade <pnemade AT redhat.com> - 0.914-8
- Initial package to rename from asana-math-fonts.
- updated/renamed this package according to fonts packaging guidelines.


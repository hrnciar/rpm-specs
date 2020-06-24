%global commit bd245c9

Name:           pcfi
Version:        2010.08.09
Release:        17.20111103git%{commit}%{?dist}
Summary:        PDF Core Font Information

License:        BSD
URL:            https://github.com/jukka/pcfi
Source0:        https://github.com/jukka/pcfi/tarball/%{commit}/jukka-pcfi-%{commit}.tar.gz
# Originally downloaded from: http://opensource.adobe.com/wiki/display/cmap/License
# This now points to Adobe's sourceforge pages
Source1:        License
BuildArch:      noarch
BuildRequires:  maven-local
Requires:       jpackage-utils


%description
Collection of PDF core font information files downloaded from Adobe's
Developer Center and elsewhere. This collection contains font metrics for the
14 PDF core fonts, CMaps for the PDF CJK fonts and the Adobe Glyph List.   The
files are stored inside the com/adobe/pdf/pcfi directory. See the individual
files for exact licensing information.


%prep
%setup -q -n jukka-pcfi-%{commit}
sed -i 's/\r//' src/main/resources/META-INF/LICENSE.txt
cp %SOURCE1 .


%build
%mvn_build


%install
%mvn_install


%files -f .mfiles
%doc README.txt src/main/resources/META-INF/LICENSE.txt License


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2010.08.09-17.20111103gitbd245c9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2010.08.09-16.20111103gitbd245c9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2010.08.09-15.20111103gitbd245c9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2010.08.09-14.20111103gitbd245c9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2010.08.09-13.20111103gitbd245c9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2010.08.09-12.20111103gitbd245c9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2010.08.09-11.20111103gitbd245c9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2010.08.09-10.20111103gitbd245c9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2010.08.09-9.20111103gitbd245c9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2010.08.09-8.20111103gitbd245c9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Orion Poplawski <orion@cora.nwra.com> - 2010.08.09-7.20111103gitbd245c9
- Use new maven macros to build

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2010.08.09-7.20111103gitbd245c9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2010.08.09-6.20111103gitbd245c9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 2010.08.09-5.20111103gitbd245c9
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2010.08.09-4.20111103gitbd245c9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2010.08.09-3.20111103gitbd245c9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Nov 3 2011 Orion Poplawski <orion@cora.nwra.com> - 2010.08.09-2.20111103gitbd245c9
- Use github upstream, build with maven
- Drop BuildRoot

* Thu Aug 11 2011 Orion Poplawski <orion@cora.nwra.com> - 2010.08.09-1
- Initial package

Name:           relaxngDatatype
Version:        2011.1
Release:        12%{?dist}
Summary:        RELAX NG Datatype API
License:        BSD
URL:            https://github.com/java-schema-utilities/relaxng-datatype-java
BuildArch:      noarch

Source0:        https://github.com/java-schema-utilities/relaxng-datatype-java/archive/relaxngDatatype-%{version}.tar.gz
# License is not available in the tarball, this copy fetched from the tarball on the old sourceforge.net site
Source1:        copying.txt

BuildRequires:  maven-local

%description
RELAX NG is a public space for test cases and other ancillary software
related to the construction of the RELAX NG language and its
implementations.

%package        javadoc
Summary:        API documentation for %{name}

%description    javadoc
This package provides %{summary}.

%prep
%setup -q -n relaxng-datatype-java-relaxngDatatype-%{version}

cp -p %{SOURCE1} .

# remove unnecessary dependency on parent POM
%pom_remove_parent

%pom_xpath_remove "pom:build/pom:extensions"

# For compatibility
%mvn_alias "com.github.relaxng:relaxngDatatype" "relaxngDatatype:relaxngDatatype"

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/relaxngDatatype
%doc copying.txt

%files javadoc -f .mfiles-javadoc
%doc copying.txt

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2011.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 22 2019 Fabio Valentini <decathorpe@gmail.com> - 2011.1-11
- Remove unnecessary dependency on parent POM.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2011.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2011.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2011.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2011.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2011.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2011.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jun 15 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 2011.1-4
- Add missing build-requires

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2011.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2011.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Oct 21 2014 Mat Booth <mat.booth@redhat.com> - 2011.1-1
- Update to version released from new project location rhbz#981275
- Build/install with maven instead of ant
- Drop old javadoc rpm bug workaround

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-12.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-11.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 21 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-10.5
- Install license file with javadoc package
- Convert versioned javadoc to versionless
- Update to current packaging guidelines
- Remove msv provides and obsoletes

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-10.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Dec 12 2012 Michal Srb <msrb@redhat.com> - 1.0-9.4
- Source0 is now URL (Resolves: #875884)

* Fri Nov  2 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-8.4
- Add maven POM

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-8.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-7.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-6.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Mar  8 2010 Peter Lemenkov <lemenkov@gmail.com> - 1.0-5.3
- Added missing Requires: jpackage-utils (%%{_javadir} and %%{_javadocdir})

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-5.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-4.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jul 10 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.0-3.2
- drop repotag

* Mon Feb 12 2007 Andrew Overholt <overholt@redhat.com> 1.0-3jpp.1
- Fixed issues for Fedora-ization
- Add patch to compress the main jar

* Tue Apr 11 2006 Ralph Apel <r.apel@r-apel.de>- 0:1.0-3jpp
- First JPP-1.7 release

* Wed Aug 25 2004 Fernando Nasser <fnasser@redhat.com>- 0:1.0-2jpp
- Require Ant > 1.6
- Rebuild with Ant 1.6.2

* Tue Jul 06 2004 Ralph Apel <r.apel at r-apel.de> - 0:1.0-1jpp
- First JPackage build from sources


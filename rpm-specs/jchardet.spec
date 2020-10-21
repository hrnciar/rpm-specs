Name:           jchardet
Version:        1.1
Release:        22%{?dist}
Summary:        Java port of Mozilla's automatic character set detection algorithm

License:        MPLv1.1 or GPLv2+ or LGPLv2+
URL:            http://jchardet.sourceforge.net/
Source0:        https://download.sourceforge.net/jchardet/%{version}/jchardet-%{version}.zip
Source1:        https://repo1.maven.org/maven2/net/sourceforge/%{name}/%{name}/1.0/%{name}-1.0.pom
BuildArch:      noarch

BuildRequires:  maven-local

%description
jchardet is a java port of the source from Mozilla's automatic charset
detection algorithm. The original author is Frank Tang. What is available
here is the java port of that code. The original source in C++ can be found
from http://lxr.mozilla.org/mozilla/source/intl/chardet/. More information can
be found at http://www.mozilla.org/projects/intl/chardet.html.

%package javadoc
Summary:    API documentation for %{name}

%description javadoc
%{summary}.

%prep
%setup -q
find -name '*.class' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;

cp %{SOURCE1} pom.xml

# fix up the provided version
%pom_xpath_set /pom:project/pom:version %{version}

# remove hard-coded compiler configuration
%pom_remove_plugin :maven-compiler-plugin

# remove distributionManagement.status from pom (maven stops build
# when it's there)
%pom_xpath_remove pom:distributionManagement

# create proper dir structure
mkdir -p src/main/java/org/mozilla/intl/chardet
mv src/*java src/main/java/org/mozilla/intl/chardet

%build
%mvn_build

%install
%mvn_install


%files -f .mfiles
%license LICENSE

%files javadoc -f .mfiles-javadoc
%license LICENSE


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 14 2020 Mat Booth <mat.booth@redhat.com> - 1.1-21
- Fix https usage

* Mon Jul 13 2020 Mat Booth <mat.booth@redhat.com> - 1.1-20
- Allow building against JDK 11

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Mar 15 2017 Michael Simacek <msimacek@redhat.com> - 1.1-15
- Specfile cleanup

* Wed Feb 22 2017 Orion Poplawski <orion@cora.nwra.com> - 1.1-14
- Fix license (bug #1422847)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Feb 21 2014 Orion Poplawski <orion@cora.nwra.com> - 1.1-9
- Require java-headless (bug #1068252)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jun 12 2013 Orion Poplawski <orion@cora.nwra.com> - 1.1-7
- Update to current Java guidelines

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.1-5
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Apr 29 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.1-2
- Build with maven and provide maven metadata
- Add javadoc subpackage

* Fri Apr 22 2011 Orion Poplawski <orion@cora.nwra.com> - 1.1-1
- Initial package

Name:          jaxb2-maven-plugin
Version:       1.6
Release:       12%{?dist}
Summary:       JAXB-2 Maven Plugin
License:       ASL 2.0
Url:           http://www.mojohaus.org/jaxb2-maven-plugin/
# Source code avialable @ https://github.com/mojohaus/jaxb2-maven-plugin
Source0:       http://repo2.maven.org/maven2/org/codehaus/mojo/%{name}/%{version}/%{name}-%{version}-source-release.zip

BuildRequires: maven-local
BuildRequires: mvn(aopalliance:aopalliance)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(net.sf.cglib:cglib)
BuildRequires: mvn(org.apache.maven.plugin-testing:maven-plugin-testing-harness)
BuildRequires: mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires: mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires: mvn(org.apache.maven:maven-artifact:2.2.1)
BuildRequires: mvn(org.apache.maven:maven-compat)
BuildRequires: mvn(org.apache.maven:maven-core)
BuildRequires: mvn(org.apache.maven:maven-model:2.2.1)
BuildRequires: mvn(org.apache.maven:maven-plugin-api)
BuildRequires: mvn(org.codehaus.mojo:mojo-parent:pom:)
BuildRequires: mvn(org.codehaus.plexus:plexus-compiler-api)
BuildRequires: mvn(org.codehaus.plexus:plexus-utils)
BuildRequires: mvn(org.glassfish.jaxb:jaxb-jxc)
BuildRequires: mvn(org.glassfish.jaxb:jaxb-xjc)
BuildRequires: mvn(org.sonatype.plexus:plexus-build-api)
BuildRequires: mvn(xmlunit:xmlunit)

BuildArch:     noarch

%description
Mojo's JAXB-2 Maven plugin is used to create an object graph from
XSDs based on the JAXB 2.1 implementation and to generate XSDs from
JAXB-annotated Java classes.

%package javadoc
Summary:       Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q

sed -i 's/\r//' LICENSE.txt

# used only mvn3 apis
%pom_remove_dep org.apache.maven:maven-project
%pom_add_dep org.apache.maven:maven-compat

# missing build deps
%pom_xpath_set "pom:dependencies/pom:dependency[pom:artifactId ='jaxb-jxc']/pom:groupId" org.glassfish.jaxb
%pom_xpath_set "pom:dependencies/pom:dependency[pom:artifactId ='jaxb-xjc']/pom:groupId" org.glassfish.jaxb

# missing test deps
%pom_add_dep aopalliance:aopalliance::test
%pom_add_dep net.sf.cglib:cglib::test

# Disable integration tests
%pom_xpath_remove "pom:profiles"

%mvn_file :%{name} %{name}

%build
%mvn_build -- -Dmaven.test.failure.ignore=true

%install
%mvn_install

%files -f .mfiles
%license LICENSE.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt

%changelog
* Sat May 16 2020 Fabio Valentini <decathorpe@gmail.com> - 1.6-12
- Add missing BuildRequires and regenerate them with xmvn-builddep.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Feb 06 2015 gil cattaneo <puntogil@libero.it> 1.6-2
- introduce license macro

* Mon Jan 26 2015 gil cattaneo <puntogil@libero.it> 1.6-1
- update to 1.6

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 1.5-4
- Use Requires: java-headless rebuild (#1067528)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 09 2013 gil cattaneo <puntogil@libero.it> 1.5-2
- switch to XMvn
- minor changes to adapt to current guideline

* Thu May 09 2013 gil cattaneo <puntogil@libero.it> 1.5-1
- initial rpm

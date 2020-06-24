%global githash cb6709646eed97c271d73f50ad750cc43c8e052a
Name:             paranamer
Version:          2.8
Release:          12%{?dist}
Summary:          Java library for accessing non-private method's parameter names at run-time
License:          BSD
URL:              https://github.com/paul-hammant/paranamer
Source0:          %{url}/archive/%{githash}/%{name}-%{githash}.tar.gz

Patch0:           0001-Port-to-current-qdox.patch

BuildRequires:    maven-local
BuildRequires:    mvn(com.thoughtworks.qdox:qdox)
BuildRequires:    mvn(javax.inject:javax.inject)
BuildRequires:    mvn(junit:junit)
BuildRequires:    mvn(org.apache.ant:ant)
BuildRequires:    mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:    mvn(org.apache.maven:maven-plugin-api)
BuildRequires:    mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:    mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:    mvn(org.mockito:mockito-all)
BuildRequires:    mvn(org.ow2.asm:asm)

BuildArch:        noarch

%description
Paranamer is a Java library that allows the parameter names of non-private
methods and constructors to be accessed at run-time. Most compilers discard
this information; traditional Reflection on JDK <= 7 would show something like
doSomething(mypackage.Person ???) instead of doSomething(mypackage.Person toMe).
The Paranamer library fills this gap for these JDK versions.

%package ant
Summary:          ParaNamer Ant

%description ant
This package contains the ParaNamer Ant tasks.

%package generator
Summary:          ParaNamer Generator

%description generator
This package contains the ParaNamer Generator.

%package integration-tests
Summary:          ParaNamer Integration Test Parent POM

%description integration-tests
ParaNamer Integration Test Parent POM.

%package it-011
Summary:          ParaNamer Integration Test 011

%description it-011
ParaNamer IT 011: can use maven plugin defaults.

%package maven-plugin
Summary:          ParaNamer Maven plugin

%description maven-plugin
This package contains the ParaNamer Maven plugin.

%package parent
Summary:          ParaNamer Parent POM

%description parent
This package contains the ParaNamer Parent POM.

%package javadoc
Summary:          Javadoc for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{githash}

%patch0 -p1

# Cleanup
find -name "*.class" -print -delete
# Do not erase test resources
find -name "*.jar" -print ! -name "test.jar" -delete

chmod -x LICENSE.txt

# remove unnecessary dependency on parent POM
%pom_remove_parent

# Remove wagon extension
%pom_xpath_remove "pom:build/pom:extensions"

%pom_remove_plugin -r :maven-dependency-plugin
%pom_remove_plugin -r :maven-javadoc-plugin
%pom_remove_plugin -r :maven-source-plugin

# Disable distribution module
%pom_disable_module %{name}-distribution

# Unavailable test deps
%pom_remove_dep -r net.sourceforge.f2j:
%pom_xpath_remove -r "pom:dependency[pom:classifier = 'javadoc' ]"
# package org.netlib.blas does not exist
rm -r %{name}/src/test/com/thoughtworks/paranamer/JavadocParanamerTest.java
# testRetrievesParameterNamesFromBootstrapClassLoader java.lang.AssertionError:
#       Should not find names for classes loaded by the bootstrap class loader.
rm -r %{name}/src/test/com/thoughtworks/paranamer/BytecodeReadingParanamerTestCase.java

%build

%mvn_build -s

%install
%mvn_install

%files -f .mfiles-%{name}
%doc README.md
%license LICENSE.txt

%files ant -f .mfiles-%{name}-ant

%files generator -f .mfiles-%{name}-generator
%license LICENSE.txt

%files integration-tests -f .mfiles-%{name}-integration-tests
%license LICENSE.txt

%files it-011 -f .mfiles-%{name}-it-011
%license LICENSE.txt

%files maven-plugin -f .mfiles-%{name}-maven-plugin

%files parent -f .mfiles-%{name}-parent
%license LICENSE.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 19 2019 Fabio Valentini <decathorpe@gmail.com> - 2.8-11
- Remove unnecessary dependency on parent POM.

* Tue Oct 08 2019 Fabio Valentini <decathorpe@gmail.com> - 2.8-10
- Add BuildRequires for ant.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Michael Simacek <msimacek@redhat.com> - 2.8-4
- Port to current qdox

* Tue Jun 21 2016 gil cattaneo <puntogil@libero.it> 2.8-3
- add missing build requires

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Sep 25 2015 gil cattaneo <puntogil@libero.it> - 2.8-1
- Upstream release 2.8
- Fix FTBFS RHBZ#1239758
- Split maven plugin to sub package RHBZ#1119279
- Use Qdox 2.x RHBZ#1191694
- Run test suite
- Use BR mvn()-like
- Fix URL field
- Introduce license macro
- Minor changes for adapt to current guideline

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jun 17 2014 Marek Goldmann <mgoldman@redhat.com> - 2.4.1-9
- Switch to xmvn

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 2.4.1-7
- Use Requires: java-headless rebuild (#1067528)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 20 2013 Marek Goldmann <mgoldman@redhat.com> - 2.4.1-5
- Using pom macros
- Fixed build by adding version to the plugin

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 2.4.1-3
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Mar 12 2012 Marek Goldmann <mgoldman@redhat.com> 2.4.1-1
- Upstream release 2.4.1
- Cleanup in spec file

* Mon Mar 12 2012 Marek Goldmann <mgoldman@redhat.com> 2.2-2
- Updated summary and url

* Tue Feb 21 2012 Marek Goldmann <mgoldman@redhat.com> 2.2-1
- Initial packaging


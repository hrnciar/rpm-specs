%global git_tag 6578a73424849be942308f263eaf47fa897bcd13

Name:           maven-indexer
Version:        6.0.0
Release:        5%{?dist}
Summary:        Standard for producing indexes of Maven repositories

License:        ASL 2.0
URL:            http://maven.apache.org/maven-indexer/index.html

Source0:        https://github.com/apache/maven-indexer/archive/%{git_tag}/maven-indexer-%{version}.tar.gz

# Port to latest lucene, sent upstream:
# - https://github.com/apache/maven-indexer/pull/37
Patch0: 0001-MINDEXER-115-Migrate-to-BooleanQuery.Builder.patch
Patch1: 0002-Eliminate-use-of-deprecated-Lucene-API.patch
Patch2: 0003-Changes-needed-to-migrate-to-Lucene-8.patch

# Drop dep on truezip
Patch3:         maven-indexer-truezip.patch

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(com.google.code.findbugs:jsr305)
BuildRequires:  mvn(com.google.inject:guice)
BuildRequires:  mvn(javax.annotation:javax.annotation-api)
BuildRequires:  mvn(javax.inject:javax.inject)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.lucene:lucene-analyzers-common)
BuildRequires:  mvn(org.apache.lucene:lucene-backward-codecs)
BuildRequires:  mvn(org.apache.lucene:lucene-core) >= 8.0.0
BuildRequires:  mvn(org.apache.lucene:lucene-highlighter)
BuildRequires:  mvn(org.apache.lucene:lucene-queryparser)
BuildRequires:  mvn(org.apache.maven.archetype:archetype-catalog)
BuildRequires:  mvn(org.apache.maven:maven-model)
BuildRequires:  mvn(org.apache.maven:maven-parent:pom:)
BuildRequires:  mvn(org.apache.maven.resolver:maven-resolver-api)
BuildRequires:  mvn(org.apache.maven.resolver:maven-resolver-util)
BuildRequires:  mvn(org.apache.maven.wagon:wagon-provider-api)
BuildRequires:  mvn(org.eclipse.sisu:org.eclipse.sisu.inject)
BuildRequires:  mvn(org.eclipse.sisu:org.eclipse.sisu.plexus)
BuildRequires:  mvn(org.eclipse.sisu:sisu-maven-plugin)
BuildRequires:  mvn(org.slf4j:slf4j-api)

Requires: lucene >= 8.0.0

%description
Apache Maven Indexer (former Sonatype Nexus Indexer) is the defacto
standard for producing indexes of Maven repositories. The Indexes
are produced and consumed by all major tools in the ecosystem.

%package javadoc
Summary:        Javadocs for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{git_tag}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3

find -name '*.jar' -delete
find -name '*.zip' -delete
find -name '*.class' -delete

# Tests need porting to a modern jetty
%pom_remove_dep -r org.mortbay.jetty:jetty
%pom_remove_plugin -r :maven-failsafe-plugin

# Remove unnecessary plugins for RPM builds
%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :apache-rat-plugin . indexer-core
%pom_remove_plugin :animal-sniffer-maven-plugin

# Avoid bundling Lucene in shaded jar
%pom_remove_plugin :maven-shade-plugin indexer-core

# Make static analysis annotations have provided scope
%pom_xpath_inject "pom:dependency[pom:artifactId='jsr305']" "<scope>provided</scope>" . indexer-core

# Disable CLI module because of how it bundles stuff
%pom_disable_module indexer-cli

# No need to ship examples
%pom_disable_module indexer-examples

# Ensure sisu index is generated
%pom_add_plugin "org.eclipse.sisu:sisu-maven-plugin:0.3.3" . \
"<executions><execution>
  <id>generate-index</id>
  <goals><goal>main-index</goal></goals>
</execution></executions>"

# Drop unneeded optional dep on truezip
%pom_remove_dep -r de.schlichtherle.truezip:
rm indexer-core/src/main/java/org/apache/maven/index/util/zip/TrueZipZipFileHandle.java

%build
# Skip tests because they need porting to modern jetty
%mvn_build -f -- -Dsource=1.8 -DdetectJavaApiLink=false

%install
%mvn_install

%files -f .mfiles
%license NOTICE
%doc README.md

%files javadoc -f .mfiles-javadoc
%license NOTICE

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 13 2020 Mat Booth <mat.booth@redhat.com> - 6.0.0-4
- Disable failsafe (we cannot run tests due to missing deps in fedora)
- Fix javadoc generation when building against JDK 11

* Thu Jun 27 2019 Mat Booth <mat.booth@redhat.com> - 6.0.0-3
- Ensure sisu indexes are generated

* Tue Jun 18 2019 Mat Booth <mat.booth@redhat.com> - 6.0.0-2
- Ensure we get a new enough lucene

* Wed Jun 12 2019 Mat Booth <mat.booth@redhat.com> - 6.0.0-1
- Update to latest upstream release
- Add patches to port to Lucene 8

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.2-0.8.gite0570bf
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.2-0.7.gite0570bf
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 20 2018 Mat Booth <mat.booth@redhat.com> - 5.1.2-0.6.gite0570bf
- Port to lucene 7

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.2-0.5.gite0570bf
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Aug 08 2017 Mat Booth <mat.booth@redhat.com> - 5.1.2-0.4.gite0570bf
- Improved lucene porting patches

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.2-0.3.gite0570bf
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 27 2017 Mat Booth <mat.booth@redhat.com> - 5.1.2-0.2.gite0570bf
- Update lucene patch

* Tue Feb 07 2017 Mat Booth <mat.booth@redhat.com> - 5.1.2-0.1.gite0570bf
- Update to 5.1.2 snapshot (as available in Maven Central)
- Port to Lucene 5
- Drop unneeded dep on truezip
- Adopt license macro

* Mon Dec 05 2016 Mat Booth <mat.booth@redhat.com> - 5.1.1-10
- Regenerate BRs

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Dec 12 2015 Gerard Ryan <galileo@fedoraproject.org> - 5.1.1-8
- Build against lucene3 now that it's available (& expected here)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Mar 22 2014 Gerard Ryan <galileo@fedoraproject.org> - 5.1.1-5
- Switch to java-headless requires
- Add patch for lucene 4 API changes

* Sat Aug 24 2013 Gerard Ryan <galileo@fedoraproject.org> - 5.1.1-4
- Stop building indexer-cli that bundles lots of stuff

* Mon Aug 12 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 5.1.1-3
- Remove unneeded animal-sniffer dependency

* Sat Aug 10 2013 Gerard Ryan <galileo@fedoraproject.org> - 5.1.1-2
- [RHBZ-958162] Migrate from aether to its subpackages
- Remove dependency on jetty-start, since it's for test

* Sat Aug 10 2013 Gerard Ryan <galileo@fedoraproject.org> - 5.1.1-1
- Update to version 5.1.1
- Replace patches with POM macros
- [RHBZ-985695] Replace sisu dependency
- [RHBZ-985705] Use new eclipse version of aether
- Clean up to use new maven guidelines and macros

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 4.1.2-4
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Wed Jul 25 2012 Gerard Ryan <galileo@fedoraproject.org> - 4.1.2-3
- Don't install super jar created by maven-shade-plugin indexer-core-*-cli.jar

* Wed Jul 25 2012 Gerard Ryan <galileo@fedoraproject.org> - 4.1.2-2
- Remove jars that we don't want to redistribute here from source zip in srpm.

* Mon Jul 09 2012 Gerard Ryan <galileo@fedoraproject.org> - 4.1.2-1
- Initial package.

Name:           maven-archetype
Version:        3.2.0
Release:        1%{?dist}
Summary:        Maven project templating toolkit

# Most of the code is under ASL 2.0, but some bundled jdom sources are
# under ASL 1.1
License:        ASL 2.0 and ASL 1.1
URL:            https://maven.apache.org/archetype/
Source0:        http://archive.apache.org/dist/maven/archetype/%{name}-%{version}-source-release.zip

# We only use groovy for running a post generation script,
# removing this continues the old behaviour of ignoring it
Patch1: 0001-Avoid-reliance-on-groovy.patch

# Taken from https://github.com/apache/maven-archetype/commit/e4eed30d1c0c6eabf45c49194ff6f0d8a4e4d5a7
Patch2: 0002-declare-dependencies.patch

# Port to commons-lang3
Patch3: 0003-Port-to-commons-lang3.patch

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(commons-collections:commons-collections)
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(net.sourceforge.jchardet:jchardet)
BuildRequires:  mvn(org.apache.commons:commons-lang3)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven:maven-archiver)
BuildRequires:  mvn(org.apache.maven:maven-artifact)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-model)
BuildRequires:  mvn(org.apache.maven:maven-parent:pom:)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven:maven-settings)
BuildRequires:  mvn(org.apache.maven:maven-settings-builder)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.shared:maven-artifact-transfer)
BuildRequires:  mvn(org.apache.maven.shared:maven-invoker)
BuildRequires:  mvn(org.apache.maven.shared:maven-script-interpreter)
BuildRequires:  mvn(org.apache.maven.wagon:wagon-provider-api)
BuildRequires:  mvn(org.apache.velocity:velocity)
BuildRequires:  mvn(org.codehaus.modello:modello-maven-plugin)
BuildRequires:  mvn(org.codehaus.plexus:plexus-archiver)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-annotations)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:  mvn(org.codehaus.plexus:plexus-interactivity-api)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.codehaus.plexus:plexus-velocity)
BuildRequires:  mvn(org.jdom:jdom)

%description
Archetype is a Maven project templating toolkit. An archetype is
defined as an original pattern or model from which all other things of
the same kind are made. The names fits as we are trying to provide a
system that provides a consistent means of generating Maven
projects. Archetype will help authors create Maven project templates
for users, and provides users with the means to generate parameterized
versions of those project templates.

Using archetypes provides a great way to enable developers quickly in
a way consistent with best practices employed by your project or
organization. Within the Maven project we use archetypes to try and
get our users up and running as quickly as possible by providing a
sample project that demonstrates many of the features of Maven while
introducing new users to the best practices employed by Maven. In a
matter of seconds a new user can have a working Maven project to use
as a jumping board for investigating more of the features in Maven. We
have also tried to make the Archetype mechanism additive and by that
we mean allowing portions of a project to be captured in an archetype
so that pieces or aspects of a project can be added to existing
projects. A good example of this is the Maven site archetype. If, for
example, you have used the quick start archetype to generate a working
project you can then quickly create a site for that project by using
the site archetype within that existing project. You can do anything
like this with archetypes.

You may want to standardize J2EE development within your organization
so you may want to provide archetypes for EJBs, or WARs, or for your
web services. Once these archetypes are created and deployed in your
organization's repository they are available for use by all developers
within your organization.


%package javadoc
Summary: API documentation for %{name}

%description    javadoc
%{summary}.

%package catalog
Summary: Maven Archetype Catalog model

%description catalog
%{summary}.

%package descriptor
Summary: Maven Archetype Descriptor model

%description descriptor
%{summary}.

%package common
Summary: Maven Archetype common classes
# Registry module was obsoleted and removed by upstream F31
Obsoletes: %{name}-registry <= 3.1.1-1

%description common
%{summary}.

%package packaging
Summary: Maven Archetype packaging configuration for archetypes

%description packaging
%{summary}.

%package -n %{name}-plugin
Summary: Maven plug-in for using archetypes

%description -n %{name}-plugin
%{summary}.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1

# Not needed for RPM builds
%pom_remove_plugin -r :apache-rat-plugin
%pom_remove_plugin -r :maven-enforcer-plugin

# Add OSGI info to catalog and descriptor jars
pushd archetype-models/archetype-catalog
    %pom_xpath_remove "pom:project/pom:packaging"
    %pom_xpath_inject "pom:project" "<packaging>bundle</packaging>"
    %pom_xpath_inject "pom:build/pom:plugins" "
      <plugin>
        <groupId>org.apache.felix</groupId>
        <artifactId>maven-bundle-plugin</artifactId>
        <extensions>true</extensions>
        <configuration>
          <instructions>
            <_nouses>true</_nouses>
            <Export-Package>org.apache.maven.archetype.catalog.*</Export-Package>
          </instructions>
        </configuration>
      </plugin>"
popd
pushd archetype-models/archetype-descriptor
    %pom_xpath_remove "pom:project/pom:packaging"
    %pom_xpath_inject "pom:project" "<packaging>bundle</packaging>"
    %pom_xpath_inject "pom:build/pom:plugins" "
      <plugin>
        <groupId>org.apache.felix</groupId>
        <artifactId>maven-bundle-plugin</artifactId>
        <extensions>true</extensions>
        <configuration>
          <instructions>
            <_nouses>true</_nouses>
            <Export-Package>org.apache.maven.archetype.metadata.*</Export-Package>
          </instructions>
        </configuration>
      </plugin>"
popd

# Remove ivy as a runtime dep
%pom_remove_dep org.apache.ivy:ivy archetype-common

# Disable processing of test resources using ant
%pom_remove_plugin org.apache.maven.plugins:maven-antrun-plugin archetype-common

%build
%mvn_package :archetype-models maven-archetype
# Tests are skipped due to missing test dependencies
%mvn_build -f -s -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dsource=1.8 -DdetectJavaApiLink=false

%install
%mvn_install

%files -f .mfiles-maven-archetype
%license LICENSE NOTICE

%files catalog -f .mfiles-archetype-catalog

%files descriptor -f .mfiles-archetype-descriptor

%files common -f .mfiles-archetype-common
%license LICENSE NOTICE

%files packaging -f .mfiles-archetype-packaging

%files -n %{name}-plugin -f .mfiles-maven-archetype-plugin

%files javadoc -f .mfiles-javadoc
%license LICENSE NOTICE

%changelog
* Sun Aug 16 2020 Mat Booth <mat.booth@redhat.com> - 3.2.0-1
- Update to latest upstream release
- Port to commons-lang3

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 13 2020 Mat Booth <mat.booth@redhat.com> - 3.1.2-2
- Allow building against JDK 11

* Thu Jul 09 2020 Mat Booth <mat.booth@redhat.com> - 3.1.2-1
- Update to latest upstream release

* Tue Jul 02 2019 Mat Booth <mat.booth@redhat.com> - 3.1.1-1
- Update to latest upstream release

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Mar 15 2017 Michael Simacek <msimacek@redhat.com> - 2.4-6
- Remove useless rat-plugin

* Thu Feb 16 2017 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.4-5
- Fix license tag

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jun 02 2016 Michael Simacek <msimacek@redhat.com> - 2.4-3
- Port to current plexus-utils

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 24 2015 Michael Simacek <msimacek@redhat.com> - 2.4-1
- Update to upstream version 2.4
- Remove Group tags

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Mar 13 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.3-1
- Update to upstream version 2.3

* Mon Jun  9 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2-5
- Regenerate build-requires
- Resolves: rhbz#1106161

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.2-4
- Use Requires: java-headless rebuild (#1067528)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 2.2-2
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Fri Feb 01 2013 Michal Srb <msrb@redhat.com> - 2.2-1
- Update to upstream version 2.2
- Build with xmvn
- Remove unnecessary depmap and patch

* Thu Aug 09 2012 Gerard Ryan <galileo@fedoraproject.org> - 2.1-7
- Add OSGI info to descriptor.jar

* Tue Aug  7 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.1-6
- Export only proper OSGI packages
- Do not generate "uses" OSGI clauses

* Mon Aug 06 2012 Gerard Ryan <galileo@fedoraproject.org> - 2.1-5
- Fix jetty namespace
- Add OSGI info to catalog.jar

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Sep 20 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.1-2
- Add depmap explanation
- Omit javadoc.sh from javadocs
- Add explicit maven NVR that is needed

* Wed Sep 14 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.1-1
- Initial version of the package

%global release_dir m2e-core-%{version}

Name:           eclipse-m2e-core
Version:        1.16.1
Release:        2%{?dist}
Summary:        Maven integration for Eclipse

# Most of components are under EPL, but some of them are licensed under
# ASL 2.0 license.
License:        EPL-2.0 and ASL 2.0
URL:            https://eclipse.org/m2e/

Source0:        https://github.com/eclipse-m2e/m2e-core/archive/%{version}.tar.gz

# Allow building against the Fedora shipped guava version
Patch0: 0001-Fix-manifests-for-guava-and-use-OSGi-fied-archetypes.patch

# Use latest versions of lucene and maven-indexer
Patch1: 0002-Port-to-latest-versions-of-maven-indexer-and-lucene.patch

# API change in aether (remove once implemented)
Patch2: 0003-Adapt-to-API-change-in-aether.patch

# Remove "mandatory" attirbutes from OSGi manifests, which cause problems with P2.
# See https://dev.eclipse.org/mhonarc/lists/p2-dev/msg05465.html
Patch3: 0004-Remove-mandatory-attirbutes-from-OSGi-manifests-whic.patch

# Use latest version of maven-archetypes
Patch4: 0005-Port-to-latest-version-of-maven-archetypes.patch

# Avoid dep on aether-connector, use java 11 instead
Patch5: 0006-Remove-dep-on-aether-connector.patch

BuildArch:      noarch

# Upstream Eclipse no longer supports non-64bit arches
ExcludeArch: s390 %{arm} %{ix86}

# Maven build-requires for the main build.  After successfull build
# they can be regenerated with the following command:
#   xmvn-builddep <path-to-build-log>
BuildRequires:  java-11-openjdk-devel
BuildRequires:  maven-local
BuildRequires:  mvn(io.takari.m2e.workspace:org.eclipse.m2e.workspace.cli)
BuildRequires:  mvn(org.apache.maven.plugins:maven-install-plugin)
BuildRequires:  mvn(org.codehaus.modello:modello-maven-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.eclipse.tycho.extras:tycho-p2-extras-plugin)
BuildRequires:  mvn(org.eclipse.tycho:target-platform-configuration)
BuildRequires:  mvn(org.eclipse.tycho:tycho-compiler-plugin)
BuildRequires:  mvn(org.eclipse.tycho:tycho-maven-plugin)
BuildRequires:  mvn(org.eclipse.tycho:tycho-p2-plugin)
BuildRequires:  mvn(org.eclipse.tycho:tycho-packaging-plugin)
BuildRequires:  mvn(org.eclipse.tycho:tycho-source-plugin)
BuildRequires:  mvn(org.sonatype.forge:forge-parent:pom:)

# Additional Maven build-requires for m2e-maven-runtime.  They cannot
# be regenerated using xmvn-builddep because m2e-maven-runtime is not
# built using %%mvn_build.
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.archetype:archetype-common) >= 3.2.0
BuildRequires:  mvn(org.apache.maven.indexer:indexer-core) >= 6.0.0
BuildRequires:  mvn(org.apache.maven:maven-compat)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-embedder)
BuildRequires:  mvn(org.apache.maven.resolver:maven-resolver-api)
BuildRequires:  mvn(org.apache.maven.resolver:maven-resolver-connector-basic)
BuildRequires:  mvn(org.apache.maven.resolver:maven-resolver-impl)
BuildRequires:  mvn(org.apache.maven.resolver:maven-resolver-spi)
BuildRequires:  mvn(org.apache.maven.resolver:maven-resolver-transport-wagon)
BuildRequires:  mvn(org.apache.maven.resolver:maven-resolver-util)
BuildRequires:  mvn(org.apache.maven.wagon:wagon-file)
BuildRequires:  mvn(org.apache.maven.wagon:wagon-http)
BuildRequires:  mvn(org.eclipse.sisu:org.eclipse.sisu.plexus)
BuildRequires:  mvn(org.eclipse.tycho:tycho-maven-plugin)
BuildRequires:  mvn(org.eclipse.tycho:tycho-p2-plugin)
BuildRequires:  mvn(org.fusesource.jansi:jansi)
BuildRequires:  mvn(org.slf4j:slf4j-simple)
BuildRequires:  mvn(org.sonatype.plexus:plexus-build-api)

# OSGi build-requires.  They can be regenerated with the following command:
#   sed -n 's/^Require-Bundle: //;T;:l;s/[;=,].*//;/^org.eclipse.m2e/bn;s/..*/BuildRequires:  osgi(&)/;T;p;:n;n;s/^ //;T;bl' `find -name *.MF` | sort -u
BuildRequires:  osgi(com.google.gson)
BuildRequires:  osgi(com.google.guava)
BuildRequires:  osgi(com.ibm.icu)
BuildRequires:  osgi(org.apache.ant)
BuildRequires:  osgi(org.apache.commons.io)
BuildRequires:  osgi(org.apache.maven.archetype.catalog)
BuildRequires:  osgi(org.apache.maven.archetype.descriptor)
BuildRequires:  osgi(org.eclipse.compare)
BuildRequires:  osgi(org.eclipse.core.expressions)
BuildRequires:  osgi(org.eclipse.core.filebuffers)
BuildRequires:  osgi(org.eclipse.core.filesystem)
BuildRequires:  osgi(org.eclipse.core.jobs)
BuildRequires:  osgi(org.eclipse.core.resources)
BuildRequires:  osgi(org.eclipse.core.runtime)
BuildRequires:  osgi(org.eclipse.core.variables)
BuildRequires:  osgi(org.eclipse.debug.core)
BuildRequires:  osgi(org.eclipse.debug.ui)
BuildRequires:  osgi(org.eclipse.emf.common)
BuildRequires:  osgi(org.eclipse.emf.ecore)
BuildRequires:  osgi(org.eclipse.emf.ecore.edit)
BuildRequires:  osgi(org.eclipse.emf.ecore.xmi)
BuildRequires:  osgi(org.eclipse.emf.edit)
BuildRequires:  osgi(org.eclipse.equinox.common)
BuildRequires:  osgi(org.eclipse.equinox.p2.core)
BuildRequires:  osgi(org.eclipse.equinox.p2.discovery)
BuildRequires:  osgi(org.eclipse.equinox.p2.discovery.compatibility)
BuildRequires:  osgi(org.eclipse.equinox.p2.metadata)
BuildRequires:  osgi(org.eclipse.equinox.p2.operations)
BuildRequires:  osgi(org.eclipse.equinox.p2.repository)
BuildRequires:  osgi(org.eclipse.equinox.p2.ui)
BuildRequires:  osgi(org.eclipse.equinox.p2.ui.discovery)
BuildRequires:  osgi(org.eclipse.equinox.registry)
BuildRequires:  osgi(org.eclipse.jdt.core)
BuildRequires:  osgi(org.eclipse.jdt.debug)
BuildRequires:  osgi(org.eclipse.jdt.debug.ui)
BuildRequires:  osgi(org.eclipse.jdt.launching)
BuildRequires:  osgi(org.eclipse.jdt.ui)
BuildRequires:  osgi(org.eclipse.jem.util)
BuildRequires:  osgi(org.eclipse.jetty.http)
BuildRequires:  osgi(org.eclipse.jetty.io)
BuildRequires:  osgi(org.eclipse.jetty.security)
BuildRequires:  osgi(org.eclipse.jetty.server)
BuildRequires:  osgi(org.eclipse.jetty.util)
BuildRequires:  osgi(org.eclipse.jface)
BuildRequires:  osgi(org.eclipse.jface.text)
BuildRequires:  osgi(org.eclipse.license) < 2.0.0
BuildRequires:  osgi(org.eclipse.ltk.core.refactoring)
BuildRequires:  osgi(org.eclipse.ltk.ui.refactoring)
BuildRequires:  osgi(org.eclipse.osgi)
BuildRequires:  osgi(org.eclipse.search)
BuildRequires:  osgi(org.eclipse.swt)
BuildRequires:  osgi(org.eclipse.ui)
BuildRequires:  osgi(org.eclipse.ui.console)
BuildRequires:  osgi(org.eclipse.ui.editors)
BuildRequires:  osgi(org.eclipse.ui.externaltools)
BuildRequires:  osgi(org.eclipse.ui.forms)
BuildRequires:  osgi(org.eclipse.ui.ide)
BuildRequires:  osgi(org.eclipse.ui.views)
BuildRequires:  osgi(org.eclipse.ui.workbench)
BuildRequires:  osgi(org.eclipse.ui.workbench.texteditor)
BuildRequires:  osgi(org.eclipse.wst.common.emf)
BuildRequires:  osgi(org.eclipse.wst.common.uriresolver)
BuildRequires:  osgi(org.eclipse.wst.sse.core)
BuildRequires:  osgi(org.eclipse.wst.sse.ui)
BuildRequires:  osgi(org.eclipse.wst.xml.core)
BuildRequires:  osgi(org.eclipse.wst.xml.ui)
BuildRequires:  osgi(org.eclipse.wst.xsd.core)
BuildRequires:  osgi(org.junit)

# Maven POM doesn't require maven-parent
BuildRequires:  maven-parent

# Install plugin is invoked explicitly from the spec file
BuildRequires:  maven-install-plugin

# Bundle requires are auto-generated, but explicit requires are needed
# for symlinks to JARs installed by other packages.  After installing
# m2e these requires can be regenerated with the following command:
#   rpm -qf --qf 'Requires:       %%{name}\n' $(readlink -f $(find /usr/share/eclipse/droplets/m2e-core -type l)) | sort -u
Requires:       aopalliance
Requires:       apache-commons-cli
Requires:       apache-commons-codec
Requires:       apache-commons-collections
Requires:       apache-commons-io
Requires:       apache-commons-lang3
Requires:       atinject
Requires:       cdi-api
Requires:       eclipse-m2e-workspace
Requires:       glassfish-el-api
Requires:       google-gson
Requires:       google-guice
Requires:       hawtjni-runtime
Requires:       jansi
Requires:       jansi-native
Requires:       jchardet
Requires:       jdom
Requires:       lucene-highlighter
Requires:       lucene-memory
Requires:       lucene-queries
Requires:       lucene-queryparser
Requires:       lucene-sandbox
Requires:       maven-archetype-catalog >= 3.2.0
Requires:       maven-archetype-common >= 3.2.0
Requires:       maven-archetype-descriptor >= 3.2.0
Requires:       maven-artifact-transfer
Requires:       maven-common-artifact-filters
Requires:       maven-indexer >= 6.0.0
Requires:       maven-invoker
Requires:       maven-lib
Requires:       maven-resolver-api
Requires:       maven-resolver-connector-basic
Requires:       maven-resolver-impl
Requires:       maven-resolver-spi
Requires:       maven-resolver-transport-wagon
Requires:       maven-resolver-util
Requires:       maven-shared-utils
Requires:       maven-wagon-file
Requires:       maven-wagon-http
Requires:       maven-wagon-provider-api
Requires:       plexus-build-api
Requires:       plexus-cipher
Requires:       plexus-classworlds
Requires:       plexus-containers-component-annotations
Requires:       plexus-interpolation
Requires:       plexus-sec-dispatcher
Requires:       plexus-utils
Requires:       plexus-velocity
Requires:       sisu-inject
Requires:       sisu-plexus
Requires:       slf4j
Requires:       velocity
Requires:       xml-commons-apis

# Obsoletes added for F31
Obsoletes: eclipse-m2e-sourcelookup < 1.1.1-1
Provides: eclipse-m2e-sourcelookup = %{version}-%{release}

# Not shipping tests or javadoc since F33
Obsoletes: %{name}-javadoc < 1.16.1-1
Obsoletes: %{name}-tests < 1.16.1-1

%description
The goal of the m2ec project is to provide a first-class Apache Maven support
in the Eclipse IDE, making it easier to edit Maven's pom.xml, run a build from
the IDE and much more. For Java developers, the very tight integration with JDT
greatly simplifies the consumption of Java artifacts either being hosted on open
source repositories such as Maven Central, or in your in-house Maven repository.

m2e is also a platform that let others provide better integration with
additional Maven plugins (e.g. Android, web development, etc.), and facilitates
the distribution of those extensions through the m2e marketplace.


%prep
%setup -q -n %{release_dir}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
rm org.eclipse.m2e.core.ui/src/org/eclipse/m2e/core/ui/internal/preferences/LocalArchetypeCatalogDialog.java
rm org.eclipse.m2e.core.ui/src/org/eclipse/m2e/core/ui/internal/preferences/RemoteArchetypeCatalogDialog.java
%pom_remove_dep :dom4j m2e-maven-runtime/org.eclipse.m2e.archetype.common
%patch5 -p1

# Remove unnecessary parent pom
%pom_remove_parent m2e-maven-runtime

find -name '*.class' -delete
find -name '*.jar' -delete

# Copy license files so they can be installed more easily.
cp -p org.eclipse.m2e.core/about_files/LICENSE-2.0.txt .

# These don't currently build, but don't seem to be absolutely necessary
for mod in org.eclipse.m2e.logback.appender \
           org.eclipse.m2e.logback.configuration \
           org.eclipse.m2e.logback.feature \
           org.eclipse.m2e.sdk.feature \
           org.eclipse.m2e.site
do
  %pom_disable_module $mod
  rm -rf $mod
done

# Don't build lemminx editor
%pom_disable_module org.eclipse.m2e.lemminx.feature
%pom_disable_module org.eclipse.m2e.editor.lemminx
%pom_disable_module org.eclipse.m2e.editor.lemminx.tests

# Don't ship tests
%pom_disable_module org.eclipse.m2e.tests.common
%pom_disable_module org.eclipse.m2e.core.tests
%pom_disable_module org.eclipse.m2e.jdt.tests
%pom_disable_module org.eclipse.m2e.editor.xml.sse.tests
%pom_disable_module org.eclipse.m2e.importer.tests
%pom_disable_module org.eclipse.m2e.binaryproject.tests
%mvn_package ":*.tests*::{}:" __noinstall
%mvn_package ":::{}:"

# Ensure all necessary resolver deps are present
pushd m2e-maven-runtime/org.eclipse.m2e.maven.runtime
%pom_remove_dep "org.apache.maven.resolver:"
%pom_add_dep "org.apache.maven.resolver:maven-resolver-api:1.1.0"
%pom_add_dep "org.apache.maven.resolver:maven-resolver-impl:1.1.0"
%pom_add_dep "org.apache.maven.resolver:maven-resolver-connector-basic:1.1.0"
%pom_add_dep "org.apache.maven.resolver:maven-resolver-spi:1.1.0"
%pom_add_dep "org.apache.maven.resolver:maven-resolver-transport-wagon:1.1.0"
%pom_add_dep "org.apache.maven.resolver:maven-resolver-util:1.1.0"
popd

# Embed all Maven dependencies.  They may be some superflous deps
# added this way, but in Fedora we don't have enough manpower to test
# dependency correctness.  And we don't even run m2e tests...
# Except for lucene and asm, avoid embedding that because of problems
for d in `find m2e-maven-runtime/* -maxdepth 0 -type d`; do
    %pom_xpath_inject pom:instructions "<Embed-Directory>jars</Embed-Directory>" $d
    %pom_xpath_set pom:Embed-Dependency "*;scope=compile|runtime;groupId=!org.apache.lucene|org.ow2.asm" $d
done

# Not needed for RPM builds
%pom_remove_plugin ":jacoco-maven-plugin"
%pom_remove_dep :tycho-buildtimestamp-jgit
%pom_remove_dep :tycho-sourceref-jgit
%pom_xpath_remove 'pom:configuration/pom:timestampProvider'
%pom_xpath_remove 'pom:configuration/pom:sourceReferences'
%pom_remove_plugin ":exec-maven-plugin" m2e-maven-runtime
%pom_remove_plugin ":properties-maven-plugin" m2e-maven-runtime

# Specify a guava version
sed -i -e '/com.google.guava/a<version>20.0</version>' \
  m2e-maven-runtime/org.eclipse.m2e.maven.runtime/pom.xml

# Avoid embedding lucene, use as ordinary OSGi bundle instead
sed -i -e '/org.slf4j/s|^\(.*\)|\1,org.apache.lucene.analysis,org.apache.lucene.analysis.standard,org.apache.lucene.analysis.util,org.apache.lucene.document,org.apache.lucene.index,org.apache.lucene.queryparser.classic,org.apache.lucene.search,org.apache.lucene.search.highlight,org.apache.lucene.store,org.apache.lucene.util|' \
  org.eclipse.m2e.core/META-INF/MANIFEST.MF org.eclipse.m2e.core.ui/META-INF/MANIFEST.MF

%build
export JAVA_HOME=%{_jvmdir}/java-11
# Building m2e is a two step process.  See upstream documentation:
# http://wiki.eclipse.org/M2E_Development_Environment#Building_m2e_on_command_line
repo=localrepo
pushd m2e-maven-runtime
xmvn -B -o package org.fedoraproject.xmvn:xmvn-mojo:builddep -Dmaven.repo.local=../${repo}
popd
# Manually install the first stage (don't rely on felix OBR)
mkdir tmp && pushd tmp
for aid in org.eclipse.m2e.archetype.common \
           org.eclipse.m2e.maven.indexer \
           org.eclipse.m2e.maven.runtime \
           org.eclipse.m2e.maven.runtime.slf4j.simple ; do
  xmvn -B -o install:install-file -DgroupId=org.eclipse.m2e -DartifactId=$aid -Dversion=1.16.0-SNAPSHOT -Dpackaging=jar \
    -Dmaven.repo.local=../${repo} -Dfile=../m2e-maven-runtime/$aid/target/$aid-1.16.0-SNAPSHOT.jar
done
popd
# Second stage build
%mvn_build -j -f -- -Dmaven.repo.local=${repo} -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8

%install
%mvn_artifact m2e-maven-runtime/$mod/pom.xml
for mod in org.eclipse.m2e.archetype.common \
           org.eclipse.m2e.maven.indexer \
           org.eclipse.m2e.maven.runtime \
           org.eclipse.m2e.maven.runtime.slf4j.simple
do
    %mvn_artifact -Dtype=eclipse-plugin m2e-maven-runtime/$mod/pom.xml m2e-maven-runtime/$mod/target/$mod-1.16.0-SNAPSHOT.jar
done

%mvn_install

# Replace bundled JARs with symlinks to system JARs using XMvn Subst.  This way
# there is no need to manually synchronize JAR lists between Maven and M2E when
# some Maven dependency changes.  All that needs to be done is rebuilding M2E.
xmvn-subst -s $(find %{buildroot}%{_datadir}/eclipse/droplets/m2e-core -name jars)

%files -f .mfiles
%license LICENSE-2.0.txt

%changelog
* Sun Aug 16 2020 Mat Booth <mat.booth@redhat.com> - 1.16.1-2
- Rebuild against maven-archetype/commons-lang3
- Regenerate Rs/BRs

* Fri Aug 14 2020 Mat Booth <mat.booth@redhat.com> - 1.16.1-1
- Update to latest upstream release

* Thu Aug 06 2020 Mat Booth <mat.booth@redhat.com> - 1.16.0-7
- Fix broken requires

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 16 2020 Mat Booth <mat.booth@redhat.com> - 1.16.0-5
- Remove explicit BR on javax.annotation-api, since Eclipse platform will pull
  in either the javax or jakarta version as required

* Mon Jul 13 2020 Jiri Vanek <jvanek@redhat.com> - 1.16.0-4
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Mon Jul 13 2020 Mat Booth <mat.booth@redhat.com> - 1.16.0-3
- Patch out dep on aether and obsolete javadoc package

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 1.16.0-2
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Thu Jun 25 2020 Mat Booth <mat.booth@redhat.com> - 1.16.0-1
- Update to latest upstream release

* Wed Apr 01 2020 Mat Booth <mat.booth@redhat.com> - 1.15.0-3
- Add patch to fix NoClassDefFoundErrors

* Wed Mar 25 2020 Mat Booth <mat.booth@redhat.com> - 1.15.0-2
- Improve archetype patch

* Sun Mar 22 2020 Mat Booth <mat.booth@redhat.com> - 1.15.0-1
- Update to latest upstream release

* Tue Jan 07 2020 Mat Booth <mat.booth@redhat.com> - 1.14.0-2
- Correctly obsolete tests

* Fri Dec 20 2019 Mat Booth <mat.booth@redhat.com> - 1.14.0-1
- Update to latest upstream release
- Don't build and ship tests

* Thu Aug 01 2019 Mat Booth <mat.booth@redhat.com> - 1.11.0-8
- Rebuild against new maven-archetype and regenerate runtime requires

* Tue Jul 02 2019 Mat Booth <mat.booth@redhat.com> - 1.11.0-7
- Re-generate OSGi BRs

* Mon Jul 01 2019 Mat Booth <mat.booth@redhat.com> - 1.11.0-6
- Drop hard requirement on xbean, not really needed by maven

* Fri Jun 21 2019 Mat Booth <mat.booth@redhat.com> - 1.11.0-5
- Backport fix to correct 'Failed to evaluate: ReferenceExpression' errors in
  log

* Tue Jun 18 2019 Mat Booth <mat.booth@redhat.com> - 1.11.0-4
- Rebuild against maven-indexer 6.0

* Wed Jun 12 2019 Mat Booth <mat.booth@redhat.com> - 1.11.0-3
- Add obsoletes for eclipse-m2e-sourcelookup

* Wed Jun 12 2019 Mat Booth <mat.booth@redhat.com> - 1.11.0-2
- Fix build against modularised maven-resolver

* Fri Mar 15 2019 Mat Booth <mat.booth@redhat.com> - 1.11.0-1
- Update to 2019-03 release
- Restrict to same architectures as Eclipse itself
- Fix bundle name of annotations-api

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 12 2018 Mat Booth <mat.booth@redhat.com> - 1.10.0-1
- Update to 2018-12 release
- Patch for latest version of maven-resolver

* Wed Sep 12 2018 Mat Booth <mat.booth@redhat.com> - 1.9.1-2
- Add BR/R on maven-wagon-http

* Wed Sep 12 2018 Mat Booth <mat.booth@redhat.com> - 1.9.1-1
- Update to latest release

* Thu Aug 23 2018 Mat Booth <mat.booth@redhat.com> - 1.9.1-0.1
- Update to latest snapshot

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 20 2018 Mat Booth <mat.booth@redhat.com> - 1.9.0-1
- Update to Photon release

* Thu Apr 19 2018 Mat Booth <mat.booth@redhat.com> - 1.8.3-0.3.git1255fb5
- Fix dep on okhttp connector
- Don't bundle asm in indexer to avoid generating a dep on java 9

* Wed Apr 18 2018 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.8.3-0.2.git1255fb5
- Switch from aether to maven-resolver Requires

* Tue Mar 20 2018 Mat Booth <mat.booth@redhat.com> - 1.8.3-0.1.git1255fb5
- Update to 1.8.3 snapshot

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Nov 24 2017 Mat Booth <mat.booth@redhat.com> - 1.8.2-2
- Use autosetup with autopatch macro

* Wed Oct 18 2017 Mat Booth <mat.booth@redhat.com> - 1.8.2-1
- Update to 1.8.2

* Mon Sep 11 2017 Mat Booth <mat.booth@redhat.com> - 1.8.1-1
- Update to latest upstream release

* Tue Aug 08 2017 Mat Booth <mat.booth@redhat.com> - 1.8.0-3
- Rebuild against newer maven-indexer

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 27 2017 Mat Booth <mat.booth@redhat.com> - 1.8.0-1
- Update to final Oxygen release
- Update lucene patch

* Wed May 31 2017 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.7.1-0.4.git3aeac6a
- Add missing build-requires on maven-install-plugin

* Fri Feb 10 2017 Mat Booth <mat.booth@redhat.com> - 1.7.1-0.3.git3aeac6a
- Rebuild against new maven-indexer
- Port tests to latest jetty to drop dep on obsolete jetty8
- Port to latest lucene and use from OSGi instead of embedding
- Organise patches

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-0.2.git3aeac6a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 20 2017 Mat Booth <mat.booth@redhat.com> - 1.7.1-0.1.git3aeac6a
- Update to 1.7.1 snapshot to get slf4j fixes

* Fri Dec 02 2016 Mat Booth <mat.booth@redhat.com> - 1.7.0-1
- Update to latest release
- Re-generate runtime requires

* Wed Jun 15 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.6.2-6
- Add missing build-requires

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Dec 14 2015 Gerard Ryan <galileo@fedoraproject.org> - 1.6.2-4
- Force minimum maven-indexer Requires

* Sat Dec 12 2015 Gerard Ryan <galileo@fedoraproject.org> - 1.6.2-3
- Update for new maven-indexer build (lucene3)

* Wed Oct 14 2015 Mat Booth <mat.booth@redhat.com> - 1.6.2-2
- Rebuild for new eclipse-m2e-workspace

* Sun Sep 13 2015 Gerard Ryan <galileo@fedoraproject.org> - 1.6.2-1
- Update to upstream 1.6.2 release.

* Fri Sep 04 2015 Roland Grunberg <rgrunber@redhat.com> - 1.6.1-2
- Minor changes to build as a droplet.

* Wed Jul 8 2015 Alexander Kurtakov <akurtako@redhat.com> 1.6.1-1
- Update to upstram 1.6.1 release.
- Port to Lucene 5 API.

* Mon Jun 22 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.6.0-1
- Update to upstream release 1.6.0 (Mars)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-0.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu May 14 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.6.0-0.3
- Update to upstream milestone 1.6.0.20150506-1605

* Mon Mar 16 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.6.0-0.2
- Remove "mandatory" attirbutes from OSGi manifests

* Thu Feb 19 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.6.0-0.1
- Update to upstream milestone 1.6.0.20150203-1921

* Mon Feb  9 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.5.0-18
- Enable test bundle

* Sat Feb  7 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.5.0-17
- Install runtime bundles in dropins directory

* Fri Dec 12 2014 Roland Grunberg <rgrunber@redhat.com> - 1.5.0-16
- Fix FTBFS by removing unnecessary type attribute.

* Thu Sep 18 2014 Michal Srb <msrb@redhat.com> - 1.5.0-15
- Rebuild to fix metadata

* Wed Sep 10 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.5.0-14
- Install with XMvn

* Sun Aug 31 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.5.0-14
- Rebuild for Maven 3.2.3

* Sat Jul 05 2014 Gerard Ryan <galileo@fedoraproject.org> - 1.5.0-13
- Symlink guava so bundles can get resolved

* Fri Jun 27 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.5.0-12
- Update to final 1.5.0 (Luna)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 30 2014 Gerard Ryan <galileo@fedoraproject.org> - 1.5.0-10
- Replace old BR on tesla-concurrent-localrepo

* Thu May 29 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.5.0-9
- Regenerate requires and build-requires, again

* Thu May 29 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.5.0-8
- Regenerate requires and build-requires

* Sun May 25 2014 Gerard Ryan <galileo@fedoraproject.org> - 1.5.0-7
- Update to latest upstream 1.5.0 milestone

* Fri May 23 2014 Gerard Ryan <galileo@fedoraproject.org> - 1.5.0-6
- Rebuild for plexus-velocity update

* Sat Mar 22 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.5.0-5
- Add explicit requires, resolves: rhbz#1079458
- Regenerate build-requires
- Rename dropin installation dir to m2e-core
- Simplify patch application with %%autopatch macro
- Use %%mvn_build and %%mvn_install macros
- Use feclipse-maven-plugin to simplify bundle installation
- Embed all dependencies in m2e-maven-runtime bundles

* Sat Mar 15 2014 Gerard Ryan <galileo@fedoraproject.org> - 1.5.0-4
- Use xmvn instead of mvn-rpmbuild

* Fri Mar 14 2014 Gerard Ryan <galileo@fedoraproject.org> - 1.5.0-3
- Patch for lucene API changes

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.5.0-2
- Use Requires: java-headless rebuild (#1067528)

* Mon Jan 27 2014 Gerard Ryan <galileo@fedoraproject.org> - 1.5.0-1
- Update to 1.5.0-SNAPSHOT

* Mon Jan 27 2014 Gerard Ryan <galileo@fedoraproject.org> - 1.4.0-13
- Fix for RHBZ#1015324: Failing to retrieve archetypes

* Thu Jan 23 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4.0-12
- Switch to netty3 compat package

* Sat Jan  4 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4.0-11
- Fully remove CGlib from Maven runtime bundle
- Exclude AOP version of Guice from Sisu dependencies
- Fix Sisu dependency scope

* Thu Jan 02 2014 Gerard Ryan <galileo@fedoraproject.org> - 1.4.0-10
- Revert removal of workaround for missing cglib and aopalliance

* Tue Dec 31 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4.0-9
- Remove workaround for rhbz#911365 (missing cglib and aopalliance)
- Add NOP SLF4J implementation JAR to classpath
- Use xmvn-subst to symlink JARs, resolves: rhbz#1020299

* Wed Dec 04 2013 Gerard Ryan <galileo@fedoraproject.org> - 1.4.0-8
- Rebuild in Rawhide

* Wed Oct 02 2013 Roland Grunberg <rgrunber@redhat.com> - 1.4.0-7
- Fix bug with plexus-utils > 3.0.5.

* Tue Oct 01 2013 Gerard Ryan <galileo@fedoraproject.org> - 1.4.0-6
- Add BR/R on aether-connector-basic in f20+

* Sun Sep 29 2013 Gerard Ryan <galileo@fedoraproject.org> - 1.4.0-5
- Fixes for maven 3.1.0

* Sat Aug 24 2013 Gerard Ryan <galileo@fedoraproject.org> - 1.4.0-4
- Bump release to rebuild in rawhide/f20

* Mon Aug 19 2013 Gerard Ryan <galileo@fedoraproject.org> - 1.4.0-3
- Use Eclipse Sisu and Eclipse Aether
- Add patch for new maven-indexer

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jun 25 2013 Gerard Ryan <galileo@fedoraproject.org> - 1.4.0-1
- Update to latest upstream version 1.4.0

* Tue May 14 2013 Gerard Ryan <galileo@fedoraproject.org> - 1.3.1-2
- Fix broken symbolic links on f19+
- Update Requires/BuildRequires

* Sun Apr 07 2013 Gerard Ryan <galileo@fedoraproject.org> - 1.3.1-1
- Update to upstream version 1.3.1

* Wed Feb 20 2013 Gerard Ryan <galileo@fedoraproject.org> - 1.2.0-7
- Bump release to test again in koji (previously broken deps)

* Mon Feb 18 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2.0-6
- Drop dependency on plexus-container-default
- Resolves: rhbz#912311

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.2.0-5
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Wed Jan 30 2013 Gerard Ryan <galileo@fedoraproject.org> - 1.2.0-4
- Update min versions of eclipse and eclipse-emf

* Thu Jan 24 2013 Gerard Ryan <galileo@fedoraproject.org> - 1.2.0-3
- Fix incorrect changelog entry dates.

* Tue Jan 22 2013 Gerard Ryan <galileo@fedoraproject.org> - 1.2.0-2
- Remove javadoc.sh file from javadoc subpackage.
- Fix URL for source0.

* Tue Dec 11 2012 Gerard Ryan <galileo@fedoraproject.org> - 1.2.0-1
- Bump to a more sane release number

* Tue Dec 11 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2.0-0.3
- Add javadoc subpackage
- Fix licensing

* Tue Dec 11 2012 Gerard Ryan <galileo@fedoraproject.org> - 1.2.0-0.2
- Require org.apache.maven.archetype.descriptor in OSGi for m2e.core.

* Mon Dec 10 2012 Gerard Ryan <galileo@fedoraproject.org> - 1.2.0-0.1
- Attempt update to upstream 1.2.0

* Mon Dec 10 2012 Gerard Ryan <galileo@fedoraproject.org> - 1.1.0-4
- Force usage of sisu over plexus-containers for DefaultPlexusContainer.

* Thu Dec 06 2012 Gerard Ryan <galileo@fedoraproject.org> - 1.1.0-3
- Add cglib and aopalliance as embedded dependencies.
- Use newer pom macro to add netty dependency.
- Add cglib and aopalliance as dependencies in org.eclipse.m2e.maven.runtime.
- Symlink catalog and descriptor jars from maven-archetype.
- Remove symlink to plexus-container-default.jar, fix sisu-guice.jar link.

* Fri Aug 10 2012 Gerard Ryan <galileo@fedoraproject.org> - 1.1.0-2
- Fix sources.

* Sun Aug 05 2012 Gerard Ryan <galileo@fedoraproject.org> - 1.1.0-1
- Initial packaging.

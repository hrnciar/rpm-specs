# Tycho depends on itself, and Eclipse to build but in certain cases these
# requirements may not be satisfiable then building Tycho becomes problematic.
# For example:
# * A library (in Fedora) used by Tycho's runtime broke API and so Tycho
#   from the buildroot is broken
# * Building into a new distro or buildroot, where neither Tycho nor Eclipse
#   is available yet and we need to build Tycho before building Eclipse
# In bootstrap mode, javac and plain xmvn are used to build a subset of
# Tycho such that it can build a bootstrap mode Eclipse and subsequently
# fully rebuild itself. In this mode, there may be reduced functionality,
# so a full non-bootstrap mode build should always be done afterwards.
%bcond_with bootstrap

# Allow conditionally building without Junit 5 support
%bcond_with junit5

# Release tags or git SHAs
%global git_tag tycho-%{version}
%global fp_p2_git_tag 290f67a4c717599b2f5166ea89aa5365571314b1

%global fp_p2_version 0.0.1
%global fp_p2_snap -SNAPSHOT

# The location of the xmvn dir into which we need to install the xmvn plugin
%global xmvn_libdir %(realpath $(dirname $(readlink -f $(which xmvn)))/../lib)

%define __requires_exclude osgi*

Name:           tycho
Version:        1.6.0
Release:        6%{?dist}
Summary:        Plugins and extensions for building Eclipse plugins and OSGI bundles with Maven

# license file is missing but all files having some licensing information are ASL 2.0
License:        ASL 2.0 and EPL-1.0
URL:            http://eclipse.org/tycho

# Tycho project source
Source0:        http://git.eclipse.org/c/tycho/org.eclipse.tycho.git/snapshot/org.eclipse.tycho-%{git_tag}.tar.xz
# Eclipse Plugin Project supporting filesystem as p2 repository
Source1:        https://github.com/rgrunber/fedoraproject-p2/archive/%{fp_p2_git_tag}/fedoraproject-p2-%{fp_p2_git_tag}.tar.gz

# this is a workaround for maven-plugin-plugin changes that happened after
# version 2.4.3 (impossible to have empty mojo created as aggregate). This
# should be fixed upstream properly
Source2:        EmptyMojo.java
Source3:        tycho-scripts.sh
Source4:        tycho-bootstrap.sh
Source5:        tycho-debundle.sh
# Script that can be used to install or simulate installation of P2
# artifacts. It is used in OSGi requires generation.
Source6:        p2-install.sh

# Fedora Eclipse bundles needed to build Tycho when Eclipse is not present
# or when the Eclipse that is present is not compatible
%if %{with bootstrap}
Source10:       eclipse-bootstrap-2019-12.tar.xz
%endif

# Fedora-specific patches
Patch0:         0001-Fix-the-Tycho-build-to-work-on-Fedora.patch
Patch1:         0002-Implement-a-custom-resolver-for-Tycho-in-local-mode.patch
Patch2:         0003-Tycho-should-always-delegate-artifact-resolution-to-.patch
Patch7:         0008-Use-custom-resolver-for-tycho-eclipserun-plugin.patch
# Submitted upstream: https://bugs.eclipse.org/bugs/show_bug.cgi?id=537963
Patch3:         0004-Bug-537963-Make-the-default-EE-Java-1.8.patch
# Fix compile error with uncaught exception
Patch4:         0005-Fix-uncaught-exception.patch
# Fix mis-scoped test deps, see: ebz#560394
Patch5:         0006-Mockito-does-not-have-test-scope.patch
# Fix incorrect generated requires
Patch6:         0007-Fix-dependency-problems-when-bootstrapping-with-extr.patch

# Upstream Eclipse no longer supports non-64bit arches
ExcludeArch: s390 %{arm} %{ix86}

BuildArch:      noarch

# Extras was folded into the main tycho package in F31
Obsoletes: tycho-extras < 1.6.0-1
Provides:  tycho-extras = %{version}-%{release}

BuildRequires:  maven-local
BuildRequires:  mvn(biz.aQute.bnd:bnd-maven-plugin)
BuildRequires:  mvn(com.beust:jcommander)
BuildRequires:  mvn(de.pdark:decentxml)
BuildRequires:  mvn(io.takari.polyglot:polyglot-common)
BuildRequires:  mvn(org.apache.commons:commons-compress)
BuildRequires:  mvn(org.apache.commons:commons-exec)
BuildRequires:  mvn(org.apache.commons:commons-lang3)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven:maven-archiver)
BuildRequires:  mvn(org.apache.maven:maven-compat)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-model)
BuildRequires:  mvn(org.apache.maven:maven-model-builder)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven.plugins:maven-clean-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-install-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.surefire:maven-surefire-common)
BuildRequires:  mvn(org.apache.maven.surefire:surefire-api)
BuildRequires:  mvn(org.codehaus.plexus:plexus-archiver)
BuildRequires:  mvn(org.codehaus.plexus:plexus-compiler-api)
BuildRequires:  mvn(org.codehaus.plexus:plexus-compiler-manager)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-annotations)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.eclipse.jdt:ecj)
BuildRequires:  mvn(org.eclipse.sisu:org.eclipse.sisu.plexus)
BuildRequires:  mvn(org.fedoraproject.xmvn:xmvn-api)
BuildRequires:  mvn(org.fedoraproject.xmvn:xmvn-core)
BuildRequires:  mvn(org.fedoraproject.xmvn:xmvn-install)
BuildRequires:  mvn(org.fedoraproject.xmvn:xmvn-parent:pom:)
BuildRequires:  mvn(org.ow2.asm:asm-tree)
BuildRequires:  mvn(org.ow2.asm:asm-util)
BuildRequires:  mvn(org.slf4j:slf4j-api)
BuildRequires:  mvn(org.slf4j:slf4j-simple)
%if %{with junit5}
BuildRequires:  mvn(org.apache.maven.surefire:surefire-junit-platform)
BuildRequires:  mvn(org.apiguardian:apiguardian-api)
BuildRequires:  mvn(org.opentest4j:opentest4j)
%endif

%if ! %{with bootstrap}
# Ordinarily Tycho additionally requires itself and Eclipse to build
BuildRequires:  %{name}
BuildRequires:  eclipse-platform >= 1:4.11
%else
# For bootstrapping, we just need the dependencies of the Eclipse bundles we use
BuildRequires:  osgi(com.ibm.icu)
BuildRequires:  osgi(org.apache.commons.jxpath)
BuildRequires:  osgi(org.apache.batik.css)
BuildRequires:  osgi(org.apache.felix.scr)
BuildRequires:  osgi(org.sat4j.core)
BuildRequires:  osgi(org.sat4j.pb)
BuildRequires:  osgi(org.w3c.css.sac)
%endif

Requires:       maven-local
Requires:       xmvn-minimal
Requires:       ecj

%if ! %{with bootstrap}
Requires:       eclipse-platform >= 1:4.11
%endif

# maven-clean-plugin is bound to "initialize" Maven phase for
# "eclipse-repository" projects
Requires:       maven-clean-plugin

%description
Tycho is a set of Maven plugins and extensions for building Eclipse
plugins and OSGI bundles with Maven. Eclipse plugins and OSGI bundles
have their own metadata for expressing dependencies, source folder
locations, etc. that are normally found in a Maven POM. Tycho uses
native metadata for Eclipse plugins and OSGi bundles and uses the POM
to configure and drive the build. Tycho supports bundles, fragments,
features, update site projects and RCP applications. Tycho also knows
how to run JUnit test plugins using OSGi runtime and there is also
support for sharing build results using Maven artifact repositories.

Tycho plugins introduce new packaging types and the corresponding
lifecycle bindings that allow Maven to use OSGi and Eclipse metadata
during a Maven build. OSGi rules are used to resolve project
dependencies and package visibility restrictions are honored by the
OSGi-aware JDT-based compiler plugin. Tycho will use OSGi metadata and
OSGi rules to calculate project dependencies dynamically and injects
them into the Maven project model at build time. Tycho supports all
attributes supported by the Eclipse OSGi resolver (Require-Bundle,
Import-Package, Eclipse-GenericRequire, etc). Tycho will use proper
classpath access rules during compilation. Tycho supports all project
types supported by PDE and will use PDE/JDT project metadata where
possible. One important design goal in Tycho is to make sure there is
no duplication of metadata between POM and OSGi metadata.

%package javadoc
Summary: Javadocs for %{name}
# Extras was folded into the main tycho package in F31
Obsoletes: tycho-extras-javadoc < 1.6.0-1
Provides:  tycho-extras-javadoc = %{version}-%{release}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n org.eclipse.tycho-%{git_tag} -a 1
mv fedoraproject-p2-%{fp_p2_git_tag} fedoraproject-p2

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

# Unneeded for RPM builds
%pom_remove_plugin :maven-site-plugin

# These tycho plug-ins don't make sense in the context of RPM builds of Eclipse plug-ins
%pom_disable_module tycho-buildtimestamp-jgit tycho-extras
%pom_disable_module tycho-sourceref-jgit tycho-extras

%if %{without junit5}
%pom_disable_module org.eclipse.tycho.surefire.junit5 tycho-surefire
%pom_remove_dep ":org.eclipse.tycho.surefire.junit5" tycho-surefire/tycho-surefire-plugin
%endif

# Move from org.sonatype.aether to org.eclipse.aether
find . -name "*.java" | xargs sed -i 's/org.sonatype.aether/org.eclipse.aether/g'
find . -name "*.java" | xargs sed -i 's/org.eclipse.aether.util.DefaultRepositorySystemSession/org.eclipse.aether.DefaultRepositorySystemSession/g'
sed -i 's/public int getPriority/public float getPriority/g' tycho-core/src/main/java/org/eclipse/tycho/core/p2/P2RepositoryConnectorFactory.java

# place empty mojo in place
mkdir -p tycho-maven-plugin/src/main/java/org/fedoraproject
pushd tycho-maven-plugin/src/main/java/org/fedoraproject
cp %{SOURCE2} .
popd

# Homogenise requirement on OSGi bundle
%if %{with bootstrap}
sed -i -e "s/>org.eclipse.platform</>org.eclipse.tycho</" pom.xml tycho-core/pom.xml sisu-equinox/sisu-equinox-embedder/pom.xml
%else
sed -i -e "s/>org.eclipse.tycho</>org.eclipse.platform</" fedoraproject-p2/xmvn-p2-installer-plugin/pom.xml
%endif

# Target platform does not really apply to RPM builds
%pom_disable_module tycho-bundles-target tycho-bundles
%pom_xpath_remove "pom:target" tycho-bundles

# Disable maven-properties-plugin used by tests
%pom_remove_plugin org.sonatype.plugins:maven-properties-plugin tycho-extras/tycho-p2-extras-plugin
# Remove dep on maven tarball used by tests
%pom_remove_dep org.apache.maven:apache-maven tycho-extras/tycho-p2-extras-plugin

# we don't have org.apache.commons:commons-compress:jar:sources
%pom_xpath_remove "pom:dependency[pom:classifier='sources' and pom:artifactId='commons-compress']" tycho-p2/tycho-p2-director-plugin

# Don't build tests
for b in core.shared.tests p2.resolver.impl.test p2.resolver.shared.tests p2.maven.repository.tests p2.tools.tests test.utils ; do
  %pom_disable_module org.eclipse.tycho.$b tycho-bundles
done
%pom_disable_module org.fedoraproject.p2.tests fedoraproject-p2
%pom_disable_module tycho-testing-harness
%pom_remove_dep -r :::test

# Bootstrap Build
%if %{with bootstrap}

# Break circular dep between tycho-lib-detector and tycho-compiler-jdt for bootstrapping
%pom_remove_plugin :maven-compiler-plugin tycho-lib-detector

# Unpack a compatible version of Eclipse we can use to build against
tar -xf %{SOURCE10}
# Install OSGi bundles into local repo to override any incompatible system version
# that may be already installed
pushd bootstrap
for f in usr/lib/eclipse/plugins/org.eclipse.osgi.compatibility.state_*.jar \
         usr/lib/eclipse/plugins/org.eclipse.osgi.services_*.jar \
         usr/lib/eclipse/plugins/org.eclipse.osgi.util_*.jar \
         usr/lib/eclipse/plugins/org.eclipse.osgi_*.jar ; do
  xmvn -o install:install-file -Dfile=$f -Dpackaging=jar -DgroupId=org.eclipse.tycho -Dmaven.repo.local=$(pwd)/../.m2 \
    -DartifactId=$(echo $(basename $f) | cut -d_ -f1) -Dversion=$(echo "${f%.jar}" | cut -d_ -f2)
done
popd

# Perform the 'minimal' (bootstrap) build of Tycho
cp %{SOURCE3} %{SOURCE4} .
./tycho-bootstrap.sh %{version}

# Non-Bootstrap Build
%else

# Set some temporary build version so that the bootstrapped build has
# a different version from the nonbootstrapped. Otherwise there will
# be cyclic dependencies.

sysVer=`grep -C 1 "<artifactId>tycho</artifactId>" %{_mavenpomdir}/tycho/tycho.pom | grep "version" | sed 's/.*>\(.*\)<.*/\1/'`
mkdir boot
sed -e 's/ns[0-9]://g' %{_datadir}/maven-metadata/tycho.xml > boot/tycho-metadata.xml

# Copy Tycho POMs from system repo and set their versions to %%{version}-SNAPSHOT.
for pom in $(grep 'pom</path>' boot/tycho-metadata.xml | sed 's|.*>\(.*\)<.*|\1|'); do
    sed -e "s/>$sysVer/>%{version}-SNAPSHOT/g" -e "s/%{fp_p2_version}%{fp_p2_snap}/%{fp_p2_version}/" <$pom >boot/$(basename $pom)
done

# Update Maven lifecycle mappings for Tycho packaging types provided by tycho-maven-plugin.
cp -p $(build-classpath tycho/tycho-maven-plugin) boot/tycho-maven-plugin.jar
jar xf boot/tycho-maven-plugin.jar META-INF/plexus/components.xml
sed -i s/$sysVer/%{version}-SNAPSHOT/ META-INF/plexus/components.xml
jar uf boot/tycho-maven-plugin.jar META-INF/plexus/components.xml

# Create XMvn metadata for the new JARs and POMs by customizing system Tycho metadata.
sed -i -e 's/xmlns=".*"//' boot/tycho-metadata.xml
%pom_xpath_remove -f "metadata/artifacts/artifact[artifactId='org.eclipse.osgi']" boot/tycho-metadata.xml
%pom_xpath_remove -f "metadata/artifacts/artifact[artifactId='org.eclipse.osgi.util']" boot/tycho-metadata.xml
%pom_xpath_remove -f "metadata/artifacts/artifact[artifactId='org.eclipse.osgi.services']" boot/tycho-metadata.xml
%pom_xpath_remove -f "metadata/artifacts/artifact[artifactId='org.eclipse.osgi.compatibility.state']" boot/tycho-metadata.xml
sed -i '
  s|>/[^<]*/\([^/]*\.pom\)</path>|>'$PWD'/boot/\1</path>|
  s|>'$sysVer'</version>|>%{version}-SNAPSHOT</version><compatVersions><version>%{version}-SNAPSHOT</version></compatVersions>|
  s|>'%{fp_p2_version}%{fp_p2_snap}'</version>|>%{fp_p2_version}</version><compatVersions><version>%{fp_p2_version}</version></compatVersions>|
  s|%{_javadir}/tycho/tycho-maven-plugin.jar|'$PWD'/boot/tycho-maven-plugin.jar|
' boot/tycho-metadata.xml
%mvn_config resolverSettings/metadataRepositories/repository $PWD/boot/tycho-metadata.xml
%endif

# Avoid duplicate execution of clean when generating javadocs, see ebz#399756
%pom_add_plugin :maven-clean-plugin tycho-bundles/tycho-standalone-p2-director "
<executions>
  <execution>
    <id>default-clean-1</id>
    <phase>initialize</phase>
    <configuration>
      <skip>true</skip>
    </configuration>
  </execution>
</executions>"

# Add fp-p2 to main build
%pom_xpath_inject "pom:modules" "<module>fedoraproject-p2</module>"

%build
%mvn_build -f -- \
  -Dtycho-version=%{version}-SNAPSHOT -DtychoBootstrapVersion=%{version}-SNAPSHOT \
  -Dmaven.repo.local=$(pwd)/.m2 -Dfedora.p2.repos=$(pwd)/bootstrap

%mvn_artifact fedoraproject-p2/org.fedoraproject.p2/pom.xml

# Relying on xmvn p2 plugin being present would be a circular dep
# So install as if all artifacts are normal jar files
sed -i -e 's|type>eclipse.*<|type>jar<|' .xmvn-reactor

# Don't package target platform definition files
%mvn_package "::target::" __noinstall

%install
# Get debundling scripts
cp %{SOURCE3} %{SOURCE5} .

%if ! %{with bootstrap}
# Debundle p2 runtime
./tycho-debundle.sh $(pwd)/tycho-bundles/tycho-bundles-external \
  $(pwd)/tycho-bundles/tycho-bundles-external/target/tycho-bundles-external-manifest.txt

# Debundle standalone p2 director
./tycho-debundle.sh $(pwd)/tycho-bundles/tycho-standalone-p2-director
%endif

%if %{with bootstrap}
# Install our own copy of OSGi runtime when bootstrapping to avoid external dep on Eclipse
for b in org.eclipse.osgi \
         org.eclipse.osgi.util \
         org.eclipse.osgi.services \
         org.eclipse.osgi.compatibility.state ; do
  osgiJarPath=$(find .m2/org/eclipse/tycho/$b/*/ -name "*.jar")
  osgiPomPath=$(find .m2/org/eclipse/tycho/$b/*/ -name "*.pom")
  %mvn_artifact $osgiPomPath $osgiJarPath
done
%endif

%mvn_install

%if ! %{with bootstrap}
install -pm 644 tycho-bundles/tycho-bundles-external/target/tycho-bundles-external-manifest.txt %{buildroot}%{_javadir}/tycho
%add_maven_depmap org.eclipse.tycho:tycho-bundles-external:txt:manifest:%{version} tycho/tycho-bundles-external-manifest.txt
%endif

%if %{with bootstrap}
# Misc other bundles needed for bootstrapping
for bnd in \
  core.contenttype \
  core.expressions \
  core.filesystem \
  core.jobs \
  core.net \
  core.resources \
  core.runtime \
  equinox.app \
  equinox.common \
  equinox.concurrent \
  equinox.preferences \
  equinox.registry \
  equinox.security ; do
bndJarPath=$(find bootstrap -name "org.eclipse.${bnd}_*.jar")
install -m 644 -T $bndJarPath $RPM_BUILD_ROOT%{_javadir}/tycho/$bnd.jar
done
%endif

# For some reason fp-p2 is treated as a compat version, this prevents that
# TODO: figure out why
sed -i '/<resolvedVersion>/d' %{buildroot}%{_datadir}/maven-metadata/tycho.xml

# p2-install script
install -dm 755 %{buildroot}%{_javadir}-utils/
install -pm 755 %{SOURCE6} %{buildroot}%{_javadir}-utils/

# Symlink XMvn P2 plugin with all dependencies so that it can be loaded by XMvn
install -dm 755 %{buildroot}%{xmvn_libdir}/installer/
%if %{with bootstrap}
ln -s %{_javadir}/tycho/org.eclipse.osgi.jar %{buildroot}%{xmvn_libdir}/installer/
%else
ln -s %{_javadir}/eclipse/osgi.jar %{buildroot}%{xmvn_libdir}/installer/
%endif
ln -s %{_javadir}/tycho/xmvn-p2-installer-plugin.jar %{buildroot}%{xmvn_libdir}/installer/
ln -s %{_javadir}/tycho/org.fedoraproject.p2.jar %{buildroot}%{xmvn_libdir}/installer/

%files -f .mfiles
%{xmvn_libdir}/installer/*
%{_javadir}-utils/p2-install.sh
%if %{with bootstrap}
%{_javadir}/tycho/core.*.jar
%{_javadir}/tycho/equinox.*.jar
%endif
%doc README.md

%files javadoc -f .mfiles-javadoc

%changelog
* Tue Aug 18 2020 Mat Booth <mat.booth@redhat.com> - 1.6.0-6
- Fix bootstrap mode against Java 11

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 11 2020 Jiri Vanek <jvanek@redhat.com> - 1.6.0-4
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Sat Mar 21 2020 Mat Booth <mat.booth@redhat.com> - 1.6.0-3
- Add missing resolver patch for eclipserun plugin

* Fri Mar 20 2020 Mat Booth <mat.booth@redhat.com> - 1.6.0-2
- Add obsoletes/provides for extras javadoc package

* Wed Feb 19 2020 Mat Booth <mat.booth@redhat.com> - 1.6.0-1
- Update to latest upstream release

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 27 2020 Mat Booth <mat.booth@redhat.com> - 1.5.0-5
- Fix build with Eclipse 4.14

* Thu Jan 23 2020 Mat Booth <mat.booth@redhat.com> - 1.5.0-4
- Remove references to kxml/xpp3

* Wed Dec 18 2019 Mat Booth <mat.booth@redhat.com> - 1.5.0-3
- Full build

* Wed Dec 18 2019 Mat Booth <mat.booth@redhat.com> - 1.5.0-2
- Bootstrap mode

* Tue Dec 17 2019 Mat Booth <mat.booth@redhat.com> - 1.5.0-1
- Update to latest upstream release

* Fri Aug 09 2019 Mat Booth <mat.booth@redhat.com> - 1.4.0-2
- Fix bootstrapping with new ECF

* Fri May 24 2019 Mat Booth <mat.booth@redhat.com> - 1.4.0-1
- Update to latest upstream release

* Tue May 07 2019 Mat Booth <mat.booth@redhat.com> - 1.3.0-5
- Don't build tests, they are not being run anyway

* Mon Mar 11 2019 Mat Booth <mat.booth@redhat.com> - 1.3.0-4
- Debootstrap build
- Restrict to the same architectures as Eclipse itself

* Mon Mar 11 2019 Mat Booth <mat.booth@redhat.com> - 1.3.0-3
- Bootstrap with new felix-scr

* Tue Feb 19 2019 Mat Booth <mat.booth@redhat.com> - 1.3.0-2
- Allow building against ASM 6

* Mon Feb 18 2019 Mat Booth <mat.booth@redhat.com> - 1.3.0-1
- Update to latest upstream release
- Allow conditionally building Junit5 support

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec 13 2018 Mat Booth <mat.booth@redhat.com> - 1.2.0-7
- Fix build against newest Mockito and ASM

* Mon Aug 20 2018 Mat Booth <mat.booth@redhat.com> - 1.2.0-6
- Rebuild against Eclipse 2018-09

* Fri Aug 17 2018 Mat Booth <mat.booth@redhat.com> - 1.2.0-5
- Bootstrap mode improvements
- Patch to use Java 8 as the default target EE, prevents unnecessary dep
  on Java 9

* Wed Jul 25 2018 Mat Booth <mat.booth@redhat.com> - 1.2.0-4
- Fix build against new surefire

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jul 12 2018 Mat Booth <mat.booth@redhat.com> - 1.2.0-2
- Bootstrap build

* Tue Jun 05 2018 Mat Booth <mat.booth@redhat.com> - 1.2.0-1
- Update to latest release for Java 10 support
- Drop upstreamed patch

* Wed May 09 2018 Mat Booth <mat.booth@redhat.com> - 1.2.0-0.5.git5d018bb
- Surefure now used maven-shared-utils instead of plexus-utils, fixes test runs
  in other packages

* Thu May 03 2018 Mat Booth <mat.booth@redhat.com> - 1.2.0-0.4.git5d018bb
- Add a proper patch for ebz#534255

* Wed May 02 2018 Mat Booth <mat.booth@redhat.com> - 1.2.0-0.3.git5d018bb
- Update tycho snapshot and simplify bootstrapping

* Wed May 02 2018 Mat Booth <mat.booth@redhat.com> - 1.2.0-0.2.gitd9ce75d
- Non-bootstrap build

* Mon Apr 30 2018 Mat Booth <mat.booth@redhat.com> - 1.2.0-0.1.gitd9ce75d
- Update to latest tycho snapshot
- Bootstrap build

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Dec 08 2017 Mat Booth <mat.booth@redhat.com> - 1.0.0-10
- Calculate xmvn/lib path, allow building against older and newer surefire

* Wed Oct 11 2017 Mat Booth <mat.booth@redhat.com> - 1.0.0-9
- Port to latest surefire

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 21 2017 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0.0-7
- Update to latest fp-p2 snapshot for XMvn 3.0.0 support

* Tue Jun 20 2017 Mat Booth <mat.booth@redhat.com> - 1.0.0-6
- Improve bootstrap mode

* Sat Jun 17 2017 Mat Booth <mat.booth@redhat.com> - 1.0.0-5
- Debootstrap build

* Sat Jun 17 2017 Mat Booth <mat.booth@redhat.com> - 1.0.0-4
- Add osgi.util bundle to tycho runtime

* Wed May 24 2017 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0.0-3
- Remove no longer needed requires on Maven plugins

* Wed Apr 26 2017 Mat Booth <mat.booth@redhat.com> - 1.0.0-2
- Debootstrap build

* Thu Apr 20 2017 Mat Booth <mat.booth@redhat.com> - 1.0.0-1
- Update to 1.0.0
- Simplify artifact installation
- Tycho 1.0 requires Eclipse Oxygen
- Add felix-scr and deps to tycho-bundles-external

* Thu Apr 20 2017 Mat Booth <mat.booth@redhat.com> - 0.26.0-3
- Fix and enable bootstrap mode

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.26.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Nov 02 2016 Mat Booth <mat.booth@redhat.com> - 0.26.0-1
- Update to latest upstream

* Mon Jul 25 2016 Mat Booth <mat.booth@redhat.com> - 0.25.0-7
- Remove incomplete SCL macros

* Thu Jun 30 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.25.0-6
- Add missing requires on maven-plugin-testing-harness

* Thu Jun 30 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.25.0-5
- Require full xmvn

* Wed Jun 15 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.25.0-4
- Add missing requires on maven-source-plugin

* Fri Apr 22 2016 Mat Booth <mat.booth@redhat.com> - 0.25.0-3
- Require newer ECJ with correct aliases

* Thu Apr 21 2016 Mat Booth <mat.booth@redhat.com> - 0.25.0-2
- Non-bootstrap build against Eclipse Neon

* Wed Apr 20 2016 Mat Booth <mat.booth@redhat.com> - 0.25.0-1
- Update to latest upstream release
- Full bootstrap mode due to incompatibility with Eclipse Mars

* Thu Apr 14 2016 Mat Booth <mat.booth@redhat.com> - 0.23.0-17
- Fix build against new maven-archiver, which removed some deprecated methods
  that tycho was using

* Tue Mar 15 2016 Mat Booth <mat.booth@redhat.com> - 0.23.0-16
- Update to latest fp-p2 snapshot

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.23.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 25 2016 Mat Booth <mat.booth@redhat.com> - 0.23.0-14
- Updates to latest version of fedoraproject-p2.
- fedoraproject-p2: Fix a concurrent modification exception when feature
  plugins have circular deps

* Mon Jan 11 2016 Roland Grunberg <rgrunber@redhat.com> - 0.23.0-13
- Updated to latest version of fedoraproject-p2.
- fedoraproject-p2: Correctly handle splitting virtual packages.

* Mon Jan  4 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.23.0-12
- Update for maven-surefire 2.19.1

* Mon Oct 26 2015 Roland Grunberg <rgrunber@redhat.com> - 0.23.0-11
- Fix bug in org.eclipse.tycho.surefire.junit4 provider.

* Tue Oct 20 2015 Roland Grunberg <rgrunber@redhat.com> - 0.23.0-10
- Update to work with maven-surefire 2.19.

* Thu Aug 27 2015 Roland Grunberg <rgrunber@redhat.com> - 0.23.0-9
- fedoraproject-p2: Enable support for p2 Droplets.

* Tue Jul 28 2015 Roland Grunberg <rgrunber@redhat.com> - 0.23.0-8
- fedoraproject-p2: Single IU resolving requirements with multiple matches.

* Fri Jul 17 2015 Roland Grunberg <rgrunber@redhat.com> - 0.23.0-7
- fedoraproject-p2: Remove host localization fragments from reactor units.

* Tue Jun 30 2015 Mat Booth <mat.booth@redhat.com> - 0.23.0-6
- Fix bootstrap build
- fedoraproject-p2: Allow xmvn-p2-installer to work in bootstrap mode

* Thu Jun 25 2015 Roland Grunberg <rgrunber@redhat.com> - 0.23.0-5
- fedoraproject-p2: Do not generate requires for fragments.
- Update to work with maven-surefire 2.18.

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jun 09 2015 Mat Booth <mat.booth@redhat.com> - 0.23.0-3
- Fix bootstrap build

* Tue Jun  9 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.23.0-2
- Port to Plexus Archiver 3.0.1

* Fri Jun 05 2015 Mat Booth <mat.booth@redhat.com> - 0.23.0-1
- Update to 0.23.0 release
- Allow tycho-bootstrap.sh to work with "set -e" to fail faster
  and see errors more easily

* Sat May 30 2015 Alexander Kurtakov <akurtako@redhat.com> 0.22.0-18
- Fix build with no tomcat servlet.

* Thu May 07 2015 Mat Booth <mat.booth@redhat.com> - 0.22.0-17
- Add org.tukaani.xz to tycho-bundles-external

* Tue Apr 28 2015 Roland Grunberg <rgrunber@redhat.com> - 0.22.0-16
- Fix resolution issues when upstream version in local repository.
- Resolves: rhbz#1216170

* Thu Apr 23 2015 Mat Booth <mat.booth@redhat.com> - 0.22.0-15
- fedoraproject-p2: Add support for archful dropins

* Mon Apr 20 2015 Roland Grunberg <rgrunber@redhat.com> - 0.22.0-14
- Handle possible changes to metadata namespace (ns[0-9]).

* Fri Apr 17 2015 Roland Grunberg <rgrunber@redhat.com> - 0.22.0-13
- fedoraproject-p2: Subpackages '*-tests' should not be in dropins.

* Sun Mar 29 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.22.0-12
- Port to Jetty 9.3.0

* Thu Feb  5 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.22.0-11
- fedoraproject-p2: Fix support for shallow dropin directory layout

* Wed Feb  4 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.22.0-10
- fedoraproject-p2: Bump BREE to JavaSE-1.8
- fedoraproject-p2: Fix installing of virtual bundles provided by p2.inf

* Wed Jan 28 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.22.0-9
- fedoraproject-p2: Allow installation of bundles not built with tycho

* Mon Jan 19 2015 Roland Grunberg <rgrunber@redhat.com> - 0.22.0-8
- Introduce basic SCL support.
- Minor changes for bootstrap build.
- Suppress failed lookups on non-existing paths in scripts.
- Explicitly depend on org.hamcrest.core where necessary.

* Thu Dec 11 2014 Mat Booth <mat.booth@redhat.com> - 0.22.0-7
- fedoraproject-p2: Fix for bundles containing underscores

* Wed Dec 10 2014 Mat Booth <mat.booth@redhat.com> - 0.22.0-6
- fedoraproject-p2: Update to latest snapshot

* Wed Dec 10 2014 Roland Grunberg <rgrunber@redhat.com> - 0.22.0-5
- Rebuild to pick up arch-independent ECF bundle locations.

* Mon Dec 08 2014 Roland Grunberg <rgrunber@redhat.com> - 0.22.0-4
- fedoraproject-p2: Permit installation of tycho-generated source features.

* Thu Dec  4 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.22.0-3
- Non-bootstrap build

* Thu Dec  4 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.22.0-2.1
- fedoraproject-p2: Add support for installation into SCLs
- Bootstrap build

* Thu Dec 04 2014 Mat Booth <mat.booth@redhat.com> - 0.22.0-2
- Fix osgi.jar symlink when in eclipse-bootstrap mode
- Remove no longer needed workaround for rhbz#1139180
- Tidy up and remove unneeded R/BRs
- Also reduce number of changes needed to SCL-ise package

* Mon Dec 01 2014 Mat Booth <mat.booth@redhat.com> - 0.22.0-1
- Update to tagged release

* Thu Nov 27 2014 Roland Grunberg <rgrunber@redhat.com> - 0.22.0-0.1.gitb1051d
- Update to 0.22.0 pre-release.

* Thu Nov 27 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.21.0-23
- fedoraproject-p2: Obtain SCL roots by parsing Java conf files
- fedoraproject-p2: Add support for installing into SCL root

* Thu Nov 27 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.21.0-22
- Install p2-install.sh script in java-utils/

* Thu Nov 27 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.21.0-21
- fedoraproject-p2: Implement installer application

* Tue Nov 25 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.21.0-20
- fedoraproject-p2: Update to latest snapshot (SCL improvements)

* Thu Nov 06 2014 Mat Booth <mat.booth@redhat.com> - 0.21.0-19
- fedoraproject-p2: Fix occasionally failing to generate metadata

* Tue Oct 28 2014 Roland Grunberg <rgrunber@redhat.com> - 0.21.0-18
- Fixes to bootstrap build.
- Package com.ibm.icu (icu4j-eclipse) for bootstrap build.
- Resolves: rhbz#1129801

* Thu Oct 09 2014 Mat Booth <mat.booth@redhat.com> - 0.21.0-17
- fedoraproject-p2: Fix incorrect metadata generation bugs

* Tue Oct 07 2014 Mat Booth <mat.booth@redhat.com> - 0.21.0-16
- fedoraproject-p2: Update to latest snapshot

* Thu Oct 02 2014 Roland Grunberg <rgrunber@redhat.com> - 0.21.0-15
- Update to build against plexus-archiver 2.6.

* Thu Sep 25 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.21.0-14
- fedoraproject-p2: Fix requires generation bug

* Wed Sep 24 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.21.0-13
- fedoraproject-p2: Allow installation of source bundles

* Mon Sep 22 2014 Roland Grunberg <rgrunber@redhat.com> - 0.21.0-12
- Add Fedora system repos to target definition resolver.
- Look for any IU if IU/Version query fails in target definition resolver.

* Fri Sep 12 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.21.0-11
- fedoraproject-p2: Allow installing the same symlink into separate dropins

* Wed Sep 10 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.21.0-10
- Fix tycho-bundles-external-manifest.txt generation

* Wed Sep 10 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.21.0-9
- fedoraproject-p2: Fix self-dependencies failing builds

* Tue Sep 9 2014 Roland Grunberg <rgrunber@redhat.com> - 0.21.0-8
- Make debundling more resilient to changes.
- fedoraproject-p2: Update to latest (Fix metapackage merging).

* Mon Sep  8 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.21.0-8
- fedoraproject-p2: Import XMvn P2 plugin
- fedoraproject-p2: Fix NPE bug
- fedoraproject-p2: Avoid extracting tycho-bundles-external.zip

* Fri Sep 05 2014 Roland Grunberg <rgrunber@redhat.com> - 0.21.0-7
- Debundle tycho-bundles-external and tycho-standalone-p2-director.
- Resolves: rhbz#789272

* Thu Sep 04 2014 Roland Grunberg <rgrunber@redhat.com> - 0.21.0-6
- Use fedoraproject-p2 to do OSGi bundle discovery.

* Wed Sep 03 2014 Mat Booth <mat.booth@redhat.com> - 0.21.0-5
- Include eclipse features dir in custom resolver

* Wed Sep 03 2014 Roland Grunberg <rgrunber@redhat.com> - 0.21.0-4
- fedoraproject-p2: Do not regenerate IU metadata on every query.

* Thu Aug 28 2014 Mat Booth <mat.booth@redhat.com> - 0.21.0-3
- Perform non-bootstrap build
- Update running-env-only patch

* Wed Aug 27 2014 Roland Grunberg <rgrunber@redhat.com> - 0.21.0-2.1
- fedoraproject-p2: Fix issues with creation of feature IUs.
- fedoraproject-p2: Fix jar corruption bug.

* Thu Aug 21 2014 Roland Grunberg <rgrunber@redhat.com> - 0.21.0-2
- Integrate fedoraproject-p2 into Tycho.

* Thu Jul 24 2014 Roland Grunberg <rgrunber@redhat.com> - 0.21.0-1
- Update to 0.21.0 Release.

* Fri Jul 11 2014 Mat Booth <mat.booth@redhat.com> - 0.20.0-18
- Allow director plugin to only assemble products for the current arch
- Drop some unneeded BR/Rs on surefire (maven-local pulls these in)

* Wed Jul 02 2014 Roland Grunberg <rgrunber@redhat.com> - 0.20.0-17
- Return non-existant expected local path when resolution fails.
- Resolves: rhbz#1114120

* Fri Jun 27 2014 Roland Grunberg <rgrunber@redhat.com> - 0.20.0-16
- Tycho should always delegate artifact resolution to Maven.

* Wed Jun 25 2014 Alexander Kurtakov <akurtako@redhat.com> 0.20.0-15
- Non-bootstrap build now that aarch64 is done.

* Tue Jun 24 2014 Roland Grunberg <rgrunber@redhat.com> - 0.20.0-14.1
- Add swt aarch64 fragment to bootstrap repo.

* Tue Jun 24 2014 Alexander Kurtakov <akurtako@redhat.com> 0.20.0-14
- Full bootstrap build for secondary archs.

* Thu Jun 12 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.20.0-13
- Restore runtime dependencies on XMvn

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Jun  3 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.20.0-11
- Skip intermediary build in non-bootstrap mode
- Resolves: rhbz#1103839
- Remove unneeded XMvn bits

* Fri May 30 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.20.0-10
- Fix runtime dependencies on XMvn in POMs
- Use custom Plexus config to lookup XMvn classes
- Lookup Aether WorkspaceReader using role hint "ide"

* Thu May 29 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.20.0-9
- Don'n install duplicate Maven metadata for sisu-equinox

* Wed May 21 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.20.0-8
- Use .mfiles generated during build

* Fri May 16 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.20.0-7
- Add support for XMvn 2.0

* Tue May 13 2014 Alexander Kurtakov <akurtako@redhat.com> 0.20.0-6
- Make tycho copy licence feature to the system repo.

* Wed Apr 30 2014 Alexander Kurtakov <akurtako@redhat.com> 0.20.0-5
- Non-bootstrap build.

* Tue Apr 29 2014 Alexander Kurtakov <akurtako@redhat.com> 0.20.0-4
- Organize patches.

* Tue Apr 22 2014 Roland Grunberg <rgrunber@redhat.com> - 0.20.0-3
- Add support for compact profiles (Bug 1090003).

* Wed Apr 02 2014 Roland Grunberg <rgrunber@redhat.com> - 0.20.0-2
- Non-bootstrap build.

* Thu Mar 27 2014 Roland Grunberg <rgrunber@redhat.com> - 0.20.0-1.1
- Update to Eclipse Luna (4.4).

* Mon Mar 24 2014 Roland Grunberg <rgrunber@redhat.com> - 0.20.0-1
- Update to 0.20.0 Release.

* Wed Mar 12 2014 Roland Grunberg <rgrunber@redhat.com> - 0.19.0-11
- Respect %%{eclipse_bootstrap} flag in tycho-bootstrap.sh.
- Update Eclipse bootstrap cache.
- Fix Equinox Launcher usage logic in copy-platform-all.

* Thu Mar 06 2014 Roland Grunberg <rgrunber@redhat.com> - 0.19.0-10
- Non-bootstrap build.

* Thu Mar 06 2014 Roland Grunberg <rgrunber@redhat.com> - 0.19.0-9.1
- Do not check %%{_libdir}/eclipse plugins/features folders twice.

* Wed Feb 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.19.0-9
- Improve logging and error handling fop copy-platform-all

* Wed Jan 15 2014 Roland Grunberg <rgrunber@redhat.com> - 0.19.0-8
- Perform a pure bootstrap build.
- Fix issues with bootstrap build.

* Thu Jan 09 2014 Roland Grunberg <rgrunber@redhat.com> - 0.19.0-7
- Fix bootstrap build.

* Mon Jan  6 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.19.0-6
- Fix usage of %%add_maven_depmap for zip files
- Resolves: rhbz#1004310

* Mon Dec 9 2013 Alexander Kurtakov <akurtako@redhat.com> 0.19.0-5
- Switch to using %%mvn_build.
- Update BR/R names.
- Adapt to asm5.

* Thu Nov 21 2013 Roland Grunberg <rgrunber@redhat.com> - 0.19.0-4
- Return expected reactor cache location when XMvn resolution fails.

* Wed Nov 20 2013 Roland Grunberg <rgrunber@redhat.com> - 0.19.0-3
- Bump release for rebuild (Bug 1031769).

* Mon Nov 18 2013 Roland Grunberg <rgrunber@redhat.com> - 0.19.0-2
- Reduce length of file lock name when file is in build directory.

* Thu Oct 24 2013 Roland Grunberg <rgrunber@redhat.com> - 0.19.0-1
- Update to 0.19.0 Release.

* Fri Oct 04 2013 Roland Grunberg <rgrunber@redhat.com> - 0.18.1-7
- Do not use XMvn internals (Bug 1015038).

* Thu Oct 3 2013 Krzysztof Daniel <kdaniel@redhat.com> 0.18.1-6
- Adjust to latest Xmvn (workaround for 1015038).

* Mon Sep  9 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.18.1-5
- Add workaround for rhbz#1004310

* Tue Jul 30 2013 Roland Grunberg <rgrunber@redhat.com> - 0.18.1-4
- Improve artifact resolution using XMvn Resolver. (Bug 986900)

* Mon Jul 29 2013 Roland Grunberg <rgrunber@redhat.com> - 0.18.1-3
- Fix Tycho file locking to work in Fedora.
- Skip validateConsistentTychoVersion by default. (Bug 987271)

* Wed Jul 24 2013 Roland Grunberg <rgrunber@redhat.com> - 0.18.1-2
- Non-bootstrap build.

* Wed Jul 24 2013 Roland Grunberg <rgrunber@redhat.com> - 0.18.1-1.1
- Update to use Eclipse Aether.
- Use MavenSession and Plexus to determine state.
- Fix bootstrap build.

* Thu Jul 18 2013 Roland Grunberg <rgrunber@redhat.com> 0.18.1-1
- Make changes to ensure intermediary build succeeds.
- Remove %%Patch6 in favour of call to sed.

* Thu Jul 18 2013 Krzysztof Daniel <kdaniel@redhat.com> 0.18.1-1
- Update to 0.18.1.

* Tue Jul 16 2013 Roland Grunberg <rgrunber@redhat.com> - 0.18.0-5
- Look for maven artifacts using XMvn Resolver.

* Tue Jul 9 2013 Roland Grunberg <rgrunber@redhat.com> 0.18.0-4
- Update to use maven-surefire 2.15 API.

* Fri Jul 5 2013 Alexander Kurtakov <akurtako@redhat.com> 0.18.0-3
- Use _jnidir too when building local p2 repo.

* Thu Jun 6 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.18.0-2
- Add Requires on plugins present in Maven super POM
- Resolves: rhbz#971301

* Tue May 28 2013 Roland Grunberg <rgrunber@redhat.com> 0.18.0-1
- Update to 0.18.0 Release.

* Thu Apr 11 2013 Roland Grunberg <rgrunber@redhat.com> 0.17.0-1
- Fix bootstrap build for potential future use.

* Tue Apr 2 2013 Roland Grunberg <rgrunber@redhat.com> 0.17.0-1
- Update to 0.17.0 Release.

* Mon Mar 18 2013 Roland Grunberg <rgrunber@redhat.com> 0.17.0-0.11.git3351b1
- Non-bootstrap build.

* Mon Mar 18 2013 Krzysztof Daniel <kdaniel@redhat.com> 0.17.0-0.10.git3351b1
- Merge mizdebsk patch with existing custom resolver patch.

* Mon Mar 18 2013 Krzysztof Daniel <kdaniel@redhat.com> 0.17.0-0.9.git3351b1
- Move the patch into better place.

* Mon Mar 18 2013 Krzysztof Daniel <kdaniel@redhat.com> 0.17.0-0.8.git3351b1
- Non-bootstrap build.

* Mon Mar 18 2013 Krzysztof Daniel <kdaniel@redhat.com> 0.17.0-0.7.git3351b1
- Commit the patch.

* Mon Mar 18 2013 Krzysztof Daniel <kdaniel@redhat.com> 0.17.0-0.6.git3351b1
- Use plexus to instantiate workspace reader.

* Sun Mar 17 2013 Roland Grunberg <rgrunber@redhat.com> 0.17.0-0.5.git3351b1
- Non-bootstrap build.

* Fri Mar 15 2013 Roland Grunberg <rgrunber@redhat.com> 0.17.0-0.4.git3351b1
- Update bootstrapped build for 0.17.0-SNAPSHOT to work against 0.16.0.
- Update to Plexus Compiler 2.2 API.

* Thu Feb 28 2013 Roland Grunberg <rgrunber@redhat.com> 0.17.0-0.3.git3351b1
- Update to using Jetty 9 API.

* Mon Feb 25 2013 Roland Grunberg <rgrunber@redhat.com> 0.17.0-0.2.git3351b1
- Set the global default execution environment to JavaSE-1.6.
- Patch clean-up.

* Mon Feb 25 2013 Krzysztof Daniel <kdaniel@redhat.com> 0.17.0-0.1.git3351b1
- Update to latest upstream.
- RHBZ#915194 - API changed in maven-surefire

* Wed Feb 6 2013 Roland Grunberg <rgrunber@redhat.com> 0.16.0-21
- Non-bootstrap build.

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 0.16.0-20.2
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Wed Feb 6 2013 Roland Grunberg <rgrunber@redhat.com> 0.16.0-20.1
- Change BR/R on maven to maven-local for XMvn support.
- Build bootstrapped to fix missing Fedora Maven class.

* Thu Jan 24 2013 Roland Grunberg <rgrunber@redhat.com> 0.16.0-20
- Use TYCHO_MVN_{LOCAL,RPMBUILD} to determine how maven was called.
- Update to maven-surefire 2.13.

* Thu Dec 20 2012 Roland Grunberg <rgrunber@redhat.com> 0.16.0-19
- Fix upstream Bug 361204.

* Mon Dec 3 2012 Roland Grunberg <rgrunber@redhat.com> 0.16.0-18
- Add support for more flexible OSGi bundle paths.
- Use OSGi Requires instead of package name.
- Expand Requires to include the Eclipse platform.

* Mon Nov 19 2012 Roland Grunberg <rgrunber@redhat.com> 0.16.0-17
- Make additional changes to get Tycho building bootstrapped.

* Mon Nov 5 2012 Roland Grunberg <rgrunber@redhat.com> 0.16.0-16
- Add capability to build without depending on Tycho or Eclipse.

* Sat Oct 20 2012 Roland Grunberg <rgrunber@redhat.com> 0.16.0-15
- Package org.eclipse.osgi and org.eclipse.jdt.core.

* Fri Oct 19 2012 Roland Grunberg <rgrunber@redhat.com> 0.16.0-14
- Update to finalized 0.16.0 Release.

* Wed Oct 17 2012 Roland Grunberg <rgrunber@redhat.com> 0.16.0-13
- Build Tycho properly in one RPM build.
- Update to 0.16.0 Release.

* Thu Oct 11 2012 Roland Grunberg <rgrunber@redhat.com> 0.16.0-12.d7f885
- Non-bootstrap build.

* Thu Oct 11 2012 Roland Grunberg <rgrunber@redhat.com> 0.16.0-11.1.d7f885
- Remove dependence on eclipse by use of self-bundled equinox launcher.

* Wed Oct 10 2012 Roland Grunberg <rgrunber@redhat.com> 0.16.0-11.d7f885
- copy-platform-all should make symlinked jars from %%{_javadir} unique.
- Non-bootstrap build (reset the %%bootstrap flag properly).

* Mon Oct 8 2012 Krzysztof Daniel <kdaniel@redhat.com> 0.16.0-10.d7f885
- Non-bootstrap build.

* Mon Oct 8 2012 Krzysztof Daniel <kdaniel@redhat.com> 0.16.0-9.1.d7f885
- Filter out OSGi dependencies.

* Thu Oct 4 2012 Roland Grunberg <rgrunber@redhat.com> 0.16.0-9.d7f885
- Non-bootstrap build.

* Thu Oct 4 2012 Roland Grunberg <rgrunber@redhat.com> 0.16.0-8.1.d7f885
- Fix Bug in overriding of BREE to JavaSE-1.6.

* Wed Oct 3 2012 Roland Grunberg <rgrunber@redhat.com> 0.16.0-8.d7f885
- Non-bootstrap build.

* Wed Oct 3 2012 Roland Grunberg <rgrunber@redhat.com> 0.16.0-7.1.d7f885
- Update to latest 0.16.0 SNAPSHOT.
- First attempts to build without cyclic dependency to JDT.

* Mon Aug 27 2012 Roland Grunberg <rgrunber@redhat.com> 0.16.0-7.df2c35
- Non bootstrap-build.

* Mon Aug 27 2012 Roland Grunberg <rgrunber@redhat.com> 0.16.0-6.1.df2c35
- Add BR/R on explicit dependency objectweb-asm4.
- Use consistent whitespace in specfile.

* Fri Aug 24 2012 Roland Grunberg <rgrunber@redhat.com> 0.16.0-6.df2c35
- Non-bootstrap build.

* Thu Aug 23 2012 Roland Grunberg <rgrunber@redhat.com> 0.16.0-5.1.df2c35
- Set BREE to at least JavaSE-1.6 for all eclipse packaging types.
- Remove unneeded workaround for JSR14 incompatibility of JDK 1.7.

* Wed Aug 15 2012 Roland Grunberg <rgrunber@redhat.com> 0.16.0-5.df2c35
- Non-bootstrap build.

* Mon Aug 13 2012 Roland Grunberg <rgrunber@redhat.com> 0.16.0-4.1.df2c35
- Correctly reference objectweb-asm4 and fix local mode resolution bug.
- Update spec file to honour new java packaging guidelines.

* Thu Aug 9 2012 Roland Grunberg <rgrunber@redhat.com> 0.16.0-4.df2c35
- Non-bootstrap build.

* Thu Aug 9 2012 Roland Grunberg <rgrunber@redhat.com> 0.16.0-3.1.df2c35
- Add tycho.local.keepTarget flag to bypass ignoring environments.

* Thu Aug 9 2012 Krzysztof Daniel <kdaniel@redhat.com> 0.16.0-3.df2c35
- Non-bootstrap build.

* Thu Aug 9 2012 Krzysztof Daniel <kdaniel@redhat.com> 0.16.0-2.1.df2c35
- Use recommended %%add_maven_depmap. 

* Thu Aug 9 2012 Krzysztof Daniel <kdaniel@redhat.com> 0.16.0-2.df2c35
- Non-bootstrap build.

* Thu Aug 9 2012 Krzysztof Daniel <kdaniel@redhat.com> 0.16.0-1.2.df2c35
- Properly change bootstrap flag.
- Add some git ignores.

* Thu Aug 9 2012 Krzysztof Daniel <kdaniel@redhat.com> 0.16.0-1.1.df2c35
- Install missing tycho-standalone-p2-director.zip.

* Thu Aug 2 2012 Roland Grunberg <rgrunber@redhat.com> 0.16.0-1.df2c35
- Update to 0.16.0 SNAPSHOT.

* Tue Jul 31 2012 Roland Grunberg <rgrunber@redhat.com> 0.15.0-3
- Non-bootstrap build.

* Tue Jul 31 2012 Roland Grunberg <rgrunber@redhat.com> 0.15.0-2.1
- Ignore defined environments in local mode.

* Mon Jul 30 2012 Roland Grunberg <rgrunber@redhat.com> 0.15.0-2
- Non-bootstrap build.

* Mon Jul 30 2012 Roland Grunberg <rgrunber@redhat.com> 0.15.0-1.1
- Fix copy-platform-all script to properly link %%{_datadir}/eclipse jars.

* Thu Jul 26 2012 Roland Grunberg <rgrunber@redhat.com> 0.15.0-1
- Update to 0.15.0.
- Set BREE to at least JavaSE-1.6 for Eclipse feature bundles.

* Wed Jul 25 2012 Roland Grunberg <rgrunber@redhat.com> 0.14.1-7
- Non-bootstrap build.

* Mon Jul 23 2012 Roland Grunberg <rgrunber@redhat.com> 0.14.1-6
- Detect OSGi jars using presence of Bundle-SymbolicName entry (BZ #838513).

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Roland Grunberg <rgrunber@redhat.com> 0.14.1-5
- Non-bootstrap build.

* Tue May 29 2012 Roland Grunberg <rgrunber@redhat.com> 0.14.1-4.1
- Fix Tycho Surfire to run Eclipse test bundles.
- Implement automatic creation of a system p2 repository.
- Allow building SWT fragments (BZ #380934).

* Wed May 23 2012 Roland Grunberg <rgrunber@redhat.com> 0.14.1-4
- Non-bootstrap build.

* Thu May 17 2012 Roland Grunberg <rgrunber@redhat.com> 0.14.1-3.1
- Set BREE to be at least JavaSE-1.6 for Eclipse OSGi bundles.

* Wed May 16 2012 Roland Grunberg <rgrunber@redhat.com> 0.14.1-3
- Non-bootstrap build.

* Wed Apr 25 2012 Roland Grunberg <rgrunber@redhat.com> 0.14.1-2.1
- Implement a custom resolver when running in local mode.
- Use upstream solution for BZ #372395 to fix the build.

* Wed Apr 4 2012 Roland Grunberg <rgrunber@redhat.com> 0.14.1-2
- Non-bootstrap build.

* Tue Mar 27 2012 Roland Grunberg <rgrunber@redhat.com> 0.14.1-1.1
- Add missing tycho-testing-harness to be packaged.
- Use %%{_eclipse_base} from eclipse-platform.

* Fri Mar 9 2012 Roland Grunberg <rgrunber@redhat.com> 0.14.1-1
- Update to 0.14.1 upstream tag.
- Allow building against maven-surefire 2.12 (instead of 2.10).
- Stop symlinking o.e.osgi and o.e.jdt.core into the m2 cache.

* Thu Feb 16 2012 Roland Grunberg <rgrunber@redhat.com> 0.14.0-4
- Non-bootstrap build.

* Tue Feb 14 2012 Roland Grunberg <rgrunber@redhat.com> 0.14.0-3
- Update to 0.14.0 upstream tag.

* Thu Feb 9 2012 Roland Grunberg <rgrunber@redhat.com> 0.14.0-2
- Non-bootstrap build.

* Wed Feb 01 2012 Roland Grunberg <rgrunber@redhat.com> - 0.14.0-1
- Update to 0.14.0.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri May 27 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.12.0-0.1.a74b1717
- Update to new version do bootstrap from scratch

* Fri May 6 2011 Alexander Kurtakov <akurtako@redhat.com> 0.10.0-3
- Non-bootstrap build.

* Tue May  3 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.10.0-2
- Add README and make build more silent

* Tue Mar 29 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.10.0-1
- First bootstrapped version

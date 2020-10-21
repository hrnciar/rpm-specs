Name:           eclipse-webtools
Version:        3.18.0
Release:        5%{?dist}
Summary:        Eclipse Webtools Projects

License:        EPL-1.0 and EPL-2.0
URL:            http://www.eclipse.org/webtools/

# Generate tarball with script:
# $ sh get-sources.sh
Source0:        %{name}-%{version}.tar.xz

# Based on https://git.eclipse.org/c/webtools-common/webtools.common.git/commit/?id=b61f1b8950dfd22ab6a1f40d1494c5a26d4eddb6
Patch0:         0001-Allow-building-on-JDK-11.patch

# Remove version checks from
# webtools.sourceediting/features/org.eclipse.wst.xml_core.feature/feature.xml
Patch1:         %{name}-rm-version-checks-from-xml_core-feature.patch

# Fix xerces api change (a method needs to return a String)
Patch2:         %{name}-xerces-api-change.patch

BuildArch:      noarch

# Upstream Eclipse no longer supports non-64bit arches
ExcludeArch: s390 %{arm} %{ix86}

BuildRequires:  maven-local
BuildRequires:  tycho
BuildRequires:  tycho-extras
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  eclipse-emf-runtime
BuildRequires:  eclipse-gef >= 3.11.0
BuildRequires:  eclipse-jdt
BuildRequires:  eclipse-license2
BuildRequires:  eclipse-pde
BuildRequires:  eclipse-xsd
BuildRequires:  osgi(org.eclipse.jetty.http)
BuildRequires:  osgi(org.eclipse.jetty.webapp)
BuildRequires:  osgi(osgi.core)
BuildRequires:  xalan-j2
BuildRequires:  xerces-j2

%description
Eclipse Webtools. This contains sub-packages for different sub-projects
of Eclipse Webtools project, including Server Tools, SourceEditing Tools,
Webservices Tools, Java EE Tools, JSF Tools, and Dali (JPA) Tools. 

%package        common
Summary:        WST Common UI and Faceted Project Framework
Requires:       eclipse-gef >= 3.11.0
# Obsoletes added in F31 -- retirement of jpa/datatools support
Obsoletes:      %{name}-dali <= 3.16.0-1
Obsoletes:      eclipse-dtp <= 1.14.105-1
# Obsoletes added in F33 -- retirement of javaee/webservices/jsf support
Obsoletes:      %{name}-javaee <= 3.18.0-2

%description common
This package includes WST common UI functionality, and faceted projects
framework. The Faceted Project Framework allows the plugin developer to think
of projects as composed of units of functionality, otherwise known as facets,
that can be added and removed by the user.

%package        servertools
Summary:        Eclipse Server Tools Framework

%description servertools
This package includes Server tools framework UI, and adapters for use
with the WST and JST server tools.

%package        sourceediting
Summary:        Eclipse Web Developer, XML, XPath, and XSL Tools

%description sourceediting
Eclipse Web Developer Tools, including HTML, CSS, XHTML, XML, DTD and XML
Schema Editors, validators, and XML Catalog support.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1
%patch1
%patch2

# Find and delete any hidden jar or zip files
find -name *.class -type f -delete
find -name *.jar -type f -delete
find -name *.zip -type f -delete

# Fixup erroneous license info, see: https://bugs.eclipse.org/bugs/show_bug.cgi?id=538094
sed -i -e '/license-feature-version/s/.\..\..\.qualifier/0.0.0/' \
  $(find -name feature.xml)

# Build useless jar that is needed to build but does nothing
# See http://dev.eclipse.org/mhonarc/lists/wtp-dev/msg08607.html
# and PERFMSR.README.txt in org.eclipse.perfmsr.core.stub/
CORE_RUNTIME_JAR=$(ls %{_prefix}/lib/eclipse/plugins/org.eclipse.core.runtime_*)
pushd webtools.common/plugins/org.eclipse.jem.util/org.eclipse.perfmsr.core.stub/src
    javac -cp $(build-classpath osgi-core):${CORE_RUNTIME_JAR} \
        org/eclipse/perfmsr/core/*.java
    jar cf ../perfmsr.jar org/
popd

# Disable JPA/JSF/JavaEE features
%pom_disable_module webtools.dali pom-build-everything.xml
%pom_disable_module webtools.javaee pom-build-everything.xml
%pom_disable_module webtools.jsf pom-build-everything.xml
%pom_disable_module webtools.webservices pom-build-everything.xml

# Disable JSDT features
%pom_disable_module webtools.jsdt pom-build-everything.xml
%pom_disable_module org.eclipse.wst.jsdt.web.core webtools.sourceediting/web/bundles
%pom_disable_module org.eclipse.wst.jsdt.web.support.jsp webtools.sourceediting/web/bundles
%pom_disable_module org.eclipse.wst.jsdt.web.ui webtools.sourceediting/web/bundles
%pom_disable_module org.eclipse.wst.web_js_support.feature webtools.sourceediting/web/features
%pom_disable_module org.eclipse.wst.web_js_support_sdk.feature webtools.sourceediting/web/features
%pom_disable_module org.eclipse.wst.web_js_support_tests.feature webtools.sourceediting/web/features
%pom_xpath_remove "includes[@id='org.eclipse.wst.web_js_support.feature']" \
  webtools.sourceediting/web/features/org.eclipse.wst.web_ui.feature/feature.xml

# Disable XSL/XPATH editing features
%pom_disable_module xsl webtools.sourceediting
%pom_disable_module xpath webtools.sourceediting

# Disable capabilities because they hide stuff by default
%pom_disable_module org.eclipse.wtp.javascript.capabilities webtools.sourceediting/web/bundles
%pom_disable_module org.eclipse.wtp.web.capabilities webtools.sourceediting/web/bundles
%pom_disable_module org.eclipse.wtp.xml.capabilities webtools.sourceediting/xml/bundles

# Disable building all repositories and tests for now
%pom_disable_module webtools.releng pom-build-everything.xml
%pom_disable_module webtools.repositories pom-build-everything.xml
%pom_disable_module site webtools.common
%pom_disable_module site webtools.servertools
%pom_disable_module site webtools.sourceediting
%pom_disable_module tests webtools.common
%pom_disable_module org.eclipse.wst.common_tests.feature webtools.common/features
%pom_disable_module tests webtools.sourceediting/{core,json,web,xml}
%pom_disable_module org.eclipse.wst.json_tests.feature webtools.sourceediting/json/features
%pom_disable_module org.eclipse.wst.web_tests.feature webtools.sourceediting/web/features
%pom_disable_module org.eclipse.wst.xml_tests.feature webtools.sourceediting/xml/features
%pom_disable_module org.eclipse.wst.web_sdk.feature webtools.sourceediting/web/features
%pom_disable_module tests/org.eclipse.wst.internet.monitor.core.tests webtools.servertools
%pom_disable_module tests/org.eclipse.wst.server.core.tests webtools.servertools
%pom_disable_module tests/org.eclipse.wst.server.http.core.tests webtools.servertools
%pom_disable_module tests/org.eclipse.wst.server.util.tests webtools.servertools
%pom_disable_module features/org.eclipse.jst.server_adapters.ext_tests.feature webtools.servertools
%pom_disable_module features/org.eclipse.jst.server_tests.feature webtools.servertools
%pom_disable_module features/org.eclipse.wst.server_tests.feature webtools.servertools

# Tighten up dep on xerces
sed -i -e '/org.apache.xerces/s/2\..\.0/2.11.0/' $(find webtools.*/bundles -name MANIFEST.MF)

# Fix dep on javax.servlet-api
sed -i -e '/javax.servlet/s/3.1.0,4.0.0/3.1.0,5.0.0/' webtools.servertools/plugins/org.eclipse.wst.server.preview/META-INF/MANIFEST.MF

# Don't use strict project settings, webtools is not ready (fixes 'unnecessary cast' errors and API access errors, etc)
%pom_xpath_inject "pom:plugin[pom:artifactId = 'tycho-compiler-plugin']/pom:configuration" \
  "<useProjectSettings>false</useProjectSettings>" wtp-parent

# Don't use jgit providers in packaging plugin
%pom_remove_dep :tycho-buildtimestamp-jgit wtp-parent
%pom_remove_dep :tycho-sourceref-jgit wtp-parent
%pom_xpath_remove pom:plugin/pom:configuration/pom:sourceReferences wtp-parent
%pom_xpath_remove pom:plugin/pom:configuration/pom:timestampProvider wtp-parent
%pom_xpath_remove pom:plugin/pom:configuration/pom:jgit.ignore wtp-parent
%pom_xpath_remove pom:plugin/pom:configuration/pom:jgit.dirtyWorkingTree wtp-parent

# Remove pre-built indexes
for index in $(find -name indexed_docs) ; do
  rm $(dirname $index)/*
  %pom_xpath_remove "plugin/extension[@point='org.eclipse.help.toc']/index" $(dirname $(dirname $index))/plugin.xml
done

# Don't install poms
%mvn_package "::pom::" __noinstall

# SDK bits
%mvn_package ":*sdk{,.feature,.documentation}" __noinstall
%mvn_package ":*.assembly.feature" __noinstall
%mvn_package ":*{.api.doc,.doc.api,.doc.isv,.doc.dev}" __noinstall
%mvn_package ":::sources{,-feature}:" __noinstall

# Common features and plugins
%mvn_package "org.eclipse.webtools.common:" common

# Server Tools features and plugins
%mvn_package "org.eclipse.webtools.servertools:" servertools

# Source Editing features and plugins
%mvn_package "org.eclipse.webtools.sourceediting:" sourceediting
%mvn_package "org.eclipse.webtools.javaee:" sourceediting

%build
# Avoid running out of heap on s390x
export MAVEN_OPTS="-Xmx1024m"

# Qualifier generated from last modification time of source tarball
QUALIFIER=$(date -u -d"$(stat --format=%y %{SOURCE0})" +v%Y%m%d%H%M)
%mvn_build -j -f -- -DforceContextQualifier=$QUALIFIER -f pom-build-everything.xml

%install
%mvn_install

%files common -f .mfiles-common
%license webtools.releng/releng.wtpbuilder/rootfiles/epl-2.0.html

%files servertools -f .mfiles-servertools

%files sourceediting -f .mfiles-sourceediting

%changelog
* Thu Aug 20 2020 Mat Booth <mat.booth@redhat.com> - 3.18.0-5
- Patch to allow building against JDK 11

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.18.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 16 2020 Mat Booth <mat.booth@redhat.com> - 3.18.0-3
- Remove no longer needed dep on jdom and json-simple and add missing BRs
  on xml deps
- Drop xsl and xpath features
- Always use java 1.8 for building due to use of CORBA

* Fri Jul 10 2020 Mat Booth <mat.booth@redhat.com> - 3.18.0-2
- Drop javaee/webservices/jsf plugins

* Wed Jun 24 2020 Mat Booth <mat.booth@redhat.com> - 3.18.0-1
- Update to latest upstream release

* Fri Jan 24 2020 Mat Booth <mat.booth@redhat.com> - 3.15.0-4
- Drop JPA tooling and remove requirement on Datatools

* Mon Dec 09 2019 Mat Booth <mat.booth@redhat.com> - 3.15.0-3
- Fix build against latest jetty version

* Mon Dec 09 2019 Mat Booth <mat.booth@redhat.com> - 3.15.0-2
- Drop JSDT features

* Mon Sep 16 2019 Mat Booth <mat.booth@redhat.com> - 3.15.0-1
- Update to latest upstream release

* Wed Jun 26 2019 Mat Booth <mat.booth@redhat.com> - 3.14.0-3
- Build missing xinclude embedded jar

* Fri Jun 14 2019 Mat Booth <mat.booth@redhat.com> - 3.14.0-2
- Avoid running out of heap on s390x

* Wed Jun 12 2019 Mat Booth <mat.booth@redhat.com> - 3.14.0-1
- Update to latest upstream release

* Tue Jun 11 2019 Mat Booth <mat.booth@redhat.com> - 3.13.0-2
- Avoid using jgit providers from tycho-extras

* Fri Mar 15 2019 Mat Booth <mat.booth@redhat.com> - 3.13.0-1
- Update to 2019-03 release
- Update license tag
- Restrict to same architectures as Eclipse itself

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 10 2019 Mat Booth <mat.booth@redhat.com> - 3.12.0-1
- Update to upstream 3.12 release to add support for JPA 2.2

* Mon Nov 19 2018 Mat Booth <mat.booth@redhat.com> - 3.11.0-3
- Rebuild for xerces update

* Tue Sep 25 2018 Mat Booth <mat.booth@redhat.com> - 3.11.0-2
- Fix missing R on commons-discovery

* Tue Sep 25 2018 Mat Booth <mat.booth@redhat.com> - 3.11.0-1
- Update to latest upstream release
- Amend license tag

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 07 2018 Mat Booth <mat.booth@redhat.com> - 3.10.0-1
- Update to Photon release
- Drop ancient provides/obsoletes
- Drop upstreamed patches

* Mon May 21 2018 Mat Booth <mat.booth@redhat.com> - 3.10.0-0.2
- Update to latest Photon snapshot

* Wed May 16 2018 Mat Booth <mat.booth@redhat.com> - 3.10.0-0.1
- Update to Photon snapshot

* Fri Apr 13 2018 Mat Booth <mat.booth@redhat.com> - 3.9.4-4
- Stop shipping deprecated Apache Axis support
- Merge jsf and javaee sub-packages; there is a dep cycle between
  them so one is always installed with the other anyway

* Tue Apr 10 2018 Mat Booth <mat.booth@redhat.com> - 3.9.4-3
- Minor spec file updates

* Tue Apr 10 2018 Mat Booth <mat.booth@redhat.com> - 3.9.4-2
- Fix source tarball to include missing changes from servertools

* Mon Apr 09 2018 Mat Booth <mat.booth@redhat.com> - 3.9.4-1
- Update to Oxygen.3a release for Java 10 support

* Wed Mar 21 2018 Mat Booth <mat.booth@redhat.com> - 3.9.3-1
- Update to latest Oxygen.3 release

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Dec 18 2017 Mat Booth <mat.booth@redhat.com> - 3.9.2-1
- Update to latest release

* Tue Oct 03 2017 Mat Booth <mat.booth@redhat.com> - 3.9.1-1
- Update to Oxygen.1a release

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 27 2017 Mat Booth <mat.booth@redhat.com> - 3.9.0-1
- Update to Oxygen final release

* Mon May 08 2017 Mat Booth <mat.booth@redhat.com> - 3.8.2-6
- Fix build against latest tycho and oxygen

* Thu Apr 20 2017 Mat Booth <mat.booth@redhat.com> - 3.8.2-5
- Revised patch for ebz#511793

* Mon Apr 10 2017 Mat Booth <mat.booth@redhat.com> - 3.8.2-4
- Backport patch to fix a thread deadlock ebz#511793

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Mat Booth <mat.booth@redhat.com> - 3.8.2-2
- Use glassfish servlet api in wst.server.preview.adapter

* Thu Jan 26 2017 Mat Booth <mat.booth@redhat.com> - 3.8.2-1
- Update to latest maintenance version

* Thu Oct 06 2016 Mat Booth <mat.booth@redhat.com> - 3.8.1-1
- Update to latest maintenance release
- Fix some broken symlinks

* Tue Aug 16 2016 Mat Booth <mat.booth@redhat.com> - 3.8.0-2
- Fix breakpoint inteference with CDT

* Tue Jul 05 2016 Mat Booth <mat.booth@redhat.com> - 3.8.0-1
- Update to tagged version
- Drop ancient provides/obsoletes
- Merge some sub-packages to eliminate cyclical deps and simplify
  the packaging a little bit
- Rationalise BRs and Rs

* Wed Jun 1 2016 Alexander Kurtakov <akurtako@redhat.com> 3.8.0-0.1gitb640484
- Update to Neon pre release.

* Tue Feb 09 2016 Roland Grunberg <rgrunber@redhat.com> - 3.7.1-3
- Update to use proper xmvn provided macros.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Oct 03 2015 Gerard Ryan <gerard@ryan.lt> - 3.7.1-1
- Update to latest upstream release tag R3_7_1 for Mars.1

* Sun Sep 13 2015 Gerard Ryan <gerard@ryan.lt> - 3.7.0-1
- Update to latest upstream release tag R3_7_0 for Mars

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Mar 02 2015 Gerard Ryan <gerard@ryan.lt> - 3.6.3-2
- Update to latest upstream release tag R3_6_3

* Sat Jan 24 2015 Gerard Ryan <gerard@ryan.lt> - 3.6.2-1
- Update to latest upstream release tag R3_6_2

* Thu Dec 11 2014 Alexander Kurtakov <akurtako@redhat.com> 3.6.1-3
- Remove unneeded BR on feclipse-maven-plugin.

* Tue Nov 18 2014 Alexander Kurtakov <akurtako@redhat.com> 3.6.1-2
- Fix typo in webtools-servertools installation.

* Fri Sep 26 2014 Gerard Ryan <gerard@ryan.lt> - 3.6.1-1
- Update to latest upstream release tag R3_6_1

* Fri Aug 22 2014 Mat Booth <mat.booth@redhat.com> - 3.6.0-7
- Prefix qualifier to ensure it is lexographically greater than the
  upstream's update site (prevents unnecessary updates)
- Make use of build-jar-repository and build-classpath utils

* Tue Aug 12 2014 Gerard Ryan <gerard@ryan.lt> - 3.6.0-6
- Use forceContextQualifier instead of git

* Sat Jul 19 2014 Gerard Ryan <gerard@ryan.lt> - 3.6.0-5
- Add features from webtools.webservices.jaxws

* Sun Jul 06 2014 Gerard Ryan <gerard@ryan.lt> - 3.6.0-4
- Add missing Obsoletes for old sdk packages

* Thu Jul 03 2014 Gerard Ryan <gerard@ryan.lt> - 3.6.0-3
- Add missing BRs

* Tue Jul 01 2014 Gerard Ryan <gerard@ryan.lt> - 3.6.0-2
- Initial RPM

Name:             eclipse-usage
Version:          4.16.0
Release:          2%{?dist}
Summary:          Usage reporting plug-ins for Eclipse

# There are two Apache licensed files, see: https://issues.redhat.com/browse/JBIDE-7410
# - usage/plugins/org.jboss.tools.usage/src/org/jboss/tools/usage/tracker/internal/Tracker.java
# - usage/plugins/org.jboss.tools.usage/src/org/jboss/tools/usage/tracker/internal/FocusPoint.java
# Everything else is Eclipse licensed
License:          EPL-1.0 and ASL 2.0
URL:              http://tools.jboss.org/

# Generate tarball with: ./get-jbosstools.sh
Source0:          jbosstools-%{version}.tar.xz
Source1:          get-jbosstools.sh

# Full text of the license is not included in the tarball
Source2:          https://www.eclipse.org/org/documents/epl-v10.html
Source3:          https://www.apache.org/licenses/LICENSE-2.0.txt

BuildArch:        noarch

# Upstream Eclipse no longer supports non-64bit arches
ExcludeArch: s390 %{arm} %{ix86}

BuildRequires: tycho
BuildRequires: tycho-extras
BuildRequires: maven-install-plugin
BuildRequires: maven-plugin-build-helper

%description
Usage reporting plug-ins for Eclipse.

%prep
%setup -q -n jbosstools-%{version}

cp %{SOURCE2} %{SOURCE3} .

# Fix whitespace error in xml declaration
sed -i -e '1s/\t//' jbosstools-build/parent/pom.xml

# Fix perms on license
chmod -x jbosstools-base/foundation/features/org.jboss.tools.foundation.license.feature/license.html

# Remove unnecessary plugins for RPM build
%pom_remove_plugin org.jboss.tools.tycho-plugins:repository-utils jbosstools-build/parent
%pom_remove_plugin org.jacoco:jacoco-maven-plugin jbosstools-build/parent
%pom_disable_module jacoco-report jbosstools-base
%pom_remove_plugin org.apache.maven.plugins:maven-enforcer-plugin jbosstools-build/parent
%pom_remove_plugin org.sonatype.plugins:nexus-staging-maven-plugin jbosstools-build/parent
%pom_remove_plugin com.googlecode.maven-download-plugin: jbosstools-build/parent
%pom_xpath_remove "pom:plugin[pom:artifactId='tycho-packaging-plugin']/pom:dependencies" jbosstools-build/parent
%pom_xpath_remove "pom:plugin[pom:artifactId='tycho-packaging-plugin']/pom:configuration/pom:sourceReferences" jbosstools-build/parent
%pom_xpath_set "pom:plugin[pom:artifactId='tycho-packaging-plugin']/pom:configuration/pom:timestampProvider" "default" jbosstools-build/parent

# Disable everything except for usage plugin
%pom_disable_module org.jboss.tools.foundation.feature jbosstools-base/foundation/features
%pom_disable_module org.jboss.tools.foundation.security.linux.feature jbosstools-base/foundation/features
%pom_disable_module org.jboss.tools.foundation.test.feature jbosstools-base/foundation/features
%pom_disable_module plugins jbosstools-base/foundation
%pom_disable_module tests jbosstools-base/foundation
%pom_disable_module org.jboss.tools.usage.test.feature jbosstools-base/usage/features
%pom_disable_module org.jboss.tools.usage.test jbosstools-base/usage/tests

# No need to install poms or license feature
%mvn_package "::pom::" __noinstall
%mvn_package ":org.jboss.tools.foundation.license.feature" __noinstall

%build
pushd jbosstools-build
# Install parent pom so main build can reference it
%mvn_build -j -- install -f parent/pom.xml
popd

# Main build
%mvn_build -j -- -Dno-target-platform -f jbosstools-base/pom.xml -e

%install
%mvn_install

%files -f .mfiles
%license epl-v10.html LICENSE-2.0.txt

%changelog
* Mon Aug 17 2020 Mat Booth <mat.booth@redhat.com> - 4.16.0-2
- Licensing clarifications

* Mon Aug 17 2020 Mat Booth <mat.booth@redhat.com> - 4.16.0-1
- Update to latest upstream release

* Wed Nov 20 2019 Mat Booth <mat.booth@redhat.com> - 4.13.0-1
- Update to latest upstream release
- Drop unnecessary dep on epp-logging

* Thu Jun 27 2019 Mat Booth <mat.booth@redhat.com> - 4.11.0-2
- Disable no-longer working AERI endpoint

* Fri Mar 15 2019 Mat Booth <mat.booth@redhat.com> - 4.11.0-1
- Update to latest release
- Update license tag
- Restrict to same architectures as Eclipse itself

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Sep 10 2018 Mat Booth <mat.booth@redhat.com> - 4.9.0-1
- Update to latest upstream release

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 12 2018 Mat Booth <mat.booth@redhat.com> - 4.6.0-0.1
- Update to AM2 release of 4.6.0

* Wed Mar 21 2018 Mat Booth <mat.booth@redhat.com> - 4.5.3-0.1
- Update to AM2 release of 4.5.3

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.2-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Dec 18 2017 Mat Booth <mat.booth@redhat.com> - 4.5.2-0.1
- Update to latest release

* Wed Aug 02 2017 Nick Boldt <nboldt@redhat.com> - 4.5.0-1
- Update to latest release

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 04 2017 Nick Boldt <nboldt@redhat.com> - 4.4.4-1
- Update to latest release

* Tue Jan 17 2017 Mat Booth <mat.booth@redhat.com> - 4.4.3-1
- Update to latest release

* Wed Oct 26 2016 Mat Booth <mat.booth@redhat.com> - 4.4.1-3
- Augment the product ID instead of the distro name

* Fri Oct 21 2016 Mat Booth <mat.booth@redhat.com> - 4.4.1-2
- Trim down the source tarball and fix the license tag

* Tue Sep 27 2016 Mat Booth <mat.booth@redhat.com> - 4.4.1-1
- Initial package

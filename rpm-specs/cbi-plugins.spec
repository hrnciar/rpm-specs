Name:           cbi-plugins
Version:        1.1.7
Release:        4%{?dist}
Summary:        A set of helpers for Eclipse CBI
License:        EPL-1.0
URL:            https://git.eclipse.org/c/cbi/org.eclipse.cbi.git/tree/maven-plugins/README.md

Source0:        https://git.eclipse.org/c/cbi/org.eclipse.cbi.git/snapshot/org.eclipse.cbi_maven-plugin-parent_%{version}.tar.xz

BuildRequires:  maven-local
BuildRequires:  mvn(com.google.auto.value:auto-value)
BuildRequires:  mvn(de.pdark:decentxml)
BuildRequires:  mvn(org.apache.commons:commons-compress)
BuildRequires:  mvn(org.apache.httpcomponents:httpclient)
BuildRequires:  mvn(org.apache.httpcomponents:httpmime)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.eclipse.tycho:tycho-core)
%if %{?rhel}%{!?rhel:0}
# On RHEL 7 need the guava20 package
BuildRequires:  mvn(com.google.guava:guava:20.0)
%endif

# Upstream Eclipse no longer supports non-64bit arches
ExcludeArch: s390 %{arm} %{ix86}
BuildArch: noarch

%description
A set of helpers for Eclipse CBI.

%package javadoc
Summary: Javadoc for %{name}

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n org.eclipse.cbi_maven-plugin-parent_%{version}
%pom_disable_module eclipse-macsigner-plugin maven-plugins
%pom_disable_module eclipse-winsigner-plugin maven-plugins
%pom_disable_module eclipse-dmg-packager maven-plugins
%pom_disable_module eclipse-flatpak-packager maven-plugins

# Disable plugins not needed for RPM builds
%pom_remove_plugin :spotbugs-maven-plugin
%pom_remove_plugin :maven-checkstyle-plugin
%pom_remove_plugin :maven-enforcer-plugin

# Build the common module
%pom_xpath_inject pom:modules "<module>../common/</module>" maven-plugins
%pom_remove_dep org.eclipse.cbi:checkstyle common

# Remove separate annotations requirement of auto
%pom_remove_dep :auto-value-annotations . common maven-plugins/common

# Parent pom and common module are "released" independently, but actually nothing changed yet since last releases
sed -i -e 's/1\.0\.6-SNAPSHOT/1.0.5/' pom.xml
sed -i -e 's/1\.2\.4-SNAPSHOT/1.2.3/' common/pom.xml

# Make dep on guava more forgiving
sed -i -e 's/>28.0-jre</>20.0</' pom.xml

# Don't use static analysis annotations
sed -i -e 's/@Nonnull//' -e '/javax.annotation.Nonnull/d' common/src/main/java/org/eclipse/cbi/common/security/*.java

%build
# Tests require jimfs which is not in Fedora
%mvn_build -f -- -f maven-plugins/pom.xml -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles

%files javadoc -f .mfiles-javadoc

%changelog
* Fri Mar 20 2020 Mat Booth <mat.booth@redhat.com> - 1.1.7-4
- Fix dep on RHEL and avoid using null annotations

* Fri Mar 20 2020 Mat Booth <mat.booth@redhat.com> - 1.1.7-3
- Fix dep on guava to be more accepting

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Dec 17 2019 Mat Booth <mat.booth@redhat.com> - 1.1.7-1
- Update to latest upstream release

* Tue Dec 17 2019 Mat Booth <mat.booth@redhat.com> - 1.1.5-7
- Restrict to same architectures as Eclipse itself

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 15 2019 Mat Booth <mat.booth@redhat.com> - 1.1.5-5
- Disable plugins that are not relevant for RPM builds (reduces the dep tree)
- Fix license tag

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Apr 29 2018 Mat Booth <mat.booth@redhat.com> - 1.1.5-2
- Disable unnecessary enforcer checks

* Thu Apr 26 2018 Mat Booth <mat.booth@redhat.com> - 1.1.5-1
- Update to latest upstream release

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 09 2016 Mat Booth <mat.booth@redhat.com> - 1.1.3-1
- Update to 1.1.3 release

* Fri Dec  9 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1.2-5
- Regenerate build-requires
- Resolves: rhbz#1403033

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jun 22 2015 Mat Booth <mat.booth@redhat.com> - 1.1.2-3
- Drop unnecessary requires

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 22 2015 Alexander Kurtakov <akurtako@redhat.com> 1.1.2-1
- Update to upstream 1.1.2 release.

* Mon Jul 28 2014 Roland Grunberg <rgrunber@redhat.com> - 1.1.1-2
- Update to 1.1.1 Release.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 1.0.5-3
- Use Requires: java-headless rebuild (#1067528)

* Wed Nov 13 2013 Alexander Kurtakov <akurtako@redhat.com> 1.0.5-2
- Disable win/mac signers.

* Wed Nov 13 2013 Alexander Kurtakov <akurtako@redhat.com> 1.0.5-1
- Update to latest upstream.

* Mon Sep 30 2013 Krzysztof Daniel <kdaniel@redhat.com> 1.0.4-1
- Update to latest upstream.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon May 27 2013 Krzysztof Daniel <kdaniel@redhat.com> 1.0.3-1
- Update to latest upstream.

* Thu Mar 14 2013 Krzysztof Daniel <kdaniel@redhat.com> 1.0.1-0.4.git734d40
- Update to latest upstream.

* Thu Feb 21 2013 Krzysztof Daniel <kdaniel@redhat.com> 1.0.1-0.3.git120561
- Delete empty line from sources.

* Thu Feb 21 2013 Krzysztof Daniel <kdaniel@redhat.com> 1.0.1-0.2.git120561
- Review remarks fixed.

* Thu Feb 21 2013 Krzysztof Daniel <kdaniel@redhat.com> 1.0.1-0.1.git120561
- Initial contribution.

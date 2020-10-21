Name:      jacoco
Version:   0.8.3
Release:   4%{?dist}
Summary:   Java Code Coverage for Eclipse 
License:   EPL
URL:       http://www.eclemma.org/jacoco/
Source0:   https://github.com/jacoco/jacoco/archive/v%{version}.tar.gz
Source1:   EnchancedManifest.mf

BuildArch:        noarch

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven:maven-project)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-assembly-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-shade-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.apache.maven.reporting:maven-reporting-api)
BuildRequires:  mvn(org.apache.maven.reporting:maven-reporting-impl)
BuildRequires:  mvn(org.apache.maven.shared:file-management)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.codehaus.mojo:buildnumber-maven-plugin)
BuildRequires:  mvn(org.codehaus.mojo:exec-maven-plugin)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.jacoco:org.jacoco.build:pom:)
BuildRequires:  mvn(org.ow2.asm:asm-debug-all)
BuildRequires:  dos2unix


%description
JaCoCo is a free code coverage library for Java, 
which has been created by the EclEmma team based on the lessons learned 
from using and integration existing libraries over the last five years. 


%package    javadoc
Summary:    Java-docs for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%package    maven-plugin
Summary:    A Jacoco plugin for maven

%description maven-plugin
A Jacoco plugin for maven.

%prep
%setup -q 

# Make it work with ASM 6.0
# TODO: forward upstream
#sed -i '/org.objectweb.asm/s/version="[^"]*"/bundle-version="[5.1.0,7.0.0)"/' $(find -name \*.MF)

%pom_disable_module ../org.jacoco.examples org.jacoco.build
%pom_disable_module ../org.jacoco.doc org.jacoco.build
%pom_disable_module ../org.jacoco.tests org.jacoco.build
%pom_disable_module ../jacoco org.jacoco.build

%mvn_package ":jacoco-maven-plugin:{jar,pom}:{}:" maven-plugin
%mvn_package ":{org.}*:{jar,pom}:runtime:"

sed -i -e "s|nb-configuration.xml|nb-configuration.xml,build.xml, pom.xml|g" org.jacoco.build/pom.xml

# Remove unnecessary dependency on maven-javadoc-plugin
%pom_remove_plugin -r :maven-javadoc-plugin

# Remove enforcer plugin that causes build failure of 'Jacoco :: Maven Plugin'
%pom_remove_plugin -f -r org.apache.maven.plugins:maven-enforcer-plugin

%pom_remove_plugin -f -r com.github.genthaler:beanshell-maven-plugin
%pom_remove_plugin -f -r com.diffplug.spotless:spotless-maven-plugin
%pom_remove_plugin -f -r org.apache.felix:maven-bundle-plugin

# Add execution config for maven.antrun.plugin
%pom_xpath_inject pom:plugin[pom:artifactId=\'maven-antrun-plugin\']/pom:executions '<execution>
             <id>parse-version</id>
             <phase>validate</phase>
             <goals>
               <goal>run</goal>
             </goals>
             <configuration>
                <target>
                     <property name="jacoco.runtime.package.name" value="org.jacoco.agent.rt.internal_${randomNumber}" />
               </target>
               <exportAntProperties>true</exportAntProperties>
             </configuration>
           </execution>' org.jacoco.build/pom.xml

for x in `find | grep "/pom.xml$"` ; do sed -i "s|<manifestFile>.*/META-INF/MANIFEST.MF</manifestFile>||" $x  ; done

%build
%mvn_build --xmvn-javadoc -f -- -Dproject.build.sourceEncoding=UTF-8

# workaround missing premain in agent.rt RH1151442. Not sure where to fix this in build.
# TODO, fix in build itself
# 'all' have already premain, 'sources' don't need.
a=`find org.jacoco.agent.rt/target/ | grep jar | grep -v -e sources -e all`
for x in $a ; do
jar -umf %{SOURCE1}  $x
done;

%install
%mvn_install

# ant config
mkdir -p %{buildroot}%{_sysconfdir}/ant.d
echo %{name} %{name}/org.jacoco.ant objectweb-asm/asm-debug-all > %{buildroot}%{_sysconfdir}/ant.d/%{name}

%files -f .mfiles
%dir %{_javadir}/%{name}
%config(noreplace) %{_sysconfdir}/ant.d/%{name}
%doc org.jacoco.doc/docroot/*
%doc org.jacoco.doc/about.html

%files maven-plugin -f .mfiles-maven-plugin

%files javadoc -f .mfiles-javadoc

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 18 2020 Fabio Valentini <decathorpe@gmail.com> - 0.8.3-3
- Remove unnecessary dependency on maven-javadoc-plugin.
- Use xmvn-javadoc unconditionally, fixing javadoc generation.
- Add files for javadoc subpackage.

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 0.8.3-2
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Thu Apr 02 2020 Jiri Vanek <jvanek@redhat.com> 0.8.3-1
- bumped to sources 8.3 which are aligned with currenlty shiped ojkectweb-asm
- aligned pugins with current fedora state
- org.apache.felix:maven-bundle-plugin should be returned, its absence is killing jdk11 exported packages generation
- the manual manifest is not an option

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Sep 12 2017 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.7.8-4
- Relax OSGi version requirements on ASM

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Alexander Kurtakov <akurtako@redhat.com> 0.7.8-1
- Update to upstream 0.7.8.

* Thu Aug 25 2016 Roman Vais <rvais@redhat.com> - 0.7.7-3
- Remove outdated dependency and enforcer plugin
- Replace problematic patch with pom_xpath_inject macro

* Thu Jun 16 2016 Alexander Kurtakov <akurtako@redhat.com> 0.7.7-2
- Add missing BRs.

* Tue Jun 7 2016 Alexander Kurtakov <akurtako@redhat.com> 0.7.7-1
- Update to upstream 0.7.7.

* Fri Feb 19 2016 Alexander Kurtakov <akurtako@redhat.com> 0.7.6-1
- Update to upstream 0.7.6.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed May 27 2015 Alexander Kurtakov <akurtako@redhat.com> 0.7.5-1
- Update to upstream 0.7.5.

* Tue Mar 31 2015 akurtakov <akurtakov@localhost.localdomain> 0.7.4-1
- Update to upstream 0.7.4.

* Mon Feb 23 2015 Alexander Kurtakov <akurtako@redhat.com> 0.7.3-1
- Update to upstream 0.7.3.

* Mon Feb 16 2015 Alexander Kurtakov <akurtako@redhat.com> 0.7.2-3
- Add asm to ant.d (RHBZ#1192749).

* Sat Oct 11 2014 Jiri Vanek <jvanek@redhat.com> 0.7.2-2
- added premain-class to agent.rt.jar
- RH1151442

* Mon Sep 15 2014 Alexander Kurtakov <akurtako@redhat.com> 0.7.2-1
- Update to upstream 0.7.2.

* Fri Jun 13 2014 Michal Srb <msrb@redhat.com> - 0.7.1-5
- Migrate to %%mvn_install

* Mon Jun 9 2014 Alexander Kurtakov <akurtako@redhat.com> 0.7.1-4
- Fix FTBFS.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 12 2014 Alexander Kurtakov <akurtako@redhat.com> 0.7.1-1
- Update to 0.7.1.

* Thu Mar 27 2014 Alexander Kurtakov <akurtako@redhat.com> 0.7.0-1
- Update to upstream version 0.7.0.

* Thu Mar 6 2014 Alexander Kurtakov <akurtako@redhat.com> 0.6.5-1
- Update to new upstream release.
- Remove licence check ant call - breaks in rawhide.

* Mon Feb 24 2014 Orion Poplawski <orion@cora.nwra.com> 0.6.4-3
- Add ant config

* Fri Feb 21 2014 Alexander Kurtakov <akurtako@redhat.com> 0.6.4-2
- R java-headless.
- Adapt to new package names.
- Fix rpmlint warnings.

* Thu Dec 19 2013 Alexander Kurtakov <akurtako@redhat.com> 0.6.4-1
- Update to 0.6.4 upstream release.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 22 2013 Krzysztof Daniel <kdaniel@redhat.com> 0.6.3-4
- Move maven plugin to the %%{javadir}.

* Mon Jul 22 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.6.3-3
- Move plugin artifact to plugin subpackage
- Resolves: rhbz#987084

* Thu Jun 20 2013 Krzysztof Daniel <kdaniel@redhat.com> 0.6.3-2
- Add missing BR.

* Thu Jun 20 2013 Krzysztof Daniel <kdaniel@redhat.com> 0.6.3-1
- Update to 0.6.3.

* Wed May 8 2013 Krzysztof Daniel <kdaniel@redhat.com> 0.6.2-1
- Update to latest upstream.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Dec 10 2012 Krzysztof Daniel <kdaniel@redhat.com> 0.6.0-3
- Merge the master branch in.

* Thu Nov 29 2012 Krzysztof Daniel <kdaniel@redhat.com> 0.6.0-2
- Package correct agent.
- Improve the name of packages.

* Wed Nov 21 2012 Alexander Kurtakov <akurtako@redhat.com> 0.6.0-1
- Update to upstream 0.6.0.

* Mon Sep 17 2012 Krzysztof Daniel <kdaniel@redhat.com> 0.5.9-2
- Add BR to fest-assert.

* Tue Sep 11 2012 Krzysztof Daniel <kdaniel@redhat.com> 0.5.9-1
- Update to upstream 0.5.10 release.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.7-0.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue May 8 2012 Krzysztof Daniel <kdaniel@redhat.com> 0.5.7-0.5
- Dropped dependency version to maven-shade-plugin.

* Tue May 8 2012 Krzysztof Daniel <kdaniel@redhat.com> 0.5.7-0.4
- Fixed rpmlint warnings.

* Tue May 8 2012 Krzysztof Daniel <kdaniel@redhat.com> 0.5.7-0.3
- Removed symlink to java.

* Tue May 8 2012 Krzysztof Daniel <kdaniel@redhat.com> 0.5.7-0.2
- Restructured packages
- Generated javadoc as set of plain files.

* Thu May 3 2012 Krzysztof Daniel <kdaniel@redhat.com> 0.5.7-0.1
- Initial release.

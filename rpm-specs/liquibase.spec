Name: liquibase
Summary: Database Refactoring Tool
Version: 3.7.0
Release: 1%{?dist}
License: ASL 2.0
URL: http://www.liquibase.org

Source0: https://github.com/liquibase/liquibase/archive/%{name}-parent-%{version}.tar.gz

BuildRequires: java-devel >= 0:1.8.0
BuildRequires: javapackages-tools
BuildRequires: maven-local
BuildRequires: mvn(ch.qos.logback:logback-classic)
BuildRequires: mvn(commons-cli:commons-cli)
BuildRequires: mvn(javax.enterprise:cdi-api)
BuildRequires: mvn(javax.servlet:servlet-api)
BuildRequires: mvn(org.apache.ant:ant)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.felix:org.apache.felix.framework)
BuildRequires: mvn(org.apache.maven:maven-compat)
BuildRequires: mvn(org.apache.maven.plugins:maven-assembly-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires: mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires: mvn(org.codehaus.mojo:javacc-maven-plugin)
BuildRequires: mvn(org.slf4j:slf4j-api)
BuildRequires: mvn(org.yaml:snakeyaml) >= 1.23

BuildArch:     noarch

Requires: java-headless >= 0:1.8.0
Requires: javapackages-filesystem
Requires: mvn(ch.qos.logback:logback-classic)
Requires: mvn(commons-cli:commons-cli)
Requires: mvn(org.apache.felix:org.apache.felix.framework)
Requires: mvn(org.slf4j:slf4j-api)
Requires: mvn(org.yaml:snakeyaml) >= 0:1.13

%description
LiquiBase is an open source (Apache 2.0 License), database-independent library
for tracking, managing and applying database changes. It is built on a simple
premise: All database changes are stored in a human readable but tracked in
source control.


%package javadoc
Summary: API documentation for %{name}
%description javadoc
This package contains %{summary}.


%package cdi
Summary: Liquibase CDI
Requires: %{name} = %{version}-%{release}
Requires: mvn(javax.enterprise:cdi-api)
%description cdi
Liquibase CDI extension.


%package parent
Summary: Liquibase Parent Configuration POM
%description parent
This package contains the %{summary}.


%package maven-plugin
Summary: Maven plugin for %{name}
BuildRequires: mvn(org.apache.maven:maven-plugin-api)
BuildRequires: mvn(org.apache.maven:maven-project)
BuildRequires: mvn(org.apache.maven.plugins:maven-plugin-plugin)
Requires: %{name} = %{version}-%{release}
Requires: mvn(org.apache.maven:maven-plugin-api)
Requires: mvn(org.apache.maven:maven-project)
Requires: maven
%description maven-plugin
%{summary}.


%prep
%setup -q -n %{name}-%{name}-parent-%{version}

find -name "*.bat" -print -delete
find -name "*.class" -print -delete
find -name "*.jar" -print -delete
# Spring isn't packaged with Fedora at the moment
find -wholename "*/integration/spring/*.java" -print -delete
# Do not bundle javascript libraries and fonts
find -name "*.js" -print -delete
rm -r %{name}-core/src/main/resources/liquibase/sdk
rm -r %{name}-core/src/main/resources/assembly
rm -r %{name}-core/src/main/resources/dist

%pom_disable_module %{name}-integration-tests
%pom_disable_module %{name}-debian
%pom_disable_module %{name}-rpm

# Use Maven 3 APIs only
%pom_change_dep -r :maven-project :maven-compat

# Unavailable plugin
%pom_remove_plugin -r :gmaven-plugin
# Unwanted tasks or tasks that break the build
%pom_remove_plugin -r :maven-assembly-plugin
%pom_remove_plugin -r :maven-javadoc-plugin
%pom_remove_plugin -r :maven-source-plugin
%pom_remove_plugin -r :maven-deploy-plugin

%pom_remove_dep -r org.springframework:spring-beans
%pom_remove_dep -r org.springframework:spring-context
%pom_remove_dep -r org.springframework:spring-core
%pom_remove_dep -r com.github.stefanbirkner:system-rules
%pom_remove_dep -r org.osgi:org.osgi.core
%pom_add_dep org.apache.felix:org.apache.felix.framework %{name}-core

# Disable test jar
%pom_xpath_remove "pom:finalName" %{name}-core

# Symlink liquibase/liquibase-core.jar to liquibase.jar
%mvn_file :%{name}-core %{name}/%{name}-core %{name}


%build
# No tests (-f) and singleton packaging (-s) (i.e. one artifact per package)
%mvn_build -s -f


%install
%mvn_install
%jpackage_script liquibase.integration.commandline.Main "" "" %{name}/%{name}-core:logback/logback-core:logback/logback-classic:slf4j/slf4j-api %{name} true
mkdir -p %{buildroot}%{_mandir}/man1
install -pm 0644 %{name}-rpm/src/main/resources/%{name}.1 %{buildroot}%{_mandir}/man1/


%files -f .mfiles-%{name}-core
%doc changelog.txt %{name}-core/DEV_NOTES.txt
%license LICENSE.txt
%doc %{_mandir}/man1/%{name}.1*
%{_bindir}/%{name}

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt

%files parent -f .mfiles-%{name}-parent
%license LICENSE.txt

%files cdi -f .mfiles-%{name}-cdi
%license LICENSE.txt

%files maven-plugin -f .mfiles-%{name}-maven-plugin

%changelog
* Mon Feb 03 2020 Alex Wood <awood@redhat.com> 3.7.0-1
- Update to 3.7.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 26 2019 Alex Wood <awood@redhat.com> 3.6.3-1
- Update to 3.6.3

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Apr 12 2018 Alex Wood <awood@redhat.com> 3.6.1-1
- Update to 3.6.1

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Dec 04 2017 Alex Wood <awood@redhat.com> 3.5.3-4
- Apply patch to address https://liquibase.jira.com/browse/CORE-2933

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Oct 14 2016 Alex Wood <awood@redhat.com> 3.5.3-1
- Update to 3.5.3

* Fri May 13 2016 Alex Wood <awood@redhat.com> 3.5.1-1
- Update to 3.5.1
- Bring package build into compliance with Java packaging guidelines

* Fri Apr 22 2016 Alex Wood <awood@redhat.com> 3.5.0-1
- Update to 3.5.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Sep 15 2015 Alex Wood <awood@redhat.com> 3.4.1-1
- Update to 3.4.1

* Tue Jul 07 2015 Alex Wood <awood@redhat.com> 3.4.0-1
- Update to 3.4.0

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Nov 04 2014 Alex Wood <awood@redhat.com> 3.3.0-1
- Update to 3.3.0

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 27 2014 Alex Wood <awood@redhat.com> 3.1.1-1
- Update to 3.1.1
- Switch to Maven based build

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 3.1.0-2
- Use Requires: java-headless rebuild (#1067528)

* Mon Jan 13 2014 Alex Wood <awood@redhat.com> 3.1.0-1
- Update to 3.1.0

* Mon Oct 28 2013 Alex Wood <awood@redhat.com> - 3.0.7-4
- Update to 3.0.7.
- Use jpackage-utils to generate launch script.
- Split javadoc into separate package.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Apr 17 2013 Alex Wood <awood@redhat.com> 2.0.5-2
- Build now requires servlet3 instead of servlet25.

* Wed Apr 03 2013 Alex Wood <awood@redhat.com> 2.0.5-1
- Updating to liquibase 2.0.5.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu May 03 2012 Devan Goodwin <dgoodwin@rm-rf.ca> 2.0.3-7
- 818510: Fix offline failures looking for dbchangelog XSD.
  (dgoodwin@redhat.com)

* Mon Apr 16 2012 Devan Goodwin <dgoodwin@rm-rf.ca> 2.0.3-6
- Generate and package javadocs.
- Cleanup rpmlint warnings.
- Switched to using javadir macro.
- Switched to using build-classpath in launcher.
* Tue Apr 03 2012 Devan Goodwin <dgoodwin@rm-rf.ca> 2.0.3-5
- Spec cleanup. (dgoodwin@redhat.com)

* Mon Apr 02 2012 Devan Goodwin <dgoodwin@rm-rf.ca> 2.0.3-4
- Fix missing javax.servlet during compile. (dgoodwin@redhat.com)

* Fri Mar 30 2012 Devan Goodwin <dgoodwin@rm-rf.ca> 2.0.3-3
- Include documentation, better tar.gz generation. (dgoodwin@redhat.com)
- Add custom launcher script. (dgoodwin@redhat.com)
- Add build.xml to compile. (dgoodwin@redhat.com)

* Thu Mar 29 2012 Devan Goodwin <dgoodwin@redhat.com> 2.0.3-2
- Initial packaging attempt.



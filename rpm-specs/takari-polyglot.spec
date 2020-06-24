Name:          takari-polyglot
Version:       0.4.4
Release:       6%{?dist}
Summary:       Modules to enable Maven usage in other JVM languages
License:       EPL-1.0
URL:           https://github.com/takari/polyglot-maven
Source0:       https://github.com/takari/polyglot-maven/archive/polyglot-%{version}.tar.gz

Patch0: 0001-Revert-072fbcb-to-fix-problem-with-building-Eclipse.patch

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-model)
BuildRequires:  mvn(org.apache.maven:maven-model-builder)
BuildRequires:  mvn(org.apache.maven:maven-parent:pom:)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-annotations)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.eclipse.sisu:org.eclipse.sisu.plexus)
BuildRequires:  mvn(org.slf4j:slf4j-api)

BuildArch:     noarch

# Package was renamed upstream tesla -> takari F31
Provides:  tesla-polyglot = %{version}-%{release}
Obsoletes: tesla-polyglot < 0.4.4-3

%description
Polyglot for Maven is an experimental distribution of Maven
that allows the expression of a POM in something other than
XML. A couple of the dialects also have the capability to
write plugins inline: the Groovy, Ruby and Scala dialects
allow this.

%package atom
Summary: Takari Polyglot :: Atom
# Package was renamed upstream tesla -> takari F31
Provides:  tesla-polyglot-atom = %{version}-%{release}
Obsoletes: tesla-polyglot-atom < 0.4.4-3

%description atom
Takari Polyglot :: Atom.

%package common
Summary: Takari Polyglot :: Common
# Package was renamed upstream tesla -> takari F31
Provides:  tesla-polyglot-common = %{version}-%{release}
Obsoletes: tesla-polyglot-common < 0.4.4-3

# Obsoletes added for retired sub-packages in F31
Obsoletes: tesla-polyglot-groovy < 0.4.4-3
Obsoletes: tesla-polyglot-yaml < 0.4.4-3

%description common
Takari Polyglot :: Common.

%package xml
Summary: Takari Polyglot :: XML
# Package was renamed upstream tesla -> takari F31
Provides:  tesla-polyglot-xml = %{version}-%{release}
Obsoletes: tesla-polyglot-xml < 0.4.4-3

%description xml
Takari Polyglot :: XML.

%package maven-plugin
Summary: Takari Polyglot :: Maven Plugin
# Package was renamed upstream tesla -> takari F31
Provides:  tesla-polyglot-maven-plugin = %{version}-%{release}
Obsoletes: tesla-polyglot-maven-plugin < 0.4.4-3

%description maven-plugin
This package contains Takari Polyglot Maven Plugin.

%package translate-plugin
Summary: Polyglot :: Translate Plugin
# Package was renamed upstream tesla -> takari F31
Provides:  tesla-polyglot-translate-plugin = %{version}-%{release}
Obsoletes: tesla-polyglot-translate-plugin < 0.4.4-3

%description translate-plugin
This package contains Polyglot Translate Plugin.

%package javadoc
Summary: Javadoc for %{name}
# Package was renamed upstream tesla -> takari F31
Provides:  tesla-polyglot-javadoc = %{version}-%{release}
Obsoletes: tesla-polyglot-javadoc < 0.4.4-3

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n polyglot-maven-polyglot-%{version}
%patch0 -p1

find -name "*.class" -delete
find -name "*.jar" -delete

# Unecessary for RPM builds
%pom_remove_plugin ":maven-enforcer-plugin"

# Takari stack is unavailable, so build like an ordinary maven plugin project
%pom_remove_parent
%pom_xpath_remove "pom:packaging" polyglot-common polyglot-atom polyglot-xml
%pom_xpath_set "pom:packaging" "maven-plugin" polyglot-maven-plugin polyglot-translate-plugin
%pom_add_plugin org.apache.maven.plugins:maven-compiler-plugin:3.0 '
<configuration>
 <source>1.8</source>
 <target>1.8</target>
 <encoding>UTF-8</encoding>
</configuration>'
for p in maven-plugin translate-plugin; do
  %pom_add_plugin "org.apache.maven.plugins:maven-plugin-plugin" polyglot-${p} "
  <configuration>
    <skipErrorNoDescriptorsFound>true</skipErrorNoDescriptorsFound>
  </configuration>"
  %pom_xpath_inject "pom:dependency[pom:groupId = 'org.apache.maven']" "<version>3.3.1</version>" polyglot-${p}
done
%pom_xpath_inject "pom:project/pom:dependencies/pom:dependency[pom:groupId = 'org.apache.maven']" '<version>${mavenVersion}</version>'

# Unavailable build deps/tools
%pom_disable_module polyglot-clojure
%pom_disable_module polyglot-scala
%pom_remove_dep -r :polyglot-scala
%pom_disable_module polyglot-ruby
%pom_remove_dep -r :polyglot-ruby
%pom_disable_module polyglot-groovy
%pom_remove_dep -r :polyglot-groovy
%pom_disable_module polyglot-java
%pom_remove_dep -r :polyglot-java
%pom_disable_module polyglot-kotlin
%pom_remove_dep -r :polyglot-kotlin
%pom_disable_module polyglot-yaml
%pom_remove_dep -r :polyglot-yaml

# Test dep com.cedarsoftware:java-util:1.19.3 is missing from Fedora
sed -i '/DeepEquals/d' polyglot-xml/src/test/java/org/sonatype/maven/polyglot/xml/TestReaderComparedToDefault.java
%pom_remove_dep com.cedarsoftware:java-util polyglot-xml

# Back-compat aliases
%mvn_alias ':polyglot-{*}' io.tesla.polyglot:tesla-polyglot-@1

%build
%mvn_build -s -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles-polyglot
%doc poms
%license LICENSE.txt

%files atom -f .mfiles-polyglot-atom

%files common -f .mfiles-polyglot-common
%license LICENSE.txt

%files xml -f .mfiles-polyglot-xml
%doc polyglot-xml/README.md

%files maven-plugin -f .mfiles-polyglot-maven-plugin

%files translate-plugin -f .mfiles-polyglot-translate-plugin

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt

%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 20 2019 Mat Booth <mat.booth@redhat.com> - 0.4.4-5
- Add missing requires/obsoletes

* Thu Dec 19 2019 Mat Booth <mat.booth@redhat.com> - 0.4.4-4
- Fix building Eclipse with tycho pomless

* Tue Dec 17 2019 Mat Booth <mat.booth@redhat.com> - 0.4.4-3
- Fixed review feedback items

* Tue Dec 17 2019 Mat Booth <mat.booth@redhat.com> - 0.4.4-2
- Rename package tesla-polyglot -> takari-polyglot

* Tue Dec 10 2019 Mat Booth <mat.booth@redhat.com> - 0.4.4-1
- Update to latest upstream release

* Tue Dec 10 2019 Mat Booth <mat.booth@redhat.com> - 0.2.1-9
- Use bootstrap mode all the time due to unavailability of takari stack
- Obsolete groovy and yaml support
- Use upstream distributed license

* Tue Jun 25 2019 Mat Booth <mat.booth@redhat.com> - 0.2.1-8
- Add obsoletes for unbuilt modules

* Tue May 07 2019 Mat Booth <mat.booth@redhat.com> - 0.2.1-7
- Restrict to same architectures as Eclipse itself

* Wed Apr 24 2019 Mat Booth <mat.booth@redhat.com> - 0.2.1-6
- Add a bootstrap mode

* Thu Apr 18 2019 Mat Booth <mat.booth@redhat.com> - 0.2.1-5
- Update license tag and general specfile cleanup

* Wed Feb 20 2019 Mat Booth <mat.booth@redhat.com> - 0.2.1-4
- Conditionally build yaml support

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 08 2018 Mat Booth <mat.booth@redhat.com> - 0.2.1-1
- Update to latest release
- Conditionally build groovy support

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Sep 20 2017 Michael Simacek <msimacek@redhat.com> - 0.2.0-1
- Update to upstream version 0.2.0

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Nov 18 2016 Michael Simacek <msimacek@redhat.com> - 0.1.19-1
- Update to upstream version 0.1.19

* Tue Aug 09 2016 gil cattaneo <puntogil@libero.it> 0.1.18-3
- add missing build requires: xmvn

* Sun Jul 03 2016 gil cattaneo <puntogil@libero.it> 0.1.18-2
- enable xml module
- use gmavenplus-plugin

* Tue Jun 21 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.1.18-1
- Update to upstream version 0.1.18

* Wed Jun 15 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.1.14-3
- Add missing build-requires

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 08 2016 gil cattaneo <puntogil@libero.it> 0.1.14-1
- update to 0.1.14
- enable (snake)YAML support

* Sat Jul 18 2015 gil cattaneo <puntogil@libero.it> 0.1.8-4
- fix FTBFS rhbz#1240065
- disable ruby module rhbz#1234368

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue May 19 2015 Michal Srb <msrb@redhat.com> - 0.1.8-2
- Build ruby module

* Mon Apr 20 2015 gil cattaneo <puntogil@libero.it> 0.1.8-1
- update to 0.1.8

* Mon Apr 20 2015 gil cattaneo <puntogil@libero.it> 0.1.6-2
- disable takari-pom support

* Mon Apr 13 2015 gil cattaneo <puntogil@libero.it> 0.1.6-1
- update to 0.1.6

* Thu Feb 12 2015 gil cattaneo <puntogil@libero.it> 0.1.0-3
- introduce license macro

* Thu Oct 23 2014 gil cattaneo <puntogil@libero.it> 0.1.0-2
- add BR on ant-junit
- added alias needed by Gradle

* Sun May 25 2014 gil cattaneo <puntogil@libero.it> 0.1.0-1
- initial rpm

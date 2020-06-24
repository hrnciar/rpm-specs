# empty debuginfo
%global debug_package %nil

Name:             snappy-java
Version:          1.1.2.4
Release:          15%{?dist}
Summary:          Fast compressor/decompresser
License:          ASL 2.0
URL:              http://xerial.org/snappy-java/
Source0:          https://github.com/xerial/snappy-java/archive/%{version}.tar.gz
# Not able to build snappy-java jni library with sbt:
# use sbt = 0.13.8 (use scala 2.11.6) available 0.13.1 (use scala 2.10.4)
# Too many missing plugins:
# com.etsy:sbt-checkstyle-plugin:0.4.3
# com.github.gseitz:sbt-release:1.0.0
# com.jsuereth:sbt-pgp:1.0.0
# com.typesafe.sbt:sbt-osgi:0.7.0
# de.johoop:findbugs4sbt:1.4.0
# de.johoop:jacoco4sbt:2.1.5
# org.xerial.sbt:sbt-sonatype:0.5.0
Source1:          http://central.maven.org/maven2/org/xerial/snappy/%{name}/%{version}/%{name}-%{version}.pom
Patch0:           snappy-java-1.1.2-build.patch
Patch1:           snappy-java-1.1.2.4-lsnappy.patch

# Use "javac -h" because "javah" command disappeared in java 11
Patch2:           javah-adaptation.patch

BuildRequires:    make
BuildRequires:    gcc-c++
BuildRequires:    libstdc++-static
BuildRequires:    snappy-devel

BuildRequires:    maven-local
BuildRequires:    mvn(com.sun:tools)
BuildRequires:    mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:    mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:    mvn(org.osgi:osgi.core)

Requires:         snappy

%description
A Java port of the snappy, a fast compresser/decompresser written in C++.

%package javadoc
Summary:          Javadoc for %{name}
BuildArch:        noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q
# Cleanup
find -name "*.class" -print -delete
find -name "*.jar" -print -delete
rm -r ./*sbt* project

# Remove prebuilt libraries
find -name "*.jnilib" -print -delete
find -name "*.dll" -print -delete
find -name "*.so" -print -delete
find -name "*.a" -print -delete
find -name "*.h" -print -delete

%patch0 -p1
%patch1 -p1
%patch2

cp %{SOURCE1} pom.xml
%pom_xpath_remove "pom:dependency[pom:scope = 'test']"

# use osgi-core instead of felix-osgi-core
%pom_change_dep :org.osgi.core org.osgi:osgi.core

# Build JNI library
%pom_add_plugin org.apache.maven.plugins:maven-antrun-plugin . '
<dependencies>
 <dependency>
  <groupId>com.sun</groupId>
  <artifactId>tools</artifactId>
  <version>1.8.0</version>
 </dependency>
</dependencies>

<executions>
  <execution>
  <id>compile</id>
  <phase>process-classes</phase>
    <configuration>
      <target>
       <javac destdir="lib"
         srcdir="src/main/java"
         source="${maven.compiler.source}" target="${maven.compiler.target}" debug="on"
         classpathref="maven.plugin.classpath">
         <include name="**/OSInfo.java"/>
       </javac>
       <exec executable="make" failonerror="true">
        <arg line="%{?_smp_mflags}"/>
       </exec>
      </target>
    </configuration>
    <goals>
      <goal>run</goal>
    </goals>
  </execution>
</executions>'
# Add OSGi support
%pom_add_plugin org.apache.felix:maven-bundle-plugin:2.5.4 . '
<extensions>true</extensions>
<configuration>
  <instructions>
    <Bundle-Activator>org.xerial.snappy.SnappyBundleActivator</Bundle-Activator>
    <Bundle-ActivationPolicy>lazy</Bundle-ActivationPolicy>
    <Bundle-SymbolicName>${project.groupId}.${project.artifactId}</Bundle-SymbolicName>
    <Bundle-Version>${project.version}</Bundle-Version>
    <Import-Package>org.osgi.framework,*</Import-Package>
  </instructions>
</configuration>
<executions>
  <execution>
    <id>bundle-manifest</id>
    <phase>process-classes</phase>
    <goals>
      <goal>manifest</goal>
    </goals>
  </execution>
</executions>'

chmod 644 NOTICE README.md
# Convert from dos to unix line ending
for file in LICENSE NOTICE README.md; do
 sed -i.orig 's|\r||g' $file
 touch -r $file.orig $file
 rm $file.orig
done

%build

CXXFLAGS="${CXXFLAGS:-%optflags}"
export CXXFLAGS
# No test deps available:
#    org.xerial.java:xerial-core:2.1
#    org.xerial:xerial-core:3.2.3
#    org.scalatest:scalatest_2.11:2.2.0
#    com.novocode:junit-interface:0.10
%mvn_build -f -- -Dproject.build.sourceEncoding=UTF-8 -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8

%install
%mvn_install

%files -f .mfiles
%doc README.md
%license LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%license LICENSE NOTICE

%changelog
* Fri Jun 19 2020 Mat Booth <mat.booth@redhat.com> - 1.1.2.4-15
- Allow building against Java 11

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Sep 18 2019 Fabio Valentini <decathorpe@gmail.com> - 1.1.2.4-13
- Migrate from the obsolete felix-osgi-core to osgi-core.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb 13 2017 Michael Simacek <msimacek@redhat.com> - 1.1.2.4-6
- Let the tooling find the JVM

* Mon Feb 13 2017 Michael Simacek <msimacek@redhat.com> - 1.1.2.4-5
- Add BR on make and g++

* Fri Feb 10 2017 Pavel Raiskup <praiskup@redhat.com> 1.1.2.4-4
- fail the build if the nested 'make' fails (rhbz#1421088)

* Thu Feb 09 2017 gil cattaneo <puntogil@libero.it> 1.1.2.4-3
- fix for rhbz#1420790 (link correctly against libsnappy.so)

* Mon Jun 20 2016 gil cattaneo <puntogil@libero.it> 1.1.2.4-2
- add missing build requires

* Wed Mar 09 2016 Ricardo Arguello <ricardo@fedoraproject.org> - 1.1.2.4-1
- Update to 1.1.2.4

* Wed Mar 09 2016 gil cattaneo <puntogil@libero.it> - 1.1.2.1-1
- Update to 1.1.2.1

* Mon Sep 21 2015 gil cattaneo <puntogil@libero.it> - 1.0.5-5
- update Url and Source0 fields
- minor changes to adapt to current guideline
- introduce license macro

* Thu Jul 23 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0.5-4
- Build as archful package
- Resolves: rhbz#1245629

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 3 2014 Ricardo Arguello <ricardo@fedoraproject.org> - 1.0.5-1
- Update to 1.0.5
- Use the snappy package instead of a precompiled library

* Mon Mar 31 2014 Ricardo Arguello <ricardo@fedoraproject.org> - 1.0.4.1-8
- Switch to XMvn
- Use pom macros

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 1.0.4.1-7
- Use Requires: java-headless rebuild (#1067528)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.0.4.1-4
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Mar 4 2012 Ricardo Arguello <ricardo@fedoraproject.org> - 1.0.4.1-2
- Cleanup of the spec file

* Tue Feb 21 2012 Marek Goldmann <mgoldman@redhat.com> - 1.0.4.1-1
- Initial packaging

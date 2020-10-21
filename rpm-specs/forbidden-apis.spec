Name:          forbidden-apis
Version:       2.5
Release:       9%{?dist}
Summary:       Policeman's Forbidden API Checker
License:       ASL 2.0
URL:           https://github.com/policeman-tools/forbidden-apis
Source0:       https://github.com/policeman-tools/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

# Avoid bundling deps
Patch0:        avoid-jarjar-bundling.patch

# Port to latest versions of gradle and maven in Fedora
Patch1:        fix-gradle-maven-build.patch

BuildArch:     noarch

BuildRequires: ivy-local
BuildRequires: maven-local
BuildRequires: ant
BuildRequires: ant-antunit
BuildRequires: ant-contrib
BuildRequires: ant-junit
BuildRequires: objectweb-asm
BuildRequires: plexus-utils
BuildRequires: maven-plugin-plugin

%description
Allows to parse Java byte code to find invocations of method/class/field
signatures and fail build (Apache Ant, Apache Maven, or Gradle).

%package javadoc
Summary: Javadoc for %{name}

%description javadoc
This package contains API documentation for %{name}.

%prep
%setup -q
%patch0
%patch1

find . -name "*.jar" -print -delete
find . -name "*.class" -print -delete

# Use system ivy settings
sed -i -e '/ivy:configure/d' build.xml

# Can't use missing maven-ant-tasks
%pom_xpath_remove "target/artifact:pom" build.xml
%pom_xpath_remove "target/artifact:mvn" build.xml
%pom_xpath_remove "target/artifact:install" build.xml
%pom_xpath_inject "target[@name='maven-descriptor']" \
"<exec executable='xmvn'>
  <arg value=\"-o\"/>
  <arg value=\"-f\"/>
  <arg value=\"\${maven-build-dir}/pom-build.xml\"/>
  <arg value=\"plugin:helpmojo\"/>
  <arg value=\"plugin:descriptor\"/>
  <arg value=\"plugin:report\"/>
  <arg value=\"-Dinjected.src.dir=src/main/java\"/>
  <arg value=\"-Dinjected.output.dir=../../build/main\"/>
  <arg value=\"-Dinjected.build.dir=\${maven-build-dir}\"/>
  <arg value=\"-Dinjected.maven-plugin-plugin.version=\${maven-plugin-plugin.version}\"/>
</exec>" build.xml
sed -i -e '/maven-ant-tasks/d' ivy.xml
sed -i -e '/uri="antlib:org.apache.maven.artifact.ant/d' build.xml

# Don't need to run RAT for RPM builds
sed -i -e '/apache-rat/d' ivy.xml
sed -i -e '/uri="antlib:org.apache.rat.anttasks/d' build.xml
rm -rf src/main/java/de/thetaphi/forbiddenapis/gradle src/test/gradle

%build
ant -Divy.mode=local jar

%install
# Add deps on unbundled jars, taken from ivy.xml
%pom_add_dep org.apache.ant:ant:1.7.0:provided build/maven/pom-deploy.xml
%pom_add_dep org.ow2.asm:asm:6.1.1 build/maven/pom-deploy.xml
%pom_add_dep org.ow2.asm:asm-commons:6.1.1 build/maven/pom-deploy.xml
%pom_add_dep org.codehaus.plexus:plexus-utils:1.1 build/maven/pom-deploy.xml
%pom_add_dep commons-cli:commons-cli:1.3.1 build/maven/pom-deploy.xml

# remove unnecessary dependency on parent POM
%pom_remove_parent build/maven/pom-deploy.xml

# Install maven artifacts
%mvn_artifact build/maven/pom-deploy.xml dist/forbiddenapis-2.5.jar
%mvn_install -J build/docs

# Install ant configuration
mkdir -p %{buildroot}%{_sysconfdir}/ant.d
echo "%{name} ant apache-commons-cli objectweb-asm/asm objectweb-asm/asm-commons plexus/utils" > %{name}-ant
install -pm 644 %{name}-ant %{buildroot}%{_sysconfdir}/ant.d/%{name}

%files -f .mfiles
%config(noreplace) %{_sysconfdir}/ant.d/%{name}
%license LICENSE.txt NOTICE.txt
%doc README.md


%changelog
* Sun Aug 30 2020 Fabio Valentini <decathorpe@gmail.com> - 2.5-9
- Remove unnecessary dependency on parent POM.

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 2.5-7
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Thu Apr 02 2020 Jiri VAnek <jvanek@redhat.com> - 2.5-6
- resurrected without gradle and docs. Not sure if it still does what it should

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Apr 18 2018 Mat Booth <mat.booth@redhat.com> - 2.5-1
- Update to latest upstream release

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Feb 03 2015 Zdenek Zambersky <zzambers@redhat.com> 1.7-1
- updated to version 1.7
- version tag in custom pom.xml is now generated automaticaly

* Fri Oct 11 2013 gil cattaneo <puntogil@libero.it> 1.3-1
- initial rpm

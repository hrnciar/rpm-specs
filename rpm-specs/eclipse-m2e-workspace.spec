%global short_name m2e-workspace

Name:           eclipse-m2e-workspace
Version:        0.4.0
Release:        16%{?dist}
Summary:        M2E CLI workspace resolver
License:        EPL-1.0
URL:            https://www.eclipse.org/m2e/
BuildArch:      noarch

Source0:        http://git.eclipse.org/c/m2e/org.eclipse.m2e.workspace.git/snapshot/%{short_name}-%{version}.tar.bz2
Source1:        http://www.eclipse.org/legal/epl-v10.html

Patch0:         takari.patch

BuildRequires:  maven-local
BuildRequires:  mvn(javax.inject:javax.inject)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-annotations)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:  mvn(org.eclipse.aether:aether-api)
BuildRequires:  mvn(org.eclipse.sisu:sisu-maven-plugin)

# Upstream Eclipse no longer supports non-64bit arches
ExcludeArch: s390 %{arm} %{ix86}

%description
Workspace dependency resolver implementation for Maven command line
build.

%package javadoc
Summary:        API documentation for %{name}

%description javadoc
This package provides %{summary}.


%prep
%setup -q -n %{short_name}-%{version}

%patch0 -p1

cp -a %{SOURCE1} .
pushd org.eclipse.m2e.workspace.cli
# Remove support for Maven 3.0.x (requires Sonatype Aether, which is
# not available in Fedora)
%pom_remove_dep org.sonatype.aether
rm src/main/java/org/eclipse/m2e/workspace/internal/Maven30WorkspaceReader.java

# Avoid deps on takari stack and build like a normal bundle
%pom_remove_plugin io.takari.maven.plugins:takari-lifecycle-plugin
%pom_xpath_set pom:project/pom:packaging bundle
%pom_add_plugin :maven-compiler-plugin '
<configuration>
<source>1.7</source>
<target>1.7</target>
</configuration>'
%pom_add_plugin org.eclipse.sisu:sisu-maven-plugin '
        <executions>
          <execution>
            <id>generate-index</id>
            <goals>
              <goal>main-index</goal><goal>test-index</goal>
            </goals>
          </execution>
        </executions>'
sed -i -e '/>maven-bundle-plugin</i<extensions>true</extensions>' \
       -e '/<supportedProjectTypes/,+2d' \
       -e '/Export-Package/a<Include-Resource>META-INF/sisu/javax.inject.Named=${project.build.outputDirectory}/META-INF/sisu/javax.inject.Named,{maven-resources}</Include-Resource>' pom.xml
popd

%build
pushd org.eclipse.m2e.workspace.cli
%mvn_build
popd

%install
pushd org.eclipse.m2e.workspace.cli
%mvn_install
popd

%files -f org.eclipse.m2e.workspace.cli/.mfiles
%license epl-v10.html

%files javadoc -f org.eclipse.m2e.workspace.cli/.mfiles-javadoc
%license epl-v10.html


%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 0.4.0-15
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 20 2019 Mat Booth <mat.booth@redhat.com> - 0.4.0-13
- Always avoid takari stack, even when not bootstrapping

* Mon Sep 23 2019 Mat Booth <mat.booth@redhat.com> - 0.4.0-12
- Restrict arches to same as Eclipse itself

* Tue Apr 23 2019 Mat Booth <mat.booth@redhat.com> - 0.4.0-11
- Add a bootstrap mode to break circular deps

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Aug 22 2018 Mat Booth <mat.booth@redhat.com> - 0.4.0-9
- License update

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Michael Simacek <msimacek@redhat.com> - 0.4.0-4
- Regenerate buildrequires

* Fri Feb 19 2016 Michael Simacek <msimacek@redhat.com> - 0.4.0-3
- Fix FTBFS

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Oct 14 2015 Sopot Cela <scela@redhat.com>- 0.4.0-1
- Upgrade to 0.4.0 for Mars. 1 release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Mar 06 2015 Michael Simacek <msimacek@redhat.com> - 0.2.0-1
- Initial packaging

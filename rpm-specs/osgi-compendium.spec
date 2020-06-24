# Optionally build with a reduced dependency set
%bcond_with jp_minimal

Name:           osgi-compendium
Version:        7.0.0
Release:        4%{?dist}
Summary:        Interfaces and Classes for use in compiling OSGi bundles
License:        ASL 2.0
URL:            http://www.osgi.org
BuildArch:      noarch

Source0:        https://osgi.org/download/r7/osgi.cmpn-%{version}.jar

BuildRequires:  maven-local
BuildRequires:  mvn(javax.servlet:javax.servlet-api)
%if %{without jp_minimal}
BuildRequires:  mvn(javax.persistence:persistence-api)
BuildRequires:  mvn(javax.ws.rs:javax.ws.rs-api) >= 2.1.5-2
%endif
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.osgi:osgi.annotation)
BuildRequires:  mvn(org.osgi:osgi.core)

%description
OSGi Compendium, Interfaces and Classes for use in compiling bundles.

%package javadoc
Summary:        API documentation for %{name}

%description javadoc
This package provides %{summary}.

%prep
%setup -q -c

# Delete pre-built binaries
rm -r org
find -name '*.class' -delete

mkdir -p src/main/{java,resources}
mv OSGI-OPT/src/org src/main/java/
mv xmlns src/main/resources

# J2ME stuff
rm -r src/main/java/org/osgi/service/io

mv META-INF/maven/org.osgi/osgi.cmpn/pom.xml .

%pom_xpath_inject pom:project '
<packaging>bundle</packaging>
<properties>
  <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
</properties>
<build>
  <plugins>
    <plugin>
      <groupId>org.apache.felix</groupId>
      <artifactId>maven-bundle-plugin</artifactId>
      <extensions>true</extensions>
      <configuration>
        <instructions>
          <Bundle-Name>${project.artifactId}</Bundle-Name>
          <Bundle-SymbolicName>${project.artifactId}</Bundle-SymbolicName>
        </instructions>
      </configuration>
    </plugin>
  </plugins>
</build>'

%pom_add_dep org.osgi:osgi.annotation::provided
%pom_add_dep org.osgi:osgi.core::provided
%pom_add_dep javax.servlet:javax.servlet-api::provided
%if %{without jp_minimal}
%pom_add_dep javax.persistence:persistence-api::provided
%pom_add_dep javax.ws.rs:javax.ws.rs-api::provided
%else
# Don't compile in Jax RS and JPA support when jp_minimal is activated
rm -r src/main/java/org/osgi/service/jaxrs
rm -r src/main/java/org/osgi/service/jpa
rm -r src/main/java/org/osgi/service/transaction/control/jpa
%endif

%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8

%install
%mvn_install


%files -f .mfiles
%license LICENSE
%doc about.html

%files javadoc -f .mfiles-javadoc
%license LICENSE


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 19 2019 Mat Booth <mat.booth@redhat.com> - 7.0.0-2
- Allow conditionally compiling in support for Jax RS and JPA

* Wed Mar 06 2019 Mat Booth <mat.booth@redhat.com> - 7.0.0-1
- Update to OSGi R7

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Oct 10 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 6.0.0-2
- Fix scopes of injected Maven dependencies

* Mon Oct 12 2015 Michael Simacek <msimacek@redhat.com> - 6.0.0-1
- Initial packaging

Name:           docker-client-java
Version:        8.11.7
Release:        6%{?dist}
Summary:        Docker Client

# Obsoletes/Provides added in F27
Provides:       docker-client = %{version}-%{release}
Obsoletes:      docker-client < %{version}-%{release}

License:        ASL 2.0
URL:            https://github.com/spotify/docker-client
Source0:        https://github.com/spotify/docker-client/archive/v%{version}.tar.gz

Patch0: 0001-Port-to-latest-version-of-Google-AutoValue.patch

BuildRequires:  maven-local
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-databind)
BuildRequires:  mvn(com.fasterxml.jackson.datatype:jackson-datatype-guava)
BuildRequires:  mvn(com.fasterxml.jackson.jaxrs:jackson-jaxrs-json-provider)
BuildRequires:  mvn(com.github.jnr:jnr-unixsocket)
BuildRequires:  mvn(com.google.auto.value:auto-value) >= 1.4.1
BuildRequires:  mvn(com.google.code.findbugs:jsr305)
BuildRequires:  mvn(com.google.guava:guava:20.0)
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(commons-lang:commons-lang)
BuildRequires:  mvn(org.apache.commons:commons-compress)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.httpcomponents:httpclient)
BuildRequires:  mvn(org.apache.httpcomponents:httpcore)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.bouncycastle:bcpkix-jdk15on)
BuildRequires:  mvn(org.glassfish.hk2:hk2-api)
BuildRequires:  mvn(org.glassfish.jersey.connectors:jersey-apache-connector)
BuildRequires:  mvn(org.glassfish.jersey.core:jersey-client)
BuildRequires:  mvn(org.glassfish.jersey.media:jersey-media-json-jackson)
BuildRequires:  mvn(org.slf4j:slf4j-api)

BuildArch: noarch

%description
The Docker Client is a Java API library for accessing a Docker daemon.

%prep
%setup -q -n docker-client-%{version}
%patch0 -p1

# The parent pom doen't add anything we can't live without
%pom_remove_parent
sed -i -e '/<packaging>/a<groupId>com.spotify</groupId>' pom.xml

# Plugins unnecessary for RPM builds
%pom_remove_plugin :maven-shade-plugin
%pom_remove_plugin :jacoco-maven-plugin

# Unnecessary static ananlysis stuff
%pom_remove_dep com.google.code.findbugs:annotations
sed -i -e '/SuppressFBWarnings/d' src/main/java/com/spotify/docker/client/DefaultDockerClient.java \
  src/main/java/com/spotify/docker/client/messages/{Host,Container}Config.java

# Missing dep for google cloud support
%pom_remove_dep :google-auth-library-oauth2-http
rm -rf src/{main,test}/java/com/spotify/docker/client/auth/gcr

# Add dep on hk2 api
%pom_add_dep org.glassfish.hk2:hk2-api

# Generate OSGi metadata
%pom_add_plugin "org.apache.felix:maven-bundle-plugin" pom.xml \
"<configuration>
  <instructions>
    <Bundle-SymbolicName>\${project.groupId}.docker.client</Bundle-SymbolicName>
    <_nouses>true</_nouses>
  </instructions>
</configuration>
<executions>
  <execution>
    <id>create-manifest</id>
    <phase>process-classes</phase>
    <goals><goal>manifest</goal></goals>
  </execution>
</executions>"
%pom_add_plugin "org.apache.maven.plugins:maven-jar-plugin" pom.xml \
"<configuration>
  <archive>
    <manifestFile>\${project.build.outputDirectory}/META-INF/MANIFEST.MF</manifestFile>
  </archive>
</configuration>"

%build
%mvn_build -j -f

%install
%mvn_install

%files -f .mfiles
%license LICENSE NOTICE
%doc README.md

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.11.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.11.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Mar 13 2019 Mat Booth <mat.booth@redhat.com> - 8.11.7-4
- Add missing BR on hk2

* Thu Mar 07 2019 Mat Booth <mat.booth@redhat.com> - 8.11.7-3
- Port to latest Google AutoValue

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.11.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Aug 22 2018 Mat Booth <mat.booth@redhat.com> - 8.11.7-1
- Update to latest upstream release

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 08 2018 Mat Booth <mat.booth@redhat.com> - 8.9.2-1
- Update to 8.9.2 release of docker client

* Thu Apr 19 2018 Mat Booth <mat.booth@redhat.com> - 6.2.5-8
- Re-generate BRs and rebuild against correct guava

* Tue Feb 06 2018 Mat Booth <mat.booth@redhat.com> - 6.2.5-7
- Rebuild against new guava to regenerate OSGi metadata.

* Wed Jan 31 2018 Mat Booth <mat.booth@redhat.com> - 6.2.5-6
- Add patch to fix ebz#530264

* Fri Jan 26 2018 Mat Booth <mat.booth@redhat.com> - 6.2.5-5
- Remove dep on jaxb-api

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 21 2017 Jeff Johnston <jjohnstn@redhat.com> - 6.2.5-3
- Renamed from docker-client to docker-client-java

* Mon Jul 03 2017 Mat Booth <mat.booth@redhat.com> - 6.2.5-2
- Adapt to unixsocket API changes

* Fri Jun 16 2017 Mat Booth <mat.booth@redhat.com> - 6.2.5-1
- Update to docker-client 6.2.5
- Remove SCL macros forbidden in Fedora

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 01 2017 Michael Simacek <msimacek@redhat.com> - 4.0.6-4
- Remove BR on jacoco-maven-plugin

* Thu Jun 30 2016 Mat Booth <mat.booth@redhat.com> - 4.0.6-3
- Add missing BR on oss-parent
- Add patch to avoid annotations removed from httpcomponents

* Wed Jun 29 2016 Mat Booth <mat.booth@redhat.com> - 4.0.6-2
- Add missing import-packages in OSGi manifest

* Thu May 19 2016 Alexander Kurtakov <akurtako@redhat.com> 4.0.6-1
- Update to upstream 4.0.6 release.

* Tue Apr 19 2016 Roland Grunberg <rgrunber@redhat.com> - 4.0.1-2
- Add com.spotify.docker.client.exceptions to exported packages.

* Mon Apr 18 2016 Alexander Kurtakov <akurtako@redhat.com> 4.0.1-1
- Update to upstream 4.0.1 release.

* Wed Apr 6 2016 Alexander Kurtakov <akurtako@redhat.com> 3.6.8-1
- Update to upstream 3.6.8 release.

* Fri Mar 25 2016 Alexander Kurtakov <akurtako@redhat.com> 3.6.6-1
- Update to upstream 3.6.6 release.

* Thu Feb 11 2016 Alexander Kurtakov <akurtako@redhat.com> 3.5.12-1
- Update to upstream 3.5.12 release.

* Mon Feb 8 2016 Alexander Kurtakov <akurtako@redhat.com> 3.5.11-1
- Update to upstream 3.5.11 release.

* Thu Feb 4 2016 Alexander Kurtakov <akurtako@redhat.com> 3.5.10-1
- Update to upstream 3.5.10 release.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 20 2016 Alexander Kurtakov <akurtako@redhat.com> 3.5.9-1
- Update to upstream 3.5.9 release.

* Fri Oct 23 2015 Alexander Kurtakov <akurtako@redhat.com> 3.1.9-1
- Update to upstream 3.1.9 release.

* Tue Oct 6 2015 akurtakov <akurtakov@localhost.localdomain> 3.1.5-1
- Update to upstream 3.1.5.
- Stripdown useless BRs.

* Thu Sep 24 2015 Alexander Kurtakov <akurtako@redhat.com> 3.1.4-1
- Update to upstream 3.1.4 release.

* Mon Aug 17 2015 Alexander Kurtakov <akurtako@redhat.com> 3.1.3-1
- Update to upstream 3.1.3 release.

* Wed Aug 5 2015 Alexander Kurtakov <akurtako@redhat.com> 3.1.2-1
- Update to upstream 3.1.2 release.

* Thu Jul 30 2015 Roland Grunberg <rgrunber@redhat.com> - 3.1.1-2
- Update manifest's Bundle-Version to match %%{version}.

* Thu Jul 30 2015 Alexander Kurtakov <akurtako@redhat.com> 3.1.1-1
- Update to upstream 3.1.1 release.

* Wed Jul 22 2015 Roland Grunberg <rgrunber@redhat.com> - 3.0.0-2
- Support the 1.19 Docker Remote API.
- Support SO_LINGER option needed when httpcomponents-core >= 4.4.

* Wed Jul 08 2015 Roland Grunberg <rgrunber@redhat.com> - 3.0.0-1
- Update to 3.0.0.

* Wed Jun 24 2015 Roland Grunberg <rgrunber@redhat.com> - 2.7.26-3
- Depend upon hk2-locator as it's needed by jersey-client at runtime.
- Require jaxb-api to temporarily satisfy an invalid requirement.

* Tue Jun 23 2015 Roland Grunberg <rgrunber@redhat.com> - 2.7.26-2
- Depend on versionless bouncycastle within manifest.

* Mon Jun 8 2015 Jeff Johnston <jjohnstn@redhat.com> 2.7.26-1
- Initial packaging.

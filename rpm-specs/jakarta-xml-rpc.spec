%global srcname jax-rpc-api

Name:           jakarta-xml-rpc
# the obsoleted geronimo-jaxrpc had a higher version
Epoch:          1
Version:        1.1.4
Release:        1%{?dist}
Summary:        Jakarta XML RPC API
License:        EPL-2.0 or GPLv2 with exceptions

URL:            https://github.com/eclipse-ee4j/jax-rpc-api
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(jakarta.servlet:jakarta.servlet-api)
BuildRequires:  mvn(jakarta.xml.soap:jakarta.xml.soap-api)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.glassfish.build:spec-version-maven-plugin)

# package renamed in fedora 33, remove in fedora 35
Provides:       geronimo-jaxrpc = %{epoch}:%{version}-%{release}
Obsoletes:      geronimo-jaxrpc < 2.1-28

%description
Jakarta XML RPC API provides standardized Java APIs for using XML-RPC.


%package javadoc
Summary:        Javadoc for %{name}

# package renamed in fedora 33, remove in fedora 35
Provides:       geronimo-jaxrpc-javadoc = %{epoch}:%{version}-%{release}
Obsoletes:      geronimo-jaxrpc-javadoc < 2.1-28

%description javadoc
API documentation for %{name}.


%prep
%autosetup -n %{srcname}-%{version} -p1

# drop useless dependency on parent POM
%pom_remove_parent

# do not build specification documentation
%pom_disable_module spec

# drop useless maven plugins
%pom_remove_plugin :maven-javadoc-plugin api
%pom_remove_plugin :maven-source-plugin api

# add dependency for javax.xml.soap package (no longer part of OpenJDK)
%pom_add_dep jakarta.xml.soap:jakarta.xml.soap-api api

# replace deprecated option that was removed with maven-jar-plugin 3.x
%pom_xpath_remove 'pom:plugin[pom:artifactId="maven-jar-plugin"]/pom:configuration/pom:useDefaultManifestFile' api
%pom_xpath_inject 'pom:plugin[pom:artifactId="maven-jar-plugin"]/pom:configuration' '<archive>
  <manifestFile>${project.build.outputDirectory}/META-INF/MANIFEST.MF</manifestFile>
</archive>' api

# disable spec verification (fails because spec-version-maven-plugin is too old)
%pom_xpath_remove 'pom:goal[text()="check-module"]' api

# do not install useless parent POM
%mvn_package jakarta.xml.rpc:rpc-api-parent __noinstall

# add compatibility alias for old maven artifact coordinates
%mvn_alias jakarta.xml.rpc:jakarta.xml.rpc-api javax.xml:jaxrpc-api

# add compatibility symlinks for old classpath
%mvn_file : %{name}/jakarta.xml.rpc-api geronimo-jaxrpc jaxrpc


%build
%mvn_build


%install
%mvn_install


%files -f .mfiles
%license LICENSE.md NOTICE.md

%files javadoc -f .mfiles-javadoc
%license LICENSE.md NOTICE.md


%changelog
* Sat Aug 22 2020 Fabio Valentini <decathorpe@gmail.com> - 1:1.1.4-1
- Initial package renamed from geronimo-jaxrpc.


%global srcname jaxrs-api

Name:           jakarta-ws-rs
Version:        2.1.6
Release:        7%{?dist}
Summary:        Jakarta RESTful Web Services
# ASL 2.0: jaxrs-api/src/main/java/javax/ws/rs/core/GenericEntity.java
License:        (EPL-2.0 or GPLv2 with exceptions) and ASL 2.0

URL:            https://github.com/eclipse-ee4j/jaxrs-api
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(jakarta.activation:jakarta.activation-api)
BuildRequires:  mvn(jakarta.xml.bind:jakarta.xml.bind-api)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.glassfish.build:spec-version-maven-plugin)
BuildRequires:  mvn(org.glassfish.jaxb:jaxb-runtime)
BuildRequires:  mvn(org.mockito:mockito-core)

# package renamed in fedora 33, remove in fedora 35
Provides:       glassfish-jax-rs-api = %{version}-%{release}
Obsoletes:      glassfish-jax-rs-api < 2.1.6-7

# javadoc subpackage is currently not built
Obsoletes:      glassfish-jax-rs-api-javadoc < 2.1.6-7

%description
JAX-RS Java API for RESTful Web Services (JSR 339).


%prep
%setup -q -n %{srcname}-%{version}

pushd jaxrs-api
# remove unnecessary maven plugins
%pom_remove_plugin :buildnumber-maven-plugin
%pom_remove_plugin :maven-checkstyle-plugin
%pom_remove_plugin :maven-deploy-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-jxr-plugin
%pom_remove_plugin :maven-source-plugin

%pom_xpath_remove "pom:build/pom:finalName"

# add aliases for old maven artifact coordinates
%mvn_alias jakarta.ws.rs:jakarta.ws.rs-api javax.ws.rs:javax.ws.rs-api
popd


%build
pushd jaxrs-api
# skip javadoc build due to https://github.com/fedora-java/xmvn/issues/58
%mvn_build -j -- -DbuildNumber=unknown
popd


%install
pushd jaxrs-api
%mvn_install
popd


%files -f jaxrs-api/.mfiles
%license LICENSE.md NOTICE.md
%doc README.md CONTRIBUTING.md


%changelog
* Thu Aug 13 2020 Fabio Valentini <decathorpe@gmail.com> - 2.1.6-7
- Initial package renamed from glassfish-jax-rs-api.


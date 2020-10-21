%global srcname jpa-api
%global specver 2.2

Name:           jakarta-persistence
Version:        2.2.3
Release:        1%{?dist}
Summary:        JPA / Jakarta Persistence API
License:        EPL-2.0 or BSD

%global src_ver %{specver}-%{version}-RELEASE

URL:            https://github.com/eclipse-ee4j/jpa-api
Source0:        %{url}/archive/%{src_ver}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.glassfish.build:spec-version-maven-plugin)

# package renamed in fedora 33, remove in fedora 35
Provides:       geronimo-jpa = %{version}-%{release}
Obsoletes:      geronimo-jpa < 1.1.1-28

%description
Jakarta Persistence defines a standard for management of persistence
and object/relational mapping in Java environments.


%package javadoc
Summary:        Javadoc for %{name}

# package renamed in fedora 33, remove in fedora 35
Provides:       geronimo-jpa-javadoc = %{version}-%{release}
Obsoletes:      geronimo-jpa-javadoc < 1.1.1-28

%description javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q -n %{srcname}-%{src_ver}

pushd api
# remove unnecessary dependency on parent POM
%pom_remove_parent

# remove unnecessary maven plugins
%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :maven-javadoc-plugin

# add alias for old artifact coordinates used by osgi-compendium
%mvn_alias jakarta.persistence:jakarta.persistence-api javax.persistence:persistence-api
popd


%build
pushd api
%mvn_build
popd


%install
pushd api
%mvn_install
popd


%files -f api/.mfiles
%license LICENSE.md NOTICE.md
%doc README.md

%files javadoc -f api/.mfiles-javadoc
%license LICENSE.md NOTICE.md


%changelog
* Thu Jul 30 2020 Fabio Valentini <decathorpe@gmail.com> - 2.2.3-1
- Updated package for Eclipse EE4J sources, renamed from geronimo-jpa.


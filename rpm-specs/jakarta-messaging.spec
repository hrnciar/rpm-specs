%global srcname jms-api

Name:           jakarta-messaging
Version:        2.0.3
Release:        1%{?dist}
Summary:        JMS / Jakarta Messaging API
License:        EPL-2.0 or GPLv2 with exceptions

%global src_ver %{version}-RELEASE

URL:            https://github.com/eclipse-ee4j/jms-api
Source0:        %{url}/archive/%{src_ver}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.glassfish.build:spec-version-maven-plugin)

# package renamed in fedora 33, remove in fedora 35
Provides:       geronimo-jms = %{version}-%{release}
Obsoletes:      geronimo-jms < 1.1.1-32

%description
This package contains the API definition source code for the Jakarta
Messaging API.


%package javadoc
Summary:        Javadoc for %{name}

# package renamed in fedora 33, remove in fedora 35
Provides:       geronimo-jms-javadoc = %{version}-%{release}
Obsoletes:      geronimo-jms-javadoc < 1.1.1-32

%description javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q -n %{srcname}-%{src_ver}

pushd api
# remove unnecessary dependency on parent POM
%pom_remove_parent

# remove unnecessary maven plugins
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-jar-plugin

# add alias for old artifact coordinates used by log4j12 and apache-log4j-extras
%mvn_alias jakarta.jms:jakarta.jms-api org.apache.geronimo.specs:geronimo-jms_1.1_spec
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
* Thu Jul 30 2020 Fabio Valentini <decathorpe@gmail.com> - 2.0.3-1
- Updated package for Eclipse EE4J sources, renamed from geronimo-jms.


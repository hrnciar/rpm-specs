%global srcname servlet-api

Name:           jakarta-servlet
Version:        5.0.0
Release:        4%{?dist}
Summary:        Server-side API for handling HTTP requests and responses
# most of the project is EPL-2.0 or GPLv2 w/exceptions,
# but some files still have Apache-2.0 license headers:
# https://github.com/eclipse-ee4j/servlet-api/issues/347
License:        (EPL-2.0 or GPLv2 with exceptions) and ASL 2.0

URL:            https://github.com/eclipse-ee4j/servlet-api
Source0:        %{url}/archive/%{version}-RELEASE/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)

# package renamed in fedora 33, remove in fedora 35
Provides:       glassfish-servlet-api = %{version}-%{release}
Obsoletes:      glassfish-servlet-api < 3.1.0-21

%description
Jakarta Servlet defines a server-side API for handling HTTP requests
and responses.


%package javadoc
Summary:        Javadoc for %{name}

# package renamed in fedora 33, remove in fedora 35
Provides:       glassfish-servlet-api-javadoc = %{version}-%{release}
Obsoletes:      glassfish-servlet-api-javadoc < 3.1.0-21

%description javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q -n %{srcname}-%{version}-RELEASE

# remove unnecessary dependency on parent POM
%pom_remove_parent . api

# do not build specification documentation
%pom_disable_module spec

# Copy to old package name
# TODO: Remove when all dependencies are migrated from javax.servlet to jakarta.servlet
cp -pr api/src/main/java/jakarta api/src/main/java/javax
sed -i -e 's/jakarta\./javax./g' $(find api/src/main/java/javax -name *.java)
%pom_xpath_replace pom:instructions/pom:Export-Package \
  '<Export-Package>jakarta.servlet.*,javax.servlet.*;version="4.0.0"</Export-Package>' api

# do not install useless parent POM
%mvn_package jakarta.servlet:servlet-parent __noinstall

# remove unnecessary maven plugins
%pom_remove_plugin -r :formatter-maven-plugin
%pom_remove_plugin -r :impsort-maven-plugin
%pom_remove_plugin -r :maven-enforcer-plugin
%pom_remove_plugin -r :maven-javadoc-plugin
%pom_remove_plugin -r :maven-source-plugin

# add maven artifact coordinate aliases for backwards compatibility
%mvn_alias jakarta.servlet:jakarta.servlet-api \
    javax.servlet:javax.servlet-api \
    javax.servlet:servlet-api

# add compat symlink for packages constructing the classpath manually
%mvn_file :{*} %{name}/@1 glassfish-servlet-api


%build
%mvn_build


%install
%mvn_install


%files -f .mfiles
%license LICENSE.md NOTICE.md
%doc README.md

%files javadoc -f .mfiles-javadoc
%license LICENSE.md NOTICE.md


%changelog
* Thu Aug 20 2020 Mat Booth <mat.booth@redhat.com> - 5.0.0-4
- Correct mvn_file macro invokation

* Wed Aug 19 2020 Fabio Valentini <decathorpe@gmail.com> - 5.0.0-3
- Add compat symlink for packages constructing the classpath manually.

* Wed Aug 19 2020 Mat Booth <mat.booth@redhat.com> - 5.0.0-2
- Also ship the API in the old javax namespace to aid transition

* Thu Aug 13 2020 Fabio Valentini <decathorpe@gmail.com> - 5.0.0-1
- Initial package renamed from glassfish-servlet-api.


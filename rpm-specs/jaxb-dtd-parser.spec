Name:           jaxb-dtd-parser
Version:        1.4.3
Release:        1%{?dist}
Summary:        SAX-like API for parsing XML DTDs
License:        BSD

URL:            https://github.com/eclipse-ee4j/jaxb-dtd-parser
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)

Obsoletes:      glassfish-dtd-parser < 1.4.3-1
Provides:       glassfish-dtd-parser = %{version}-%{release}

%description
SAX-like API for parsing XML DTDs.


%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.


%prep
%setup -q

pushd dtd-parser
# remove unnecessary dependency on parent POM
# org.eclipse.ee4j:project is not packaged and isn't needed
%pom_remove_parent

# remove unnecessary plugins
%pom_remove_plugin :buildnumber-maven-plugin
%pom_remove_plugin :glassfish-copyright-maven-plugin

# remove unsupported --release argument for maven-compiler-plugin
# re-evaluate after switching to OpenJDK 9+
%pom_xpath_remove "pom:plugin[pom:artifactId='maven-compiler-plugin']/pom:configuration"
%pom_xpath_remove "pom:execution[pom:id='base-compile']/pom:configuration"

# remove unsupported --release argument for maven-javadoc-plugin
# re-evaluate after switching to OpenJDK 9+
%pom_xpath_remove "pom:plugin[pom:artifactId='maven-javadoc-plugin']/pom:configuration"

# remove module-info.java, which breaks compilation on OpenJDK 8
# re-evaluate after switching to OpenJDK 9+
rm src/main/java/module-info.java
popd


%build
pushd dtd-parser
%mvn_build
popd


%install
pushd dtd-parser
%mvn_install
popd


%files -f dtd-parser/.mfiles
%license LICENSE.md NOTICE.md
%doc README.md

%files javadoc -f dtd-parser/.mfiles-javadoc
%license LICENSE.md NOTICE.md


%changelog
* Fri May 08 2020 Fabio Valentini <decathorpe@gmail.com> - 1.4.3-1
- Initial package renamed from glassfish-dtd-parser.


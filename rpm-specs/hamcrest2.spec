%global srcname hamcrest

Name:           hamcrest2
Version:        2.2
Release:        3%{?dist}
Summary:        Library of matchers for building test expressions
License:        BSD

URL:            https://github.com/hamcrest/JavaHamcrest
Source0:        %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz
Source1:        https://repo1.maven.org/maven2/org/%{srcname}/%{srcname}/%{version}/%{srcname}-%{version}.pom

BuildArch:      noarch

BuildRequires:  java-1.8.0-openjdk-devel
BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)

%description
Provides a library of matcher objects (also known as constraints or predicates)
allowing 'match' rules to be defined declaratively, to be used in other
frameworks. Typical scenarios include testing frameworks, mocking libraries and
UI validation rules.


%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
Javadoc for %{name}.


%prep
%setup -q -n JavaHamcrest-%{version}

# drop docs and unused gradle build system
rm -r docs
rm -r *gradle*
rm -r */*.gradle

# drop everything but hamcrest itself
# -core:        empty legacy module, only contains a deprecation warning
# -integration: legacy module, stuck at an old version
# -library:     empty legacy module, only contains a deprecation warning
mv hamcrest/src .
rm -r hamcrest
rm -r hamcrest-core
rm -r hamcrest-integration
rm -r hamcrest-library

# use pom.xml from maven central and add junit dependency manually
cp -p %{SOURCE1} pom.xml
%pom_add_dep junit:junit

# convert LICENSE.txt to unix line endings
sed -i 's/\r//' LICENSE.txt


%build
# build against OpenJDK 8, code is not compatible with Java 9+ yet
export JAVA_HOME=%{_jvmdir}/java-1.8.0
# forcing Java 8 because of required language features
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8


%install
%mvn_install


%files -f .mfiles
%doc README.md
%license LICENSE.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 23 2020 Fabio Valentini <decathorpe@gmail.com> - 2.2-2
- Build against java-1.8.0-openjdk, package is not ready for Java 9+ yet.

* Mon May 11 2020 Fabio Valentini <decathorpe@gmail.com> - 2.2-1
- Update to version 2.2.

* Sat May 09 2020 Fabio Valentini <decathorpe@gmail.com> - 2.1-1
- Initial package for hamcrest2.


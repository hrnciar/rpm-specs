%global commit e5dc3b04eeb9c7107f5a2b80c2b0f43434722cfd
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%bcond_with javadoc

Name:          apache-log4j-extras
Version:       1.2.17.1
Release:       18%{?dist}
Summary:       Apache Extras Companion for Apache log4j
License:       ASL 2.0

URL:           http://logging.apache.org/log4j/extras
Source0:       https://github.com/apache/log4j-extras/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz

BuildArch:     noarch

BuildRequires: maven-local
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(log4j:log4j:1.2.17)
BuildRequires: mvn(org.apache:apache:pom:)
BuildRequires: mvn(org.apache.geronimo.specs:specs:pom:)
BuildRequires: mvn(org.apache.geronimo.specs:geronimo-jms_1.1_spec)
BuildRequires: mvn(org.apache.rat:apache-rat-plugin)
BuildRequires: mvn(org.hsqldb:hsqldb)

Requires:      mvn(log4j:log4j:1.2.17)

%description
Apache Extras Companion for Apache log4j is a collection of appenders, 
filters, layouts, and receivers for Apache log4j 1.2

%if %{with javadoc}
%package javadoc
Summary:       Javadoc for %{name}

%description javadoc
This package contains the API documentation for %{name}.
%endif


%prep
%setup -qn log4j-extras-%{commit}
# Cleanup
find . -name '*.class' -delete
find . -name '*.jar' -delete

# Unnecessary plugins
%pom_remove_plugin :maven-assembly-plugin
%pom_remove_plugin :maven-changes-plugin
%pom_remove_plugin :maven-pmd-plugin
%pom_remove_plugin :maven-site-plugin

%pom_xpath_set "pom:project/pom:dependencies/pom:dependency[pom:groupId='hsqldb']/pom:groupId" org.hsqldb

# remove maven-compiler-plugin configuration that is broken with Java 11
%pom_xpath_remove 'pom:plugin[pom:artifactId="maven-compiler-plugin"]/pom:configuration'

%build
%if %{without javadoc}
args="-j"
%endif
# Tests disabled because of failures
%mvn_build $args -- -DskipTests -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8

%install
%mvn_install

%files -f .mfiles
%license LICENSE NOTICE
%dir %{_javadir}/%{name}

%if %{with javadoc}
%files javadoc -f .mfiles-javadoc
%license LICENSE NOTICE
%endif

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.17.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 18 2020 Fabio Valentini <decathorpe@gmail.com> - 1.2.17.1-17
- Set javac source and target to 1.8 to fix Java 11 builds.

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 1.2.17.1-16
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.17.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.17.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.17.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.17.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.2.17.1-11
- Escape macros in %%changelog

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.17.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.17.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.17.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.17.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.17.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Mar 03 2015 gil cattaneo <puntogil@libero.it> 1.2.17.1-5
- introduce license macro
- fix BR list

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.17.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Robert Rati <rrati@redhat> - 1.2.17.1-3
- Add BuildRequires on log4j12
- Conditionalize javadoc generation

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 1.2.17.1-2
- Use Requires: java-headless rebuild (#1067528)

* Wed Jan 29 2014 Robert Rati <rrati@redhat> - 1.2.17.1-1
- Update to upstream 1.2.17.1
- Use new %%mvn_* macros

* Sat Dec 24 2011 David Nalley <david@gnsa.us> - 1.1-3
- switching from ant to maven because ant doesn't have a javadoc target

* Thu Oct 20 2011 David Nalley <david@gnsa.us> - 1.1-2
- removing forbidden unicode trademark symbols

* Thu Oct 20 2011 David Nalley <david@gnsa.us> - 1.1-1 
- Initial packaging

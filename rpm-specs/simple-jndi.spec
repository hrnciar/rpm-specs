Name:          simple-jndi
Version:       0.11.4.1
Release:       19%{?dist}
Summary:       A JNDI implementation
License:       BSD
Url:           https://github.com/hen/osjava
Source0:       http://osjava.googlecode.com/svn/dist/releases/official/simple-jndi/simple-jndi-0.11.4.1-src.tar.gz
# wget -O simple-jndi-0.11.4.1.pom http://osjava.googlecode.com/svn/releases/simple-jndi-0.11.4.1/pom.xml
Source1:       simple-jndi-%{version}.pom
Patch0:        simple-jndi-0.11.4.1-jdk7.patch

BuildRequires: java-devel
BuildRequires: javapackages-local
BuildRequires: ant
BuildRequires: apache-commons-dbcp
BuildRequires: apache-commons-pool
BuildRequires: junit

BuildArch:     noarch

%description
Simple-JNDI is intended to solve two problems. The first is
that of finding a container independent way of opening a
database connection, the second is to find a good way of
specifying application configurations.
1. Unit tests or prototype code often need to emulate the
  environment within which the code is expected to run.
  A very common one is to get an object of type
  javax.sql.DataSource from JNDI so a java.sql.Connection
  to your database of choice may be opened.
2. Applications need configuration; a JNDI implementation
  makes a handy location for configuration values. Either
  as a globally available system, or via IoC through the
  use of some kind of JNDI configuration facade (see gj-config).
A solution: simple implementation of JNDI. It is entirely
library based, so no server instances are started, and it
sits upon Java .properties files, XML files or Windows-style
.ini files, so it is easy to use and simple to understand.
The files may be either on the file system or in the classpath.

%package javadoc
Summary:       Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n simple-jndi-%{version}
find . -name "*.class" -delete
find . -name "*.jar" -delete
%patch0 -p0

# this test at random fails
rm -r src/test/org/osjava/sj/memory/SharedMemoryTest.java

%build

%ant \
  -Dlibdir=lib \
  -Dcommons-pool.jar=file://$(build-classpath commons-pool) \
  -Dcommons-dbcp.jar=file://$(build-classpath commons-dbcp) \
  jar javadoc

%install
%mvn_artifact %{SOURCE1} target/%{name}-%{version}.jar
%mvn_file %{name}:%{name} %{name}
%mvn_install -J dist/docs/api

%files -f .mfiles
%license LICENSE.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.4.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 11 2020 Jiri Vanek <jvanek@redhat.com> - 0.11.4.1-18
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.4.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.4.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.4.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.4.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.4.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.4.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.4.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.4.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.4.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Mar 15 2015 gil cattaneo <puntogil@libero.it> 0.11.4.1-8
- fix Url tag

* Wed Feb 11 2015 gil cattaneo <puntogil@libero.it> 0.11.4.1-7
- introduce license macro

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 0.11.4.1-5
- Use Requires: java-headless rebuild (#1067528)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Apr 06 2012 gil cattaneo <puntogil@libero.it> 0.11.4.1-1
- initial rpm

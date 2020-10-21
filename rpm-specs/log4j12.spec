%global archiversion %(echo %{version} | tr . _ )

%bcond_without dtd

Name:          log4j12
Version:       1.2.17
Release:       30%{?dist}
Summary:       Java logging package
License:       ASL 2.0
URL:           http://logging.apache.org/log4j/1.2/
BuildArch:     noarch

Source0:       https://github.com/apache/log4j/archive/v%{archiversion}.tar.gz
Source1:       log4j.catalog

Patch0:        0001-logfactor5-changed-userdir.patch
Patch1:        0009-Fix-tests.patch
Patch2:        0010-Fix-javadoc-link.patch
Patch3:        0001-Backport-fix-for-CVE-2017-5645.patch
Patch4:        0001-Fix-tests-java11.patch

BuildRequires: maven-local
BuildRequires: mvn(ant-contrib:ant-contrib)
BuildRequires: mvn(jakarta.activation:jakarta.activation-api)
BuildRequires: mvn(javax.mail:mail)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.ant:ant-junit)
BuildRequires: mvn(org.apache.ant:ant-nodeps)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.geronimo.specs:geronimo-jms_1.1_spec)
BuildRequires: mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-assembly-plugin)
BuildRequires: mvn(oro:oro)

Obsoletes:     log4j <= 0:1.2.17-14

%description
Log4j is a tool to help the programmer output log statements to a
variety of output targets.

%package javadoc
Summary:       Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n log4j-%{archiversion}
# Cleanup
find . -name "*.jar" -print -delete
find . -name "*.class" -print -delete
find . -name "*.dll" -print -delete
rm -rf docs/api

%patch0 -p1 -b .logfactor-home
%patch1 -p1 -b .fix-tests
%patch2 -p1 -b .xlink-javadoc
%patch3 -p1
%patch4 -p1

# Remove unavailable plugin
%pom_remove_plugin :clirr-maven-plugin
# Remove unwanted plugin
%pom_remove_plugin :maven-site-plugin
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :rat-maven-plugin
# Disable javadoc jar
%pom_xpath_remove "pom:build/pom:plugins/pom:plugin[pom:artifactId = 'maven-javadoc-plugin']/pom:executions"

# Remove openejb from dependencies
%pom_remove_dep org.apache.openejb:javaee-api

%pom_remove_dep sun.jdk:tools

# Fix ant gId
sed -i.ant "s|groupId>ant<|groupId>org.apache.ant<|g" pom.xml

sed -i.javac "s|1.4|1.8|g" pom.xml build.xml
sed -i.javac "s|1.4|1.8|g" pom.xml build.xml
sed -i.javac "s|1.1|1.8|g" tests/build.xml
sed -i.javac "s|1.1|1.8|g" tests/build.xml

# Fix OSGi manifest
sed -i.javax.jmdns "s|javax.jmdns.*;resolution:=optional,|!javax.jmdns.*,|g" pom.xml
# Add proper bundle symbolicname
%pom_xpath_inject "pom:build/pom:plugins/pom:plugin[pom:artifactId = 'maven-bundle-plugin']/pom:configuration/pom:instructions" "
  <Bundle-SymbolicName>org.apache.log4j</Bundle-SymbolicName>
  <_nouses>true</_nouses>"

# Disable build unwanted dll library 
%pom_xpath_remove "pom:build/pom:plugins/pom:plugin[pom:artifactId = 'maven-antrun-plugin']/pom:executions/pom:execution[pom:phase = 'process-classes' ]"

# Don't use deprecated "assembly" goal of Maven Assembly Plugin, which
# was removed in version 3.0.0.
%pom_xpath_set "pom:plugin[pom:artifactId='maven-assembly-plugin']/pom:executions/pom:execution/pom:goals/pom:goal[text()='assembly']" single

sed -i 's/\r//g' LICENSE NOTICE src/site/resources/css/*.css

# fix encoding of mailbox files
for i in contribs/JimMoore/mail*;do
    iconv --from=ISO-8859-1 --to=UTF-8 "$i" > new
    mv new "$i"
done

# Needed by tests
mkdir -p tests/lib/
(cd tests/lib/
  ln -s `build-classpath jakarta-oro`
  ln -s `build-classpath javamail/mail`
  ln -s `build-classpath junit`
  ln -s `build-classpath jakarta-activation/jakarta.activation-api`
)

%mvn_compat_version log4j:log4j 1.2.17 1.2.16 1.2.15 1.2.14 1.2.13 1.2.12 12
# Remove Microsoft Windows platform specific files
rm -r src/main/java/org/apache/log4j/nt/NTEventLogAppender.java \
 tests/src/java/org/apache/log4j/nt/NTEventLogAppenderTest.java

# AssertionFailedError
rm tests/src/java/org/apache/log4j/net/TelnetAppenderTest.java
sed -i '/TelnetAppenderTest/d' tests/src/java/org/apache/log4j/CoreTestSuite.java

%mvn_file log4j:log4j log4j %{name}

%build
%mvn_build -- -Dsource=1.8

%install
%mvn_install -X

# log4j-1 symlink for use with build-classpath et al.
ln -s log4j-%{version}.jar %{buildroot}%{_javadir}/log4j-1.jar

%if %{with dtd}
# DTD and the SGML catalog (XML catalog handled in scriptlets)
install -pD -T -m 644 src/main/javadoc/org/apache/log4j/xml/doc-files/log4j.dtd \
  %{buildroot}%{_datadir}/sgml/log4j/log4j.dtd
install -pD -T -m 644 %{SOURCE1} \
  %{buildroot}%{_datadir}/sgml/log4j/catalog

%post
# Note that we're using versioned catalog, so this is always ok.
if [ -x %{_bindir}/install-catalog -a -d %{_sysconfdir}/sgml ]; then
  %{_bindir}/install-catalog --add \
    %{_sysconfdir}/sgml/log4j-%{version}-%{release}.cat \
    %{_datadir}/sgml/log4j/catalog > /dev/null || :
fi
if [ -x %{_bindir}/xmlcatalog -a -w %{_sysconfdir}/xml/catalog ]; then
  %{_bindir}/xmlcatalog --noout --add public "-//APACHE//DTD LOG4J 1.2//EN" \
    file://%{_datadir}/sgml/log4j/log4j.dtd %{_sysconfdir}/xml/catalog \
    > /dev/null
  %{_bindir}/xmlcatalog --noout --add system log4j.dtd \
    file://%{_datadir}/sgml/log4j/log4j.dtd %{_sysconfdir}/xml/catalog \
    > /dev/null || :
fi

%preun
if [ $1 -eq 0 ]; then
  if [ -x %{_bindir}/xmlcatalog -a -w %{_sysconfdir}/xml/catalog ]; then
    %{_bindir}/xmlcatalog --noout --del \
      file://%{_datadir}/sgml/log4j/log4j.dtd \
      %{_sysconfdir}/xml/catalog > /dev/null || :
  fi
fi

%postun
# Note that we're using versioned catalog, so this is always ok.
if [ -x %{_bindir}/install-catalog -a -d %{_sysconfdir}/sgml ]; then
  %{_bindir}/install-catalog --remove \
    %{_sysconfdir}/sgml/log4j-%{version}-%{release}.cat \
    %{_datadir}/sgml/log4j/catalog > /dev/null || :
fi

%endif # with dtd

%files -f .mfiles
%{_javadir}/log4j-1.jar
%if %{with dtd}
%{_datadir}/sgml/log4j
%endif
%license LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%license LICENSE NOTICE

%changelog
* Wed Sep 09 2020 Fabio Valentini <decathorpe@gmail.com> - 1.2.17-30
- Adapt to Java 11.

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.17-29
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.17-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 11 2020 Jiri Vanek <jvanek@redhat.com> - 1.2.17-27
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.17-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.17-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.17-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.17-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.17-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan  9 2018 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2.17-21
- Remove unneeded BR on xmvn

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.17-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 02 2017 Michael Simacek <msimacek@redhat.com> - 1.2.17-19
- Backport fix for CVE-2017-5645

* Wed Mar 15 2017 Michael Simacek <msimacek@redhat.com> - 1.2.17-18
- Add dtd conditional

* Mon Feb 13 2017 Michael Simacek <msimacek@redhat.com> - 1.2.17-17
- Add more compat versions

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.17-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Nov 17 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2.17-15
- Don't use deprecated goal of maven-assembly-plugin

* Wed Aug 10 2016 gil cattaneo <puntogil@libero.it> 1.2.17-14
- add missing build requires: xmvn
- remove test failure
- increase to 1.6 javac source/target

* Wed Jun 15 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2.17-13
- Add missing build-requires

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.17-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 30 2016 gil cattaneo <puntogil@libero.it> 1.2.17-11
- rebuilt

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.17-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Feb 10 2015 gil cattaneo <puntogil@libero.it> 1.2.17-9
- introduce license macro

* Fri Jan 23 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2.17-8
- Add symlink log4j-1

* Fri Sep 05 2014 gil cattaneo <puntogil@libero.it> 1.2.17-7
- fix rhbz#1120854

* Fri Jul 18 2014 gil cattaneo <puntogil@libero.it> 1.2.17-6
- enabling XMvn debugging output rhbz#1120854

* Thu Jul 10 2014 gil cattaneo <puntogil@libero.it> 1.2.17-5
- fix conflict rhbz#1114135

* Wed Jun 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2.17-4
- Add compat version 1.2.12 (used by velocity and xbean)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 22 2014 gil cattaneo <puntogil@libero.it> 1.2.17-2
- fix compat version

* Thu May 22 2014 gil cattaneo <puntogil@libero.it> 1.2.17-1
- initial rpm

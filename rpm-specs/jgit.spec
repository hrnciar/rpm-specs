%global gittag 5.8.0.202006091008-r

Name:           jgit
Version:        5.8.0
Release:        1%{?dist}
Summary:        A pure java implementation of git

# We don't ship the EPL-licensed Eclipse features in this package
License:        BSD
URL:            https://www.eclipse.org/jgit/
Source0:        https://git.eclipse.org/c/jgit/jgit.git/snapshot/jgit-%{gittag}.tar.xz

# Set the correct classpath for the command line tools
Patch0: 0001-Ensure-the-correct-classpath-is-set-for-the-jgit-com.patch
# Remove dep on assertj-core from bc bundle
Patch1: 0002-Unnecessary-dep-on-assertj-core-in-bc-bundle.patch

BuildArch: noarch

BuildRequires:  maven-local
BuildRequires:  mvn(args4j:args4j)
BuildRequires:  mvn(com.google.code.gson:gson)
BuildRequires:  mvn(com.googlecode.javaewah:JavaEWAH)
BuildRequires:  mvn(com.jcraft:jsch)
BuildRequires:  mvn(com.jcraft:jzlib)
BuildRequires:  mvn(javax.servlet:javax.servlet-api)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(net.i2p.crypto:eddsa)
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(org.apache.commons:commons-compress)
BuildRequires:  mvn(org.apache.httpcomponents:httpclient)
BuildRequires:  mvn(org.apache.httpcomponents:httpcore)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.apache.sshd:sshd-osgi) >= 2.4.0
BuildRequires:  mvn(org.apache.sshd:sshd-sftp) >= 2.4.0
BuildRequires:  mvn(org.bouncycastle:bcpg-jdk15on) >= 1.65
BuildRequires:  mvn(org.bouncycastle:bcpkix-jdk15on) >= 1.65
BuildRequires:  mvn(org.bouncycastle:bcprov-jdk15on) >= 1.65
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.eclipse.jetty:jetty-servlet)
BuildRequires:  mvn(org.osgi:osgi.core)
BuildRequires:  mvn(org.slf4j:slf4j-api)
BuildRequires:  mvn(org.slf4j:slf4j-simple)
BuildRequires:  mvn(org.tukaani:xz)

# Runtime requirements
Requires:       bouncycastle >= 1.65
Requires:       apache-sshd >= 1:2.4.0
Requires:       jzlib

%description
A pure Java implementation of the Git version control system and command
line interface.

%package javadoc
Summary:        API documentation for %{name}

%description javadoc
%{summary}.

%prep
%setup -n jgit-%{gittag} -q
%patch0 -p1
%patch1 -p1

# Disable multithreaded build
rm .mvn/maven.config

# Disable "errorprone" compiler that is not available in distro
%pom_xpath_remove "pom:plugin[pom:artifactId='maven-compiler-plugin']/pom:executions/pom:execution[pom:id='compile-with-errorprone']" pom.xml
%pom_xpath_remove "pom:plugin[pom:artifactId='maven-compiler-plugin']/pom:executions/pom:execution[pom:id='default-compile']/pom:configuration" pom.xml
%pom_xpath_remove "pom:plugin[pom:artifactId='maven-compiler-plugin']/pom:dependencies" pom.xml

# Use newer Felix dep
%pom_change_dep -r org.osgi:org.osgi.core org.osgi:osgi.core:\${osgi-core-version}:provided

# Remove unnecessary plugins for RPM builds
%pom_disable_module org.eclipse.jgit.coverage
%pom_disable_module org.eclipse.jgit.benchmarks
%pom_remove_plugin :jacoco-maven-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin -r :maven-source-plugin
%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin -r :japicmp-maven-plugin

# Avoid failures due to lack of jacoco
sed -i -e 's/@{argLine}//' $(find -name pom.xml)

# Don't attach shell script artifact
%pom_remove_plugin org.codehaus.mojo:build-helper-maven-plugin org.eclipse.jgit.pgm

# Don't have spring-boot
%pom_remove_plugin :spring-boot-maven-plugin org.eclipse.jgit.pgm
%pom_xpath_remove "pom:plugins/pom:plugin/pom:executions/pom:execution[pom:id='create_jgit']" org.eclipse.jgit.pgm
sed -i -e 's/org\.springframework\.boot\.loader\.JarLauncher/org.eclipse.jgit.pgm.Main/' \
  org.eclipse.jgit.pgm/jgit.sh

# Relax junit restriction
sed -i -e '/org\.junit/s/4\.13/4.12/' $(grep -r -l --include MANIFEST.MF org.junit)

# Relax jsch restriction
sed -i -e '/jsch/s/1\.55/1.54/' org.eclipse.jgit.junit.ssh/META-INF/MANIFEST.MF

# Remove unnecessary dep on org.apache.log4j
%pom_remove_dep log4j:log4j . org.eclipse.jgit.pgm
%pom_change_dep org.slf4j:slf4j-log4j12 org.slf4j:slf4j-simple . org.eclipse.jgit.pgm

# No need to build test modules if we aren't running tests
sed -i -e '/\.test<\/module>/d' pom.xml

# Never install test jars
%mvn_package ":*.test" __noinstall

%build
# Don't run tests due to missing dependencies
%mvn_build -f -- -Pjavac

%install
%mvn_install

# Install CLI invoker script
install -dm 755 %{buildroot}%{_bindir}
install -m 755 org.eclipse.jgit.pgm/jgit.sh %{buildroot}%{_bindir}/jgit

# Ant task configuration
install -dm 755 %{buildroot}%{_sysconfdir}/ant.d
cat > %{buildroot}%{_sysconfdir}/ant.d/jgit <<EOF
jgit/org.eclipse.jgit jgit/org.eclipse.jgit.ant slf4j/slf4j-api slf4j/slf4j-simple jzlib jsch commons-compress xz-java javaewah httpcomponents/httpcore httpcomponents/httpclient commons-logging commons-codec eddsa apache-sshd/sshd-osgi apache-sshd/sshd-sftp
EOF

%files -f .mfiles
%license LICENSE
%doc README.md
%{_bindir}/jgit
%config(noreplace) %{_sysconfdir}/ant.d/jgit

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
* Mon Jun 22 2020 Mat Booth <mat.booth@redhat.com> - 5.8.0-1
- Update to latest upstream release

* Fri May 15 2020 Mat Booth <mat.booth@redhat.com> - 5.7.0-3
- Fix erroneous dep on osgi.core with provided scope

* Sun Mar 22 2020 Mat Booth <mat.booth@redhat.com> - 5.7.0-2
- Relax dep on junit

* Sun Mar 22 2020 Mat Booth <mat.booth@redhat.com> - 5.7.0-1
- Update to latest upstream release

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 19 2019 Mat Booth <mat.booth@redhat.com> - 5.6.0-1
- Update to latest upstream release

* Tue Sep 17 2019 Mat Booth <mat.booth@redhat.com> - 5.5.0-1
- Update to latest upstream release

* Thu Jul 25 2019 Mat Booth <mat.booth@redhat.com> - 5.4.0-6
- Make dep on OSGi 'provided' in scope

* Thu Jul 25 2019 Mat Booth <mat.booth@redhat.com> - 5.4.0-5
- Ignore test failures again due to 'Mount point not found' errors

* Thu Jul 25 2019 Mat Booth <mat.booth@redhat.com> - 5.4.0-4
- Better summary to avoid rpmlint warnings and add better comments
- Conditionalise BR on git with other test dependencies
- Drop explicit dep on jzlib, jgit no longer considers it optional
- Simplify javadoc package specification
- Use of maven-source-plugin is unnecessary for RPM builds
- Don't ignore test failures
- Truncate changelog

* Wed Jul 24 2019 Mat Booth <mat.booth@redhat.com> - 5.4.0-3
- Package jgit libs and command line tooling separately from the Eclipse plug-in


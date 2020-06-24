%global namedreltag .Beta3
%global namedversion %{version}%{?namedreltag}

Name:           papaki
Version:        1.0.0
Release:        0.17%{?namedreltag}%{?dist}
Summary:        An annotation scanner and repository

License:        LGPLv2+
URL:            http://anonsvn.jboss.org/repos/jbossas/projects/annotations/trunk/


# svn export http://anonsvn.jboss.org/repos/jbossas/projects/annotations/tags/PAPAKI_1_0_0_BETA3 papaki-1.0.0.Beta3
# find papaki-1.0.0.Beta3 -name "*.jar" -type f -delete
# find papaki-1.0.0.Beta3 -name ".svn" -type d | xargs rm -rf
# tar -czf papaki-1.0.0.Beta3.tar.gz papaki-1.0.0.Beta3
# List of removed files: https://gist.github.com/2496466
Source0:        %{name}-%{namedversion}.tar.gz

# POM file for artifact: papaki-core
Source1:        https://repository.jboss.org/nexus/content/groups/public/org/jboss/papaki/papaki-core/1.0.0.Beta3/papaki-core-1.0.0.Beta3.pom

# POM file for artifact: papaki-indexer
Source2:        https://repository.jboss.org/nexus/content/groups/public/org/jboss/papaki/papaki-indexer/1.0.0.Beta3/papaki-indexer-1.0.0.Beta3.pom

# Commented out retrieving jars from Internet and limiting the jars to build
Patch0:         %{name}-ivy.patch

# Commented out trying to download Ivy from the Internet
Patch1:         %{name}-build.patch

# Add jdepend to classpath for javadoc
Patch2:         %{name}-javadoc.patch
 
BuildArch:      noarch

BuildRequires:  javapackages-local
BuildRequires:  java-devel >= 1:1.6.0

BuildRequires:  apache-ivy
BuildRequires:  junit
BuildRequires:  ant
BuildRequires:  apiviz
BuildRequires:  jdepend
BuildRequires:  javassist

Requires:       javassist

%description
Papaki is a library for scanning annotations in Java 5+ code
and generate a repository of these annotations.

%package javadoc
Summary:          Javadocs for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}

%patch0 -p1
%patch1 -p1
%patch2 -p1

# Remove class-path from MANIFEST.MF
sed -i '/class-path/I d' core/src/main/resources/core-manifest.mf
sed -i '/class-path/I d' indexer/src/main/resources/indexer-manifest.mf

%build
ant docs release

%install

install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# JARs
install -pm 644 target/%{name}-core.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-core.jar
install -pm 644 target/%{name}-indexer.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-indexer.jar

# POMs
install -pm 644 %{SOURCE1} $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-%{name}-core.pom
install -pm 644 %{SOURCE2} $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-%{name}-indexer.pom

%add_maven_depmap JPP.%{name}-%{name}-core.pom %{name}/%{name}-core.jar
%add_maven_depmap JPP.%{name}-%{name}-indexer.pom %{name}/%{name}-indexer.jar

# JAVADOC
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}/%{name}-core
cp -rp build/%{name}-%{namedversion}/doc/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}/%{name}-core
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}/%{name}-indexer
cp -rp target/docs/indexer/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}/%{name}-indexer

%files
%{_mavenpomdir}/*
%{_javadir}/*
%{_datadir}/maven-metadata/*
%doc README.txt

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.17.Beta3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.16.Beta3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.15.Beta3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 23 2018 Lin Gao <lgao@redhat.com> - 1.0.0-0.14.Beta3
- Replace BuildRequires from jpackage-utils to javapackages-local

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.13.Beta3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.0-0.12.Beta3
- Escape macros in %%changelog

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.11.Beta3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.10.Beta3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.9.Beta3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.8.Beta3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-0.7.Beta3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 25 2014 Lin Gao <lgao@redhat.com> - 1.0.0-0.6.Beta3
- Fix %%files list(#1105925)

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-0.5.Beta3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-0.4.Beta3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-0.3.Beta3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-0.2.Beta3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon May 14 2012 Lin Gao <lgao@redhat.com> 1.0.0-0.1.Beta3
- Initial packaging

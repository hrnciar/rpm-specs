%global	commit		4f623957bc2cc1b90c254cec70f73b28f68a9278
%global shortcommit	%(c=%{commit}; echo ${c:0:7})

Name:		jacop
Version:	4.7
Release:	4%{?dist}
License:	AGPLv3 with exceptions 
Summary:	Java Constraint Programming solver
URL:		http://jacop.osolpro.com/
Source0:	https://github.com/radsz/%{name}/archive/%{commit}/%{name}-%{commit}.tar.gz
BuildRequires:	maven-local
BuildRequires:	mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:	mvn(org.codehaus.mojo:javacc-maven-plugin)
BuildRequires:	mvn(org.mockito:mockito-all)
BuildRequires:	mvn(org.scala-lang:scala-compiler)
BuildArch:	noarch

%description
Java Constraint Programming solver, JaCoP for short, is an open-source
Java library, which provides Java users with Constraint Programming
technology.  JaCoP has been under active development since the year
2001.  Krzysztof Kuchcinski and Radoslaw Szymanek are the core
developers of this Java library.

%package javadoc
Summary:	Javadocs for %{name}

%description	javadoc
This package contains the API documentation for %{name}.

%prep
%autosetup -n %{name}-%{commit}

# jacoco-maven-plugin has been dropped from Fedora
%pom_remove_plugin org.jacoco:jacoco-maven-plugin

# maven-scala-plugin is not available in Fedora
%pom_remove_plugin org.scala-tools:maven-scala-plugin

# maven-jdeps-plugin is not available in Fedora
%pom_remove_plugin org.apache.maven.plugins:maven-jdeps-plugin

# We do not need to create a source jar
%pom_remove_plugin org.apache.maven.plugins:maven-source-plugin

# Remove unnecessary dependency on maven-javadoc-plugin
%pom_remove_plugin :maven-javadoc-plugin

# scala-xml is not available in Fedora
%pom_remove_dep org.scala-lang.modules:scala-xml_2.12

# Remove unused slf4j dependencies.  Will be in upstream version 4.8.
# https://github.com/radsz/jacop/commit/e61795bdd161499173933bd90a7ecfc0804e76df
%pom_remove_dep org.slf4j

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%license LICENSE.md
%doc CHANGELOG README.md

%files javadoc -f .mfiles-javadoc
%license LICENSE.md

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 18 2020 Fabio Valentini <decathorpe@gmail.com> - 4.7-3
- Remove unnecessary dependency on maven-javadoc-plugin.

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 4.7-2
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Fri Feb 21 2020 Jerry James <loganjerry@gmail.com> - 4.7-1
- Version 4.7
- Upstream now ships a license file
- Drop unnecessary BRs
- Drop upstreamed -privilege patch

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Nov 14 2017 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 4.2-7
- Correct FTBFS in rawhide (#1423750)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 22 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 4.2-3
- Rebuild for newer scala.

* Sun Jan 25 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 4.2-2
- Use the license macro (#1177191#c2)
- Add explicit requires to owners of directories (#1177191#c2)
- Become owner of maven-poms/jacop directory (#1177191#c2)

* Sat Dec 20 2014 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 4.2-1
- Initial jacop spec.

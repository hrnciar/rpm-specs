%global spec_ver 1.1
%global spec_name geronimo-jcdi_%{spec_ver}_spec

%global namedreltag %nil
%global namedversion %{version}%{?namedreltag}

Name:          geronimo-jcdi-1.1-api
Version:       1.0
Release:       8%{?dist}
Summary:       Apache Geronimo JCDI Spec 1.1
License:       ASL 2.0
URL:           http://geronimo.apache.org/
Source0:       http://repo2.maven.org/maven2/org/apache/geronimo/specs/%{spec_name}/%{namedversion}/%{spec_name}-%{namedversion}-source-release.zip

BuildRequires: maven-local
BuildRequires: mvn(javax.el:javax.el-api)
BuildRequires: mvn(javax.inject:javax.inject)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.geronimo.specs:specs-parent:pom:)
BuildRequires: mvn(org.apache.geronimo.specs:geronimo-annotation_1.1_spec)
BuildRequires: mvn(org.jboss.spec.javax.interceptor:jboss-interceptors-api_1.2_spec)

BuildArch:     noarch

%description
Apache Geronimo implementation of the JSR-346 Context and
Dependency Injection 1.1 and 1.2 Specification.

%package javadoc
Summary:       Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{spec_name}-%{namedversion}

# org.apache.geronimo.genesis:genesis-java5-flava:2.2
%pom_remove_parent
%pom_add_parent org.apache.geronimo.specs:specs-parent:1.6

%pom_change_dep org.apache.geronimo.specs:geronimo-el_2.2_spec javax.el:javax.el-api:3.0.0
%pom_change_dep :geronimo-interceptor_1.1_spec org.jboss.spec.javax.interceptor:jboss-interceptors-api_1.2_spec:1.0.0.Final
%pom_change_dep :geronimo-atinject_1.0_spec javax.inject:javax.inject:1

sed -i 's,${artifactId},${project.artifactId},;s,${version},${project.version},' pom.xml

%mvn_file : %{name}

%build

%mvn_build -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%license LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%license LICENSE NOTICE

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Oct 30 2015 gil cattaneo <puntogil@libero.it> 1.0-1
- update to 1.0

* Mon Feb 02 2015 gil cattaneo <puntogil@libero.it> 1.0-0.1.alpha.1
- initial rpm

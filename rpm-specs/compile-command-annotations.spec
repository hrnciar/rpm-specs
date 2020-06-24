Name:          compile-command-annotations
Version:       1.2.1
Release:       7%{?dist}
Summary:       Hotspot compile command annotations
License:       ASL 2.0
URL:           https://github.com/nicoulaj/compile-command-annotations
Source0:       https://github.com/nicoulaj/compile-command-annotations/archive/%{version}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(com.google.guava:guava)
BuildRequires: mvn(commons-io:commons-io)
#BuildRequires: mvn(org.apache.maven.plugins:maven-invoker-plugin)
BuildRequires: mvn(org.assertj:assertj-core)
BuildRequires: mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires: mvn(org.codehaus.mojo:exec-maven-plugin)
BuildRequires: mvn(org.testng:testng)
BuildRequires: mvn(org.jacoco:jacoco-maven-plugin)
# For IT suite
#BuildRequires: mvn(org.codehaus.groovy:groovy)

BuildArch:     noarch

%description
Annotation based configuration file generator for the
Hotspot JVM JIT compiler.

%package javadoc
Summary:       Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{version}

# net.ju-n:net-ju-n-parent:32
%pom_remove_parent

# Prevent IT failures
#find ./src/it/tests -name "pom.xml" -exec sed -i "s/@project.build.sourceEncoding@/UTF-8/g" {} +
#find ./src/it/tests -name "pom.xml" -exec sed -i "s/@exec-maven-plugin.version@/1.4.0/g" {} +
#find ./src/it/tests -name "pom.xml" -exec sed -i "s/@maven-compiler-plugin.version@/3.3/g" {} +
# Fails on koji only
%pom_remove_plugin :maven-invoker-plugin

# TestNG support requires version 4.7 or above
%pom_change_dep :testng ::6.8.21

%mvn_file net.ju-n.compile-command-annotations:%{name} %{name}

%build

%mvn_build -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%doc README.md
%license COPYING

%files javadoc -f .mfiles-javadoc
%license COPYING

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Mar 07 2017 Tomas Repik <trepik@redhat.com> - 1.2.1-1
- version update

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jul 20 2015 gil cattaneo <puntogil@libero.it> 1.2.0-1
- initial rpm

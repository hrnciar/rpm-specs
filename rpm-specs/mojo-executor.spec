# Testing note: this package relies on an old version of mockito.  Compilation
# of the tests fails with the version of mockito currently in Fedora.  Porting
# to the new version is needed.

Name:           mojo-executor
Version:        2.3.1
Release:        4%{?dist}
Summary:        Execute other plugins within a maven plugin

License:        ASL 2.0
URL:            https://github.com/TimMoore/%{name}
Source0:        %{url}/archive/%{name}-parent-%{version}.tar.gz
# Convert from commons-lang to commons-lang3
# https://pagure.io/java-maint-sig/issue/4
Patch0:         %{name}-commons-lang3.patch

BuildArch:      noarch
BuildRequires:  maven-local
BuildRequires:  mvn(ant-contrib:ant-contrib)
BuildRequires:  mvn(org.apache.commons:commons-lang3)
BuildRequires:  mvn(org.apache.maven:maven-parent:pom:)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-invoker-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.jacoco:jacoco-maven-plugin)
BuildRequires:  mvn(org.mockito:mockito-core)

%description
The Mojo Executor provides a way to to execute other Mojos (plugins)
within a Maven plugin, allowing you to easily create Maven plugins that
are composed of other plugins.

%package parent
Summary:        Parent POM for mojo-executor

%description parent
%{summary}.

%package maven-plugin
Summary:        Maven plugin for mojo-executor

%description maven-plugin
%{summary}.

%package javadoc
Summary:        API documentation for %{name}

%description javadoc
This package contains %{summary}.

%prep
%autosetup -n %{name}-%{name}-parent-%{version} -p1

# sonatype-oss-parent is deprecated in Fedora
%pom_remove_parent

# maven-release is not needed
%pom_remove_plugin :maven-release-plugin

# Modernize the junit dependency
%pom_change_dep :junit-dep :junit mojo-executor-maven-plugin/src/it/mojo-executor-test-project/pom.xml
%pom_change_dep :junit-dep :junit mojo-executor-maven-plugin/src/it/mojo-executor-test-project-no-plugin-version/pom.xml
%pom_change_dep :junit-dep :junit mojo-executor-maven-plugin/src/it/mojo-executor-test-project-null-maven-project/pom.xml
%pom_change_dep :junit-dep :junit mojo-executor-maven-plugin/src/it/mojo-executor-test-project-quiet/pom.xml

# ant-contrib has no POM
%pom_remove_dep ant-contrib: mojo-executor-maven-plugin/src/it/mojo-executor-test-project-with-dependencies/pom.xml
sed -i 's,classpath.*,classpath="%{_javadir}/ant-contrib/ant-contrib.jar" />,' \
  mojo-executor-maven-plugin/src/it/mojo-executor-test-project-with-dependencies/pom.xml

%build
%mvn_build -s -f

%install
%mvn_install

%files -f .mfiles-%{name}
%license LICENSE.txt
%doc README.md

%files parent -f .mfiles-%{name}-parent

%files maven-plugin -f .mfiles-%{name}-maven-plugin

%files javadoc -f .mfiles-javadoc

%changelog
* Sun Aug  2 2020 Jerry James <loganjerry@gmail.com> - 2.3.1-4
- Add -commons-lang3 patch

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Apr 30 2020 Jerry James <loganjerry@gmail.com> - 2.3.1-2
- Drop unnecessary maven-release-plugin BR

* Sat Jan 18 2020 Jerry James <loganjerry@gmail.com> - 2.3.1-1
- Initial RPM

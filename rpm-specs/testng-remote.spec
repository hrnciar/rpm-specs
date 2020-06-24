%global gittag testng-remote-parent-%{version}

Name:    testng-remote
Version: 1.3.0
Release: 6%{?dist}
Summary: Modules for running TestNG remotely
# org/testng/remote/strprotocol/AbstractRemoteTestRunnerClient.java is CPL
License: ASL 2.0 and CPL
URL:     https://github.com/testng-team/testng-remote
Source0: https://github.com/testng-team/testng-remote/archive/%{gittag}.tar.gz

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(com.google.auto.service:auto-service)
BuildRequires:  mvn(com.google.code.gson:gson)
BuildRequires:  mvn(org.apache.maven.plugins:maven-shade-plugin)
BuildRequires:  mvn(org.testng:testng) >= 6.12

Requires:  mvn(org.testng:testng) >= 6.12

%description
TestNG Remote contains the modules for running TestNG remotely. This is
normally used by IDE to communicate with TestNG run-time, e.g. receive the
Test Result from run-time so that can display them on IDE views.

%package javadoc
Summary: API documentation for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n testng-remote-%{gittag}

# Avoid bundling gson
%pom_remove_plugin :maven-shade-plugin remote

# Plugin not in Fedora
%pom_remove_plugin :git-commit-id-plugin
%pom_remove_plugin :git-commit-id-plugin remote
sed -i -e 's/${git.branch}/%{gittag}/' -e 's/${git.commit.id}/%{gittag}/' -e 's/${git.build.version}/%{version}/' \
  remote/src/main/resources/revision.properties

# Not needed for RPM builds
%pom_remove_plugin -r :jacoco-maven-plugin

# Disable support for old versions of TestNG that are not in Fedora
%pom_disable_module remote6_10
%pom_disable_module remote6_9_10
%pom_disable_module remote6_9_7
%pom_disable_module remote6_5
%pom_disable_module remote6_0
%pom_remove_dep :testng-remote6_10 dist
%pom_remove_dep :testng-remote6_9_10 dist
%pom_remove_dep :testng-remote6_9_7 dist
%pom_remove_dep :testng-remote6_5 dist
%pom_remove_dep :testng-remote6_0 dist

# Package the shaded artifact (contains all testng-remote modules in a single jar)
%mvn_package ":testng-remote-dist:jar:shaded:"

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%license LICENSE

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jul 28 2017 Mat Booth <mat.booth@redhat.com> - 1.3.0-1
- Update to latest release for testng 6.12 compatibility

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 04 2017 Mat Booth <mat.booth@redhat.com> - 1.2.1-1
- Update to latest release

* Wed Jun 14 2017 Mat Booth <mat.booth@redhat.com> - 1.1.0-4
- Remove unneeded jacoco plugin

* Fri Feb 17 2017 Mat Booth <mat.booth@redhat.com> - 1.1.0-3
- License correction

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Nov 01 2016 Mat Booth <mat.booth@redhat.com> - 1.1.0-1
- Update to tagged release
- Enable tests

* Mon Apr 25 2016 Mat Booth <mat.booth@redhat.com> - 1.0.0-0.2.gitfc5cfab
- Package the all-in-one shaded jar

* Mon Apr 25 2016 Mat Booth <mat.booth@redhat.com> - 1.0.0-0.1.gitfc5cfab
- Initial packaging of latest upstream snapshot.


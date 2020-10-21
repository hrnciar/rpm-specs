Name:           maven-patch-plugin
Version:        1.2
Release:        15%{?dist}
Summary:        Maven Patch Plugin

License:        ASL 2.0
URL:            http://maven.apache.org/plugins/maven-patch-plugin/
Source0:        http://repo1.maven.org/maven2/org/apache/maven/plugins/%{name}/%{version}/%{name}-%{version}-source-release.zip

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven.plugins:maven-clean-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-install-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-invoker-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugins:pom:)

%description
The Patch Plugin is used to apply patches to source files.

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
API documentation for %{name}.

%prep
%setup -q

%build
%mvn_build --post "install invoker:run" -- -Dmaven.repo.local=$PWD/.m2

%install
%mvn_install

%files -f .mfiles
%license LICENSE NOTICE
%dir %{_javadir}/%{name}

%files javadoc -f .mfiles-javadoc
%license LICENSE NOTICE

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 1.2-14
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 08 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 1.2-12
- Drop BuildRequires: mvn(org.apache.maven.plugins:maven-docck-plugin)
- Build for EPEL 8

* Tue Jan 07 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 1.2-11
- Drop BuildRequires: mvn(org.apache.maven.plugins:maven-deploy-plugin)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Apr 04 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 1.2-9
- Drop BuildRequires: mvn(org.apache.maven.plugins:maven-gpg-plugin)

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Feb 16 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 1.2-4
- Add missing BuildRequires on maven-plugins-pom

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.2-1
- Update to version 1.2

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Sep 11 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.1.1-8
- Use mvn-build instead of mvn-rpmbuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.1.1-5
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Sun Nov 25 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.1.1-4
- Add NOTICE file to javadoc package

* Sun Nov 25 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.1.1-3
- Enable tests on Fedora 19 again - broken dependancies fixed

* Fri Nov 23 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.1.1-2
- Disable tests on Fedora 19 due to broken dependencies

* Thu Nov  1 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.1.1-1
- Initial Package

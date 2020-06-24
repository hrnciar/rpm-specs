Name:           jnr-unixsocket
Version:        0.21
Release:        4%{?dist}
Summary:        Unix sockets for Java
License:        ASL 2.0
URL:            https://github.com/jnr/%{name}/
Source0:        https://github.com/jnr/%{name}/archive/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(com.github.jnr:jnr-constants)
BuildRequires:  mvn(com.github.jnr:jnr-enxio)
BuildRequires:  mvn(com.github.jnr:jnr-ffi)
BuildRequires:  mvn(com.github.jnr:jnr-posix)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)

%description
Unix sockets for Java.

%package javadoc
Summary:        Javadocs for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}

find ./ -name '*.jar' -delete
find ./ -name '*.class' -delete

# remove unnecessary wagon extension
%pom_xpath_remove pom:build/pom:extensions

# Unnecessary for RPM builds
%pom_remove_plugin :maven-checkstyle-plugin
%pom_remove_plugin :findbugs-maven-plugin
%pom_remove_plugin :maven-pmd-plugin
%pom_remove_plugin :maven-javadoc-plugin

# Can't run integration tests
%pom_remove_plugin :maven-assembly-plugin
%pom_remove_plugin :exec-maven-plugin

# Remove enxio classes to avoid OSGi split-package problems,
# see https://github.com/jnr/jnr-unixsocket/pull/41
rm -r src/main/java/jnr/enxio

# Fix jar plugin usage
%pom_xpath_remove "pom:plugin[pom:artifactId='maven-jar-plugin']/pom:executions"

%build
# Tests fails on some arches
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%license LICENSE
%doc README.md

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Dec 08 2018 Mat Booth <mat.booth@redhat.com> - 0.21-1
- Update to latest upstream release

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 08 2018 Mat Booth <mat.booth@redhat.com> - 0.18-4
- Avoid OSGi split-package problems

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 30 2017 Mat Booth <mat.booth@redhat.com> - 0.18-2
- Disable tests that fail on some architectures

* Fri Jun 30 2017 Mat Booth <mat.booth@redhat.com> - 0.18-1
- Update to latest release

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 16 2016 Merlin Mathesius <mmathesi@redhat.com> - 0.12-2
- Add missing BuildRequires to fix FTBFS (BZ#1405615).

* Tue Apr 19 2016 Alexander Kurtakov <akurtako@redhat.com> 0.12-1
- Update to upstream 0.12 release and remove custom OSGification(done upstream).

* Fri Feb 5 2016 Alexander Kurtakov <akurtako@redhat.com> 0.10-1
- Update to upstream 0.10 release.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Jeff Johnston <jjohnstn@redhat.com> 0.8-3
- Add MANIFEST.MF.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue May 5 2015 Alexander Kurtakov <akurtako@redhat.com> 0.8-1
- Update to upstream 0.8 release.

* Fri Jun 27 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 0.2-5
- Update junit BRs (#1106960)

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 0.2-3
- Use Requires: java-headless rebuild (#1067528)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Feb 11 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 0.2-1
- Initial package.

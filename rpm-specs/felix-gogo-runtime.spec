%global bundle  org.apache.felix.gogo.runtime

Name:           felix-gogo-runtime
Version:        1.1.0
Release:        8%{?dist}
Summary:        Apache Felix Gogo command line shell for OSGi
# One file is also MIT licensed:
#  src/main/java/org/apache/felix/gogo/runtime/Expression.java
License:        ASL 2.0 and MIT
URL:            http://felix.apache.org/documentation/subprojects/apache-felix-gogo.html

Source0:        http://archive.apache.org/dist/felix/%{bundle}-%{version}-source-release.tar.gz

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:gogo-parent:pom:) >= 4
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.mockito:mockito-core)
BuildRequires:  mvn(org.osgi:osgi.cmpn)
BuildRequires:  mvn(org.osgi:osgi.core)

%description
Apache Felix Gogo is a subproject of Apache Felix implementing a command
line shell for OSGi. It is used in many OSGi runtimes and servers.

%package javadoc
Summary: Javadoc for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{bundle}-%{version}

# Remove 2 failing assertions on Java 11 in TestParser.testPipe()
sed -i '/(echoout/ d' src/test/java/org/apache/felix/gogo/runtime/TestParser.java

%mvn_file : felix/%{bundle}

%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dsource=1.8 -DdetectJavaApiLink=false

%install
%mvn_install

%files -f .mfiles
%license LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%license LICENSE NOTICE

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 1.1.0-7
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Fri Jun 26 2020 Roland Grunberg <rgrunber@redhat.com> - 1.1.0-6
- Set source/target to 1.8 for Java 11 build.
- Disable Java API link detection for javadoc generation as this fails.
- Disable some assertions in TestParser.testPipe() that fail on Java 11.

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 12 2019 Mat Booth <mat.booth@redhat.com> - 1.1.0-4
- Fix license tag to include MIT

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Aug 17 2018 Mat Booth <mat.booth@redhat.com> - 1.1.0-1
- Update to latest release
- Enable tests

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri May 05 2017 Michael Simacek <msimacek@redhat.com> - 1.0.4-1
- Update to upstream version 1.0.4

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jun 16 2016 Alexander Kurtakov <akurtako@redhat.com> 0.16.2-4
- Add BR maven-bundle-plugin to fix build.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jun 29 2015 Mat Booth <mat.booth@redhat.com> - 0.16.2-2
- Remove incomplete and forbidden SCL macros

* Fri Jun 19 2015 Alexander Kurtakov <akurtako@redhat.com> 0.16.2-1
- Update to upstream 0.16.2.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jul 3 2014 Alexander Kurtakov <akurtako@redhat.com> 0.12.1-1
- Update to upstream 0.12.1.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.10.0-11
- Use Requires: java-headless rebuild (#1067528)

* Tue Aug 06 2013 Michal Srb <msrb@redhat.com> - 0.10.0-10
- Adapt to current guidelines
- Install NOTICE file with javadoc subpackage

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Mar 15 2013 Krzysztof Daniel <kdaniel@redhat.com> 0.10.0-8
- Initial SCLization.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 0.10.0-6
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jan 18 2012 Tomas Radej <tradej@redhat.com> - 0.10.0-4
- Changed jar path

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Dec 16 2011 Tomas Radej <tradej@redhat.com> - 0.10.0-2
- Repackaged, minor changes

* Mon Nov 07 2011 Tomas Radej <tradej@redhat.com> - 0.10.0-1
- Initial packaging

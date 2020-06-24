Name:           maven-invoker
Version:        3.0.1
Release:        2%{?dist}
Summary:        Fires a maven build in a clean environment
License:        ASL 2.0
URL:            http://maven.apache.org/shared/maven-invoker/
BuildArch:      noarch

Source0:        http://repo1.maven.org/maven2/org/apache/maven/shared/%{name}/%{version}/%{name}-%{version}-source-release.zip

# Patch rejected upstream
Patch1:         %{name}-MSHARED-279.patch

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-components:pom:)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-annotations)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
# Required by tests
BuildRequires:  maven-antrun-plugin
BuildRequires:  maven-clean-plugin

%description
This API is concerned with firing a Maven build in a new JVM. It accomplishes
its task by building up a conventional Maven command line from options given in
the current request, along with those global options specified in the invoker
itself. Once it has the command line, the invoker will execute it, and capture
the resulting exit code or any exception thrown to signal a failure to execute.
Input/output control can be specified using an InputStream and up to two
InvocationOutputHandlers.

This is a replacement package for maven-shared-invoker

%package javadoc
Summary:        Javadoc for %{name}
    
%description javadoc
API documentation for %{name}.

%prep
%setup -q
%patch1 -p1

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Aug 08 2019 Marian Koncek <mkoncek@redhat.com> - 3.0.1-1
- Update to upstream version 3.0.1

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jun 15 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2-4
- Regenerate build-requires
- Remove old obsoletes/provides

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Mar 25 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2-1
- Update to upstream version 2.2

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Sep 23 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.1.1-10
- Fix failing tests

* Mon Sep 23 2013 Michal Srb <msrb@redhat.com> - 2.1.1-9
- Remove some tests which fail on koji

* Mon Sep 23 2013 Michal Srb <msrb@redhat.com> - 2.1.1-8
- Migrate to XMvn

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Mar 13 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.1.1-6
- Add patch for MSHARED-278, resolves rhbz#921068
- Add patch for MSHARED-279, resolves rhbz#921067

* Wed Feb 20 2013 Tomas Radej <tradej@redhat.com> - 2.1.1-5
- Added B/R on maven-shared

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 2.1.1-3
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Mon Jan 14 2013 Tomas Radej <tradej@redhat.com> - 2.1.1-2
- Disabled tests

* Fri Jan 11 2013 Tomas Radej <tradej@redhat.com> - 2.1.1-1
- Initial version


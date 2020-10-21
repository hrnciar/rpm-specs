Name:           maven-javadoc-plugin
Version:        3.2.0
Release:        3%{?dist}
Summary:        Maven Javadoc Plugin
License:        ASL 2.0

URL:            https://maven.apache.org/plugins/maven-javadoc-plugin
Source0:        https://repo1.maven.org/maven2/org/apache/maven/plugins/%{name}/%{version}/%{name}-%{version}-source-release.zip

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(com.thoughtworks.qdox:qdox)
BuildRequires:  mvn(org.apache.commons:commons-lang3)
BuildRequires:  mvn(org.apache.httpcomponents:httpclient)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-sink-api)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-site-renderer)
BuildRequires:  mvn(org.apache.maven:maven-archiver)
BuildRequires:  mvn(org.apache.maven:maven-artifact)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-model)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven:maven-settings)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugins:pom:)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.reporting:maven-reporting-api)
BuildRequires:  mvn(org.apache.maven.shared:maven-artifact-transfer) >= 0.11.0
BuildRequires:  mvn(org.apache.maven.shared:maven-common-artifact-filters)
BuildRequires:  mvn(org.apache.maven.shared:maven-invoker)
BuildRequires:  mvn(org.apache.maven.wagon:wagon-provider-api)
BuildRequires:  mvn(org.codehaus.modello:modello-maven-plugin)
BuildRequires:  mvn(org.codehaus.plexus:plexus-archiver)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-annotations)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:  mvn(org.codehaus.plexus:plexus-interactivity-api)
BuildRequires:  mvn(org.codehaus.plexus:plexus-io)
BuildRequires:  mvn(org.codehaus.plexus:plexus-java)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)

%description
The Maven Javadoc Plugin is a plugin that uses the javadoc tool for
generating javadocs for the specified project.

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n %{name}-%{version}

%build
%mvn_build -f -- -DmavenVersion=3.6.0

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 3.2.0-2
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Wed May 06 2020 Fabio Valentini <decathorpe@gmail.com> - 3.2.0-1
- Update to version 3.2.0.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 20 2019 Fabio Valentini <decathorpe@gmail.com> - 3.1.1-2
- Non-bootstrap build with re-enabled javadoc generation.

* Sun Nov 03 2019 Fabio Valentini <decathorpe@gmail.com> - 3.1.1-1
- Update to version 3.1.1.
- Bootstrap build without javadocs for maven-artifact-transfer 0.11.0 rebuild.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Michael Simacek <msimacek@redhat.com> - 3.0.1-1
- Update to upstream version 3.0.1

* Fri Feb 23 2018 Michael Simacek <msimacek@redhat.com> - 3.0.0-4
- Remove maven-enforcer-plugin (fixes FTBFS)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Dec 07 2017 Michael Simacek <msimacek@redhat.com> - 3.0.0-2
- Update to upstream version 3.0.0

* Wed Sep 13 2017 Michael Simacek <msimacek@redhat.com> - 3.0.0-1
- Update to upstream version 3.0.0-M1

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Michael Simacek <msimacek@redhat.com> - 2.10.4-3
- Specify the exact version

* Thu Feb 09 2017 Michael Simacek <msimacek@redhat.com> - 2.10.4-2
- Use log4j12

* Mon Jun 13 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.10.4-1
- Update to upstream version 2.10.4

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Apr 10 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.10.3-1
- Update to upstream version 2.10.3

* Wed Mar 18 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.10.2-1
- Update to upstream version 2.10.2

* Wed Nov 12 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.10.1-3
- Remove dependency on qdox

* Tue Oct 14 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.10.1-2
- Remove legacy Obsoletes/Provides for maven2 plugin

* Mon Sep 29 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.10.1-1
- Update to upstream version 2.10.1

* Tue Sep 16 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.10-1
- Update to upstream version 2.10

* Fri Jul 18 2014 Roland Grunberg <rgrunber@redhat.com> - 2.9.1-10
- Rebuild against maven-doxia-sitetools 1.6.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.9.1-8
- Use Requires: java-headless rebuild (#1067528)

* Fri Feb 21 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.9.1-7
- Fix BR on plexus-interactivity

* Thu Feb 20 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.9.1-6
- Migrate to Wagon subpackages

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.9.1-5
- Fix unowned directory

* Mon Jan 27 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.9.1-4
- Remove dependency on maven2

* Fri Jan 17 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.9.1-3
- Update to current packaging guidelines
- Update to Maven 3.x

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jun 30 2013 Mat Booth <fedora@matbooth.co.uk> - 2.9.1-1
- Update to latest upstream, fixes rhbz #979577, works around CVE-2013-1571
- Remove dep on jakarta-commons-httpclient

* Wed Apr 10 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.9-6
- Remove test dependencies from POM

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 2.9-4
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Tue Jan  8 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.9-3
- Add missing requires
- Resolves: rhbz#893166

* Mon Nov 26 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.9-2
- Add LICENSE and NOTICE files to packages (#879605)
- Add dependency exclusion to make enforcer happy

* Tue Oct 23 2012 Alexander Kurtakov <akurtako@redhat.com> 2.9-1
- Update to latest upstream version.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jan 24 2012 Alexander Kurtakov <akurtako@redhat.com> 2.8.1-1
- Update to latest upstream version.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Dec 14 2011 Tomas Radej <tradej@redhat.com> - 2.8-4
- Added maven-compat dep to pom.xml

* Mon Dec 12 2011 Alexander Kurtakov <akurtako@redhat.com> 2.8-3
- Add BR on modello.

* Tue Dec 6 2011 Alexander Kurtakov <akurtako@redhat.com> 2.8-2
- FIx build in pure maven 3 environment.

* Wed May 11 2011 Alexander Kurtakov <akurtako@redhat.com> 2.8-1
- Update to latest upstream version.
- Guidelines fixes.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 24 2010 Alexander Kurtakov <akurtako@redhat.com> 2.7-3
- Add missing invoker requires.

* Wed Jul 21 2010 Alexander Kurtakov <akurtako@redhat.com> 2.7-2
- Add missing invoker BR.

* Wed Jul 21 2010 Alexander Kurtakov <akurtako@redhat.com> 2.7-1
- Update to 2.7.

* Fri May  7 2010 Mary Ellen Foster <mefoster at gmail.com> - 2.4-2
- Add jpackage-utils requirements
- Update requirements of javadoc subpackage

* Thu May  6 2010 Mary Ellen Foster <mefoster at gmail.com> - 2.4-1
- Initial version, based on akurtakov's initial spec

Name:           maven-resources-plugin
Version:        3.2.0
Release:        1%{?dist}
Summary:        Maven Resources Plugin
License:        ASL 2.0

URL:            https://maven.apache.org/plugins/maven-resources-plugin
Source0:        https://repo1.maven.org/maven2/org/apache/maven/plugins/%{name}/%{version}/%{name}-%{version}-source-release.zip

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.commons:commons-lang3)
BuildRequires:  mvn(org.apache.maven.plugin-testing:maven-plugin-testing-harness)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugins:pom:)
BuildRequires:  mvn(org.apache.maven.shared:maven-filtering) >= 3.2.0
BuildRequires:  mvn(org.apache.maven:maven-compat)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-model)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-annotations)
BuildRequires:  mvn(org.codehaus.plexus:plexus-interpolation)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.eclipse.aether:aether-api)
BuildRequires:  mvn(org.eclipse.sisu:org.eclipse.sisu.plexus)

%description
The Resources Plugin handles the copying of project resources
to the output directory.


%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
API documentation for %{name}.


%prep
%setup -q


%build
%mvn_build


%install
%mvn_install


%files -f .mfiles
%license LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%license LICENSE NOTICE


%changelog
* Tue Aug 11 2020 Fabio Valentini <decathorpe@gmail.com> - 3.2.0-1
- Update to version 3.2.0.

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 3.1.0-7
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 31 2018 Michael Simacek <msimacek@redhat.com> - 3.1.0-3
- Install license file

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 02 2018 Michael Simacek <msimacek@redhat.com> - 3.1.0-1
- Update to upstream version 3.1.0

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec  8 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.0.2-1
- Update to upstream version 3.0.2

* Mon Jun 13 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.0.1-1
- Update to upstream version 3.0.1

* Mon May  9 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.0.0-1
- Update to upstream version 3.0.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Oct 14 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.7-2
- Remove legacy Obsoletes/Provides for maven2 plugin

* Fri Oct  3 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.7-1
- Update to upstream version 2.7

* Mon Aug  4 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.6-9
- Fix build-requires on parent POM

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.6-7
- Use Requires: java-headless rebuild (#1067528)

* Mon Aug 12 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.6-6
- Update to current packaging guidelines

* Mon Aug 12 2013 Alexander Kurtakov <akurtako@redhat.com> 2.6-5
- Build using xmvn.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 2.6-2
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Tue Oct 23 2012 Alexander Kurtakov <akurtako@redhat.com> 2.6-1
- Update to latest upstream.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Sep 06 2011 Tomas Radej <tradej@redhat.com> - 2.5-4
- Fixed dependency on plexus-container-default

* Tue Aug 30 2011 Tomas Radej <tradej@redhat.com> - 2.5-3
- Added changelog

* Mon Aug 29 2011 Tomas Radej <tradej@redhat.com> - 2.5-1
- Update to 2.5
- Guideline fixes
- Added maven-filtering dep

* Thu Jun 23 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.4.3-4
- Add several packages to BR/R as stated in pom.xml

* Tue Jun 21 2011 Alexander Kurtakov <akurtako@redhat.com> 2.4.3-3
- Build with maven 3.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

*Thu Sep 09 2010 Pierre-Yves Chibon <pingou@pingoured.fr> - 2.4.3-1
- Update to 2.4.3

* Fri May 21 2010 Hui Wang <huwang@redhat.com> - 2.2-6
- delete duplicate maven2-plugin-jar
- delete source1

* Tue May 20 2010 Hui Wang <huwang@redhat.com> - 2.2-5
- Add maven-resources-plugin-demap.xml
- Set maven test ignore

* Wed May 19 2010 Hui Wang <huwang@redhat.com> - 2.2-4
- Add missing obsoletes/provides

* Wed May 19 2010 Hui Wang <huwang@redhat.com> - 2.2-3
- Add missing BR:maven-shared-reporting-impl

* Mon May 17 2010 Hui Wang <huwang@redhat.com> - 2.2-2
- Fixed install -pm 644 pom.xml

* Thu May 13 2010 Hui Wang <huwang@redhat.com> - 2.2-1
- Initial version of the package


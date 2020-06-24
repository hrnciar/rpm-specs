Name:           maven-source-plugin
Summary:        Plugin creating source JAR
Version:        3.2.1
Release:        1%{?dist}
License:        ASL 2.0

URL:            http://maven.apache.org/plugins/maven-source-plugin/
Source0:        https://repo1.maven.org/maven2/org/apache/maven/plugins/%{name}/%{version}/%{name}-%{version}-source-release.zip

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.maven:maven-archiver) >= 3.5.0
BuildRequires:  mvn(org.apache.maven:maven-compat)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-model)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugins:pom:)
BuildRequires:  mvn(org.apache.maven.plugin-testing:maven-plugin-testing-harness)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.codehaus.plexus:plexus-archiver) >= 4.2.0
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils) >= 3.3.0

%description
The Maven Source Plugin creates a JAR archive of the
source files of the current project.


%package        javadoc
Summary:        Javadoc for %{name}

%description    javadoc
API documentation for %{name}.


%prep
%setup -q


%build
%mvn_file : %{name}
%mvn_build


%install
%mvn_install


%files -f .mfiles
%license LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%license LICENSE NOTICE


%changelog
* Mon Mar 02 2020 Fabio Valentini <decathorpe@gmail.com> - 3.2.1-1
- Update to version 3.2.1.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Nov 03 2019 Fabio Valentini <decathorpe@gmail.com> - 3.2.0-1
- Update to version 3.2.0.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 29 2019 Fabio Valentini <decathorpe@gmail.com> - 3.1.0-1
- Update to version 3.1.0.

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jun 23 2016 Michael Simacek <msimacek@redhat.com> - 3.0.1-1
- Update to upstream version 3.0.1
- Enable tests

* Mon May 02 2016 Michael Simacek <msimacek@redhat.com> - 3.0.0-1
- Update to upstream version 3.0.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr 14 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.4-2
- Cleanup spec file

* Mon Jan 19 2015 Michael Simacek <msimacek@redhat.com> - 2.4-1
- Update to upstream version 2.4

* Tue Oct 14 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.3-2
- Remove legacy Obsoletes/Provides for maven2 plugin

* Sun Jul 20 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.3-1
- Update to upstream version 2.3

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.2.1-7
- Use Requires: java-headless rebuild (#1067528)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 2.2.1-4
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Wed Jan 16 2013 Michal Srb <msrb@redhat.com> - 2.2.1-3
- Build with xmvn

* Fri Nov 23 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2.1-2
- Install license files
- Resolves: rhbz#876837

* Tue Oct 23 2012 Alexander Kurtakov <akurtako@redhat.com> 2.2.1-1
- Update to latest upstream release.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jun 8 2011 Alexander Kurtakov <akurtako@redhat.com> 2.1.2-6
- Use upstream source.
- Build with maven 3.x.
- Guidelines fixes.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Sep 9 2010 Alexander Kurtakov <akurtako@redhat.com> 2.1.2-4
- Do not exclude plexus-container-default from dependencies.

* Fri May 28 2010 Alexander Kurtakov <akurtako@redhat.com> 2.1.2-3
- Add provides/obsoletes.

* Thu May 27 2010 Alexander Kurtakov <akurtako@redhat.com> 2.1.2-2
- Fix Url.
- More descriptive summary.
- Add missing BR.

* Thu May 27 2010 Alexander Kurtakov <akurtako@redhat.com> 2.1.2-1
- Initial package.


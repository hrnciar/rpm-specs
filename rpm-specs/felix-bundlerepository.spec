Name:           felix-bundlerepository
Version:        2.0.10
Release:        11%{?dist}
Summary:        Bundle repository service
License:        ASL 2.0 and MIT
URL:            https://felix.apache.org/documentation/subprojects/apache-felix-osgi-bundle-repository.html
BuildArch:      noarch

Source0:        https://archive.apache.org/dist/felix/org.apache.felix.bundlerepository-%{version}-source-release.tar.gz

Patch1:         0001-Unbundle-libraries.patch
Patch2:         0002-Compatibility-with-osgi-r6.patch

BuildRequires:  maven-local
BuildRequires:  mvn(net.sf.kxml:kxml2)
BuildRequires:  mvn(org.apache.felix:felix-parent:pom:)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.felix:org.apache.felix.gogo.runtime)
BuildRequires:  mvn(org.apache.felix:org.apache.felix.shell)
BuildRequires:  mvn(org.apache.felix:org.apache.felix.utils)
BuildRequires:  mvn(org.apache.felix:org.osgi.service.obr)
BuildRequires:  mvn(org.codehaus.woodstox:woodstox-core-asl)
BuildRequires:  mvn(org.easymock:easymock)
BuildRequires:  mvn(org.osgi:osgi.cmpn)
BuildRequires:  mvn(org.osgi:osgi.core)
BuildRequires:  mvn(xpp3:xpp3)
BuildRequires:  mvn(org.mockito:mockito-all)

%description
Bundle repository service

%package javadoc
Summary:          API documentation for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n org.apache.felix.bundlerepository-%{version}
%patch1 -p1
%patch2 -p1

%pom_remove_plugin :maven-source-plugin

# Unbundle xpp3
%pom_add_dep "xpp3:xpp3:1.1.3.4.O" pom.xml "<optional>true</optional>"

# Inject junit and mockito dep
%pom_add_dep junit:junit::test
%pom_add_dep org.mockito:mockito-all::test

# Make felix utils mandatory dep
%pom_xpath_remove "pom:dependency[pom:artifactId[text()='org.apache.felix.utils']]/pom:optional"

%pom_change_dep :easymock :::test

# Use latest OSGi implementation
%pom_change_dep :org.osgi.core org.osgi:osgi.core
%pom_change_dep :org.osgi.compendium org.osgi:osgi.cmpn

# For compatibility reasons
%mvn_file : felix/%{name}

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%license LICENSE LICENSE.kxml2 NOTICE
%doc DEPENDENCIES

%files javadoc -f .mfiles-javadoc
%license LICENSE LICENSE.kxml2 NOTICE

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.10-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 2.0.10-10
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Tue Apr 28 2020 Dinesh Prasanth M K <dmoluguw@redhat.com> - 2.0.10-9
- Inject junit and mockito dependecy for test

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 17 2019 Mat Booth <mat.booth@redhat.com> - 2.0.10-7
- Rebuild against OSGi R7 APIs

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu May 04 2017 Michael Simacek <msimacek@redhat.com> - 2.0.10-1
- Update to upstream version 2.0.10

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Oct 05 2016 Michael Simacek <msimacek@redhat.com> - 2.0.8-1
- Update to upstream version 2.0.8

* Thu Jun 16 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.6.6-20
- Regenerate build-requires
- Update to current packaging guidelines

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.6-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.6-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jul 30 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.6.6-17
- Fix build-requires on felix-parent

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.6-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Michal Srb <msrb@redhat.com> - 1.6.6-14
- Fix license tag. kxml is licensed under MIT, not BSD

* Tue Jul 09 2013 Michal Srb <msrb@redhat.com> - 1.6.6-13
- Make easymock and junit test-only dependencies

* Tue Jul 09 2013 Michal Srb <msrb@redhat.com> - 1.6.6-12
- Run some tests only contidionally
- Remove unneeded BR: mockito

* Wed Jul 03 2013 Michal Srb <msrb@redhat.com> - 1.6.6-11
- Build with XMvn
- Replace patches with %%pom_ macros
- Fix BR

* Wed Jul 03 2013 Michal Srb <msrb@redhat.com> - 1.6.6-10
- Fix BR (Resolves: #979500)

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.6.6-8
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon May 21 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.6.6-6
- Make felix-utils mandatory dep in pom.xml

* Mon Apr 30 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.6.6-5
- Unbundle libraries
- Add dependency on xpp3
- Include NOTICE in javadoc package
- Resolves #817581

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Oct 12 2011 Jaromir Capik <jcapik@redhat.com> - 1.6.6-3
- osgi.org groupId patch removed (fixed in felix-osgi-* packages)

* Thu Oct 06 2011 Jaromir Capik <jcapik@redhat.com> - 1.6.6-2
- Depmap removed (not needed anymore)
- woodstox-core-asl renamed to woodstox-core

* Tue Sep 14 2011 Jaromir Capik <jcapik@redhat.com> - 1.6.6-1
- Initial packaging

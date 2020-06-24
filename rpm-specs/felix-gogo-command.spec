%global bundle  org.apache.felix.gogo.command

Name:           felix-gogo-command
Version:        1.0.2
Release:        10%{?dist}
Summary:        Apache Felix Gogo command line shell for OSGi
License:        ASL 2.0
URL:            https://felix.apache.org/documentation/subprojects/apache-felix-gogo.html
BuildArch:      noarch

Source0:        https://repo1.maven.org/maven2/org/apache/felix/%{bundle}/%{version}/%{bundle}-%{version}-source-release.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.felix:gogo-parent:pom:)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.felix:org.apache.felix.gogo.runtime)
BuildRequires:  mvn(org.mockito:mockito-core)
BuildRequires:  mvn(org.osgi:osgi.cmpn)
BuildRequires:  mvn(org.osgi:osgi.core)
BuildRequires:  mvn(junit:junit)

%description
Apache Felix Gogo is a subproject of Apache Felix implementing a command
line shell for OSGi. It is used in many OSGi runtimes and servers.

This package implements a set of basic commands.

%package javadoc
Summary: Javadoc for %{name}

%description javadoc
This package contains API documentation for %{name}.

%prep
%setup -q -n %{bundle}-%{version}

%mvn_file : felix/%{bundle}

# Use provided scope because this is useful on OSGi frameworks other than Felix
%pom_change_dep :org.osgi.core :osgi.core::provided
%pom_change_dep :org.osgi.compendium :osgi.cmpn::provided

%pom_add_dep junit:junit::test

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%license LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%license LICENSE NOTICE

%changelog
* Tue Apr 28 2020 Dinesh Prasanth M K <dmoluguw@redhat.com> - 1.0.2-10
- Inject jUnit dependency

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Aug 18 2018 Mat Booth <mat.booth@redhat.com> - 1.0.2-6
- Fix install location as in the other felix packages

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 19 2017 Mat Booth <mat.booth@redhat.com> - 1.0.2-2
- Make dependencies on OSGi framework provided scope

* Fri May 05 2017 Michael Simacek <msimacek@redhat.com> - 1.0.2-1
- Update to upstream version 1.0.2

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Oct 07 2015 Mat Booth <mat.booth@redhat.com> - 0.16.0-2
- Remove unneeded hard dep on felix-bundlerepository

* Tue Oct 6 2015 Alexander Kurtakov <akurtako@redhat.com> 0.16.0-1
- Update to upstream 0.16.0 release.
- Drop no longer needed Java 7 compatibility patch.

* Mon Jun 29 2015 Mat Booth <mat.booth@redhat.com> - 0.14.0-5
- Drop incomplete and forbidden SCL macros

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Mar 30 2015 Mat Booth <mat.booth@redhat.com> - 0.14.0-3
- Avoid unnecessary runtime deps and re-generate build-deps

* Thu Jul 03 2014 Mat Booth <mat.booth@redhat.com> - 0.14.0-2
- BR/R: gogo-runtime >= 0.12.0

* Thu Jul 3 2014 Alexander Kurtakov <akurtako@redhat.com> 0.14.0-1
- Update to 0.14.0.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 16 2014 Alexander Kurtakov <akurtako@redhat.com> 0.12.0-10
- Start using mvn_build/install.

* Mon Aug 5 2013 Krzysztof Daniel <kdaniel@redhat.com> 0.12.0-9
- Fix FTBS.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Mar 15 2013 Krzysztof Daniel <kdaniel@redhat.com> 0.12.0-7
- Initial SCLization.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 0.12.0-5
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 27 2012 Krzysztof Daniel <kdaniel@redhat.com> 0.12.0-3
- Dependency to Java 7 added.
- Sources are patched to compile with OpenJDK 7.

* Tue Jan 10 2012 Krzysztof Daniel <kdaniel@redhat.com> 0.12.0-2
- description formatting removed
- jar_repack removed
- license added to the javadoc

* Tue Jan 10 2012 Krzysztof Daniel <kdaniel@redhat.com> 0.12.0-1
- Release 0.12.0

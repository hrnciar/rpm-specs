# Version 0.14.0 is available, but requires Java 9

Name:          maven-jaxb2-plugin
Version:       0.13.3
Release:       3%{?dist}
Summary:       Provides the capability to generate java sources from schemas
License:       BSD and ASL 2.0
URL:           https://github.com/highsource/%{name}
Source0:       %{url}/archive/%{version}.tar.gz
# Don't try to use an internal bundled resolver, as this is not available in
# Fedora:
Patch0:        %{name}-0.13.0-dont-use-internal-resolver.patch
# Adapt for Maven 3:
Patch1:        %{name}-0.13.0-adapt-for-maven-3.patch
# Remove the encoding option as the version of the XJC compiler that we build
# in Fedora doesn't have it:
Patch2:        %{name}-0.13.0-remove-encoding-option.patch

BuildArch:     noarch
BuildRequires: java-headless
BuildRequires: maven-local
BuildRequires: mvn(com.sun.codemodel:codemodel)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.commons:commons-lang3)
BuildRequires: mvn(org.apache.maven:maven-compat)
BuildRequires: mvn(org.apache.maven:maven-core)
BuildRequires: mvn(org.apache.maven:maven-plugin-api)
BuildRequires: mvn(org.apache.maven.plugin-testing:maven-plugin-testing-harness)
BuildRequires: mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires: mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires: mvn(org.codehaus.plexus:plexus-utils)
BuildRequires: mvn(org.glassfish.jaxb:jaxb-runtime)
BuildRequires: mvn(org.glassfish.jaxb:jaxb-xjc)
BuildRequires: mvn(org.slf4j:slf4j-api)
BuildRequires: mvn(org.sonatype.plexus:plexus-build-api)
BuildRequires: mvn(xml-resolver:xml-resolver)

%description
This Maven 2 plugin wraps the JAXB 2.x XJC compiler and provides the capability
to generate Java sources from XML Schemas.

Also see the jaxb2-maven-plugin package.

%package javadoc
Summary: API documentation for %{name}

%description javadoc
The API documentation of %{name}.

%prep
%autosetup -p1


# Remove parent
%pom_remove_parent

# use glassfish-jaxb = 2.0.5
%pom_disable_module plugin-2.0
# use glassfish-jaxb = 2.1.13
%pom_disable_module plugin-2.1

# Add dependency on codemodel:
# because org.glassfish.jaxb:codemodel:2.2.11 have missing classes use @ runtime by these plugins:
%pom_add_dep com.sun.codemodel:codemodel:2.6 plugin
%pom_add_dep com.sun.codemodel:codemodel:2.6 plugin-2.2

# rename java files with everything commented out, helpmojo can't handle those:
cd plugin-core/src/main/java/org/jvnet/jaxb2/maven2/resolver/tools/
mv DelegatingReaderWrapper.java DelegatingReaderWrapper.java_
mv DelegatingInputStreamWrapper.java DelegatingInputStreamWrapper.java_


%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.md
%license LICENSE

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
* Mon Jun 08 2020 Fabio Valentini <decathorpe@gmail.com> - 0.13.3-3
- Remove unnecessary BuildRequires on maven-release-plugin.

* Wed May 27 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.13.3-2
- Use new upstream github repo url.

* Sat May 23 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.13.3-1
- Update as per review comments
- Correct typo in patch
- Remove deprecated parent pom
- Remove subshell
- Add note about related package

* Sun May 17 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.13.3-1
- Unretire
- Update to latest release
- Use autosetup

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Karsten Hopp <karsten@redhat.com> - 0.13.0-5
- helpmojo can't handle java file where everything is commented out
  mv them out of the way


* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Oct 26 2015 gil cattaneo <puntogil@libero.it> 0.13.0-1
- Update to 0.13.0

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Feb 11 2015 gil cattaneo <puntogil@libero.it> 0.12.3-1
- Update to 0.12.3
- introduce license macro

* Tue Jan 20 2015 gil cattaneo <puntogil@libero.it> 0.9.1-3
- rebuilt rhbz#1068387

* Tue Jan 20 2015 gil cattaneo <puntogil@libero.it> 0.9.1-2
- rebuilt rhbz#1068387

* Tue Jan 20 2015 gil cattaneo <puntogil@libero.it> 0.9.1-1
- Update to 0.9.1

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 0.8.1-12
- Use Requires: java-headless rebuild (#1067528)

* Mon Aug 05 2013 gil cattaneo <puntogil@libero.it> 0.8.1-11
- rebuilt rhbz#992193
- swith to Xmvn
- adapt to new guideline

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 0.8.1-8
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Tue Jul 24 2012 Juan Hernandez <juan.hernandez@redhat.com> - 0.8.1-7
- Added maven-enforcer-plugin build time dependency

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Mar 12 2012 Juan Hernandez <juan.hernandez@redhat.com> 0.8.1-5
- Added maven-anno-plugin to the runtime requirements

* Mon Mar 12 2012 Juan Hernandez <juan.hernandez@redhat.com> 0.8.1-4
- Fixed the license header as some files use ASL 2.0
- Changed the URL to a more reliable one

* Fri Mar 9 2012 Juan Hernandez <juan.hernandez@redhat.com> 0.8.1-3
- Added maven-surefire-provider-junit4 to the build requirements

* Wed Feb 22 2012 Juan Hernandez <juan.hernandez@redhat.com> 0.8.1-2
- Cleanup of the spec file

* Sat Jan 21 2012 Marek Goldmann <mgoldman@redhat.com> 0.8.1-2
- Initial packaging

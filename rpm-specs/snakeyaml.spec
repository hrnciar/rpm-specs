%global vertag e91772b1bc0b

%bcond_with spring

Name:           snakeyaml
Summary:        YAML parser and emitter for Java
Version:        1.26
Release:        2%{?dist}
License:        ASL 2.0

URL:            https://bitbucket.org/asomov/%{name}
Source0:        %{url}/get/%{name}-%{version}.tar.gz

# Upstream has forked gdata-java and base64 and refuses [1] to
# consider replacing them by external dependencies.  Bundled libraries
# need to be removed and their use replaced by system libraries.
# See rhbz#875777 and http://code.google.com/p/snakeyaml/issues/detail?id=175
#
# Replace use of bundled Base64 implementation with java.util.Base64
Patch0:         0001-replace-bundled-base64coder-with-java.util.Base64.patch
# We don't have gdata-java in Fedora any longer, use commons-codec instead
Patch1:         0002-Replace-bundled-gdata-java-client-classes-with-commo.patch

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(commons-codec:commons-codec)
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.commons:commons-lang3)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.apache.velocity:velocity)
%if %{with spring}
BuildRequires:  mvn(org.springframework:spring-core)
BuildRequires:  mvn(org.springframework:spring-beans)
BuildRequires:  mvn(org.springframework:spring-context-support)
%endif

%description
SnakeYAML features:
    * a complete YAML 1.1 parser. In particular,
      SnakeYAML can parse all examples from the specification.
    * Unicode support including UTF-8/UTF-16 input/output.
    * high-level API for serializing and deserializing
      native Java objects.
    * support for all types from the YAML types repository.
    * relatively sensible error messages.


%package        javadoc
Summary:        API documentation for %{name}

%description    javadoc
This package contains %{summary}.


%prep
%setup -q -n asomov-%{name}-%{vertag}
%patch0 -p1
%patch1 -p1

%mvn_file : %{name}

%pom_remove_plugin :cobertura-maven-plugin
%pom_remove_plugin :maven-changes-plugin
%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :maven-license-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-site-plugin
%pom_remove_plugin :nexus-staging-maven-plugin

sed -i "/<artifactId>spring</s/spring/&-core/" pom.xml
rm -f src/test/java/examples/SpringTest.java

# Replacement for bundled gdata-java-client
%pom_add_dep commons-codec:commons-codec

# Unnecessary test-time only dependency
%pom_remove_dep joda-time:joda-time
rm -rf src/test/java/examples/jodatime

# remove bundled stuff
rm -rf target

# fails in rpmbuild only due to different locale
rm src/test/java/org/yaml/snakeyaml/issues/issue67/NonAsciiCharsInClassNameTest.java
# fails after unbundling
rm src/test/java/org/yaml/snakeyaml/issues/issue318/ContextClassLoaderTest.java

# convert CR+LF to LF
sed -i 's/\r//g' LICENSE.txt

%if %{without spring}
%pom_remove_dep org.springframework
rm -r src/test/java/org/yaml/snakeyaml/issues/issue9
rm src/test/java/org/yaml/snakeyaml/helpers/FileTestHelper.java
%endif


%build
%mvn_build


%install
%mvn_install


%files -f .mfiles
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt


%changelog
* Wed May 06 2020 Mat Booth <mat.booth@redhat.com> - 1.26-2
- Drop unnecessary dep on joda-time

* Wed Apr 15 2020 Severin Gehwolf <sgehwolf@redhat.com> - 1.26-1
- Update to latest upstream 1.26 release.
- Resolves: CVE-2017-18640

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.25-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 15 2019 Fabio Valentini <decathorpe@gmail.com> - 1.25-3
- Replace base64coder dependency with java.util.Base64 from JDK8.

* Tue Oct 15 2019 Fabio Valentini <decathorpe@gmail.com> - 1.25-2
- Backport fix for a broken test from upstream.

* Thu Aug 22 2019 Fabio Valentini <decathorpe@gmail.com> - 1.25-1
- Update to version 1.25.

* Sun Jul 28 2019 Fabio Valentini <decathorpe@gmail.com> - 1.17-9
- Disable support for spring.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.17-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.17-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.17-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.17-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 02 2017 Michael Simacek <msimacek@redhat.com> - 1.17-2
- Add conditional for spring

* Mon Oct 17 2016 Michael Simacek <msimacek@redhat.com> - 1.17-1
- Update to upstream version 1.17

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Sep 28 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.16-1
- Update to upstream version 1.16

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.13-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr 21 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.13-8
- Remove maven-javadoc-plugin from POM

* Tue Mar 31 2015 Michael Simacek <msimacek@redhat.com> - 1.13-7
- Remove BR on maven-changes-plugin

* Wed Mar 25 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.13-6
- Remove build dependency on cobertura

* Wed Mar 11 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.13-5
- Add BR on objectweb-asm3

* Wed Jan 21 2015 Mat Booth <mat.booth@redhat.com> - 1.13-4
- Add missing BR on maven-site-plugin

* Mon Jun 16 2014 Michal Srb <msrb@redhat.com> - 1.13-3
- Fix FTBFS

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Sep 30 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.13-1
- Update to upstream version 1.13

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 21 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.11-6
- Update to current packaging guidelines

* Fri Apr 26 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.11-5
- Explain gdata-java and base64 bundling situation
- Resolves: rhbz#875777

* Mon Apr 22 2013 Michal Srb <msrb@redhat.com> - 1.11-5
- Replace bundled base64 implementation
- Replace bundled gdata-java-client classes with apache-commons-codec

* Wed Apr 10 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.11-4
- Conditionally disable tests
- Conditionally remove test dependencies from POM

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.11-2
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Mon Oct 15 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.11-1
- Update to upstream version 1.11

* Mon Oct 15 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.9-3
- Remove unneeded dependencies: base64coder, gdata-java
- Convert pom.xml patch to POM macro

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 20 2012 Mo Morsi <mmorsi@redhat.com> - 1.9-1
- Update to latest upstream release
- patch2, patch3 no longer needed
- update to latest fedora java guidelines

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jun 20 2011 Jaromir Capik <jcapik@redhat.com> - 1.8-6
- Patch for the issue67 test removed

* Fri Jun 17 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.8-5
- Add osgi metadata to jar file (#713935)

* Thu Jun 09 2011 Jaromir Capik <jcapik@redhat.com> - 1.8-4
- File handle leaks patched

* Tue Jun 07 2011 Jaromir Capik <jcapik@redhat.com> - 1.8-3
- base64coder-java renamed to base64coder

* Wed Jun 01 2011 Jaromir Capik <jcapik@redhat.com> - 1.8-2
- Bundled stuff removal

* Mon May 16 2011 Jaromir Capik <jcapik@redhat.com> - 1.8-1
- Initial version of the package


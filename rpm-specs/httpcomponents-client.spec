%bcond_with        memcached
%bcond_with        ehcache

Name:              httpcomponents-client
Summary:           HTTP agent implementation based on httpcomponents HttpCore
Version:           4.5.10
Release:           2%{?dist}
License:           ASL 2.0
URL:               http://hc.apache.org/
Source0:           http://www.apache.org/dist/httpcomponents/httpclient/source/%{name}-%{version}-src.tar.gz

Patch0:            0001-Use-system-copy-of-effective_tld_names.dat.patch
Patch1:            0002-Port-to-mockito-2.patch

BuildArch:         noarch

BuildRequires:     maven-local
BuildRequires:     mvn(commons-codec:commons-codec)
BuildRequires:     mvn(commons-logging:commons-logging)
BuildRequires:     mvn(junit:junit)
%if %{with ehcache}
BuildRequires:     mvn(net.sf.ehcache:ehcache-core)
%endif
%if %{with memcached}
BuildRequires:     mvn(net.spy:spymemcached)
%endif
BuildRequires:     mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:     mvn(org.apache.httpcomponents:httpcomponents-parent:pom:)
BuildRequires:     mvn(org.apache.httpcomponents:httpcore)
BuildRequires:     mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:     mvn(org.mockito:mockito-core)

BuildRequires:     publicsuffix-list
Requires:          publicsuffix-list

Obsoletes:         %{name}-tests < 4.4

%description
HttpClient is a HTTP/1.1 compliant HTTP agent implementation based on
httpcomponents HttpCore. It also provides reusable components for
client-side authentication, HTTP state management, and HTTP connection
management. HttpComponents Client is a successor of and replacement
for Commons HttpClient 3.x. Users of Commons HttpClient are strongly
encouraged to upgrade.

%package        cache
Summary:        Cache module for %{name}

%description    cache
This package provides client side caching for %{name}.

%package        javadoc
Summary:        API documentation for %{name}

%description    javadoc
%{summary}.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1
%patch1 -p1

%mvn_package :::tests: __noinstall
%mvn_package :httpclient-cache cache

# Remove optional build deps not available in Fedora
%pom_disable_module httpclient-osgi
%pom_disable_module httpclient-win
%pom_remove_plugin :docbkx-maven-plugin
%pom_remove_plugin :clirr-maven-plugin
%pom_remove_plugin :maven-checkstyle-plugin
%pom_remove_plugin :apache-rat-plugin
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :animal-sniffer-maven-plugin

# Fails due to strict crypto policy - uses DSA in test data
rm httpclient/src/test/java/org/apache/http/conn/ssl/TestSSLSocketFactory.java

# Don't compile/run httpclient-cache tests - they are incompatible with EasyMock 3.3
%pom_remove_dep org.easymock:easymockclassextension
%pom_remove_dep org.slf4j:slf4j-jcl httpclient-cache
%pom_remove_dep :::test httpclient-cache
rm -rf httpclient-cache/src/test

%pom_remove_plugin :download-maven-plugin httpclient

%pom_xpath_inject "pom:archive" "
    <manifestFile>\${project.build.outputDirectory}/META-INF/MANIFEST.MF</manifestFile>"

%pom_xpath_inject pom:build/pom:plugins "
    <plugin>
      <groupId>org.apache.felix</groupId>
      <artifactId>maven-bundle-plugin</artifactId>
      <executions>
        <execution>
          <id>bundle-manifest</id>
          <phase>process-classes</phase>
          <goals>
            <goal>manifest</goal>
          </goals>
        </execution>
      </executions>
    </plugin>"

%pom_xpath_inject pom:build "
<pluginManagement>
  <plugins>
    <plugin>
      <groupId>org.apache.felix</groupId>
      <artifactId>maven-bundle-plugin</artifactId>
      <configuration>
        <instructions>
          <Export-Package>org.apache.http.*,!org.apache.http.param</Export-Package>
          <Private-Package></Private-Package>
          <_nouses>true</_nouses>
          <Import-Package>!org.apache.avalon.framework.logger,!org.apache.log,!org.apache.log4j,*</Import-Package>
        </instructions>
        <excludeDependencies>true</excludeDependencies>
      </configuration>
    </plugin>
  </plugins>
</pluginManagement>
" httpclient

%pom_xpath_inject pom:build "
<pluginManagement>
  <plugins>
    <plugin>
      <groupId>org.apache.felix</groupId>
      <artifactId>maven-bundle-plugin</artifactId>
      <extensions>true</extensions>
      <configuration>
        <instructions>
          <Export-Package>*</Export-Package>
          <Import-Package>net.sf.ehcache;resolution:=optional,net.spy.memcached;resolution:=optional,*</Import-Package>
          <Private-Package></Private-Package>
          <_nouses>true</_nouses>
        </instructions>
        <excludeDependencies>true</excludeDependencies>
      </configuration>
    </plugin>
  </plugins>
</pluginManagement>" httpclient-cache

# requires network
rm httpclient/src/test/java/org/apache/http/client/config/TestRequestConfig.java

%if %{without memcached}
rm -r httpclient-cache/src/*/java/org/apache/http/impl/client/cache/memcached
%pom_remove_dep :spymemcached httpclient-cache
%endif
%if %{without ehcache}
rm -r httpclient-cache/src/*/java/org/apache/http/impl/client/cache/ehcache
%pom_remove_dep :ehcache-core httpclient-cache
%endif

%build
%mvn_file ":{*}" httpcomponents/@1

%mvn_build

%install
%mvn_install


%files -f .mfiles
%doc LICENSE.txt NOTICE.txt README.txt RELEASE_NOTES.txt

%files cache -f .mfiles-cache

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 16 2019 Marian Koncek <mkoncek@redhat.com> - 4.5.10-1
- Update to upstream version 4.5.10

* Thu Aug 29 2019 Fabio Valentini <decathorpe@gmail.com> - 4.5.7-3
- Disable memcached and ehcache support.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb 04 2019 Marian Koncek <mkoncek@redhat.com> - 4.5.7-1
- Update to upstream version 4.5.7
- Fixes: RHBZ #1669148

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Dec 07 2018 Mat Booth <mat.booth@redhat.com> - 4.5.6-2
- Add a patch to allow building with mockito 2
- Don't package tests jars, the tests jars have the same OSGi metadata as the
  main jars, which can cause tycho to resolve the wrong one when building
  eclipse plugins

* Mon Oct  8 2018 Mikolaj Izdebski <mizdebsk@redhat.com> - 4.5.6-1
- Update to upstream version 4.5.6

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 19 2018 Michael Simacek <msimacek@redhat.com> - 4.5.5-4
- Fix FTBFS (weak crypto in test data)

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 4.5.5-3
- Escape macros in %%changelog

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 22 2018 Michael Simacek <msimacek@redhat.com> - 4.5.5-1
- Update to upstream version 4.5.5

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 02 2017 Michael Simacek <msimacek@redhat.com> - 4.5.3-2
- Add conditionals for memcached and ehcache

* Thu Jan 26 2017 Michael Simacek <msimacek@redhat.com> - 4.5.3-1
- Update to upstream version 4.5.3

* Fri Jun 24 2016 Michael Simacek <msimacek@redhat.com> - 4.5.2-4
- Fix build with httpcomponents-core-4.4.5

* Wed Jun 15 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 4.5.2-3
- Add missing build-requires

* Wed Mar 16 2016 Sopot Cela <scela@redhat.com> - 4.5.2-2
- Make the fluent API into a bundle

* Mon Feb 29 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 4.5.2-1
- Update to upstream version 4.5.2

* Wed Feb 10 2016 Mat Booth <mat.booth@redhat.com> - 4.5.1-4
- Enable the fluent API module

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 25 2016 Mat Booth <mat.booth@redhat.com> - 4.5.1-2
- Make client cache jar into a OSGi bundle

* Wed Sep 16 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 4.5.1-1
- Update to upstream version 4.5.1

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 04 2015 Michael Simacek <msimacek@redhat.com> - 4.5-1
- Update to upstream version 4.5

* Tue Mar 31 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 4.4.1-1
- Update to upstream version 4.4.1

* Wed Feb 18 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 4.4-1
- Update to upstream version 4.4

* Thu Jan 22 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 4.4-0.3.beta1
- Split httpclient-cache into subpackage

* Tue Jan 20 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 4.4-0.2.beta1
- Unbundle publicsuffix-list
- Resolves: rhbz#1183782

* Mon Jan 19 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 4.4-0.1.beta1
- Update to upstream version 4.4 beta1
- Remove tests subpackage

* Fri Jan  9 2015 Richard Fearn <richardfearn@gmail.com> - 4.3.5-3
- Also build HttpClient Cache (bug #1180696)

* Tue Dec 02 2014 Michael Simacek <msimacek@redhat.com> - 4.3.5-2
- Build and install tests artifact (needed by copr-java)

* Tue Aug  5 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 4.3.5-1
- Update to upstream version 4.3.5

* Mon Aug  4 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 4.3.4-2
- Fix build-requires on httpcomponents-project

* Fri Jun  6 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 4.3.4-1
- Update to upstream version 4.3.4

* Fri Feb 28 2014 Michael Simacek <msimacek@redhat.com> - 4.3.3-1
- Update to upstream version 4.3.3

* Mon Jan 20 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 4.3.2-1
- Update to upstream version 4.3.2

* Mon Jan 06 2014 Michael Simacek <msimacek@redhat.com> - 4.3.1-1
- Update to upstream version 4.3.1
- Temporarily disable tests due to bug in mockito

* Thu Oct  3 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 4.3-2
- Don't try to remove maven-notice-plugin from POM

* Fri Sep 13 2013 Michal Srb <msrb@redhat.com> - 4.3-1
- Update to upstream version 4.3
- Drop group tag

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jun 10 2013 Michal Srb <msrb@redhat.com> - 4.2.5-2
- Enable tests on Fedora

* Thu Apr 25 2013 Michal Srb <msrb@redhat.com> - 4.2.5-1
- Update to upstream version 4.2.5

* Thu Apr 11 2013 Michal Srb <msrb@redhat.com> - 4.2.4-1
- Update to upstream version 4.2.4

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 4.2.3-3
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Fri Jan 25 2013 Michal Srb <msrb@redhat.com> - 4.2.3-2
- Build with xmvn
- Disable fluent-hc module

* Thu Jan 24 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 4.2.3-1
- Update to upstream version 4.2.3

* Thu Oct 25 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 4.2.2-1
- Update to upstream version 4.2.2

* Wed Aug  1 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 4.2.1-3
- Fix OSGi manifest in httpmime

* Fri Jul 27 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 4.2.1-2
- Install NOTICE.txt file
- Fix javadir directory ownership
- Fix directory permissions
- Preserve timestamps
- Replace add_to_maven_depmap with add_maven_depmap

* Fri Jul 27 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 4.2.1-1
- Update to upstream version 4.2.1
- Convert patches to POM macros

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed May 2 2012 Alexander Kurtakov <akurtako@redhat.com> 4.1.3-3
- Do not export org.apache.http.param in osgi.

* Mon Mar 26 2012 Alexander Kurtakov <akurtako@redhat.com> 4.1.3-2
- Do not export * but only org.apache.http.* .
- Do not generate uses clauses in the manifest.

* Thu Mar  1 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> 4.1.3-1
- Update to latest upstream bugfix

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Aug 16 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 4.1.2-1
- Update to latest upstream (4.1.2)
- Minor tweaks according to guidelines

* Fri Jul 15 2011 Severin Gehwolf <sgehwolf@redhat.com> 4.1.1-3
- Fix for RH Bz#718830. Add instructions so as to not
  Import-Package optional dependencies.

* Thu Apr 7 2011 Severin Gehwolf <sgehwolf@redhat.com> 4.1.1-2
- Add BR/R apache-commons-codec, since httpcomponents-client's
  MANIFEST.MF has an Import-Package: org.apache.commons.codec
  header.

* Tue Mar 29 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 4.1.1-1
- New upstream bugfix version (4.1.1)

* Tue Mar 15 2011 Severin Gehwolf <sgehwolf@redhat.com> 4.1-6
- Explicitly set PrivatePackage to the empty set, so as to
  export all packages.

* Thu Mar 10 2011 Alexander Kurtakov <akurtako@redhat.com> 4.1-5
- OSGi export more packages.

* Fri Feb 25 2011 Alexander Kurtakov <akurtako@redhat.com> 4.1-4
- Build httpmime module.

* Fri Feb 18 2011 Alexander Kurtakov <akurtako@redhat.com> 4.1-3
- Don't use basename as an identifier.

* Fri Feb 18 2011 Alexander Kurtakov <akurtako@redhat.com> 4.1-2
- OSGify properly.
- Install into %%{_javadir}/%%{basename}.

* Thu Feb 17 2011 Alexander Kurtakov <akurtako@redhat.com> 4.1-1
- Update to latest upstream version.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 22 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 4.0.3-2
- Added license to javadoc subpackage

* Mon Dec 20 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 4.0.3-1
- Initial version

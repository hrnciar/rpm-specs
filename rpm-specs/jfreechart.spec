Name:           jfreechart
Version:        1.0.19
Release:        13%{?dist}
Summary:        Java chart library

License:        LGPLv2+
URL:            http://www.jfree.org/jfreechart/
Source0:        http://download.sourceforge.net/sourceforge/jfreechart/%{name}-%{version}.zip
Patch0:         build_swt_encoding_fix.patch

BuildRequires:  maven-local
BuildRequires:  maven-plugin-bundle
BuildRequires:  mvn(org.jfree:jcommon) >= 1.0.23
BuildRequires:  mvn(javax.servlet:javax.servlet-api) >= 2.5
%if 0%{?fedora}
BuildRequires:  eclipse-swt
%endif
BuildRequires:  sonatype-oss-parent
BuildRequires:  ant

BuildArch:      noarch

%description
JFreeChart is a free 100% Java chart library that makes it easy for
developers to display professional quality charts in their applications.

%if 0%{?fedora}
%package swt
Summary:        Swt extension for jfreechart
Requires:       %{name} = %{version}-%{release}
Requires:       eclipse-swt jpackage-utils

%description swt
Experimental swt extension for jfreechart.
%endif

%package javadoc
Summary:        Javadocs for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       jpackage-utils

%description javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q
# Erase prebuilt files
find \( -name '*.jar' -o -name '*.class' \) -exec rm -f '{}' \;
%patch0 -p2

MVN_BUNDLE_PLUGIN_EXTRA_XML="<extensions>true</extensions>
        <configuration>
          <instructions>
            <Bundle-SymbolicName>org.jfree.jfreechart</Bundle-SymbolicName>
            <Bundle-Vendor>Fedora Project</Bundle-Vendor>
            <Bundle-Version>%{version}</Bundle-Version>
            <!-- Do not autogenerate uses clauses in Manifests -->
            <Import-Package>
              !javax.servlet,
              !javax.servlet.http,
              *
            </Import-Package>
            <_nouses>true</_nouses>
          </instructions>
        </configuration>"
%pom_remove_plugin :maven-gpg-plugin
%pom_remove_plugin :nexus-staging-maven-plugin
%pom_remove_plugin :cobertura-maven-plugin
%pom_remove_plugin :maven-site-plugin
%pom_remove_plugin :animal-sniffer-maven-plugin
%pom_remove_plugin :maven-jxr-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_change_dep javax.servlet:servlet-api: javax.servlet:javax.servlet-api:

%pom_add_plugin org.apache.felix:maven-bundle-plugin . "$MVN_BUNDLE_PLUGIN_EXTRA_XML"
%pom_add_plugin org.apache.maven.plugins:maven-javadoc-plugin . "<configuration><excludePackageNames>org.jfree.chart.fx*</excludePackageNames></configuration>"
# Change to packaging type bundle so as to be able to use it
# as an OSGi bundle.
%pom_xpath_set "pom:packaging" "bundle"

%build
# Ignore failing test: SegmentedTimelineTest
%mvn_build -- -Dmaven.test.failure.ignore=true

%if 0%{?fedora}
# /usr/lib/java/swt.jar is an arch independent path to swt
ant -f ant/build-swt.xml \
        -Dswt.jar=/usr/lib/java/swt.jar \
        -Djcommon.jar=$(build-classpath jcommon) \
        -Djfreechart.jar=target/jfreechart-%{version}.jar
%endif

%install
%mvn_install

%if 0%{?fedora}
install -m 644 lib/swtgraphics2d.jar  $RPM_BUILD_ROOT%{_javadir}/%{name}/swtgraphics2d.jar
install -m 644 lib/jfreechart-%{version}-swt.jar  $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-swt.jar
%endif

%files -f .mfiles
%doc ChangeLog NEWS README.txt

%if 0%{?fedora}
%files swt
%{_javadir}/%{name}/swtgraphics2d*.jar
%{_javadir}/%{name}/%{name}-swt*.jar
%endif

%files javadoc -f .mfiles-javadoc

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.19-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.19-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.19-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.19-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.19-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jul 28 2017 Severin Gehwolf <sgehwolf@redhat.com> - 1.0.19-8
- Fix FTBFS, by changing servlet API BRs so as to pull in
  glassfish-servlet-api which provides correct maven artifacts.

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.19-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.19-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Merlin Mathesius <mmathesi@redhat.com> - 1.0.19-5
- Add missing BuildRequires to fix FTBFS (BZ#1406128).

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.19-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Sep 04 2014 Severin Gehwolf <sgehwolf@redhat.com> 1.0.19-2
- Don't Import-Package javax.servlet*

* Tue Sep 02 2014 Severin Gehwolf <sgehwolf@redhat.com> 1.0.19-1
- Update to upstream 1.0.19 release.
- Switch to building with xmvn where possible (swt sub-package
  still uses ant).

* Tue Jun 10 2014 Severin Gehwolf <sgehwolf@redhat.com> 1.0.14-12
- Fix FTBFS. Resolves RHBZ#1106941

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.14-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.14-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Feb 19 2013 Severin Gehwolf <sgehwolf@redhat.com> 1.0.14-9
- Fix FTBFS due to build-classpath not finding swt.jar any
  longer. See RHBZ#912664.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.14-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Nov 21 2012 Severin Gehwolf <sgehwolf@redhat.com> 1.0.14-7
- Remove itext dependency in pom.

* Fri Nov 16 2012 Severin Gehwolf <sgehwolf@redhat.com> 1.0.14-6
- Conditionally build jfreechart-swt.

* Mon Sep 17 2012 Severin Gehwolf <sgehwolf@redhat.com> 1.0.14-4
- Set proper Bundle-{Version,SymbolicName,Name} in manifest.

* Tue Jul 24 2012 Severin Gehwolf <sgehwolf@redhat.com> 1.0.14-3
- Add aqute bnd instructions so as to produce OSGi metadata.
- Based on kdaniel's suggestion, use build-classpath script to find swt

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Apr 23 2012 Alexander Kurtakov <akurtako@redhat.com> 1.0.14-1
- Update to new upstream version 1.0.14.
- Use pom.xml file from the tarball.

* Wed Feb 15 2012 Marek Goldmann <mgoldman@redhat.com> 1.0.13-5
- Added Maven POM: BZ#789586

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jun 29 2011 Alexander Kurtakov <akurtako@redhat.com> 1.0.13-3
- Adapt to current guidelines.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Apr 19 2010 Lubomir Rintel <lkundrak@v3.sk> - 1.0.13-1
- Update to a later release
- Cosmetic fixes

* Mon Apr 19 2010 Lubomir Rintel <lkundrak@v3.sk> - 1.0.10-4
- Enable SWT support (ELMORABITY Mohamed, #583339)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Jul 19 2008 Lubomir Rintel (Fedora Astronomy) <lkundrak@fedoraproject.org> - 1.0.10-1
- Initial packaging

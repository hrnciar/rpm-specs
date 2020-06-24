# Conditionally build with a minimal dependency set
%bcond_with jp_minimal

Name:           freemarker
Version:        2.3.29
Release:        4%{?dist}
Summary:        The Apache FreeMarker Template Engine
License:        ASL 2.0
URL:            https://freemarker.apache.org/
Source0:        https://github.com/apache/freemarker/archive/v%{version}/%{name}-%{version}.tar.gz

# Remove JSP 2.0 API usage
Patch1:         jsp-api.patch
# Compile only the classes compatible with the version of jython
Patch2:         jython-compatibility.patch
# illegal character in the javadoc comment
Patch3:         fix-javadoc-encoding.patch
# Disable JRebel integration, it is not free software and not in Fedora
Patch5:         no-javarebel.patch
# enable jdom extension
Patch6:         enable-jdom.patch
# Fix compatibility with javacc 7
Patch7:         javacc-7.patch

BuildArch:      noarch

BuildRequires: ant
BuildRequires: apache-parent
BuildRequires: apache-commons-logging
BuildRequires: aqute-bnd
BuildRequires: hamcrest
BuildRequires: ivy-local
BuildRequires: glassfish-jsp-api
BuildRequires: glassfish-servlet-api
BuildRequires: javacc >= 7.0
BuildRequires: jaxen >= 1.1
BuildRequires: jcl-over-slf4j
BuildRequires: jdom >= 1.0
BuildRequires: junit
BuildRequires: log4j-over-slf4j
BuildRequires: slf4j
BuildRequires: xalan-j2 >= 2.7.0

%if %{without jp_minimal}
BuildRequires: dom4j
BuildRequires: saxpath
BuildRequires: jython
BuildRequires: rhino >= 1.6
%endif

%description
Apache FreeMarker is a template engine: a Java library to generate text output
(HTML web pages, e-mails, configuration files, source code, etc.) based on
templates and changing data. Templates are written in the FreeMarker Template
Language (FTL), which is a simple, specialized language (not a full-blown
programming language like PHP).

%package javadoc
Summary: Javadoc for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q

find -type f -name "*.jar" -delete
find -type f -name "*.class" -delete

%patch1
%patch2
%patch3
%patch5
%patch6
%patch7 -p1

# Use system ivy settings
rm ivysettings.xml

# Correct classpath for Javadoc generation
sed -i 's/cachepath conf="IDE"/cachepath conf="javadoc"/' build.xml
sed -i '/conf name="IDE"/i<conf name="javadoc" extends="build.jython2.5,build.jsp2.1" />' ivy.xml

# Disable Java 8 javadoc linting
sed -i '/<javadoc/a\ additionalparam="-Xdoclint:none" encoding="UTF-8"' build.xml

# Drop unnecessary dep on avalon
sed -i -e '/avalon-logkit/d' ivy.xml
rm src/main/java/freemarker/log/_AvalonLoggerFactory.java

%if %{with jp_minimal}
# Drop dep on optional extra deps for minimal build
sed -i -e '/"rhino"/d' -e '/"jython"/d' ivy.xml
rm -rf src/main/java/freemarker/ext/{rhino,jython,ant}
rm src/main/java/freemarker/template/utility/JythonRuntime.java
# Drop dep on additional xml backends for minimal build
sed -i -e '/dom4j/d' -e '/saxpath/d' ivy.xml
rm src/main/java/freemarker/ext/xml/_Dom4jNavigator.java
%endif

%mvn_file org.%{name}:%{name} %{name}

%build
export LANG=C.UTF-8
ant -Divy.mode=local -Ddeps.available=true javacc jar javadoc maven-pom

%install
export LANG=C.UTF-8
%mvn_artifact build/pom.xml build/%{name}.jar
%mvn_install -J build/api

%files -f .mfiles
%doc README.md RELEASE-NOTES
%license LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%license LICENSE NOTICE

%changelog
* Wed Apr 01 2020 Mat Booth <mat.booth@redhat.com> - 2.3.29-4
- Rebuild for rawhide

* Tue Mar 24 2020 Mat Booth <mat.booth@redhat.com> - 2.3.29-3
- Fix source encoding for javadoc generation

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.29-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct 23 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.29-1
- Update to version 2.3.29.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.28-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat May 11 2019 Mat Booth <mat.booth@redhat.com> - 2.3.28-3
- Allow conditionally building with a reduced dependency set

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Aug 22 2018 Mat Booth <mat.booth@redhat.com> - 2.3.28-1
- Update to latest upstream release
- Drop unnecessary dep on saxpath and avalon

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.27-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Dec 06 2017 Mat Booth <mat.booth@redhat.com> - 2.3.27-1
- Update to latest release, project moved to the Apache Foundation
- Drop unnecessary dep on findbugs
- Build against glassfish instead of jboss

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.23-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Apr 04 2017 Michael Simacek <msimacek@redhat.com> - 2.3.23-4
- Fix compatibility with javacc 7

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.23-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 06 2016 Omair Majid <omajid@redhat.com> - 2.3.23-1
- Update to 2.3.23

* Thu Jul 02 2015 gil cattaneo <puntogil@libero.it> 2.3.19-11
- fix FTBFS
- adapt to current guideline
- fix some rpmlint problems
- enable javadoc task
- enable maven-upload task for generate pom file
- Fix paths to jython

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.19-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 09 2014 Omair Majid <omajid@redhat.com> - 2.3.19-9
- Use .mfiles to pick up xmvn metadata
- Don't use obsolete _mavendepmapfragdir macro
- Fix FTBFS issues

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.19-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Feb 24 2014 Omair Majid <omajid@redhat.com> - 2.3.19-8
- Require java-headless

* Fri Oct 04 2013 Omair Majid <omajid@redhat.com> - 2.3.19-7
- Fix upstream Source URL for pom file

* Mon Aug 05 2013 Omair Majid <omajid@redhat.com> - 2.3.19-7
- Fix build dependencies

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.19-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.19-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Aug 01 2012 Omair Majid <omajid@redhat.com> - 2.3.19-4
- Build remaining classes with target 6 too.
- Fixes RHBZ#842594

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 27 2012 Omair Majid <omajid@redhat.com> - 2.3.19-2
- Remove obsolete patches

* Tue Jun 05 2012 gil cattaneo <puntogil@libero.it - 2.3.19-2
- update patch for logging

* Thu May 31 2012 Omair Majid <omajid@redhat.com> - 2.3.19-1
- Add dependency on apache-commons-logging

* Wed May 16 2012 gil cattaneo <puntogil@libero.it> - 2.3.19-1
- update to 2.3.19

* Wed Feb 01 2012 Marek Goldmann <mgoldman@redhat.com> - 2.3.13-14
- Added Maven POM, RHBZ#786383

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.13-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Mar 16 2011 Omair Majid <omajid@redhat.com> - 2.3.13-12
- Drop build dependency on struts
- Remove buildroot cleaning and definition
- Remove versioned jars
- Remove dependency of javadoc subpackage on main package

* Mon Feb 28 2011 Omair Majid <omajid@redhat.com> - 2.3.13-12
- Remove dependency on tomcat5

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.13-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Sep 13 2010 Alexander Kurtakov <akurtako@redhat.com> 2.3.13-10
- Adapt to tomcat6-el jar rename.

* Mon Sep 13 2010 Alexander Kurtakov <akurtako@redhat.com> 2.3.13-9
- Add tomcat6-libs BR.
- Use global instead of define.

* Sat Feb 27 2010 Victor G. Vasilyev <victor.vasilyev@sun.com> 2.3.13-8
- fix build patch for use of the javacc 5.0
- patch for encoding
- disable brp-java-repack-jars

* Sat Feb 27 2010 Victor G. Vasilyev <victor.vasilyev@sun.com> 2.3.13-7
- patch for logging
- remove name from the summary

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Sep 01 2008 Victor G. Vasilyev <victor.vasilyev@sun.com> 2.3.13-4
- Redundant dependency upon xerces-j2 is removed (#456276#c6)
- The dos2unix package is added as the build requirements
- The ant-nodeps build-time requirement is added

* Wed Aug 20 2008 Victor G. Vasilyev <victor.vasilyev@sun.com> 2.3.13-3
- The downloads.sourceforge.net host is used in the source URL
- %%{__install} and %%{__cp} are used everywhere
- %%defattr(-,root,root,-) is used everywhere

* Thu Aug 14 2008 Victor G. Vasilyev <victor.vasilyev@sun.com> 2.3.13-2
- Appropriate values of Group Tags are chosen from the official list
- Versions of java-devel & jpackage-utils are corrected
- Name of dir for javadoc is changed
- Manual is removed due to http://freemarker.org/docs/index.html

* Fri Jun 06 2008 Victor G. Vasilyev <victor.vasilyev@sun.com> 2.3.13-1
- Initial version

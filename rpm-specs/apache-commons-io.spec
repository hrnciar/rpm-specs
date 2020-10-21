# unit tests do not finish or crash the JVM
%bcond_with tests

%global srcname commons-io

Name:           apache-commons-io
Epoch:          1
Version:        2.8.0
Release:        1%{?dist}
Summary:        Utilities to assist with developing IO functionality
License:        ASL 2.0

URL:            https://commons.apache.org/io
Source0:        https://archive.apache.org/dist/commons/io/source/%{srcname}-%{version}-src.tar.gz

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.commons:commons-parent:pom:)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)

%if %{with tests}
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter)
BuildRequires:  mvn(org.mockito:mockito-core)
BuildRequires:  mvn(org.apache.maven.surefire:surefire-junit-platform)
%endif

%description
Commons-IO contains utility classes, stream implementations,
file filters, and endian classes. It is a library of utilities
to assist with developing IO functionality.


%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
API documentation for %{name}.


%prep
%setup -q -n %{srcname}-%{version}-src
sed -i 's/\r//' *.txt

%if %{with tests}
# com.google.jimfs:jimfs is not packaged for fedora
%pom_remove_dep com.google.jimfs:jimfs
rm src/test/java/org/apache/commons/io/input/ReversedLinesFileReaderTestParamFile.java

# junit-pioneer is not packaged for fedora
%pom_remove_dep :junit-pioneer
rm src/test/java/org/apache/commons/io/input/XmlStreamReaderTest.java
rm src/test/java/org/apache/commons/io/output/XmlStreamWriterTest.java
%endif

%mvn_file  : commons-io %{name}
%mvn_alias : org.apache.commons:


%build
%if %{with tests}
%mvn_build -- -Dcommons.osgi.symbolicName=org.apache.commons.io
%else
%mvn_build -f -- -Dcommons.osgi.symbolicName=org.apache.commons.io
%endif


%install
%mvn_install


%files -f .mfiles
%license LICENSE.txt NOTICE.txt
%doc RELEASE-NOTES.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt NOTICE.txt


%changelog
* Fri Oct 16 2020 Fabio Valentini <decathorpe@gmail.com> - 1:2.8.0-1
- Update to version 2.8.0.

* Tue Aug 18 2020 Fabio Valentini <decathorpe@gmail.com> - 1:2.7-1
- Update to version 2.7.

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 1:2.6-9
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 07 2019 Mat Booth <mat.booth@redhat.com> - 1:2.6-6
- Rebuild to regenerate OSGi metadata

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 29 2018 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:2.6-2
- Cleanup spec file

* Sun Oct 22 2017 Michael Simacek <msimacek@redhat.com> - 1:2.6-1
- Update to upstream version 2.6

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jun 23 2016 Michael Simacek <msimacek@redhat.com> - 1:2.5-1
- Update to upstream version 2.5

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Oct 14 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:2.4-13
- Remove legacy Obsoletes/Provides for jakarta-commons

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1:2.4-11
- Use Requires: java-headless rebuild (#1067528)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Apr 22 2013 Michal Srb <msrb@redhat.com> - 1:2.4-9
- Rebuild

* Mon Apr 15 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:2.4-8
- Update to current packaging guidelines

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1:2.4-6
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Wed Jan  9 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:2.4-5
- Bump release tag

* Tue Jan  8 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:2.4-4
- Build with xmvn

* Mon Nov 19 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:2.4-3
- Add Provides/Obsoletes for jakarta-commons-io

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 19 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:2.4-1
- Updae to 2.4

* Mon Apr 16 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:2.3-1
- Update to 2.3

* Wed Apr 4 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:2.2-1
- Update to 2.2
- Remove rpm bug workaround
- Finalize renaming from jakarta-comons-io

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Dec 7 2011 Alexander Kurtakov <akurtako@redhat.com> 1:2.1-1
- Update to latest upstream (2.1).

* Thu Jun 23 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1:2.0.1-3
- Fix build with maven3
- Use new add_maven_depmap macro

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jan 18 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1:2.0.1-1
- Update to 2.0.1
- Versionless jars & javadocs
- Use maven 3 to build
- Use apache-commons-parent for BR

* Fri Oct 22 2010 Chris Spike <chris.spike@arcor.de> 1:2.0-1
- Updated to 2.0
- Cleaned up BRs

* Thu Jul  8 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1:1.4-6
- Add license to javadoc subpackage

* Fri May 21 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1:1.4-5
- Correct depmap filename for backward compatibility

* Mon May 17 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1:1.4-4
- Fix maven depmap JPP name to short_name

* Wed May 12 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1:1.4-3
- Add obsoletes to javadoc sub-package

* Wed May 12 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1:1.4-2
- Add symlink to short_name.jar
- Fix mavendepmapfragdir wildcard

* Tue May 11 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1:1.4-1
- Rename and rebase of jakarta-commons-io
- Clean up whole spec


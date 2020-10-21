%global base_name       configuration
%global short_name      commons-%{base_name}

Name:           apache-%{short_name}
Version:        1.10
Release:        18%{?dist}
Summary:        Commons Configuration Package

License:        ASL 2.0
URL:            http://commons.apache.org/%{base_name}/
Source0:        http://archive.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz
BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(commons-beanutils:commons-beanutils)
BuildRequires:  mvn(commons-codec:commons-codec)
BuildRequires:  mvn(commons-collections:commons-collections)
BuildRequires:  mvn(commons-digester:commons-digester)
BuildRequires:  mvn(commons-jxpath:commons-jxpath)
BuildRequires:  mvn(commons-lang:commons-lang)
BuildRequires:  mvn(commons-logging:commons-logging)
BuildRequires:  mvn(javax.servlet:servlet-api)
BuildRequires:  mvn(log4j:log4j:1.2.17)
BuildRequires:  mvn(org.apache.commons:commons-jexl)
BuildRequires:  mvn(org.apache.commons:commons-parent:pom:)
BuildRequires:  mvn(org.apache.commons:commons-vfs2)
BuildRequires:  mvn(org.codehaus.mojo:javacc-maven-plugin)
BuildRequires:  mvn(xml-apis:xml-apis)
BuildRequires:  mvn(xml-resolver:xml-resolver)


%description
Configuration is a project to provide a generic Configuration
interface and allow the source of the values to vary. It
provides easy typed access to single, as well as lists of
configuration values based on a 'key'.
Right now you can load properties from a simple properties
file, a properties file in a jar, an XML file, JNDI settings,
as well as use a mix of different sources using a
ConfigurationFactory and CompositeConfiguration.
Custom configuration objects are very easy to create now
by just subclassing AbstractConfiguration. This works
similar to how AbstractList works.

%if 0
%package        javadoc
Summary:        API documentation for %{name}

%description    javadoc
%{summary}.
%endif


%prep
%setup -q -n %{short_name}-%{version}-src
sed -i 's/\r//' LICENSE.txt NOTICE.txt

%pom_change_dep :log4j ::1.2.17

%build
%mvn_file   : %{short_name} %{name}
%mvn_alias  : org.apache.commons:%{short_name}
# We skip tests because we don't have test deps (dbunit in particular).
# FIXME Javadocs are temporarly disabled due to JDK bug, see
# https://bugzilla.redhat.com/show_bug.cgi?id=1423421
%mvn_build -f -j

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt

%if 0
%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt
%endif


%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-18
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 1.10-16
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 17 2017 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.10-9
- Temporarly disable javadoc generation

* Fri Feb 10 2017 Michael Simacek <msimacek@redhat.com> - 1.10-8
- Use log4j12

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Oct 14 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.10-4
- Remove legacy Obsoletes/Provides for jakarta-commons

* Thu Jun 12 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.10-3
- Fix BR on commons-parent

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Oct 29 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.10-1
- Update to upstream version 1.10

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Apr 29 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.9-5
- Remove unneeded BR: maven-idea-plugin

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.9-3
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Tue Jan 15 2013 Michal Srb <msrb@redhat.com> - 1.9-2
- Build with xmvn

* Thu Aug 23 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.9-1
- Update to upstream version 1.9
- Update to currennt packaging guidelines

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 19 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.8-1
- Update to upstream 1.8
- Install NOTICE.txt file

* Wed Apr 18 2012 Alexander Kurtakov <akurtako@redhat.com> 1.6-7
- Update to current guidelines.
- Move to servlet 3.

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 15 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.6-5
- Change ant dep groupId to org.apache.ant to fix build
- Versionless jar & javadocs
- Use maven 3 to build

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Oct 14 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.6-3
- tomcat5 -> tomcat6 BRs/Rs
- jakarta -> apache BRs/Rs

* Thu Jul  8 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.6-2
- Add license to javadoc subpackage

* Thu May 27 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.6-1
- Rename package (jakarta-commons-configuration->apache-commons-configuration)
- Build with maven instead of ant, drop deprecated patches
- Rebase, cleanups, drop epoch

* Thu Aug 20 2009 Alexander Kurtakov <akurtako@redhat.com> 0:1.4-7
- Fix description.
- Remove requires(post/postun) for javadoc subpackage.
- Use sed instead of dos2unix.

* Thu Aug 20 2009 Alexander Kurtakov <akurtako@redhat.com> 0:1.4-6
- Remove gcj support.
- Initial build for Fedora.

* Mon May 18 2009 Fernando Nasser <fnasser@redhat.com> - 0:1.4-5
- Fix license
- Fix source URL

* Wed Mar 18 2009 Yong Yang <yyang@redhat.com> - 0:1.4-4
- rebuild with new maven2 2.0.8 built in bootstrap mode

* Thu Feb 05 2009 Yong Yang <yyang@redhat.com> - 0:1.4-3
- Fix release tag

* Wed Jan 14 2009 Yong Yang <yyang@redhat.com> - 0:1.4-2jpp
- Import from dbhole's maven 2.0.8 packages, initial building

* Mon Aug 13 2007 Ralph Apel <r.apel at r-apel.de> - 0:1.4-1jpp
- Upgrade to 1.4
- Add pom file

* Thu May 03 2007 Ralph Apel <r.apel at r-apel.de> - 0:1.2-3jpp
- Patch one test

* Wed Mar 07 2007 Ralph Apel <r.apel at r-apel.de> - 0:1.2-2jpp
- Add gcj_support option
- Optionally build without maven

* Mon Feb 20 2006 Ralph Apel <r.apel at r-apel.de> - 0:1.2-1jpp
- Upgrade to 1.2

* Mon Feb 20 2006 Ralph Apel <r.apel at r-apel.de> - 0:1.1-2jpp
- Rebuild for JPP-1.7 and maven-1.1

* Thu Sep 15 2005 Ralph Apel <r.apel at r-apel.de> - 0:1.1-1jpp
- Upgrade to 1.1
- Omit findbugs and tasks reports: don't have these plugins yet
- Requires java 1.4.2 to build

* Mon Feb 21 2005 Ralph Apel <r.apel at r-apel.de> - 0:1.0.f-1jpp
- Upgrade to 1.0 final, letter in version can be bumped with 1.1
- Prepare for build with maven, but still build with ant

* Sun Aug 23 2004 Randy Watler <rwatler at finali.com> - 0:1.0.d3-2jpp
- Rebuild with ant-1.6.2
- Upgrade to Ant 1.6.X
* Mon Jan 19 2004 Ralph Apel <r.apel at r-apel.de> - 0:1.0.d3-1jpp
- First JPackage release

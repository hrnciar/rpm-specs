%global namedreltag .GA
%global namedversion %{version}%{?namedreltag}

Name:             apiviz
Version:          1.3.2
Release:          24%{?dist}
Summary:          APIviz is a JavaDoc doclet to generate class and package diagrams
License:          LGPLv2+
URL:              http://code.google.com/p/apiviz/
Source0:          http://apiviz.googlecode.com/files/apiviz-%{namedversion}-dist.tar.gz
Patch0:           0001-JDK7-compatibility.patch
Patch1:           0002-JDK8-compatibility.patch
Patch2:           0003-fix-deprecated-assembly-goal.patch

BuildArch:        noarch

BuildRequires:    maven-local
BuildRequires:    mvn(ant-contrib:ant-contrib)
BuildRequires:    mvn(com.sun:tools)
BuildRequires:    mvn(jdepend:jdepend)
BuildRequires:    mvn(junit:junit)
BuildRequires:    mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:    mvn(org.apache.maven.plugins:maven-assembly-plugin)
BuildRequires:    mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:    mvn(org.jboss:jboss-parent:pom:)

%description
APIviz is a JavaDoc doclet which extends the Java standard doclet.
It generates comprehensive UML-like class and package diagrams for
quick understanding of the overall API structure. 

%package javadoc
Summary:          Javadocs for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n apiviz-%{namedversion}
%patch0 -p1

%if 0%{?fedora} || 0%{?rhel} > 7
%patch1 -p1
%patch2 -p0
%endif

find -name '*.class' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;

#%pom_xpath_remove "pom:dependencies/pom:dependency[pom:artifactId = 'tools']/pom:scope"
#%pom_xpath_remove "pom:dependencies/pom:dependency[pom:artifactId = 'tools']/pom:systemPath"

%pom_remove_dep com.sun:tools
%pom_add_dep com.sun:tools

%mvn_alias "org.jboss.apiviz:apiviz" "net.gleamynode.apiviz:apiviz"

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc COPYRIGHT.txt LICENSE.jdepend.txt LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-24
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 1.3.2-22
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri May 25 2018 Michael Simacek <msimacek@redhat.com> - 1.3.2-17
- Regenerate BRs

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 09 2018 Troy Dawson <tdawson@redhat.com> - 1.3.2-15
- Add BuildRequires: maven-assembly-plugin

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 04 2017 Merlin Mathesius <mmathesi@redhat.com> - 1.3.2-12
- Correct deprecated assembly goal that was eliminated from
  maven-assembly-plugin 3.x to fix FTBFS (BZ#1402518).

* Wed Dec 14 2016 Merlin Mathesius <mmathesi@redhat.com> - 1.3.2-11
- Add missing BuildRequires for jboss-parent to fix FTBFS (BZ#1402518).

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jun 17 2014 Marek Goldmann <mgoldman@redhat.com> - 1.3.2-8
- Switch to xmvn + BR updates

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 1.3.2-6
- Use Requires: java-headless rebuild (#1067528)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.3.2-3
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Wed Oct 17 2012 Marek Goldmann <mgoldman@redhat.com> - 1.3.2-2
- Added maven-enforcer-plugin BR

* Wed Oct 17 2012 Marek Goldmann <mgoldman@redhat.com> - 1.3.2-1
- Upstream release 1.3.2.GA
- Removed JDK7 patch

* Mon Sep  3 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3.1-8
- Add missing R: graphviz

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Mar 12 2012 Marek Goldmann <mgoldman@redhat.com> 1.3.1-6
- Added additional POM mapping

* Fri Mar 09 2012 Marek Goldmann <mgoldman@redhat.com> 1.3.1-5
- Relocated jars to _javadir

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Nov 18 2011 Marek Goldmann <mgoldman@redhat.com> 1.3.1-3
- Working on on jdk7

* Wed Jul 27 2011 Marek Goldmann <mgoldman@redhat.com> 1.3.1-2
- Using upstream tarball

* Wed Jul 20 2011 Marek Goldmann <mgoldman@redhat.com> 1.3.1-1
- Initial packaging


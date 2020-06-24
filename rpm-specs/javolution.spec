%global namedversion %{version}
Name:          javolution
Version:       5.5.1
Release:       0.16%{?dist}
Summary:       Java Solution for Real-Time and Embedded Systems
License:       BSD
URL:           http://javolution.org/
# svn export https://svn.kenai.com/svn/javolution~source-code-repository/Javolution/ javolution-5.5.1
# rm -r javolution-5.5.1/colapi.jar javolution-5.5.1/banner.png javolution-5.5.1/index.html javolution-5.5.1/css
# rm -r javolution-5.5.1/src/main/java/org
# tar czf javolution-5.5.1-src-svn.tar.gz javolution-5.5.1
Source0:       %{name}-%{namedversion}-src-svn.tar.gz
# http://bugs.sun.com/view_bug.do?bug_id=6904536
Patch0:        %{name}-oj7-template.patch

BuildArch:     noarch

BuildRequires: java-devel
BuildRequires: junit
BuildRequires: maven-local
BuildRequires: maven-resources-plugin
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-antrun-plugin)

%description
Javolution - Java Solution for Real-Time and Embedded Systems.
This project provides a Java library for real-time 
applications. It is maven-based and can be used to 
build multi-platform real-time applications. It uses template 
classes to generates java code for various versions of the 
Java run-time (e.g. J2ME, 1.4, GCJ, 1.5).

%package javadoc
Summary:       Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -qn %{name}-%{namedversion}
%patch0 -p1

# disable wagon-svn, colapi
%pom_remove_plugin javolution:colapi
%pom_xpath_remove "pom:project/pom:build/pom:extensions"

sed -i 's/\r//' LICENSE.txt

%mvn_file  "%{name}:%{name}" %{name}

%build
# random test failure in Struct for UNSIGNED32
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.1-0.16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.1-0.15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.1-0.14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.1-0.13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.1-0.12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.1-0.11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb 13 2017 Pete MacKinnon <pmackinn@redhat.com> 5.5.1-0.10
- Add maven-[antrun,bundle,source]-plugin deps

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.1-0.9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.1-0.8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.5.1-0.7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.5.1-0.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 5.5.1-0.5
- Use Requires: java-headless rebuild (#1067528)

* Mon Dec 2 2013 Pete MacKinnon <pmackinn@redhat.com> 5.5.1-0.4
- dist bump for new build

* Thu Sep 19 2013 Peter MacKinnon <pmackinn@redhat.com> 5.5.1-0.3
- removed unnecessary javadoc noarch

* Thu Sep 19 2013 Peter MacKinnon <pmackinn@redhat.com> 5.5.1-0.2
- changes from review feedback

* Tue Sep 17 2013 Peter MacKinnon <pmackinn@redhat.com> 5.5.1-0.1
- 5.5.1 release due to felix/OJ7 issues
- maven-local macros

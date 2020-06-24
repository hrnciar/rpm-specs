%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             hibernate-jpa-2.0-api
Version:          1.0.1
Release:          26%{?dist}
Summary:          Java Persistence 2.0 (JSR 317) API
License:          EPL and BSD
URL:              http://www.hibernate.org/
# svn export http://anonsvn.jboss.org/repos/hibernate/jpa-api/tags/hibernate-jpa-2.0-api-1.0.1.Final/ hibernate-jpa-2.0-api-1.0.1.Final
# tar -zcvf hibernate-jpa-2.0-api-1.0.1.Final.tar.gz hibernate-jpa-2.0-api-1.0.1.Final
Source0:          %{name}-%{namedversion}.tar.gz
Patch0:           %{name}-%{namedversion}-encoding.patch
Patch1:           %{name}-%{namedversion}-osgi-manifest.patch

BuildArch:        noarch

BuildRequires:    maven-local

%description
Hibernate definition of the Java Persistence 2.0 (JSR 317) API.

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}
%patch0 -p1
%patch1 -p1

%pom_xpath_remove pom:build/pom:extensions

%pom_remove_plugin :maven-release-plugin
%pom_remove_plugin :maven-source-plugin

# Fixing wrong-file-end-of-line-encoding
sed -i 's/\r//' src/main/javadoc/jdstyle.css

%build
%mvn_build

%install
# Fixing wrong-file-end-of-line-encoding
sed -i 's/\r//' target/site/apidocs/jdstyle.css
%mvn_install

%files -f .mfiles
%doc readme.txt
%license license.txt

%files javadoc -f .mfiles-javadoc
%license license.txt

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Oct 14 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.1-25
- Remove useless maven-release-plugin to fix builds.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jun 21 2016 gil cattaneo <puntogil@libero.it> 1.0.1-18
- fix BR list
- adapt to current guideline
- introduce license macro
- fix some rpmlint problem

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jul 21 2014 Marek Goldmann <mgoldman@redhat.com> - 1.0.1-15
- Switch to xmvn

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 1.0.1-13
- Use Requires: java-headless rebuild (#1067528)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Feb 19 2013 Marek Goldmann <mgoldman@redhat.com> - 1.0.1-11
- Removed wagon extension

* Fri Feb 15 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0.1-10
- Don't install depmap for javax.persistence:persistence-api

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.0.1-8
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 19 2012 Gerard Ryan <galileo@fedoraproject.org> 1.0.1-6
- Add OSGI info to MANIFEST.MF

* Fri Mar 16 2012 Marek Goldmann <mgoldman@redhat.com> 1.0.1-5
- Relocated jars to _javadir
- Added javax.persistence:persistence-api POM mapping

* Sun Jan 15 2012 Marek Goldmann <mgoldman@redhat.com> 1.0.1-4
- Fixed encoding

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jul 27 2011 Marek Goldmann <mgoldman@redhat.com> 1.0.1-2
- Removed unnecessary macros, using new add_maven_depmap
- License fix

* Tue Jul 05 2011 Marek Goldmann <mgoldman@redhat.com> 1.0.1-1
- Upstream release, license fix

* Fri May 20 2011 Marek Goldmann <mgoldman@redhat.com> 1.0.0-1
- Initial packaging


%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}
%global oname jboss-jsp-api_2.3_spec

Name:             jboss-jsp-2.3-api
Version:          1.0.3
Release:          2%{dist}
Summary:          JavaServer Pages 2.3 API (JSP)
License:          (CDDL or GPLv2 with exceptions) or ASL 2.0

URL:              https://github.com/jboss/jboss-jsp-api_spec
Source0:          %{url}/archive/%{oname}-%{namedversion}.tar.gz
Source1:          http://www.apache.org/licenses/LICENSE-2.0.txt

BuildArch:        noarch

BuildRequires:    maven-local
BuildRequires:    mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:    mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:    mvn(org.jboss:jboss-parent:pom:)
BuildRequires:    mvn(org.jboss.spec.javax.el:jboss-el-api_3.0_spec)
BuildRequires:    mvn(org.jboss.spec.javax.servlet:jboss-servlet-api_3.1_spec)

%description
JSR-000245: JavaServer Pages 2.3

%package javadoc
Summary:          Javadoc for %{name}

%description javadoc	
This package contains the API documentation for %{name}.

%prep
%setup -q -n jboss-jsp-api_spec-%{oname}-%{namedversion}

cp %{SOURCE1} .

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README
%license LICENSE LICENSE-2.0.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE LICENSE-2.0.txt

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Oct 05 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.3-1
- Update to version 1.0.3.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jun 01 2016 gil cattaneo <puntogil@libero.it> 1.0.1-1
- update to 1.0.1.Final
- fix BR list and use BR mvn()-like
- introduce license macro
- remove some rpmlint problems
- remove duplicate files

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.6.Beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-0.5.Beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-0.4.Beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Dec 13 2013 Marek Goldmann <mgoldman@redhat.com> - 1.0.0-0.3.Beta1
- Removed the API dir
- Removed provides

* Fri Dec 13 2013 Marek Goldmann <mgoldman@redhat.com> - 1.0.0-0.2.Beta1
- Fixed license tag
- Added provides for API
- Cleaned up BR
- Added ASL 2.0 license

* Thu Dec 12 2013 Marek Goldmann <mgoldman@redhat.com> - 1.0.0-0.1.Beta1
- Initial packaging



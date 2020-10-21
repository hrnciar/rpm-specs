%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:    jboss-jsf-2.1-api
Version: 2.0.2
Release: 22%{dist}
Summary: JavaServer Faces 2.1 API
License: CDDL or GPLv2 with exceptions
URL:     http://www.jboss.org

# git clone git://github.com/jboss/jboss-jsf-api_spec.git jboss-jsf-2.1-api
# cd jboss-jsf-2.1-api/ && git archive --format=tar --prefix=jboss-jsf-2.1-api-2.0.2.Final/ jboss-jsf-api_2.1_spec-2.0.2.Final | xz > jboss-jsf-2.1-api-2.0.2.Final.tar.xz
Source0: %{name}-%{namedversion}.tar.xz

# Fix the FSF address in the license file:
Patch0:  %{name}-fix-fsf-address.patch

BuildRequires: mvn(javax.validation:validation-api)
BuildRequires: mvn(org.jboss:jboss-parent:pom:)
BuildRequires: mvn(org.jboss.spec.javax.el:jboss-el-api_2.2_spec)
BuildRequires: mvn(org.jboss.spec.javax.servlet.jsp:jboss-jsp-api_2.2_spec)
BuildRequires: mvn(org.jboss.spec.javax.servlet.jstl:jboss-jstl-api_1.2_spec)
BuildRequires: maven-local
BuildRequires: maven-plugin-bundle
BuildRequires: objenesis

BuildArch:     noarch


%description
JavaServer Faces API classes based on Version 2.1 of Specification.

%package javadoc
Summary: Javadoc for %{name}

%description javadoc	
This package contains the API documentation for %{name}.

%prep

# Unpack the sources:
%setup -q -n %{name}-%{namedversion}
# Apply the patches:
%patch0 -p1

%mvn_file :jboss-jsf-api_2.1_spec %{name}
%mvn_alias :jboss-jsf-api_2.1_spec javax.faces:jsf-api

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%license LICENSE
%doc README

%files javadoc -f .mfiles-javadoc
%license LICENSE
%doc README

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-22
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 2.0.2-20
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Feb 12 2015 gil cattaneo <puntogil@libero.it> 2.0.2-10
- fix for RHBZ#1085433,1106882,1068229
- adapt to current guideline
- introduce license macro

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 2.0.2-8
- Use Requires: java-headless rebuild (#1067528)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 2.0.2-5
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Mar 28 2012 Juan Hernandez <juan.hernandez@redhat.com> 2.0.2-3
- Added geronimo-validation to the build requirements

* Fri Mar 23 2012 Juan Hernandez <juan.hernandez@redhat.com> 2.0.2-2
- Use global instead of define

* Thu Mar 22 2012 Juan Hernandez <juan.hernandez@redhat.com> 2.0.2-1
- Update to upstream version 2.0.0
- Cleanup of the spec file

* Fri Aug 12 2011 Marek Goldmann <mgoldman@redhat.com> 2.0.0-1
- Initial packaging


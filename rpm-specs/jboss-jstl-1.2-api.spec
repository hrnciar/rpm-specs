%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}
%global pname jboss-jstl-api_spec
%global oname jboss-jstl-api_1.2_spec

Name:          jboss-jstl-1.2-api
Version:       1.1.2
Release:       9%{dist}
Summary:       JSP Standard Template Library 1.2 API
License:       ASL 2.0 and (CDDL or GPLv2 with exceptions)
URL:           https://github.com/jboss/jboss-jstl-api_spec
Source0:       https://github.com/jboss/jboss-jstl-api_spec/archive/%{oname}-%{namedversion}.tar.gz
# Fix the FSF address in the license file:
Patch0:        %{name}-fix-fsf-address.patch
Patch1:        %{name}-endorse_xalan.patch

BuildRequires: maven-local
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.easymock:easymock)
BuildRequires: mvn(org.jboss:jboss-parent:pom:)
BuildRequires: mvn(org.jboss.spec.javax.el:jboss-el-api_3.0_spec)
BuildRequires: mvn(org.jboss.spec.javax.servlet:jboss-servlet-api_3.1_spec)
BuildRequires: mvn(org.jboss.spec.javax.servlet.jsp:jboss-jsp-api_2.3_spec)
BuildRequires: mvn(xalan:xalan)

BuildArch:     noarch

%description
Java Server Pages Standard Template Library 1.2 API.

%package javadoc
Summary: Javadoc for %{name}

%description javadoc	
This package contains the API documentation for %{name}.

%prep
# Unpack the sources:
%setup -q -n %{pname}-%{oname}-%{namedversion}
# Apply the patches:
%patch0 -p1
# only for EL, in fedora ibm jdk is not available
%if 0%{?el7}
%patch1 -p1
%endif

%pom_remove_plugin :maven-source-plugin

%mvn_file : %{name}

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%license LICENSE README
%doc CHANGES.txt README.md

%files javadoc -f .mfiles-javadoc
%license LICENSE README

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Feb 08 2017 gil cattaneo <puntogil@libero.it> 1.1.2-3
- fix FTBFS

* Sat Nov 19 2016 gil cattaneo <puntogil@libero.it> 1.1.2-2
- add missing build requires: easymock

* Wed Jul 06 2016 gil cattaneo <puntogil@libero.it> 1.1.2-1
- update to 1.1.2.Final (rhbz#1346387)

* Tue Jun 21 2016 gil cattaneo <puntogil@libero.it> 1.0.3-15
- add missing build requires
- add check for PATCH1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Nov 11 2015 Michael Mraka <michael.mraka@redhat.com> 1.0.3-13
- fixed s390x + java-ibm build (#1279214)

* Thu Jul 30 2015 gil cattaneo <puntogil@libero.it> - 1.0.3-12
- Fix FTBFS RHBZ#1239597
- Switch to xmvn
- Use BR mvn()-like
- Fix some rpmlint problem
- Introduce license macro
- Adapt to current guideline

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 04 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 1.0.3-10
- Fix FTBFS due to F21 XMvn changes (#1106885)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 1.0.3-8
- Use Requires: java-headless rebuild (#1067528)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.0.3-5
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Tue Jul 24 2012 Juan Hernandez <juan.hernandez@redhat.com> - 1.0.3-4
- Added maven-enforcer-plugin build time dependency

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Mar 23 2012 Juan Hernandez <juan.hernandez@redhat.com> 1.0.3-2
- Use global instead of define

* Thu Mar 22 2012 Juan Hernandez <juan.hernandez@redhat.com> 1.0.3-1
- Update to upstream version 1.0.3
- Cleanup of the spec file

* Fri Aug 12 2011 Marek Goldmann <mgoldman@redhat.com> 1.0.0-1
- Initial packaging


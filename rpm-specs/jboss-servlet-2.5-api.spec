%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             jboss-servlet-2.5-api
Version:          1.0.1
Release:          19%{dist}
Summary:          Java Servlet 2.5 API
License:          ASL 2.0 and W3C
Url:              http://www.jboss.org

# git clone git://github.com/jboss/jboss-servlet-api_spec.git
# cd jboss-servlet-api_spec/ && git archive --format=tar --prefix=jboss-servlet-2.5-api/ jboss-servlet-api_2.5_spec-1.0.1.Final | xz > jboss-servlet-2.5-api-1.0.1.Final.tar.xz
Source0:          jboss-servlet-2.5-api-%{namedversion}.tar.xz

BuildRequires:    maven-local
BuildRequires:    mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:    mvn(org.jboss.spec:jboss-specs-parent:pom:)

BuildArch:        noarch

%description
The Java Servlet 2.5 API classes.

%package javadoc
Summary:          Javadoc for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n jboss-servlet-2.5-api

%mvn_file : %{name}

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%license LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%license LICENSE NOTICE

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jun 21 2016 gil cattaneo <puntogil@libero.it> 1.0.1-12
- add missing build requires

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jul 30 2015 gil cattaneo <puntogil@libero.it> - 1.0.1-10
- Fix FTBFS RHBZ#1239607
- Switch to xmvn
- Use BR mvn()-like
- Fix some rpmlint problem
- Introduce license macro
- Adapt to current guideline

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 27 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 1.0.1-8
- Fix FTBFS due to recent XMvn changes (#1106899)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 1.0.1-6
- Use Requires: java-headless rebuild (#1067528)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 11 2013 Ade Lee <alee@redhat.com> 1.0.1-4
- Removed unneeded build dependencies

* Thu Apr 4 2013 Ade Lee <alee@redhat.com> 1.0.1-3
- Removed javax.servlet mapping

* Wed Apr 3 2013 Ade Lee <alee@redhat.com> 1.0.1-2
- Corrected license

* Tue Apr 2 2013 Ade Lee <alee@redhat.com> 1.0.1-1
- Initial packaging

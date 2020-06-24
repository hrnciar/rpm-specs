Name:           jmdns
Version:        3.5.5
Release:        1%{?dist}
Summary:        Java implementation of multi-cast DNS

License:        ASL 2.0
URL:            https://github.com/jmdns/jmdns
Source0:        %{url}/archive/%{name}-%{version}/%{name}-%{version}.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.slf4j:slf4j-api)

BuildArch:      noarch

%description
JmDNS is a Java implementation of multi-cast DNS
and can be used for service registration and discovery
in local area networks. JmDNS is fully compatible
with Apple's Bonjour.


%prep
%autosetup -n %{name}-%{name}-%{version} -p1

# Remove duplicate jar execution
%pom_xpath_remove "pom:plugin[pom:artifactId='maven-jar-plugin']/pom:executions"

# Javadoc temporary disabled while upsteam not fix javadoc generation
# https://github.com/jmdns/jmdns/issues/199
%pom_xpath_remove "pom:plugin[pom:artifactId='maven-javadoc-plugin']"
%pom_xpath_remove "pom:properties[pom:javadoc.opts]"

chmod -x README.md


%build
# Tests are disabled because they try to use network
%mvn_build -f --skip-javadoc


%install
%mvn_install


%files -f .mfiles
%license LICENSE
%doc README.md



%changelog
* Mon Apr 06 2020 ElXreno <elxreno@gmail.com> - 3.5.5-1
- Updated to version 3.5.5

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Feb 16 2017 Mat Booth <mat.booth@redhat.com> - 3.4.1-12
- Fix failure to build from source

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Sep 01 2014 Michal Srb <msrb@redhat.com> - 3.4.1-8
- Fix BR

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 3.4.1-6
- Use Requires: java-headless rebuild (#1067528)

* Thu Feb 20 2014 Michal Srb <msrb@redhat.com> - 3.4.1-5
- Backport Jenkins patch: faster shutdown
- Add alias org.jenkins-ci:jmdns

* Thu Feb 20 2014 Michal Srb <msrb@redhat.com> - 3.4.1-4
- Fix directory ownership
- Add script for creating clean tarball

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri May 03 2013 Michal Srb <msrb@redhat.com> - 3.4.1-2
- Fix license tag
- Fix rpmlint warnings

* Thu May 02 2013 Michal Srb <msrb@redhat.com> - 3.4.1-1
- Initial package

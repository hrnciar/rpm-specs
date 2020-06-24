%global commit 8e55762cef51784b0308ed4cdcfeceaadb03e1d6
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           datanucleus-maven-parent
Version:        3.3
Release:        11%{?dist}
Summary:        DataNucleus Maven parent project 

License:        ASL 2.0
URL:            https://github.com/datanucleus/datanucleus-maven-parent
Source:         https://github.com/datanucleus/%{name}/archive/%{commit}/%{name}-%{commit}.tar.gz

# jira opened for missing ASL file
# http://www.datanucleus.org/servlet/jira/browse/NUCACCESS-130
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt 

BuildArch: noarch

BuildRequires:  maven-local
BuildRequires:  maven-clean-plugin
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)

%description
Datanucleus Maven parent pom used by other datanucleus packages.

%prep
%setup -q -n %{name}-%{commit}
cp -p %{SOURCE1} LICENSE
%pom_remove_plugin org.codehaus.mojo:findbugs-maven-plugin

%pom_xpath_remove "pom:extension[pom:artifactId[text()='wagon-ssh-external']]"

%pom_remove_parent

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb 13 2017 Pete MacKinnon <pmackinn@redhat.com> - 3.3-5
- Remove oss-parent
- Add maven-plugin-bundle dep

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 12 2014 Pete MacKinnon <pmackinn@redhat.com> - 3.3-1
- Initial version
- remove wagon-ssh-external
- git commit for src

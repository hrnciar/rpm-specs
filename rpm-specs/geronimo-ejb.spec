Name:           geronimo-ejb
Version:        1.0
Release:        24%{?dist}
Summary:        Java EE: EJB API v3.1
License:        ASL 2.0
URL:            http://geronimo.apache.org
BuildArch:      noarch

Source0:        http://repo2.maven.org/maven2/org/apache/geronimo/specs/%{name}_3.1_spec/%{version}/%{name}_3.1_spec-%{version}-source-release.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.geronimo.specs:geronimo-annotation_1.1_spec)
BuildRequires:  mvn(org.apache.geronimo.specs:geronimo-interceptor_1.1_spec)
BuildRequires:  mvn(org.apache.geronimo.specs:geronimo-jaxrpc_1.1_spec)
BuildRequires:  mvn(org.apache.geronimo.specs:geronimo-jta_1.1_spec)
BuildRequires:  mvn(org.apache.geronimo.specs:geronimo-osgi-locator)
BuildRequires:  mvn(org.apache.geronimo.specs:specs:pom:)

%description
Contains the Enterprise JavaBeans classes and interfaces that define the
contracts between the enterprise bean and its clients and between the
enterprise bean and the EJB container.

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}_3.1_spec-%{version}
sed -i 's/\r//' LICENSE
# Use parent pom files instead of unavailable 'genesis-java5-flava'
%pom_set_parent org.apache.geronimo.specs:specs:1.4

%mvn_alias : org.apache.geronimo.specs:geronimo-ejb_2.1_spec
%mvn_alias : org.apache.geronimo.specs:geronimo-ejb_3.0_spec
%mvn_alias : javax.ejb:ejb
%mvn_alias : javax.ejb:ejb-api

%mvn_file : %{name} ejb

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%license LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%license LICENSE NOTICE

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Apr 18 2018 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-20
- Update to current packaging guidelines

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.0-13
- Use Requires: java-headless rebuild (#1067528)

* Thu Aug 15 2013 Mat Booth <fedora@matbooth.co.uk> - 1.0-12
- Add dependency mapping for javax.ejb:ejb-api, rhbz #826859

* Thu Aug  8 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.0-11
- Update to latest packaging guidelines

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Mar 03 2013 Mat Booth <fedora@matbooth.co.uk> - 1.0-9
- Change BR from maven2 to maven-local, fixes FTBFS rhbz #914027

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Dec 16 2011 Alexander Kurtakov <akurtako@redhat.com> 1.0-5
- Build with maven 3.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Aug 5 2010 Chris Spike <chris.spike@arcor.de> 1.0-3
- Fixed missing BR maven2
- Fixed missing BR geronimo-parent-poms
- Fixed missing BR maven-resources-plugin

* Wed Aug 4 2010 Chris Spike <chris.spike@arcor.de> 1.0-2
- Fixed wrong EOL encoding in LICENSE
- Removed custom depmap
- Added 'org.apache.geronimo.specs:geronimo-ejb_2.1_spec' to maven depmap
- Added 'org.apache.geronimo.specs:geronimo-ejb_3.0_spec' to maven depmap

* Thu Jul 22 2010 Chris Spike <chris.spike@arcor.de> 1.0-1
- Initial version of the package

%global bundle org.apache.felix.shell

Name:           felix-shell
Version:        1.4.3
Release:        17%{?dist}
Summary:        Apache Felix Shell Service
License:        ASL 2.0
URL:            https://felix.apache.org
Source0:        https://archive.apache.org/dist/felix/%{bundle}-%{version}-source-release.tar.gz

BuildArch: noarch

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.felix:felix-parent:pom:)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.osgi:osgi.cmpn)
BuildRequires:  mvn(org.osgi:osgi.core)
BuildRequires:  mvn(junit:junit)

%description
A simple OSGi command shell service.

%package javadoc
Summary:        API documentation for %{name}

%description javadoc
This package contains API documentation for %{name}.

%prep
%setup -q -n %{bundle}-%{version}

%pom_remove_plugin org.codehaus.mojo:rat-maven-plugin

# Use latest OSGi implementation
%pom_change_dep :org.osgi.core org.osgi:osgi.core
%pom_change_dep :org.osgi.compendium org.osgi:osgi.cmpn

# To run tests
%pom_add_dep junit:junit::test

%mvn_file :%{bundle} "felix/%{bundle}"

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%license LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%license LICENSE NOTICE

%changelog
* Mon Apr 27 2020 Dinesh Prasanth M K <dmoluguw@redhat.com> - 1.4.3-17
- Add junit dependency for running tests

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 17 2019 Mat Booth <mat.booth@redhat.com> - 1.4.3-15
- Build against OSGi R7 APIs

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.4.3-5
- Use Requires: java-headless rebuild (#1067528)

* Mon Aug 05 2013 Mat Booth <fedora@matbooth.co.uk> - 1.4.3-4
- Update for latest guidelines

* Sun Aug 04 2013 Mat Booth <fedora@matbooth.co.uk> - 1.4.3-3
- Add missing BRs

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Apr 15 2013 Mat Booth <fedora@matbooth.co.uk> - 1.4.3-1
- Update to latest upstream version rhbz #895405.
- Enable tests

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.4.2-8
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Apr 06 2012 Hui Wang <huwang@redhat.com> - 1.4.2-6
- Bug 810214

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Aug 02 2010 Hui Wang <huwang@redhat.com> - 1.4.2-3
- Fix source0
- Remove "rm -rf target/site/api/*"

* Fri Jul 30 2010 Hui Wang <huwang@redhat.com> - 1.4.2-2
- Add LICENSE to javadoc subpackage
- Use upstream source tarball
- Fix directory that owned by other package in files section

* Fri Jun 25 2010 Hui Wang <huwang@redhat.com> - 1.4.2-1
- Initial version of the package

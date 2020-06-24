Name:           jopt-simple
Version:        5.0.4
Release:        6%{?dist}
Summary:        A Java command line parser
License:        MIT
URL:            http://jopt-simple.github.io/jopt-simple
BuildArch:      noarch

Source0:        https://github.com/jopt-simple/jopt-simple/archive/jopt-simple-%{version}.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)

%description
JOpt Simple is a Java library for parsing command line options, such as those
you might pass to an invocation of javac.

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n jopt-simple-jopt-simple-%{version}

%pom_xpath_remove "pom:build/pom:extensions"
%pom_remove_dep org.infinitest:continuous-testing-toolkit
%pom_remove_plugin org.pitest:pitest-maven
%pom_remove_plugin org.codehaus.mojo:cobertura-maven-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-pmd-plugin
%pom_remove_plugin :animal-sniffer-maven-plugin

%build
# Unit testing is disabled due to a missing dependency in Fedora of continuous-testing-toolkit
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%license LICENSE.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Sep 14 2017 Mikolaj Izdebski <mizdebsk@redhat.com> - 5.0.4-1
- Update to upstream version 5.0.4

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Merlin Mathesius <mmathesi@redhat.com> - 4.6-4
- Add missing BuildRequires to fix FTBFS (BZ#1406157).

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 09 2014 Mat Booth <mat.booth@redhat.com> - 4.6-1
- Update to latest upstream release
- Drop unnecessary BRs

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Feb 27 2014 Mat Booth <fedora@matbooth.co.uk> - 4.5-3
- Update for latest guidelines rhbz #1068301

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jun 24 2013 Mat Booth <fedora@matbooth.co.uk> - 4.5-1
- Update to latest upstream, fixes rhbz #958111

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 3.3-7
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jan 16 2012 Karel Klíč <kklic@redhat.com> - 3.3-5
- Added maven-enforcer-plugin and maven-dependency-plugin as build
  requires to fix the build process (although not sure why that is
  neccessary)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Aug 11 2011 Karel Klíč <kklic@redhat.com> - 3.3-3
- Include the license text in the javadoc package, which is
  independent from the main package
- Use %%add_maven_depmap instead of %%add_to_maven_depmap

* Fri Jul 29 2011 Karel Klíč <kklic@redhat.com> - 3.3-2
- Use %%{_mavenpomdir} instead of %%{_datadir}/maven2/poms
- Removed %%post(un) %%update_maven_depmap calls, not needed in F-15+

* Wed Jun 29 2011 Karel Klíč <kklic@redhat.com> - 3.3-1
- Use maven3 instead of maven2 to build the package.
- Updated to upstream final 3.3 release.

* Thu Apr 28 2011 Karel Klíč <kklic@redhat.com> - 3.3-0.2.git12c0e63
- Added jpackage-utils dependency to -javadoc package (needed for directory)
- Better versioning

* Tue Apr 26 2011 Karel Klíč <kklic@redhat.com> - 3.3-0.1.git12c0e63
- Repackaged to follow Fedora guidelines
- Upstream version 3.2 source code seems not to be available,
  3.3-SNAPSHOT is available in git and seems stable

* Tue Aug 18 2009 Ralph Apel <r.apel@r-apel.de> - 0:3.1-1
- first release

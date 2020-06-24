Name:           plexus-build-api
Version:        0.0.7
Release:        27%{?dist}
Summary:        Plexus Build API
License:        ASL 2.0
URL:            https://github.com/sonatype/sisu-build-api
BuildArch:      noarch

#Fetched from https://github.com/sonatype/sisu-build-api/tarball/plexus-build-api-0.0.7
Source0:        sonatype-sisu-build-api-plexus-build-api-0.0.7-0-g883ea67.tar.gz
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt

# Forwarded upstream: https://github.com/sonatype/sisu-build-api/pull/2
Patch0:         %{name}-migration-to-component-metadata.patch

# Port to plexus-utils 3.3.0 (implement a dummy method)
Patch1:         %{name}-utils-3.3.0.patch

BuildRequires:  maven-local
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:  mvn(org.codehaus.plexus:plexus-container-default)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils) >= 3.3.0

%description
Plexus Build API

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n sonatype-sisu-build-api-f1f8849
cp -p %{SOURCE1} .

%patch0 -p1
%patch1 -p1

# remove unnecessary dependency on parent POM
%pom_remove_parent

%mvn_file : plexus/%{name}

%pom_xpath_remove "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-compiler-plugin']/pom:configuration"

%build
%mvn_build -- -Dmaven.compiler.source=1.6 -Dmaven.compiler.target=1.6

%install
%mvn_install

%files -f .mfiles
%doc LICENSE-2.0.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE-2.0.txt

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.7-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 25 2019 Fabio Valentini <decathorpe@gmail.com> - 0.0.7-26
- Remove unnecessary dependency on parent POM.

* Wed Nov 13 2019 Fabio Valentini <decathorpe@gmail.com> - 0.0.7-25
- Explicitly specify maven compiler source and target versions.

* Thu Oct 17 2019 Fabio Valentini <decathorpe@gmail.com> - 0.0.7-24
- Port to plexus-utils 3.3.0.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.7-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.7-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.7-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.0.7-20
- Escape macros in %%changelog

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.7-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.7-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.7-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.7-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.7-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr  8 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.0.7-14
- Update to current packaging guidelines

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.0.7-12
- Remove BuildRequires on maven-surefire-provider-junit4

* Wed May 21 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.0.7-11
- Use .mfiles generated during build

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.0.7-10
- Use Requires: java-headless rebuild (#1067528)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 0.0.7-7
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Mon Nov 26 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - error: source 0 defined multiple times
- Install license files
- Resolves: rhbz#880200

* Thu Nov 22 2012 Jaromir Capik <jcapik@redhat.com> - 0.0.7-5
- Migration to plexus-containers-container-default

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Nov 04 2011 Jaromir Capik <jcapik@redhat.com> - 0.0.7-2
- Migration from plexus-maven-plugin to plexus-containers-component-metadata

* Tue Aug 2 2011 Alexander Kurtakov <akurtako@redhat.com> 0.0.7-1
- Update to latest upstream version.

* Thu Jun 23 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.0.6-7
- Add spice-parent to Requires

* Fri Jun 3 2011 Alexander Kurtakov <akurtako@redhat.com> 0.0.6-6
- Build with maven.
- Fix requires.
- Guidelines fixes.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed May 26 2010 Hui Wang <huwnag@redhat.com> 0.0.6-3
- Add missing requires

* Wed May 26 2010 Hui Wang <huwnag@redhat.com> 0.0.6-2
- Change JPP-%%{name}.pom to JPP.plexus-%%{name}.pom

* Wed May 19 2010 Hui Wang <huwang@redhat.com> 0.0.6-1
- Initial version of the package

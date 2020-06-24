%global version_url %(echo %{version}|tr . _)

Name:          umlgraph
Version:       5.7.2
Release:       22%{?dist}
Summary:       Automated Drawing of UML Diagrams

License:       BSD
URL:           http://www.spinellis.gr/%{name}
Source0:       https://github.com/dspinellis/%{name}/archive/R%{version_url}.tar.gz#/%{name}-%{version}.tar.gz
# git can not be used for build
Patch0:        %{name}-nogit.patch

BuildRequires: ant
BuildRequires: java-devel

%if 0%{?fedora} 
BuildRequires: javapackages-local
%else # epel
#BuildRequires: javapackages-tools
BuildRequires: maven-local
%endif

# runtime needs dot command
BuildRequires: graphviz
Requires:      graphviz

BuildArch:     noarch

%description
%{name} allows the declarative specification and drawing of UML class
and sequence diagrams. The specification is done in text diagrams, 
that are then transformed into the appropriate graphical representations. 

%package javadoc
Summary:       Javadoc for %{name}

%description javadoc
API documentation for %{name}.


%prep
%setup -q -nUMLGraph-R%{version_url}
%patch0 -p1

find -name Makefile -print -delete
find -name \*.jar -print -delete
rm -rfv legacy

# W: class-path-in-manifest
# http://fedoraproject.org/wiki/Packaging:Java#No_class-path_in_MANIFEST.MF
sed -i /Class-Path/d build.xml

# clean make environment
sed -i 's|\${VERSION}|%{version}|g' build.xml
sed -i -r 's|UmlGraph(.jar)|%{name}\1|g' build.xml

# Configure the installation path
%mvn_file org.%{name}:%{name} %{name}


%build
export JAVA_HOME=%{java_home}
ant pom
# FIXME abrt reports a weird crash in graphviz/dot, rhbz#1281451
ant javadocs
#find javadoc -name \*.dot -delete

%install
# Generated depmap
%mvn_artifact pom.xml lib/%{name}.jar
# Install: jar, depmap, pom, ...
%mvn_install -J javadoc
find %{buildroot}%{_javadocdir}/%{name} -name \*.dot |xargs sed -i -r 's:(/usr)/local:\1:'

%check
export JAVA_HOME=%{java_home}
ant test


%files -f .mfiles
%license LICENSE
%doc README.txt TODO

%files javadoc -f .mfiles-javadoc
%license LICENSE


%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.7.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.7.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.7.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.7.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.7.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.7.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.7.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 01 2017 Raphael Groner <projects.rg@smart.ms> - 5.7.2-15
- bump release

* Tue Dec 13 2016 Raphael Groner <projects.rg@smart.ms> - 5.7.2-14
- rhbz#1402957, fix patch for manifest to not break package functionaility
- drop patch for java7 as epel7 now has java8
- fix E: wrong-script-interpreter

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.7.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 24 2015 Raphael Groner <projects.rg@smart.ms> - 5.7.2-12
- add compatibility with epel7

* Tue Nov 17 2015 Raphael Groner <projects.rg@smart.ms> - 5.7.2-11
- use ant directly, ignore Makefile
- use new style packaging
- fix URL
- ignore legacy folder

* Thu Nov 12 2015 Raphael Groner <projects.rg@smart.ms> - 5.7.2-10
- unretire

* Sat Nov 22 2014 Raphael Groner <projects.rg [AT] smart.ms> - 5.7.2-9
- R5_7_2 (rhbz#1159808)
- release from github
- remove upstreamed jdk8 patch
- remove deprecated Group tags
- license file for subpackage

* Wed Jun 11 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 5.6-8
- Fix FTBFS (#1107031)

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Feb 21 2014 Alexander Kurtakov <akurtako@redhat.com> 5.6-6
- Require java-headless.
- Use autosetup.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jul 23 2012 Alexander Kurtakov <akurtako@redhat.com> 5.6-3
- Do not call git during build.

* Mon Jul 23 2012 Alexander Kurtakov <akurtako@redhat.com> 5.6-2
- BR git.

* Mon Jul 23 2012 Alexander Kurtakov <akurtako@redhat.com> 5.6-1
- New upstream release.

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jan 11 2011 Alexander Kurtakov <akurtako@redhat.com> 5.4-1
- Update to upstream 5.4.

* Thu Oct 8 2009 Alexander Kurtakov <akurtako@redhat.com> 5.2-3
- BR openjdk.

* Wed Oct 7 2009 Alexander Kurtakov <akurtako@redhat.com> 5.2-2
- Add missing BR/R on graphviz.

* Thu Oct 1 2009 Alexander Kurtakov <akurtako@redhat.com> 5.2-1
- Initial package.

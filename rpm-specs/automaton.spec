# Upstream has not made a tarball for the 1.12.2 release, so pull it from git
%global commit      328cf493ec2537af9d2bbce0eb4b4ef118b66547
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           automaton
Version:        1.12.2
Release:        4%{?dist}
Summary:        A Java finite state automata/regular expression library

License:        BSD
URL:            https://www.brics.dk/automaton/
Source0:        https://github.com/cs-au-dk/dk.brics.automaton/archive/%{commit}/%{name}-%{version}.tar.gz
# Fix for javadoc error: tag not supported in the generated HTML version
Patch0:         %{name}-javadoc.patch

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.maven.plugins:maven-javadoc-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.codehaus.mojo:exec-maven-plugin)

BuildArch:      noarch

%description
This Java package contains a DFA/NFA (finite-state automata) implementation
with Unicode alphabet (UTF-16) and support for the standard regular expression
operations (concatenation, union, Kleene star) and a number of non-standard
ones (intersection, complement, etc.).

In contrast to many other automaton/regexp packages, this package is fast,
compact, and implements real, unrestricted regular operations.  It uses a
symbolic representation based on intervals of Unicode characters.

%package javadoc
Summary:        A Java finite state automata/regular expression library
BuildArch:      noarch

%description javadoc
Javadoc documentation for automaton.

%prep
%autosetup -n dk.brics.%{name}-%{commit} -p1

# Remove references to unneeded plugins
%pom_remove_plugin org.sonatype.plugins:nexus-staging-maven-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-gpg-plugin

# Generate code for JDK 8 instead of JDK 6
sed -e 's,>1.6<,>1.8<,g' \
    -e 's,Xdoclint.*,&\n          <source>8</source>,' \
    -i pom.xml

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc ChangeLog README
%license COPYING

%files javadoc -f .mfiles-javadoc

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 13 2020 Jiri Vanek <jvanek@redhat.com> - 1.12.2-3
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 1.12.2-2
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Mon May  4 2020 Jerry James <loganjerry@gmail.com> - 1.12.2-1
- Upgrade to 1.12.2
- Drop the pom source since it is now included in the upstream tarball

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.12r1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.12r1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.12r1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.12r1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.12r1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Jerry James <loganjerry@gmail.com> - 1.12r1-1
- Upgrade to 1.12-1
- Build with maven

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.11r8-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.11r8-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.11r8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11r8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Feb 11 2015 Jerry James <loganjerry@gmail.com> - 1.11r8-10
- Install POM
- Use license macro

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11r8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Mar 27 2014 Jerry James <loganjerry@gmail.com> - 1.11r8-8
- Use upstream versioning in the maven depmap

* Fri Feb 21 2014 Jerry James <loganjerry@gmail.com> - 1.11r8-7
- BR java-headless instead of java (bz 1067974)
- Link with offline Java javadocs
- Minor spec file cleanups

* Mon Jan 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.11r8-6
- Add Maven metadata
- Resolves: rhbz#1052304

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11r8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11r8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11r8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan  6 2012 Jerry James <loganjerry@gmail.com> - 1.11r8-2
- Conform to latest Java guidelines

* Mon Sep 19 2011 Jerry James <loganjerry@gmail.com> - 1.11r8-1
- Upgrade to 1.11-8
- Drop clean at start of %%install and %%defattr
- Update BuildRequires and Requires

* Wed Mar 30 2011 Jerry James <loganjerry@gmail.com> - 1.11r7-1
- Upgrade to 1.11-7

* Mon Mar 21 2011 Jerry James <loganjerry@gmail.com> - 1.11r6-1
- Upgrade to 1.11-6
- Drop %%clean section

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11r5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 17 2011 Jerry James <loganjerry@gmail.com> - 1.11r5-1
- Upgrade to 1.11-5
- BR openjdk to get better javadoc generation

* Tue Nov 23 2010 Jerry James <loganjerry@gmail.com> - 1.11r4-1
- Upgrade to 1.11-4
- Drop the gcj bits
- Drop the BuildRoot definition

* Tue Jul  6 2010 Jerry James <loganjerry@gmail.com> - 1.11r3-1
- Upgrade to 1.11-3

* Mon Aug 17 2009 Jerry James <loganjerry@gmail.com> - 1.11r2-1
- Upgrade to 1.11-2

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11r1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11r1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jan  6 2009 Jerry James <loganjerry@gmail.com> - 1.11r1-1
- Upgrade to 1.11-1

* Fri Sep 12 2008 Jerry James <loganjerry@gmail.com> - 1.10r5-1
- Upgrade to 1.10-5

* Mon Jun 30 2008 Jerry James <loganjerry@gmail.com> - 1.10r4-2
- Conditionalize gcj invocations
- Remove the prebuilt jar before building

* Fri Jun  6 2008 Jerry James <loganjerry@gmail.com> - 1.10r4-1
- Upgrade to 1.10-4

* Fri Apr 18 2008 Jerry James <loganjerry@gmail.com> - 1.10r3-2
- Conform to the new Java packaging guidelines

* Mon Jan  7 2008 Jerry James <loganjerry@gmail.com> - 1.10r3-1
- Fix the version number as suggested by Jason L. Tibbitts III

* Tue Nov 20 2007 Jerry James <loganjerry@gmail.com> - 1.10.3-1
- Initial RPM

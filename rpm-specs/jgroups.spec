%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:          jgroups
Version:       3.6.10
Release:       11%{?dist}
Summary:       Toolkit for reliable multicast communication
License:       ASL 2.0 and LGPLv2+
URL:           http://www.jgroups.org
Source0:       https://github.com/belaban/JGroups/archive/JGroups-%{namedversion}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.logging.log4j:log4j-core)
BuildRequires: mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires: mvn(org.bouncycastle:bcprov-jdk15on)
BuildRequires: mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires: mvn(org.jboss.byteman:byteman-bmunit)
BuildRequires: mvn(org.testng:testng)

BuildArch:     noarch

%description
JGroups is a toolkit for reliable multicast communication. (Note that
this doesn't necessarily mean IP Multicast, JGroups can also use
transports such as TCP). It can be used to create groups of processes
whose members can send messages to each other.

%package  javadoc
Summary:       API documentation for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n JGroups-JGroups-%{namedversion}

find . -name '*.class' -delete
find . -name '*.jar' -delete

%pom_remove_plugin :nexus-staging-maven-plugin
# Useless tasks
%pom_remove_plugin :maven-jar-plugin
%pom_remove_plugin :maven-source-plugin

# Set encoding
%pom_xpath_inject pom:project/pom:properties '
  <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
  <project.reporting.outputEncoding>UTF-8</project.reporting.outputEncoding>'

%pom_change_dep "bouncycastle:bcprov-jdk15" "org.bouncycastle:bcprov-jdk15on:1.52"

chmod 644 README

%build
# A few failed tests:
# DEBUG: Failed tests: 
# DEBUG:   PrioTest.init:40 null
# DEBUG:   BecomeServerTest>BMNGRunner.bmngAfterTest:65->BMNGAbstractRunner.bmngAfterTest:193 ? FileNotFound
# DEBUG:   ForwardToCoordFailoverTest>BMNGRunner.bmngAfterTest:65->BMNGAbstractRunner.bmngAfterTest:193 ? FileNotFound
# DEBUG:   MessageBeforeConnectedTest>BMNGRunner.bmngAfterTest:65->BMNGAbstractRunner.bmngAfterTest:193 ? FileNotFound
# DEBUG:   SequencerFailoverTest>BMNGRunner.bmngAfterTest:65->BMNGAbstractRunner.bmngAfterTest:193 ? FileNotFound
# DEBUG:   TCPGOSSIP_Test.stopRouter:56 NullPointer
# DEBUG:   TUNNELDeadLockTest.tearDown:73 NullPointer
# DEBUG:   TUNNEL_Test.stopRouter:56 NullPointer
# DEBUG: Tests run: 1795, Failures: 8, Errors: 0, Skipped: 1
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc INSTALL.html README
%license LICENSE

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.10-11
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.10-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 3.6.10-9
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jul 09 2016 gil cattaneo <puntogil@libero.it> 3.6.10-1
- update to 3.6.10.Final
- use BRs mvn()-like
- use license macro

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 3.4.2-2
- Use Requires: java-headless rebuild (#1067528)

* Fri Feb 14 2014 Marek Goldmann <mgoldman@redhat.com> - 3.4.2-1
- Upstream release 3.4.2.Final

* Tue Oct 08 2013 Marek Goldmann <mgoldman@redhat.com> - 3.4.0-0.1.Beta1
- Upstream release 3.4.0.Beta1

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 16 2013 Marek Goldmann <mgoldman@redhat.com> - 3.3.2-1
- Upstream release 3.3.2.Final

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 3.0.6-3
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Apr 20 2012 Marek Goldmann <mgoldman@redhat.com> 3.0.6-1
- Upstream release 3.0.6.Final

* Tue Jan 31 2012 Marek Goldmann <mgoldman@redhat.com> - 3.0.4-1
- Upstream release: 3.0.4

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.12.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Aug 18 2011 Marek Goldmann <mgoldman@redhat.com> - 2.12.1.3
- Upstream release: 2.12.1.3
- Moved to Maven

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.9.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Feb 2 2011 mbooth <mbooth@sd.matbooth.co.uk> 2.2.9.2-7
- Drop GCJ support, versioned jars, plus other cleanup.
- No longer requires mx4j (it's included in JDKs >= 1.5).

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:2.2.9.2-6.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:2.2.9.2-5.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jul  9 2008 Deepak Bhole <dbhole@redhat.com> 2.2.9.2-4.6
- Fix bouncycastle classpath

* Wed Jul  9 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0:2.2.9.2-4.5
- drop repotag

* Thu May 29 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0:2.2.9.2-4jpp.4
- fix license tag

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0:2.2.9.2-4jpp.3
- Autorebuild for GCC 4.3

* Thu Sep 27 2007 Jesse Keating <jkeating@redhat.com> - 2.2.9.2-3jpp.3
- Fix the group typo.

* Mon Aug 14 2006 Vivek Lakshmanan <vivekl@redhat.com> - 0:2.2.9.2-3jpp.2
- Keep ENCRYPTAsymmetricTest since BC now available.

* Fri Aug 11 2006 Vivek Lakshmanan <vivekl@redhat.com> - 0:2.2.9.2-3jpp.1
- Resync with latest from JPP.
- Re-enable bouncycastle dependencies.

* Mon Jul 24 2006 Vivek Lakshmanan <vivekl@redhat.com> - 0:2.2.9.2-2jpp_2fc
- Rebuild.

* Sun Jul 23 2006 Vivek Lakshmanan <vivekl@redhat.com> - 0:2.2.9.2-2jpp_1fc
- Merge with latest version from JPP.
- Remove jars from the source tarball.
- Add ant-junit as a build requires.
- Remove tests/junit/org/jgroups/protocols/ENCRYPTAsymmetricTest.java
  temporarily since it needs BouncyCastle.

* Sat Jul 22 2006 Jakub Jelinek <jakub@redhat.com> - 0:2.2.6-1jpp_7fc
- Rebuilt

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 0:2.2.6-1jpp_6fc
- rebuild

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 0:2.2.6-1jpp_5fc
- rebuild

* Mon Mar  6 2006 Jeremy Katz <katzj@redhat.com> - 0:2.2.6-1jpp_4fc
- stop scriptlet spew

* Wed Dec 21 2005 Jesse Keating <jkeating@redhat.com> 0:2.2.6-1jpp_3fc
- rebuilt again

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com> 0:2.2.6-1jpp_2fc
- rebuilt

* Thu Jun 16 2005 Gary Benson <gbenson@redhat.com> 0:2.2.6-1jpp_1fc
- Build into Fedora.

%global gittag 5.8.0.202006091008-r

Name:           eclipse-jgit
Version:        5.8.0
Release:        1%{?dist}
Summary:        Eclipse JGit

# The jgit Eclipse plug-ins are "EDL" licensed, which is equivilent to the new BSD license
License:        BSD
URL:            https://www.eclipse.org/jgit/
Source0:        https://git.eclipse.org/c/jgit/jgit.git/snapshot/jgit-%{gittag}.tar.xz

# Set the correct classpath for the command line tools
Patch0:         0001-Ensure-the-correct-classpath-is-set-for-the-jgit-com.patch
# Switch to feature requirements for third-party bundles, also makes the following changes:
#  javaewah -> com.googlecode.javaewah.JavaEWAH
#  org.slf4j.api -> slf4j.api
#  org.slf4j.impl.log4j12 -> slf4j.simple
Patch1:         0002-Don-t-embed-versions-of-third-party-libs-use-feature.patch

# Remove req on assertj
Patch2:         0003-Remove-requirement-on-assertj-core.patch

BuildArch: noarch

# Upstream Eclipse no longer supports non-64bit arches
ExcludeArch: s390 %{arm} %{ix86}

BuildRequires:  tycho
BuildRequires:  jgit = %{version}

Requires:       eclipse-platform
Requires:       jgit = %{version}

%description
A pure Java implementation of the Git version control system.

%prep
%setup -n jgit-%{gittag} -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

# Disable multithreaded build
rm .mvn/maven.config

# Don't try to get deps from local *maven* repo, use tycho resolved ones
for p in $(find org.eclipse.jgit.packaging -name pom.xml) ; do
  grep -q dependencies $p && %pom_xpath_remove "pom:dependencies" $p
done

# Don't need target platform or repository modules with xmvn
%pom_disable_module org.eclipse.jgit.target org.eclipse.jgit.packaging
%pom_disable_module org.eclipse.jgit.repository org.eclipse.jgit.packaging
%pom_xpath_remove "pom:build/pom:pluginManagement/pom:plugins/pom:plugin/pom:configuration/pom:target" org.eclipse.jgit.packaging/pom.xml

# Don't build source features
%pom_disable_module org.eclipse.jgit.source.feature org.eclipse.jgit.packaging

# Remove unnecessary plugins for RPM builds
%pom_remove_plugin :maven-enforcer-plugin org.eclipse.jgit.packaging

pushd org.eclipse.jgit.packaging
%mvn_package "::pom::" __noinstall
popd

%build
pushd org.eclipse.jgit.packaging
%mvn_build -j
popd

%install
pushd org.eclipse.jgit.packaging
%mvn_install
popd

%files -f org.eclipse.jgit.packaging/.mfiles
%license LICENSE
%doc README.md

%changelog
* Mon Jun 22 2020 Mat Booth <mat.booth@redhat.com> - 5.8.0-1
- Update to latest upstream release

* Sun Mar 22 2020 Mat Booth <mat.booth@redhat.com> - 5.7.0-1
- Update to latest upstream release

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 19 2019 Mat Booth <mat.booth@redhat.com> - 5.6.0-1
- Update to latest upstream release

* Tue Sep 17 2019 Mat Booth <mat.booth@redhat.com> - 5.5.0-1
- Update to latest upstream release

* Thu Jul 25 2019 Mat Booth <mat.booth@redhat.com> - 5.4.0-4
- Move the core jgit library out into a separate package, allows us to simplify
  this package tremendously; see https://pagure.io/stewardship-sig/issue/13 and
  rhbz#1732894 for details

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 27 2019 Mat Booth <mat.booth@redhat.com> - 5.4.0-2
- Fix jgit command line launching script

* Thu Jun 27 2019 Mat Booth <mat.booth@redhat.com> - 5.4.0-1
- Update to final tagged release

* Fri May 31 2019 Mat Booth <mat.booth@redhat.com> - 5.4.0-0.1
- Update to latest milestone release

* Fri Apr 19 2019 Mat Booth <mat.booth@redhat.com> - 5.3.0-6
- Allowing conditional build of eclipse features without being in 'bootstrap'
  mode

* Tue Mar 19 2019 Mat Booth <mat.booth@redhat.com> - 5.3.0-5
- Disable incomplete source feature

* Sat Mar 16 2019 Mat Booth <mat.booth@redhat.com> - 5.3.0-4
- Rebuild to regenerate symlinks

* Sat Mar 16 2019 Mat Booth <mat.booth@redhat.com> - 5.3.0-3
- Rebuild against apache sshd 2

* Wed Mar 13 2019 Mat Booth <mat.booth@redhat.com> - 5.3.0-2
- Rebuild to regenerate symlinks

* Wed Mar 13 2019 Mat Booth <mat.booth@redhat.com> - 5.3.0-1
- Update to 2019-03 release

* Wed Mar 13 2019 Mat Booth <mat.booth@redhat.com> - 5.3.0-0.5
- Full build

* Wed Mar 13 2019 Mat Booth <mat.booth@redhat.com> - 5.3.0-0.4
- Improved feature versions patch
- Skip hanging tests

* Wed Mar 13 2019 Mat Booth <mat.booth@redhat.com> - 5.3.0-0.3
- Restrict to same architectures as Eclipse itself

* Tue Mar 12 2019 Mat Booth <mat.booth@redhat.com> - 5.3.0-0.2
- Update to 2019-03 RC1 release

* Tue Feb 26 2019 Mat Booth <mat.booth@redhat.com> - 5.3.0-0.1
- Update to latest milestone build

* Mon Feb 11 2019 Todd Zullinger <tmz@pobox.com> - 5.2.0-5
- Add javapackages-tools requires to jgit for /usr/bin/build-classpath

* Thu Feb 07 2019 Mat Booth <mat.booth@redhat.com> - 5.2.0-4
- Add missing requires for optional dep on bouncycastle

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Dec 07 2018 Mat Booth <mat.booth@redhat.com> - 5.2.0-2
- Full rebuild

* Fri Dec 07 2018 Mat Booth <mat.booth@redhat.com> - 5.2.0-1
- Update to 5.2.0 release
- Port to apache-sshd 2.1.0

* Tue Sep 25 2018 Mat Booth <mat.booth@redhat.com> - 5.1.1-2
- Full build

* Mon Sep 24 2018 Mat Booth <mat.booth@redhat.com> - 5.1.1-1
- Update to 5.1.1 release

* Wed Aug 22 2018 Mat Booth <mat.booth@redhat.com> - 5.1.0-0.2
- Full build

* Wed Aug 22 2018 Mat Booth <mat.booth@redhat.com> - 5.1.0-0.1
- Update to latest snapshot

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 22 2018 Mat Booth <mat.booth@redhat.com> - 5.0.1-1
- Update to latest upstream release

* Wed Mar 21 2018 Alexander Kurtakov <akurtako@redhat.com> 4.11.0-2
- Full build.

* Tue Mar 20 2018 nickboldt <nboldt@redhat.com> - 4.11.0-1
- Update to latest upstream release 4.11.0

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 05 2018 Mat Booth <mat.booth@redhat.com> - 4.10.0-2
- Rebuild to generate Eclipse features

* Fri Jan 05 2018 Mat Booth <mat.booth@redhat.com> - 4.10.0-1
- Update to latest upstream release

* Fri Dec 15 2017 Mat Booth <mat.booth@redhat.com> - 4.9.1-2
- Rebuild to generate Eclipse features

* Fri Dec 15 2017 Mat Booth <mat.booth@redhat.com> - 4.9.1-1
- Update to latest release
- Bootstrap mode

* Tue Nov 21 2017 Mat Booth <mat.booth@redhat.com> - 4.9.0-2
- Rebuild to generate Eclipse features

* Tue Nov 21 2017 Mat Booth <mat.booth@redhat.com> - 4.9.0-1
- Update to latest upstream version
- Allow bootstrap build to work without tycho/eclipse

* Mon Jul 31 2017 Mat Booth <mat.booth@redhat.com> - 4.8.0-4
- Add requires on eclipse-platform to the subpackage that contains the Eclipse
  features

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 15 2017 Mat Booth <mat.booth@redhat.com> - 4.8.0-2
- Rebuild to regenerate symlinks
- Add missing BR on jetty-continuation

* Thu Jun 15 2017 Mat Booth <mat.booth@redhat.com> - 4.8.0-1
- Update to Oxygen release

* Tue May 30 2017 Mikolaj Izdebski <mizdebsk@redhat.com> - 4.7.0-8
- Add missing build-requires on maven-install-plugin

* Tue May 23 2017 Mat Booth <mat.booth@redhat.com> - 4.7.0-7
- Fix NCDFE when doing jgit clone over http, resolves: rhbz#1454585

* Fri May 12 2017 Mat Booth <mat.booth@redhat.com> - 4.7.0-6
- Allow using jgit from ant tasks

* Wed May 10 2017 Mat Booth <mat.booth@redhat.com> - 4.7.0-5
- Full build once again
- Don't package tests with main artifacts
- Enable test suite at build-time

* Wed May 10 2017 Mat Booth <mat.booth@redhat.com> - 4.7.0-4
- Rebuild for new javaewah
- Temporarily disable features

* Thu May 04 2017 Mat Booth <mat.booth@redhat.com> - 4.7.0-3
- Re-enable jetty-using features

* Wed May 03 2017 Mat Booth <mat.booth@redhat.com> - 4.7.0-2
- Temporarily disable features that use jetty

* Mon Apr 10 2017 nboldt <nickboldt+redhat@gmail.com> - 4.7.0-1
- Update to jgit 4.7

* Mon Mar 27 2017 Nick Boldt <nboldt@redhat.com> - 4.6.1-1
- Update to Neon.3 release version; remove jetty 9.4.0 patch

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 05 2017 Mat Booth <mat.booth@redhat.com> - 4.6.0-2
- Bump to rebuild symlinks

* Wed Jan 04 2017 Mat Booth <mat.booth@redhat.com> - 4.6.0-1
- Update to latest release

* Tue Oct 4 2016 Alexander Kurtakov <akurtako@redhat.com> 4.5.0-2
- Remove no longer needed patch.

* Tue Oct 4 2016 Alexander Kurtakov <akurtako@redhat.com> 4.5.0-1
- Update to upstream 4.5.0 release.

* Wed Aug 03 2016 Sopot Cela <scela@redhat.com> - 4.4.1-1
- Upgrade to 4.4.1

* Fri Jul 01 2016 Mat Booth <mat.booth@redhat.com> - 4.4.0-4
- Fix IllegalStateException when starting git daemon from the command line

* Wed Jun 15 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 4.4.0-3
- Add missing build-requires

* Mon Jun 13 2016 Mat Booth <mat.booth@redhat.com> - 4.4.0-2
- Rebuild to regenerate symlinks

* Mon Jun 13 2016 Mat Booth <mat.booth@redhat.com> - 4.4.0-1
- Update to latest release

* Mon May 02 2016 Mat Booth <mat.booth@redhat.com> - 4.3.0-2
- Avoid embedding versions of external deps in features. This avoids the need to
  rebuild when a dependency changes version.

* Fri Apr 15 2016 Sopot Cela <scela@redhat.com> - 4.3.0-1
- Upgrade to 4.3.0

* Wed Apr  6 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 4.2.0-9
- Rebuild for slf4j 1.7.21

* Wed Mar 30 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 4.2.0-8
- Rebuild for slf4j 1.7.20

* Thu Mar 24 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 4.2.0-7
- Rebuild for slf4j 1.7.19

* Mon Feb 29 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 4.2.0-6
- Rebuild for slf4j 1.7.18

* Mon Feb 22 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 4.2.0-5
- Rebuild for slf4j 1.7.17

* Wed Feb 17 2016 Alexander Kurtakov <akurtako@redhat.com> 4.2.0-4
- Rebuild for latest slf4j.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 25 2016 Mat Booth <mat.booth@redhat.com> - 4.2.0-2
- Rebuilt to generate symlinks

* Fri Jan 22 2016 Mat Booth <mat.booth@redhat.com> - 4.2.0-1
- Update to latest upstream release
- Add patch for latest version of jetty

* Tue Dec 08 2015 Mat Booth <mat.booth@redhat.com> - 4.1.1-2
- Rebuild to re-generate symlinks

* Tue Dec 08 2015 Mat Booth <mat.booth@redhat.com> - 4.1.1-1
- Update to latest upstream release

* Sun Nov 29 2015 Mat Booth <mat.booth@redhat.com> - 4.1.0-6
- Fix a problem with command line "jgit daemon" invocation
- This should also fix rhbz#1228138

* Mon Nov 16 2015 Alexander Kurtakov <akurtako@redhat.com> 4.1.0-5
- Rebuild for latest slf4j.

* Mon Oct 12 2015 Mat Booth <mat.booth@redhat.com> - 4.1.0-4
- Drop R on slf4j.

* Thu Oct 08 2015 Roland Grunberg <rgrunber@redhat.com> - 4.1.0-3
- Use slf4j.simple instead of slf4j.log4j12.

* Wed Sep 30 2015 Mat Booth <mat.booth@redhat.com> - 4.1.0-2
- Regenerate symlinks

* Tue Sep 29 2015 Mat Booth <mat.booth@redhat.com> - 4.1.0-1
- Update to 4.1.0

* Mon Sep 14 2015 Roland Grunberg <rgrunber@redhat.com> - 4.0.1-5
- Rebuild as an Eclipse p2 Droplet.

* Tue Jul  7 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 4.0.1-4
- Relax version restriction for args4j

* Tue Jun 30 2015 Mat Booth <mat.booth@redhat.com> - 4.0.1-3
- Does not require eclipse-platform, only eclipse-filesystem
- Drop incomplete SCL macros

* Wed Jun 24 2015 Alexander Kurtakov <akurtako@redhat.com> 4.0.1-2
- Rebuild to fix symlinks.

* Wed Jun 24 2015 Alexander Kurtakov <akurtako@redhat.com> 4.0.1-1
- Update to 4.0.1.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 10 2015 Alexander Kurtakov <akurtako@redhat.com> 4.0.0-2
- Rebuild to fix symlinks.

* Tue Jun 9 2015 Alexander Kurtakov <akurtako@redhat.com> 4.0.0-1
- Update to 4.0 final.

* Mon Jun 1 2015 Alexander Kurtakov <akurtako@redhat.com> 4.0.0-0.2.rc2
- Switch to xz tarball.

* Wed May 27 2015 Alexander Kurtakov <akurtako@redhat.com> 4.0.0-0.1.rc2
- Update to 4.0 rc2.

* Thu May 14 2015 Alexander Kurtakov <akurtako@redhat.com> 3.7.1-1
- Update to 3.7.1 release.

* Mon Mar 02 2015 Roland Grunberg <rgrunber@redhat.com> - 3.7.0-2
- Manually add slf4j-log4j12 requires.

* Mon Mar 02 2015 Roland Grunberg <rgrunber@redhat.com> - 3.7.0-1
- Update to upstream 3.7.0.

* Fri Jan 23 2015 Roland Grunberg <rgrunber@redhat.com> - 3.6.2-2
- Use Equinox's OSGi runtime instead of Felix's.

* Fri Jan 23 2015 Alexander Kurtakov <akurtako@redhat.com> 3.6.2-1
- Update to upstream 3.6.2.

* Mon Jan 5 2015 Alexander Kurtakov <akurtako@redhat.com> 3.6.1-1
- Update to upstream 3.6.1.

* Fri Dec 19 2014 Alexander Kurtakov <akurtako@redhat.com> 3.5.3-1
- Update to upstream 3.5.3 release.

* Thu Dec 18 2014 Alexander Kurtakov <akurtako@redhat.com> 3.5.2-1
- Update to upstream 3.5.2 release.

* Tue Nov 11 2014 Mat Booth <mat.booth@redhat.com> - 3.5.0-3
- Rebuild to generate correct symlinks
- Drop unnecessary requires (now autogenerated by xmvn)

* Fri Nov 07 2014 Mat Booth <mat.booth@redhat.com> - 3.5.0-2
- Build/install eclipse plugin with mvn_build/mvn_install

* Fri Oct 03 2014 Mat Booth <mat.booth@redhat.com> - 3.5.0-1
- Update to latest upstream release 3.5.0

* Thu Jun 26 2014 Mat Booth <mat.booth@redhat.com> - 3.4.1-1
- Update to latest upstream release 3.4.1
- Drop unnecessary BRs

* Fri Jun 13 2014 Alexander Kurtakov <akurtako@redhat.com> 3.4.0-1
- Update to upstream 3.4.0.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 30 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.3.2-5
- Use .mfiles geterated during build

* Fri May 30 2014 Alexander Kurtakov <akurtako@redhat.com> 3.3.2-4
- Add missing Rs ( rhbz #1079706 ).

* Wed May 28 2014 Alexander Kurtakov <akurtako@redhat.com> 3.3.2-3
- Rebuild for latest commons-compress.

* Wed May 21 2014 Alexander Kurtakov <akurtako@redhat.com> 3.3.2-2
- Fix compile against latest args4j.

* Fri Apr 25 2014 Alexander Kurtakov <akurtako@redhat.com> 3.3.2-1
- Update to 3.3.2.

* Mon Mar 31 2014 Alexander Kurtakov <akurtako@redhat.com> 3.3.1-2
- Remove bundled commons-compress.

* Fri Mar 28 2014 Alexander Kurtakov <akurtako@redhat.com> 3.3.1-1
- Update to 3.3.1.

* Tue Mar 11 2014 Alexander Kurtakov <akurtako@redhat.com> 3.3.0-1
- Update to 3.3.0.

* Sun Dec 29 2013 Alexander Kurtakov <akurtako@redhat.com> 3.2.0-1
- Update to 3.2.0.

* Thu Oct 3 2013 Krzysztof Daniel <kdaniel@redhat.com> 3.1.0-1
- Update to Kepler SR1.

* Mon Aug 5 2013 Krzysztof Daniel <kdaniel@redhat.com> 3.0.0-7
- Add missing jgit plugin back.

* Tue Jul 16 2013 Krzysztof Daniel <kdaniel@redhat.com> 3.0.0-6
- Change the build system to mvn-rpmbuild.
- Use feclipse-maven-plugin to install things.
- Bug 413163 - Incompatible change in latest args4j: multiValued removed from @Option

* Fri Jul 5 2013 Neil Brian Guzman <nguzman@redhat.com> 3.0.0-5
- Bump release

* Tue Jun 25 2013 Neil Brian Guzman <nguzman@redhat.com> 3.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jun 25 2013 Krzysztof Daniel <kdaniel@redhat.com> 3.0.0-3
- Add missing R: javaewah to eclipse-jgit.

* Tue Jun 25 2013 Krzysztof Daniel <kdaniel@redhat.com> 3.0.0-2
- Move symlinks to eclipse-jgit.
- Fix jgit classpath.

* Thu Jun 20 2013 Neil Brian Guzman <nguzman@redhat.com> 3.0.0-1
- Update to 3.0.0 release

* Tue May 14 2013 Krzysztof Daniel <kdaniel@redhat.com> 2.3.1-2
- Rebuild with latest icu4j.

* Thu Feb 21 2013 Roland Grunberg <rgrunber@redhat.com> - 2.3.1-1
- SCL-ize package.

* Thu Feb 21 2013 Roland Grunberg <rgrunber@redhat.com> - 2.3.1-1
- Update to 2.3.1 release.

* Thu Feb 14 2013 Roland Grunberg <rgrunber@redhat.com> - 2.2.0-3
- jgit subpackage should own its symlinked dependencies.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jan 3 2013 Krzysztof Daniel <kdaniel@redhat.com> 2.2.0-1
- Update to 2.2.0 release.

* Mon Oct 1 2012 Alexander Kurtakov <akurtako@redhat.com> 2.1.0-1
- Update to 2.1.0 release.

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 2 2012 Alexander Kurtakov <akurtako@redhat.com> 2.0.0-1
- Update to 2.0.0 upstream release.

* Fri Apr 27 2012 Severin Gehwolf <sgehwolf@redhat.com> 1.3.0-3
- Use eclipse-pdebuild over old pdebuild script.

* Thu Apr 26 2012 Severin Gehwolf <sgehwolf@redhat.com> 1.3.0-2
- Tweak .spec so as to avoid modifying to much of the .spec file
- Fix upstream 1.3 release sources.

* Fri Feb 17 2012 Andrew Robinson <arobinso@redhat.com> 1.3.0-1
- Update to 1.3.0 upstream release.

* Thu Jan 5 2012 Alexander Kurtakov <akurtako@redhat.com> 1.2.0-2
- Build eclipse plugin first to not interfere with maven artifacts.

* Thu Jan 5 2012 Alexander Kurtakov <akurtako@redhat.com> 1.2.0-1
- Update to 1.2.0 release.

* Fri Oct 28 2011 Andrew Robinson <arobinso@redhat.com> 1.1.0-4
- Add jsch jar to the classpath.

* Fri Oct 28 2011 Alexander Kurtakov <akurtako@redhat.com> 1.1.0-3
- Drop libs subpackage and use the sh script directly instead of the shaded executable.
- Install jars in _javadir subdir as per guidelines.

* Thu Oct 27 2011 Andrew Robinson <arobinso@redhat.com> 1.1.0-2
- Added Java libraries, javadocs and console binary subpackages.

* Fri Sep 23 2011 Andrew Robinson <arobinso@redhat.com> 1.1.0-1
- Update to upstream release 1.1.0.

* Tue Jun 14 2011 Chris Aniszczyk <zx@redhat.com> 1.0.0-2
- Update to upstream release 1.0.0.201106090707-r.

* Tue Jun 07 2011 Chris Aniszczyk <zx@redhat.com> 1.0.0-1
- Update to upstream release 1.0.0.

* Tue May 03 2011 Chris Aniszczyk <zx@redhat.com> 0.12.1-1
- Update to upstream release 0.12.1.

* Tue Feb 22 2011 Chris Aniszczyk <zx@redhat.com> 0.11.3-1
- Update to upstream release 0.11.3.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 22 2010 Chris Aniszczyk <zx@redhat.com> 0.10.1-1
- Update to upstream release 0.10.1.

* Thu Oct 7 2010 Chris Aniszczyk <zx@redhat.com> 0.9.3-1
- Update to upstream release 0.9.3.

* Wed Sep 15 2010 Severin Gehwolf <sgehwolf@redhat.com> 0.9.1-1
- Update to upstream release 0.9.1.

* Thu Aug 26 2010 Severin Gehwolf <sgehwolf at, redhat.com> 0.9.0-0.1.20100825git
- Make release tag more readable (separate "0.1" and pre-release tag by ".").

* Wed Aug 25 2010 Severin Gehwolf <sgehwolf at, redhat.com> 0.9.0-0.120100825git
- Pre-release version of JGit 0.9.0

* Fri Jun 25 2010 Severin Gehwolf <sgehwolf at, redhat.com> 0.8.4-2
- Increase release number to make tagging work.

* Wed Jun 23 2010 Severin Gehwolf <sgehwolf at, redhat.com> 0.8.4-1
- Rebase to 0.8.4 release.

* Mon Apr 12 2010 Jeff Johnston <jjohnstn@redhat.com> 0.7.1-1
- Rebase to 0.7.1 release.

* Tue Feb 9 2010 Alexander Kurtakov <akurtako@redhat.com> 0.6.0-0.1.git20100208
- New git snapshot.

* Thu Nov 5 2009 Alexander Kurtakov <akurtako@redhat.com> 0.6.0-0.1.git20091029
- Correct release.

* Thu Oct 29 2009 Alexander Kurtakov <akurtako@redhat.com> 0.6.0-0.git20091029.1
- Initial package

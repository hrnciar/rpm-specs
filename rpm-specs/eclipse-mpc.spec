%global mpc_repo_tag afa59f5940eca87d3eb2c7472b905115af7d1f57
%global uss_repo_tag 39ddd657b518213cb0631c4f02893db96454da34

Name:           eclipse-mpc
Version:        1.8.3
Release:        2%{?dist}
Summary:        Eclipse Marketplace Client

License:        EPL-2.0
URL:            http://www.eclipse.org/mpc/
Source0:        http://git.eclipse.org/c/mpc/org.eclipse.epp.mpc.git/snapshot/org.eclipse.epp.mpc-%{mpc_repo_tag}.tar.xz

# This could be broken out into a separate srpm if something else requires it in the future
Source1:        http://git.eclipse.org/c/usssdk/org.eclipse.usssdk.git/snapshot/org.eclipse.usssdk-%{uss_repo_tag}.tar.xz

BuildArch: noarch

# Upstream Eclipse no longer supports non-64bit arches
ExcludeArch: s390 %{arm} %{ix86}

BuildRequires: eclipse-pde
BuildRequires: eclipse-p2-discovery
BuildRequires: tycho
BuildRequires: tycho-extras
BuildRequires: maven-plugin-build-helper
BuildRequires: eclipse-license2
BuildRequires: httpcomponents-client
Requires: eclipse-platform
Requires: eclipse-p2-discovery

%description
The Eclipse Marketplace Client provides access to extension catalogs.

%prep
%setup -q -n org.eclipse.epp.mpc-%{mpc_repo_tag}

# Add USS plug-ins to the build
tar --strip-components=1 -xf %{SOURCE1} org.eclipse.usssdk-%{uss_repo_tag}/org.eclipse.userstorage{,.ui,.oauth,-feature}
%pom_xpath_inject "pom:modules" "<module>org.eclipse.userstorage</module><module>org.eclipse.userstorage.ui</module><module>org.eclipse.userstorage.oauth</module><module>org.eclipse.userstorage-feature</module>"
for b in org.eclipse.userstorage{,.ui,.oauth,-feature} ; do
%pom_set_parent "org.eclipse.epp.mpc:org.eclipse.epp.mpc-bundle:%{version}-SNAPSHOT" $b
%pom_xpath_inject "pom:parent" "<relativePath>../org.eclipse.epp.mpc-parent/bundle</relativePath>" $b
done
sed -i -e '/license-feature-version/s/2\.0\.2\.v20181016-2210/0.0.0/' org.eclipse.userstorage-feature/feature.xml
sed -i -e '/license-feature-version/s/2\.0\.2/0.0.0/' org.eclipse.epp.mpc.feature/feature.xml

# PMD and findbugs is unnecessary to the build
%pom_remove_plugin org.apache.maven.plugins:maven-pmd-plugin org.eclipse.epp.mpc-parent
%pom_remove_plugin org.apache.maven.plugins:maven-pmd-plugin org.eclipse.epp.mpc-parent/bundle
%pom_remove_plugin :spotbugs-maven-plugin org.eclipse.epp.mpc-parent
%pom_remove_plugin :spotbugs-maven-plugin org.eclipse.epp.mpc-parent/bundle
%pom_remove_plugin :maven-enforcer-plugin org.eclipse.epp.mpc-parent

# Remove bundles that are not applicable to Linux
%pom_disable_module org.eclipse.epp.mpc.core.win32
%pom_xpath_remove "feature/plugin[@id='org.eclipse.epp.mpc.core.win32']" org.eclipse.epp.mpc.feature/feature.xml

# Don't need to build update sites or target platforms for RPM builds
%pom_disable_module org.eclipse.epp.mpc.site
%pom_disable_module org.eclipse.epp.mpc-target
%pom_remove_plugin org.eclipse.tycho:target-platform-configuration org.eclipse.epp.mpc-parent/pom.xml

%pom_xpath_remove "pom:build/pom:pluginManagement/pom:plugins/pom:plugin[pom:artifactId='tycho-packaging-plugin']" org.eclipse.epp.mpc-parent/pom.xml
%pom_disable_module org.eclipse.epp.mpc.tests
%pom_disable_module org.eclipse.epp.mpc.tests.catalog
%pom_disable_module org.eclipse.epp.mpc.dependencies.feature

# Non-strict compiler checking
sed -i -e '/strictCompilerTarget/d' org.eclipse.epp.mpc-parent/pom.xml

%mvn_package "::pom::" __noinstall
%mvn_package "::jar:sources{,-feature}:"

%build
# Qualifier generated from last modification time of source tarball
QUALIFIER=$(date -u -d"$(stat --format=%y %{SOURCE0})" +v%Y%m%d-%H%M)
%mvn_build -j -f -- -DforceContextQualifier=$QUALIFIER

%install
%mvn_install

%files -f .mfiles

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 22 2020 Mat Booth <mat.booth@redhat.com> - 1.8.3-1
- Update to latest upstream release

* Sun Mar 22 2020 Mat Booth <mat.booth@redhat.com> - 1.8.2-1
- Update to latest upstream release
- Remove useless dep on maven-enforcer

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 19 2019 Mat Booth <mat.booth@redhat.com> - 1.8.1-1
- Update to latest upstream release

* Mon Sep 16 2019 Mat Booth <mat.booth@redhat.com> - 1.8.0-1
- Update to latest upstream release

* Tue Jun 11 2019 Mat Booth <mat.booth@redhat.com> - 1.7.7-1
- Update to latest upstream release

* Fri Mar 15 2019 Mat Booth <mat.booth@redhat.com> - 1.7.5-2
- Fix widget is disposed error on start up

* Wed Mar 13 2019 Mat Booth <mat.booth@redhat.com> - 1.7.5-1
- Update to 2019-03 release
- Restrict to same architectures as Eclipse itself
- Don't package common license feature

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Dec 07 2018 Mat Booth <mat.booth@redhat.com> - 1.7.3-1
- Update for 2018-12 release

* Wed Aug 22 2018 Mat Booth <mat.booth@redhat.com> - 1.7.2-1
- Update to latest release

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 12 2018 Mat Booth <mat.booth@redhat.com> - 1.7.0-1
- Update to Photon release

* Tue Mar 20 2018 Mat Booth <mat.booth@redhat.com> - 1.6.4-1
- Update to latest release

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Oct 02 2017 Mat Booth <mat.booth@redhat.com> - 1.6.2-1
- Update to Oxygen.1a release

* Sun Sep 17 2017 Mat Booth <mat.booth@redhat.com> - 1.6.1-1
- Update to Oxygen.1 release

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-0.4.gitfce01a1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 22 2017 Mat Booth <mat.booth@redhat.com> - 1.6.0-0.3.gitfce01a1
- Correct typo in qualifier

* Thu Jun 22 2017 Mat Booth <mat.booth@redhat.com> - 1.6.0-0.2.gitfce01a1
- Update to latest Oxygen snapshot

* Mon May 08 2017 Mat Booth <mat.booth@redhat.com> - 1.6.0-0.1
- Update to Oxygen compatibile snapshot

* Wed Mar 29 2017 Mat Booth <mat.booth@redhat.com> - 1.5.4-1
- Update to latest upstream version

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 11 2017 Mat Booth <mat.booth@redhat.com> - 1.5.3-1
- Update to latest release

* Thu Oct 13 2016 Mat Booth <mat.booth@redhat.com> - 1.5.2-1
- Update to 1.5.2 for Neon.1a

* Tue Oct 04 2016 Mat Booth <mat.booth@redhat.com> - 1.5.1-1
- Update to Neon.1 version

* Mon Aug 01 2016 Mat Booth <mat.booth@redhat.com> - 1.5.0-3
- Drop usage of PMD plugin

* Mon Jul 11 2016 Mat Booth <mat.booth@redhat.com> - 1.5.0-2
- Add missing BR

* Mon Jul 11 2016 Mat Booth <mat.booth@redhat.com> - 1.5.0-1
- Update to neon release

* Wed Jun 15 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4.2-2
- Add missing build-requires

* Wed Mar 09 2016 Mat Booth <mat.booth@redhat.com> - 1.4.2-1
- Update to Mars.2 release

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Oct 05 2015 Mat Booth <mat.booth@redhat.com> - 1.4.1-1
- Update to Mars.1 release

* Mon Sep 14 2015 Roland Grunberg <rgrunber@redhat.com> - 1.4.0-2
- Rebuild as an Eclipse p2 Droplet.

* Thu Jul 2 2015 Alexander Kurtakov <akurtako@redhat.com> 1.4.0-1
- Update to upstream 1.4.0 release.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Mar 06 2015 Mat Booth <mat.booth@redhat.com> - 1.3.2-1
- Update to Luna SR2 release

* Fri Feb  6 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3.1-5
- Rebuild to generate missing OSGi auto-requires

* Tue Jan 20 2015 Mat Booth <mat.booth@redhat.com> - 1.3.1-4
- Make direct hamcrest use explicit in manifest

* Wed Dec 3 2014 Alexander Kurtakov <akurtako@redhat.com> 1.3.1-3
- Build with xmvn.

* Fri Nov 7 2014 Alexander Kurtakov <akurtako@redhat.com> 1.3.1-2
- Prepend v to qualifier to make update center not proposing updates.

* Tue Oct 07 2014 Roland Grunberg <rgrunber@redhat.com> - 1.3.1-1
- Update to upstream 1.3.1 release.

* Mon Oct 06 2014 Roland Grunberg <rgrunber@redhat.com> - 1.3.0-2
- Make org.eclipse.epp.mpc.core a singleton bundle.
- Resolves: rhbz#1149469

* Thu Sep 11 2014 Alexander Kurtakov <akurtako@redhat.com> 1.3.0-1
- Update to upstream 1.3.0 release.

* Thu Sep 4 2014 Alexander Kurtakov <akurtako@redhat.com> 1.2.2-1
- Update to official 1.2.2 release.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-0.2.git519e70b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Nov 11 2013 Alexander Kurtakov <akurtako@redhat.com> 1.2.1-0.1.git519e70b
- This is gonna be version 1.2.1.

* Tue Oct 1 2013 Krzysztof Daniel <kdaniel@redhat.com> 1.1.2-0.6.git7feb49
- Fix the build (remove jgit timestamp provider).

* Tue Oct 1 2013 Krzysztof Daniel <kdaniel@redhat.com> 1.1.2-0.4.git7feb49
- Update to latest upstream.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-0.4.git00b427
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jun 20 2013 Krzysztof Daniel <kdaniel@redhat.com> 1.1.2-0.3.git00b427
- Update to latest upstream (likely Kepler, but not tagged yet).

* Tue May 7 2013 Krzysztof Daniel <kdaniel@redhat.com> 1.1.2-0.2.gitb114a5
- Tranistion to tycho build. 

* Mon May 6 2013 Krzysztof Daniel <kdaniel@redhat.com> 1.1.2-0.1.gitb114a5
- Update to latest upstream.

* Thu Feb 14 2013 Krzysztof Daniel <kdaniel@redhat.com> 1.1.1-4
- Fix the build.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Feb 10 2012 Alexander Kurtakov <akurtako@redhat.com> 1.1.1-1
- Update to upstream 1.1.1 release.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jul 13 2011 Alexander Kurtakov <akurtako@redhat.com> 1.1.0-2
- Use upstream sources.
- Adapt to current guidelines.

* Thu Jun 02 2011 Chris Aniszczyk <zx@redhat.com> 1.1.0-1
- Updating to the 1.1.0 release

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Sep 9 2010 Chris Aniszczyk <zx@redhat.com> 1.0.1-1
- Initial packaging

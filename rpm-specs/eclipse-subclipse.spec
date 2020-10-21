# Conditionally build svnkit/javahl support; we build javahl support by default becuase it's rock solid
# Otherwise fallback to svnkit where subversion is not present or not new enough
%bcond_without javahl

Name:           eclipse-subclipse
Version:        4.3.0
Release:        8%{?dist}
Summary:        Subversion Eclipse plugin

# The svnclientadaptor layer is Apache licensed
# The actual Subclipse plugins are Eclipse licensed
License:        EPL-1.0 and ASL 2.0
URL:            https://github.com/subclipse/subclipse/wiki

%global svnclientadapter_version 1.14.0
%global javahl_version 1.14.0
%global svnkit_version 1:1.8.12

%global subclipse_tag %{version}
%global svnclientadapter_tag fd5bd3587c578ef76df75d8021424b4c1306459c
%global javahl_tag %{javahl_version}

Source0:        https://github.com/subclipse/subclipse/archive/%{subclipse_tag}/subclipse-%{version}.tar.gz
# Upstream moved the svnclientadapter into a separate repo which could be packaged separately if needed
Source1:        https://github.com/subclipse/svnclientadapter/archive/%{svnclientadapter_tag}/svnclientadapter-%{svnclientadapter_version}.tar.gz
# Upstream moved the javahl fragments into a separate repo which could be packaged separately if needed
Source2:        https://github.com/subclipse/javahl-windows/archive/%{javahl_tag}/javahl-windows-%{javahl_version}.tar.gz

Source3:        eclipse-subclipse.metainfo.xml

# Allow building against Fedora's svnkit
# TODO fix this properly when deps are properly OSGified
Patch1:         svnkit.patch

BuildArch:      noarch

# Upstream Eclipse no longer supports non-64bit arches
ExcludeArch: s390 %{arm} %{ix86}

BuildRequires:  tycho
BuildRequires:  tycho-extras
BuildRequires:  maven-install-plugin
BuildRequires:  eclipse-gef
BuildRequires:  libappstream-glib
%if %{with javahl}
BuildRequires:  subversion-javahl >= 1.12.0
Requires:       subversion-javahl >= 1.12.0
%endif
BuildRequires:  svnkit-javahl >= %{svnkit_version}
Requires:       svnkit-javahl >= %{svnkit_version}

%description
Subclipse is an Eclipse plugin that adds Subversion integration to the Eclipse
IDE.

%prep
%setup -q -n subclipse-%{subclipse_tag} -a 1
%patch1

# Fix pom xml declarations
# PR sent upstream here: https://github.com/subclipse/subclipse/pull/138
sed -i -e 's/4\.2\.0/4.0.0/g' {.,features,bundles}/pom.xml

cp -p svnclientadapter-%{svnclientadapter_tag}/LICENSE.md LICENSE-apache.md

# Insert Javahl features/bundles into build
tar xf %{SOURCE2} --strip-components=1 javahl-windows-%{javahl_version}/{releng/javahl.configuration,features/feature.javahl,bundles/svnapi.javahl}
%pom_xpath_inject "pom:modules" "<module>feature.javahl</module>" features
%pom_xpath_inject "pom:modules" "<module>svnapi.javahl</module>" bundles
%pom_xpath_remove "feature/plugin[@os='win32']" features/feature.javahl/feature.xml

# Delete pre-built artifacts
find -name '*.jar' -delete

# Don't need to build update site
%pom_disable_module releng

# Dont't ship source jars
%pom_remove_plugin :maven-source-plugin svnclientadapter*

%if %{without javahl}
# Don't build javahl
%pom_disable_module feature.javahl features
%pom_disable_module svnapi.javahl bundles
%pom_change_dep "org.apache.subversion:javahl" "org.tmatesoft.svnkit:svnkit-javahl16" svnclientadapter-%{svnclientadapter_tag}/javahl
%endif

# Must be dir-shaped bundles so we can symlink system versions of libs
for b in bundles/svnapi.* ; do
  echo "Eclipse-BundleShape: dir" >> $b/META-INF/MANIFEST.MF
  sed -i -e 's/-1\.[0-9]\+\.[0-9]\+\.jar/.jar/' $b/META-INF/MANIFEST.MF $b/build.properties
done

# Don't build mylyn features because mylyn is not shipped in Fedora
%pom_disable_module feature.mylyn features
%pom_disable_module subclipse.mylyn bundles

pushd svnclientadapter-%{svnclientadapter_tag}
%pom_remove_plugin ":bnd-maven-plugin" base cmdline javahl svnkit
%pom_remove_plugin ":maven-jar-plugin" base cmdline javahl svnkit
popd

# Don't install poms
%mvn_package "::pom::" __noinstall

%build
pushd svnclientadapter-%{svnclientadapter_tag}
# TODO: Make subversion-javahl package install a pom file
%if %{with javahl}
xmvn -B -o install:install-file -Dfile=$(build-classpath svn-javahl) -Dpackaging=jar \
      -DgroupId=org.apache.subversion -DartifactId=javahl -Dversion=%{svnclientadapter_version}
%endif

%mvn_build -j
popd

cp -p $(find svnclientadapter-%{svnclientadapter_tag} -name adapter-base*.jar) bundles/svnapi.core/lib/adapter-base.jar
%if %{with javahl}
# JavaHL libs
cp -p $(find svnclientadapter-%{svnclientadapter_tag} -name adapter-javahl*.jar) bundles/svnapi.javahl/lib/adapter-javahl.jar
ln -s $(build-classpath svn-javahl) bundles/svnapi.javahl/lib/javahl.jar
%endif
# SVNKit libs
cp -p $(find svnclientadapter-%{svnclientadapter_tag} -name adapter-svnkit*.jar) bundles/svnapi.svnkit/lib/adapter-svnkit.jar
cp -p $(find svnclientadapter-%{svnclientadapter_tag} -name adapter-javahl*.jar) bundles/svnapi.svnkit/lib/adapter-javahl.jar
for j in \
    svnkit/svnkit svnkit/svnkit-javahl16 \
    sqljet antlr32/antlr-runtime-3.2 sequence-library trilead-ssh2 \
    jsch-agent-proxy/jsch.agentproxy.connector-factory \
    jsch-agent-proxy/jsch.agentproxy.core \
    jsch-agent-proxy/jsch.agentproxy.pageant \
    jsch-agent-proxy/jsch.agentproxy.sshagent \
    jsch-agent-proxy/jsch.agentproxy.svnkit-trilead-ssh2 \
    jsch-agent-proxy/jsch.agentproxy.usocket-jna \
    jsch-agent-proxy/jsch.agentproxy.usocket-nc \
    jna/jna jna/jna-platform ; do
  ln -s $(build-classpath $j) bundles/svnapi.svnkit/lib/$(basename $j).jar
  sed -i -e "/Bundle-ClassPath/s/: /: lib\/$(basename $j).jar,/" bundles/svnapi.svnkit/META-INF/MANIFEST.MF
done

# Qualifier generated from last modification time of source tarball
QUALIFIER=$(date -u -d"$(stat --format=%y %{SOURCE0})" +%Y%m%d%H%M)
%mvn_build -j -- -DforceContextQualifier=$QUALIFIER

%install
%mvn_install

droplet=%{buildroot}%{_datadir}/eclipse/droplets/subclipse

# Replace jar with link to system libraries
%if %{with javahl}
# JavaHL libs
pushd $droplet/plugins/org.tigris.subversion.clientadapter.javahl_*
rm lib/javahl.jar
ln -s $(build-classpath svn-javahl) lib/javahl.jar
popd
%endif
# SVNKit libs
pushd $droplet/plugins/org.tigris.subversion.clientadapter.svnkit_*
for j in \
    svnkit/svnkit svnkit/svnkit-javahl16 \
    sqljet antlr32/antlr-runtime-3.2 sequence-library trilead-ssh2 \
    jsch-agent-proxy/jsch.agentproxy.connector-factory \
    jsch-agent-proxy/jsch.agentproxy.core \
    jsch-agent-proxy/jsch.agentproxy.pageant \
    jsch-agent-proxy/jsch.agentproxy.sshagent \
    jsch-agent-proxy/jsch.agentproxy.svnkit-trilead-ssh2 \
    jsch-agent-proxy/jsch.agentproxy.usocket-jna \
    jsch-agent-proxy/jsch.agentproxy.usocket-nc \
    jna/jna jna/jna-platform ; do
  rm lib/$(basename $j).jar
  ln -s $(build-classpath $j) lib/$(basename $j).jar
done
popd

# Install appdata
install -m644 -D %{SOURCE3} %{buildroot}%{_datadir}/appdata/eclipse-subclipse.metainfo.xml
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/eclipse-subclipse.metainfo.xml

%files -f .mfiles
%doc CHANGELOG.md README.md
%license LICENSE.md LICENSE-apache.md
%{_datadir}/appdata/eclipse-subclipse.metainfo.xml

%changelog
* Wed Aug 26 2020 Mat Booth <mat.booth@redhat.com> - 4.3.0-8
- Actual minimum supported native JavaHL version is 1.12

* Wed Aug 26 2020 Mat Booth <mat.booth@redhat.com> - 4.3.0-7
- Update JavaHL support bundles to 1.14

* Mon Aug 17 2020 Mat Booth <mat.booth@redhat.com> - 4.3.0-6
- Clarify licensing and install copy of the Apache license

* Mon Aug 17 2020 Mat Booth <mat.booth@redhat.com> - 4.3.0-5
- Update project URL

* Tue May 05 2020 Mat Booth <mat.booth@redhat.com> - 4.3.0-4
- Drop dependency on mylyn

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 19 2019 Mat Booth <mat.booth@redhat.com> - 4.3.0-1
- Update to final 4.3.0 release

* Fri Mar 15 2019 Mat Booth <mat.booth@redhat.com> - 4.3.0-0.3.git43b895a
- Restrict to same architectures as Eclipse itself

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-0.2.git43b895a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 22 2018 Mat Booth <mat.booth@redhat.com> - 4.3.0-0.1
- Update to latest upstream snapshot for SVN 1.10 support
- Update license tag

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 09 2018 Mat Booth <mat.booth@redhat.com> - 4.2.3-4
- Fix reference to droplets directory tree

* Wed Mar 21 2018 Mat Booth <mat.booth@redhat.com> - 4.2.3-3
- Enable conditional build support for svn backends

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Nov 24 2017 Mat Booth <mat.booth@redhat.com> - 4.2.3-1
- Update to latest upstream release
- Add patch to fix "unable to auto-share" error, rhbz#1380666

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 30 2017 Mikolaj Izdebski <mizdebsk@redhat.com> - 4.2.2-3
- Add missing build-requires on maven-install-plugin
- Run xmvn in batch mode

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jan 21 2017 Mat Booth <mat.booth@redhat.com> - 4.2.2-1
- Update to latest upstream release
- Project moved to github and absorbed the merge client plugin
- Obsolete/Provide the collabnet-merge package

* Wed Apr 20 2016 Mat Booth <mat.booth@redhat.com> - 1.10.11-3
- Build/install with tycho/xmvn

* Wed Mar 09 2016 Mat Booth <mat.booth@redhat.com> - 1.10.11-2
- Add appdata add-on metadata

* Wed Mar 09 2016 Mat Booth <mat.booth@redhat.com> - 1.10.11-1
- Update to latest upstream release

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Oct 29 2015 Mat Booth <mat.booth@redhat.com> - 1.10.10-1
- Update to 1.10.10 with Subversion 1.9 support

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Mar 03 2015 Mat Booth <mat.booth@redhat.com> - 1.10.9-1
- Update to latest upstream release

* Thu Jan 15 2015 Alexander Kurtakov <akurtako@redhat.com> 1.10.5-2
- Adapt pde-build.sh call to gef path change.

* Fri Jul 18 2014 Mat Booth <mat.booth@redhat.com> - 1.10.5-1
- Update to latest upstream release
- Drop ancient obsoletes on subclipse-book, drop unnecessary BRs
- Fix bogus dates in changelog
- Install license files as %%doc

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Oct 1 2013 Krzysztof Daniel <kdaniel@redhat.com> 1.10.2-2
- Fix the javahl version.

* Tue Oct 1 2013 Krzysztof Daniel <kdaniel@redhat.com> 1.10.2-1
- Update to 1.10.2.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jun 19 2013 Krzysztof Daniel <kdaniel@redhat.com> 1.10.0-2
- Upload sources.

* Wed Jun 19 2013 Krzysztof Daniel <kdaniel@redhat.com> 1.10.0-1
- Update to 1.10.0.

* Wed Jun 19 2013 Krzysztof Daniel <kdaniel@redhat.com> 1.8.21-1
- Update to 1.8.21.

* Fri May 3 2013 Krzysztof Daniel <kdaniel@redhat.com> 1.8.20-1
- Update to latest upstream release.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Oct 11 2012 Sami Wagiaalla <swagiaal@redhat.com> 1.8.16-1
- Update to release 1.8.16.

* Wed Aug 8 2012 Krzysztof Daniel <kdaniel@redhat.com> 1.8.13-2
- Get rid off eclipse-svnkit dependency.

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jul 13 2012 Krzysztof Daniel <kdaniel@redhat.com> 1.8.13-1
- Update to latest upstream release.

* Thu May 3 2012 Krzysztof Daniel <kdaniel@redhat.com> 1.8.9-2
- Bug 818472 - Bump javahl BR/R.

* Wed May 2 2012 Krzysztof Daniel <kdaniel@redhat.com> 1.8.9-1
- Update to latest upstream release.

* Wed Feb 29 2012 Alexander Kurtakov <akurtako@redhat.com> 1.8.5-1
- Update to latest upstream release.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 12 2011 Alexander Kurtakov <akurtako@redhat.com> 1.6.18-1
- Update to 1.6.18.

* Fri Feb 25 2011 Alexander Kurtakov <akurtako@redhat.com> 1.6.17-1
- Update to 1.6.17.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 14 2010 Alexander Kurtakov <akurtako@redhat.com> 1.6.16-1
- Update to 1.6.16.

* Tue Nov 9 2010 Alexander Kurtakov <akurtako@redhat.com> 1.6.15-1
- Update to 1.6.15.

* Tue Jul 13 2010 Alexander Kurtakov <akurtako@redhat.com> 1.6.12-1
- Update to 1.6.12.

* Thu Mar 11 2010 Alexander Kurtakov <akurtako@redhat.com> 1.6.10-1
- Update to 1.6.10.

* Tue Feb 23 2010 Alexander Kurtakov <akurtako@redhat.com> 1.6.8-1
- Update to upstream 1.6.8.

* Fri Feb 19 2010 Alexander Kurtakov <akurtako@redhat.com> 1.6.7-1
- Update to upstream 1.6.7.

* Thu Feb 4 2010 Alexander Kurtakov <akurtako@redhat.com> 1.6.6-1
- Update to upstream 1.6.6.

* Sun Nov 22 2009 Alexander Kurtakov <akurtako@redhat.com> 1.6.5-3
- Fix typo.

* Sun Nov 22 2009 Alexander Kurtakov <akurtako@redhat.com> 1.6.5-2
- Do not pass non-existing folders to pdebuild -o.
- Switch to using %%global instead of %%define.

* Tue Aug 18 2009 Alexander Kurtakov <akurtako@redhat.com> 1.6.5-1
- Update to upstream 1.6.5.

* Mon Aug 10 2009 Alexander Kurtakov <akurtako@redhat.com> 1.6.4-1
- Update to upstream 1.6.4.

* Mon Jul 27 2009 Alexander Kurtakov <akurtako@redhat.com> 1.6.2-1
- Update to upstream 1.6.2.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Apr 26 2009 Robert Marcano <robert@marcanoonline.com> 1.6.0-1
- Update to upstream 1.6.0

* Mon Mar 23 2009 Alexander Kurtakov <akurtako@redhat.com> 1.4.7-4
- Rebuild to not ship p2 context.xml.

* Tue Feb 24 2009 Robert Marcano <robert@marcanoonline.com> 1.4.7-3
- Update to upstream 1.4.7
- eclipse-subclipse-book is obsoleted, not provided upstream
- New eclipse-subclipse-graph subpackage

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Oct 13 2008 Alexander Kurtakov <akurtako@redhat.com> - 1.2.4-12
- Bump revision.

* Mon Oct 13 2008 Alexander Kurtakov <akurtako@redhat.com> - 1.2.4-11
- Fix build with eclipse 3.4.
- Rediff plugin-classpath.patch.

* Sun Sep 21 2008 Ville Skyttä <ville.skytta at iki.fi> - 1.2.4-10
- Fix Patch0:/%%patch mismatch.

* Fri Apr 04 2008 Robert Marcano <robert@marcanoonline.com> 1.2.4-9
- Fix Bug 440818: changed links to svn-javahl.jar

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.2.4-7
- Autorebuild for GCC 4.3

* Mon Nov 12 2007 Robert Marcano <robert@marcanoonline.com> 1.2.4-6
- Build for all supported arquitectures

* Fri Oct 19 2007 Robert Marcano <robert@marcanoonline.com> 1.2.4-3
- Disable ppc64 build for f8, see Bug #298071

* Wed Sep 19 2007 Robert Marcano <robert@marcanoonline.com> 1.2.4-2
- Fix wrong applied classpath patch, fixing error: An error occurred while
automatically activating bundle org.tigris.subversion.subclipse.core

* Mon Sep 10 2007 Robert Marcano <robert@marcanoonline.com> 1.2.4-1
- Update to upstream 1.2.4
- Build for all supported arquitectures

* Sun Sep 09 2007 Robert Marcano <robert@marcanoonline.com> 1.2.2-6
- Change MANIFEST.MF patch to be applied on prep stage

* Wed Aug 29 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 1.2.2-4
- Rebuild for selinux ppc32 issue.

* Wed Jun 20 2007 Robert Marcano <robert@marcanoonline.com> 1.2.2-2
- Update to upstream 1.2.2
- Dependency changed from javasvn to svnkit
- Patch to support EPEL5 sent by Rob Myers

* Thu Dec 21 2006 Robert Marcano <robert@marcanoonline.com> 1.1.9-2
- Update to upstream 1.1.9
- Removed patch that added source attribute to the javac ant task
- Using the "eclipse" launcher

* Wed Nov 08 2006 Robert Marcano <robert@marcanoonline.com> 1.1.8-2
- Update to upstream 1.1.8

* Mon Aug 28 2006 Robert Marcano <robert@marcanoonline.com> 1.1.5-2
- Rebuild

* Mon Aug 21 2006 Robert Marcano <robert@marcanoonline.com> 1.1.5-1
- Update to upstream 1.1.5
- svnClientAdapter documentation files added. Subclipse includes an eclipse
  based documentation for the plugins

* Sun Aug 06 2006 Robert Marcano <robert@marcanoonline.com> 1.1.4-1
- Update to upstream 1.1.4
- License changed to EPL
- svnClientAdapter-1.1.4-javac-target.patch added fix to svnClientAdapter ant
  script

* Tue Jul 04 2006 Andrew Overholt <overholt@redhat.com> 1.0.3-2
- Use versionless pde.build.
- Remove strict SDK version requirement due to above.

* Sun Jul 02 2006 Robert Marcano <robert@marcanoonline.com> 1.0.3-2
- Embeeding the script that fetch the source code

* Sun Jun 25 2006 Robert Marcano <robert@marcanoonline.com> 1.0.3-1
- Update to 1.0.3
- Dependency name changed to ganymed-ssh2

* Sun Jun 11 2006 Robert Marcano <robert@marcanoonline.com> 1.0.1-6
- rpmlint fixes and debuginfo generation workaround

* Thu Jun 01 2006 Robert Marcano <robert@marcanoonline.com> 1.0.1-5
- Use package-build from eclipse SDK

* Sun May 28 2006 Robert Marcano <robert@marcanoonline.com> 1.0.1-4
- Integrated svnClientAdapter inside this package

* Tue May 23 2006 Ben Konrath <bkonrath@redhat.com> 1.0.1-3
- Rename package to eclipse-subclipse.
- Use copy-platform script for now.

* Sun May 07 2006 Robert Marcano <robert@marcanoonline.com> 1.0.1-2
- use external libraries from dependent packages

* Wed Apr 26 2006 Ben Konrath <bkonrath@redhat.com> 1.0.1-1
- initial version based on the work of Robert Marcano

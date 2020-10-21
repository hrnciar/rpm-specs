%global git_tag b1bdab816fe2541091ed36931f933d03f02cf879

Name:           eclipse-remote
Version:        3.0.1
Release:        6%{?dist}
Summary:        Eclipse Remote Services plug-in
License:        EPL-1.0
URL:            https://www.eclipse.org/ptp/

Source0:        http://git.eclipse.org/c/ptp/org.eclipse.remote.git/snapshot/org.eclipse.remote-%{git_tag}.tar.xz

BuildArch:      noarch

# Upstream Eclipse no longer supports non-64bit arches
ExcludeArch: s390 %{arm} %{ix86}

BuildRequires:    tycho
BuildRequires:    tycho-extras
BuildRequires:    jsch
BuildRequires:    eclipse-pde
BuildRequires:    eclipse-license
BuildRequires:    eclipse-cdt
BuildRequires:    eclipse-cdt-terminal

Requires:         jsch
Requires:         eclipse-platform

%description
Remote Services provides an extensible remote services framework.

%prep
%setup -q -n org.eclipse.remote-%{git_tag}

find -name *.jar -exec rm -rf {} \;
find -name *.class -exec rm -rf {} \;

# Remove use of tycho-sourceref-jgit (source is not a git repo)
%pom_remove_plugin org.eclipse.tycho:tycho-packaging-plugin releng/org.eclipse.remote.build/pom.xml

# Don't need to build repo or target platform for RPM builds
%pom_disable_module ../../releng/org.eclipse.remote.repo releng/org.eclipse.remote.build/pom.xml
%pom_disable_module ../../releng/org.eclipse.remote.target releng/org.eclipse.remote.build/pom.xml
%pom_xpath_remove "pom:target" releng/org.eclipse.remote.build/pom.xml

# Don't build the proxy product
%pom_disable_module ../../releng/org.eclipse.remote.proxy.server.product releng/org.eclipse.remote.build
%pom_disable_module ../../releng/org.eclipse.remote.proxy.server.linux.ppc64le releng/org.eclipse.remote.build
%pom_disable_module ../../releng/org.eclipse.remote.proxy.server.linux.x86_64 releng/org.eclipse.remote.build
%pom_disable_module ../../releng/org.eclipse.remote.proxy.server.macosx.x86_64 releng/org.eclipse.remote.build
%pom_xpath_remove "feature/plugin[@id='org.eclipse.remote.proxy.server.linux.ppc64le']" \
  features/org.eclipse.remote.proxy-feature/feature.xml
%pom_xpath_remove "feature/plugin[@id='org.eclipse.remote.proxy.server.linux.x86_64']" \
  features/org.eclipse.remote.proxy-feature/feature.xml
%pom_xpath_remove "feature/plugin[@id='org.eclipse.remote.proxy.server.macosx.x86_64']" \
  features/org.eclipse.remote.proxy-feature/feature.xml

%mvn_package "::pom::" __noinstall

%build
%mvn_build  -j -- -Dproject.build.sourceEncoding=UTF-8 \
  -DforceContextQualifier=%(date -u +%%Y%%m%%d1000) \
  -f releng/org.eclipse.remote.build/pom.xml

%install
%mvn_install

%files -f .mfiles
%license features/org.eclipse.remote-feature/epl-v10.html

%changelog
* Fri Aug 14 2020 Mat Booth <mat.booth@redhat.com> - 3.0.1-6
- Update dep on tm-terminal

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Mar 14 2019 Mat Booth <mat.booth@redhat.com> - 3.0.1-2
- Upload correct source

* Thu Mar 14 2019 Mat Booth <mat.booth@redhat.com> - 3.0.1-1
- Update to 2019-03 release
- Restrict to same architectures as Eclipse itself

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-0.7.git14c6611
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 05 2018 Mat Booth <mat.booth@redhat.com> - 3.0.0-0.6.git14c6611
- Rebuild to regenerate requires
- Update license tag

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-0.5.git14c6611
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Mar 20 2018 Mat Booth <mat.booth@redhat.com> - 3.0.0-0.4.git14c6611
- Update to latest snapshot

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-0.3.git96f33c6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-0.2.git96f33c6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jun 17 2017 Mat Booth <mat.booth@redhat.com> - 3.0.0-0.1.git96f33c6
- Update to Oxygen snapshot

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Oct 04 2016 Mat Booth <mat.booth@redhat.com> - 2.1.1-1
- Update to Neon.1 release

* Wed Jun 29 2016 Mat Booth <mat.booth@redhat.com> - 2.1.0-1
- Update to Neon release

* Thu Mar 10 2016 Mat Booth <mat.booth@redhat.com> - 2.0.2-1
- Adopt license macro and set context qualifier

* Thu Mar 03 2016 Sopot Cela <scela@redhat.com> - 2.0.2-0.1.gitb1e764a
- Update for Mars.2

* Thu Feb 04 2016 Roland Grunberg <rgrunber@redhat.com> - 2.0.1-2
- Remove dependency org.eclipse.ui.trace.

* Thu Feb 04 2016 Mat Booth <mat.booth@redhat.com> - 2.0.1-1
- Update to upstream release 2.0.1

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Sep 14 2015 Roland Grunberg <rgrunber@redhat.com> - 2.0.0-2
- Rebuild as an Eclipse p2 Droplet.

* Wed Jun 24 2015 Alexander Kurtakov <akurtako@redhat.com> 2.0.0-1
- Update to 2.0 final.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-0.4.git4488f6f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 3 2015 Alexander Kurtakov <akurtako@redhat.com> 2.0.0-0.3.git4488f6f
- BR eclipse-tm-terminal to do full build.

* Tue Jun 2 2015 Alexander Kurtakov <akurtako@redhat.com> 2.0.0-0.2.git4488f6f
- New git snapshot.
- Build serial plugins.

* Mon Jun 1 2015 Alexander Kurtakov <akurtako@redhat.com> 2.0.0-0.1.git76ac23a
- Update to 2.0 prerelease.

* Wed Mar 04 2015 Mat Booth <mat.booth@redhat.com> - 1.1.1-1
- Update to 1.1.1

* Fri Feb  6 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1.0-2
- Rebuild to generate missing OSGi auto-requires

* Tue Sep 30 2014 Mat Booth <mat.booth@redhat.com> - 1.1.0-1
- Update to 1.1.0

* Thu Sep 25 2014 Mat Booth <mat.booth@redhat.com> - 1.0.0-3
- Rebuild to regenerate auto requires

* Fri Sep 12 2014 Mat Booth <mat.booth@redhat.com> - 1.0.0-2
- Build/install with xmvn

* Fri Jun 27 2014 Mat Booth <mat.booth@redhat.com> - 1.0.0-1
- Update to upstream released version
- Add BR on eclipse-license

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-0.5.git19f4d9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 07 2014 Mat Booth <mat.booth@redhat.com> - 1.0.0-0.4.git19f4d9
- Drop requirement on jpackage-utils

* Tue May 06 2014 Mat Booth <mat.booth@redhat.com> - 1.0.0-0.3.git19f4d9
- Update to latest upstream.

* Tue May 06 2014 Mat Booth <mat.booth@redhat.com> - 1.0.0-0.2.gite09793
- Don't include the cdt feature.

* Tue May 06 2014 Mat Booth <mat.booth@redhat.com> - 1.0.0-0.1.gite09793
- Initial package.

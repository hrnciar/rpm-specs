Name:		canl-java
Version:	2.6.0
Release:	9%{?dist}
Summary:	EMI Common Authentication library - bindings for Java

#		The main parts of the code are BSD
#		Parts derived from glite security utils java are Apache 2.0
#		Parts derived from bouncycastle are MIT
#		Parts derived from Apache Commons IO are Apache 2.0
#		See LICENSE.txt for details
License:	BSD and ASL 2.0 and MIT
URL:		https://github.com/eu-emi/%{name}/
Source0:	https://github.com/eu-emi/%{name}/archive/canl-%{version}/%{name}-%{version}.tar.gz
#		Disable tests that require network connections
Patch0:		%{name}-test.patch
#		Adapt to bouncycastle 1.63. Still builds with older versions.
#		https://github.com/eu-emi/canl-java/pull/102
Patch1:		%{name}-tagged-seq.patch
#		Fix javadoc issues with JDK 11
#		https://github.com/eu-emi/canl-java/pull/103
Patch2:		%{name}-jdk11-javadoc.patch

BuildArch:	noarch

BuildRequires:	maven-local
BuildRequires:	mvn(commons-io:commons-io) >= 2.4
BuildRequires:	mvn(junit:junit) >= 4.8
BuildRequires:	mvn(org.bouncycastle:bcpkix-jdk15on) >= 1.54
BuildRequires:	mvn(org.bouncycastle:bcprov-jdk15on) >= 1.54
Requires:	mvn(org.bouncycastle:bcpkix-jdk15on) >= 1.54
Requires:	mvn(org.bouncycastle:bcprov-jdk15on) >= 1.54

%description
This is the Java part of the EMI caNl -- the Common Authentication Library.

%package javadoc
Summary:	Javadoc documentation for %{name}

%description javadoc
Javadoc documentation for EMI caNl.

%prep
%setup -q -n %{name}-canl-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

# Remove maven-wagon-webdav-jackrabbit dependency
%pom_xpath_remove pom:build/pom:extensions

# GPG signing requires a GPG key
%pom_remove_plugin org.apache.maven.plugins:maven-gpg-plugin

%if %{?fedora}%{!?fedora:0} >= 33 || %{?rhel}%{!?rhel:0} >= 8
# F33+ and EPEL8+ doesn't use the maven-javadoc-plugin to generate javadoc
# Remove maven-javadoc-plugin configuration to avoid build failure
%pom_remove_plugin org.apache.maven.plugins:maven-javadoc-plugin
%endif

# Do not create source jars
%pom_remove_plugin org.apache.maven.plugins:maven-source-plugin

# Do not stage
%pom_remove_plugin org.sonatype.plugins:nexus-staging-maven-plugin

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc API-Changes.txt README.md
%license LICENSE.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 15 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 2.6.0-8
- Fedora 33 builds javadoc the same way EPEL 8 does

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 2.6.0-7
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Tue May 05 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 2.6.0-6
- Only remove the maven-javadoc-plugin configuration on EPEL 8
- Fix javadoc issues with JDK 11

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 07 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 2.6.0-4
- Adapt to bouncycastle 1.63. Still builds with older versions.

* Mon Aug 19 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 2.6.0-3
- Remove maven-javadoc-plugin configuration

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 22 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 2.6.0-1
- Update to 2.6.0
- Drop patch canl-java-javadoc.patch (previously backported)

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 04 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 2.5.0-1
- Update to 2.5.0
- Javadoc fixes (backport from upstream)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Sep 10 2016 Mattias Ellert <mattias.ellert@physics.uu.se> - 2.4.1-1
- Update to 2.4.1

* Mon Jul 11 2016 Mattias Ellert <mattias.ellert@physics.uu.se> - 2.4.0-1
- Update to 2.4.0
- Drop patch canl-java-javadoc.patch (accepted upstream)

* Fri Apr 15 2016 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.3.0-1
- Update to 2.3.0 - requires bouncycastle 1.54 (Fedora 25+)

* Sat Feb 13 2016 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.2.1-1
- Update to 2.2.1

* Sat Feb 13 2016 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.1.2-1
- New upstream version
- Drop patch canl-java-use-proper-size-of-the-returned-array.patch

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Aug 05 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.2.0-1
- Update to 2.2.0 - requires bouncycastle 1.52 (Fedora 23+)
- Drop patches no longer needed with new version

* Wed Aug 05 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.1.1-4
- Drop bouncycastle 1.52 modifications (Fedora 23+ now uses canl-java 2.2.0)
- Minor javadoc fixes

* Sat Jul 11 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.1.1-3
- Adapt to bouncycastle 1.52 (Fedora 23+)
- Implement new license packaging guidelines

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Oct 13 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.1.1-1
- New upstream version

* Wed Jun 11 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.1.0-3
- Fix test that fails when using OpenJDK 1.8 (patch from upstream git)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Apr 06 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.1.0-1
- New upstream version

* Thu Mar 13 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.0.0-2
- Use upstream's fix for the failing test

* Fri Feb 28 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.0.0-1
- Update to version 2.0.0 to support newer bouncycastle

* Fri Feb 28 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.3.1-1
- New upstream version

* Wed Nov 27 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.3.0-1
- New upstream version

* Sun Aug 18 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.2.1-1
- New upstream version
- Use xmvn instead of mvn-rpmbuild

* Fri May 17 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.2.0-1
- New upstream version
- Drop canl-java-java7.patch (fixed upstream)

* Thu Feb 14 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.1.0-1
- Initial Fedora build

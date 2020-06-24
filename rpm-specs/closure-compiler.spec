#global _check 1

Summary:    JavaScript minifier and checker
Name:       closure-compiler
#define commit ad29f06d581fb8c54ad031334b82a5c301b6ce0a
#define shorthash %%(printf %%.7s %%commit)
Version:    20160315
Release:    13%{?dist}
License:    ASL 2.0
URL:        https://developers.google.com/closure/compiler/
Source0:    https://github.com/google/closure-compiler/archive/maven-release-v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:    closure-compiler.xml
BuildArch:  noarch

BuildRequires:  maven-local
BuildRequires:  mvn(args4j:args4j)
BuildRequires:  mvn(com.google.code.findbugs:jsr305)
BuildRequires:  mvn(com.google.code.gson:gson)
BuildRequires:  mvn(com.google.guava:guava:20.0)
BuildRequires:  mvn(com.google.protobuf:protobuf-java)
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-shade-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)

BuildRequires: libxslt
BuildRequires: docbook-style-xsl
# Explicit requires for javapackages-tools since closure-compiler script
# uses /usr/share/java-utils/java-functions
Requires:      javapackages-tools

# There was a javadoc package, but is empty now. Let's just disable
# it. No idea what changed an why, but this package is too outdated
# for anyone to be using the javadocs for anything.
Obsoletes: %{name}-javadoc < 20160315-13

%description
The Closure Compiler is a tool for making JavaScript download and run
faster. It is a true compiler for JavaScript. Instead of compiling
from a source language to machine code, it compiles from JavaScript to
better JavaScript. It parses your JavaScript, analyzes it, removes
dead code and rewrites and minimizes what’s left. It also checks
syntax, variable references, and types, and warns about common
JavaScript pitfalls.

%prep
%autosetup -n %{name}-maven-release-v%{version}
rm -rf lib/*

# Don't build shaded jar because it bundles all deps
%pom_disable_module "pom-main-shaded.xml" pom-main.xml
%mvn_alias :closure-compiler-unshaded :closure-compiler

# Make static analysis annotations have provided scope
%pom_xpath_inject "pom:dependency[pom:artifactId='jsr305']" "<scope>provided</scope>" pom-main.xml

# Fix OSGi metadata
%pom_xpath_inject "pom:plugin[pom:artifactId='maven-bundle-plugin']" \
"<configuration><instructions>
  <Bundle-SymbolicName>\${project.groupId}</Bundle-SymbolicName>
</instructions></configuration>" pom-main.xml

%build
%mvn_build -f

xsltproc \
        --nonet \
        --stringparam man.output.quietly 1 \
        --stringparam funcsynopsis.style ansi \
        --stringparam man.authors.section.enabled 0 \
        --stringparam man.copyright.section.enabled 0 \
        http://docbook.sourceforge.net/release/xsl/current/manpages/docbook.xsl %{SOURCE1}

%install
%mvn_install
%jpackage_script com.google.javascript.jscomp.CommandLineRunner "" "" args4j:google-gson:jsr-305:protobuf-java:guava20:%{name} %{name} true

install -Dm0644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

%global _docdir_fmt %{name}

%files -f .mfiles
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.*

%license COPYING
%doc README.md

%changelog
* Sun Jun 14 2020 Adrian Reber <adrian@lisas.de> - 20160315-13
- Rebuilt for protobuf 3.12

* Tue Mar 10 2020 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 20160315-12
- Remove -javadoc subpackage and fix build (#1799234)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20160315-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20160315-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 01 2019 Mat Booth <mat.booth@redhat.com> - 20160315-10
- Make static analysis annotations have provided scope because they are not
  needed at runtime

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20160315-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 12 2018 Mat Booth <mat.booth@redhat.com> - 20160315-8
- Remove erroneous mention of rhino from jpackage script

* Fri Aug 31 2018 Severin Gehwolf <sgehwolf@redhat.com> - 20160315-7
- Add explicit requirement on javapackages-tools for jpackage_script-based
  launcher. See RHBZ#1600426.

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20160315-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Mar 06 2018 Mat Booth <mat.booth@redhat.com> - 20160315-5
- Fix BR and script dep on guava

* Wed Feb 14 2018 Mat Booth <mat.booth@redhat.com> - 20160315-4
- Drop guava compatibility hacks

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20160315-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20160315-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 28 2017 Mat Booth <mat.booth@redhat.com> - 20160315-1
- Update to newer version of closure-compiler
- Regenerate BRs and fix-up OSGi metadata

* Tue Jun 13 2017 Orion Poplawski <orion@cora.nwra.com> - 20141215-8
- Rebuild for protobuf 3.3.1

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20141215-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 23 2017 Orion Poplawski <orion@cora.nwra.com> - 20141215-6
- Rebuild for protobuf 3.2.0

* Fri Nov 18 2016 Orion Poplawski <orion@cora.nwra.com> - 20141215-5
- Rebuild for protobuf 3.1.0

* Fri Nov 04 2016 Orion Poplawski <orion@cora.nwra.com> - 20141215-4
- Add new BRs for maven build

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20141215-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jul 26 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 20141215-2
- Add missing dependency on junit (#1246897)

* Sat Jul 25 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 20141215-1
- Update to latest release which does not require truth
- Add missing dependency on jarjar (#1246759)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20140923-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Oct 01 2014 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 20140923-1
- Update to the latest release.

* Fri Jun 13 2014 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 20140613.gite5cfc63-1
- Convert to maven build and update to latest version from git (#1106062).

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20140110-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Feb 05 2014 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 20140110-2
- Use java-headless (#1068009).

* Wed Feb 05 2014 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 20140110-1
- Fix requires.
- Convert manpage to docbook.
- Add disabled %%check.
- Update license.
- Update to newest upstream version.

* Tue Oct 29 2013 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 20131118-1
- Update to latest upstream release.
- Remove bundled tools/maven-ant-tasks in %%prep and add dependencies
  on replacement packages.
- Replace json with android-json-org-java completely.

* Tue Oct 29 2013 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 20131014-2
- Replace json with android-json-org-java.
- Put requires java libraries in Requires.
- Add main-class manifests to the jar.

* Mon Oct 28 2013 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 20131014-1
- Initial packaging.

Name:     jnr-ffi
Version:  2.1.8
Release:  5%{?dist}
Summary:  Java Abstracted Foreign Function Layer
License:  ASL 2.0
URL:      http://github.com/jnr/%{name}/
Source0:  https://github.com/jnr/%{name}/archive/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make

BuildRequires:  maven-local
BuildRequires:  mvn(com.github.jnr:jffi)
BuildRequires:  mvn(com.github.jnr:jffi::native:)
BuildRequires:  mvn(com.github.jnr:jnr-x86asm)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.ow2.asm:asm)
BuildRequires:  mvn(org.ow2.asm:asm-analysis)
BuildRequires:  mvn(org.ow2.asm:asm-commons)
BuildRequires:  mvn(org.ow2.asm:asm-tree)
BuildRequires:  mvn(org.ow2.asm:asm-util)
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)

BuildArch:     noarch

# don't obsolete/provide jaffl, gradle is using both jaffl and jnr-ffi...

%description
An abstracted interface to invoking native functions from java

%package javadoc
Summary:        Javadocs for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}

# remove all builtin jars
find -name '*.jar' -o -name '*.class' -exec rm -f '{}' \;

# Unnecessary for RPM builds
%pom_remove_plugin ":maven-javadoc-plugin"

# don't fail on unused parameters... (TODO: send patch upstream)
sed -i 's|-Werror||' libtest/GNUmakefile

%build
%mvn_build -- -Dasm.version=7.0

%install
%mvn_install

%files -f .mfiles
%license LICENSE

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 10 2018 Mat Booth <mat.booth@redhat.com> - 2.1.8-2
- Set the required version of ASM

* Sat Dec 08 2018 Mat Booth <mat.booth@redhat.com> - 2.1.8-1
- Update to latest upstream release

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Sep 12 2017 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.1.6-3
- Rebuild to regenerate OSGi manifest after ASM6 upgrade

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 30 2017 Mat Booth <mat.booth@redhat.com> - 2.1.6-1
- Update to latest release, fix FTBFS, re-enable tests

* Mon Feb 06 2017 Michael Simacek <msimacek@redhat.com> - 2.1.2-3
- Regenerate BRs

* Wed Feb  1 2017 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.1.2-2
- Add missing build-requires on GCC

* Mon Dec 19 2016 Alexander Kurtakov <akurtako@redhat.com> 2.1.2-1
- Update to upstream 2.1.2.

* Fri Dec 16 2016 Merlin Mathesius <mmathesi@redhat.com> - 2.0.9-2
- Add missing BuildRequires to fix FTBFS (BZ#1405595).

* Mon Apr 18 2016 Alexander Kurtakov <akurtako@redhat.com> 2.0.9-1
- Update to upstream 2.0.9 release.

* Fri Feb 5 2016 Alexander Kurtakov <akurtako@redhat.com> 2.0.6-1
- Update to upstream 2.0.6 release.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Oct 23 2015 Alexander Kurtakov <akurtako@redhat.com> 2.0.4-1
- Update to upstream 2.0.4 and drop unneeded osgification patch/source.

* Tue Jun 23 2015 Roland Grunberg <rgrunber@redhat.com> - 2.0.3-4
- Add missing Import-Package statements to manifest.

* Wed Jun 17 2015 Jeff Johnston <jjohnstn@redhat.com> - 2.0.3-3
- Add proper MANIFEST.MF.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue May 5 2015 Alexander Kurtakov <akurtako@redhat.com> 2.0.3-1
- Update to upstream 2.0.3.
- Skip tests.

* Thu Apr 30 2015 Alexander Kurtakov <akurtako@redhat.com> 2.0.2-1
- Update to upstream 2.0.2.

* Thu Feb 19 2015 Michal Srb <msrb@redhat.com> - 2.0.1-3
- Skip tests on arm

* Wed Feb 18 2015 Michal Srb <msrb@redhat.com> - 2.0.1-2
- Build with jffi-native

* Mon Jan 05 2015 Mo Morsi <mmorsi@redhat.com> - 2.0.1-1
- Update to 2.0.1

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Sep 25 2013 Michal Srb <msrb@redhat.com> - 0.7.10-4
- Adapt to current guidelines
- Remove unneeded patch
- Enable tests
- Fix BR

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 06 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 0.7.10-2
- Depend on objectweb-asm4, not objectweb-asm.

* Tue Feb 05 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 0.7.10-1
- Update to version 0.7.10.
- Switch from ant to maven.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Aug 23 2011 Mo Morsi <mmorsi@redhat.com> - 0.5.10-3
- more updates to conform to fedora guidelines

* Wed Aug 10 2011 Mo Morsi <mmorsi@redhat.com> - 0.5.10-2
- updated to conform to fedora guidelines

* Tue Aug 02 2011 Mo Morsi <mmorsi@redhat.com> - 0.5.10-1
- initial package

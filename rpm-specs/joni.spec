Name:             joni
Version:          2.1.3
Release:          11%{?dist}
Summary:          Java port of Oniguruma regexp library 
License:          MIT
URL:              http://github.com/jruby/%{name}
Source0:          https://github.com/jruby/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.zip
Patch1:           joni-remove-useless-wagon-dependency.patch

BuildRequires:    java-devel
BuildRequires:    jcodings
BuildRequires:    jpackage-utils
BuildRequires:    junit
BuildRequires:    maven-local
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-surefire-plugin
BuildRequires:    sonatype-oss-parent

BuildRequires:    objectweb-asm

Requires:         jcodings
Requires:         jpackage-utils
Requires:         objectweb-asm

BuildArch:      noarch


%description
joni is a port of Oniguruma, a regular expressions library,
to java. It is used by jruby.

%package javadoc
Summary:        Javadoc for %{name}
Requires:       jpackage-utils

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}
%patch1 -p0

# fixes rpmlint warning about wrong-file-end-of-line-encoding
sed -i -e 's|\r||' test/org/joni/test/TestC.java
sed -i -e 's|\r||' test/org/joni/test/TestU.java
sed -i -e 's|\r||' test/org/joni/test/TestA.java

%mvn_file : %{name}

%build
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc MANIFEST.MF

%files javadoc -f .mfiles-javadoc

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Sep 24 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.1.3-4
- Update requires on objectweb-asm

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jan 05 2015 Mo Morsi <mmorsi@redhat.com> - 2.1.3-1
- Update to 2.1.3

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 1.1.9-4
- Use Requires: java-headless rebuild (#1067528)

* Mon Aug 12 2013 Alexander Kurtakov <akurtako@redhat.com> 1.1.9-3
- Start using xmvn.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Feb 26 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 1.1.9-1
- Updated to version 1.1.9.
- Switched from ant to maven.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Oct 09 2012 gil cattaneo <puntogil@libero.it> - 1.1.3-8
- add maven pom
- adapt to current guideline

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Feb 22 2010 Mohammed Morsi <mmorsi@redhat.com> - 1.1.3-4
- fixed end of line encoding rpmlint warning
- removed uneccessary deps

* Wed Feb 17 2010 Mohammed Morsi <mmorsi@redhat.com> - 1.1.3-3
- removed gcj bits
- updated package to conform to guidelines based on feedback
- corrected source url

* Fri Jan 22 2010 Mohammed Morsi <mmorsi@redhat.com> - 1.1.3-2
- Unorphaned / updated package

* Fri Mar 6 2009 Conrad Meyer <konrad@tylerc.org> - 1.1.3-1
- Bump to 1.1.3.

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Dec 12 2008 Conrad Meyer <konrad@tylerc.org> - 1.1.2-1
- Bump to 1.1.2.

* Fri Nov 28 2008 Conrad Meyer <konrad@tylerc.org> - 1.1.1-1
- Bump to 1.1.1.

* Sun Aug 31 2008 Conrad Meyer <konrad@tylerc.org> - 1.0.3-1
- Official 1.0.3 release.

* Sat Jul 19 2008 Conrad Meyer <konrad@tylerc.org> - 1.0.3-0.3.svn7235
- Build AOT bits.

* Sat Jul 19 2008 Conrad Meyer <konrad@tylerc.org> - 1.0.3-0.2.svn7235
- Bump revision because of stupid packager's mistake.

* Sat Jul 19 2008 Conrad Meyer <konrad@tylerc.org> - 1.0.3-0.1.svn7235
- Bump to trunk version of joni for JRuby 1.1.3.
- Switch to noarch for fc10 and up.

* Sat Apr 5 2008 Conrad Meyer <konrad@tylerc.org> - 1.0.2-4
- Compile AOT bits.

* Sun Mar 16 2008 Conrad Meyer <konrad@tylerc.org> - 1.0.2-3
- Bump to 1.0.2.
- Add pom.xml to doc.
- Install unversioned jar.

* Sun Mar 2 2008 Conrad Meyer <konrad@tylerc.org> - 1.0.1-2
- joni is MIT, not BSD.
- Require java and BuildRequire java-devel, not icedtea.

* Sun Mar 2 2008 Conrad Meyer <konrad@tylerc.org> - 1.0.1-1
- Initial package.
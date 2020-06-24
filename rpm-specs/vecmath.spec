%global commit 41fddda1a4f430e45bef0154e1fdfe5671025f1e
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:          vecmath
Version:       1.6.0
Release:       0.13.20130710git41fddda%{?dist}
Summary:       The 3D vector math Java package, javax.vecmath
# License is GNU General Public License, version 2, with the Classpath Exception
License:       GPLv2 with exceptions
URL:           http://github.com/hharrison/vecmath
Source0:       https://github.com/hharrison/vecmath/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz
# missing pom file
# https://bugzilla.redhat.com/show_bug.cgi?id=1022506
Source1:       https://repo1.maven.org/maven2/javax/vecmath/vecmath/1.5.2/vecmath-1.5.2.pom
# Fix link to javadoc and javadoc errors
Patch0:        vecmath-javadoc.patch
BuildArch:     noarch

BuildRequires: ant
BuildRequires: java-devel >= 1:1.6.0
BuildRequires: java-javadoc
BuildRequires: javapackages-local

Requires:      java-headless >= 1:1.6.0

%description
The 3D vector math Java package, javax.vecmath.

%package javadoc
Summary:       Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -qn %{name}-%{commit}
%patch0 -p1
sed -e "s|<version>1.5.2</version>|<version>1.6.0</version>|" %{SOURCE1} > %{name}.pom
%mvn_file javax.vecmath:vecmath %{name}

%build
%ant

%install
%mvn_artifact %{name}.pom build/jars/%{name}.jar
%mvn_install -J build/javadoc

%files -f .mfiles
%doc docs/api-changes* COPYRIGHT.txt LICENSE.txt LICENSE-SPEC.html

%files javadoc -f .mfiles-javadoc
%doc COPYRIGHT.txt LICENSE.txt LICENSE-SPEC.html

%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-0.13.20130710git41fddda
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-0.12.20130710git41fddda
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-0.11.20130710git41fddda
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-0.10.20130710git41fddda
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-0.9.20130710git41fddda
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-0.8.20130710git41fddda
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-0.7.20130710git41fddda
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-0.6.20130710git41fddda
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Sep 24 2015 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> - 1.6.0-0.5.20130710git41fddda
- build with maven
- re-add maven pom (rhbz#1022506)
- fix javadoc errors

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-0.4.20130710git41fddda
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-0.3.20130710git41fddda
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 1.6.0-0.2.20130710git41fddda
- Use Requires: java-headless rebuild (#1067528)

* Thu Sep 5 2013 Harvey Harrison <harvey.harrison@gmail.com> - 1.6.0-0.1.20130710git41fddda
- change upstream source to github
- upgrade to 1.6.0

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Sep 07 2012 gil cattaneo <puntogil@libero.it> 1.5.2-1
- Use tarball from 1.5.2 tag (no change in source code)
- Added maven pom
- Adapt to current guideline
- Added javadoc sub package

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-5.20090922cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-4.20090922cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-3.20090922cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Sep 28 2009 Jussi Lehtola <jussilehtola@fedoraproject.org> - 0-2.20090922cvs
- Minor review fixes.

* Tue Sep 22 2009 Jussi Lehtola <jussilehtola@fedoraproject.org> - 0-1.20090922cvs
- First release.

%global    _version 2.0.17
%global    _compat_version 1.1.0

Name:      lpg
Version:   %{_version}
Release:   30%{?dist}
Summary:   LALR Parser Generator
# although the text of the licence isn't distributed with some of the source,
# the author has exlicitly stated that everything is covered under the EPL
# see: http://sourceforge.net/forum/forum.php?thread_id=3277926&forum_id=523519
License:   EPL-1.0
URL:       http://lpg.sourceforge.net/

Source0:   http://downloads.sourceforge.net/lpg/lpg-java-runtime-src-%{version}.zip
Source1:   http://downloads.sourceforge.net/lpg/lpg-generator-cpp-src-%{version}.zip
Source2:   http://downloads.sourceforge.net/lpg/lpg-generator-templates-%{version}.zip

# source archive for the java compat lib
Source3:   http://downloads.sourceforge.net/lpg/lpgdistribution-05-16-06.zip

# upstream does not provide a build script or manifest file for the java
# compat lib
Source4:   %{name}-build.xml
Source5:   %{name}-manifest.mf

# TODO: drop Source3, 4, 5 and obsolete the java-compat package when dependent
# projects are ported to LPG 2.x.x

# executable name in the bootstrap make target is wrong; sent upstream, see:
# https://sourceforge.net/tracker/?func=detail&aid=2794057&group_id=155963&atid=797881
Patch0:    %{name}-bootstrap-target.patch

# change build script to build the base jar with osgi bundle info
Patch1:    %{name}-osgi-jar.patch

# fix segfault caused by aggressive optimisation of null checks in gcc 4.9
Patch2:    %{name}-segfault.patch

BuildRequires: gcc-c++
BuildRequires: make

BuildRequires: ant
BuildRequires: ant-apache-regexp
BuildRequires: javapackages-local

%description
The LALR Parser Generator (LPG) is a tool for developing scanners and parsers
written in Java, C++ or C. Input is specified by BNF rules. LPG supports
backtracking (to resolve ambiguity), automatic AST generation and grammar
inheritance.

%package       java
Summary:       Java runtime library for LPG

BuildArch:     noarch

%description   java
Java runtime library for parsers generated with the LALR Parser Generator
(LPG).

%package       java-compat
Version:       %{_compat_version}
Summary:       Compatibility Java runtime library for LPG 1.x

BuildArch:     noarch

%description   java-compat
Compatibility Java runtime library for parsers generated with the LALR Parser
Generator (LPG) 1.x.

%prep
%setup -q -T -c -n %{name}-%{version}

# because you can't use setup to unzip to subdirectories when your source
# archives do not create top level directories
unzip -qq %{SOURCE0} -d lpg-java-runtime
unzip -qq %{SOURCE1} -d lpg-generator-cpp
unzip -qq %{SOURCE2} -d lpg-generator-templates
chmod -Rf a+rX,u+w,g-w,o-w .

# setup java compat stuff
%setup -q -D -T -a 3 -n %{name}-%{version}
cp -p %{SOURCE4} lpgdistribution/build.xml
cp -p %{SOURCE5} lpgdistribution/MANIFEST.MF

# apply patches
%patch0 -p0 -b .orig
%patch1 -p0 -b .orig
%patch2 -p0 -b .orig

%build
# build java stuff
(cd lpg-java-runtime && ant -f exportPlugin.xml)

# build java compat stuff
(cd lpgdistribution && ant)

# build native stuff
pushd lpg-generator-cpp/src

# ARCH just tells us what tools to use, so this can be the same on all arches
# we build twice in order to bootstrap the grammar parser
make clean install ARCH=linux_x86 \
  LOCAL_CFLAGS="%{optflags} -Wno-strict-overflow" LOCAL_CXXFLAGS="%{optflags} -Wno-strict-overflow"
make bootstrap ARCH=linux_x86
make clean install ARCH=linux_x86 \
  LOCAL_CFLAGS="%{optflags} -Wno-strict-overflow" LOCAL_CXXFLAGS="%{optflags} -Wno-strict-overflow"

popd

%install
# Install native stuff
install -pD -T lpg-generator-cpp/bin/%{name}-linux_x86 \
  %{buildroot}%{_bindir}/%{name}

# Install java stuff
%mvn_package "lpg.runtime:java" java
%mvn_package "net.sourceforge.lpg:lpgjavaruntime" java-compat
%mvn_artifact "lpg.runtime:java:%{_version}" lpg-java-runtime/lpgruntime.jar
%mvn_artifact "net.sourceforge.lpg:lpgjavaruntime:%{_compat_version}" lpgdistribution/lpgjavaruntime.jar
%mvn_file "lpg.runtime:" lpgruntime
%mvn_file "net.sourceforge.lpg:" lpgjavaruntime
%mvn_install

%files
%doc lpg-generator-templates/docs/*
%{_bindir}/%{name}

%files java -f .mfiles-java
%doc lpg-java-runtime/Eclipse*.htm

%files java-compat -f .mfiles-java-compat
%doc lpg-java-runtime/Eclipse*.htm

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.17-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.17-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 11 2019 Mat Booth <mat.booth@redhat.com> - 2.0.17-28
- Fix license tag

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.17-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.17-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.17-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Aug 08 2017 Mat Booth <mat.booth@redhat.com> - 2.0.17-24
- Install with xmvn

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.17-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.17-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.17-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb  1 2017 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.0.17-20
- Add missing build-requires on GCC

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.17-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jul 10 2015 Mat Booth <mat.booth@redhat.com> - 2.0.17-18
- Add Wno-strict-overflow flag to remove unnecessary warning about subtracting
  one from an index value.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.17-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.0.17-16
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.17-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jun 16 2014 Mat Booth <mat.booth@redhat.com> - 2.0.17-14
- Patch to fix segfault caused by aggressive optimisation of null checks in gcc 4.9

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.17-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 11 2014 Mat Booth <fedora@matbooth.co.uk> - 2.0.17-12
- Drop versioned jars and switch to R: java-headless
  RHBZ #1068378 and #1022141

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.17-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Feb 16 2013 Mat Booth <fedora@matbooth.co.uk> - 2.0.17-10
- Fix rpm %%doc parsing by globbing instead of escaping.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.17-9.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.17-8.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.17-7.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.17-6.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Oct 05 2010 jkeating - 2.0.17-5.1
- Rebuilt for gcc bug 634757

* Mon Sep 13 2010 Mat Booth <fedora@matbooth.co.uk> 2.0.17-5
- Re-patch the OSGi manifest because for some reason Eclipse Orbit decided
  not to use the same symbolic bundle name as LPG upstream did.

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 15 2009 Mat Booth <fedora@matbooth.co.uk> 2.0.17-3
- Add missing build dependency on ant-apache-regexp.
- Remove empty sub-package that was accidentally left.

* Sun Jul 05 2009 Mat Booth <fedora@matbooth.co.uk> 2.0.17-2
- Add version constants so we get the correct version numbers on the java
  libraries.

* Sat Jul 04 2009 Mat Booth <fedora@matbooth.co.uk> 2.0.17-1
- Update to 2.0.17.
- Add OSGI manifest info to the runtime jar.
- Bundle generator docs with the generator in the main package.

* Tue May 19 2009 Mat Booth <fedora@matbooth.co.uk> 2.0.16-2
- Better document source files/patches.

* Tue Apr 28 2009 Mat Booth <fedora@matbooth.co.uk> 2.0.16-1
- Initial release of version 2.

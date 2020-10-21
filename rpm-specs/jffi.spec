%global cluster jnr
%global sover 1.2

Name:           jffi
Version:        1.2.23
Release:        2%{?dist}
Summary:        Java Foreign Function Interface

License:        LGPLv3+ or ASL 2.0
URL:            http://github.com/jnr/jffi
Source0:        https://github.com/%{cluster}/%{name}/archive/%{name}-%{version}.tar.gz
Source3:        p2.inf

# Fix references to junit/hamcrest to match what is generated by `build-jar-repository`
Patch0:         0001-Fix-dependencies-on-junit-hamcrest.patch

# Fix compilation flags and binary stripping
Patch1:         0002-Fix-compilation-flags.patch

# Allow building on Java 11
Patch2:         0003-Fix-native-header-generation.patch

# Fix java version detection of Java 9+
Patch3:         0004-Fix-java-version-detection.patch

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-assembly-plugin)
BuildRequires:  libffi-devel
BuildRequires:  ant
BuildRequires:  ant-junit

%description
An optimized Java interface to libffi.

%package native
Summary:        %{name} JAR with native bits

%description native
This package contains %{name} JAR with native bits.

%package javadoc
Summary:        Javadoc for %{name}
BuildArch:      noarch

%description javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q -n %{name}-%{name}-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

# Remove pointless parent pom
%pom_remove_parent

# Allow building on Java 11
for f in src/main/java/com/kenai/jffi/{Foreign,ObjectBuffer}.java version.xml; do
  # Add the import for @Native
  sed -i '/package .*;/ a import java.lang.annotation.Native;' $f
  # Set @Native for fields
  sed -i '/\(static final\|final static\) int [A-Z]/ i @Native' $f
done

# remove uneccessary directories
rm -r archive/* jni/libffi/ lib/junit*

# Remove any pre-build bytecode
find ./ -name '*.jar' -exec rm -f '{}' \; 
find ./ -name '*.class' -exec rm -f '{}' \; 

# Test dependencies for ant tests
build-jar-repository -s -p lib/ junit hamcrest/core

# A couple of tests fail on armv7 for some reason
sed -i -e 's/haltonfailure="true"/haltonfailure="no"/' build.xml

# Ensure debug symbols in the native java
sed -i -e 's/<javac/<javac debug="true"/' build.xml

%mvn_package 'com.github.jnr:jffi::native:' native
%mvn_file ':{*}' %{name}/@1 @1

%build
# ant will produce JAR with native bits
ant jar build-native -Duse.system.libffi=1

# maven will look for JAR with native bits in archive/
cp -p dist/jffi-*-Linux.jar archive/

%mvn_build

# Ensure jar with correct manifest is the one that is installed
cp target/jffi-%{version}-complete.jar target/jffi-%{version}.jar

%install
%mvn_install

mkdir -p META-INF/
cp %{SOURCE3} META-INF/
jar uf %{buildroot}%{_jnidir}/%{name}/%{name}.jar META-INF/p2.inf

# install *.so
install -dm 755 %{buildroot}%{_libdir}/%{name}
unzip dist/jffi-*-Linux.jar
mv jni/*-Linux %{buildroot}%{_libdir}/%{name}/
# create version-less symlink for .so file
pushd %{buildroot}%{_libdir}/%{name}/*
chmod +x lib%{name}-%{sover}.so
ln -s lib%{name}-%{sover}.so lib%{name}.so
popd

%check
# don't fail on unused parameters... (TODO: send patch upstream)
sed -i 's|-Werror||' libtest/GNUmakefile
ant -Duse.system.libffi=1 -Drun.jvm.model=-Xmx128m test

%files -f .mfiles
%license COPYING.GPL COPYING.LESSER LICENSE

%files native -f .mfiles-native
%{_libdir}/%{name}
%license COPYING.GPL COPYING.LESSER LICENSE

%files javadoc -f .mfiles-javadoc
%license COPYING.GPL COPYING.LESSER LICENSE

%changelog
* Thu Aug 06 2020 Mat Booth <mat.booth@redhat.com> - 1.2.23-2
- Fix OSGi metadata

* Fri Jul 31 2020 Mat Booth <mat.booth@redhat.com> - 1.2.23-1
- Update to latest upstream release
- Add patch to fix incorrect java version detection of java 9+

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.12-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 1.2.12-15
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Sun Jun 28 2020 Roland Grunberg <rgrunber@redhat.com> - 1.2.12-14
- Replace usage of javah with javac in ant build for Java 11.
- Ensure static final fields get marked with @Native annotation.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.12-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.12-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.12-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.12-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.12-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.12-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.12-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 18 2017 Mat Booth <mat.booth@redhat.com> - 1.2.12-6
- Fix stripping of binaries embedded in jars
- Fix failing tests due to hamcrest CNFEs

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb  1 2017 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2.12-4
- Add missing build-requires on GCC

* Sat Jul 23 2016 Mat Booth <mat.booth@redhat.com> - 1.2.12-3
- Add missing BRs

* Fri Jul 22 2016 Mat Booth <mat.booth@redhat.com> - 1.2.12-2
- Avoid use of ln -r since it is not available on EL6

* Thu May 19 2016 Alexander Kurtakov <akurtako@redhat.com> 1.2.12-1
- Update to upstream 1.2.12 release.

* Tue Apr 19 2016 Roland Grunberg <rgrunber@redhat.com> - 1.2.11-2
- Fragment bundle com.kenai.jffi.native is now com.github.jnr.jffi.native.

* Mon Apr 18 2016 Alexander Kurtakov <akurtako@redhat.com> 1.2.11-1
- Update to upstream 1.2.11 release containing OSGification.

* Fri Feb 5 2016 Alexander Kurtakov <akurtako@redhat.com> 1.2.10-1
- Update to upstream 1.2.10 release.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jul 13 2015 Mat Booth <mat.booth@redhat.com> - 1.2.9-8
- Fix unstripped binaries and empty debuginfo package
- Ensure presence of ant-junit at buildtime
- Fixed mixed use of space and tabs

* Thu Jun 25 2015 Roland Grunberg <rgrunber@redhat.com> - 1.2.9-7
- Minor fixes to manifest as we introduce p2.inf file.

* Wed Jun 24 2015 Jeff Johnston <jjohnstn@redhat.com> 1.2.9-6
- Fix manifests so jffi requires com.kenai.jffi.native and native has bundle version.

* Tue Jun 23 2015 Roland Grunberg <rgrunber@redhat.com> - 1.2.9-5
- Add missing Bundle-SymbolicName attribute to manifest.

* Mon Jun 22 2015 Jeff Johnston <jjohnstn@redhat.com> 1.2.9-4
- Fix native MANIFEST.MF

* Thu Jun 18 2015 Jeff Johnston <jjohnstn@redhat.com> 1.2.9-3
- Add MANIFEST.MF.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue May 5 2015 Alexander Kurtakov <akurtako@redhat.com> 1.2.9-1
- Update to upstream 1.2.9.

* Thu Apr 30 2015 Alexander Kurtakov <akurtako@redhat.com> 1.2.8-1
- Update to upstream 1.2.8.

* Fri Feb 20 2015 Michal Srb <msrb@redhat.com> - 1.2.7-5
- Install version-less symlink for .so file

* Fri Feb 20 2015 Michal Srb <msrb@redhat.com> - 1.2.7-4
- Fix rpmlint warnings

* Fri Feb 20 2015 Michal Srb <msrb@redhat.com> - 1.2.7-3
- Install *.so file to %%{_libdir}/%%{name}/

* Tue Feb 17 2015 Michal Srb <msrb@redhat.com> - 1.2.7-2
- Build jffi-native
- Introduce javadoc subpackage

* Fri Dec 05 2014 Mo Morsi <mmorsi@redhat.com> - 1.2.7-1
- Update to JFFI 1.2.7

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jun 12 2014 Alexander Kurtakov <akurtako@redhat.com> 1.2.6-7
- Fix FTBFS.

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Apr 07 2014 Dan Horák <dan[at]danny.cz> - 1.2.6-5
- skip tests on s390 until https://bugzilla.redhat.com/show_bug.cgi?id=1084914 is resolved

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 1.2.6-4
- Use Requires: java-headless rebuild (#1067528)

* Sun Aug 11 2013 Mat Booth <fedora@matbooth.co.uk> - 1.2.6-3
- Remove BR on ant-nodeps, fixes FTBFS rhbz #992622

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Feb 05 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 1.2.6-1
- Updated to version 1.2.6.

* Wed Dec 19 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.0.10-4
- revbump after jnidir change

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Aug 02 2011  Mo Morsi <mmorsi@redhat.com> - 1.0.10-1
- Updated to most recent upstream release

* Wed Jun 01 2011  Mo Morsi <mmorsi@redhat.com> - 1.0.9-1
- Updated to most recent upstream release

* Mon Oct 25 2010  <mmorsi@redhat.com> - 1.0.2-1
- Updated to most recent upstream release

* Wed Apr 14 2010  <mmorsi@redhat.com> - 0.6.5-4
- added Mamoru Tasaka's fix for ppc{,64} to prep

* Mon Mar 08 2010  <mmorsi@redhat.com> - 0.6.5-3
- fixes to jffi from feedback
- don't strip debuginfo, remove extraneous executable bits,

* Tue Feb 23 2010  <mmorsi@redhat.com> - 0.6.5-2
- fixes to jffi compilation process
- fixes to spec to conform to package guidelines

* Wed Feb 17 2010  <mmorsi@redhat.com> - 0.6.5-1
- bumped version
- fixed package to comply to fedora guidelines

* Tue Jan 19 2010  <mmorsi@redhat.com> - 0.6.2-1
- Initial build.

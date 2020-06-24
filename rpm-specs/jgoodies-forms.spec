%define shortname forms

Name:           jgoodies-forms
Version:        1.8.0
Release:        11%{?dist}
Summary:        Framework to lay out and implement elegant Swing panels in Java

License:        BSD
URL:            http://www.jgoodies.com/freeware/forms/
Source0:        http://www.jgoodies.com/download/libraries/%{shortname}/%{name}-%(tr "." "_" <<<%{version}).zip

# Fontconfig and DejaVu fonts needed for tests
BuildRequires:  dejavu-sans-fonts
BuildRequires:  fontconfig
BuildRequires:  maven-local
BuildRequires:  mvn(com.jgoodies:jgoodies-common) >= 1.8.0
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)
BuildArch:      noarch

%description
The JGoodies Forms framework helps you lay out and implement elegant Swing
panels quickly and consistently. It makes simple things easy and the hard stuff
possible, the good design easy and the bad difficult.


%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
This package contains the API documentation for %{name}.


%prep
%autosetup

# Unzip source and test files from provided JARs
mkdir -p src/main/java/ src/test/java/
pushd src/main/java/
jar -xf ../../../%{name}-%{version}-sources.jar
popd
pushd src/test/java/
jar -xf ../../../%{name}-%{version}-tests.jar
popd

# Delete prebuild JARs
find -name "*.jar" -exec rm {} \;

# Drop tests that require a running X11 server
rm src/test/java/com/jgoodies/forms/layout/SerializationTest.java
sed -i "/SerializationTest.class,/d" src/test/java/com/jgoodies/forms/layout/AllFormsTests.java

# Delete ClassLoader test
# TODO: fix it to make it work
rm src/test/java/com/jgoodies/forms/layout/ClassLoaderTest.java
sed -i "/ClassLoaderTest.class,/d" src/test/java/com/jgoodies/forms/layout/AllFormsTests.java

# Fix wrong end-of-line encoding
for file in LICENSE.txt RELEASE-NOTES.txt; do
  sed -i.orig "s/\r//" $file && \
  touch -r $file.orig $file && \
  rm $file.orig
done

%mvn_file :%{name} %{name} %{name}


%build
%mvn_build


%install
%mvn_install


%files -f .mfiles
%doc README.html RELEASE-NOTES.txt
%license LICENSE.txt


%files javadoc -f .mfiles-javadoc


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 17 2017 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.8.0-5
- Add missing BR on mvn(org.sonatype.oss:oss-parent:pom:)
- Spec cleanup

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 13 2014 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.8.0-1
- Update to 1.8.0

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Feb 12 2014 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.7.2-1
- Update to 1.7.2

* Fri Aug 16 2013 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.7.1-3
- Update for newer guidelines

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat May 11 2013 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.7.1-1
- Update to 1.7.1

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.6.0-2
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Wed Jan 02 2013 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.6.0-1
- Update to 1.6.0

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu May 10 2012 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.5.1-1
- Update to 1.5.1

* Wed Feb 15 2012 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.5.0-1
- Update to 1.5.0

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Dec 16 2011 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.4.2-1
- Update to 1.4.2
- Spec cleanup

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon May 19 2008 Mary Ellen Foster <mefoster at gmail.com> 1.2.0-1
- Update to 1.2.0

* Tue Oct 16 2007 Mary Ellen Foster <mefoster at gmail.com> 1.1.0-2
- Fix encoding on HTML files
- Use empty CLASSPATH when building
- Fix indentation in spec file

* Wed Sep  5 2007 Mary Ellen Foster <mefoster at gmail.com> 1.1.0-1
- Initial version for Fedora, based on JPackage spec by Eric Lavarde

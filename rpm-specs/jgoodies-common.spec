%global shortname common

Name:           jgoodies-common
Version:        1.8.1
Release:        8%{?dist}
Summary:        Common library shared by JGoodies libraries and applications

License:        BSD
URL:            http://www.jgoodies.com/
Source0:        http://www.jgoodies.com/download/libraries/%{shortname}/%{name}-%(tr "." "_" <<<%{version}).zip

# fontconfig and DejaVu fonts needed for tests
BuildRequires:  dejavu-sans-fonts
BuildRequires:  fontconfig
BuildRequires:  maven-local
BuildArch:      noarch

%description
The JGoodies Common library provides convenience code for other JGoodies
libraries and applications.


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

# Remove DOS line endings
for file in LICENSE.txt RELEASE-NOTES.txt; do
  sed 's|\r||g' $file > $file.new && \
  touch -r $file $file.new && \
  mv $file.new $file
done

# remove unnecessary dependency on parent POM
%pom_remove_parent

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
* Sun Aug 30 2020 Fabio Valentini <decathorpe@gmail.com> - 1.8.1-8
- Remove unnecessary dependency on parent POM.

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 1.8.1-6
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 30 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.8.1-1
- Update to 1.8.1

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

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 1.7.0-2
- Use Requires: java-headless rebuild (#1067528)

* Wed Feb 12 2014 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.7.0-1
- Update to 1.7.0

* Fri Aug 16 2013 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.6.0-3
- Update for newer guidelines

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat May 11 2013 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.6.0-1
- Update to 1.6.0

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.4.0-2
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Tue Jan 01 2013 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.4.0-1
- Update to 1.4.0

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu May 03 2012 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.3.1-1
- Update to 1.3.1

* Wed Feb 15 2012 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.3.0-1
- Update to 1.3.0

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Sep 03 2011 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.2.1-1
- Update to 1.2.1

* Sat Feb 19 2011 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.1.1-2
- Remove obsolete clean section and BuildRoot tag

* Wed Feb 09 2011 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.1.1-1
- Initial RPM release

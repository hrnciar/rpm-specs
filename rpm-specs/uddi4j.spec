Name:		uddi4j
Version:	2.0.5
Release:	23%{?dist}
Summary:	Universal Description, Discovery and Integration registry API for Java
License:	IBM
URL:		http://sourceforge.net/projects/uddi4j/

Source0:	http://downloads.sf.net/project/uddi4j/uddi4j/%{version}/uddi4j-src-%{version}.zip
Source1:	%{name}-MANIFEST.MF

# A couple of utf8 incompatible chars prevent compile
Patch0:		uddi4j-remove-nonutf8-chars.patch

BuildArch:	noarch

BuildRequires:	ant
BuildRequires:	javapackages-local

%description
UDDI4J is a Java class library that provides an API to interact with a 
UDDI (Universal Description, Discovery and Integration) registry.

%package javadoc
Summary:	Javadocs for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}
%patch0 -p1

find -name '*.class' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;

# Disable java 8 doclinting
sed -i -e '/<javadoc/aadditionalparam="-Xdoclint:none"' build.xml

%build
ant -Djavac.executable=javac compile javadocs

%install
# inject OSGi manifests
mkdir -p META-INF
cp -p %{SOURCE1} META-INF/MANIFEST.MF
touch META-INF/MANIFEST.MF
zip -u build/lib/%{name}.jar META-INF/MANIFEST.MF

%mvn_artifact "org.uddi4j:uddi4j:%{version}" build/lib/uddi4j.jar
%mvn_file ":uddi4j" uddi4j
%mvn_install -J build/javadocs

%files -f .mfiles
%license LICENSE.html
%doc ReleaseNotes.html

%files javadoc -f .mfiles-javadoc
%license LICENSE.html

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 11 2020 Jiri Vanek <jvanek@redhat.com> - 2.0.5-22
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Apr 13 2018 Mat Booth <mat.booth@redhat.com> - 2.0.5-17
- Remove dep on obsolete axis

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Aug 07 2017 Mat Booth <mat.booth@redhat.com> - 2.0.5-15
- Modernise spec file

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Gerard Ryan <galileo@fedoraproject.org> - 2.0.5-10
- Remove old maven depmap stuff

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Feb 25 2014 Gerard Ryan <galileo@fedoraproject.org> - 2.0.5-8
- RHBZ#1068576: Switch to java-headless requires

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 01 2012 Gerard Ryan <galileo@fedoraproject.org> - 2.0.5-4
- Remove Bundle-Classpath from MANIFEST.MF
- Update Source0 URL so it's not just relying on one mirror

* Tue May 29 2012 Gerard Ryan <galileo@fedoraproject.org> - 2.0.5-3
- Add line to copy javadocs

* Tue May 29 2012 Gerard Ryan <galileo@fedoraproject.org> - 2.0.5-2
- Fix rpmlint issues: source urls; tabs and space warnings
- Remove BuildDate.txt and ReleaseNotes.html from javadoc
- Drop -version from javadoc install path
- Change group to Development/Libraries
- Remove defattr(-,root,root,-)
- Remove rm -rf RPM_BUILD_ROOT

* Mon May 28 2012 Gerard Ryan <galileo@fedoraproject.org> - 2.0.5-1
- Initial packaging

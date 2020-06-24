Name:		wsil4j
Version:	1.0
Release:	21%{?dist}
Summary:	Web Services Inspection Language for Java API

License:	ASL 1.1
URL:		http://svn.apache.org/repos/asf/webservices/archive/wsil4j/

# svn co http://svn.apache.org/repos/asf/webservices/archive/wsil4j/trunk/java/ wsil4j-1.0
# tar -cJf wsil4j-1.0.tar.xz wsil4j-1.0
Source0:	%{name}-%{version}.tar.xz
Source1:	%{name}-MANIFEST.MF 
Source2:	%{name}-%{version}.pom
BuildArch:	noarch

BuildRequires:	ant
BuildRequires:	uddi4j
BuildRequires:	wsdl4j
BuildRequires:	javapackages-local

%description
The Web Services Inspection Language (WS-Inspection) provides a distributed Web
service discovery method, by specifying how to inspect a web site for available
Web services. The WS-Inspection specification defines the locations on a Web
site where you could look for Web service descriptions.

%package javadoc
Summary:	Javadocs for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q

find -name '*.class' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;

# Disable java 8 doclinting
sed -i -e '/<javadoc/aadditionalparam="-Xdoclint:none"' build.xml

%build
ant -DCLASS_PATH=$(build-classpath uddi4j wsdl4j) compile javadocs

%install
# inject OSGi manifest
mkdir -p META-INF
cp -p %{SOURCE1} META-INF/MANIFEST.MF
touch META-INF/MANIFEST.MF
zip -u build/lib/%{name}.jar META-INF/MANIFEST.MF

%mvn_artifact %{SOURCE2} build/lib/wsil4j.jar
%mvn_file ":wsil4j" wsil4j
%mvn_install -J build/javadocs

%files -f .mfiles
%license LICENSE
%doc docs
%doc README.htm

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Apr 13 2018 Mat Booth <mat.booth@redhat.com> - 1.0-17
- Remove dep on obsolete axis

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Aug 07 2017 Mat Booth <mat.booth@redhat.com> - 1.0-15
- Modernise spec file

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Gerard Ryan <galileo@fedoraproject.org> - 1.0-10
- Remove old maven depmap stuff

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Feb 24 2014 Gerard Ryan <galileo@fedoraproject.org> - 1.0-8
- Use java-headless instead of java

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 08 2012 Gerard Ryan <galileo@fedoraproject.org> - 1.0-4
- Fully removed dependency on xerces-j2

* Fri Jun 08 2012 Gerard Ryan <galileo@fedoraproject.org> - 1.0-3
- Added POM; removed dependency on xerces-j2

* Fri Jun 08 2012 Gerard Ryan <galileo@fedoraproject.org> - 1.0-2
- Added zip to BuildRequires

* Mon May 28 2012 Gerard Ryan <galileo@fedoraproject.org> - 1.0-1
- Initial packaging

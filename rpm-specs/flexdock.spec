Name:		    flexdock
Version:        1.2.4
Release:	    14%{?dist}
Summary:	    Docking framework for Java Swing GUI apps


#Licence is MIT on their website
License:	    MIT 
URL:		    http://forge.scilab.org/index.php/p/flexdock/

Source0:	    http://forge.scilab.org/index.php/p/flexdock/downloads/get/%{name}-%{version}.tar.gz

#Removes the java media framework from the demos to satisfy reqs
Patch1:		    flexdock-0001-nojmf.patch
#Modifies the build process  -- fedora specific
Patch2:		    flexdock-0002-fedora-build.patch
#Set javac source and target version to 1.8 to fix builds with Java 11
Patch3:         flexdock-0003-java-1.8.patch

BuildRequires:	java-devel
BuildRequires:	ant
BuildRequires:	jpackage-utils
BuildRequires:	jgoodies-common
BuildRequires:	jgoodies-looks
BuildRequires:	skinlf

Requires:       java
Requires:       jpackage-utils
Requires:       jgoodies-common
Requires:       jgoodies-looks
Requires:       skinlf

BuildArch:      noarch

%description
FlexDock is a Java docking framework for use in cross-platform
Swing applications.

%prep
%setup -q

%patch1 -p1
%patch2 -p1
%patch3 -p1

#Override the build file's default hard-coded paths
echo "sdk.home=%{java_home}" > workingcopy.properties

#JAR "dependency" handling
find ./ -name \*.jar -exec rm {} \;
build-jar-repository -s -p lib skinlf jgoodies-looks jgoodies-common

#Remove the jmf-using demo files
rm src/java/demo/org/flexdock/demos/raw/jmf/MediaPanel.java
rm src/java/demo/org/flexdock/demos/raw/jmf/JMFDemo.java

#Endline convert Doc files
for i in "LICENSE.txt README release-notes.txt" ;
do
    %{__sed} -i 's/\r//' $i
done

%build
ant jar

%install
mkdir -p %{buildroot}%{_javadir}
install -pm644 build/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

%files
%doc LICENSE.txt README release-notes.txt
%{_javadir}/*

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jul 19 2020 Fabio Valentini <decathorpe@gmail.com> - 1.2.4-13
- Set javac source and target to 1.8 to fix Java 11 builds.

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 1.2.4-12
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Aug 12 2013 Clément David <c.david86@gmail.com> - 1.2.4-1
- Update version to 1.2.4

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Feb 25 2013 Clément David <c.david86@gmail.com> - 1.2.3-1
- Update version

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 21 2013 Clément David <c.david86@gmail.com> - 1.2.2-2
- Update version to 1.2.2

* Thu Jan 03 2013 Clément David <c.david86@gmail.com> - 1.2.1-1
- Update version

* Fri Jul 27 2012 Clément David <c.david86@gmail.com> - 1.2.0-2
- Add the jcommons-logging dependency

* Wed Jul 25 2012 Clément David <c.david86@gmail.com> - 1.2.0-1
- Update version
- Change website url
- Remove the generate tarball script

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Aug 16 2011 Clément David <c.david86@gmail.com> 0.5.2-1
- Bump version
- Normalize patches
- Normalize tarball name and root

* Tue Sep 30 2008 <mycae(a!t)yahoo.com> 0.5.1-1
- Create spec file


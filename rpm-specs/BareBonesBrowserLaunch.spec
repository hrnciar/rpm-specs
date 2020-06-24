Name:          BareBonesBrowserLaunch
Version:       3.1
Release:       19%{?dist}
Summary:       Simple library to launch a browser window from Java
License:       Public Domain
URL:           http://www.centerkey.com/java/browser/
Source0:       http://www.centerkey.com/java/browser/myapp/real/bare-bones-browser-launch-%{version}.jar

BuildRequires: java-devel
BuildRequires: javapackages-local

BuildArch:     noarch

%description
Utility class to open a web page from a Swing application in the user's 
default browser. Supports: Mac OS X, GNU/Linux, Unix, Windows XP

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
This package contains the API documentation for %{name}

%prep
%setup -q -c

find * -name *.class -delete
rm -rf doc/*

%build

%{javac} com/centerkey/utils/BareBonesBrowserLaunch.java
%{jar} -cf %{name}.jar com/centerkey/utils/BareBonesBrowserLaunch.class
%{javadoc} -encoding UTF-8 -d doc com/centerkey/utils/BareBonesBrowserLaunch.java -windowtitle "%{name} %{version}"

%install
%mvn_artifact com.centerkey.utils:%{name}:%{version} %{name}.jar
%mvn_file com.centerkey.utils:%{name} %{name}
%mvn_install -J doc

%files -f .mfiles

%files javadoc -f .mfiles-javadoc

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Mar 01 2015 gil cattaneo <puntogil@libero.it> 3.1-10
- use new javapackage macros

* Sun Feb 15 2015 gil cattaneo <puntogil@libero.it> 3.1-9
- Add maven metadata
- Adapt to current guideline

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Oct 22 2013 Orion Poplawski <orion@cora.nwra.com> 3.1-2
- Ship unversioned jar (bug #1022081)

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 8 2010 Orion Poplawski <orion@cora.nwra.com> 3.1-1
- Update to 3.1

* Thu Jun 3 2010 Orion Poplawski <orion@cora.nwra.com> 3.0-1
- Update to 3.0
- Don't make javadoc require main package

* Wed Jan 6 2010 Orion Poplawski <orion@cora.nwra.com> 2.0-2
- Unversion javadoc dir

* Mon Dec 28 2009 Orion Poplawski <orion@cora.nwra.com> 2.0-1
- Update to 2.0
- Use upstream jar source directly
- Cleanup spec

* Thu Feb 5 2009 John Matthews <jmatthews@redhat.com> 1.5-1
- initial package

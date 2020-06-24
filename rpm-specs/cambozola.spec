Name:           cambozola
Version:        0.936
Release:        11%{?dist}
Summary:        A viewer for multipart jpeg streams
License:        GPLv2+
URL:            http://www.charliemouse.com/code/cambozola/index.html
Source0:        http://www.andywilcock.com/code/cambozola/%{name}-latest.tar.gz

#patch to add javadoc generation in build.xml
Patch0:         %{name}-add-javadoc.patch
# Update target/source flags for JDK11 compatibility
# https://fedoraproject.org/wiki/Changes/Java11#copr_preliminary_rebuild
Patch1:         %{name}-source-target.patch

BuildArch:      noarch

BuildRequires:  jpackage-utils
BuildRequires:  java-devel
BuildRequires:  ant
BuildRequires:  findutils
%{?el6:BuildRequires:  ant-nodeps}

Requires:       jpackage-utils
Requires:       java

%description
Cambozola is a very simple (cheesy!) viewer for multipart jpeg streams
that are often pumped out by a streaming webcam server,
sending over multiple images per second.

%package javadoc
Summary:        Javadoc for %{name}
Requires:       jpackage-utils

%description javadoc
This package contains the API documentation for %{name}.

%prep
%autosetup -p 1

# Remove pre-built JAR and class files
find -name '*.jar' -exec rm -f '{}' \;
find -name '*.class' -exec rm -f '{}' \;

%build
%ant javadoc
%ant

%install
mkdir -p %{buildroot}%{_javadir}
cp -p dist/%{name}.jar   \
  %{buildroot}%{_javadir}/%{name}.jar
cp -p dist/%{name}-server.jar   \
  %{buildroot}%{_javadir}/%{name}-server.jar

# javadoc
mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -rp javadoc/*  \
  %{buildroot}%{_javadocdir}/%{name}

%files
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-server.jar
%doc LICENSE README.html

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Mon May 04 2020 Andrew Bauer <zonexpertconsulting@outlook.com> - 0.936-11
- Patch target and source for compatibility with newer java
- Update specfile to recent packaging standards

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.936-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.936-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.936-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.936-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.936-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.936-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.936-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Dec 31 2016 Cédric OLIVIER <cedric.olivier@free.fr>  0.936-3
- Enable 0.936 on EL6 

* Mon Feb 08 2016 Cédric OLIVIER <cedric.olivier@free.fr>  0.936-2
- Update source location

* Thu Feb 04 2016 Cédric OLIVIER <cedric.olivier@free.fr>  0.936-1
- Update to 0.936

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.93-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.93-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.93-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Aug 05 2013 Cédric OLIVIER <cedric.olivier@free.fr>  0.93-1
- Update to 0.93
- Remove ant-nodeps build requires

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.92-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.92-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.92-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.92-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.92-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild


* Sun Jan 16 2011 Cédric OLIVIER <cedric.olivier@free.fr>  0.92-2
- According to Java packaging guidelines version removed from jar file name
- Reduce the spelling errors in description
- Remove clean section
- Remove unneeded requires in javadoc section

* Wed Dec 22 2010 Cédric OLIVIER <cedric.olivier@free.fr>  0.92-1
- Update to 0.92 release

* Sun Nov 21 2010 Cédric OLIVIER <cedric.olivier@free.fr>  0.80-1
- First release


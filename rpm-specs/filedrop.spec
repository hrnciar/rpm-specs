Summary:	Drag-and-drop support for Java
URL:		http://iharder.sourceforge.net/current/java/filedrop/
Name:		filedrop
License:	Public Domain
Version:	1.1
Release:	13%{?dist}

BuildArch:	noarch

Source0:	http://download.sourceforge.net/iharder/%{name}-%{version}.zip

BuildRequires:	java-devel >= 1:1.6.0
BuildRequires:	jpackage-utils
BuildRequires:	dos2unix

Requires:	java >= 1:1.6.0
Requires:	jpackage-utils

%description
FileDrop makes it easy to drag and drop files from the operating
system to a Java program. Any java.awt.Component can be dropped onto,
but only javax.swing.JComponents will indicate the drop event with a
changed border.

%prep
%setup -q

# fix line endings in source file
dos2unix FileDrop.java

# delete the supplied JAR file, we *must* build from source
rm filedrop.jar

%build
javac FileDrop.java
jar -cf %{name}.jar *.class

%install
export NO_BRP_CHECK_BYTECODE_VERSION=true

install -dm 755 %{buildroot}%{_javadir}/
install -m 644 %{name}.jar %{buildroot}%{_javadir}/


%files
%{_javadir}/%{name}.jar
%doc index.html files.gif filedrop.gif Example.java


%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 1.1-12
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 24 2012 Eric Smith <brouhaha@fedoraproject.org> - 1.1-2
- Use install directly rather than by macro, per Jason Tibbitts' advice
  in package review bug (#834964).

* Sun Jun 24 2012 Eric Smith <eric@brouhaha.com> - 1.1-1
- Initial version

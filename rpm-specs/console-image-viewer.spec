%global upstream ConsoleImageViewer
%global launcher consoleImageViewer

Name:    console-image-viewer

Version: 1.2
Release: 9%{?dist}
Summary: Terminal image viewer

License:  MIT
URL:      https://github.com/judovana/ConsoleImageViewer
Source0:  https://github.com/judovana/ConsoleImageViewer/archive/%{upstream}-%{version}.tar.gz
Source1:  %{launcher}.man

BuildArch: noarch

BuildRequires: java-devel
BuildRequires: ant

Requires: java-headless
Requires: javapackages-tools

%description
Highly scale-able, high quality, image viewer for ANSI terminals.


%prep
%setup -q -n %{upstream}-%{upstream}-%{version}
find -name '*.class' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;
sed 's;<attribute name="Main-Class" value="${main.class}"/>;;' -i nbproject/build-impl.xml

%build
ant


%install
mkdir -p $RPM_BUILD_ROOT/%{_javadir}
cp dist/%{upstream}.jar $RPM_BUILD_ROOT/%{_javadir}/%{upstream}.jar

mkdir -p $RPM_BUILD_ROOT/%{_bindir}/
cat <<EOF > $RPM_BUILD_ROOT/%{_bindir}/%{launcher}
#!/bin/bash
. /usr/share/java-utils/java-functions
MAIN_CLASS=org.judovana.linux.ConsoleImageViewer
set_classpath "%{upstream}-%{version}"
run \${@}
EOF

chmod 755 $RPM_BUILD_ROOT/%{_bindir}/%{launcher}

mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man1/
gzip -c %{SOURCE1}  > $RPM_BUILD_ROOT/%{_mandir}/man1/%{launcher}.1.gz

%files 
%{_javadir}/%{upstream}.jar
%{_bindir}/%{launcher}
%{_mandir}/man1/%{launcher}.1.gz


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Dec 02 2015 Jiri Vanek <jvanek@redhat.com> - 1.2-1
- initial package

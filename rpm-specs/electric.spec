Name:           electric
Version:        8.09
Release:        18%{?dist}
Summary:        Sophisticated ASIC and MEM CAD System

License:        GPLv3
URL:            http://www.staticfreesoft.com/

Source0:        ftp://ftp.gnu.org/pub/gnu/electric/%{name}-%{version}.jar
Source1:        %{name}.desktop
Source2:        %{name}.1

BuildRequires:  java-devel
BuildRequires:  ant
BuildRequires:  desktop-file-utils

Requires:       java
Requires:       electronics-menu

BuildArch:      noarch

%description
Electric is a sophisticated electrical CAD system that can handle
many forms of circuit design, including custom IC layout (ASICs),
schematic drawing, hardware description language specifications,
and electro-mechanical hybrid layout.


%package javadoc
Summary:        Javadocs for %{name}


%description javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q -T -c %{name}-%{version} -a 0

find -name '*.jar' -o -name '*.class' -exec rm -f '{}' \;

jar xf %{SOURCE0}

#wrong-file-end-of-line-encoding
sed -i 's/\r//' packaging/README.txt packaging/LicenseGNU.txt

%build
ant -verbose        \
    jarForGNUBinary \
    javadoc


%install
# generating empty directories
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_javadir}/%{name}

# real java binary created by this spec file
install -pm 0755 %{name}-%{version}.jar \
                 %{buildroot}%{_javadir}/%{name}/%{name}.jar


# dummy executable file to call %%{name}.jar
cat > %{name} << EOF
#!/bin/bash
java -jar %{_javadir}/%{name}/%{name}.jar
EOF
install -pm 0755 %{name} %{buildroot}%{_bindir}/%{name}

# Man page
install -d %{buildroot}%{_mandir}/man1/
install -pm 0644 %{SOURCE2} %{buildroot}%{_mandir}/man1/

# desktop file and its icon
desktop-file-install --vendor "" \
    --dir %{buildroot}%{_datadir}/applications \
    %{SOURCE1}
install -d %{buildroot}%{_datadir}/pixmaps/
install -pm 0644 com/sun/electric/tool/user/help/helphtml/iconplug.png \
                 %{buildroot}%{_datadir}/pixmaps/%{name}.png


# javadoc API
install -d %{buildroot}%{_javadocdir}/%{name}
%{__cp} -rp apidoc/* %{buildroot}%{_javadocdir}/%{name}


%files
%doc packaging/README.txt ChangeLog.txt packaging/LicenseGNU.txt
%{_bindir}/%{name}
%dir %{_javadir}/%{name}/
%{_javadir}/%{name}/%{name}.jar
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_mandir}/man1/%{name}.1.gz

%files javadoc
%{_javadocdir}/%{name}


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.09-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.09-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.09-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8.09-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8.09-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8.09-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8.09-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 8.09-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.09-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.09-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 25 2014 Michael Simacek <msimacek@redhat.com> - 8.09-8
- Remove version from JAR name

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.09-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.09-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.09-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Feb 17 2012 Deepak Bhole <dbhole@redhat.com> 8.09-4
- Resolves rhbz#791348
- Patch from Omair Majid <omajid@redhat.com> to remove explicit Java 6 req.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.09-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.09-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 23 2009 Chitlesh GOORAH <chitlesh [AT] fedoraproject DOT org> - 8.09-1
- new upstream release

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.08-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Feb 01 2009 Chitlesh GOORAH <chitlesh [AT] fedoraproject DOT org> - 8.08-2
- bugfix for RHBZ #483343

* Tue Dec 23 2008 Chitlesh GOORAH <chitlesh [AT] fedoraproject DOT org> - 8.08-1
- new upstream release

* Sun Dec 07 2008 Chitlesh GOORAH <chitlesh [AT] fedoraproject DOT org> - 8.07-2
- Added desktop-file-utils as BR

* Sat Nov 22 2008 Chitlesh GOORAH <chitlesh [AT] fedoraproject DOT org> - 8.07-1
- Updated to 8.07 and making electric compile for fedora.
- spec file was entirely revamped
- subpackage javadoc
- comply to electronics-menu structure and desktop file
- build arch : noarch

* Wed Jun 25 2008 Aanjhan Ranganathan <aanjhan@tuxmaniac.com> - 8.06-1
- Initial Fedora Package version 8.06


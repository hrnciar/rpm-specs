Name:           cortado
Version:        0.6.0
Release:        19%{?dist}
Summary:        Java media framework
URL:            http://www.theora.org/cortado/
# The codecs are all LGPLv2+, the jst framework is mixed, the player applet GPL
License:        LGPLv2+ and GPLv2+
Source0:        http://downloads.xiph.org/releases/%{name}/%{name}-%{version}.tar.gz
Patch0:         cortado-0.6.0-javadoc-fix.patch
BuildArch:      noarch
BuildRequires:  jpackage-utils java-devel jorbis
Requires:       java jpackage-utils jorbis

%description
Cortado is a Java media framework based on GStreamer's design.


%package javadoc
Summary:        Java docs for %{name}
Requires:       jpackage-utils

%description javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q
%patch0 -p1
# Remove included jorbis copy
rm -fr src/com/jcraft
# We don't want to include the examples in the jar we build
mv src/com/fluendo/examples .
# javac does not like the UTF-8 x, ∗, − and ’ symbols used in the comments
sed -i "s/×/x/g" src/com/fluendo/jheora/Quant.java
sed -i "s/∗/*/g" src/com/fluendo/jheora/Quant.java
sed -i "s/−/-/g" src/com/fluendo/jheora/Quant.java
sed -i "s/’/'/g" src/com/fluendo/jheora/Quant.java


%build
javac `find stubs -name "*.java"`
export CLASSPATH=stubs:%{_javadir}/jogg.jar:%{_javadir}/jorbis.jar:.
javac `find src -name "*.java"`
pushd src
jar cf %{name}.jar `find -name "*.class"`
popd
javadoc -d doc -public `find src -name "*.java"`


%install
mkdir -p $RPM_BUILD_ROOT%{_javadir}
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}
cp -a src/%{name}.jar $RPM_BUILD_ROOT%{_javadir}
cp -a doc $RPM_BUILD_ROOT%{_javadocdir}/%{name}


%files
%doc ChangeLog HACKING LICENSE.* NEWS README RELEASE TODO examples
%{_javadir}/%{name}.jar

%files javadoc
%doc LICENSE.*
%doc %{_javadocdir}/%{name}


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Hans de Goede <hdegoede@redhat.com> - 0.6.0-11
- Fix FTBFS

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jan 15 2012 Hans de Goede <hdegoede@redhat.com> - 0.6.0-5
- Fix building with the latest openjdk

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Nov 17 2010 Hans de Goede <hdegoede@redhat.com> 0.6.0-2
- Make javadoc package installable without the main package (#649781)

* Thu Nov  4 2010 Hans de Goede <hdegoede@redhat.com> 0.6.0-1
- Initial Fedora package

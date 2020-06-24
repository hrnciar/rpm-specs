Name:           logisim
Version:        2.7.1
Release:        11%{?dist}
Summary:        Educational tool for simulating digital logic circuits

License:        GPLv2+
URL:            http://www.cburch.com/logisim/
Source0:        http://downloads.sourceforge.net/project/circuit/2.7.x/%{version}/%{name}-generic-%{version}.jar
Source1:        logisim.desktop
Source2:        x-logisim-circuit.xml
Source3:        logisim.appdata.xml
Source4:        logisim-stats.png
Source5:        logisim.png

Patch1:         0001-Drop-Mac-specific-cruft.patch
Patch2:         0002-Port-to-jfontchooser-1.0.5.patch
Patch3:         0001-Use-stock-JColorChooser.patch

BuildRequires:  desktop-file-utils
BuildRequires:  java-devel
BuildRequires:  javahelp2
BuildRequires:  jfontchooser
BuildRequires:  libappstream-glib

Requires:       java
Requires:       javahelp2
Requires:       jfontchooser
Requires:       jpackage-utils

BuildArch:      noarch

%description
Logisim is an educational tool for designing and simulating digital logic 
circuits. With its simple toolbar interface and simulation of circuits as you 
build them, it is simple enough to facilitate learning the most basic concepts 
related to logic circuits. With the capacity to build larger circuits from 
smaller subcircuits, and to draw bundles of wires with a single mouse drag, 
Logisim can be used (and is used) to design and simulate entire CPUs for 
educational purposes.


%prep
%setup -q -c
%patch1 -p1
%patch2 -p1
%patch3 -p1

# Kill BOM
sed 's/\xef\xbb\xbf//' -i src/com/cburch/draw/shapes/CurveUtil.java

# Kill prebuilt and bundled stuff
find -name '*.class' -delete
rm -r resources/bric resources/connectina


%build
find src/ -name '*.java' |xargs javac -classpath $(build-classpath javahelp2 jfontchooser) -d .
find -name '*.class' |xargs jar cf logisim.jar resources


%install
mkdir -p %{buildroot}%{_javadir}
cp logisim.jar %{buildroot}%{_javadir}
%jpackage_script com.cburch.logisim.Main "" "" logisim:javahelp2:jfontchooser logisim true

install -d %{buildroot}%{_datadir}/pixmaps
cp -a resources/logisim/img/logisim-icon-128.png \
        %{buildroot}%{_datadir}/pixmaps/logisim.png
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}
install -d %{buildroot}%{_datadir}/mime/packages
install -pm644 %{SOURCE2} %{buildroot}%{_datadir}/mime/packages/
install -d %{buildroot}%{_datadir}/appdata
install -pm644 %{SOURCE3} %{buildroot}%{_datadir}/appdata/


%check
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/*.appdata.xml

%files
%{_javadir}/logisim.jar
%{_bindir}/logisim
%{_datadir}/applications/logisim.desktop
%{_datadir}/mime/packages/x-logisim-circuit.xml
%{_datadir}/pixmaps/logisim.png
%{_datadir}/appdata/logisim.appdata.xml
%license COPYING.TXT


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Apr 29 2016 Lubomir Rintel <lkundrak@v3.sk> - 2.7.1-4
- Add AppStream metadata

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Dec 08 2015 Lubomir Rintel <lkundrak@v3.sk> - 2.7.1-2
- Use a stock color chooser

* Fri Nov 27 2015 Lubomir Rintel <lkundrak@v3.sk> - 2.7.1-1
- Initial packaging

%global antflags -Dno_arduino_builder=true -Dsystem_avr=true -Dlight_bundle=true

%global appstream_id cc.arduino.arduinoide

%global avr_version 1.8.2
%global ethernet_version 2.0.0
%global gsm_version 1.0.6
%global stepper_version 1.1.3
%global tft_version 1.0.6
%global wifi_version 1.2.7
%global firmata_version 2.5.8
%global bridge_version 1.7.0
%global robot_control_version 1.0.4
%global robot_motor_version 1.0.3
%global robotirremote_version 2.0.0
%global spacebrewyun_version 1.0.2
%global temboo_version 1.2.1
%global esplora_version 1.0.4
%global mouse_version 1.0.1
%global keyboard_version 1.0.2
%global sd_version 1.2.4
%global servo_version 1.1.6
%global liquidcrystal_version 1.0.7
%global adafruit_version 1.10.4

%global reference_version 1.6.6-3
%global wifi_firmware_updater_version 0.10.10

Name:           arduino
Epoch:          1
Version:        1.8.13
Release:        4%{?dist}
Summary:        An IDE for Arduino-compatible electronics prototyping platforms

License:        GPLv2+ and LGPLv2+ and CC-BY-SA
URL:            https://www.arduino.cc/
Source0:        https://github.com/arduino/Arduino/archive/%{version}/%{name}-%{version}.tar.gz

Source10:       https://downloads.arduino.cc/cores/avr-%{avr_version}.tar.bz2
Source11:       https://github.com/arduino-libraries/Ethernet/archive/%{ethernet_version}/Ethernet-%{ethernet_version}.zip
Source12:       https://github.com/arduino-libraries/GSM/archive/%{gsm_version}/GSM-%{gsm_version}.zip
Source13:       https://github.com/arduino-libraries/Stepper/archive/%{stepper_version}/Stepper-%{stepper_version}.zip
Source14:       https://github.com/arduino-libraries/TFT/archive/%{tft_version}/TFT-%{tft_version}.zip
Source15:       https://github.com/arduino-libraries/WiFi/archive/%{wifi_version}/WiFi-%{wifi_version}.zip
Source16:       https://github.com/firmata/arduino/archive/%{firmata_version}/Firmata-%{firmata_version}.zip
Source17:       https://github.com/arduino-libraries/Bridge/archive/%{bridge_version}/Bridge-%{bridge_version}.zip
Source18:       https://github.com/arduino-libraries/Robot_Control/archive/%{robot_control_version}/Robot_Control-%{robot_control_version}.zip
Source19:       https://github.com/arduino-libraries/Robot_Motor/archive/%{robot_motor_version}/Robot_Motor-%{robot_motor_version}.zip
Source20:       https://github.com/arduino-libraries/RobotIRremote/archive/%{robotirremote_version}/RobotIRremote-%{robotirremote_version}.zip
Source21:       https://github.com/arduino-libraries/SpacebrewYun/archive/%{spacebrewyun_version}/SpacebrewYun-%{spacebrewyun_version}.zip
Source22:       https://github.com/arduino-libraries/Temboo/archive/%{temboo_version}/Temboo-%{temboo_version}.zip
Source23:       https://github.com/arduino-libraries/Esplora/archive/%{esplora_version}/Esplora-%{esplora_version}.zip
Source24:       https://github.com/arduino-libraries/Mouse/archive/%{mouse_version}/Mouse-%{mouse_version}.zip
Source25:       https://github.com/arduino-libraries/Keyboard/archive/%{keyboard_version}/Keyboard-%{keyboard_version}.zip
Source26:       https://github.com/arduino-libraries/SD/archive/%{sd_version}/SD-%{sd_version}.zip
Source27:       https://github.com/arduino-libraries/Servo/archive/%{servo_version}/Servo-%{servo_version}.zip
Source28:       https://github.com/arduino-libraries/LiquidCrystal/archive/%{liquidcrystal_version}/LiquidCrystal-%{liquidcrystal_version}.zip
Source29:       https://github.com/Adafruit/Adafruit_CircuitPlayground/archive/%{adafruit_version}/Adafruit_Circuit_Playground-%{adafruit_version}.zip

Source50:       https://downloads.arduino.cc/reference-%{reference_version}.zip
Source51:       https://github.com/arduino-libraries/WiFi101-FirmwareUpdater-Plugin/releases/download/v%{wifi_firmware_updater_version}/WiFi101-Updater-ArduinoIDE-Plugin-%{wifi_firmware_updater_version}.zip

Patch0:         arduino-use-system-avrdude.patch
Patch1:         arduino-use-system-astyle.patch
Patch2:         arduino-use-system-libserialport.patch
Patch3:         arduino-drop-macosx.patch
Patch4:         arduino-wrapper.patch
Patch5:         arduino-add-to-groups.patch
Patch6:         arduino-fix-path-to-builder.patch
Patch7:         arduino-fix-fresh-rsyntaxtextarea.patch

BuildRequires:  ant
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  javapackages-tools
BuildRequires:  java-devel

BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-annotations)
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-core)
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-databind)
BuildRequires:  mvn(com.fifesoft:rsyntaxtextarea)
BuildRequires:  mvn(com.github.zafarkhaja:java-semver)
BuildRequires:  mvn(com.jcraft:jsch)
BuildRequires:  mvn(commons-codec:commons-codec)
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(org.apache.commons:commons-compress)
BuildRequires:  mvn(org.apache.commons:commons-exec)
BuildRequires:  mvn(org.apache.commons:commons-lang3)
BuildRequires:  mvn(org.apache.commons:commons-logging)
BuildRequires:  mvn(org.apache.commons:commons-net)
BuildRequires:  mvn(org.apache.logging.log4j:log4j-api)
BuildRequires:  mvn(org.apache.xmlgraphics:batik-all)
BuildRequires:  mvn(org.bouncycastle:bcpg-jdk15)
BuildRequires:  mvn(org.jmdns:jmdns)
BuildRequires:  mvn(org.scream3r:jssc)

Requires:       %{name}-core = %{epoch}:%{version}-%{release}
Requires:       %{name}-devel = %{epoch}:%{version}-%{release}
Requires:       javapackages-tools
Requires:       polkit

# Require arduino-builder, which is a go project and won't exist outside these arches
ExclusiveArch:  %{go_arches}
Requires:       %{name}-builder >= 1.3.25

BuildArch:      noarch
ExcludeArch:    ppc64le s390x

%description
Arduino is an open-source electronics prototyping platform based on
flexible, easy-to-use hardware and software. It's intended for artists,
designers, hobbyists, and anyone interested in creating interactive
objects or environments.

This package contains an IDE that can be used to develop and upload code
to the micro-controller.

%package        core
Summary:        Files required for compiling code for Arduino-compatible micro-controllers

Requires:       %{name}-doc = %{epoch}:%{version}-%{release}
Requires:       %{name}-listSerialPortsC
Requires:       astyle
Requires:       avrdude
Requires:       avr-gcc
Requires:       avr-gcc-c++
Requires:       avr-libc
Requires:       java

Requires:       mvn(apache:commons-httpclient)
Requires:       mvn(com.fasterxml.jackson.core:jackson-annotations)
Requires:       mvn(com.fasterxml.jackson.core:jackson-core)
Requires:       mvn(com.fasterxml.jackson.core:jackson-databind)
Requires:       mvn(com.fifesoft:rsyntaxtextarea)
Requires:       mvn(com.github.zafarkhaja:java-semver)
Requires:       mvn(com.jcraft:jsch)
Requires:       mvn(commons-codec:commons-codec)
Requires:       mvn(commons-io:commons-io)
Requires:       mvn(org.apache.commons:commons-compress)
Requires:       mvn(org.apache.commons:commons-exec)
Requires:       mvn(org.apache.commons:commons-lang3)
Requires:       mvn(org.apache.commons:commons-logging)
Requires:       mvn(org.apache.commons:commons-net)
Requires:       mvn(org.apache.logging.log4j:log4j-api)
Requires:       mvn(org.apache.xmlgraphics:batik-all)
Requires:       mvn(org.apache.xmlgraphics:xmlgraphics-commons)
Requires:       mvn(org.bouncycastle:bcpg-jdk15)
Requires:       mvn(org.jmdns:jmdns)
Requires:       mvn(org.ow2.asm:asm-all)
Requires:       mvn(org.scream3r:jssc)
Requires:       mvn(org.slf4j:slf4j-api)
Requires:       mvn(xml-apis:xml-apis)

%description    core
Arduino is an open-source electronics prototyping platform based on
flexible, easy-to-use hardware and software. It's intended for artists,
designers, hobbyists, and anyone interested in creating interactive
objects or environments.

This package contains the core files required to compile and upload
Arduino code.

%package        doc
Summary:        Documentation for the Arduino micro-controller platform

%description    doc
Arduino is an open-source electronics prototyping platform based on
flexible, easy-to-use hardware and software. It's intended for artists,
designers, hobbyists, and anyone interested in creating interactive
objects or environments.

This package contains reference documentation.

%package        devel
Summary:        Devel package for %{name}

Requires:       %{name}-core

%description    devel
Devel package for %{name}.


%prep
%autosetup -n Arduino-%{version} -N

tar -xvf %{SOURCE10} -C hardware

# Need improve this moment...
# patch0 requires unpacked archive with hardware things
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

cp %{SOURCE10} %{SOURCE11} %{SOURCE12} %{SOURCE13} %{SOURCE14} %{SOURCE15} %{SOURCE16} %{SOURCE17} %{SOURCE18} %{SOURCE19} %{SOURCE20} %{SOURCE21} %{SOURCE22} %{SOURCE23} %{SOURCE24} %{SOURCE25} %{SOURCE26} %{SOURCE27} %{SOURCE28} %{SOURCE29} build/
cp %{SOURCE50} %{SOURCE51} build/shared/

# Remove Windows and OSX specific code
find -type d \( -name macosx -o -name windows \) -print0 | xargs -0 rm -rf

# Drop binaries
find -name '*.elf' -delete
find -name '*.class' -delete
find -name '*.jar' -delete
find -name '*.so' -delete

# Disable update check
echo -e "\n# By default, don't notify the user of a new upstream version." \
        "\n# https://bugzilla.redhat.com/show_bug.cgi?id=773519" \
        "\nupdate.check=false" >> build/shared/lib/preferences.txt

# Include requires jars to arduino-core/lib folder
build-jar-repository -p arduino-core/lib/ \
    apache-commons-codec \
    apache-commons-compress \
    apache-commons-exec \
    apache-commons-io \
    apache-commons-lang3 \
    apache-commons-logging \
    apache-commons-net \
    bcpg \
    bcprov \
    jackson-annotations \
    jackson-core \
    jackson-databind \
    jmdns \
    jsch \
    jsemver \
    jssc

# Include few libraries manually
ln -s /usr/share/java/log4j/log4j-api.jar arduino-core/lib/log4j-api.jar

# Include requires jars to app/lib folder
build-jar-repository -p app/lib/ \
    apache-commons-compress \
    apache-commons-lang3 \
    batik \
    jsch \
    jsemver \
    jssc \
    rsyntaxtextarea
    
# Include library manually
ln -s /usr/share/java/log4j/log4j-api.jar app/lib/log4j-api.jar


%build
pushd build
echo %{version} | ant build %{antflags}
mkdir -p linux/work/hardware/arduino/
mv ../hardware/*/ linux/work/hardware/arduino/
popd


%install
pushd build

# Install wrapper
install -m 0755 -Dp linux/work/%{name} %{buildroot}%{_bindir}/%{name}

# Install desktop file
cp -p linux/dist/desktop.template linux/dist/%{appstream_id}.desktop
desktop-file-install --dir=%{buildroot}%{_datadir}/applications --set-icon=%{appstream_id} --set-key=Exec --set-value=%{name} linux/dist/%{appstream_id}.desktop

# Install app data
install -m 0644 -Dp linux/dist/appdata.xml %{buildroot}%{_datadir}/metainfo/%{appstream_id}.appdata.xml

# Install mime data
install -m 0644 -Dp linux/dist/mime.xml %{buildroot}%{_datadir}/mime/packages/%{appstream_id}.xml

# Install icons
for dir in shared/icons/*; do
    if [ -d $dir ]
    then
        size=`basename $dir`
        install -m 0644 -Dp $dir/apps/%{name}.png %{buildroot}%{_datadir}/icons/hicolor/$size/apps/%{appstream_id}.png
    fi
done


# Install libs, examples, etc
mkdir -p                                    %{buildroot}%{_datadir}/%{name}
cp -ap linux/work/{examples,hardware,lib}   %{buildroot}%{_datadir}/%{name}/

rm -rf \
    %{buildroot}%{_datadir}/%{name}/lib/*.jar \
    %{buildroot}%{_datadir}/%{name}/lib/desktop.template \
    %{buildroot}%{_datadir}/%{name}/lib/version.txt \
    %{buildroot}%{_datadir}/%{name}/hardware/tools

cp -a linux/work/lib/{arduino-core.jar,pde.jar} %{buildroot}%{_datadir}/%{name}/lib/

install -m 0755 -Dp linux/dist/%{name}-add-groups %{buildroot}%{_libexecdir}/%{name}-add-groups
install -m 0644 -Dp linux/dist/cc.arduino.add-groups.policy %{buildroot}%{_datadir}/polkit-1/actions/cc.arduino.add-groups.policy

# Install configs
mkdir -p %{buildroot}%{_sysconfdir}/%{name}
ln -s %{_datadir}/%{name}/hardware/avr/boards.txt       %{buildroot}%{_sysconfdir}/%{name}/boards.txt
ln -s %{_datadir}/%{name}/hardware/avr/programmers.txt  %{buildroot}%{_sysconfdir}/%{name}/programmers.txt
ln -s %{_datadir}/%{name}/lib/preferences.txt           %{buildroot}%{_sysconfdir}/%{name}/preferences.txt

popd


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.appdata.xml

# Disabled because nothing provides org.fest.swing.*
# # Include requires jars to app/lib folder
# build-jar-repository -p app/test-lib/ \
#     jackson-databind \
#     junit
# 
# pushd build
# ant test
# popd


%files core
%license license.txt
%doc README.md
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/lib/

%files doc
%{_datadir}/%{name}/examples/

%files devel
%{_datadir}/%{name}/hardware/

%files
%{_bindir}/%{name}
%{_libexecdir}/%{name}-add-groups
%{_datadir}/applications/%{appstream_id}.desktop
%{_datadir}/metainfo/%{appstream_id}.appdata.xml
%{_datadir}/mime/packages/%{appstream_id}.xml
%{_datadir}/icons/hicolor/*/apps/%{appstream_id}.png
%{_datadir}/polkit-1/actions/cc.arduino.add-groups.policy



%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.8.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 1:1.8.13-3
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Wed Jun 17 2020 ElXreno <elxreno@gmail.com> - 1:1.8.13-2
- Rebuild

* Wed Jun 17 2020 ElXreno <elxreno@gmail.com> - 1:1.8.13-1
- Updated to version 1.8.13

* Tue May 19 2020 ElXreno <elxreno@gmail.com> - 1:1.8.12-4
- Replace java-headless by java. Fixes RHBZ#1837100

* Tue Apr 28 2020 ElXreno <elxreno@gmail.com> - 1:1.8.12-3
- Fixed running with fresh rsyntaxtextarea library

* Thu Apr 16 2020 ElXreno <elxreno@gmail.com> - 1:1.8.12-2
- Added doc subpackage to requires

* Mon Apr 13 2020 ElXreno <elxreno@gmail.com> - 1:1.8.12-1
- Updated to version 1.8.12

* Mon Apr 13 2020 ElXreno <elxreno@gmail.com> - 1:1.8.5-12
- Fixed run script. RHBZ#1823195

* Sat Apr 11 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 1:1.8.5-11
- Re-add Epoch so package isn't a downgrade

* Tue Apr 07 2020 ElXreno <elxreno@gmail.com> - 1:1.8.5-10
- Set proper java package

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.8.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.8.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.8.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 11 2018 Gianluca Sforna <giallu@gmail.com> - 1:1.8.5-6
- Fix #1518055 by requiring java = 1:1.8.0

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.8.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar  2 2018 Peter Oliver <rpm@mavit.org.uk> - 1:1.8.5-4
- Consistenty use appstream ID to ensure inclusion in, e.g., Gnome Software.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.8.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1:1.8.5-2
- Remove obsolete scriptlets

* Tue Oct 10 2017 Gianluca Sforna <giallu@gmail.com> - 1:1.8.5-1
- update to 1.8.5
- add versioned require for arduino-builder
- fix buider usage by adding an empty tools-builder directory

* Thu Aug 24 2017 Gianluca Sforna <giallu@gmail.com> - 1:1.8.4-1
- update to 1.8.4

* Wed Aug 23 2017 Gianluca Sforna <giallu@gmail.com> - 1:1.8.3-1
- update to 1.8.3, based off Tom Callaway patches

* Wed Jul 26 2017 Gianluca Sforna <giallu@gmail.com> - 1:1.6.7-2
- re-uploaded all sources

* Mon Jul 24 2017 Gianluca Sforna <giallu@gmail.com> - 1:1.6.7-1
- update to 1.6.7
- rebase patches

* Fri Jul 21 2017 Gianluca Sforna <giallu@gmail.com> - 1:1.6.6-4
- allow arduino-builder to live in /usr/bin
- do not delete needed binary firmware files

* Thu Jul 13 2017 Petr Pisar <ppisar@redhat.com> - 1:1.6.6-3
- perl dependency renamed to perl-interpreter
  <https://fedoraproject.org/wiki/Changes/perl_Package_to_Install_Core_Modules>

* Wed Jul 12 2017 Gianluca Sforna <giallu@gmail.com> - 1:1.6.6-2
- update astyle patch for 3.0 (#1444550)

* Tue Jan 24 2017 Gianluca Sforna <giallu@gmail.com> - 1:1.6.6-1
- update to 1.6.6

* Sun Oct 30 2016 Dennis Chen <barracks510@gmail.com> - 1:1.6.4-10
- Fixed Bugzilla #1380938

* Thu Sep 22 2016 Dennis Chen <barracks510@gmail.com> - 1:1.6.4-9
- Fixed broken rawhide deps

* Sat Jul 16 2016 Dennis Chen <barracks510@gmail.com> - 1:1.6.4-8
- Fixed Bugzilla #1357005

* Sun Mar 13 2016 Dennis Chen <barracks510@gmail.com> - 1:1.6.4-7
- Fixed Bugzilla #1315104

* Sun Mar 13 2016 Dennis Chen <barracks510@gmail.com> - 1:1.6.4-6
- Fixed Bugzilla #1307326 FTBFS in Rawhide.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.6.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan  7 2016 Dennis Chen <barracks510@gmail.com> - 1:1.6.4-4
- Fix Bugzilla #1296002

* Wed Dec 30 2015 Dennis Chen <barracks510@gmail.com> - 1:1.6.4-3
- Fix the Arduino startup script and redirect system astyle libraries.

* Fri Dec 25 2015 Dennis Chen <barracks510@gmail.com> - 1:1.6.4-2
- Update dependencies list to include newly packaged JSSC.

* Fri Dec 25 2015 Dennis Chen <barracks510@gmail.com> - 1:1.6.4-1
- Update to 1.6.4 and refactor most of the patches and spec file.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Apr  9 2015 Peter Oliver <rpm@mavit.org.uk> - 1:1.0.6-2
- Passing the --directory argument to `git apply` is no longer required.

* Mon Apr  6 2015 Peter Oliver <rpm@mavit.org.uk> - 1:1.0.6-1
- Update to 1.0.6.

* Tue Jul 08 2014 Rex Dieter <rdieter@fedoraproject.org> 1:1.0.5-8
- optimize mimeinfo scriptlet

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Dec 29 2013 Peter Oliver <rpm@mavit.org.uk> - 1:1.0.5-6
- Associate .ino files with the Arduino IDE.

* Thu Nov  7 2013 Peter Oliver <rpm@mavit.org.uk> - 1:1.0.5-5
- Force update of icon cache so that icon appears straight away.
- Add appdata.xml.

* Mon Aug  5 2013 Peter Oliver <rpm@mavit.org.uk> - 1:1.0.5-4
- Unversion documentation directory.

* Mon Aug  5 2013 Peter Oliver <rpm@mavit.org.uk> - 1:1.0.5-3
- Add arduino-build-platform.patch to allow building on ARM (rhbz 991988).

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu May 23 2013 Peter Oliver <rpm@mavit.org.uk> - 1:1.0.5-1
- Update to 1.0.5.
- Remove bug891556.patch.
- Remove wifishield firmware for now, until I figure out whether it's
  reasonable/permissible to include.

* Sat Feb 16 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1:1.0.1-4
- own /etc/arudino and /usr/share/arduino (bug 911931)

* Mon Feb 04 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1:1.0.1-3
- ino needs to know the arduino version (bug 905681)

* Fri Feb 01 2013 T.C. Hollingsworth <tchollingsworth@gmail.com>
- define __AVR_LIBC_DEPRECATED_ENABLE__ (bug 891556)

* Sun Jul 22 2012 Peter Oliver <rpm@mavit.org.uk> - 1:1.0.1-1
- Update to 1.0.1.
- Compress source with xz.

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri May  4 2012 Peter Oliver <rpm@mavit.org.uk> - 1:1.0-4
- Pass version number to "ant build" (fixes #815079).

* Sat Jan 14 2012 Peter Oliver <rpm@mavit.org.uk> - 1:1.0-3
- Change the default preferences so that we don't notify the user that a
  new upstream version has been released (#773519).

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jan  2 2012 Peter Oliver <rpm@mavit.org.uk> - 1:1.0-2
- Add arduino-no-avrdude64.patch to prevent copying of (for us,
  unbundled) avrdude64.

* Mon Jan  2 2012 Peter Oliver <rpm@mavit.org.uk> - 1:1.0-1
- Update to 1.0 (#753103).
- Drop arduino-use-system-avrdude.patch and arduino-boards-txt.patch,
  since they're no-longer needed.
- Move preferences.txt to /etc.

* Mon Sep 12 2011 Peter Oliver <rpm@mavit.org.uk> - 0022-5
- Treat boards.txt and programmers.txt as config files (#726135).
- Make building with "fedpkg local" work.

* Fri Jul 15 2011 Peter Oliver <rpm@mavit.org.uk> - 0022-4
- Include missing examples (#722351).

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0022-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Dec 31 2010 Peter Oliver <rpm@mavit.org.uk> - 0022-2
- Prompt the user if they are not a member of the required groups,
  rather than failing silently.

* Thu Dec 30 2010 Peter Oliver <rpm@mavit.org.uk> - 0022-1
- Update to 0022 release (#666309).
- Use the new upstream source tarball rather than git.
- Drop oro requirement and related patch, since it is no-longer used.

* Fri Dec 17 2010 Peter Oliver <rpm@mavit.org.uk> - 0021-2
- Patch boards.txt to use the "arduino" programmer type for Uno boards,
  allowing Fedora's version of avrdude to work with these boards.

* Thu Oct  7 2010 Peter Oliver <rpm@mavit.org.uk> - 0021-1
- New upstream release 0021.
- Add patch for new upstream icons.
- Override device scan in RXTX to allow use of Arduino Uno.

* Mon Sep 20 2010 Peter Oliver <rpm@mavit.org.uk> - 0019-6
- Explictly mention documentation with doc macro.
- Move reference documentation into -doc package.

* Thu Sep  9 2010 Peter Oliver <rpm@mavit.org.uk> - 0019-5
- Add missing BuildRequires.
- Use build-jar-repository to locate java libraries to build against.
- Eliminate cross-package symlinks.

* Wed Sep  8 2010 Peter Oliver <rpm@mavit.org.uk> - 0019-4
- Make sure all jars are removed from the source bundle.
- Add missing documentation.

* Tue Sep  7 2010 Peter Oliver <rpm@mavit.org.uk> - 0019-3
- Split into two packages, making the IDE optional to install.
- Build during the build phase not the install phase.
- More dependencies.

* Mon Sep  6 2010 Peter Oliver <rpm@mavit.org.uk> - 0019-2
- Expanded dependencies.

* Sun Sep  5 2010 Peter Oliver <rpm@mavit.org.uk> - 0019-1
- Initial version.  Based in part on the Debian package.

Summary:   Tools for the Hughski Colorimeter
Name:      colorhug-client
Version:   0.2.8
Release:   11%{?dist}
License:   GPLv2+
URL:       http://www.hughski.com/
Source0:   http://people.freedesktop.org/~hughsient/releases/%{name}-%{version}.tar.xz

BuildRequires: gettext
BuildRequires: glib2-devel
BuildRequires: gtk3-devel
BuildRequires: intltool
BuildRequires: libgusb-devel >= 0.1.4
BuildRequires: colord-devel >= 1.2.3
BuildRequires: colord-gtk-devel >= 0.1.24
BuildRequires: libsoup-devel
BuildRequires: libtool
BuildRequires: docbook-utils
BuildRequires: libcanberra-devel >= 0.10
BuildRequires: gobject-introspection-devel
BuildRequires: gnome-doc-utils
BuildRequires: yelp-tools
BuildRequires: itstool
BuildRequires: bash-completion

# require all the subpackages to deal with upgrades
Requires: colorhug-client-ccmx%{?_isa} = %{version}-%{release}
Requires: colorhug-client-flash%{?_isa} = %{version}-%{release}
Requires: colorhug-client-refresh%{?_isa} = %{version}-%{release}

%description
The Hughski ColorHug colorimeter is a low cost open-source hardware
sensor used to calibrate screens.

This package includes the client tools which allows the user to upgrade
the firmware on the sensor or to access the sensor from command line
scripts.

%package backlight
Summary: ColorHug Backlight Utility
Requires: colorhug-client-common%{?_isa} = %{version}-%{release}

%description backlight
Sample the ambient light level to control the backlight.

%package ccmx
Summary: ColorHug CCMX Utility
Requires: yelp
Requires: colorhug-client-common%{?_isa} = %{version}-%{release}

%description ccmx
GUI for adding and changing CCMX calibration matrices.

%package flash
Summary: ColorHug Firmare Flash Utility
Requires: yelp
Requires: colorhug-client-common%{?_isa} = %{version}-%{release}

%description flash
GUI for updating the device firmware.

%package refresh
Summary: ColorHug Display Analysis Utility
Requires: yelp
Requires: colorhug-client-common%{?_isa} = %{version}-%{release}

%description refresh
GUI for analyzing a display.

%package common
Summary: ColorHug Client Common files

%description common
Common files used in the other subpackages.

%prep
%setup -q

%build
%configure --disable-static

make %{?_smp_mflags} V=1

%install
make install DESTDIR=$RPM_BUILD_ROOT

find %{buildroot} -type f -name "*.la" -delete

%find_lang %{name}

%files
%doc COPYING

%files backlight
%doc COPYING
%{_bindir}/colorhug-backlight
%{_datadir}/appdata/com.hughski.ColorHug.Backlight.appdata.xml
%{_datadir}/applications/com.hughski.ColorHug.Backlight.desktop
%{_datadir}/icons/hicolor/*/apps/colorhug-backlight.png
%{_mandir}/man1/colorhug-backlight.1.gz

%files ccmx
%doc COPYING
%{_bindir}/colorhug-ccmx
%{_datadir}/appdata/com.hughski.ColorHug.CcmxLoader.appdata.xml
%{_datadir}/applications/com.hughski.ColorHug.CcmxLoader.desktop
%{_datadir}/icons/hicolor/*/mimetypes/application-x-ccmx.*
%{_datadir}/icons/hicolor/*/apps/colorhug-ccmx.png
%{_mandir}/man1/colorhug-ccmx.1.gz

%files flash
%doc COPYING
%{_bindir}/colorhug-flash
%{_datadir}/appdata/com.hughski.ColorHug.FlashLoader.appdata.xml
%{_datadir}/applications/com.hughski.ColorHug.FlashLoader.desktop
%{_datadir}/icons/hicolor/*/apps/colorhug-flash.png
%{_mandir}/man1/colorhug-flash.1.gz

%files refresh
%doc COPYING
%{_bindir}/colorhug-refresh
%{_datadir}/appdata/com.hughski.ColorHug.DisplayAnalysis.appdata.xml
%{_datadir}/applications/com.hughski.ColorHug.DisplayAnalysis.desktop
%{_datadir}/icons/hicolor/*/apps/colorhug-refresh.png
%{_mandir}/man1/colorhug-refresh.1.gz

%files common -f %{name}.lang
%doc README AUTHORS NEWS COPYING
%{_bindir}/colorhug-cmd
%{_datadir}/applications/colorhug-docs.desktop
%{_datadir}/colorhug-client
%{_datadir}/glib-2.0/schemas/com.hughski.colorhug-client.gschema.xml
%{_datadir}/help/*/colorhug-client
%{_datadir}/icons/hicolor/*/apps/colorhug.*
%{_datadir}/icons/hicolor/*/apps/colorimeter-colorhug-inactive.png
%dir %{_datadir}/colorhug-client
%{_libexecdir}/colorhug*
%{_mandir}/man1/colorhug-cmd.1.gz
%{_datadir}/bash-completion/completions/colorhug-cmd

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 06 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.8-6
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 19 2016 Richard Hughes <richard@hughsie.com> 0.2.8-1
- New upstream version
- Add a --device argument to colorhug-cmd
- Support the ColorHugALS in SensorHID mode for backlight changes

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Apr 19 2015 Richard Hughes <richard@hughsie.com> 0.2.7-1
- New upstream version
- Fix a typo to allow exporting results again
- Never auto-dim less than 5%

* Tue Mar 10 2015 Richard Hughes <richard@hughsie.com> 0.2.6-1
- New upstream version
- Add new ambient light sensor test application

* Thu Dec 18 2014 Richard Hughes <richard@hughsie.com> 0.2.5-1
- New upstream version
- Add a simple man page and AppData file for colorhug-refresh
- Add keywords to the various desktop files
- Do not install the bash-completion files in /etc

* Mon Dec 15 2014 Richard Hughes <richard@hughsie.com> 0.2.4-2
- Split up the utilities into indervidual subpackages for gnome-software.

* Thu Dec 04 2014 Richard Hughes <richard@hughsie.com> 0.2.4-1
- New upstream version
- Add colorhug-refresh for measuring display latency and refresh rates
- Do not use deprecated libgusb API
- Remove colorhug-inhx32-to-bin and move functionality into colorhug-cmd

* Mon Nov 10 2014 Richard Hughes <richard@hughsie.com> 0.2.3-1
- New upstream version
- Do not show CCMX matrices for different device types
- Show the Yxy and sRGB values when using take-readings-xyz

* Fri Sep 12 2014 Richard Hughes <richard@hughsie.com> 0.2.2-1
- New upstream version
- Support ColorHug2 in colorhug-ccmx and colorhug-flash
- Support getting and setting the DAC value on ColorHug+
- Do not use deprecated widgets in the spectro tool
- Remove suspicious usage of sizeof with a numeric constant

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jul 25 2014 Peter Robinson <pbrobinson@fedoraproject.org> 0.2.1-3
- Add upstream patch to fix FTBFS

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Nov 11 2013 Richard Hughes <richard@hughsie.com> 0.2.1-1
- New upstream version
- Add an AppData file for colorhug-flash and colorhug-ccmx

* Tue Jul 30 2013 Richard Hughes <rhughes@redhat.com> - 0.2.0-2
- Rebuild for colord soname bump

* Wed May 01 2013 Richard Hughes <richard@hughsie.com> 0.2.0-1
- Add a command to get the spectral data from the CCD
- Add help buttons to colorhug-flash and colorhug-ccmx
- Add some yelp documentation for the ColorHug device
- Add the ability to get and set CCD calibration values
- Do not refresh the calibration data twice when setting a custom CCMX
- Remove the internal libcolorhug and depend on the system copy
- Set a title when generating a CCMX file

* Mon Feb 04 2013 Richard Hughes <richard@hughsie.com> 0.1.14-1
- New upstream version
- Lots of translation updates
- Add a 'ccmx-upload' command to colorhug-cmd
- Allow the user to easily generate a CCMX correction matrix
- Use libcolorhug from colord

* Mon Nov 06 2012 Richard Hughes <richard@hughsie.com> 0.1.13-1
- New upstream version
- Add defines for the ColorHug Spectro
- Allow the user to flash an Intel HEX file from the command line
- Don't return flashing success when the device failed to re-appear

* Mon Aug 20 2012 Richard Hughes <richard@hughsie.com> 0.1.12-1
- New upstream version
- Add colorhug-profile to compare the measurement modes
- Add subcommands to get and set the measurement mode
- Accept full HID packets from devices with firmware >= 1.2.0
- Fix a small memory leak when commands with helpers and callbacks fail

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 02 2012 Richard Hughes <richard@hughsie.com> 0.1.11-1
- New upstream version.
- Show the calibration types when doing 'list-calibration'
- Ask the user to cover the aperture before doing a dark cal
- Do not hardcode the type as 'all' when loading a CCMX
- Recognise the INVALID_CALIBRATION error enum
- Recognise the NO_WELCOME errata enum
- Do not spin if enter is pressed at [Y/n]
- Set the post-scale to unity for the dark offsets

* Mon Jun 11 2012 Richard Hughes <richard@hughsie.com> 0.1.10-1
- New upstream version.
- Add support for TYPE_FACTORY when loading CCMX files from disk
- Also reset the calibration map when resetting the factory calibration
- Do not offer to repair twice when using 'colorhug-ccmx --repair'
- Support LED types in colorhug-cmd get/set-calibration

* Wed May 23 2012 Richard Hughes <richard@hughsie.com> 0.1.9-2
- Allow people using the legacy VID/PID to use colorhug-ccmx.

* Tue May 22 2012 Richard Hughes <richard@hughsie.com> 0.1.9-1
- Add commands to get and set the remote profile hash on the device
- Add support for the new self-test command
- Allow the colorhug tool to download and upload icc profiles
- Fix up the documentation for the command line tool options
- Install the colorhug command line tool as /usr/bin/colorhug-cmd
- Remove colorhug-gui, it's no longer useful
- Use CdIt8 for ccmx parsing and bump the colord dep to 0.1.20

* Tue Apr 17 2012 Richard Hughes <richard@hughsie.com> 0.1.8-1
- New upstream version.
- Automatically use the correct proxy server using glib-networking
- Make a sound when colorhug-flash fails or completes the update.
- Prevent a possible crash when verifying firmware.
- Prevent critical warnings when doing 'colorhug list-calibration'

* Thu Mar 15 2012 Richard Hughes <richard@hughsie.com> 0.1.7-1
- New upstream version.
- Allow the user to update to test firmware if enabled in GSettings
- Create a trivial libcolorhug library for low level access
- Correctly detect the failure to re-enumerate

* Sun Mar 04 2012 Richard Hughes <richard@hughsie.com> 0.1.6-1
- New upstream version.

* Thu Jan 26 2012 Richard Hughes <richard@hughsie.com> 0.1.5-1
- New upstream version.

* Tue Jan 10 2012 Richard Hughes <richard@hughsie.com> 0.1.4-1
- New upstream version.
- A huge number of new translations and some bugfixes.

* Mon Dec 26 2011 Richard Hughes <richard@hughsie.com> 0.1.3-1
- New upstream version.

* Fri Dec 09 2011 Richard Hughes <richard@hughsie.com> 0.1.2-1
- New upstream version.

* Wed Nov 30 2011 Richard Hughes <richard@hughsie.com> 0.1.1-1
- New upstream version.

* Sat Nov 26 2011 Richard Hughes <richard@hughsie.com> 0.1.0-2
- BR the correct version of GTK.

* Fri Nov 11 2011 Richard Hughes <richard@hughsie.com> 0.1.0-1
- Initial version for Fedora package review

%global _artwork_version 5.7

%global cinnamon_desktop_version 4.6.0
%global csd_version 4.6.0
%global cinnamon_menus_version 4.6.0
%global redhat_menus_version 1.8
%global libXrandr_version 1.2.99

Summary: Utilities to configure the Cinnamon desktop
Name:    cinnamon-control-center
Version: 4.6.2
Release: 1%{?dist}
# The following files contain code from
# ISC for panels/network/rfkill.h
# And MIT for wacom/calibrator/calibrator.c
# wacom/calibrator/calibrator.h
# wacom/calibrator/gui_gtk.c
# wacom/calibrator/gui_gtk.h
# wacom/calibrator/main.c
License: GPLv2+ and LGPLv2+ and MIT and ISC
URL:     https://github.com/linuxmint/%{name}
Source0: %url/archive/%{version}/%{name}-%{version}.tar.gz
Source1: http://packages.linuxmint.com/pool/main/m/mint-artwork-cinnamon/mint-artwork-cinnamon_%{_artwork_version}.tar.gz

Requires: cinnamon-settings-daemon >= %{csd_version}
Requires: redhat-menus >= %{redhat_menus_version}
Requires: hicolor-icon-theme
Requires: cinnamon-translations
Requires: dbus-x11
Requires: %{name}-filesystem%{?_isa} = %{version}-%{release}
# we need XRRGetScreenResourcesCurrent
Requires: libXrandr >= %{libXrandr_version}
# For the user languages
Requires: iso-codes
# For the sound panel and gnome-sound-applet
Requires: adwaita-icon-theme
# For the printers panel
Requires: cups-pk-helper
# For the network panel
Requires: nm-connection-editor
# For the info/details panel
Requires: glx-utils
# For the colour panel
Requires: gnome-color-manager

BuildRequires: pkgconfig(librsvg-2.0)
BuildRequires: pkgconfig(cinnamon-desktop) >= %{cinnamon_desktop_version}
BuildRequires: pkgconfig(libcinnamon-menu-3.0) >= %{cinnamon_menus_version}
BuildRequires: pkgconfig(cinnamon-settings-daemon) >= %{csd_version}
BuildRequires: pkgconfig(xkbfile)
BuildRequires: pkgconfig(xscrnsaver)
BuildRequires: pkgconfig(gnome-doc-utils)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(libcanberra)
BuildRequires: pkgconfig(upower-glib)
BuildRequires: pkgconfig(libnm) >= 1.2
BuildRequires: pkgconfig(libnma) >= 1.2
BuildRequires: pkgconfig(mm-glib) >= 0.7
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(polkit-agent-1)
BuildRequires: pkgconfig(libgtop-2.0)
BuildRequires: pkgconfig(ice)
BuildRequires: pkgconfig(iso-codes)
BuildRequires: pkgconfig(colord)
BuildRequires: pkgconfig(libnotify)
BuildRequires: pkgconfig(ibus-1.0)
BuildRequires: pkgconfig(libgnomekbd)
BuildRequires: pkgconfig(libxklavier)
BuildRequires: chrpath
BuildRequires: desktop-file-utils
BuildRequires: gnome-common
BuildRequires: intltool
BuildRequires: pkgconfig(krb5)
BuildRequires: pkgconfig(libwacom)

# GOA
BuildRequires: pkgconfig(goa-1.0)
BuildRequires: pkgconfig(goa-backend-1.0) >= 3.21.5


%description
This package contains configuration utilities for the Cinnamon desktop, which
allow to configure accessibility options, desktop fonts, keyboard and mouse
properties, sound setup, desktop theme and background, user interface
properties, screen resolution, and other settings.


%package filesystem
Summary: Cinnamon Control Center directories
# NOTE: this is an "inverse dep" subpackage. It gets pulled in
# NOTE: by the main package an MUST not depend on the main package

%description filesystem
The Cinnamon control-center provides a number of extension points
for applications. This package contains directories where applications
can install configuration files that are picked up by the control-center
utilities.


%package devel
Summary: Development package for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files and libraries for developing Muffin plugins. Also includes
utilities for testing Metacity/Muffin themes.


%prep
%autosetup -a 1 -p 1
NOCONFIGURE=1 ./autogen.sh


%build
%configure \
        --disable-static \
        --disable-silent-rules \
        --enable-systemd \
        --enable-onlineaccounts \
        --disable-cups

# drop unneeded direct library deps with --as-needed
# libtool doesn't make this easy, so we do it the hard way
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool

%make_build


%install
%make_install

desktop-file-install                                    \
  --delete-original                                     \
  --dir %{buildroot}/%{_datadir}/applications         \
  %{buildroot}/%{_datadir}/applications/*.desktop

# remove useless libtool archive files
find %{buildroot} -name '*.la' -exec rm -f {} \;

# remove rpath
chrpath --delete %{buildroot}/%{_libdir}/cinnamon-control-center-1/panels/*.so
chrpath --delete %{buildroot}/%{_bindir}/cinnamon-control-center

# install sound files
mkdir -p %{buildroot}/%{_datadir}/cinnamon-control-center/sounds/
install -pm 0644 mint-artwork-cinnamon-%{_artwork_version}/%{_datadir}/mint-artwork-cinnamon/sounds/* %{buildroot}/%{_datadir}/cinnamon-control-center/sounds/

%find_lang %{name}-timezones


%ldconfig_scriptlets


%files -f %{name}-timezones.lang
%doc AUTHORS README
%license COPYING
%{_datadir}/cinnamon-control-center/ui/
%{_datadir}/cinnamon-control-center/sounds/*.og*
%{_datadir}/applications/*.desktop
%{_datadir}/desktop-directories/*
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/cinnamon-control-center/datetime/
# list all binaries explicitly, so we notice if one goes missing
%{_bindir}/cinnamon-control-center
%config(noreplace) %{_sysconfdir}/xdg/menus/cinnamoncc.menu
%{_libdir}/libcinnamon-control-center.so.1*
%dir %{_libdir}/cinnamon-control-center-1/
%{_libdir}/cinnamon-control-center-1/panels/libcolor.so
%{_libdir}/cinnamon-control-center-1/panels/libdate_time.so
%{_libdir}/cinnamon-control-center-1/panels/libdisplay.so
%{_libdir}/cinnamon-control-center-1/panels/libnetwork.so
%{_libdir}/cinnamon-control-center-1/panels/libonline-accounts.so
%{_libdir}/cinnamon-control-center-1/panels/libregion.so
%{_libdir}/cinnamon-control-center-1/panels/libwacom-properties.so
%{_datadir}/polkit-1/actions/org.cinnamon.controlcenter.datetime.policy
%{_datadir}/polkit-1/rules.d/cinnamon-control-center.rules


%files filesystem
%dir %{_datadir}/cinnamon-control-center/
%dir %{_datadir}/cinnamon-control-center/sounds/


%files devel
%{_includedir}/cinnamon-control-center-1/
%{_libdir}/libcinnamon-control-center.so
%{_libdir}/pkgconfig/libcinnamon-control-center.pc


%changelog
* Tue Aug 11 2020 Leigh Scott <leigh123linux@gmail.com> - 4.6.2-1
- Update to 4.6.2 release

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 21 2020 Leigh Scott <leigh123linux@gmail.com> - 4.6.1-1
- Update to 4.6.1 release

* Tue May 12 2020 Leigh Scott <leigh123linux@gmail.com> - 4.6.0-1
- Update to 4.6.0 release

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Nov 16 2019 Leigh Scott <leigh123linux@googlemail.com> - 4.4.0-1
- Update to 4.4.0 release

* Wed Jul 31 2019 Leigh Scott <leigh123linux@googlemail.com> - 4.2.2-1
- Update to 4.2.2 release

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jul 14 2019 Leigh Scott <leigh123linux@googlemail.com> - 4.2.1-1
- Update to 4.2.1 release

* Fri Jun 14 2019 Leigh Scott <leigh123linux@googlemail.com> - 4.2.0-1
- Update to 4.2.0 release

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec 06 2018 Leigh Scott <leigh123linux@googlemail.com> - 4.0.1-1
- Update to 4.0.1 release

* Tue Oct 30 2018 Leigh Scott <leigh123linux@googlemail.com> - 4.0.0-1
- Update to 4.0.0 release

* Sun Oct 07 2018 Leigh Scott <leigh123linux@googlemail.com> - 3.8.2-2
- Drop EPEL/RHEL support

* Fri Sep 21 2018 Leigh Scott <leigh123linux@googlemail.com> - 3.8.2-1
- Update to 3.8.2 release

* Thu Aug 16 2018 Leigh Scott <leigh123linux@googlemail.com> - 3.8.1-1
- Update to 3.8.1 release

* Mon Jul 16 2018 Leigh Scott <leigh123linux@googlemail.com> - 3.8.0-5
- Revert last commit

* Sat Jul 14 2018 Leigh Scott <leigh123linux@googlemail.com> - 3.8.0-4
- Exclude armv7hl, ppc64  and ppc64le due to FTBFS

* Fri Jul 13 2018 Leigh Scott <leigh123linux@googlemail.com> - 3.8.0-3
- Remove unused buildrequires and requires

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Apr 17 2018 Leigh Scott <leigh123linux@googlemail.com> - 3.8.0-1
- Update to 3.8.0 release

* Thu Mar 15 2018 Leigh Scott <leigh123linux@googlemail.com> - 3.6.6-0.1.20180314gitd63b51c
- Update to git snapshot

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.6.5-3
- Remove obsolete scriptlets

* Tue Nov 21 2017 Björn Esser <besser82@fedoraproject.org> - 3.6.5-2
- Updated patch for network panel

* Mon Nov 20 2017 Björn Esser <besser82@fedoraproject.org> - 3.6.5-1
- update to 3.6.5 release

* Mon Nov 20 2017 Björn Esser <besser82@fedoraproject.org> - 3.6.4-2
- update to 3.6.4 release

* Mon Nov 20 2017 Björn Esser <besser82@fedoraproject.org> - 3.6.3-8
- Add patch fixing a Gtk warning in online-accounts

* Mon Nov 20 2017 Björn Esser <besser82@fedoraproject.org> - 3.6.3-7
- Add patch fixing i18n
- Split other patches

* Mon Nov 20 2017 Björn Esser <besser82@fedoraproject.org> - 3.6.3-6
- Another updated patch for network panel

* Sun Nov 19 2017 Björn Esser <besser82@fedoraproject.org> - 3.6.3-5
- Updated patch for rebased network panel again

* Sun Nov 19 2017 Björn Esser <besser82@fedoraproject.org> - 3.6.3-4
- Updated patch for rebased network panel

* Sun Nov 19 2017 Björn Esser <besser82@fedoraproject.org> - 3.6.3-3
- Add patch to fix loading the OpenVPN plugin

* Sun Nov 19 2017 Björn Esser <besser82@fedoraproject.org> - 3.6.3-2
- Add patch with some bugfixes to network panel

* Fri Nov 17 2017 Björn Esser <besser82@fedoraproject.org> - 3.6.3-1
- update to 3.6.3 release and update mint-artwork-cinnamon

* Wed Nov 15 2017 Björn Esser <besser82@fedoraproject.org> - 3.6.2-3
- Add Patch from upstream to remove the extra vertical scrollbar

* Mon Nov 13 2017 Leigh Scott <leigh123linux@googlemail.com> - 3.6.2-2
- Add build requires libICE-devel

* Mon Nov 13 2017 Leigh Scott <leigh123linux@googlemail.com> - 3.6.2-1
- update to 3.6.2 release

* Mon Oct 23 2017 Leigh Scott <leigh123linux@googlemail.com> - 3.6.0-1
- update to 3.6.0 release

* Thu Sep 07 2017 Björn Esser <besser82@fedoraproject.org> - 3.4.0-8
- Add support for online-accounts

* Mon Jul 31 2017 Florian Weimer <fweimer@redhat.com> - 3.4.0-7
- Rebuild with binutils fix for ppc64le (#1475636)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 24 2017 Björn Esser <besser82@fedoraproject.org> - 3.4.0-5
- Update patch for libnm-1.2, fixes crash when trying to connect to
  a hidden wifi network (rhbz#1474448)

* Fri Jul 07 2017 Leigh Scott <leigh123linux@googlemail.com> - 3.4.0-4
- Update mint-artwork-cinnamon

* Wed May 10 2017 Björn Esser <besser82@fedoraproject.org> - 3.4.0-3
- Update patch for libnm-1.2, fixes crash in vpn-dialogs

* Tue May 09 2017 Björn Esser <besser82@fedoraproject.org> - 3.4.0-2
- Add patch to port to libnm-1.2 (rhbz#1413610)

* Thu May 04 2017 Leigh Scott <leigh123linux@googlemail.com> - 3.4.0-1
- update to 3.4.0 release

* Fri Apr 21 2017 Dan Horák <dan[at]danny.cz> - 3.4.0-0.2.20170420gitf992a30
- update BR

* Thu Apr 20 2017 Leigh Scott <leigh123linux@googlemail.com> - 3.4.0-0.1.20170420gitf992a30
- update to git snapshot

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 12 2016 leigh scott <leigh123linux@googlemail.com> - 3.2.1-1
- update to 3.2.1 release

* Mon Nov 07 2016 Leigh Scott <leigh123linux@googlemail.com> - 3.2.0-1
- update to 3.2.0 release

* Fri Jun 24 2016 Leigh Scott <leigh123linux@googlemail.com> - 3.0.1-1
- update to 3.0.1 release

* Sat Apr 23 2016 Leigh Scott <leigh123linux@googlemail.com> - 3.0.0-1
- update to 3.0.0 release

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov 09 2015 Leigh Scott <leigh123linux@googlemail.com> - 2.8.0-2
- rebuilt

* Sat Oct 17 2015 Leigh Scott <leigh123linux@googlemail.com> - 2.8.0-1
- update to 2.8.0 release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu May 28 2015 Leigh Scott <leigh123linux@googlemail.com> - 2.6.0-3
- fix schema path

* Wed May 20 2015 Leigh Scott <leigh123linux@googlemail.com> - 2.6.0-2
- re-add dist tag

* Wed May 20 2015 Leigh Scott <leigh123linux@googlemail.com> - 2.6.0-1
- update to 2.6.0 release

* Tue May 05 2015 Leigh Scott <leigh123linux@googlemail.com> - 2.5.0-0.1.git0febe4d
- update to git snapshot

* Sun Mar 01 2015 Leigh Scott <leigh123linux@googlemail.com> - 2.4.2-2
- remove the NetworkManager version checking altogether

* Tue Dec 02 2014 Leigh Scott <leigh123linux@googlemail.com> - 2.4.2-1
- update to 2.4.2
- hide virtual profiles in colour plugin

* Wed Nov 26 2014 Leigh Scott <leigh123linux@googlemail.com> - 2.4.1-2
- fix mobile broadband setup menu

* Wed Nov 12 2014 Leigh Scott <leigh123linux@googlemail.com> - 2.4.1-1
- update to 2.4.1

* Fri Oct 31 2014 Leigh Scott <leigh123linux@googlemail.com> - 2.4.0-1
- update to 2.4.0

* Tue Sep 30 2014 Leigh Scott <leigh123linux@googlemail.com> - 2.4.0-0.1.git9677670
- update to latest git

* Mon Sep 22 2014 Leigh Scott <leigh123linux@googlemail.com> - 2.2.10-4
- fix upower-0.99 power panel issue

* Mon Aug 18 2014 Kalev Lember <kalevlember@gmail.com> - 2.2.10-3
- Rebuilt for upower 0.99.1 soname bump

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.10-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jul 17 2014 Rex Dieter <rdieter@fedoraproject.org> 2.2.10-1.1
- rebuild (for pulseaudio, bug #1117683)

* Fri Jun 27 2014 Leigh Scott <leigh123linux@googlemail.com> - 2.2.10-1
- update to 2.2.10
- add requires gnome-color-manager (don't rely on gnome-packagekit to do it)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Leigh Scott <leigh123linux@googlemail.com> - 2.2.9-1
- update to 2.2.9

* Tue May 20 2014 Leigh Scott <leigh123linux@googlemail.com> - 2.2.8-1
- update to 2.2.8

* Sun May 11 2014 Leigh Scott <leigh123linux@googlemail.com> - 2.2.7-1
- update to 2.2.7

* Fri May  9 2014 Peter Robinson <pbrobinson@fedoraproject.org> 2.2.4-2
- Should be using clutter-gst2 in Fedora too, not just RHEL-7

* Fri May 02 2014 Leigh Scott <leigh123linux@googlemail.com> - 2.2.4-1
- update to 2.2.4

* Mon Apr 14 2014 Leigh Scott <leigh123linux@googlemail.com> - 2.2.3-1
- update to 2.2.3

* Sat Apr 12 2014 Leigh Scott <leigh123linux@googlemail.com> - 2.2.1-1
- update to 2.2.1

* Fri Jan 17 2014 Leigh Scott <leigh123linux@googlemail.com> - 2.0.9-4
- add log out dialogue for language change in region panel

* Mon Jan 13 2014 Leigh Scott <leigh123linux@googlemail.com> - 2.0.9-3
- make changes for epel7

* Tue Jan 07 2014 Leigh Scott <leigh123linux@googlemail.com> - 2.0.9-2
- cleanup region panel

* Sat Nov 23 2013 Leigh Scott <leigh123linux@googlemail.com> - 2.0.9-1
- update to 2.0.9
- add some sound files for actions

* Sat Nov 16 2013 Leigh Scott <leigh123linux@googlemail.com> - 2.0.7-2
- patch for upower 1.0 changes (not complete)

* Fri Nov 08 2013 Leigh Scott <leigh123linux@googlemail.com> - 2.0.7-1
- update to 2.0.7

* Fri Oct 25 2013 Leigh Scott <leigh123linux@googlemail.com> - 2.0.5-1
- update to 2.0.5

* Thu Oct 24 2013 Leigh Scott <leigh123linux@googlemail.com> - 2.0.4-1
- update to 2.0.4

* Fri Oct 18 2013 Leigh Scott <leigh123linux@googlemail.com> - 2.0.3-1
- update to 2.0.3

* Wed Oct 09 2013 Leigh Scott <leigh123linux@googlemail.com> - 2.0.2-1
- update to 2.0.2
- drop undefined nm symbol patch

* Mon Oct 07 2013 Leigh Scott <leigh123linux@googlemail.com> - 2.0.1-3
- fix undefined nm symbol (br 1011649)

* Thu Oct 03 2013 Leigh Scott <leigh123linux@googlemail.com> - 2.0.1-2
- remove unused build requires

* Wed Oct 02 2013 Leigh Scott <leigh123linux@googlemail.com> - 2.0.1-1
- update to 2.0.1

* Mon Sep 30 2013 Leigh Scott <leigh123linux@googlemail.com> - 1.9.1-1
- update to 1.9.1

* Sat Sep 28 2013 Rex Dieter <rdieter@fedoraproject.org> 1.9.0-0.15.git31ce8a8
- add systemd-login1 support

* Fri Sep 20 2013 Leigh Scott <leigh123linux@googlemail.com> - 1.9.0-0.14.git31ce8a8
- Try add fix region input source selection

* Wed Sep 18 2013 Leigh Scott <leigh123linux@googlemail.com> - 1.9.0-0.13.git31ce8a8
- update to latest git

* Thu Aug 29 2013 Leigh Scott <leigh123linux@googlemail.com> - 1.9.0-0.12.git39bd295
- Remove bluetooth support (Screw bluez5!)

* Sun Aug 25 2013 Leigh Scott <leigh123linux@googlemail.com> - 1.9.0-0.11.git39bd295
- update to latest git
- Change buildrequires to cinnamon-desktop-devel
- Change requires to cinnamon-desktop

* Sat Aug 24 2013 Leigh Scott <leigh123linux@googlemail.com> - 1.9.0-0.10.git16717a7
- update to latest git
- adjust for new cinnamon-translations package
- add requires cinnamon-translations

* Thu Aug 22 2013 Leigh Scott <leigh123linux@googlemail.com> - 1.9.0-0.9.git7d365d0
- rebuilt

* Mon Aug 05 2013 leigh <leigh123linux@googlemail.com> - 1.9.0-0.8.git7d365d0
- rebuilt

* Wed Jul 31 2013 leigh <leigh123linux@googlemail.com> - 1.9.0-0.7.git7d365d0
- rebuilt

* Sun Jul 28 2013 Leigh Scott <leigh123linux@googlemail.com> - 1.9.0-0.6.git7d365d0
- fix missing bluetooth menu icon

* Sun Jul 28 2013 Leigh Scott <leigh123linux@googlemail.com> - 1.9.0-0.5.git7d365d0
- enable bluetooth support

* Sat Jul 27 2013 Leigh Scott <leigh123linux@googlemail.com> - 1.9.0-0.4.git7d365d0
- update to latest git
- fix icon name in color desktop file

* Wed Jul 24 2013 Leigh Scott <leigh123linux@googlemail.com> - 1.9.0-0.3.git430927a
- add missing licences to tag
- remove requires alsa-lib

* Mon Jul 22 2013 Leigh Scott <leigh123linux@googlemail.com> - 1.9.0-0.2.git430927a
- make review changes

* Thu Jul 18 2013 Leigh Scott <leigh123linux@googlemail.com> - 1.9.0-0.1.git430927a
- Inital build

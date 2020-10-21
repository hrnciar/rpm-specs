%global cinnamon_desktop_version 4.6.0

Name:           cinnamon-settings-daemon
Version:        4.6.4
Release:        2%{?dist}
Summary:        The daemon sharing settings from CINNAMON to GTK+/KDE applications

License:        GPLv2+ and LGPLv2+
URL:            https://github.com/linuxmint/%{name}
Source0:        %url/archive/%{version}/%{name}-%{version}.tar.gz

# add hard cinnamon-desktop required version due logind schema
Requires:       cinnamon-desktop%{?_isa} >= %{cinnamon_desktop_version}
Requires:       iio-sensor-proxy%{?_isa}

BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(cinnamon-desktop) >= %{cinnamon_desktop_version}
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libgnomekbd)
BuildRequires:  pkgconfig(libnm)
BuildRequires:  pkgconfig(libnma)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(polkit-agent-1)
BuildRequires:  pkgconfig(libxklavier)
BuildRequires:  pkgconfig(upower-glib)
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(nss)
BuildRequires:  pkgconfig(colord) >= 0.1.12
BuildRequires:  pkgconfig(lcms2) >= 2.2
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(ibus-1.0)
BuildRequires:  cups-devel
BuildRequires:  desktop-file-utils
BuildRequires:  docbook-style-xsl
BuildRequires:  gnome-common
BuildRequires:  intltool
BuildRequires:  libxslt
BuildRequires:  pkgconfig(librsvg-2.0)
%ifnarch s390 s390x %{?rhel:ppc ppc64}
BuildRequires:  pkgconfig(xorg-wacom)
BuildRequires:  pkgconfig(libwacom)
%endif

%description
A daemon to share settings from CINNAMON to other applications. It also
handles global keybindings, and many of desktop-wide settings.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

Requires:       dbus-glib-devel

%description    devel
This package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1
NOCONFIGURE=1 ./autogen.sh

%build
%configure --disable-static \
           --enable-profiling \
           --disable-smartcard-support

%make_build V=1


%install
%make_install
find %buildroot -name '*.la' -exec rm -f {} ';'

desktop-file-install --delete-original           \
  --dir %buildroot%{_sysconfdir}/xdg/autostart/  \
  %buildroot%{_sysconfdir}/xdg/autostart/*

desktop-file-install --delete-original           \
  --dir %buildroot%{_datadir}/applications/  \
  %buildroot%{_datadir}/applications/csd-automount.desktop
  
# Fix non-executable script
chmod a+x %buildroot%{_datadir}/cinnamon-settings-daemon-3.0/input-device-example.sh


%files
%doc AUTHORS
%license COPYING COPYING.LIB
%config %{_sysconfdir}/xdg/autostart/*
%{_libdir}/cinnamon-settings-daemon-3.0/
%{_libexecdir}/csd-a11y-keyboard
%{_libexecdir}/csd-a11y-settings
%{_libexecdir}/csd-automount
%{_libexecdir}/csd-background
%{_libexecdir}/csd-backlight-helper
%{_libexecdir}/csd-clipboard
%{_libexecdir}/csd-color
%{_libexecdir}/csd-cursor
%{_libexecdir}/csd-datetime-mechanism
%{_libexecdir}/csd-dummy
%{_libexecdir}/csd-housekeeping
%{_libexecdir}/csd-input-helper
%{_libexecdir}/csd-keyboard
%{_libexecdir}/csd-locate-pointer
%{_libexecdir}/csd-media-keys
%{_libexecdir}/csd-mouse
%{_libexecdir}/csd-orientation
%{_libexecdir}/csd-power
%{_libexecdir}/csd-printer
%{_libexecdir}/csd-print-notifications
%{_libexecdir}/csd-screensaver-proxy
#{_libexecdir}/csd-smartcard
%{_libexecdir}/csd-sound
%{_libexecdir}/csd-xrandr
%{_libexecdir}/csd-xsettings
%ifnarch s390 s390x %{?rhel:ppc ppc64}
%{_libexecdir}/csd-list-wacom
%{_libexecdir}/csd-wacom
%{_libexecdir}/csd-wacom-led-helper
%{_libexecdir}/csd-wacom-osd
%endif
%{_datadir}/applications/csd-automount.desktop
%{_datadir}/cinnamon-settings-daemon/
%{_datadir}/dbus-1/system.d/org.cinnamon.SettingsDaemon.DateTimeMechanism.conf
%{_datadir}/dbus-1/system-services/org.cinnamon.SettingsDaemon.DateTimeMechanism.service
%{_datadir}/glib-2.0/schemas/org.cinnamon.settings-daemon*.xml
%{_datadir}/icons/hicolor/*/apps/csd-*
%{_datadir}/polkit-1/actions/org.cinnamon.settings*.policy

%files devel
%{_includedir}/cinnamon-settings-daemon-3.0/
%{_libdir}/pkgconfig/cinnamon-settings-daemon.pc
%{_datadir}/cinnamon-settings-daemon-3.0/


%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 21 2020 Leigh Scott <leigh123linux@gmail.com> - 4.6.4-1
- Update to 4.6.4 release

* Wed Jun 17 2020 Leigh Scott <leigh123linux@gmail.com> - 4.6.3-1
- Update to 4.6.3 release

* Thu Jun 11 2020 Leigh Scott <leigh123linux@gmail.com> - 4.6.2-1
- Update to 4.6.2 release

* Wed May 27 2020 Leigh Scott <leigh123linux@gmail.com> - 4.6.1-1
- Update to 4.6.1 release

* Tue May 12 2020 Leigh Scott <leigh123linux@gmail.com> - 4.6.0-1
- Update to 4.6.0 release

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 18 2019 Leigh Scott <leigh123linux@googlemail.com> - 4.4.0-2
- Restore old check for logind

* Sat Nov 16 2019 Leigh Scott <leigh123linux@googlemail.com> - 4.4.0-1
- Update to 4.4.0 release

* Wed Jul 31 2019 Leigh Scott <leigh123linux@googlemail.com> - 4.2.2-1
- Update to 4.2.2 release

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jul 14 2019 Leigh Scott <leigh123linux@googlemail.com> - 4.2.1-1
- Update to 4.2.1 release

* Sun Jun 23 2019 Leigh Scott <leigh123linux@googlemail.com> - 4.2.0-1
- Update to 4.2.0 release

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec 06 2018 Leigh Scott <leigh123linux@googlemail.com> - 4.0.3-1
- Update to 4.0.3 release

* Tue Nov 20 2018 Leigh Scott <leigh123linux@googlemail.com> - 4.0.2-1
- Update to 4.0.2 release

* Mon Nov 12 2018 Leigh Scott <leigh123linux@googlemail.com> - 4.0.1-1
- Update to 4.0.1 release

* Tue Oct 30 2018 Leigh Scott <leigh123linux@googlemail.com> - 4.0.0-1
- Update to 4.0.0 release

* Sun Oct 07 2018 Leigh Scott <leigh123linux@googlemail.com> - 3.8.6-2
- Drop EPEL/RHEL support

* Fri Sep 21 2018 Leigh Scott <leigh123linux@googlemail.com> - 3.8.6-1
- Update to 3.8.6 release

* Thu Aug 16 2018 Leigh Scott <leigh123linux@googlemail.com> - 3.8.4-1
- Update to 3.8.4 release

* Mon Jul 16 2018 Leigh Scott <leigh123linux@googlemail.com> - 3.8.3-3
- Remove requires cinnamon-control-center-filesystem

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 08 2018 Leigh Scott <leigh123linux@googlemail.com> - 3.8.3-1
- Update to 3.8.3 release

* Sun Jun 03 2018 Leigh Scott <leigh123linux@googlemail.com> - 3.8.2-1
- Update to 3.8.2 release

* Sun May 06 2018 Leigh Scott <leigh123linux@googlemail.com> - 3.8.1-1
- Update to 3.8.1 release

* Tue Apr 17 2018 Leigh Scott <leigh123linux@googlemail.com> - 3.8.0-1
- Update to 3.8.0 release

* Thu Feb 15 2018 Leigh Scott <leigh123linux@googlemail.com> - 3.6.3-0.1.20180214git63f501e
- update to git snapshot

* Thu Feb 15 2018 Leigh Scott <leigh123linux@googlemail.com> - 3.6.2-1
- update to 3.6.2 release

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 3.6.1-3
- Rebuilt for switch to libxcrypt

* Sun Jan 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.6.1-2
- Remove obsolete scriptlets

* Thu Nov 16 2017 Leigh Scott <leigh123linux@googlemail.com> - 3.6.1-1
- update to 3.6.1 release
- disable smartcard support till we can fix it

* Mon Oct 23 2017 Leigh Scott <leigh123linux@googlemail.com> - 3.6.0-1
- update to 3.6.0 release

* Thu Aug 31 2017 Björn Esser <besser82@fedoraproject.org> - 3.4.4-3
- Drop patch for csd-sharing

* Wed Aug 30 2017 Björn Esser <besser82@fedoraproject.org> - 3.4.4-2
- Adjustments for EPEL7

* Thu Aug 10 2017 Leigh Scott <leigh123linux@googlemail.com> - 3.4.4-1
- update to 3.4.4 release

* Thu Aug 10 2017 Leigh Scott <leigh123linux@googlemail.com> - 3.4.3-2
- revert bad xrandr commit

* Wed Aug 09 2017 Leigh Scott <leigh123linux@googlemail.com> - 3.4.3-1
- update to 3.4.3 release

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 21 2017 Leigh Scott <leigh123linux@googlemail.com> - 3.4.2-1
- update to 3.4.2 release

* Wed Jun 14 2017 Leigh Scott <leigh123linux@googlemail.com> - 3.4.1-2
- fix sharing patch again (rhbz #1461426)

* Tue May 23 2017 Leigh Scott <leigh123linux@googlemail.com> - 3.4.1-1
- update to 3.4.1 release

* Fri May 19 2017 Leigh Scott <leigh123linux@googlemail.com> - 3.4.0-5
- Remove invalid symlink

* Sat May 13 2017 Leigh Scott <leigh123linux@googlemail.com> - 3.4.0-4
- Add patch to fix dbus names

* Wed May 10 2017 Leigh Scott <leigh123linux@googlemail.com> - 3.4.0-3
- Update sharing patch (adds libnm support)

* Wed May 10 2017 Björn Esser <besser82@fedoraproject.org> - 3.4.0-2
- Rebuilt to replace nm-glib with libnm (rhbz#1413610)

* Wed May 03 2017 Leigh Scott <leigh123linux@googlemail.com> - 3.4.0-1
- update to 3.4.0 release

* Tue May 02 2017 Leigh Scott <leigh123linux@googlemail.com> - 3.4.0-0.7.20170423git358e90c
- Fix startup delay caused by sharing plugin

* Sun Apr 23 2017 Leigh Scott <leigh123linux@googlemail.com> - 3.4.0-0.6.20170423git358e90c
- update to git snapshot

* Fri Apr 21 2017 Leigh Scott <leigh123linux@googlemail.com> - 3.4.0-0.5.20170420gitf328d98
- revert 'update BR for s390 wacom'

* Fri Apr 21 2017 Leigh Scott <leigh123linux@googlemail.com> - 3.4.0-0.4.20170420gitf328d98
- update to git snapshot
- update BR for s390 wacom

* Thu Apr 20 2017 Leigh Scott <leigh123linux@googlemail.com> - 3.4.0-0.3.20170420git3819441
- update to git snapshot

* Thu Apr 20 2017 Leigh Scott <leigh123linux@googlemail.com> - 3.4.0-0.2.20170420gitc0cb143
- update to git snapshot
- remove gstreamer build requires
- spec file clean up

* Wed Apr 19 2017 Leigh Scott <leigh123linux@googlemail.com> - 3.4.0-0.1.20170419git494e448
- update to git snapshot

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Dec 10 2016 leigh scott <leigh123linux@googlemail.com> - 3.2.1-1
- update to 3.2.1 release

* Mon Nov 07 2016 Leigh Scott <leigh123linux@googlemail.com> - 3.2.0-1
- update to 3.2.0 release

* Wed Aug 24 2016 Leigh Scott <leigh123linux@googlemail.com> - 3.0.1-2
- add sharing plugin port

* Mon May 16 2016 Leigh Scott <leigh123linux@googlemail.com> - 3.0.1-1
- update to 3.0.1 release

* Sun May 01 2016 Leigh Scott <leigh123linux@googlemail.com> - 3.0.0-3
- remove account service background as it's ubuntu only

* Sun Apr 24 2016 Leigh Scott <leigh123linux@googlemail.com> - 3.0.0-2
- fix cinnamon-settings-daemon 'command not found'

* Sat Apr 23 2016 Leigh Scott <leigh123linux@googlemail.com> - 3.0.0-1
- update to 3.0.0 release

* Wed Mar 09 2016 Leigh Scott <leigh123linux@googlemail.com> - 2.8.4-1
- update to 2.8.4 release

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov 09 2015 Leigh Scott <leigh123linux@googlemail.com> - 2.8.1-2
- rebuilt

* Mon Nov 09 2015 Leigh Scott <leigh123linux@googlemail.com> - 2.8.1-1
- update to 2.8.1 release

* Fri Oct 16 2015 Leigh Scott <leigh123linux@googlemail.com> - 2.8.0-1
- update to 2.8.0 release

* Wed Sep 09 2015 Leigh Scott <leigh123linux@googlemail.com> - 2.6.3-5
- Stop using deprecated GSettings schema property

* Fri Aug 28 2015 Leigh Scott <leigh123linux@googlemail.com> - 2.6.3-4
- fix more glib2 regressions

* Fri Aug 28 2015 Leigh Scott <leigh123linux@googlemail.com> - 2.6.3-3
- add patch to fix glib2 regression

* Sun Jun 28 2015 Leigh Scott <leigh123linux@googlemail.com> - 2.6.3-2
- update to 2.6.3 release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 25 2015 Leigh Scott <leigh123linux@googlemail.com> - 2.6.1-1
- update to 2.6.1 release

* Sun May 24 2015 Leigh Scott <leigh123linux@googlemail.com> - 2.6.0-2
- add patch to fix keyboard shortcuts for power actions (bz 1224523)

* Wed May 20 2015 Leigh Scott <leigh123linux@googlemail.com> - 2.6.0-1
- update to 2.6.0 release

* Wed May 06 2015 Leigh Scott <leigh123linux@googlemail.com> - 2.5.0-0.2.gitd228d00
- update to git snapshot

* Tue May 05 2015 Leigh Scott <leigh123linux@googlemail.com> - 2.5.0-0.1.git8430be2
- update to git snapshot

* Sun Mar 01 2015 Leigh Scott <leigh123linux@googlemail.com> - 2.4.3-3
- patch to fix xrandr log spam

* Sun Feb 22 2015 Leigh Scott <leigh123linux@googlemail.com> - 2.4.3-2
- cherry pick upstream (includes bz 1182457)

* Wed Nov 12 2014 Leigh Scott <leigh123linux@googlemail.com> - 2.4.3-1
- update to 2.4.3

* Sat Nov 08 2014 Leigh Scott <leigh123linux@googlemail.com> - 2.4.2-1
- update to 2.4.2

* Fri Oct 31 2014 Leigh Scott <leigh123linux@googlemail.com> - 2.4.1-1
- update to 2.4.1

* Fri Oct 31 2014 Leigh Scott <leigh123linux@googlemail.com> - 2.4.0-1
- update to 2.4.0

* Fri Oct 10 2014 Leigh Scott <leigh123linux@googlemail.com> - 2.4.0-0.2.git5a6ee03
- update to latest git

* Tue Sep 30 2014 Leigh Scott <leigh123linux@googlemail.com> - 2.4.0-0.1.gitec2ca3a
- update to latest git

* Mon Aug 18 2014 Kalev Lember <kalevlember@gmail.com> - 2.2.4-5
- Rebuilt for upower 0.99.1 soname bump

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Aug 01 2014 Leigh Scott <leigh123linux@googlemail.com> - 2.2.4-3
- more upower-0.99 fixes

* Mon Jul 14 2014 Leigh Scott <leigh123linux@googlemail.com> - 2.2.4-2
- Fix lid action with external monitor (upower-0.99)

* Fri Jun 27 2014 Leigh Scott <leigh123linux@googlemail.com> - 2.2.4-1
- update to 2.2.4
- Touchpad support: Added support for two and three finger clicks

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 30 2014 Leigh Scott <leigh123linux@googlemail.com> - 2.2.3-2
- add fedora support to datetime

* Tue May 20 2014 Leigh Scott <leigh123linux@googlemail.com> - 2.2.3-1
- update to 2.2.3

* Mon May 05 2014 Leigh Scott <leigh123linux@googlemail.com> - 2.2.2-2
- add patch to add support for upower critical action

* Fri May 02 2014 Leigh Scott <leigh123linux@googlemail.com> - 2.2.2-1
- update to 2.2.2

* Fri Apr 18 2014 Leigh Scott <leigh123linux@googlemail.com> - 2.2.1-3
- fix lid suspend action

* Fri Apr 18 2014 Leigh Scott <leigh123linux@googlemail.com> - 2.2.1-2
- add mpris pause fix

* Mon Apr 14 2014 Leigh Scott <leigh123linux@googlemail.com> - 2.2.1-1
- update to 2.2.1

* Sat Apr 12 2014 Leigh Scott <leigh123linux@googlemail.com> - 2.2.0-1
- update to 2.2.0

* Thu Mar 06 2014 Leigh Scott <leigh123linux@googlemail.com> - 2.0.8-5
- Fix DPMS issue with Xorg 1.14

* Sat Feb 15 2014 Leigh Scott <leigh123linux@googlemail.com> - 2.0.8-4
- more logind changes

* Mon Jan 13 2014 Leigh Scott <leigh123linux@googlemail.com> - 2.0.8-3
- rebuilt

* Mon Jan 13 2014 Leigh Scott <leigh123linux@googlemail.com> - 2.0.8-2
- rebuilt

* Mon Dec 02 2013 Leigh Scott <leigh123linux@googlemail.com> - 2.0.8-1
- update to 2.0.8

* Sun Nov 10 2013 Leigh Scott <leigh123linux@googlemail.com> - 2.0.7-1
- update to 2.0.7

* Sat Nov 09 2013 Leigh Scott <leigh123linux@googlemail.com> - 2.0.6-5
- remove obsolete battery recall code

* Thu Nov 07 2013 Rex Dieter <rdieter@fedoraproject.org> - 2.0.6-4
- upower breakage (#1026036)

* Mon Nov 04 2013 Leigh Scott <leigh123linux@googlemail.com> - 2.0.6-3
- add conditional as f19 glib is too old

* Mon Nov 04 2013 Leigh Scott <leigh123linux@googlemail.com> - 2.0.6-2
- patch to add mpris support to media-keys

* Sun Nov 03 2013 Leigh Scott <leigh123linux@googlemail.com> - 2.0.6-1
- update to 2.0.6

* Fri Oct 25 2013 Leigh Scott <leigh123linux@googlemail.com> - 2.0.5-1
- update to 2.0.5

* Thu Oct 24 2013 Leigh Scott <leigh123linux@googlemail.com> - 2.0.4-2
- revert background changes made for vbox

* Thu Oct 24 2013 Leigh Scott <leigh123linux@googlemail.com> - 2.0.4-1
- update to 2.0.4

* Fri Oct 18 2013 Leigh Scott <leigh123linux@googlemail.com> - 2.0.3-1
- update to 2.0.3

* Fri Oct 18 2013 Leigh Scott <leigh123linux@googlemail.com> - 2.0.2-1
- update to 2.0.2
- sort out files section

* Thu Oct 17 2013 Leigh Scott <leigh123linux@googlemail.com> - 2.0.1-2
- Stop cinnamon-fallback-mount-helper starting in gnome-shell

* Wed Oct 02 2013 Leigh Scott <leigh123linux@googlemail.com> - 2.0.1-1
- update to 2.0.1

* Mon Sep 30 2013 Leigh Scott <leigh123linux@googlemail.com> - 1.9.1-1
- update to latest 1.9.1
- drop appmenu patch

* Sat Sep 28 2013 Leigh Scott <leigh123linux@googlemail.com> - 1.0.0-0.15.gitcb4d724
- patch to fix appmenu issue

* Wed Sep 18 2013 Leigh Scott <leigh123linux@googlemail.com> - 1.0.0-0.14.gitcb4d724
- update to latest git

* Sun Aug 25 2013 Leigh Scott <leigh123linux@googlemail.com> - 1.0.0-0.13.gitaf7fe4d
- update to latest git
- Change buildrequires to cinnamon-desktop-devel
- drop 3.9 patch
- add keyboard branch patch

* Thu Aug 22 2013 Leigh Scott <leigh123linux@googlemail.com> - 1.0.0-0.12.gitb8b57d9
- redo 3.9 patch for more gnome changes

* Thu Aug 22 2013 Leigh Scott <leigh123linux@googlemail.com> - 1.0.0-0.11.gitb8b57d9
- rebuilt

* Mon Aug 12 2013 Leigh Scott <leigh123linux@googlemail.com> - 1.0.0-0.10.gitb8b57d9
- update to latest git

* Sat Aug 10 2013 Leigh Scott <leigh123linux@googlemail.com> - 1.0.0-0.9.git50787a1
- update to latest git
- drop gsettings patch

* Sat Aug 10 2013 Leigh Scott <leigh123linux@googlemail.com> - 1.0.0-0.8.git3f73d50
- add patch to remove obsolete gsettings for menu and button icon till upstream fixes it

* Tue Aug 06 2013 Leigh Scott <leigh123linux@googlemail.com> - 1.0.0-0.7.git3f73d50
- update to latest git
- remove dead bits from spec file

* Wed Jul 31 2013 Leigh Scott <leigh123linux@googlemail.com> - 1.0.0-0.6.git6c1f75c
- update to latest git
- drop media key patch

* Wed Jul 24 2013 Leigh Scott <leigh123linux@googlemail.com> - 1.0.0-0.5.gitd5d8dfa
- change require gnome control-center to cinnamon

* Wed Jul 24 2013 Leigh Scott <leigh123linux@googlemail.com> - 1.0.0-0.4.gitd5d8dfa
- add patch to fix media keys
- update to latest git

* Sat Jul 20 2013 Leigh Scott <leigh123linux@googlemail.com> - 1.0.0-0.3.git42cc1ce
- rebuilt as the koji storage move lost the previous build

* Thu Jul 18 2013 Leigh Scott <leigh123linux@googlemail.com> - 1.0.0-0.2.git42cc1ce
- add %%config to files
- fix directory ownership on %%{_libdir}/cinnamon-settings-daemon-3.0
- remove dead bits from spec file

* Sat May 25 2013 Leigh Scott <leigh123linux@googlemail.com> - 1.0.0-0.1.git42cc1ce
- Initial build


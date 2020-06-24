%global gtk3_version                      3.16.0
%global glib2_version                     2.37.3
%global startup_notification_version      0.5
%global gtk_doc_version                   1.9
%global po_package                        cinnamon-desktop-3.0

Summary: Shared code among cinnamon-session, nemo, etc
Name:    cinnamon-desktop
Version: 4.6.2
Release: 1%{?dist}
License: GPLv2+ and LGPLv2+ and MIT
URL:     https://github.com/linuxmint/%{name}
Source0: %url/archive/%{version}/%{name}-%{version}.tar.gz
Source1: x-cinnamon-mimeapps.list

Patch0:   set_font_defaults.patch

Requires: redhat-menus

# Make sure to update libgnome schema when changing this
%if 0%{?fedora}
Requires: system-backgrounds-gnome
%else
Requires: system-backgrounds
%endif

# Make sure that gnome-themes-standard gets pulled in for upgrades
Requires: gnome-themes-standard


BuildRequires: pkgconfig(gtk+-3.0) >= %{gtk3_version}
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: pkgconfig(libstartup-notification-1.0) >= %{startup_notification_version}
BuildRequires: pkgconfig(xkbfile)
BuildRequires: pkgconfig(xkeyboard-config)
BuildRequires: pkgconfig(gtk-doc) >= %{gtk_doc_version}
BuildRequires: pkgconfig(libpulse)
BuildRequires: pkgconfig(accountsservice) 
BuildRequires: meson
BuildRequires: intltool
BuildRequires: itstool

%description
The cinnamon-desktop package contains an internal library
(libcinnamon-desktop) used to implement some portions of the CINNAMON
desktop, and also some data files and other shared components of the
CINNAMON user environment.

%package devel
Summary:  Libraries and headers for libcinnamon-desktop
License:  LGPLv2+
Requires: %{name}%{?_isa} = %{version}-%{release}

Requires: gtk3-devel >= %{gtk3_version}
Requires: glib2-devel >= %{glib2_version}
Requires: startup-notification-devel >= %{startup_notification_version}

%description devel
Libraries and header files for the CINNAMON-internal private library
libcinnamon-desktop.

%prep
%autosetup -p1

%build
%meson -Dpnp_ids=/usr/share/hwdata/pnp.ids -Ddeprecation_warnings=false
%meson_build

%install
%meson_install

#Remove libtool archives.
find %buildroot -name '*.la' -or -name '*.a' | xargs rm -f

mkdir -p %buildroot%{_datadir}/applications/
install -m 644 %SOURCE1 %buildroot%{_datadir}/applications/x-cinnamon-mimeapps.list

%find_lang %{po_package} --all-name --with-gnome


%ldconfig_scriptlets


%files -f %{po_package}.lang
%doc AUTHORS README
%license COPYING COPYING.LIB
%{_datadir}/glib-2.0/schemas/org.cinnamon.*.xml
%{_datadir}/applications/x-cinnamon-mimeapps.list
%{_libdir}/*.so.*
%{_libdir}/girepository-1.0/C*.typelib

%files devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/cinnamon-desktop/
%{_datadir}/gir-1.0/C*.gir

%changelog
* Sun Jun 21 2020 Leigh Scott <leigh123linux@gmail.com> - 4.6.2-1
- Update to 4.6.2 release

* Sat Jun 06 2020 Leigh Scott <leigh123linux@gmail.com> - 4.6.1-1
- Update to 4.6.1 release

* Tue May 12 2020 Leigh Scott <leigh123linux@gmail.com> - 4.6.0-1
- Update to 4.6.0 release

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 12 2019 Leigh Scott <leigh123linux@googlemail.com> - 4.4.1-1
- Update to 4.4.1 release

* Sat Nov 16 2019 Leigh Scott <leigh123linux@googlemail.com> - 4.4.0-1
- Update to 4.4.0 release

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 14 2019 Leigh Scott <leigh123linux@googlemail.com> - 4.2.0-1
- Update to 4.2.0 release

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 12 2018 Leigh Scott <leigh123linux@googlemail.com> - 4.0.1-1
- Update to 4.0.1 release

* Tue Oct 30 2018 Leigh Scott <leigh123linux@googlemail.com> - 4.0.0-1
- Update to 4.0.0 release

* Sun Oct 07 2018 Leigh Scott <leigh123linux@googlemail.com> - 3.8.1-3
- Drop EPEL/RHEL support

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun May 06 2018 Leigh Scott <leigh123linux@googlemail.com> - 3.8.1-1
- Update to 3.8.1 release

* Mon Apr 16 2018 Leigh Scott <leigh123linux@googlemail.com> - 3.8.0-1
- Update to 3.8.0 release

* Wed Feb 21 2018 Leigh Scott <leigh123linux@googlemail.com> - 3.6.3-0.5.20180218git119a96b
- Update to git snapshot

* Thu Feb 15 2018 Leigh Scott <leigh123linux@googlemail.com> - 3.6.3-0.4.20180214git90547df
- Update to git snapshot

* Sat Feb 10 2018 Leigh Scott <leigh123linux@googlemail.com> - 3.6.3-0.3.20180209git90bf499
- Fix missing schema

* Fri Feb 09 2018 Leigh Scott <leigh123linux@googlemail.com> - 3.6.3-0.2.20180209git90bf499
- Update to git snapshot

* Thu Feb 08 2018 Leigh Scott <leigh123linux@googlemail.com> - 3.6.3-0.1.20180208gited3d24c
- Update to git snapshot

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Nov 13 2017 Leigh Scott <leigh123linux@googlemail.com> - 3.6.2-3
- update to 3.6.2 release

* Sat Oct 28 2017 Leigh Scott <leigh123linux@googlemail.com> - 3.6.0-2
- Update mimeapps list

* Mon Oct 23 2017 Leigh Scott <leigh123linux@googlemail.com> - 3.6.0-1
- update to 3.6.0 release

* Wed Aug 30 2017 Björn Esser <besser82@fedoraproject.org> - 3.4.2-5
- Fix invocation of `/sbin/ldconfig`

* Wed Aug 30 2017 Björn Esser <besser82@fedoraproject.org> - 3.4.2-4
- Adjustments for EPEL7

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 21 2017 Leigh Scott <leigh123linux@googlemail.com> - 3.4.2-1
- update to 3.4.2 release

* Tue May 23 2017 Leigh Scott <leigh123linux@googlemail.com> - 3.4.1-1
- update to 3.4.1 release

* Wed May 03 2017 Leigh Scott <leigh123linux@googlemail.com> - 3.4.0-1
- update to 3.4.0 release

* Tue May 02 2017 Leigh Scott <leigh123linux@googlemail.com> - 3.4.0-0.2.20170421git75d297a
- remove requires xorg-x11-drv-libinput

* Fri Apr 21 2017 Leigh Scott <leigh123linux@googlemail.com> - 3.4.0-0.1.20170421git75d297a
- update to git snapshot

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Dec 14 2016 leigh scott <leigh123linux@googlemail.com> - 3.2.4-1
- update to 3.2.4 release

* Sat Dec 10 2016 leigh scott <leigh123linux@googlemail.com> - 3.2.2-1
- update to 3.2.2 release

* Wed Nov 23 2016 Dan Horák <dan[at]danny.cz> - 3.2.1-2
- no libinput driver on s390(x)

* Wed Nov 23 2016 leigh scott <leigh123linux@googlemail.com> - 3.2.1-1
- update to 3.2.1 release

* Thu Nov 10 2016 Leigh Scott <leigh123linux@googlemail.com> - 3.2.0-3
- switch to xorg-x11-drv-libinput
- remove requires xorg-x11-drv-synaptics
- add requires xorg-x11-drv-libinput

* Tue Nov 08 2016 Leigh Scott <leigh123linux@googlemail.com> - 3.2.0-2
- patch PAM file for selinux

* Mon Nov 07 2016 Leigh Scott <leigh123linux@googlemail.com> - 3.2.0-1
- update to 3.2.0 release

* Tue Sep 06 2016 Peter Hutterer <peter.hutterer@redhat.com> 3.0.2-2
- Move the synaptics override to /etc/ (related #1338585)

* Sat May 21 2016 Leigh Scott <leigh123linux@googlemail.com> - 3.0.2-1
- update to 3.0.2 release

* Tue May 17 2016 Leigh Scott <leigh123linux@googlemail.com> - 3.0.1-2
- add setting for gtk overlay scrollbars

* Mon May 16 2016 Leigh Scott <leigh123linux@googlemail.com> - 3.0.1-1
- update to 3.0.1 release

* Sun May 01 2016 Leigh Scott <leigh123linux@googlemail.com> - 3.0.0-2
- remove account service background as it's ubuntu only

* Sat Apr 23 2016 Leigh Scott <leigh123linux@googlemail.com> - 3.0.0-1
- update to 3.0.0 release

* Wed Mar 09 2016 Leigh Scott <leigh123linux@googlemail.com> - 2.8.1-1
- update to 2.8.1 release

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov 09 2015 Leigh Scott <leigh123linux@googlemail.com> - 2.8.0-2
- rebuilt

* Fri Oct 16 2015 Leigh Scott <leigh123linux@googlemail.com> - 2.8.0-1
- update to 2.8.0 release

* Thu Sep 10 2015 Leigh Scott <leigh123linux@googlemail.com> - 2.6.5-5
- fix warning message when background is xml file

* Mon Jul 13 2015 Dan Horák <dan[at]danny.cz> - 2.6.5-4
- no synaptic driver on s390(x)

* Fri Jul 03 2015 Leigh Scott <leigh123linux@googlemail.com> - 2.6.5-3
- block known buggy images (bz 1212827)

* Thu Jul 02 2015 Leigh Scott <leigh123linux@googlemail.com> - 2.6.5-2
- add requires xorg-x11-drv-synaptics

* Sun Jun 28 2015 Leigh Scott <leigh123linux@googlemail.com> - 2.6.5-1
- update to 2.6.5 release

* Fri Jun 26 2015 Leigh Scott <leigh123linux@googlemail.com> - 2.6.4-6
- move synaptics conf to posttrans

* Fri Jun 26 2015 Leigh Scott <leigh123linux@googlemail.com> - 2.6.4-5
- ghost the synaptics conf file

* Thu Jun 18 2015 Leigh Scott <leigh123linux@googlemail.com> - 2.6.4-4
- rename the mimeapps.list

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 01 2015 Leigh Scott <leigh123linux@googlemail.com> - 2.6.4-2
- use new license macro

* Mon Jun 01 2015 Leigh Scott <leigh123linux@googlemail.com> - 2.6.4-1
- update to 2.6.4 release

* Thu May 28 2015 Leigh Scott <leigh123linux@googlemail.com> - 2.6.3-2
- Fix synaptics issue

* Mon May 25 2015 Leigh Scott <leigh123linux@googlemail.com> - 2.6.3-1
- update to 2.6.3 release

* Thu May 21 2015 Leigh Scott <leigh123linux@googlemail.com> - 2.6.2-1
- update to 2.6.2 release

* Thu May 21 2015 Leigh Scott <leigh123linux@googlemail.com> - 2.6.1-2
- add upstream patch to fix USERNAME issue

* Thu May 21 2015 Leigh Scott <leigh123linux@googlemail.com> - 2.6.1-1
- update to 2.6.1 release

* Wed May 20 2015 Leigh Scott <leigh123linux@googlemail.com> - 2.6.0-1
- update to 2.6.0 release

* Wed May 06 2015 Leigh Scott <leigh123linux@googlemail.com> - 2.5.1-0.2.gitfcbafe3
- update to git snapshot

* Tue May 05 2015 Leigh Scott <leigh123linux@googlemail.com> - 2.5.1-0.1.gitdb43144
- update to git snapshot

* Fri Apr 24 2015 Leigh Scott <leigh123linux@googlemail.com> - 2.4.2-2
- add cinnamon-mimeapps.list for F22

* Sun Nov 23 2014 Leigh Scott <leigh123linux@googlemail.com> - 2.4.2-1
- update to 2.4.2

* Wed Nov 19 2014 Leigh Scott <leigh123linux@googlemail.com> - 2.4.1-3
- set default screensaver fonts

* Wed Nov 12 2014 Leigh Scott <leigh123linux@googlemail.com> - 2.4.1-2
- patch cinnamon-desktop-migrate-mediakeys

* Sat Nov 08 2014 Leigh Scott <leigh123linux@googlemail.com> - 2.4.1-1
- update to 2.4.1

* Fri Oct 31 2014 Leigh Scott <leigh123linux@googlemail.com> - 2.4.0-1
- update to 2.4.0

* Fri Oct 10 2014 Leigh Scott <leigh123linux@googlemail.com> - 2.4.0-0.2.git5194ced
- update to latest git

* Tue Sep 30 2014 Leigh Scott <leigh123linux@googlemail.com> - 2.4.0-0.1.gitf4ee205
- update to latest git

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 22 2014 Kalev Lember <kalevlember@gmail.com> - 2.2.3-3
- Rebuilt for gobject-introspection 1.41.4

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 20 2014 Leigh Scott <leigh123linux@googlemail.com> - 2.2.3-1
- update to 2.2.3

* Sun May 11 2014 Leigh Scott <leigh123linux@googlemail.com> - 2.2.2-1
- update to 2.2.2

* Sat May 03 2014 Leigh Scott <leigh123linux@googlemail.com> - 2.2.1-1
- update to 2.2.1

* Sat Apr 12 2014 Leigh Scott <leigh123linux@googlemail.com> - 2.2.0-1
- update to 2.2.0

* Mon Dec 02 2013 Leigh Scott <leigh123linux@googlemail.com> - 2.0.4-1
- update to 2.0.4

* Sun Nov 03 2013 Leigh Scott <leigh123linux@googlemail.com> - 2.0.3-1
- update to 2.0.3

* Thu Oct 24 2013 Leigh Scott <leigh123linux@googlemail.com> - 2.0.2-1
- update to 2.0.2

* Wed Oct 09 2013 Leigh Scott <leigh123linux@googlemail.com> - 2.0.1-1
- update to 2.0.1

* Wed Oct 02 2013 Leigh Scott <leigh123linux@googlemail.com> - 2.0.0-1
- update to 2.0.0

* Mon Sep 30 2013 Leigh Scott <leigh123linux@googlemail.com> - 1.9.1-1
- update to 1.9.1

* Wed Sep 18 2013 Leigh Scott <leigh123linux@googlemail.com> - 1.0.0-0.4.git37ca83b
- update to latest git

* Sun Aug 25 2013 Leigh Scott <leigh123linux@googlemail.com> - 1.0.0-0.3.git22ab5c0
- update to latest git
- change to linuxmint source

* Sat Aug 24 2013 Leigh Scott <leigh123linux@googlemail.com> - 1.0.0-0.2.gita631087
- update to latest git

* Sat Aug 24 2013 Leigh Scott <leigh123linux@googlemail.com> - 1.0.0-0.1.gitbf41f5f
- initial build



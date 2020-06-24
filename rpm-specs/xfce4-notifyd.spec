# Review: https://bugzilla.redhat.com/show_bug.cgi?id=499282

%global minorversion 0.6
%global xfceversion 4.14

Name:           xfce4-notifyd
Version:        0.6.1
Release:        1%{?dist}
Summary:        Simple notification daemon for Xfce

License:        GPLv2
URL:            http://goodies.xfce.org/projects/applications/xfce4-notifyd
#VCS:           git:git://http://git.xfce.org/apps/xfce4-notifyd/
Source0:        http://archive.xfce.org/src/apps/%{name}/%{minorversion}/%{name}-%{version}.tar.bz2

BuildRequires:  gcc-c++
BuildRequires:  gtk3-devel >= 3.20.0
BuildRequires:  libxfce4ui-devel >= %{xfceversion}
BuildRequires:  libxfce4util-devel >= %{xfceversion}
BuildRequires:  xfconf-devel >= %{xfceversion}
BuildRequires:  xfce4-panel-devel >= %{xfceversion}
BuildRequires:  glib2-devel >= 2.42.0
BuildRequires:  libnotify-devel >= 0.7.0
BuildRequires:  desktop-file-utils
BuildRequires:  intltool
BuildRequires:  systemd

Requires:       dbus
Requires:       hicolor-icon-theme
# for compatibility this package provides
Provides:       desktop-notification-daemon
# and obsoletes all notification-daemon-xfce releases
Obsoletes:      notification-daemon-xfce <= 0.3.7


%description
Xfce4-notifyd is a simple, visually-appealing notification daemon for Xfce 
that implements the freedesktop.org desktop notifications specification.
Features:
* Themable using the GTK+ theming mechanism
* Visually appealing: rounded corners, shaped windows
* Supports transparency and fade effects


%prep
%setup -q


%build
%configure
%make_build

%install
%make_install

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}-config.desktop
%find_lang %{name}

# remove libtool archives
find $RPM_BUILD_ROOT -name \*.la -exec rm {} \;

%ldconfig_scriptlets

%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog NEWS README TODO
%{_bindir}/xfce4-notifyd-config
%{_libdir}/xfce4/notifyd/
%{_libdir}/xfce4/panel/plugins/libnotification-plugin.so
%{_datadir}/applications/xfce4-notifyd-config.desktop
%{_datadir}/dbus-1/services/org.xfce.xfce4-notifyd.Notifications.service
%{_datadir}/icons/hicolor/48x48/apps/xfce4-notifyd.png
%{_datadir}/themes/Default/xfce-notify-4.0/
%{_datadir}/themes/Smoke/
%{_datadir}/themes/ZOMG-PONIES!/
%{_datadir}/themes/Bright/
%{_datadir}/themes/Retro/
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/xfce4/panel/plugins/notification-plugin.desktop
%{_mandir}/man1/xfce4-notifyd-config.1.*
%{_userunitdir}/xfce4-notifyd.service

%changelog
* Mon May 04 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.6.1-1
- Update to 0.6.1

* Wed Apr 08 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.6.0-1
- Update to 0.6.0

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 22 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.4.4-1
- Update to 0.4.4

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Oct 28 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.4.3-1
- Update to 0.4.3

* Sat Aug 11 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.4.2-20
- Rebuilt (xfce 4.13)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Mar 03 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.4.2-2
- Modernize spec

* Thu Mar 01 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.4.2-1
- Update to 0.4.2

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Dec 12 2017 Kevin Fenzi <kevin@scrye.com> - 0.4.1-1
- Update to 0.4.1

* Wed Oct 18 2017 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.4.0-2
- Add xfce4-panel-devel as buildrequires
- Updates files section

* Wed Oct 18 2017 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.4.0-1
- Update to 0.4.0

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Mar 20 2017 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.3.6-1
- Update to 0.3.6

* Mon Feb 13 2017 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.3.5-1
- Update to 0.3.5

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Nov 09 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.3.4-1
- Update to 0.3.4

* Sun Oct 02 2016 Kevin Fenzi <kevin@scrye.com> - 0.3.3-1
- Update to 0.3.3. bugfix release

* Sat Sep 10 2016 Kevin Fenzi <kevin@scrye.com> - 0.3.2-1
- Update to 0.3.2. bugfix release

* Tue Sep 06 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.3.1-1
- Update to 0.3.1. bugfix release

* Fri Jul 29 2016 Kevin Fenzi <kevin@scrye.com> - 0.3.0-1
- Update to 0.3.0. Fixes bug #1361562

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Feb 28 2015 Kevin Fenzi <kevin@scrye.com> 0.2.4-7
- Rebuild again with provider and against Xfce 4.12

* Sat Feb 28 2015 Kevin Fenzi <kevin@scrye.com> 0.2.4-6
- Rebuild without provider to bootstrap against Xfce 4.12

* Sat Feb 21 2015 Till Maas <opensource@till.name> - 0.2.4-5
- Rebuilt for Fedora 23 Change
  https://fedoraproject.org/wiki/Changes/Harden_all_packages_with_position-independent_code

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu May 09 2013 Christoph Wickert <cwickert@fedoraproject.org> - 0.2.4-1
- Update to 0.2.4

* Mon Apr 22 2013 Christoph Wickert <cwickert@fedoraproject.org> - 0.2.3-1
- Update to 0.2.3 (fixes #759053 and #926785)
- BR libnotify-devel
- Drop upstreamed patches

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Oct 06 2012 Christoph Wickert <cwickert@fedoraproject.org> - 0.2.2-6
- Remove obsolete libsexy checks
- Add patch to avoid flickering
- Add patch to support image URI locations
- Make xfce4-notifyd-config show up in xfce4-settings-manager

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Apr 01 2012 Kevin Fenzi <kevin@scrye.com> - 0.2.2-4
- Rebuild for new lbxfce4util

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.2.2-2
- Rebuild for new libpng

* Tue Aug 09 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.2.2-1
- Update to 0.2.2
- Remove upstreamed Fix-race-with-window-becoming-invalid.patch

* Sun Jul 31 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.2.1-3
- Fix crash in handle_error. Thanks to Ricky Zhou (#706677)
- Remove obsolete BuildRequires libglade2-devel

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Feb 02 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.2.1-1
- Update to 0.2.1 (fixes #660549)
- Own %%{_libdir}/xfce4/notifyd/

* Sat Nov 27 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.2.0-1
- Update to 0.2.0

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.0-2
- Patch to rename dbus-service file to avoid conflict with notification-daemon
- Add Debian's patch support the reason arg in libnotify 0.4.5

* Mon Feb 23 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.0-1
- Initial Fedora Package

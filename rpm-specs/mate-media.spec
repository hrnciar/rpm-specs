Name:           mate-media
Version:        1.24.0
Release:        2%{?dist}
Summary:        MATE media programs
License:        GPLv2+ and LGPLv2+
URL:            http://mate-desktop.org
Source0:        http://pub.mate-desktop.org/releases/1.24/%{name}-%{version}.tar.xz

# https://github.com/mate-desktop/mate-media/pull/157
Patch1:         mate-media_0001-panel-applet-ensure-speaker-can-be-shown-alongside-o.patch

BuildRequires:  desktop-file-utils
BuildRequires:  gtk3-devel
BuildRequires:  libmatemixer-devel
BuildRequires:  libxml2-devel
BuildRequires:  libcanberra-devel
BuildRequires:  mate-desktop-devel
BuildRequires:  mate-common
BuildRequires:  mate-panel-devel

%description
This package contains a few media utilities for the MATE desktop,
including a volume control.


%prep
%autosetup -p1

%build
%configure \
        --disable-static \
        --disable-schemas-compile \
        --enable-statusicon=yes

make %{?_smp_mflags} V=1

%install
%{make_install}

find %{buildroot} -name '*.la' -exec rm -rf {} ';'

desktop-file-install                                                    \
        --delete-original                                               \
        --dir=%{buildroot}%{_datadir}/applications                      \
%{buildroot}%{_datadir}/applications/mate-volume-control.desktop

# disable autostart of na-tray-applet
rm -rf %{buildroot}%{_sysconfdir}/xdg/autostart/mate-volume-control-status-icon.desktop

%find_lang %{name} --with-gnome --all-name


%files -f %{name}.lang
%doc AUTHORS COPYING NEWS README
%{_mandir}/man1/*
%{_bindir}/mate-volume-control
%{_bindir}/mate-volume-control-status-icon
%{_datadir}/mate-media/
%{_datadir}/sounds/mate/
%{_datadir}/applications/mate-volume-control.desktop
%{_libexecdir}/mate-volume-control-applet
%{_datadir}/dbus-1/services/org.mate.panel.applet.GvcAppletFactory.service
%{_datadir}/mate-panel/applets/org.mate.applets.GvcApplet.mate-panel-applet


%changelog
* Sun Mar 08 2020 Wolfgang Ulbrich <fedora@raveit.de> - 1.24.0-2
- fix volume-applet for vertical panels
- rhbz (#1794568)

* Mon Feb 10 2020 Wolfgang Ulbrich <fedora@raveit.de> - 1.24.0-1
- update to 1.24.0
- build status-applet again

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 20 2019 Wolfgang Ulbrich <fedora@raveit.de> - 1.22.2-1
- update 1.22.2 release

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 01 2019 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.22.1-1
- update to 1.22.1
- disable GtkStatusIcon for f30

* Mon Mar 04 2019 Wolfgang Ulbrich <fedora@raveit.de> - 1.22.0-1
- update to 1.22.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec 20 2018 Wolfgang Ulbrich <fedora@raveit.de> - 1.20.2-1
- update to 1.20.2

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 15 2018 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.20.1-1
- update to 1.20.1 release

* Sun Feb 11 2018 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.20.0-1
- update to 1.20.0 release
- switch to using autosetup

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.19.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Sep 11 2017 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.19.1-1
- update to 1.19.1 release

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.19.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.19.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed May 10 2017 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.19.0-1
- update to 1.19.0 release

* Tue Mar 14 2017 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.18.0-1
- update to 1.18.0 release

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Dec 03 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.17.0-1
- update to 1.17.0 release

* Wed Sep 21 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.16.0-1
- update to 1.16.0 release

* Thu Jun 09 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.15.0-1
- update to 1.15.0 release
- switch to gtk+3

* Wed Apr 06 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.14.0-1
- update to 1.14.0 release

* Sun Feb 07 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.13.0-1
- update to 1.13.0 release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Dec 02 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.12.1-1
- update to 1.12.1 release

* Fri Nov 06 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.12.0-1
- update to 1.12.0 release

* Wed Oct 21 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.11.0-1
- update to 1.11.0 release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue May 05 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.10.0-1
- update to 1.10.0 release

* Sat Apr 04 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.9.90-1
- update to 1.9.90 release

* Sun Nov 23 2014 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.9.2-1
- update to 1.9.2 release

* Tue Nov 11 2014 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.9.1-1
- update to 1.9.1 release

* Mon Oct 27 2014 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.9.0-1
- update to 1.9.0 release

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Mar 05 2014 Dan Mashal <dan.mashal@fedoraproject.org> - 1.8.0-1
- Update to 1.8.0

* Wed Feb 19 2014 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.7.90-1
- update to 1.7.90

* Tue Feb 11 2014 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.7.1-1
- update to 1.7.1 release
- remove --disable-scrollkeeper configure flag
- goodby gst-mixer for f21, fix rhbz (#1045742)
- switch complete to pulse-audio

* Mon Jan 20 2014 Wolfgang Ulbrich <chat-to-me@raveit.de> 1.7.0-1
- update to 1.7.0 release
- use modern 'make install' macro
- change BR's
- add --with-gnome --all-name for find language
- clean up file section

* Fri Jan 3 2014 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.6.1-1
- update to 1.6.1 release
- removed upstreamed multimedia category patch

* Sun Sep 22 2013 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.6.0-4
- enable pulseaudio, fix rhbz (#1008011)
- cleanup BRs
- remove --all-name from find locale
- sort file section
- remove needless gsettings convert file
- show-mixer-controls-in-multimedia-category

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Apr 03 2013 Dan Mashal <dan.mashal@fedoraproject.org> - 1.6.0-1
- Update to latest 1.6.0 stable release.

* Tue Mar 26 2013 Dan Mashal <dan.mashal@fedoraproject.org> 1.5.2-1
- Update to latest upstream release

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Dec 22 2012 Nelson Marques <nmo.marques@gmail.com> - 1.5.1-3
- mate-settings-daemon was build with gstreamer, we want to make
  sure we also have proper gstreamer support here. Only from MATE
  1.8 we will be able to support both backends

* Tue Dec 11 2012 Dan Mashal <dan.mashal@fedoraproject.org> - 1.5.1-2
- Remove duplicate configure flag
- Fix gstreamer applet compilation error the right way

* Mon Dec 10 2012 Dan Mashal <dan.mashal@fedoraproject.org> - 1.5.1-1
- Bump to latest upstream version
- Add patch to fix compilation errors for gstreamer applet
- Clean up spec file
- Add update-desktop-database scriptlet
- Switch to buildroot macro

* Thu Nov 08 2012 Leigh Scott <leigh123linux@googlemail.com> - 1.5.0-1
- update to 1.5.0 release
- drop devel sub-package and obsolete it

* Sat Nov 03 2012 Dan Mashal <dan.mashal@fedoraproject.org> - 1.4.0-4
- Rebuild to fix autoqa bug on bodhi

* Mon Oct 22 2012 Leigh Scott <leigh123linux@googlemail.com> - 1.4.0-3
- add Icon Cache scriptlets

* Mon Oct 22 2012 Leigh Scott <leigh123linux@googlemail.com> - 1.4.0-2
- add LGPLv2+ to license

* Mon Oct 22 2012 Leigh Scott <leigh123linux@googlemail.com> - 1.4.0-1
- Initial build


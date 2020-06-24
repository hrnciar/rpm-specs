Name:           x2goclient
Version:        4.1.2.2
Release:        2%{?dist}
Summary:        X2Go Client application

License:        GPLv2+
URL:            http://www.x2go.org
Source0:        http://code.x2go.org/releases/source/%{name}/%{name}-%{version}.tar.gz
# Drop clumsy attempt at Kerberos delegation
# http://bugs.x2go.org/cgi-bin/bugreport.cgi?bug=731
Patch0:         x2goclient-krb5.patch
# ensure RPM_LD_FLAGS/RPM_OPT_FLAGS are used
# https://bugzilla.redhat.com/show_bug.cgi?id=1306463
Patch2:         x2goclient-optflags.patch
# Select X11 backend on wayland
# https://bugzilla.redhat.com/show_bug.cgi?id=1756430
# https://bugs.x2go.org/cgi-bin/bugreport.cgi?bug=1414
Patch4:         0001-Select-X11-backend-on-wayland.patch
# Also fix desktop files created by session manager
# https://bugzilla.redhat.com/show_bug.cgi?id=1820989
Patch5:         0002-Select-X11-backend-for-desktop-files-created-by-sess.patch

BuildRequires:  gcc-c++
BuildRequires:  cups-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libssh-devel
BuildRequires:  libXpm-devel
%if 0%{?fedora} || 0%{?rhel} >= 7
BuildRequires:  man2html-core
%else
BuildRequires:  man
%endif
BuildRequires:  openldap-devel
%if 0%{?fedora} || 0%{?rhel} >= 8
BuildRequires:  pkgconfig(Qt5)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  qt5-linguist
%else
BuildRequires:  qt-devel
%endif
Requires:       hicolor-icon-theme
Requires:       nxproxy
# For GSSAPI authenticated connections
Requires:       openssh-clients
# For local folder sharing and printing
Requires:       openssh-server
Obsoletes:      x2goplugin < 4.1.2.1
%if 0%{?rhel} == 7
# libssh is x86_64 only for EL7
ExclusiveArch:  x86_64
%endif

%description
X2Go is a server-based computing environment with
    - session resuming
    - low bandwidth support
    - session brokerage support
    - client-side mass storage mounting support
    - client-side printing support
    - audio support
    - authentication by smartcard and USB stick

X2Go Client is a graphical client for the X2Go system.
You can use it to connect to running sessions and start new sessions.


%prep
%autosetup -p1
# Fix up install issues
sed -i -e 's/-o root -g root//' Makefile
sed -i -e '/^MOZPLUGDIR=/s/lib/%{_lib}/' Makefile
%if 0%{?fedora} || 0%{?rhel} >= 8
sed -i -e 's/qt4/qt5/' Makefile
%endif
sed -i -e '/^LIBS /s/$/ -ldl/' x2goclient.pro


%build
%if 0%{?fedora} || 0%{?rhel} >= 8
export PATH=%{_qt5_bindir}:$PATH
%else
export PATH=%{_qt4_bindir}:$PATH
%endif
%make_build


%install
%make_install PREFIX=%{_prefix}
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

mkdir -p %{buildroot}%{_sysconfdir}/httpd/conf.d

%files
%license COPYING LICENSE 
%doc AUTHORS
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
%{_datadir}/%{name}/
%{_mandir}/man1/%{name}.1.gz


%changelog
* Fri Apr 17 2020 Orion Poplawski <orion@nwra.com> - 4.1.2.2-2
- Select X11 backend on wayland for created desktop files (bz#1820989)

* Fri Feb 14 2020 Orion Poplawski <orion@nwra.com> - 4.1.2.2-1
- Update to 4.1.2.2

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 13 2019 Orion Poplawski <orion@nwra.com> - 4.1.2.1-5
- Select X11 backend on wayland (bz#1756430)

* Fri Aug 16 2019 Orion Poplawski <orion@nwra.com> - 4.1.2.1-4
- Add patch to support newer libssh
- Build with Qt5 on RHEL8

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 19 2018 Orion Poplawski <orion@cora.nwra.com> - 4.1.2.1-1
- Update to 4.1.2.1
- Really build against Qt5 on Fedora
- Drops x2goplugin

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Mar 6 2018 Orion Poplawski <orion@cora.nwra.com> - 4.1.1.1-1
- Update to 4.1.1.1

* Tue Feb 20 2018 Orion Poplawski <orion@nwra.com> - 4.1.1.0-4
- Add upstream patch to fix hang when connecting to a server with Kerberos auth
  (bug #1546908)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov 29 2017 Orion Poplawski <orion@cora.nwra.com> - 4.1.1.0-2
- Rebuild for proper libssh
- Make x86_64 only for EL7 (libssh dep)

* Mon Oct 30 2017 Orion Poplawski <orion@cora.nwra.com> - 4.1.1.0-1
- Update to 4.1.1.0

* Wed Sep 20 2017 Orion Poplawski <orion@cora.nwra.com> - 4.1.0.1-1
- Update to 4.1.0.1

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Feb 23 2017 Orion Poplawski <orion@cora.nwra.com> - 4.1.0.0-1
- Update to 4.1.0.0

* Thu Feb 23 2017 Orion Poplawski <orion@cora.nwra.com> - 4.0.5.2-3
- Add patch to disable clumsy attempt at Kerberos delegation

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Sep 21 2016 Orion Poplawski <orion@cora.nwra.com> - 4.0.5.2-1
- Update to 4.0.5.2
- Drop upstream qt5 patch

* Thu Mar 24 2016 Orion Poplawski <orion@cora.nwra.com> - 4.0.5.1-1
- Update to 4.0.5.1
- Drop shell and pubkey patch applied upstream
- Use original qt5 patch
- Use %%license

* Wed Mar 23 2016 Orion Poplawski <orion@cora.nwra.com> - 4.0.5.0-6
- Build with Qt5 for F24+

* Tue Mar 01 2016 Rex Dieter <rdieter@fedoraproject.org> - 4.0.5.0-5
- x2goclient no longer built with $RPM_OPT_FLAGS (#1306463)

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Sep 21 2015 Orion Poplawski <orion@cora.nwra.com> - 4.0.5.0-3
- Fix segfault due to typo (bug #1264609)

* Tue Aug 25 2015 Orion Poplawski <orion@cora.nwra.com> - 4.0.5.0-2
- Use login shells to spawn remote commands (bug #1256799)

* Thu Jul 30 2015 Orion Poplawski <orion@cora.nwra.com> - 4.0.5.0-1
- Update to 4.0.5.0

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed May 27 2015 Orion Poplawski <orion@cora.nwra.com> - 4.0.4.0-1
- Update to 4.0.4.0

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 4.0.3.2-2
- Rebuilt for GCC 5 C++11 ABI change

* Thu Feb 19 2015 Orion Poplawski <orion@cora.nwra.com> - 4.0.3.2-1
- Update to 4.0.3.2

* Mon Dec 1 2014 Orion Poplawski <orion@cora.nwra.com> - 4.0.3.1-1
- Update to 4.0.3.1

* Thu Oct 23 2014 Orion Poplawski <orion@cora.nwra.com> - 4.0.3.0-1
- Update to 4.0.3.0

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jul 14 2014 Orion Poplawski <orion@cora.nwra.com> - 4.0.2.1-1
- Update to 4.0.2.1

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 10 2014 Orion Poplawski <orion@cora.nwra.com> - 4.0.2.0-1
- Update to 4.0.2.0

* Tue Feb 18 2014 Orion Poplawski <orion@cora.nwra.com> - 4.0.1.3-4
- Add patch to fix ssh options (bug #1066744)

* Wed Jan 29 2014 Orion Poplawski <orion@cora.nwra.com> - 4.0.1.3-3
- Add patch to fix libssh password auth issue (bug #1057871)

* Wed Jan 22 2014 Orion Poplawski <orion@cora.nwra.com> - 4.0.1.3-2
- Add patch to fix libssh timeout issue (bug #1053923)

* Wed Jan 22 2014 Orion Poplawski <orion@cora.nwra.com> - 4.0.1.3-1
- Update to 4.0.1.3
- Drop provider patch applied upstream

* Tue Dec 17 2013 Orion Poplawski <orion@cora.nwra.com> - 4.0.1.2-1
- Update to 4.0.1.2
- Update summary and description from upstream
- Split out browser plugin into x2goplugin package
- Add x2goplugin-provider package for apache config

* Wed Sep 11 2013 Orion Poplawski <orion@cora.nwra.com> - 4.0.1.1-1
- Update to 4.0.1.1
- Drop patches applied upstream

* Thu Sep 5 2013 Orion Poplawski <orion@cora.nwra.com> - 4.0.1.0-5
- Build against system qtbrowserplugin

* Fri Aug 30 2013 Orion Poplawski <orion@cora.nwra.com> - 4.0.1.0-4
- Add BR desktop-file-utils and validate desktop file
- Add gtk-update-icon-cache scriptlets

* Wed Apr 10 2013 Orion Poplawski <orion@cora.nwra.com> - 4.0.1.0-3
- Add patch to set dpi automatically

* Thu Mar 28 2013 Orion Poplawski <orion@cora.nwra.com> - 4.0.1.0-2
- Add patch to fix proxy connection issue

* Mon Mar 25 2013 Orion Poplawski <orion@cora.nwra.com> - 4.0.1.0-1
- Update to 4.0.1.0

* Tue Feb 12 2013 Orion Poplawski <orion@cora.nwra.com> - 4.0.0.2-1
- Update to 4.0.0.2

* Fri Jan 18 2013 Orion Poplawski <orion@cora.nwra.com> - 4.0.0.1-1
- Update to 4.0.0.1

* Wed Dec 12 2012 Orion Poplawski <orion@cora.nwra.com> - 3.99.3.1-0.1
- Update to latest git

* Tue Dec 11 2012 Orion Poplawski <orion@cora.nwra.com> - 3.99.3.0-1
- Initial Fedora package

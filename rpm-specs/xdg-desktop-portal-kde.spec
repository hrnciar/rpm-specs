%undefine __cmake_in_source_build

%global base_name    xdg-desktop-portal-kde

Name:    xdg-desktop-portal-kde
Summary: Backend implementation for xdg-desktop-portal using Qt/KF5
Version: 5.20.1
Release: 1%{?dist}

License: GPLv2+
URL:     https://cgit.kde.org/%{base_name}.git

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/%{stable}/plasma/%{version}/%{base_name}-%{version}.tar.xz

BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-rpm-macros
BuildRequires:  qt5-qtdeclarative-devel
BuildRequires:  qt5-qtquickcontrols2-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtbase-private-devel
BuildRequires:  qt5-qtwayland-devel
# libQt5PrintSupport.so.5(Qt_5_PRIVATE_API)(64bit)
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}

BuildRequires:  plasma-wayland-protocols-devel
BuildRequires:  wayland-devel

BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5Wayland)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(KF5Plasma)
BuildRequires:  cmake(KF5Kirigami2)
BuildRequires:  cmake(KF5Declarative)

Requires:   xdg-desktop-portal
# TODO: please document why this dep is needed -- rdieter
Requires:   flatpak

Supplements: (plasma-desktop and (flatpak or snapd))

%description
A backend implementation for xdg-desktop-portal that is using Qt/KF5 and various
pieces of KDE infrastructure.


%prep
%autosetup -n %{base_name}-%{version} -p1


%build
%{cmake_kf5}
%cmake_build


%install
%cmake_install

%find_lang xdg-desktop-portal-kde


%files -f xdg-desktop-portal-kde.lang
%license COPYING
%{_libexecdir}/xdg-desktop-portal-kde
%{_datadir}/dbus-1/services/org.freedesktop.impl.portal.desktop.kde.service
%{_datadir}/xdg-desktop-portal/portals/kde.portal
%{_datadir}/xdg-desktop-portal-kde/qml/*.qml
%{_datadir}/applications/org.freedesktop.impl.portal.desktop.kde.desktop
%{_datadir}/knotifications5/xdg-desktop-portal-kde.notifyrc

%changelog
* Tue Oct 20 15:31:01 CEST 2020 Jan Grulich <jgrulich@redhat.com> - 5.20.1-1
- 5.20.1

* Sun Oct 11 19:50:05 CEST 2020 Jan Grulich <jgrulich@redhat.com> - 5.20.0-1
- 5.20.0

* Fri Sep 18 2020 Jan Grulich <jgrulich@redhat.com> - 5.19.90-1
- 5.19.90

* Fri Sep 11 2020 Jan Grulich <jgrulich@redhat.com> - 5.19.5-2
- rebuild (qt5)

* Tue Sep 01 2020 Jan Grulich <jgrulich@redhat.com> - 5.19.5-1
- 5.19.5

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.19.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Jan Grulich <jgrulich@redhat.com> - 5.19.4-1
- 5.19.4

* Tue Jul 07 2020 Jan Grulich <jgrulich@redhat.com> - 5.19.3-1
- 5.19.3

* Tue Jun 23 2020 Jan Grulich <jgrulich@redhat.com> - 5.19.2-1
- 5.19.2

* Wed Jun 17 2020 Martin Kyral <martin.kyral@gmail.com> - 5.19.1-1
- 5.19.1

* Tue Jun 9 2020 Martin Kyral <martin.kyral@gmail.com> - 5.19.0-1
- 5.19.0

* Fri May 15 2020 Martin Kyral <martin.kyral@gmail.com> - 5.18.90-1
- 5.18.90

* Tue May 05 2020 Jan Grulich <jgrulich@redhat.com> - 5.18.5-1
- 5.18.5

* Mon Apr 06 2020 Rex Dieter <rdieter@fedoraproject.org> - 5.18.4.1-2
- rebuild (qt5)

* Sat Apr 04 2020 Rex Dieter <rdieter@fedoraproject.org> - 5.18.4.1-1
- 5.18.4.1

* Tue Mar 31 2020 Jan Grulich <jgrulich@redhat.com> - 5.18.4-1
- 5.18.4

* Tue Mar 10 2020 Jan Grulich <jgrulich@redhat.com> - 5.18.3-1
- 5.18.3

* Tue Feb 25 2020 Jan Grulich <jgrulich@redhat.com> - 5.18.2-1
- 5.18.2

* Tue Feb 18 2020 Jan Grulich <jgrulich@redhat.com> - 5.18.1-1
- 5.18.1

* Tue Feb 11 2020 Jan Grulich <jgrulich@redhat.com> - 5.18.0-1
- 5.18.0

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.17.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 16 2020 Jan Grulich <jgrulich@redhat.com> - 5.17.90-1
- 5.17.90

* Wed Jan 08 2020 Jan Grulich <jgrulich@redhat.com> - 5.17.5-1
- 5.17.5

* Mon Dec 09 2019 Jan Grulich <jgrulich@redhat.com> - 5.17.4-2
- rebuild (qt5)

* Thu Dec 05 2019 Jan Grulich <jgrulich@redhat.com> - 5.17.4-1
- 5.17.4

* Wed Nov 13 2019 Martin Kyral <martin.kyral@gmail.com> - 5.17.3-1
- 5.17.3

* Wed Oct 30 2019 Jan Grulich <jgrulich@redhat.com> - 5.17.2-1
- 5.17.2

* Wed Oct 23 2019 Jan Grulich <jgrulich@redhat.com> - 5.17.1-1
- 5.17.1

* Thu Oct 10 2019 Jan Grulich <jgrulich@redhat.com> - 5.17.0-1
- 5.17.0

* Wed Sep 25 2019 Jan Grulich <jgrulich@redhat.com> - 5.16.90-2
- rebuild (qt5)

* Fri Sep 20 2019 Martin Kyral <martin.kyral@gmail.com> - 5.16.90-1
- 5.16.90

* Fri Sep 06 2019 Martin Kyral <martin.kyral@gmail.com> - 5.16.5-1
- 5.16.5

* Tue Jul 30 2019 Martin Kyral <martin.kyral@gmail.com> - 5.16.4-1
- 5.16.4

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.16.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 10 2019 Martin Kyral <martin.kyral@gmail.com> - 5.16.3-1
- 5.16.3

* Wed Jun 26 2019 Martin Kyral <martin.kyral@gmail.com> - 5.16.2-1
- 5.16.2

* Tue Jun 25 2019 Rex Dieter <rdieter@fedoraproject.org> - 5.16.1-2
- rebuild (qt5)

* Tue Jun 18 2019 Rex Dieter <rdieter@fedoraproject.org> - 5.16.1-1
- 5.16.1

* Mon Jun 17 2019 Jan Grulich <jgrulich@redhat.com> - 5.16.0-2
- rebuild (qt5)

* Tue Jun 11 2019 Martin Kyral <martin.kyral@gmail.com> - 5.16.0-1
- 5.16.0

* Thu May 16 2019 Martin Kyral <martin.kyral@gmail.com> - 5.15.90-1
- 5.15.90

* Thu May 09 2019 Martin Kyral <martin.kyral@gmail.com> - 5.15.5-1
- 5.15.5

* Wed Apr 03 2019 Rex Dieter <rdieter@fedoraproject.org> - 5.15.4-1
- 5.15.4

* Tue Mar 12 2019 Martin Kyral <martin.kyral@gmail.com> - 5.15.3-1
- 5.15.3

* Sun Mar 03 2019 Rex Dieter <rdieter@fedoraproject.org> - 5.15.2-2
- rebuild (qt5)

* Tue Feb 26 2019 Rex Dieter <rdieter@fedoraproject.org> - 5.15.2-1
- 5.15.2

* Tue Feb 19 2019 Rex Dieter <rdieter@fedoraproject.org> - 5.15.1-1
- 5.15.1

* Wed Feb 13 2019 Martin Kyral <martin.kyral@gmail.com> - 5.15.0-1
- 5.15.0

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.14.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jan 20 2019 Martin Kyral <martin.kyral@gmail.com> - 5.14.90-1
- 5.14.90

* Wed Dec 12 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.14.4-2
- rebuild (qt5)

* Tue Nov 27 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.14.4-1
- 5.14.4

* Thu Nov 08 2018 Martin Kyral <martin.kyral@gmail.com> - 5.14.3-1
- 5.14.3

* Wed Oct 24 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.14.2-1
- 5.14.2

* Tue Oct 16 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.14.1-1
- 5.14.1

* Thu Oct 11 2018 Jan Grulich <jgrulich@redhat.com> - 5.14.0-2
- Make initialization of drm and egl non-fatal

* Sat Oct 06 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.14.0-1
- 5.14.0

* Fri Sep 21 2018 Jan Grulich <jgrulich@redhat.com> - 5.13.90-2
- rebuild (qt5)

* Fri Sep 14 2018 Martin Kyral <martin.kyral@gmail.com> - 5.13.90-1
- 5.13.90

* Tue Sep 04 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.13.5-1
- 5.13.5

* Tue Sep 04 2018 Jan Grulich <jgrulich@redhat.com> - 5.13.4-4
- Make sure we build screencast support

* Fri Aug 31 2018 Jan Grulich <jgrulich@redhat.com> - 5.13.4-3
- Do not link against libspa

* Wed Aug 22 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.13.4-2
- rebuild

* Thu Aug 09 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.13.4-1
- 5.13.4

* Thu Aug 09 2018 Jan Grulich <jgrulich@redhat.com> - 5.13.3-7
- Rebuild for broken updates

* Wed Aug 01 2018 Jan Grulich <jgrulich@redhat.com> - 5.13.3-6
- Search for libpipewire-0.2

* Tue Jul 24 2018 Jan Grulich <jgrulich@redhat.com> - 5.13.3-5
- Add support for PipeWire 0.2.x

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.13.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Martin Kyral <martin.kyral@gmail.com> - 5.13.3-1
- 5.13.3

* Mon Jul 09 2018 Martin Kyral <martin.kyral@gmail.com> - 5.13.2-1
- 5.13.2

* Thu Jun 21 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.13.1-3
- rebuild (qt5)

* Tue Jun 19 2018 Martin Kyral <martin.kyral@gmail.com> - 5.13.1-1
- 5.13.1

* Tue Jun 12 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.13.0-2
- Supplements: (plasma-desktop and (flatpak or snapd))

* Sat Jun 09 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.13.0-1
- 5.13.0

* Sun May 27 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.12.90-2
- rebuild (qt5)
- use %%make_build

* Fri May 18 2018 Martin Kyral <martin.kyral@gmail.com> - 5.12.90-1
- 5.12.90

* Tue May 01 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.12.5-1
- 5.12.5

* Tue Mar 27 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.12.4-1
- 5.12.4

* Tue Mar 06 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.12.3-1
- 5.12.3

* Wed Feb 21 2018 Jan Grulich <jgrulich@redhat.com> - 5.12.2-1
- 5.12.2

* Tue Feb 13 2018 Jan Grulich <jgrulich@redhat.com> - 5.12.1-1
- 5.12.1

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Feb 02 2018 Jan Grulich <jgrulich@redhat.com> - 5.12.0-1
- 5.12.0

* Mon Jan 15 2018 Jan Grulich <jgrulich@redhat.com> - 5.11.95-1
- 5.11.95

* Tue Jan 02 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.11.5-1
- 5.11.5

* Sun Dec 31 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.11.4-2
- rebuild (qt-5.10.0)

* Thu Nov 30 2017 Martin Kyral <martin.kyral@gmail.com> - 5.11.4-1
- 5.11.4

* Mon Nov 27 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.11.3-2
- rebuild (qt5)

* Wed Nov 08 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.11.3-1
- 5.11.3

* Wed Oct 25 2017 Martin Kyral <martin.kyral@gmail.com> - 5.11.2-1
- 5.11.2

* Tue Oct 17 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.11.1-1
- 5.11.1

* Wed Oct 11 2017 Martin Kyral <martin.kyral@gmail.com> - 5.11.0-1
- 5.11.0

* Wed Oct 11 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.10.5-2
- BR: qt5-qtbase-private-devel, drop needless scriptlet, use %%autosetup, cosmetics

* Thu Aug 24 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.10.5-1
- 5.10.5

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.10.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.10.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 21 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.10.4-1
- 5.10.4

* Wed Jun 28 2017 Martin Kyral <martin.kyral@gmail.com> - 5.10.3-1
- 5.10.3

* Wed Jun 14 2017 Martin Kyral <martin.kyral@gmail.com> - 5.10.2-1
- 5.10.2

* Wed May 31 2017 Martin Kyral <martin.kyral@gmail.com> - 5.10.0-1
- 5.10.0 (new package)

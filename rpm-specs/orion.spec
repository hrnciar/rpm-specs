Name:           orion
Version:        1.6.7
Release:        1%{?dist}
Summary:        Seek and watch streams on Twitch

License:        GPLv3+
URL:            https://github.com/alamminsalo/orion
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(Qt5)
BuildRequires:  pkgconfig(Qt5QuickControls2)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5WebEngine)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  libappstream-glib
BuildRequires:  desktop-file-utils
Requires:       hicolor-icon-theme
Requires:       qt5-qtquickcontrols
Requires:       qt5-qtquickcontrols2
Recommends:     (gstreamer1-vaapi or gstreamer1-libav or gstreamer1-plugin-openh264)

# Depends on qt5-qt5webengine
ExclusiveArch: %{qt5_qtwebengine_arches}

%description
A desktop client for Twitch.tv. Features:

 - Login by twitch credentials
 - Desktop notifications
 - Integrated player
 - Chat support
 - Support for live streams and vods

%prep
%autosetup -p1 -n %{name}-%{version}

%build
mkdir build
cd build
%{qmake_qt5} ../ "CONFIG+=multimedia"
%make_build

%install
cd build
%make_install INSTALL_ROOT=%{buildroot}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/Orion.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/Orion.appdata.xml

%files
%license COPYING LICENSE.txt
%doc README.md
%{_bindir}/orion
%{_datadir}/metainfo/Orion.appdata.xml
%{_datadir}/applications/Orion.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

%changelog
* Thu Jan 30 20:14:18 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.6.7-1
- Update to 1.6.7

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jul 20 22:35:54 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.6.6-4
- Add Recommends for h264 decoding

* Wed Jun 26 10:12:40 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.6.6-3
- Add missing Requires qt5-qtquickcontrols2

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 15 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.6.6-1
- Release 1.6.6

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Apr 06 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.6.5-2
- Add missing Requires qt5-qtquickcontrols
- Fixes #1542258

* Fri Apr 06 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.6.5-1
- Release 1.6.5

* Wed Mar 07 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.6.1-4
- Add missing BR gcc-c++

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.6.1-2
- Remove obsolete scriptlets

* Sun Sep 17 2017 Robert-André Mauchin <zebob.m@gmail.com> - 1.6.1-1
- Release 1.6.1

* Thu Jul 20 2017 Robert-André Mauchin <zebob.m@gmail.com> - 1.5.1-2
- Update to Fedora Packaging Guidelines specification

* Sun Jul 09 2017  Robert-André Mauchin <zebob.m@gmail.com> - 1.5.1-1
- Release 1.5.1

* Sun Apr 30 2017 Robert-André Mauchin <zebob.m@gmail.com> - 1.5.1.rc-1
- Pre-release 1.5.1.rc

* Thu Feb 2 2017 Robert-André Mauchin <zebob.m@gmail.com> - 1.4.0-1
- Release 1.4.0

* Sun Oct 16 2016 Robert-André Mauchin <zebob.m@gmail.com> - 1.3.5-1
- Release 1.3.5

* Mon Oct 10 2016 Robert-André Mauchin <zebob.m@gmail.com> - 1.3.2-1
- Release 1.3.2

* Thu Sep 22 2016 Robert-André Mauchin <zebob.m@gmail.com> - 1.3.1-1
- First RPM release

%global _vpath_srcdir Kvantum
%undefine __cmake_in_source_build

Name:           kvantum
Version:        0.16.1
Release:        1%{?dist}
Summary:        SVG-based theme engine for Qt5, KDE and LXQt

License:        GPLv3
URL:            https://github.com/tsujan/Kvantum
Source0:        %url/archive/V%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(Qt5)
BuildRequires:  pkgconfig(Qt5Designer)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  desktop-file-utils
BuildRequires:  kde-filesystem
Requires:       %{name}-data
Requires:       hicolor-icon-theme

%description
Kvantum is an SVG-based theme engine for Qt5, KDE and LXQt, with an emphasis
on elegance, usability and practicality.

Kvantum has a default dark theme, which is inspired by the default theme of
Enlightenment. Creation of realistic themes like that for KDE was the first
reason to make Kvantum but it goes far beyond its default theme: you could
make themes with very different looks and feels for it, whether they be
photorealistic or cartoonish, 3D or flat, embellished or minimalistic, or
something in between, and Kvantum will let you control almost every aspect of
Qt widgets.

Kvantum also comes with extra themes that are installed as root with Qt5
installation and can be selected and activated by using Kvantum Manager.

%package data
Summary:    SVG-based theme engine for Qt5, KDE and LXQt
BuildArch:  noarch
Requires:   kvantum

%description data
Kvantum is an SVG-based theme engine for Qt5, KDE and LXQt, with an emphasis
on elegance, usability and practicality.

This package contains the data needed Kvantum.

%prep
%autosetup -n Kvantum-%{version}

%build
%cmake
%cmake_build

%install
%cmake_install

# desktop-file-validate doesn't recognize LXQt
sed -i "s|LXQt|X-LXQt|" %{buildroot}%{_datadir}/applications/kvantummanager.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/kvantummanager.desktop

%find_lang %{name} --all-name --with-qt

%files
%license Kvantum/COPYING
%doc Kvantum/ChangeLog Kvantum/NEWS Kvantum/README.md
%{_bindir}/kvantummanager
%{_bindir}/kvantumpreview
%{_qt5_plugindir}/styles/libkvantum.so

%files data -f %{name}.lang
%{_datadir}/Kvantum/
%{_datadir}/applications/kvantummanager.desktop
%{_datadir}/color-schemes/Kv*.colors
%{_datadir}/icons/hicolor/scalable/apps/kvantum.svg
%{_datadir}/themes/Kv*/
%dir %{_datadir}/kvantumpreview
%dir %{_datadir}/kvantumpreview/translations
%dir %{_datadir}/kvantummanager
%dir %{_datadir}/kvantummanager/translations

%changelog
* Mon Aug 24 15:30:29 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.16.1-1
- Release 0.16.1 (#1867843)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 01 14:24:08 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.16.0-1
- Release 0.16.0 (#1850067)

* Wed Jun 17 22:50:35 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.15.3-1
- Release 0.15.3 (#1812291)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 11 18:45:16 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.14.1-1
- Release 0.14.1 (#1786895)

* Thu Dec 05 22:47:54 CET 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.13.0-1
- Release 0.13.0 (#1780135)

* Sat Oct 12 14:37:59 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.12.1-1
- Release 0.12.1 (#1761073)

* Tue Oct 08 15:44:10 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.12.0-1
- Release 0.12.0 (#1759377)

* Thu Aug 08 22:28:36 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.11.2-1
- Release 0.11.2

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun May 12 22:31:24 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.11.1-1
- Release 0.11.1 (#1709046)

* Sun Mar 24 14:57:08 CET 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.11.0-1
- Release 0.11.0

* Tue Feb 19 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.10.9-1
- Release 0.10.9

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Nov 06 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.10.8-2
- Remove dependency to kde-filesystem and plasma-desktop

* Tue Oct 02 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.10.8-1
- Initial release

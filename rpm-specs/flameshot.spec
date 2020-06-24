Name: flameshot
Version: 0.6.0
Release: 5%{?dist}

# Main code: GPLv3
# Logo: Free Art License v1.3
# Button icons: Apache License 2.0
# capture/capturewidget.cpp and capture/capturewidget.h: GPLv2
# regiongrabber.cpp: LGPL
# Qt-Color-Widgets: LGPL/GPL
# More information: https://github.com/lupoDharkael/flameshot#license
License: GPLv3+ and ASL 2.0 and GPLv2 and LGPLv3 and Free Art
Summary: Powerful and simple to use screenshot software

URL: https://github.com/lupoDharkael/flameshot
Source0: %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5Network)
BuildRequires: pkgconfig(Qt5Multimedia)
BuildRequires: pkgconfig(Qt5Concurrent)
BuildRequires: pkgconfig(Qt5DBus)
BuildRequires: cmake(Qt5Svg)

BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib
BuildRequires: qt5-linguist
BuildRequires: gcc-c++
BuildRequires: gcc

Requires: hicolor-icon-theme
Requires: qt5-qtsvg%{?_isa}

%description
Powerful and simple to use screenshot software with built-in
editor with advanced features.

%prep
%autosetup -p1
mkdir %{_target_platform}

%build
pushd %{_target_platform}
    %qmake_qt5 PREFIX=%{_prefix} CONFIG+=packaging ..
popd

%make_build -C %{_target_platform}

%install
%make_install INSTALL_ROOT=%{buildroot} -C %{_target_platform}
%find_lang Internationalization --with-qt

%check
appstream-util validate-relax --nonet "%{buildroot}%{_datadir}/metainfo/%{name}.appdata.xml"
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files -f Internationalization.lang
%doc README.md
%license LICENSE img/app/flameshotLogoLicense.txt
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/translations
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/dbus-1/interfaces/*.xml
%{_datadir}/dbus-1/services/*.service
%{_datadir}/icons/hicolor/*/apps/%{name}.*

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 27 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 0.6.0-3
- Added missing runtime requirements (rhbz#1724679).

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Aug 26 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 0.6.0-1
- Updated to version 0.6.0.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Feb 24 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 0.5.1-1
- Updated to version 0.5.1.

* Mon Jan 08 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 0.5.0-2
- Minor SPEC fixes.

* Sat Jan 06 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 0.5.0-1
- Initial SPEC release.

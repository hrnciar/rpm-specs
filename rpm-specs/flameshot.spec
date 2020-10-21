%undefine __cmake_in_source_build

Name: flameshot
Version: 0.8.5
Release: 1%{?dist}

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
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: cmake(Qt5LinguistTools)
BuildRequires: cmake(Qt5Multimedia)
BuildRequires: cmake(Qt5Concurrent)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(Qt5Network)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5DBus)
BuildRequires: cmake(Qt5Gui)
BuildRequires: cmake(Qt5Svg)

BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib
BuildRequires: ninja-build
BuildRequires: gcc-c++
BuildRequires: fdupes
BuildRequires: cmake
BuildRequires: gcc

Requires: hicolor-icon-theme
Requires: qt5-qtsvg%{?_isa}

%description
Powerful and simple to use screenshot software with built-in
editor with advanced features.

%prep
%autosetup -p1

%build
%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release
%cmake_build

%install
%cmake_install
%find_lang Internationalization --with-qt
%fdupes %{buildroot}%{_datadir}/icons

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files -f Internationalization.lang
%doc README.md
%license LICENSE
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/translations
%dir %{_datadir}/bash-completion/completions
%dir %{_datadir}/zsh/site-functions
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_metainfodir}/*.metainfo.xml
%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/zsh/site-functions/_%{name}
%{_datadir}/dbus-1/interfaces/*.xml
%{_datadir}/dbus-1/services/*.service
%{_datadir}/icons/hicolor/*/apps/*

%changelog
* Thu Oct 15 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 0.8.5-1
- Updated to version 0.8.5.

* Tue Sep 29 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 0.8.3-1
- Updated to version 0.8.3.

* Thu Sep 24 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 0.8.1-1
- Updated to version 0.8.1.

* Sun Sep 20 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 0.8.0-1
- Updated to version 0.8.0.

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

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

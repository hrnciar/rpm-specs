Name:           deepin-screensaver
Version:        0.0.10
Release:        3%{?dist}
Summary:        Screensaver Tool
License:        GPLv3+
Url:            https://github.com/linuxdeepin/%{name}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  qt5-qtdeclarative-devel
BuildRequires:  pkgconfig(xscrnsaver)

Requires:       %{name}-data = %{version}-%{release}

%description
Deepin screensaver viewer and tools.

%package data
Summary:        Screensaver data
BuildArch:      noarch
Requires:       xscreensaver-extras
Requires:       xscreensaver-gl-extras

%description data
Extra data for Deepin Screensaver.

%prep
%setup -q
sed -i 's|/lib|/libexec|' xscreensaver/xscreensaver.pro common.pri
sed -i 's|/usr/lib|%{_libexecdir}|' tools/preview/main.cpp

%build
%qmake_qt5 PREFIX=%{_prefix}
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

%files
%doc CHANGELOG.md
%{_bindir}/%{name}
%{_datadir}/dbus-1/services/*
%{_datadir}/dbus-1/interfaces/*

%files data
%{_libexecdir}/%{name}


%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 05 2019 Robin Lee <cheeselee@fedoraproject.org> - 0.0.10-1
- Release 0.0.10

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 28 2019 Robin Lee <cheeselee@fedoraproject.org> - 0.0.7-1
- Initial packaging

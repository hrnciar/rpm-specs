%undefine __cmake_in_source_build
%global         min_qt_version 5.12
%global         min_kf_version 5.66

Name:           kio-fuse
Version:        4.95.0
Release:        2%{?dist}
Summary:        KIO FUSE

License:        GPLv3+
URL:            https://invent.kde.org/system/kio-fuse
Source0:        %{url}/-/archive/v%{version}/%{name}-v%{version}.tar.bz2

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules  >= %{min_kf_version}

BuildRequires:  pkgconfig(fuse3)

BuildRequires:  cmake(Qt5Gui)        >= %{min_qt_version}
BuildRequires:  cmake(Qt5Core)       >= %{min_qt_version}

BuildRequires:  cmake(KF5KIO)        >= %{min_kf_version}
BuildRequires:  cmake(KF5Auth)       >= %{min_kf_version}
BuildRequires:  cmake(KF5Solid)      >= %{min_kf_version}
BuildRequires:  cmake(KF5Codecs)     >= %{min_kf_version}
BuildRequires:  cmake(KF5Service)    >= %{min_kf_version}
BuildRequires:  cmake(KF5CoreAddons) >= %{min_kf_version}
BuildRequires:  cmake(KF5DBusAddons) >= %{min_kf_version}
BuildRequires:  cmake(KF5JobWidgets) >= %{min_kf_version}

Requires:       systemd
Requires:       dbus-common

%description
KioFuse works by acting as a bridge between KDE's KIO filesystem design and
FUSE.


%prep
%autosetup -p1 -n %{name}-v%{version}


%build
%{cmake_kf5}
%cmake_build


%install
%cmake_install


%files
%license LICENSES/GPL-3.0-or-later.txt
%doc README
%{_libexecdir}/kio-fuse
%{_kf5_datadir}/dbus-1/services/org.kde.KIOFuse.service
%{_tmpfilesdir}/%{name}-tmpfiles.conf


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.95.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Yaroslav Sidlovsky <zawertun@gmail.com> - 4.95.0-1
- first spec for version 4.95.0


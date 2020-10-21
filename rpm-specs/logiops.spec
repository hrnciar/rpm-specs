Name:    logiops
Version: 0.2.2
Release: 1%{?dist}
Summary: Unofficial driver for Logitech mice and keyboard

License: GPLv3
URL:     https://github.com/PixlOne/logiops

Source0: https://github.com/PixlOne/logiops/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  systemd-devel
BuildRequires:  systemd-udev
BuildRequires:  systemd-rpm-macros
BuildRequires:  libconfig-devel
BuildRequires:  libevdev-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++

%description
This is an unofficial driver for Logitech mice and keyboard.

This is currently only compatible with HID++ >2.0 devices.

%prep
%setup -q -n %{name}-%{version}

%build
%{cmake}
%{cmake_build}

%install
%{cmake_install}

%post
%systemd_post logid.service

%preun
%systemd_preun logid.service

%postun
%systemd_postun_with_restart logid.service

%files
%{_bindir}/logid
%{_unitdir}/logid.service
%license LICENSE
%doc README.md
%doc TESTED.md
%doc logid.example.cfg

%changelog
* Mon Aug 31 2020 Nicolas De Amicis <deamicis@bluewin.ch> - 0.2.2-1
- Initial packaging

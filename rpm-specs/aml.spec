# -*-Mode: rpm-spec -*-

Name:     aml
Version:  0.1.0
Release:  3%{?dist}
Summary:  Another Main Loop
# main source is ISC
# include/sys/queue.h is BSD
License:  ISC and BSD

URL:      https://github.com/any1/aml
Source:   %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: meson

%description

Event loop handler developed for wayvnc (Wayland VNC server) and
wlvncc (Wayland VNC client) - see https://github.com/any1

Goals:
 * Portability
 * Utility
 * Simplicity

Non-goals:
 * MS Windows (TM) support
 * Solving the C10K problem

Features:
 * File descriptor event handlers
 * Timers
 * Tickers
 * Signal handlers
 * Idle dispatch callbacks
 * Thread pool
 * Interoperability with other event loops

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
This package contains header files for %{name}.

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install

%files
%{_libdir}/lib%{name}.so.0*

%doc README.md

%license COPYING

%files devel
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/*

%changelog
* Tue Aug 04 2020 Bob Hepple <bob.hepple@gmail.com> - 0.1.0-3
- rebuilt

* Sun Aug 02 2020 Bob Hepple <bob.hepple@gmail.com> - 0.1.0-2
- improv description

* Tue Jul 28 2020 Bob Hepple <bob.hepple@gmail.com> - 0.1.0-1
- Initial version of the package

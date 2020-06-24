# -*-Mode: rpm-spec -*-

Name:     neatvnc
Version:  0.1.0
Release:  3%{?dist}
Summary:  a liberally licensed VNC server library
# main source is ISC
# include/sys/queue.h is BSD
# bundled miniz is MIT and Unlicense
License:  ISC and MIT and Unlicense and BSD

URL:      https://github.com/any1/neatvnc
Source:   %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:   neatvnc-remove-cpu-dependent-flags.patch

BuildRequires: gcc
BuildRequires: meson
BuildRequires: pkgconfig(gnutls)
BuildRequires: pkgconfig(libdrm)
# this will not be needed in the next release:
BuildRequires: pkgconfig(libuv)
BuildRequires: pkgconfig(pixman-1)

# removed in later versions:
Provides: bundled(miniz) = 2.1.0

%description

This is a liberally licensed VNC server library that's intended to be
fast and neat. Note: This is a beta release, so the interface is not
yet stable.

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
* Thu Apr 16 2020 Bob Hepple <bob.hepple@gmail.com> - 0.1.0-3
- fixed spelling of Unlicense

* Wed Apr 15 2020 Bob Hepple <bob.hepple@gmail.com> - 0.1.0-2
- fixed per review RHBZ#1824016

* Wed Apr 15 2020 Bob Hepple <bob.hepple@gmail.com> - 0.1.0-1
- Initial version of the package

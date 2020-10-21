# the package gets input from scanner devices from network
# can be possibly dangerous if an attacker camouflages himself
# as a scanner
%global _hardened_build 1

Name:           sane-airscan
Version:        0.99.17
Release:        1%{?dist}
Summary:        SANE backend for AirScan (eSCL) and WSD document scanners
# the exception is defined in LICENSE, meant for SANE project in most cases
License:        GPLv2+ with exceptions
URL:            https://github.com/alexpevzner/sane-airscan
Source:         %{URL}/archive/%{version}/%{name}-%{version}.tar.gz

# backported from upstream


# needed for querying and getting mDNS messages from local network
BuildRequires:  avahi-devel
# project is written in C
BuildRequires:  gcc
# git is used during autosetup
BuildRequires:  git
# creating credentials and SHA256 for UUID
BuildRequires:  gnutls-devel
# needed for creating output image
BuildRequires:  libjpeg-turbo-devel, libpng-devel
# XML data are carried on HTTP protocol, we need to create them and parse them
BuildRequires:  libxml2-devel
# used in Makefile to get the correct compile and link flags
BuildRequires:  pkgconf-pkg-config
# package is meant to be as one of SANE backends - it uses SANE API for handling
# devices, strings, words (bytes) and backend itself
BuildRequires:  sane-backends-devel

# needs shared library implementing the backend
Requires: libsane-airscan%{?_isa} = %{version}-%{release}

%description
This package contains a tool for discovering scanning devices in cases
when automatic discovery fails - airscan-discover.

%package -n libsane-airscan
Summary: SANE backend for eSCL or WSD

%description -n libsane-airscan
This package contain a SANE backend for MFP and document scanners that
implements either eSCL (AirScan/AirPrint scanning) or WSD "driverless"
scanning protocol.


%prep
%autosetup -S git

%build
# we need to set default CFLAGS, CPPFLAGS and LDFLAGS to get flags
# from build system into the build, otherwise project's default
# are used
%set_build_flags
%make_build


%install
mkdir -p %{buildroot}/
%make_install STRIP=''

%files
%license COPYING LICENSE
%{_bindir}/airscan-discover
# I'm not fond of wildcards in %%files, but FPG demands it for manpages
%{_mandir}/man1/airscan-discover.1*

%files -n libsane-airscan
%license COPYING LICENSE
%dir %{_sysconfdir}/sane.d
%config(noreplace) %{_sysconfdir}/sane.d/airscan.conf
%dir %{_sysconfdir}/sane.d/dll.d
%config(noreplace) %{_sysconfdir}/sane.d/dll.d/airscan
%dir %{_libdir}/sane
%{_libdir}/sane/libsane-airscan.so.1
# I'm not fond of wildcards in %%files, but FPG demands it for manpages
%{_mandir}/man5/sane-airscan.5*


%changelog
* Fri Oct 09 2020 Zdenek Dohnal <zdohnal@redhat.com> - 0.99.17-1
- 1886593 - sane-airscan-0.99.17 is available

* Mon Oct 05 2020 Zdenek Dohnal <zdohnal@redhat.com> - 0.99.16-2
- 1882520 - Crash on libsane-airscan when trying to activate scanner

* Tue Sep 01 2020 Zdenek Dohnal <zdohnal@redhat.com> - 0.99.16-1
- 0.99.16

* Mon Aug 24 2020 Zdenek Dohnal <zdohnal@redhat.com> - 0.99.15-1
- 0.99.15

* Mon Aug 17 2020 Zdenek Dohnal <zdohnal@redhat.com> - 0.99.14-1
- 0.99.14 - fixing 1867126

* Thu Aug 13 2020 Zdenek Dohnal <zdohnal@redhat.com> - 0.99.13-2
- 1867692 - airscan driver crashes in mock during wsdd_cleanup()

* Mon Aug 10 2020 Zdenek Dohnal <zdohnal@redhat.com> - 0.99.13-1
- 0.99.13

* Wed Aug 05 2020 Zdenek Dohnal <zdohnal@redhat.com> - 0.99.12-1
- 0.99.12
- removed dependency to glib and libsoup - HTTP parser is implemented inside,
  bringing gnutls dependency
- sort buildrequires alphabetically

* Wed Jul 29 2020 Zdenek Dohnal <zdohnal@redhat.com> - 0.99.11-1
- Initial import (#1859207)

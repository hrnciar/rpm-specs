# the package can work with devices from network, so use hardened build
%global _hardened_build 1

Name: lprint
Version: 1.0
Release: 1%{?dist}
Summary: A Label Printer Application

License: ASL 2.0
URL: https://www.msweet.org/lprint
Source0: https://github.com/michaelrsweet/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz

# dns-sd support for register/sharing devices
BuildRequires: pkgconfig(avahi-client) >= 0.7
# uses CUPS API for arrays, options, rastering, HTTP, IPP support
BuildRequires: cups-devel >= 2.2.0
# written in C
BuildRequires: gcc
# for autosetup
BuildRequires: git
# PNG printing support
BuildRequires: pkgconfig(libpng) >= 1.6.0
# USB printing support
BuildRequires: pkgconfig(libusb-1.0) >= 1.0
# uses Makefile
BuildRequires: make
# using pkg-config in configure script
BuildRequires: pkgconf-pkg-config


%description
LPrint is a label printer application for macOS and Linux. Basically,
LPrint is a print spooler optimized for label printing. It accepts
"raw" print data as well as PNG images (like those used for shipping
labels by most shippers' current web APIs) and has built-in "drivers"
to send the print data to USB and network-connected label printers.


%prep
%autosetup -S git


%build
# use gcc
export CC=%{__cc}

# get system default CFLAGS and LDFLAGS
%set_build_flags

# enable libpng, PAM and libusb support and use avahi for DNS-SD
%configure --enable-libpng \
           --enable-libusb \
           --with-dnssd=avahi \
           --enable-pam

%make_build


%install
%make_install DESTDIR=''

%files
%doc README.md DOCUMENTATION.md DESIGN.md CONTRIBUTING.md CHANGES.md
%license LICENSE NOTICE
%{_bindir}/lprint
%{_mandir}/man1/lprint-add.1*
%{_mandir}/man1/lprint-cancel.1*
%{_mandir}/man1/lprint-default.1*
%{_mandir}/man1/lprint-delete.1*
%{_mandir}/man1/lprint-devices.1*
%{_mandir}/man1/lprint-drivers.1*
%{_mandir}/man1/lprint-jobs.1*
%{_mandir}/man1/lprint-modify.1*
%{_mandir}/man1/lprint-printers.1*
%{_mandir}/man1/lprint-server.1*
%{_mandir}/man1/lprint-shutdown.1*
%{_mandir}/man1/lprint-status.1*
%{_mandir}/man1/lprint-submit.1*
%{_mandir}/man1/lprint.1*
%{_mandir}/man5/lprint.conf.5*


%changelog
* Mon Aug 17 2020 Zdenek Dohnal <zdohnal@redhat.com> - 1.0-1
- Initial import (#1867587)

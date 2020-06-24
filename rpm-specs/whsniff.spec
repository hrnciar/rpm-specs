Name:           whsniff
Version:        1.2
Release:        1%{?dist}
Summary:        Command line utility that interfaces TI CC2531 USB dongle

License:        GPLv2
URL:            https://github.com/homewsn/whsniff
Source0:        https://github.com/homewsn/whsniff/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  libusb-devel

%description
Whsniff is a command line utility that interfaces TI CC2531 USB dongle with
Wireshark for capturing and displaying IEEE 802.15.4 traffic at 2.4 GHz.

Whsniff reads the packets from TI CC2531 USB dongle with sniffer_fw_cc2531
firmware, converts to the PCAP format and writes to the standard output.

%prep
%autosetup

%build
%make_build CFLAGS="%{optflags}"

%install
%make_install PREFIX=%{buildroot} BINDIR=%{buildroot}/usr/bin

%files
%doc ReadMe.md
%license LICENSE
%{_bindir}/%{name}

%changelog
* Fri Feb 07 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.2-1
- Update to latest upstream release 1.2 (rhbz#1800490)

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 04 2019 Fabian Affolter <mail@fabian-affolter.ch> - 1.1-1
- Initial package for Fedora

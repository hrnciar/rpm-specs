Summary:        Scan for mDNS/DNS-SD services published on the local network
Name:           mdns-scan
Version:        0.5
Release:        1%{?dist}
License:        GPLv2+
URL:            https://github.com/alteholz/mdns-scan/
Source0:        https://github.com/alteholz/mdns-scan/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         mdns-scan-0.5-typo.patch
BuildRequires:  make
BuildRequires:  gcc

%description
mdns-scan is a tool for scanning for mDNS/DNS-SD services published on
the local network. It works by issuing a mDNS PTR query to the special
RR _services._dns-sd._udp.local for retrieving a list of all currently
registered services on the local link.

%prep
%setup -q
%patch0 -p1 -b .typo

%build
%make_build CFLAGS="$RPM_OPT_FLAGS $RPM_LD_FLAGS"

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
%make_install
install -D -p -m 0644 %{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1

%files
%license LICENSE
%doc README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Fri May 01 2020 Robert Scheck <robert@fedoraproject.org> 0.5-1
- Upgrade to 0.5 (#1830539)
- Initial spec file for Fedora and Red Hat Enterprise Linux

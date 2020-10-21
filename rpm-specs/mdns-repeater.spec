Summary:        Multicast DNS repeater
Name:           mdns-repeater
Version:        1.11
Release:        2%{?dist}
License:        GPLv2+
URL:            https://github.com/kennylevinsen/mdns-repeater
Source0:        https://github.com/kennylevinsen/mdns-repeater/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}.service
Source2:        %{name}.sysconfig
Source3:        %{name}.tmpfilesd
Patch0:         mdns-repeater-1.11-pidfile.patch
BuildRequires:  gcc
%if 0%{?fedora}
BuildRequires:  systemd-rpm-macros
%endif
%if 0%{?rhel}
BuildRequires:  systemd
%endif
%{?systemd_requires}

%description
mdns-repeater is a Multicast DNS repeater for Linux. Multicast DNS
uses the 224.0.0.51 address, which is "administratively scoped" and
does not leave the subnet.

This program re-broadcasts mDNS packets from one interface to other
interfaces.

%prep
%setup -q
%patch0 -p1 -b .pidfile

%build
gcc \
  $RPM_OPT_FLAGS $RPM_LD_FLAGS \
  -DHGVERSION="\"%{version}\"" \
  -DPIDFILE="\"%{_rundir}/%{name}/%{name}.pid\"" \
  %{name}.c -o %{name}

%install
install -D -p -m 0755 %{name} $RPM_BUILD_ROOT%{_sbindir}/%{name}
install -D -p -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_unitdir}/%{name}.service
install -D -p -m 0644 %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/%{name}
install -D -p -m 0644 %{SOURCE3} $RPM_BUILD_ROOT%{_tmpfilesdir}/%{name}.conf
mkdir -p $RPM_BUILD_ROOT%{_rundir}/%{name}/

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%license LICENSE.txt
%doc README.txt
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%{_unitdir}/%{name}.service
%{_tmpfilesdir}/%{name}.conf
%{_sbindir}/%{name}
%dir %attr(0750,root,root) %{_rundir}/%{name}/

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 01 2020 Robert Scheck <robert@fedoraproject.org> 1.11-1
- Upgrade to 1.11 (#1830458)
- Initial spec file for Fedora and Red Hat Enterprise Linux

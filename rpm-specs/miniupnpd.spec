Name:       miniupnpd
Version:    2.1
Release:    9%{?dist}
Summary:    Daemon to offer UPnP-IGD and NAT-PMP support

License:    BSD
URL:        http://miniupnp.free.fr/
Source0:    http://miniupnp.free.fr/files/%{name}-%{version}.tar.gz
Source1:    miniupnpd.service
# https://github.com/miniupnp/miniupnp/issues/346
Patch1:     miniupnpd-nfc.patch

# CVE patches from upstream
Patch2:     miniupnpd-cve-2019-12107.patch
Patch3:     miniupnpd-cve-2019-12108-12109-1.patch
Patch4:     miniupnpd-cve-2019-12108-12109-2.patch
Patch5:     miniupnpd-cve-2019-12111.patch

BuildRequires:  gcc
%{?systemd_requires}
BuildRequires:  systemd
BuildRequires:  iptables-devel
%if 0%{?with_netfilter}
Buildrequires:  libmnl-devel
Buildrequires:  libnftnl-devel
%endif
BuildRequires:  libuuid-devel
BuildRequires:  procps-ng


%description
The MiniUPnP daemon is a UPnP Internet Gateway Device.

UPnP and NAT-PMP are used to improve internet connectivity for devices behind
a NAT router. Any peer to peer network application such as games, IM, etc. can
benefit from a NAT router supporting UPnP and/or NAT-PMP.


%prep
%setup -q
%patch1 -p2 -b.nfc
%patch2 -p2 -b.cve-2019-12107
%patch3 -p2 -b.cve-12108-12109-1
%patch4 -p2 -b.cve-12108-12109-2
%patch5 -p2 -b.cve-12111


%build
export CFLAGS="%{optflags}"
export LDFLAGS="%{__global_ldflags}"
CONFIG_OPTIONS="--ipv6 --igd2" make %{?_smp_mflags} -f Makefile.linux


%install
export STRIP="/bin/true"
DESTDIR=%{buildroot} make -f Makefile.linux install

install -Dpm 644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service

#Do not ship SysVinit script
rm -f %{buildroot}/etc/init.d/%{name}


%post
%systemd_post %{name}.service


%preun
%systemd_preun %{name}.service


%postun
%systemd_postun_with_restart %{name}.service


%files
%license LICENSE
%doc INSTALL README
%{_sbindir}/%{name}
%dir %{_sysconfdir}/%{name}
%{_sysconfdir}/%{name}/ip6tables_init.sh
%{_sysconfdir}/%{name}/ip6tables_removeall.sh
%{_sysconfdir}/%{name}/iptables_init.sh
%{_sysconfdir}/%{name}/iptables_removeall.sh
%{_sysconfdir}/%{name}/miniupnpd_functions.sh
%config(noreplace) %{_sysconfdir}/%{name}/miniupnpd.conf
%{_mandir}/man8/%{name}.8.gz
%{_unitdir}/%{name}.service


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 13 2019 Michael Cronenworth <mike@cchtml.com> - 2.1-7
- Patch CVEs (RHBZ#1714990,1715005,1715006,1715007)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 25 2019 Björn Esser <besser82@fedoraproject.org> - 2.1-5
- Rebuilt (iptables)

* Sun Feb 03 2019 - Michael Cronenworth <mike@cchtml.com> - 2.1-4
- Upstream patch for kernel 5.0 changes

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 05 2018 - Michael Cronenworth <mike@cchtml.com> - 2.1-1
- Initial release


Name: dhcpcd
Version: 6.11.3
Release: 10%{?dist}
Summary: A minimalistic network configuration daemon with DHCPv4, rdisc and DHCPv6 support
License: BSD
URL: http://roy.marples.name/projects/%{name}/index
Source0: http://roy.marples.name/downloads/%{name}/%{name}-%{version}.tar.xz
Source1: %{name}.service
Source2: %{name}@.service
BuildRequires:  gcc
BuildRequires: systemd
BuildRequires: ntp
BuildRequires: systemd-devel
BuildRequires: ypbind
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
%description
The dhcpcd package provides a minimalistic network configuration daemon
that supports IPv4 and IPv6 configuration including configuration discovery
through NDP, DHCPv4 and DHCPv6 protocols.

%prep
%setup -q

%build
%configure \
    --dbdir=/var/lib/%{name}
make %{?_smp_mflags}

%check
make test

%install
export BINMODE=755
%make_install
find %{buildroot} -name '*.la' -delete -print
install -D -m 644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service
install -D -m 644 %{SOURCE2} %{buildroot}%{_unitdir}/%{name}@.service
install -d %{buildroot}%{_sharedstatedir}/%{_name}

%post
%systemd_post dhcpcd.service

%preun
%systemd_preun dhcpcd.service

%postun
%systemd_postun_with_restart dhcpcd.service

%files
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_datadir}/%{name}/hooks/10-wpa_supplicant
%{_datadir}/%{name}/hooks/15-timezone
%{_datadir}/%{name}/hooks/29-lookup-hostname
%{_datadir}/%{name}/hooks/50-yp.conf
%{_libdir}/%{name}
%{_libexecdir}/%{name}-hooks
%{_libexecdir}/%{name}-run-hooks
%{_mandir}/man5/%{name}.conf.5.gz
%{_mandir}/man8/%{name}-run-hooks.8.gz
%{_mandir}/man8/%{name}.8.gz
%{_sbindir}/%{name}
%{_unitdir}/%{name}.service
%{_unitdir}/%{name}@.service
%{_sharedstatedir}/%{name}

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.11.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.11.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.11.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 6.11.3-7
- Rebuild with fixed binutils

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.11.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.11.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.11.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.11.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.11.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Aug 26 2016 Pavel Šimerda <psimerda@redhat.com> - 6.11.3-1
- New version 6.11.3

* Wed Aug 10 2016 Pavel Šimerda <psimerda@redhat.com> - 6.11.2-1
- New version 6.11.2

* Fri Feb 19 2016 Pavel Šimerda <psimerda@redhat.com> - 6.10.1-4
- initial version

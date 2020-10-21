%global _hardened_build 1

Name:		addrwatch
Version:	1.0.2
Release:	0%{?dist}
Summary:	Monitoring IPv4/IPv6 and Ethernet address pairings

License:	GPLv3
URL:		https://github.com/fln/addrwatch
Source0:	%{url}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:	%{name}.service
Source2:	%{name}.sysconfig

%{?systemd_requires}
BuildRequires:	libpcap-devel, libevent-devel, systemd, mariadb-devel, sqlite-devel, gcc
BuildRequires:	autoconf automake
Requires(pre):	shadow-utils


%description
It main purpose is to monitor network and log discovered Ethernet/IP pairings.

Main features of addrwatch:

 * IPv4 and IPv6 address monitoring
 * Monitoring multiple network interfaces with one daemon
 * Monitoring of VLAN tagged (802.1Q) packets.
 * Output to std-out, plain text file, syslog, sqlite3 db, MySQL db
 * IP address usage history preserving output/logging

Addrwatch is extremely useful in networks with IPv6 auto configuration (RFC4862)
enabled. It allows to track IPv6 addresses of hosts using IPv6 privacy
extensions (RFC4941).

%prep
%autosetup -p1

%build
autoreconf -fiv
%configure --enable-sqlite3 --enable-mysql LDFLAGS="-I/usr/include/mysql -L/usr/lib64/mysql"
%make_build

%install
%make_install
mkdir -p %{buildroot}%{_unitdir}/
install -p -m 644 %{SOURCE1} %{buildroot}%{_unitdir}/
mkdir -p %{buildroot}%{_sysconfdir}/sysconfig/
install -p -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/sysconfig/addrwatch
mkdir -p %{buildroot}/var/lib/addrwatch

%files
%{_bindir}/addrwatch
%{_bindir}/addrwatch_stdout
%{_bindir}/addrwatch_mysql
%{_bindir}/addrwatch_syslog
%{_mandir}/man8/addrwatch.8*
%{_unitdir}/addrwatch.service
%config(noreplace) %{_sysconfdir}/sysconfig/addrwatch
%license COPYING
%attr(-, addrwatch, addrwatch) /var/lib/addrwatch

%pre
getent group %{name} >/dev/null || groupadd -r %{name}
getent passwd %{name} >/dev/null || \
    useradd -r -g %{name} -d /var/lib/%{name} -s /sbin/nologin \
    -c "network neighborhoud watch" %{name}
exit 0

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%changelog
* Mon Sep 28 2020 Jens Kuehnel <bugzilla-redhat@jens.kuehnel.org> - 1.0.1-0
- update to 1.0.2

* Mon Sep 28 2020 Jens Kuehnel <bugzilla-redhat@jens.kuehnel.org> - 1.0.1-9
- rebuilt for new libevent side tag 'f34-build-side-30069'

* Fri Jul 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-8
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 23 2020 Jeff Law <law@redhat.com> - 1.0.1-6
- Use strsignal, not sys_siglist.  Corresponding configure.ac changes
- Run autoreconf to generate new configure file.  Depend on autoconf/automake

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Aug 28 2018 Jens Kuehnel <bugzilla-redhat@jens.kuehnel.org> - 1.0.1-2
- Integrate Comment #2 from Package Review

* Fri Aug 03 2018 Jens Kuehnel <addrwatch@jens.kuehnel.org> - 1.0.1-1
- initial packaging


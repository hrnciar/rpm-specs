%{?el6:%global use_sysvinit 1}
%if "0%{?rhel}" >= "8" || 0%{?fedora}
%global use_subpackages 1
%endif

Name: sshguard
Version: 2.4.1
Release: 3%{?dist}
# The entire source code is BSD
# except src/parser/* which is GPLv2+
# except src/blocker/hash_32a.c & src/blocker/fnv.h which are Public Domain
# the latter two get compiled in, the license is thus superseded
# src/parser/* is compiled into its own binary %%{_libexecdir}/%%{name}/sshg_parser
License: BSD and GPLv2+
Summary: Protects hosts from brute-force attacks against SSH and other services
Url: http://www.sshguard.net
Source0: http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1: %{name}.conf.in
Source2: %{name}.whitelist
Source3: %{name}.init
Source4: %{name}.logrotate

# fnv is a very small implementation of the fnv hash algorithm not worth splitting
# into its own package. It has not seen updates since 2012, and upstream does not
# distribute it as a stand-alone library
Provides: bundled(fnv) = 5.0.2
# simclist is a small library not worth splitting into its own package, and has not
# seen updates since 2011
Provides: bundled(simclist) = 1.4.4

%if 0%{?use_subpackages}
# Autoinstall appropriate firewall backends
Recommends: (%{name}-firewalld if firewalld)
Recommends: (%{name}-iptables if iptables-services)
Recommends: (%{name}-nftables if nftables)
%endif

BuildRequires: gcc
BuildRequires: flex
BuildRequires: byacc
Requires: coreutils
Requires: grep

%if 0%{?use_sysvinit}
# for logging to file
Requires: logrotate
# for SysVinit service configuration
Requires(post): chkconfig
Requires(preun): chkconfig
# for /sbin/service
Requires(preun): initscripts
Requires(postun): initscripts
%else
Requires: systemd
# for systemd service installation support
%if 0%{?fedora} > 29
BuildRequires: systemd-rpm-macros
%else
BuildRequires: systemd
%endif
%endif

%description
Sshguard protects hosts from brute-force attacks against SSH and other
services. It aggregates system logs and blocks repeat offenders using one of
several firewall backends.

Sshguard can read log messages from standard input or monitor one or more log
files. Log messages are parsed, line-by-line, for recognized patterns. If an
attack, such as several login failures within a few seconds, is detected, the
offending IP is blocked. Offenders are unblocked after a set interval, but can
be semi-permanently banned using the blacklist option.

%if 0%{?use_subpackages}
%package iptables
Requires: iptables-services %{name}
Conflicts: %{name}-firewalld %{name}-nftables
Summary: Configuration for iptables backend of SSHGuard
RemovePathPostfixes: .iptables
%description iptables
Sshguard-iptables provides a configuration file for SSHGuard to use iptables
as the firewall backend.

%package firewalld
Requires: firewalld ipset %{name}
Conflicts: %{name}-iptables %{name}-nftables
Summary: Configuration for firewalld backend of SSHGuard
RemovePathPostfixes: .firewalld
%description firewalld
Sshguard-firewalld provides a configuration file for SSHGuard to use firewalld
as the firewall backend.

%package nftables
Requires: nftables %{name}
Conflicts: %{name}-firewalld %{name}-iptables
Summary: Configuration for nftables backend of SSHGuard
RemovePathPostfixes: .nftables
%description nftables
Sshguard-nftables provides a configuration file for SSHGuard to use nftables
as the firewall backend.
%endif

#-- PREP, BUILD & INSTALL -----------------------------------------------------#
%prep
%autosetup -p1

sed -i -e "s|%%{_bindir}|%{_bindir}|g" \
       -e "s|%%{_sbindir}|%{_sbindir}|g" \
       -e "s|%%{_libexecdir}|%{_libexecdir}|g" \
       -e "s|%%{_sysconfdir}|%{_sysconfdir}|g" \
       -e "s|%%{_initddir}|%{_initddir}|g" \
       -e "s|%%{_localstatedir}|%{_localstatedir}|g" \
       -e "s|%%{_sharedstatedir}|%{_sharedstatedir}|g" \
       -e "s|%%{_rundir}|%{_rundir}|g" \
       -e "s|%%{_pkgdocdir}|%{_pkgdocdir}|g" \
       -e "s|%%{name}|%{name}|g" \
       %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4}

%build
%{configure} --prefix=%{_prefix} --sysconfdir=%{_sysconfdir} --sbindir=%{_sbindir} --libexecdir=%{_libexecdir}/%{name}
%{make_build}

%install
%{make_install}
install -p -d -m 0755 %{buildroot}%{_pkgdocdir}/
install -p -d -m 0755 %{buildroot}%{_sysconfdir}/
install -p -d -m 0755 %{buildroot}%{_sharedstatedir}/%{name}/
%if 0%{?use_subpackages}
sed -e "s|__BACKEND__|sshg-fw-firewalld|g" %{SOURCE1} > %{buildroot}%{_sysconfdir}/%{name}.conf.firewalld
sed -e "s|__BACKEND__|sshg-fw-nft-sets|g" %{SOURCE1} > %{buildroot}%{_sysconfdir}/%{name}.conf.nftables
sed -e "s|__BACKEND__|sshg-fw-iptables|g" %{SOURCE1} > %{buildroot}%{_sysconfdir}/%{name}.conf.iptables
chmod 0644 %{buildroot}%{_sysconfdir}/%{name}.conf.*
%endif
install -p -m 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/%{name}.whitelist
%if 0%{?use_sysvinit}
install -p -d -m 0755 %{buildroot}%{_initddir}
install -p -m 0755 %{SOURCE3} %{buildroot}%{_initddir}/%{name}
install -p -d -m 0755 %{buildroot}%{_sysconfdir}/logrotate.d
install -p -m 0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}
%else
install -p -d -m 0755 %{buildroot}%{_unitdir}
sed -i -e "/ExecStartPre=/d" examples/%{name}.service
sed -i -e "s|ExecStart=/usr/local/sbin/sshguard|ExecStart=%{_sbindir}/%{name}|g" examples/%{name}.service
install -p -m 0644 examples/%{name}.service %{buildroot}%{_unitdir}/
%endif

# cleanup
# *.plist is only relevant for MacOS systems
rm examples/net.sshguard.plist
# we already ship a service file
rm examples/sshguard.service

%check
make check

#-- SCRIPTLETS -----------------------------------------------------------------#
%post
%if 0%{?use_sysvinit}
# This adds the proper /etc/rc*.d links for the script
/sbin/chkconfig --add %{_initddir}/%{name}
%else
%systemd_post %{name}.service
%endif

%if 0%{?use_subpackages}
# with iptables backend, sshguard does not auto-create its tables, so we do that here
%post iptables
if [[ $1 -eq 1 ]]; then
  iptables -N sshguard
  iptables -A INPUT -j sshguard
  iptables-save > /etc/sysconfig/iptables
  ip6tables -N sshguard
  ip6tables -A INPUT -j sshguard
  ip6tables-save > /etc/sysconfig/ip6tables
fi
exit 0
%endif

%preun
%if 0%{?use_sysvinit}
if [[ $1 -eq 0 ]]; then
    /sbin/service %{name} stop >/dev/null 2>&1
    /sbin/chkconfig --del %{name}
fi
%else
%systemd_preun %{name}.service
%endif

%postun
%if 0%{?use_sysvinit}
if [ $1 -ge 1 ] ; then
    /sbin/service %{name} condrestart >/dev/null 2>&1 || :
fi
%else
%systemd_postun_with_restart %{name}.service
%endif

#-- FILES ---------------------------------------------------------------------#
%files
%doc examples
%doc README.rst
%doc CONTRIBUTING.rst
%license COPYING
%{_sbindir}/%{name}
%{_mandir}/man8/%{name}*
%{_mandir}/man7/%{name}*
%dir %{_sharedstatedir}/%{name}/
%dir %{_libexecdir}/%{name}/
%{_libexecdir}/%{name}/sshg-logtail
%{_libexecdir}/%{name}/sshg-parser
%{_libexecdir}/%{name}/sshg-blocker
%{_libexecdir}/%{name}/sshg-fw-firewalld
%{_libexecdir}/%{name}/sshg-fw-hosts
%{_libexecdir}/%{name}/sshg-fw-ipfilter
%{_libexecdir}/%{name}/sshg-fw-ipfw
%{_libexecdir}/%{name}/sshg-fw-ipset
%{_libexecdir}/%{name}/sshg-fw-iptables
%{_libexecdir}/%{name}/sshg-fw-null
%{_libexecdir}/%{name}/sshg-fw-pf
%{_libexecdir}/%{name}/sshg-fw-nft-sets
%if 0%{?use_sysvinit}
%{_initddir}/%{name}
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%else
%{_unitdir}/%{name}.service
%endif
%config(noreplace) %{_sysconfdir}/%{name}.whitelist

%if 0%{?use_subpackages}
%files iptables
%config(noreplace) %{_sysconfdir}/%{name}.conf.iptables

%files firewalld
%config(noreplace) %{_sysconfdir}/%{name}.conf.firewalld

%files nftables
%config(noreplace) %{_sysconfdir}/%{name}.conf.nftables
%endif

#-- CHANGELOG -----------------------------------------------------------------#
%changelog
* Fri Sep 11 2020 Christopher Engelhard <ce@lcts.de> 2.4.1-3
- Revert patch from previous release as it could cause attacks
  to not be blocked.

* Thu Sep 03 2020 Christopher Engelhard <ce@lcts.de> 2.4.1-2
- add patch that fixes high load when banning many IPs using firewalld

* Sat Aug 01 2020 Christopher Engelhard <ce@lcts.de> 2.4.1-1
- Update to 2.4.1

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Nov 17 2019 Christopher Engelhard <ce@lcts.de> 2.4.0-12
- include patch to fully whitelist localhost in IPv6/v4 (PR #56)
- add explicit Requires: ipset to firewalld backend

* Mon Oct 21 2019 Christopher Engelhard <ce@lcts.de> 2.4.0-11
- replace systemd with systemd-rpm-macros in f30+ BuildRequires
- remove %%systemd_requires macro

* Fri Oct 04 2019 Christopher Engelhard <ce@lcts.de> 2.4.0-10
- add missing dependencies
- move examples to (docdir)/examples subfolder
- prefix directories with %%dir in %%files
- use complete & commented config files
- add white/blacklisting

* Mon Sep 30 2019 Christopher Engelhard <ce@lcts.de> 2.4.0-9
- add bundled provides for fnv and simclist
- add systemd dependency
- fix changelog formatting
- patch & use upstream service file
- revert 05037d7b - disallow building on rhel < 6
- make package own /usr/libexec/sshguard

* Tue Sep 24 2019 Christopher Engelhard <ce@lcts.de> 2.4.0-8
- Allow building on rhel < 6

* Thu Aug 29 2019 Christopher Engelhard <ce@lcts.de> 2.4.0-7
- add explicit dependency on logrotate for epel6
- fixed iptables install scriptlet

* Sun Aug 25 2019 Christopher Engelhard <ce@lcts.de> 2.4.0-6
- fixes to initscript for CentOS/RHEL6
- added logrotate config for sysvinit systems

* Wed Aug 21 2019 Christopher Engelhard <ce@lcts.de> 2.4.0-5
- fixed rpm macros not being replaced in service/init file

* Tue Aug 20 2019 Christopher Engelhard <ce@lcts.de> 2.4.0-4
- Create iptables chains for sshguard on install

* Fri Jul 19 2019 Christopher Engelhard <ce@lcts.de> 2.4.0-3
- use own service file instead of example

* Tue Jul 16 2019 Christopher Engelhard <ce@lcts.de> 2.4.0-2
- changed SysV initscript handling to match EPEL guidelines
- enable subpackages for RHEL8

* Tue Jul 16 2019 Christopher Engelhard <ce@lcts.de> 2.4.0-1
- updated for 2.4.0

* Tue Jan 08 2019 Christopher Engelhard <ce@lcts.de> 2.3.1-1
- remove upgrade notice for upgrade from v2.2.0-5,
  people should have noticed by now
- update to v2.3.1

* Sun Dec 16 2018 Christopher Engelhard <ce@lcts.de> 2.3.0-1
- update to 2.3.0

* Tue Oct 23 2018 Christopher Engelhard <ce@lcts.de> 2.2.0-8
- allow building for EPEL
- use RPM path macros in config/init files

* Mon Oct 22 2018 Christopher Engelhard <ce@lcts.de> 2.2.0-7
- Change subpackages to weak dependencies
- Make sshguard-iptables depend on iptables-services
  instead of iptables

* Mon Oct 22 2018 Christopher Engelhard <ce@lcts.de> 2.2.0-6
- split off configuration into subpackages, allows autoconfig
  of multiple firewall backends

* Sat Sep 29 2018 Christopher Engelhard <ce@lcts.de> 2.2.0-5
- include upstream patches for issues #100 and #101 instead of my own

* Tue Sep 25 2018 Christopher Engelhard <ce@lcts.de> 2.2.0-4
- add patch to fix upstream Issue #100, firewalld errors

* Sun Sep 23 2018 Christopher Engelhard <ce@lcts.de> 2.2.0-3
- disabled LFS in repo, incompatible with COPR (ce@lcts.de)

* Sun Sep 23 2018 Christopher Engelhard <ce@lcts.de> 2.2.0-2
- new package built with tito

* Thu Sep 13 2018 Christopher Engelhard <ce@lcts.de> - 2.2.0-1
- first release of this package


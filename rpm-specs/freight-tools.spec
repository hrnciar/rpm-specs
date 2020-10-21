%global gittag aa7fe1c1
%global checkout 20151221git%{gittag}

Name: freight-tools 
Version: 0 
Release: 15.%{checkout}%{?dist}
URL: https://github.com/FreightAgent/freight-tools
Source: freight-tools-%{checkout}.tgz
Source1: freight-agent-node.config
Source2: freightctl-tennant.config
Source3: freight-agent.service
Source4: freight-agent.sysconfig
Source5: freightproxy.service
Source6: freightproxy.sysconfig
Source7: freightproxy.config

Patch0: xmlrpc-buildfix.patch

Summary: Build/Control utility for Freight container management system
License: GPLv2
BuildRequires:  gcc
BuildRequires: autoconf, automake, libconfig-devel 
BuildRequires: libpq-devel, sqlite-devel
BuildRequires: xmlrpc-c-devel
BuildRequires: systemd
Requires: dnf, rpm-build, btrfs-progs

%description
freight-tools contains the base tools to create containers for the freight
container management system 

%package agent 
Summary:	Node server component to the freight container management system
Requires:	dnf, sqlite, xmlrpc-c, btrfs-progs
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units

%package proxy
Summary:	Xmlrpc proxy server component to freight
Requires:	dnf, sqlite, xmlrpc-c, btrfs-progs
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units

%description agent
Node server for freight container management system.  A freight node is
responsible for the running of containers in a cluster

%description proxy
Proxy server functions as an xmlrpc front end to freight for external clients

%prep
%setup -q -n freight-tools 

%patch0 -p1

%build
./autogen.sh
%configure
make %{?_smp_mflags}

%install
%make_install
rm -f $RPM_BUILD_ROOT/%{_bindir}/test-int
install -m755 ./scripts/createfreightdb-pg.sh $RPM_BUILD_ROOT/%{_bindir}
install -m755 ./scripts/createfreightdb-sqlite.sh $RPM_BUILD_ROOT/%{_bindir}
install -m755 ./scripts/createtennant-pg.sh $RPM_BUILD_ROOT/%{_bindir}
install -m755 ./scripts/createtennant-sqlite.sh $RPM_BUILD_ROOT/%{_bindir}
mkdir -m755 -p $RPM_BUILD_ROOT/var/lib/freight-agent
mkdir -m775 -p $RPM_BUILD_ROOT/etc/freight-agent
install -m644 %{SOURCE1} $RPM_BUILD_ROOT/etc/freight-agent/freight-agent-node.config
install -m644 %{SOURCE2} $RPM_BUILD_ROOT/etc/freight-agent/config
mkdir -m775 -p $RPM_BUILD_ROOT/etc/sysconfig
mkdir -m775 -p $RPM_BUILD_ROOT/%{_unitdir}
install -m644 %{SOURCE3} $RPM_BUILD_ROOT/%{_unitdir}
install -m644 %{SOURCE4} $RPM_BUILD_ROOT/etc/sysconfig/freight-agent
install -m644 %{SOURCE5} $RPM_BUILD_ROOT/%{_unitdir}
install -m644 %{SOURCE6} $RPM_BUILD_ROOT/etc/sysconfig/freightproxy
install -m644 %{SOURCE7} $RPM_BUILD_ROOT/etc/freight-agent/freightproxy.config

%files
%{_bindir}/freight-builder
%{_bindir}/freightctl
%{_mandir}/man1/freight-builder.1.gz
%{_mandir}/man1/freightctl.1.gz
%{_mandir}/man1/freight-network-config.1.gz
%dir /etc/freight-agent/
%config(noreplace) /etc/freight-agent/config
%license LICENSE
%doc README.md doc/HOWTO.md
%doc examples/*

%files agent
%{_bindir}/freight-agent
%{_bindir}/createfreightdb-pg.sh
%{_bindir}/createfreightdb-sqlite.sh
%{_bindir}/createtennant-pg.sh
%{_bindir}/createtennant-sqlite.sh
%{_unitdir}/freight-agent.service
%{_mandir}/man1/freight-agent.1.gz
%dir /var/lib/freight-agent
%config(noreplace) /etc/freight-agent/freight-agent-node.config
%config(noreplace) /etc/sysconfig/freight-agent


%files proxy
%{_bindir}/freightproxy
%{_mandir}/man1/freightproxy.1.gz
%{_unitdir}/freightproxy.service
%config(noreplace) /etc/sysconfig/freightproxy
%config(noreplace) /etc/freight-agent/freightproxy.config

%post agent
%systemd_post freight-agent.service
/usr/bin/createfreightdb-sqlite.sh /var/lib/freight-agent/fr.db
/usr/bin/createtennant-sqlite.sh /var/lib/freight-agent/fr.db t1 tp tpp f

%preun agent
%systemd_preun freight-agent.service

%postun agent
%systemd_postun_with_restart freight-agent.service

%post proxy 
%systemd_post freightproxy.service

%preun proxy 
%systemd_preun freightproxy.service

%postun proxy 
%systemd_postun_with_restart freightproxy.service


%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-15.20151221gitaa7fe1c1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-14.20151221gitaa7fe1c1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-13.20151221gitaa7fe1c1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-12.20151221gitaa7fe1c1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 24 2018 Adam Williamson <awilliam@redhat.com> - 0-11.20151221gitaa7fe1c1
- Rebuild for new libconfig

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-10.20151221gitaa7fe1c1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-9.20151221gitaa7fe1c1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-8.20151221gitaa7fe1c1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-7.20151221gitaa7fe1c1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-6.20151221gitaa7fe1c1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 25 2017 Neil Horman <nhorman@redhat.com> - 0.5-20151221gitaa7fe1c1
- Fix build break with new xmlrpc

* Sat Jan 21 2017 Igor Gnatenko <ignatenko@redhat.com> - 0-4.20151221gitaa7fe1c1
- Rebuild for xmlrpc-c

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-3.20151221gitaa7fe1c1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Dec 22 2015 - Neil horman <nhorman@tuxdriver.com> - 1.20151221git24dae12b
- Added missing buildrequires for systemd

* Mon Dec 21 2015 - Neil Horman <nhorman@tuxdriver.com> - 0.20151221git24dae12b 
- Initial Build


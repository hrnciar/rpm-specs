%global commit0 1abcec1285585ede73b937b4082828755ee9c61c
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

%if 0%{?rhel} == 6
%global perl_interpreter perl
%else
%global perl_interpreter perl-interpreter
%endif

Name:		clatd
Version:	1.5
Release:	5%{?dist}
Summary:	CLAT / SIIT-DC Edge Relay implementation for Linux

License:	MIT
URL:		https://github.com/toreanderson/clatd
Source0:	https://github.com/toreanderson/%{name}/archive/v%{version}.tar.gz

# Upstream patch 9a1a4ae correcting the license inside the clatd source to 
# match the one in the LICENSE file. Acknowledged by upstream author. 
#Patch1:		clatd-1.4_fix_license_9a1a4ae.patch

# Upstream patches 1abcec1 and 18dca08, with documentation fixes
#Patch2:		clatd-1.4_fix_doc_1abcec1+18dca08.patch

# Upstream patch fb4587b with NetworkManager script fix
#Patch3:		clatd-1.4_fix_nm_script_fb4587b.patch

BuildArch:	noarch
BuildRequires:	%perl_interpreter
BuildRequires:	coreutils
BuildRequires:	%{_bindir}/pod2man

Requires:	iproute
Requires:	iptables
Requires:	tayga
Requires:	%perl_interpreter
Requires:	perl(Net::DNS)
Requires:	perl(IO::Socket::INET6)
Requires:	perl(File::Temp)
Requires:	perl(Net::IP)

%if 0%{?fedora} >= 18 || 0%{?rhel} >=7
Requires(post):		systemd
Requires(preun):	systemd
Requires(postun):	systemd
BuildRequires:		systemd
%endif


%description
clatd implements the CLAT component of the 464XLAT network architecture
specified in RFC 6877. It allows an IPv6-only host to have IPv4
connectivity that is translated to IPv6 before being routed to an upstream
PLAT (which is typically a Stateful NAT64 operated by the ISP) and there
translated back to IPv4 before being routed to the IPv4 internet.


%prep
%setup -q v%{release}.tar.gz
%build
pod2man	--name %{name} \
	--center "clatd - a CLAT implementation for Linux" \
	--section 8 \
	README.pod %{name}.8
gzip %{name}.8
echo '# Default clatd.conf
# See clatd(8) for a list of config directives' > %{name}.conf

sed -i "s,%{_sbindir}/clatd,%{_sbindir}/clatd -c %{_sysconfdir}/%{name}.conf," \
	scripts/*


%install
install -p -D -m0755 %{name} %{buildroot}%{_sbindir}/%{name}
install -p -D -m0644 %{name}.8.gz %{buildroot}%{_mandir}/man8/%{name}.8.gz
install -p -D -m0644 %{name}.conf %{buildroot}%{_sysconfdir}/%{name}.conf
install -p -D -m0755 scripts/%{name}.networkmanager %{buildroot}%{_prefix}/lib/NetworkManager/dispatcher.d/50-%{name}
%if 0%{?fedora} >= 18 || 0%{?rhel} >= 7
install -p -D -m 0644 scripts/%{name}.systemd %{buildroot}%{_unitdir}/%{name}.service
%else
install -p -D -m0644 scripts/%{name}.upstart %{buildroot}%{_sysconfdir}/init/%{name}.conf;
%endif

%post
%if 0%{?fedora} >= 18 || 0%{?rhel} >= 7
%systemd_post %{name}.service
%else
# upstart services do not need any chkconfig to be enabled
%endif


%files
%{_sbindir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_prefix}/lib/NetworkManager
%doc README.pod
%{_mandir}/man8/*.8*
%if 0%{?fedora} >= 22 || 0%{?rhel} >= 7
%license LICENCE
%else
%doc LICENCE
%endif
%if 0%{?fedora} >= 18 || 0%{?rhel} >= 7
%{_unitdir}/%{name}.service
%else
%{_sysconfdir}/init/%{name}.conf
%endif


%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Aug 22 2019 Lubomir Rintel <lkundrak@v3.sk> - 3.5-3
- Move the NetworkManager dispatcher script out of /etc

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 21 2019 Ingvar Hagelund <ingvar@redpill-linpro.com> - 1.5-1
- New upstream release
- Dropped patches included upstream

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Sep 26 2017 Ingvar Hagelund <ingvar@redpill-linpro.com> - 1.4-7
- Set a macro perl-interpreter for backwards compatibility for el6

* Tue Sep 26 2017 Ingvar Hagelund <ingvar@redpill-linpro.com> - 1.4-6
- Readded requirement of Net::IP. By some reason, it is not added
  automatically in mock builds. Closes bz #1494867

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 13 2017 Petr Pisar <ppisar@redhat.com> - 1.4-4
- perl dependency renamed to perl-interpreter
  <https://fedoraproject.org/wiki/Changes/perl_Package_to_Install_Core_Modules>

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jun 28 2016 Ingvar Hagelund <ingvar@redpill-linpro.com> 1.4-2
- Fixes for bz#1302876, including
- Now BuildRequires pod2man
- Requires perl(Net::IP) is autogenerated, so not needed explicit
- clatd.conf is marked as config file
- Packaged 1.4 release tarball, and added changes from upstream as patches

* Tue Feb 23 2016 Ingvar Hagelund <ingvar@redpill-linpro.com> 1.4-1.3.20160128git1abcec1
- Package now (co)owns /etc/NetworkManager/dispatcher.d, and no longer
  requires initscripts (bz #1302876)

* Thu Jan 28 2016 Ingvar Hagelund <ingvar@redpill-linpro.com> 1.4-1.2.20160128git1abcec1
- First wrap for fedora and epel

#
# spec file for package wide-dhcpv6
#

%global ubuntu_release 13
%global my_release 2
%global _hardened_build 1

Name:           wide-dhcpv6
BuildRequires:  gcc
BuildRequires:  bison flex flex-devel systemd
# The entire source code is BSD except the bison parser code which is GPL
License:        BSD and GPLv2+
Summary:        DHCP Client and Server for IPv6
Version:        20080615
Url:            https://launchpad.net/ubuntu/+source/%{name}/%{version}-%{ubuntu_release}
Release:        %{ubuntu_release}.%{my_release}%{dist}
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:        CHANGELOG-LINUX
Source2:        COPYRIGHT
Source3:        dhcp6c-script
Source4:        dhcp6c.service
Source5:        dhcp6r.service
Source6:        dhcp6s.service
Source7:        RELEASENOTES
Source8:        dhcp6c@.service
Patch1:         wide-dhcpv6-0001-Fix-manpages.patch
Patch2:         wide-dhcpv6-0002-Don-t-strip-binaries.patch
Patch3:         wide-dhcpv6-0003-Close-inherited-file-descriptors.patch
Patch4:         wide-dhcpv6-0004-GNU-libc6-fixes.patch
Patch5:         wide-dhcpv6-0005-Update-ifid-on-interface-restart.patch
Patch6:         wide-dhcpv6-0006-Add-new-feature-dhcp6c-profiles.patch
Patch7:         wide-dhcpv6-0007-Adding-ifid-option-to-the-dhcp6c.conf-prefix-interfa.patch
Patch8:         wide-dhcpv6-0008-Make-sla-len-config-optional.patch
Patch9:         wide-dhcpv6-0009-Make-sla-id-config-optional.patch
Patch10:        wide-dhcpv6-0010-move-client-script-to-after-update_ia.patch
Patch11:        wide-dhcpv6-0011-fedora20-cflag.patch
Patch12:	wide-dhcpv6-0012-Fix-renewal-of-IA-NA.patch
Patch13:	wide-dhcpv6-0013-Fix-parallel-make-race-condition.patch
Requires(preun): systemd
Requires(postun): systemd

%description
This is the DHCPv6 package from WIDE project. For more information visit the
project web site at http://wide-dhcpv6.sourceforge.net/

DHCPv6 allows prefix delegation and host configuration for the IPv6 network
protocol.

Multiple network interfaces are supported by this DHCPv6 package.

This package contains the server, relay and client.


%prep
%setup -q 
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1


%build
%configure --sysconfdir=%{_sysconfdir}/%{name} --enable-libdhcp=no
make %{?_smp_mflags}	

%install
mkdir -p %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{_sysconfdir}/%{name}
mkdir -p %{buildroot}%{_mandir}/man{8,5}
mkdir -p %{buildroot}%{_defaultdocdir}/%{name}
mkdir -p %{buildroot}%{_unitdir}
install -p -m 755 dhcp6c dhcp6s dhcp6relay dhcp6ctl %{buildroot}%{_sbindir}
install -p -m 644 dhcp6c.8 dhcp6s.8 dhcp6relay.8 dhcp6ctl.8 %{buildroot}/%{_mandir}/man8
install -p -m 644 dhcp6c.conf.5 dhcp6s.conf.5 %{buildroot}/%{_mandir}/man5
install -p -m 644 %{SOURCE1} %{buildroot}%{_defaultdocdir}/%{name}
install -p -m 644 %{SOURCE2} %{buildroot}%{_defaultdocdir}/%{name}
install -p -m 644 %{SOURCE3} %{buildroot}%{_defaultdocdir}/%{name}
install -p -m 644 %{SOURCE4} %{buildroot}%{_defaultdocdir}/%{name}
install -p -m 644 %{SOURCE5} %{buildroot}%{_defaultdocdir}/%{name}
install -p -m 644 %{SOURCE6} %{buildroot}%{_defaultdocdir}/%{name}
install -p -m 644 %{SOURCE7} %{buildroot}%{_defaultdocdir}/%{name}
install -p -m 644 %{SOURCE8} %{buildroot}%{_unitdir}
install -p -m 644 README CHANGES %{buildroot}%{_defaultdocdir}/%{name}
install -p -m 644 dhcp6c.conf.sample %{buildroot}%{_defaultdocdir}/%{name}
install -p -m 644 dhcp6s.conf.sample %{buildroot}%{_defaultdocdir}/%{name}

%preun
if [ $1 -lt 1 ] ; then
%systemd_preun dhcp6c@.service
fi
%systemd_preun dhcp6c.service
%systemd_preun dhcp6r.service
%systemd_preun dhcp6s.service

%postun
%systemd_postun_with_restart dhcp6c.service
%systemd_postun_with_restart dhcp6r.service
%systemd_postun_with_restart dhcp6s.service

%files
%dir %{_sysconfdir}/%{name}
%{_defaultdocdir}/%{name}/*
%{_sbindir}/*
%{_mandir}/man?/*
%{_unitdir}/*

%changelog
* Fri Aug 14 2020 dave@bevhost.com 20080615-13.2
- Added parameterized systemd unit file for client
- Added more complete usage example to RELEASENOTES

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20080615-13.1.11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20080615-13.1.10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20080615-13.1.9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20080615-13.1.8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20080615-13.1.7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20080615-13.1.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20080615-13.1.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20080615-13.1.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20080615-13.1.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20080615-13.1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20080615-13.1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Feb 7 2015 dave@bevhost.com 20080615-13.1
- Added patch 12 from ubuntu version
- Added patch 13 so we can use parallel make

* Tue Jan 14 2014 dave@bevhost.com 20080615-11.1.5
- Added patch 11 provided by Scott Shambarger
- Documentation directory now has no version number

* Thu May 16 2013 dave@bevhost.com 20080615-11.1.4
- Added patches 8 and 9, which simplify configuration
- Added patch 10 which moves client script execution to after IP addr are added.
- Added RELEASENOTES

* Tue May 7 2013 dave@bevhost.com 20080615-11.1.3
- make the build specific to fedora rawhide 

* Mon May 6 2013 dave@bevhost.com 20080615-11.1.2
- use macros in spec file wherever possible
- add support for systemd

* Wed Apr 24 2013 dave@bevhost.com 20080615-11.1.1
- Move sysconfdir from /etc to /etc/wide-dhcpv6 to match man pages

* Tue Apr 02 2013 dave@bevhost.com
- converted from debian package



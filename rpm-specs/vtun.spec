Name: vtun
Version: 3.0.4
Release: 10%{?dist}
Summary: Virtual tunnel over TCP/IP networks
License: GPLv2+
Url: http://vtun.sourceforge.net
Source0: http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1: vtun.socket
Source2: vtun.service
Source3: vtun.sysconfig
Patch0: vtun-nostrip.patch

Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units
BuildRequires:  gcc
BuildRequires: zlib-devel lzo-devel bison flex systemd-units autoconf
%if 0%{?fedora} >= 26
BuildRequires: compat-openssl10-devel
%else
BuildRequires: openssl-devel
%endif

#enable PIE/PIC:
%global _hardened_build 1

%description
VTun provides a method for creating Virtual Tunnels over TCP/IP networks
and allows one to shape, compress, and encrypt traffic in those tunnels.
Supported types of tunnels are: PPP, IP, Ethernet and most other serial
protocols and programs.
VTun is easily and highly configurable: it can be used for various
network tasks like VPN, Mobile IP, Shaped Internet access, IP address
saving, etc. It is completely a user space implementation and does not
require modification to any kernel parts.

%prep
%setup -q
%patch0 -p1

%build
autoconf
# FIXME: Package suffers from c11/inline issues.
# Workaround by appending --std=gnu89 to CFLAGS
# Proper fix would be to fix the source-code
%configure CFLAGS="${RPM_OPT_FLAGS} --std=gnu89"
make %{?_smp_mflags}

%install
install -D -m 0644 -p %{SOURCE1} %{buildroot}/%{_unitdir}/vtun.socket
install -D -m 0644 -p %{SOURCE2} %{buildroot}/%{_unitdir}/vtun.service
install -D -m 0644 -p %{SOURCE3} %{buildroot}/%{_sysconfdir}/sysconfig/vtun
make install DESTDIR=%{buildroot} INSTALL_OWNER= INSTALL="/usr/bin/install -p"
# tmpfiles.d configuration for /var/lock/vtund:
mkdir -p %{buildroot}/%{_tmpfilesdir}
cat > %{buildroot}/%{_tmpfilesdir}/%{name}.conf << EOT
d %{_localstatedir}/lock/vtund 0755 root root -
EOT

%post
%systemd_post vtun.service vtun.socket

%preun
%systemd_preun vtun.service vtun.socket

%postun
%systemd_postun vtun.service vtun.socket

%files
%doc ChangeLog Credits FAQ README README.LZO README.Setup README.Shaper TODO vtund.conf
%config(noreplace) %{_sysconfdir}/vtund.conf
%config(noreplace) %{_sysconfdir}/sysconfig/vtun
%{_unitdir}/vtun.socket
%{_unitdir}/vtun.service
%{_sbindir}/vtund
%{_tmpfilesdir}/%{name}.conf
%dir %{_localstatedir}/log/vtund
%dir %{_localstatedir}/lock/vtund
%{_mandir}/man5/vtund.conf.5*
%{_mandir}/man8/vtun.8*
%{_mandir}/man8/vtund.8*

%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Sep 02 2017 Gabriel Somlo <somlo at cmu.edu> 3.0.3-5
- remove segfaulting  openssl-1.1 patch; use compat-openssl10 instead

* Sat Sep 02 2017 Gabriel Somlo <somlo at cmu.edu> 3.0.3-4
- apply openssl-1.1 patch only on Fedora >= 26, to avoid epel7 (#1487003)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Mon Jul 31 2017 Gabriel Somlo <somlo at cmu.edu> 3.0.3-2
- add /usr/lib/tmpfiles.d/vtun.conf to enable lock dir. on tmpfs

* Fri Mar 17 2017 Gabriel Somlo <somlo at cmu.edu> 3.0.3-1
- update to 3.0.4
- patch for openssl-1.1 transition

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Mar 21 2016 Gabriel Somlo <somlo at cmu.edu> 3.0.3-15
- patch to fix #1319858,#1319859,#1319861

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jun 22 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.0.3-13
- Append --stdc=gnu89 to CFLAGS (Work-around to c11/inline compatibility
  issues. Fix FTBFS).

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Dec 23 2014 Gabriel Somlo <somlo at cmu.edu> 3.0.3-11
- enhanced service file (remove "KillMode", use default "cgroup" mode)

* Thu Nov 20 2014 Gabriel Somlo <somlo at cmu.edu> 3.0.3-10
- enhanced service file (-n to prevent daemonizing vtund)

* Fri Nov 14 2014 Gabriel Somlo <somlo at cmu.edu> 3.0.3-9
- added /etc/sysconfig/vtun environment file
- updated unit files

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon May 13 2013 Gabriel Somlo <somlo at cmu.edu> 3.0.3-5
- added autoconf step to support aarch64 (#926708)

* Wed May 01 2013 Gabriel Somlo <somlo at cmu.edu> 3.0.3-4
- rebuild with PIE (#955286)

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> 
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Sep 16 2012 Gabriel Somlo <somlo at cmu.edu> 3.0.3-2
- avoid stripping too early to preserve debuginfo (#857716)

* Thu Sep 13 2012 Gabriel Somlo <somlo at cmu.edu> 3.0.3-1
- update to 3.0.3
- new systemd-rpm macros (#850362)

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon May 21 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 3.0.1-14
- Fix unit file location, cleanup and modernise spec

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Sep 10 2011 Gabriel Somlo <somlo at cmu.edu> 3.0.1-12
- removed xinetd and sysvinit support

* Sat Sep 10 2011 Gabriel Somlo <somlo at cmu.edu> 3.0.1-11
- update support for systemd (#737195)

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan 06 2011 Gabriel Somlo <somlo at cmu.edu> 3.0.1-9
- add support for systemd (#661331)

* Tue Nov 30 2010 Gabriel Somlo <somlo at cmu.edu> 3.0.1-8
- using ghost on /var/lock/vtund directory (#656720)

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 3.0.1-7
- rebuilt with new openssl

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Jan 18 2009 Tomas Mraz <tmraz@redhat.com> 3.0.1-4
- rebuild with new openssl

* Mon Nov 17 2008 Gabriel Somlo <somlo at cmu.edu> 3.0.1-3
- scriptlets fixes

* Fri Nov 14 2008 Gabriel Somlo <somlo at cmu.edu> 3.0.1-2
- spec file fixes: defattr, -p flag to install program

* Mon Oct 20 2008 Gabriel Somlo <somlo at cmu.edu> 3.0.1-1
- initial fedora package

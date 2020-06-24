%define _default_patch_fuzz 2
Name: pads
Version: 1.2
Release: 28%{?dist}
Summary: Passive Asset Detection System
License: GPLv2+
URL: http://passive.sourceforge.net/
Source0: http://prdownloads.sourceforge.net/passive/%{name}-%{version}.tar.gz
Source1: pads.service
Source2: pads.sysconfig
Patch1: pads-1.2-cleanup.patch
Patch2: pads-1.2-memleak.patch
Patch3: pads-1.2-overrun.patch
Patch4: pads-1.2-disable-debug.patch
Patch5: pads-1.2-daemonize.patch
Patch6: pads-1.2-ether-codes-update.patch
Patch7: pads-1.2-misc.patch
Patch8: pads-1.2-arp.patch
Patch9: pads-1.2-prelude.patch
Patch10: pads+vlan.patch
Patch11: pads-1.2-prelude-cleanup.patch
Patch12: pads-1.2-readonly.patch
Patch13: pads-1.2-bstring.patch
Patch14: pads-1.2-leak.patch
Patch15: pads-1.2-perf.patch
Patch16: pads-1.2-daemon.patch
Patch17: pads-1.2-pthreads.patch
Patch18: pads-aarch64.patch
Patch19: pads-1.2-inline-cleanup.patch
Patch20: pads-1.2-extra-libs.patch
BuildRequires:  gcc
BuildRequires: automake autoconf
BuildRequires: pcre-devel libpcap-devel
BuildRequires: perl-generators
BuildRequires: systemd
Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units


%description
PADS is a libpcap based detection engine used to passively 
detect network assets.

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
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1

%build
autoreconf -fv --install
%configure 
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_sysconfdir}/sysconfig
make install DESTDIR=%{buildroot}
install -m 644 %SOURCE1 %{buildroot}%{_unitdir}/pads.service
install -m 640 %SOURCE2 %{buildroot}%{_sysconfdir}/sysconfig/%{name}
# Remove installed docs since we pick this up another way
rm -rf $RPM_BUILD_ROOT/usr/share/pads/

%post
%systemd_post auditd.service

%preun
%systemd_preun auditd.service

%postun
%systemd_postun_with_restart pads.service

%files
%doc doc/AUTHORS doc/COPYING doc/README doc/ChangeLog
%{_sysconfdir}/pads-ether-codes
%{_sysconfdir}/pads-signature-list
%config(noreplace) %attr(0640,root,root) %{_sysconfdir}/pads.conf
%config(noreplace) %attr(0640,root,root) %{_sysconfdir}/sysconfig/%{name}
%{_unitdir}/pads.service
%{_bindir}/pads
%{_bindir}/pads-report
%{_mandir}/*/*

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Sep 21 2017 Steve Grubb <sgrubb@redhat.com> 1.2-23
- Add systemd macros. (#850262)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Aug 17 2015 Steve Grubb <sgrubb@redhat.com> 1.2-18
- Fix bad inline keyword use (#1239755)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1.2-13
- Perl 5.18 rebuild

* Fri Jun 21 2013 Steve Grubb <sgrubb@redhat.com> 1.2-12
- Drop prelude support

* Sun Jun 02 2013 Steve Grubb <sgrubb@redhat.com> 1.2-11
- Support Aarch64 (#926298)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Feb 20 2012 Jon Ciesla <limburgher@gmail.com> - 1.2-8
- Migrate to systemd, BZ 661632.

* Fri Feb 10 2012 Petr Pisar <ppisar@redhat.com> - 1.2-7
- Rebuild against PCRE 8.30

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Oct 28 2008 Steve Grubb <sgrubb@redhat.com> 1.2-2
- Update CFLAGS for newer libprelude (#465964)

* Tue Aug 12 2008 Steve Grubb <sgrubb@redhat.com> 1.2-1
 Initial rpm build with many bug fixes

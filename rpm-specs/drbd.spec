Name: drbd
Summary: DRBD user-land tools and scripts
Version: 9.13.1
Release: 3%{?dist}
Source0: http://www.linbit.com/downloads/%{name}/utils/%{name}-utils-%{version}.tar.gz
Source1: drbd.service
Source2: drbd.ocf
Patch0: drbd-utils-9.12.2-disable_xsltproc_network_read.patch
Patch1: drbd-utils-9.12.2-v84_setup_option.patch
License: GPLv2+
ExclusiveOS: linux
URL: http://www.drbd.org/
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: flex
BuildRequires: libxslt
BuildRequires: docbook-style-xsl
BuildRequires: perl-generators
BuildRequires: po4a
Requires: %{name}-utils = %{version}
Requires: %{name}-udev = %{version}
BuildRequires: udev

%description
DRBD refers to block devices designed as a building block to form high
availability (HA) clusters. This is done by mirroring a whole block device
via an assigned network. DRBD can be understood as network based raid-1.

This is a virtual package, installing the full user-land suite.

%files
%doc COPYING
%doc ChangeLog


%prep
%setup -q -n drbd-utils-%{version}

# Don't let xsltproc make network calls during build
%patch0 -p1
%patch1 -p1

%build
%configure \
    --with-utils \
    --without-km \
    --with-udev \
%ifarch %{ix86} x86_64
    --with-xen \
%else
    --without-xen \
%endif
    --with-pacemaker \
    --with-rgmanager \
    --with-distro=generic \
    --with-initdir=%{_initddir}
#make %{?_smp_mflags}
%{make_build}

%install
rm -rf $RPM_BUILD_ROOT
#make install DESTDIR=$RPM_BUILD_ROOT
%{make_install}

# Remove old init script, replace with systemd unit file
rm -f $RPM_BUILD_ROOT/%{_initddir}/drbd
install -d -m755 $RPM_BUILD_ROOT/%{_unitdir}
install -m644 %{SOURCE1} $RPM_BUILD_ROOT/%{_unitdir}/drbd.service
rm -f $RPM_BUILD_ROOT/drbd.service

# Remove old heartbeat files that aren't needed any longer in Fedora
rm -rf $RPM_BUILD_ROOT/etc/ha.d

# RHBZ 1253056: Fix pacemaker integration problem
install -m 755 %{SOURCE2} $RPM_BUILD_ROOT/usr/lib/ocf/resource.d/linbit/drbd

%package utils
Summary: Management utilities for DRBD

%description utils
DRBD mirrors a block device over the network to another machine.
Think of it as networked raid 1. It is a building block for
setting up high availability (HA) clusters.

This packages includes the DRBD administration tools.

%files utils
%defattr(755,root,root,-)
%{_sbindir}/drbdsetup
%{_sbindir}/drbdadm
%{_sbindir}/drbdmeta
%{_sbindir}/drbdmon

# systemd-related stuff
%attr(0644,root,root) %{_unitdir}/drbd.service
%{_tmpfilesdir}/%{name}.conf

# Yes, these paths are peculiar. Upstream is peculiar.
# Be forewarned: rpmlint hates this stuff.
%defattr(755,root,root,-)
/lib/drbd/drbd
/lib/drbd/drbdadm-*
/lib/drbd/drbdsetup-*
/usr/lib/drbd/*.sh
/usr/lib/drbd/rhcs_fence

%defattr(-,root,root,-)
%dir %{_var}/lib/%{name}
%config(noreplace) %{_sysconfdir}/drbd.conf
%dir %{_sysconfdir}/drbd.d
%config(noreplace) %{_sysconfdir}/drbd.d/global_common.conf
%{_mandir}/man8/drbd*gz
%{_mandir}/man5/drbd*gz
%{_mandir}/ja/man5/drbd*gz
%{_mandir}/ja/man8/drbd*gz
%doc scripts/drbd.conf.example
%license COPYING
%doc ChangeLog


# armv7hl/aarch64 doesn't have Xen packages
%ifarch %{ix86} x86_64
%package xen
Summary: Xen block device management script for DRBD
Requires: %{name}-utils = %{version}-%{release}

%description xen
This package contains a Xen block device helper script for DRBD, capable of
promoting and demoting DRBD resources as necessary.

%files xen
%defattr(755,root,root,-)
%{_sysconfdir}/xen/scripts/block-drbd
%endif


%package udev
Summary: udev integration scripts for DRBD
Requires: %{name}-utils = %{version}-%{release}, udev

%description udev
This package contains udev helper scripts for DRBD, managing symlinks to
DRBD devices in /dev/drbd/by-res and /dev/drbd/by-disk.

%files udev
%{_udevrulesdir}/65-drbd.rules


%package pacemaker
Summary: Pacemaker resource agent for DRBD
Requires: %{name}-utils = %{version}-%{release}
Requires: pacemaker
License: GPLv2

%description pacemaker
This package contains the master/slave DRBD resource agent for the
Pacemaker High Availability cluster manager.

%files pacemaker
%defattr(755,root,root,-)
%{_prefix}/lib/ocf/resource.d/linbit/drbd
%{_prefix}/lib/ocf/resource.d/linbit/drbd.shellfuncs.sh
%{_mandir}/man7/ocf_linbit_drbd*gz


%package rgmanager
Summary: Red Hat Cluster Suite agent for DRBD
Requires: %{name}-utils = %{version}-%{release}
Conflicts: resource-agents >= 3

%description rgmanager
This package contains the DRBD resource agent for the Red Hat Cluster Suite
resource manager.

As of Red Hat Cluster Suite 3.0.1, the DRBD resource agent is included
in the Cluster distribution.

%files rgmanager
%defattr(755,root,root,-)
%{_datadir}/cluster/drbd.sh

%defattr(-,root,root,-)
%{_datadir}/cluster/drbd.metadata


%package bash-completion
Summary: Programmable bash completion support for drbdadm
Requires: %{name}-utils = %{version}-%{release}

%description bash-completion
This package contains programmable bash completion support for the drbdadm
management utility.

%files bash-completion
%config %{_sysconfdir}/bash_completion.d/drbdadm*


%post utils
%systemd_post drbd.service

%preun utils
%systemd_preun drbd.service

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 9.13.1-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 9.13.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 17 2020 Peter Hanecak <hany@hany.sk> - 9.13.1-1
- Upstream release of 9.13.1

* Wed Apr 29 2020 Peter Hanecak <hany@hany.sk> - 9.12.2-1
- Upstream release of 9.12.2
- Small spec tweaks
- Updated xsltproc network read patch
- Added patch for setup_option in v84
- Build now requires also po4a

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 9.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 9.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 9.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 19 2018 Major Hayden <major@mhtx.net> - 9.5.0-1
- Upstream release of 9.5.0

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8.9.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8.9.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8.9.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8.9.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8.9.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Mar 07 2016 Major Hayden <major@mhtx.net> - 8.9.6-2
- Fix RHBZ 1314970

* Fri Feb 05 2016 Major Hayden <major@mhtx.net> - 8.9.6-1
- Upstream release of 8.9.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 8.9.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Dec 23 2015 Major Hayden <major@mhtx.net> - 8.9.5-1
- Upstream release of 8.9.5

* Mon Sep 21 2015 Major Hayden <major@mhtx.net> - 8.9.4-1
- Upstream release of 8.9.4

* Thu Aug 13 2015 Major Hayden <major@mhtx.net> - 8.9.3-2
- Fix RHBZ 1253056

* Tue Jun 16 2015 Major Hayden <major@mhtx.net> - 8.9.3-1
- New upstream release 8.9.3.

* Tue May 12 2015 Major Hayden <major@mhtx.net> - 8.9.2-3
- Lots of spec/patch fixes

* Tue May 12 2015 Major Hayden <major@mhtx.net> - 8.9.2-2
- Updated global_common.conf patch

* Tue May 12 2015 Major Hayden <major@mhtx.net> - 8.9.2-1
- New upstream release 8.9.2.

* Wed Jan 07 2015 Major Hayden <major@mhtx.net> - 8.9.1-2
- Removed xen dependency for drbd-xen

* Thu Dec 04 2014 Major Hayden <major@mhtx.net> - 8.9.1-1
- New upstream release 8.9.1.

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.9.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Aug 08 2014 Major Hayden <major@mhtx.net> - 8.9.0-7
- Don't write Xen scripts on arm systems

* Fri Aug 08 2014 Major Hayden <major@mhtx.net> - 8.9.0-6
- Don't assemble xen package on armv7hl/aarch64 systems

* Thu Aug 07 2014 Major Hayden <major@mhtx.net> - 8.9.0-5
- Removing unneeded rgmanager dependency

* Wed Aug 06 2014 Major Hayden <major@mhtx.net> - 8.9.0-4
- Big cleanup and update for F21

* Mon Aug 04 2014 Major Hayden <major@mhtx.net> - 8.9.0-3
- Fixing path to drbdadm in systemd unit file

* Mon Aug 04 2014 Major Hayden <major@mhtx.net> - 8.9.0-2
- Added systemd unit file for drbd

* Fri Jul 25 2014 Major Hayden <major@mhtx.net> - 8.9.0-1
- New upstream release 8.9.0.  DRBD utilities are now split from the kernel modules.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Mar 31 2014 Major Hayden <major@mhtx.net> - 8.4.4-1
- New upstream release 8.4.4.

* Sat Aug 03 2013 Petr Pisar <ppisar@redhat.com> - 8.4.3-2
- Perl 5.18 rebuild

* Wed Jul 31 2013 Major Hayden <major@mhtx.net> - 8.4.3-1
- New upstream release.

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 8.4.2-4
- Perl 5.18 rebuild

* Thu Jun 20 2013 Major Hayden <major@mhtx.net> - 8.4.2-3
- Removed heartbeat package
- Corrected Source0 URL

* Mon Mar 11 2013 Karsten Hopp <karsten@redhat.com> 8.4.2-2
- work around macro expansion problems on PPC64

* Thu Mar 07 2013 Major Hayden <major@mhtx.net> - 8.4.2-1
- Version bump to match F18 kernel modules

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.3.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Nov 04 2012 Major Hayden <major@mhtx.net> - 8.3.13-1
- Version bump to match F17/F18 kernel modules

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.3.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Apr 01 2012 Major Hayden <major@mhtx.net> - 8.3.11-5
- Removed bash completion dependency (#807633)

* Mon Feb 20 2012 Major Hayden <major@mhtx.net> - 8.3.11-4
- Removed heartbeat, pacemaker, and rgmanager requirements in main drbd package.

* Tue Feb 14 2012 Oliver Falk <oliver@linux-kernel.at> - 8.3.11-3
- Don't require xen in the main package if built with xen

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.3.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Aug 03 2011 Major Hayden <major@mhtx.net> - 8.3.11-1
- New upstream release.

* Mon Mar 14 2011 Major Hayden <major@mhtx.net> - 8.3.9-1
- New upstream release.
- Matches DRBD modules in 2.6.38 for Fedora 15.

* Tue Mar 01 2011 Major Hayden <major@mhtx.net> - 8.3.8.1-1
- New upstream release.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.3.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

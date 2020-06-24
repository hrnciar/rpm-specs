%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}
%{!?with_check: %global with_check 1}

%global		package_version 0.5.16
%global		package_name mom

%if 0%{?fedora} >= 30 || 0%{?rhel} >= 8
%global     python_interpreter /usr/bin/python3
%global     python_target_version python3
%global     python_sitelib %{python3_sitelib}
%else
%global     python_interpreter /usr/bin/python2
%global     python_target_version python2
%global     python_sitelib %{python2_sitelib}
%endif

Name:		%{package_name}
Version:	0.5.16
Release:	4%{?dist}
Summary:	Dynamically manage system resources on virtualization hosts

License:	GPLv2
URL:		http://www.ovirt.org
Source:		https://resources.ovirt.org/pub/src/%{name}/%{package_name}-%{package_version}.tar.gz
BuildArch:	noarch

# Fix build with Python 3.9
# From the upstream PR: https://gerrit.ovirt.org/#/c/108074/
Patch0:         fix-py39-build.patch

BuildRequires:	%{python_target_version}-devel
BuildRequires:	%{python_target_version}-nose
BuildRequires:	%{python_target_version}-mock

Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
BuildRequires: systemd

# MOM makes use of libvirt by way of the python bindings to monitor and
# interact with virtual machines.
Requires:	libvirt-daemon-driver-qemu
%if 0%{?fedora} >= 30 || 0%{?rhel} >= 8
Requires:	%{python_target_version}-libvirt
Requires:	%{python_target_version}-six
%else
Requires:	libvirt-python
Requires:	python-six
%endif
Requires:	procps


%description
MOM is a policy-driven tool that can be used to manage overcommitment on KVM
hosts. Using libvirt, MOM keeps track of active virtual machines on a host. At
a regular collection interval, data is gathered about the host and guests. Data
can come from multiple sources (eg. the /proc interface, libvirt API calls, a
client program connected to a guest, etc). Once collected, the data is
organized for use by the policy evaluation engine. When started, MOM accepts a
user-supplied overcommitment policy. This policy is regularly evaluated using
the latest collected data. In response to certain conditions, the policy may
trigger reconfiguration of the system’s overcommitment mechanisms. Currently
MOM supports control of memory ballooning and KSM but the architecture is
designed to accommodate new mechanisms such as cgroups.

%prep
%setup -q -n %{package_name}-%{package_version}

%patch0 -p1

%build
%configure \
        PYTHON="%{python_interpreter}" \
        --docdir="%{_pkgdocdir}"
make %{?_smp_mflags}

%install
make DESTDIR="%{buildroot}" install

install -dm 755 %{buildroot}%{_unitdir}
install contrib/momd.service %{buildroot}%{_unitdir}
install -d -m 0755 "%{buildroot}/%{_sysconfdir}"
install -m 0644 doc/mom-balloon+ksm.conf "%{buildroot}/%{_sysconfdir}/momd.conf"

%check
%if 0%{with_check}
make check %{?_smp_mflags}
%endif

%post
%systemd_post momd.service

%preun
%systemd_preun momd.service

%postun
%systemd_postun_with_restart momd.service

%files
%config(noreplace) %{_sysconfdir}/momd.conf
%license COPYING
%doc README

%dir %{_pkgdocdir}/examples
%{_pkgdocdir}/examples/*
# COPYING is handled by license macro, avoid to ship duplicates
%exclude %{_pkgdocdir}/COPYING

%{_unitdir}/momd.service
%{_sbindir}/momd
%{python_sitelib}/mom/

%changelog
* Wed Jun 03 2020 Charalampos Stratakis <cstratak@redhat.com> - 0.5.16-4
- Fix build with Python 3.9 (#1813907)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.5.16-3
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Sep 04 2019 Sandro Bonazzola <sbonazzo@redhat.com> - 0.5.16-1
- Rebase on upstream 0.5.16

* Wed Aug 21 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.15-2
- Rebuilt for Python 3.8

* Tue Aug 20 2019 Sandro Bonazzola <sbonazzo@redhat.com> - 0.5.15-1
- Rebase on upstream 0.5.15

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.13-3
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 02 2019 Sandro Bonazzola <sbonazzo@redhat.com> - 0.5.13-1
- Rebase on upstream 0.5.13

* Fri Jun 14 2019 Sandro Bonazzola <sbonazzo@redhat.com> - 0.5.12-1
- Rebase on upstream 0.5.12

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Feb 20 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.5.6-5
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Sep 07 2016 Martin Sivak <msivak@redhat.com> - 0.5.6-1
- Apply IO QoS even when no QoS exists yet
  Resolves: rhbz#1346754

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.5-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Jun 27 2016 Martin Sivak <msivak@redhat.com> - 0.5.5-1
- Improve message when a VM disappears
  Resolves: rhbz#1234953
- Add GuestIoTuneOptional collector
  Resolves: rhbz#1346252

* Wed Jun  1 2016 Martin Sivak <msivak@redhat.com> - 0.5.4-1
- Rebase to the latest version
- Use i8 XML-RPC extension for transfering big numbers
  Resolves: rhbz#1294833
- Fix the momd.service file syntax
  Resolves: rhbz#1263983
- Add IO limit support
- Add GuestBalloonOptional collector
  Resolves: rhbz#1337834

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Sep 17 2015 Martin Sivak <msivak@redhat.com> - 0.5.1-3
- Final doc dir packaging fix

* Thu Sep 17 2015 Martin Sivak <msivak@redhat.com> - 0.5.1-2
- Fix docdir packaging

* Thu Sep 17 2015 Martin Sivak <msivak@redhat.com> - 0.5.1-1
- Fix vdsmxmlrpc hypervisor interface when no ballooning
  information is present.
  Resolves: rhbz#1264095

* Mon Jul 13 2015 Martin Sivak <msivak@redhat.com> - 0.5.0-1
- Upgrade to 0.5.0

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 11 2015 Martin Sivak <msivak@redhat.com> - 0.4.5-2
- Fix systemd dependencies for install scripts

* Thu Jun 11 2015 Martin Sivak <msivak@redhat.com> - 0.4.5-1
- Upgrade to 0.4.5

* Fri May 15 2015 Adam Litke <alitke@redhat.com> - 0.4.4-1
- Upgrade to 0.4.4

* Wed Nov 26 2014 Adam Litke <alitke@redhat.com> - 0.4.3-1
- Upgrade to 0.4.3

* Thu Sep 11 2014 Adam Litke <alitke@redhat.com> - 0.4.2-1
- Upgrade to 0.4.2

* Wed Jun 18 2014 Adam Litke <alitke@redhat.com> - 0.4.1-1
- Upgrade to 0.4.1

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Jan 31 2014 Adam Litke <alitke@redhat.com> - 0.4.0-1
- Upgrade to 0.4.0 and update build process

* Fri Jan 10 2014 Adam Litke <alitke@redhat.com> - 0.3.2-8
- Sync Fedora spec file with package spec file

* Wed Dec 11 2013 Ville Skyttä <ville.skytta@iki.fi> - 0.3.2-7
- Install docs to %%{_pkgdocdir} where available (#993977).

* Thu Nov 21 2013 Adam Litke <alitke@redhat.com> 0.3.2-6
- Bump version and rebuild

* Thu Aug 22 2013 Adam Litke <agl@us.ibm.com> 0.3.2-5
- Added patch to fix error in reporting CPU usage

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 30 2013 Adam Litke <agl@us.ibm.com> - 0.3.2-3
- Fix a typo in the HostMemory Collector
- Convert strings to int when using the vdsm API

* Thu Jul 18 2013 Adam Litke <agl@us.ibm.com> - 0.3.2-2
- Pushed an additional patch for oVirt policy

* Tue Jul 16 2013 Adam Litke <agl@us.ibm.com> - 0.3.2-1
- Upgrade to version 0.3.2
- Policy updates to support oVirt

* Mon Jul 8 2013 Adam Litke <agl@us.ibm.com> - 0.3.1-1
- Upgrade to version 0.3.1
- MOM now uses an autotools build process
- Multiple policy support

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Oct 05 2012 Adam Litke <agl@us.ibm.com> - 0.3.0-1
- Upgrade to version 0.3.0
- Upstream fixes CVE-2012-4480

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jan 12 2011 Adam Litke <agl@us.ibm.com> - 0.2.2-1
- Upgrade to version 0.2.2
- Packaging related changes merged upstream so patches dropped

* Fri Jan 7 2011 Adam Litke <agl@us.ibm.com> - 0.2.1-5
- Address review comments by Michael Schwendt
- Fix use of _defaultdocdir macro
- Add some comments to the spec file

* Tue Oct 26 2010 Adam Litke <agl@us.ibm.com> - 0.2.1-4
- Third round of package review comments
- Remove useless shebang on non-executable python script

* Tue Oct 26 2010 Adam Litke <agl@us.ibm.com> - 0.2.1-3
- Second round of package review comments
- Add a default config file: /etc/momd.conf

* Wed Oct 13 2010 Adam Litke <agl@us.ibm.com> - 0.2.1-2
- Address initial package review comments

* Mon Sep 27 2010 Adam Litke <agl@us.ibm.com> - 0.2.1-1
- Initial package

%global project skiboot

Name:		opal-prd
Version:	6.6.1
Release:	1%{?dist}
Summary:	OPAL Processor Recovery Diagnostics Daemon

License:	ASL 2.0
URL:		http://github.com/open-power/skiboot

# Presently opal-prd is supported on ppc64le architecture only.
ExclusiveArch:	ppc64le

BuildRequires:	systemd
BuildRequires:	gcc
%if 0%{?fedora}
BuildRequires:	gcc-powerpc64-linux-gnu
%endif
BuildRequires:	openssl-devel

Requires(post):		systemd
Requires(preun):	systemd
Requires(postun):	systemd

Source0: https://github.com/open-power/%{project}/archive/v%{version}/%{project}-%{version}.tar.gz
Source1: opal-prd-rsyslog
Source2: opal-prd-logrotate


%description
This package provides a daemon to load and run the OpenPower firmware's
Processor Recovery Diagnostics binary. This is responsible for run time
maintenance of OpenPower Systems hardware.


%package -n	opal-utils
Summary:	OPAL firmware utilities

%description -n opal-utils
This package contains utility programs.

The 'gard' utility, can read, parse and clear hardware gard partitions
on OpenPower platforms. The 'getscom' and 'putscom' utilities provide
an interface to query or modify the registers of the different chipsets
of an OpenPower system. 'pflash' is a tool to access the flash modules
on such systems and update the OpenPower firmware.

%package -n	opal-firmware
Summary:	OPAL firmware
BuildArch:	noarch

%description -n	opal-firmware
OPAL firmware, aka skiboot, loads the bootloader and provides runtime
services to the OS (Linux) on IBM Power and OpenPower systems.


%prep
%setup -q -n %{project}-%{version}


%build
OPAL_PRD_VERSION=%{version} make V=1 CC="gcc" CFLAGS="%{build_cflags}" LDFLAGS="%{build_ldflags}" ASFLAGS="-m64 -Wa,--generate-missing-build-notes=yes" -C external/opal-prd
GARD_VERSION=%{version} make V=1 CC="gcc" CFLAGS="%{build_cflags}" LDFLAGS="%{build_ldflags}" -C external/gard
PFLASH_VERSION=%{version} make V=1 CC="gcc" CFLAGS="%{build_cflags}" LDFLAGS="%{build_ldflags}" -C external/pflash
XSCOM_VERSION=%{version} make V=1 CC="gcc" CFLAGS="%{build_cflags}" LDFLAGS="%{build_ldflags}" -C external/xscom-utils

# build skiboot with a cross-compiler on Fedora and with system compiler otherwise
# and always use upstream compiler flags for the firmware (no CFLAGS override)
%if 0%{?fedora}
SKIBOOT_VERSION=%{version} make V=1 CROSS="powerpc64-linux-gnu-"
%else
SKIBOOT_VERSION=%{version} make V=1 CROSS=
%endif


%install
make -C external/opal-prd install DESTDIR=%{buildroot} prefix=/usr
make -C external/gard install DESTDIR=%{buildroot} prefix=/usr
make -C external/pflash install DESTDIR=%{buildroot} prefix=/usr
make -C external/xscom-utils install DESTDIR=%{buildroot} prefix=/usr

mkdir -p %{buildroot}%{_unitdir}
install -m 644 -p external/opal-prd/opal-prd.service %{buildroot}%{_unitdir}/opal-prd.service

mkdir -p %{buildroot}%{_datadir}/qemu
install -m 644 -p skiboot.lid %{buildroot}%{_datadir}/qemu/skiboot.lid
install -m 644 -p skiboot.lid.xz %{buildroot}%{_datadir}/qemu/skiboot.lid.xz

# log opal-prd messages to /var/log/opal-prd.log
mkdir -p %{buildroot}%{_sysconfdir}/{rsyslog.d,logrotate.d}
install -m 644 %{SOURCE1} %{buildroot}/%{_sysconfdir}/rsyslog.d/opal-prd.conf
install -m 644 %{SOURCE2} %{buildroot}/%{_sysconfdir}/logrotate.d/opal-prd


%post
%systemd_post opal-prd.service

%preun
%systemd_preun opal-prd.service

%postun
%systemd_postun_with_restart opal-prd.service


%files
%doc README.md
%license LICENCE
%config(noreplace) %{_sysconfdir}/logrotate.d/opal-prd
%config(noreplace) %{_sysconfdir}/rsyslog.d/opal-prd.conf
%{_sbindir}/opal-prd
%{_unitdir}/opal-prd.service
%{_mandir}/man8/*

%files -n opal-utils
%doc README.md
%license LICENCE
%{_sbindir}/opal-gard
%{_sbindir}/getscom
%{_sbindir}/putscom
%{_sbindir}/pflash
%{_sbindir}/getsram
%{_mandir}/man1/*

%files -n opal-firmware
%doc README.md
%license LICENCE
%{_datadir}/qemu/


%changelog
* Tue Jun 09 2020 Dan Horák <dan@danny.cz> - 6.6.1-1
- update to 6.6.1

* Thu Apr 23 2020 Dan Horák <dan@danny.cz> - 6.6-1
- update to 6.6

* Fri Mar 20 2020 Dan Horák <dan@danny.cz> - 6.5.4-1
- update to 6.5.4

* Wed Mar 11 2020 Dan Horák <dan@danny.cz> - 6.5.3-1
- update to 6.5.3

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 12 2019 Dan Horák <dan@danny.cz> - 6.5.2-1
- update to 6.5.2

* Thu Oct 24 2019 Dan Horák <dan@danny.cz> - 6.5.1-1
- update to 6.5.1

* Mon Aug 19 2019 Dan Horák <dan@danny.cz> - 6.5-1
- update to 6.5

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 16 2019 Dan Horák <dan@danny.cz> - 6.4-1
- update to 6.4

* Fri May 24 2019 Than Ngo <than@redhat.com> - 6.3.1-1
- update to 6.3.1
- log messages to /var/log/opal-prd.log

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec 20 2018 Than Ngo <than@redhat.com> - 6.2-2
- add man pages

* Thu Dec 20 2018 Than Ngo <than@redhat.com> - 6.2-1
- update to 6.2

* Thu Sep 27 2018 Than Ngo <than@redhat.com> - 6.1-4
- log opal-prd messages to /var/log/opal-prd.log

* Fri Sep 21 2018 Than Ngo <than@redhat.com> - 6.1-3
- Fixed opal-prd crash
- Fixed annocheck distro flag failures

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jul 12 2018 Dan Horák <dan@danny.cz> - 6.1-1
- Update to latest upstream 6.1

* Mon May 28 2018 Dan Horák <dan@danny.cz> - 6.0.4-1
- Update to latest upstream 6.0.4

* Thu May 17 2018 Dan Horák <dan@danny.cz> - 6.0.1-1
- Update to latest upstream 6.0.1

* Mon Apr 09 2018 Dan Horák <dan@danny.cz> - 5.11-1
- Update to latest upstream 5.11

* Mon Mar 12 2018 Than Ngo <than@redhat.com> - 5.10.2-1
- update to latest upstream 5.10.2

* Thu Mar 08 2018 Than Ngo <than@redhat.com> - 5.10.1-2
- fixed bz#1552650 - incomplete Fedora build flags injection

* Fri Mar 02 2018 Dan Horák <dan[at]danny.cz> - 5.10.1-1
- Update to latest upstream 5.10.1

* Wed Feb 28 2018 Dan Horák <dan[at]danny.cz> - 5.10-1
- Update to latest upstream 5.10

* Mon Feb 26 2018 Dan Horák <dan[at]danny.cz> - 5.9.8-3
- fix firmware build (#1545784)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.9.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 25 2018 Dan Horák <dan[at]danny.cz> - 5.9.8-1
- Update to latest upstream 5.9.8

* Fri Aug 4 2017 Vasant Hegde <hegdevasant@linux.vnet.ibm.com> - 5.7.0-1
- Update to latest upstream 5.7.0

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Apr 19 2017 Vasant Hegde <hegdevasant@linux.vnet.ibm.com> - 5.5.0-2
- Fix build warning
- Include skiboot.lid.xz file

* Tue Apr 18 2017 Vasant Hegde <hegdevasant@linux.vnet.ibm.com> - 5.5.0-1
- Update to latest upstream 5.5.0

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Mar 21 2016 Vasant Hegde <hegdevasant@linux.vnet.ibm.com> - 5.2.0
- Update to latest upstream 5.2.0

* Fri Feb 26 2016 Vasant Hegde <hegdevasant@linux.vnet.ibm.com> - 5.1.13-4
- Fix stack frame compilation issue on gcc6
- Remove ppc64 from ExclusiveArch list

* Mon Feb 22 2016 Vasant Hegde <hegdevasant@linux.vnet.ibm.com> - 5.1.13-3
- Fix opal-prd recompilation issse during install

* Mon Feb 22 2016 Vasant Hegde <hegdevasant@linux.vnet.ibm.com> - 5.1.13-2
- Added "Requires(post|preun|postun) tags"

* Tue Feb 09 2016 Vasant Hegde <hegdevasant@linux.vnet.ibm.com> - 5.1.13
- Update to latest upstream 5.1.13
- Fixed specfile based on Dan's review comment (#1284527)

* Wed Nov 25 2015 Vasant Hegde <hegdevasant@linux.vnet.ibm.com> - 5.1.11-4
- Fixed specfile based on Dan's review comment (#1284527)

* Tue Nov 24 2015 Vasant Hegde <hegdevasant@linux.vnet.ibm.com> - 5.1.11-3
- Consistent use of build macros
- Removed defattr from files section

* Tue Nov 24 2015 Vasant Hegde <hegdevasant@linux.vnet.ibm.com> - 5.1.11-2
- Minor update to spec file

* Mon Nov 23 2015 Vasant Hegde <hegdevasant@linux.vnet.ibm.com> - 5.1.11
- Initial Fedora packaging

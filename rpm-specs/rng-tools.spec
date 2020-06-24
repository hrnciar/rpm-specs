%global _hardened_build 1
%global _sbindir /sbin

Summary:        Random number generator related utilities
Name:           rng-tools
Version:        6.10
Release:        3%{?dist}
License:        GPLv2+
URL:            https://github.com/nhorman/rng-tools
Source0:        https://github.com/nhorman/rng-tools/archive/rng-tools-%{version}.tar.gz
Source1:        rngd.service

# https://sourceforge.net/p/gkernel/patches/111/

BuildRequires: gcc make
BuildRequires:  gettext
BuildRequires:  systemd-units
BuildRequires: libgcrypt-devel
BuildRequires: autoconf automake
BuildRequires: libsysfs-devel libcurl-devel
BuildRequires: libxml2-devel openssl-devel
BuildRequires: jitterentropy-devel
BuildRequires: libp11-devel
BuildRequires: jansson-devel
BuildRequires: rtl-sdr-devel

Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units
Provides: jitterentropy-rngd

%description
Hardware random number generation tools.

%prep 
%autosetup 

%build
./autogen.sh
%configure
%make_build

%install
%make_install

# install systemd unit file
install -Dt %{buildroot}%{_unitdir} -m0644 %{SOURCE1}

%post
%systemd_post rngd.service

%preun
%systemd_preun rngd.service

%postun
%systemd_postun_with_restart rngd.service

%files
%{!?_licensedir:%global license %%doc}
%license COPYING
%doc AUTHORS NEWS README
%{_bindir}/rngtest
%{_sbindir}/rngd
%{_mandir}/man1/rngtest.1.*
%{_mandir}/man8/rngd.8.*
%attr(0644,root,root)   %{_unitdir}/rngd.service

%changelog
* Fri Mar 27 2020 Neil Horman <nhorman@redhat.com> - 6.10-3
- Fix missing buildrequires

* Fri Mar 27 2020 Neil Horman <nhorman@redhat.com> - 6.10-2
- Fix missing buildrequires

* Fri Mar 27 2020 Neil Horman <nhorman@redhat.com> - 6.10-1
- Update to latest upstream

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 13 2020 Neil Horman <nhorman@redhat.com> - 6.9-2
- Correct default pkcs11 path on 32 bit arch (bz 1788083)

* Tue Dec 17 2019 Neil Horman <nhorman@redhat.com> - 6.9-1
- update to latest upstream

* Mon Aug 05 2019 Volker Froehlich <volker27@gmx.at> - 6.7-4
- Remove explicit Requires for libraries

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 24 2019 Neil Horman <nhorman@redhat.com> -6.7-2
- Fix race in shutdown leading to hang (bz 1690364)
- bump version number

* Thu Feb 14 2019 Neil Horman <nhorman@redhat.com> - 6.7-1
- Update to latest upstream

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 01 2018 Neil Horman <nhorman@redhat.com> - 6.3.1-2
- Add Provides for jitterentropy-rngd (bz 1634788)

* Mon Jul 16 2018 Neil Horman <nhorman@redhat.com> - 6.3.1-1
- Update to latest upstream

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jul 06 2018 Neil Horman <nhorman@redhat.com> - 6.3-1
- update to latest upstream (#1598608)

* Thu May 10 2018 Neil Horman <nhorman@redhat.com>
- Update to latest upstream 

* Thu Feb 15 2018 Adam Williamson <awilliam@redhat.com> - 6.1-4
- Drop all attempts to 'fix' #1490632, revert spec to same as 6.1-1

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov 02 2017 Neil Horman <nhorman@redhat.com> - 6.1-2
- Enable rngd on entropy src availability (bz 1490632)

* Tue Oct 10 2017 Neil Horman <nhorman@redhat.com> - 6.1-1
- update to latest upstream

* Fri Jul 28 2017 Neil Horman <nhorman@redhat.com> - 6-1
- Update to latest upstream

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Oct 18 2016 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 5-8
- If device is not found exit immediately (#892178)

* Sun Mar  6 2016 Peter Robinson <pbrobinson@fedoraproject.org> 5-7
- Use %%license

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Dec 10 2014 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 5-4
- Build with hardening flags (#1051344)
- Fail nicely if no hardware generator is found (#892178)
- Drop unneeded dependency

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Apr 23 2014 Luke Macken <lmacken@redhat.com> - 5-1
- Update to release version 5.
- Remove rng-tools-man.patch

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Sep 25 2012 Jaromir Capik <jcapik@redhat.com> - 4-2
- Migration to new systemd macros

* Mon Aug 6 2012 Jeff Garzik <jgarzik@redhat.com> - 4-1
- Update to release version 4.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Jiri Popelka <jpopelka@redhat.com> - 3-4
- 2 patches from RHEL-6
- systemd service
- man page fixes
- modernize spec file

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul  3 2010 Jeff Garzik <jgarzik@redhat.com> - 3-2
- comply with renaming guidelines, by Providing rng-utils = 1:2.0-4.2

* Sat Jul  3 2010 Jeff Garzik <jgarzik@redhat.com> - 3-1
- Update to release version 3.

* Fri Mar 26 2010 Jeff Garzik <jgarzik@redhat.com> - 2-3
- more minor updates for package review

* Thu Mar 25 2010 Jeff Garzik <jgarzik@redhat.com> - 2-2
- several minor updates for package review

* Wed Mar 24 2010 Jeff Garzik <jgarzik@redhat.com> - 2-1
- initial revision (as rng-tools)


Summary: Utility for flashing LEGO Mindstorms NXT firmware
Name: libnxt
Version: 0.3
Release: 23%{?dist}
License: GPLv2+
URL: http://code.google.com/p/libnxt/
Source0: http://libnxt.googlecode.com/files/%{name}-%{version}.tar.gz
# Short document describing how to reflash the NXT firmware
Source1: %{name}-NXT-REFLASH-HOWTO
# Use appropriate tool's names (as per arm-gp2x-linux-gcc package)
Patch0: %{name}-flash-write-makefile.patch
# Use the hashlib module instead of the deprecated sha module
# Switch from using python2 to python3
Patch1: %{name}-switch-from-using-python2-to-python3.patch
# Removes the following compilation warning and make the code
# endian-independent:
# samba.c: In function 'nxt_read_common':
# samba.c:90: warning: dereferencing type-punned pointer will break
# strict-aliasing rules
Patch2: %{name}-samba-endian-independent.patch
# Respect CFLAGS and LDFLAGS environment variables during the build
Patch3: %{name}-sconstruct-optflags.patch
# Upstream issue: http://code.google.com/p/libnxt/issues/detail?id=2
Patch4: %{name}-detach-driver.patch
# Fix compilation error: duplicate 'const' declaration
Patch5: %{name}-fix-compilation-error-duplicate-const-declaration-sp.patch

BuildRequires: gcc
BuildRequires: /usr/bin/git
BuildRequires: python3
BuildRequires: libusb-devel
BuildRequires: scons
BuildRequires: arm-none-eabi-gcc-cs


%description
LibNXT is an utility library for talking to the LEGO Mindstorms NXT.
 It currently does:
 * Handling USB communication and locating the NXT in the USB tree.
 * Interaction with the Atmel AT91SAM boot assistant.
 * Flashing of a firmware image to the NXT.
 * Execution of code directly in RAM.


%prep
%autosetup -S git
cp -p %{SOURCE1} NXT-REFLASH-HOWTO
make -C flash_write clean # to be sure that we will regenerate the flash.bin


%build
make -C flash_write
export CFLAGS="%{optflags}"
export LDFLAGS="%{optflags}"
scons %{?_smp_mflags}


%install
install -p -D -m 755 fwexec %{buildroot}%{_bindir}/nxt-fwexec
install -p -D -m 755 fwflash %{buildroot}%{_bindir}/nxt-fwflash


%files
%license COPYING
%doc README NXT-REFLASH-HOWTO
%{_bindir}/nxt-fwexec
%{_bindir}/nxt-fwflash


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Aug 01 2019 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0.3-22
- Fix FTBFS rhbz#1736034

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 20 2018 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0.3-19
- Fix FTBFS RH BZ #1604623
- Switch from using python2 to python3
- Modernize spec file

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 07 2018 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0.3-17
- Add missing BR (gcc)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Aug 05 2013 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0.3-8
- switch to use arm-none-eabi-gcc-cs toolkit, fixes rhbz#992103,
- add patch to detach kernel driver,
- specfile cleanup.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Sep 13 2010 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0.3-2
- Fix for respecting CFLAGS and LDFLAGS during the build,
- Fix for strict-aliasing rules problem,
- Describe purpose of the patches,
- Firmware reflash HOWTO added.

* Mon Jul 19 2010 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0.3-1
- Initial RPM release

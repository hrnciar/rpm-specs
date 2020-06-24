Name:           dfu-programmer
Version:        0.7.2
Release:        6%{?dist}
Summary:        A Device Firmware Update based USB programmer for Atmel chips

License:        GPLv2+
URL:            http://dfu-programmer.github.io/
Source0:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  pkgconfig(libusb-1.0) >= 1.0.0

%description 
A linux based command-line programmer for Atmel chips with a USB
bootloader supporting ISP. This is a mostly Device Firmware Update
(DFU) 1.0 compliant user-space application. Supports all DFU enabled
Atmel chips with USB support.

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Oct 17 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.7.2-1
- Update to 0.7.2

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Jan  6 2014 Peter Robinson <pbrobinson@fedoraproject.org> 0.6.2-1
- Update to 0.6.2 and build against libusbx

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jan 16 2011 Weston Schmidt <weston_schmidt at alumni.purdue.edu> - 0.5.4-1
- added atmega8u2 support
* Sun Jan 16 2011 Weston Schmidt <weston_schmidt at alumni.purdue.edu> - 0.5.3-1
- added at32uc3c* support
- fixed a number of defects
* Sat Aug 22 2009 Weston Schmidt <weston_schmidt at alumni.purdue.edu> - 0.5.2-1
- added ability to read from STDIN
- added ability to configure AVR32 fuses
- Applied a number of bug fixes
- Fixed AVR device support
* Wed Dec 10 2008 Weston Schmidt <weston_schmidt at alumni.purdue.edu> - 0.5.1-1
- add new flag to surpress bootloader memory checking
* Wed Dec 03 2008 Weston Schmidt <weston_schmidt at alumni.purdue.edu> - 0.5.0-1
- update the description
- fix the broken hal rules
* Fri Aug 29 2008 Weston Schmidt <weston_schmidt at alumni.purdue.edu> - 0.4.6-1
- change udev rules and permissions to be hal based
* Wed Aug 20 2008 Weston Schmidt <weston_schmidt at alumni.purdue.edu> - 0.4.5-1
- added 4K bootloader support
- added eeprom-dump and eeprom-flash support
- fixed the Source0 url

Name:          dfu-util
Version:       0.9
Release:       9%{?dist}
Summary:       USB Device Firmware Upgrade tool
License:       GPLv2+

# Can't use normal SourceForge URL per Fedora Packaging/SourceURL
#   https://fedoraproject.org/wiki/Packaging:SourceURL
# because the project is not actually using the SourceForge file release
# system. They're just using SourceForge as a web server.
URL:            http://dfu-util.sourceforge.net/
Source0:        http://dfu-util.sourceforge.net/releases/%{name}-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: libusbx-devel

%description
USB Device Firmware Upgrade (DFU) is an official USB device class specification 
of the USB Implementers Forum. It specifies a vendor and device independent way 
of updating the firmware of a USB device. The idea is to have only one 
vendor-independent firmware update tool as part of the operating system, which 
can then (given a particular firmware image) be downloaded into the device. 

In addition to firmware download, it also specifies firmware upload, i.e.
loading the currently installed device firmware to the USB Host.

The DFU specification can be found at:
 http://www.usb.org/developers/devclass_docs/usbdfu10.pdf


%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
make DESTDIR=%{buildroot} install


%files
%license COPYING
%doc ChangeLog README DEVICES.txt TODO
%{_bindir}/*
%{_mandir}/man1/*


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Oct 24 2016 Peter Robinson <pbrobinson@fedoraproject.org> 0.9-1
- Latest 0.9 upstream release
- Minor spec cleanups

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Dec 15 2014 Eric Smith <brouhaha@fedoraproject.org> - 0.8-1
- Latest 0.8 upstream release

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 07 2013 Eric Smith <brouhaha@fedoraproject.org> - 0.7-1
- Latest 0.7 upstream release

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Dec 21 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 0.5-1
- Latest 0.5 upstream release
- Add license and appropriate docs

* Sat Jun 11 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 0.3-1
- Latest 0.3 upstream release
- Update URL and source location
- cleanup spec file

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-0.12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jun 22 2010 Juha Tuomala <tuju@iki.fi> - 0.1-0.11
- Update to first release, 0.1.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-0.10.20090307svn4917
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Mar 10 2009 Juha Tuomala <tuju@iki.fi> - 0.1-0.9.20090307svn4917
- Fix builds for Fedora 11.

* Tue Mar 10 2009 Juha Tuomala <tuju@iki.fi> - 0.1-0.8.20090307svn4917
- Add 64-bit archs again as x86_64 seems to work.

* Tue Mar 10 2009 Jaroslav Reznik <jreznik@redhat.com> - 0.1-0.7.20090307svn4917
- glibc-devel BR

* Tue Mar 10 2009 Juha Tuomala <tuju@iki.fi> - 0.1-0.6.20090307svn4917
- Update to snpshot 4917.

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-0.5.20080922svn4662
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Sep 22 2008 Juha Tuomala <tuju@iki.fi> - 0.1-0.4.20080922svn4662
- fixed perms and excluded static binary.

* Mon Sep 22 2008 Juha Tuomala <tuju@iki.fi> - 0.1-0.3.20080922svn4662
- Added missing BRs.

* Mon Sep 22 2008 Juha Tuomala <tuju@iki.fi> - 0.1-0.2.20080922svn4662
- Removed unecessary Requires: tag. Added ExlcudeArch for 64bit machines.

* Mon Sep 22 2008 Juha Tuomala <tuju@iki.fi> - 0.1-0.1.20080922svn4662
- Fixed version, license conflict, url, etc rpmlit warnings.

* Sun Sep 21 2008 Juha Tuomala <tuju@iki.fi> - 0.0svn4160
- Initial package version.

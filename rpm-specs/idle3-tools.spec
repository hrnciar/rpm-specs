Name:           idle3-tools
Version:        0.9.1
Release:        14%{?dist}
Summary:        Manipulate the value of the idle3 timer found on recent WD Hard Disk Drives
License:        GPLv3
URL:            http://idle3-tools.sourceforge.net/
Source0:        http://sourceforge.net/projects/idle3-tools/files/%{name}-%{version}.tgz
BuildRequires:  gcc
BuildRequires:  kernel-headers

%description
Idle3-tools provides a linux/unix utility that can disable, get and set the
value of the infamous idle3 timer found on recent Western Digital Hard Disk
Drives.  It can be used as an alternative to the official wdidle3.exe
proprietary utility, without the need to reboot in a DOS environement.  A power
off/on cycle of the drive will still be mandatory for new settings to be taken
into account.

Idle3-tools is an independant project, unrelated in any way to Western Digital Corp.
WARNING: THIS SOFTWARE IS EXPERIMENTAL AND NOT WELL TESTED. IT ACCESSES LOW
LEVEL INFORMATION OF YOUR HARDDRIVE. USE AT YOUR OWN RISK.

%prep
%setup -q

%build
CFLAGS="${RPM_OPT_FLAGS}" make %{?_smp_mflags} \
    LDFLAGS="${RPM_LD_FLAGS}" STRIP=/bin/true

%install
rm -rf $RPM_BUILD_ROOT
%make_install binprefix=/usr

%files
%doc COPYING
%{_sbindir}/idle3ctl
%{_mandir}/man8/idle3ctl*

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Dec 31 2013 Ville Skyttä <ville.skytta@iki.fi> - 0.9.1-2
- Fix -debuginfo (#883104).

* Mon Dec  3 2012 Paul Komkoff <i@stingr.net> - 0.9.1-1
- initial version

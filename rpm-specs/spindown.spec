Summary:    Daemon that can spin idle disks down
Name:       spindown
Version:    0.4.0
Release:    27%{?dist}
License:    GPLv3+
Url:        http://code.google.com/p/spindown
Source0:    http://spindown.googlecode.com/files/spindown-%{version}.tar.gz
Source1:    spindown.service
Source2:    01spindown

Patch0: spindown-0.4.0-Makefile.patch
Patch1: spindown-0.4.0-iniparser.patch
Patch2: spindown-0.4.0-iniparser-3.0-1.patch
Patch3: spindown-0.4.0-bz1037334.patch

Requires(preun): systemd-units

BuildRequires:  gcc-c++
BuildRequires: iniparser-devel
BuildRequires: systemd-units

%description
Spindown is a daemon that can spin idle disks down and thus save energy and
improve disk lifetime. It periodically checks for read or written blocks. When
no blocks are read or written the disk is idle. When a disk stays idle long
enough, spindown uses custom command like sg_start or hdparm to spin it down.
It also works with USB disks and hot-swappable disks because it doesn't watch
the device name (hda, sdb, ...), but the device ID. This means that it doesn't
matter if the disk is swapped while the daemon is running.

%prep
%setup -q
rm -rf src/ininiparser3.0b
cp -pf %{SOURCE1} spindown.service
cp -pf %{SOURCE2} 01spindown
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
make %{?_smp_mflags} OPT="$RPM_OPT_FLAGS"

%install
make DESTDIR="$RPM_BUILD_ROOT" install
mkdir -p $RPM_BUILD_ROOT/%{_libdir}/pm-utils/sleep.d
mkdir -p $RPM_BUILD_ROOT/%{_unitdir}
install -p -m 755 01spindown $RPM_BUILD_ROOT/%{_libdir}/pm-utils/sleep.d/01spindown
install -p -m 755 spindown.service $RPM_BUILD_ROOT/%{_unitdir}/spindown.service

%preun
%systemd_preun spindown.service

%files
%doc COPYING CHANGELOG README
%{_unitdir}/spindown.service
%{_sbindir}/spindownd
%{_libdir}/pm-utils/sleep.d/01spindown
%config(noreplace) %{_sysconfdir}/spindown.conf

%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.4.0-17
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jan 02 2014 Martin Cermak <mcermak@redhat.com> 0.4.0-14
- Use new systemd-rpm macros in spindown spec file (resolves bz850324)

* Tue Dec 03 2013 Martin Cermak <mcermak@redhat.com> 0.4.0-13
- Build correctly with -Werror=format-security (resolves bz1037334)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-9
- Rebuilt for c++ ABI breakage

* Tue Feb 21 2012 Martin Cermak <mcermak@redhat.com> 0.4.0-8
- Improved fix for bz787231 as discussed in bz769059#c7
- Fixed systemd unit installation

* Fri Feb 03 2012 Martin Cermak <mcermak@redhat.com> 0.4.0-7
- Behave correctly after waking from suspend (resolves bz787231)

* Tue Jan 31 2012 Martin Cermak <mcermak@redhat.com> 0.4.0-6
- Fixed against iniparser-3.0-1

* Thu Jan 26 2012 Martin Cermak <mcermak@redhat.com> 0.4.0-5
- Replaced sysvinitscript with a systemd unit

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri May  6 2011 Martin Cermak <mcermak@redhat.com> 0.4.0-3
- Initscript changed according to comment #5 in bz700571

* Wed May  4 2011 Martin Cermak <mcermak@redhat.com> 0.4.0-2
- Multiple changes described in the comment #3 in bz700571

* Thu Apr 28 2011 Martin Cermak <mcermak@redhat.com> 0.4.0-1
- Packaged for Fedora 



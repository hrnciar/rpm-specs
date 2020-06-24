Name:       ArpON
Version:    3.0
Release:    13%{?dist}
Summary:    ARP handler inspection

License:    BSD
URL:        http://arpon.sourceforge.net/
Source0:    http://downloads.sourceforge.net/project/arpon/arpon/ArpON-%{version}/ArpON-%{version}-ng.tar.gz
Patch1:     ArpON-gcc-7-fixes.patch
Patch2:     ArpON-gcc-8-fixes.patch

BuildRequires:  gcc
BuildRequires:  libpcap-devel
BuildRequires:  cmake
BuildRequires:  libnet-devel
BuildRequires:  libdnet-devel

%description
ArpON (ARP handler inspection) is a Host-based solution that make the ARP
standardized protocol secure in order to avoid the Man In The Middle (MITM)
attack through the ARP spoofing, ARP cache poisoning or ARP poison routing
attack.

%prep
%setup -q -n %{name}-%{version}-ng
%patch1 -p1
%patch2 -p1

%build
%cmake -DCMAKE_INSTALL_PREFIX="/" .
%{__make} %{?_smp_mflags}

%install
%{__install} -D -pm 755 src/arpon %{buildroot}%{_sbindir}/arpon
%{__install} -D -pm 644 man8/arpon.8 %{buildroot}%{_mandir}/man8/arpon.8
%{__install} -D -pm 644 etc/arpon.conf %{buildroot}/etc/arpon.conf
%{__install} -D -pm 644 log/arpon.log %{buildroot}/var/log/arpon.log

%files
%license LICENSE
%doc AUTHOR CHANGELOG doc/*
%{_sbindir}/arpon
/etc/arpon.conf
/var/log/arpon.log
%{_mandir}/man8/arpon.8*

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Sep 04 2018 Arun S A G <sagarun@fedoraproject.org> - 3.0-10
- Fix GCC 8 compiler warnings are treated as errors

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Apr 11 2018 Filipe Rosset <rosset.filipe@gmail.com> - 3.0-8
- added patch to build with gcc7 fixes rhbz #1555446

* Tue Mar 06 2018 Fabian Affolter <mail@fabian-affolter.ch> - 3.0-7
- Fix BR

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Apr 12 2016 Ville Skyttä <ville.skytta@iki.fi> - 3.0-2
- Build with %%{optflags}, follow cmake guidelines, mark LICENSE as %%license

* Sat Apr 02 2016 Arun S A G <sagarun@fedoraproject.org> - 3.0-1
- New generation of ArpON

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Oct 07 2014 Fabian Affolter <mail@fabian-affolter.ch> - 2.7-9
- Update spec file

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jan 06 2013 Arun S A G <sagarun@gmail.com> - 2.7-4
- Bug:856179 Fix spelling mistakes in man page
 
* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Mar 30 2012 Jon Ciesla <limburgher@gmail.com> - 2.7-2
- libnet rebuild.

* Sat Jan 21 2012 Arun SAG <sagarun@gmail.com> - 2.7-1
- Updated to latest upstream version 2.7
- Remove explicit requires on libraries

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Jul 31 2011 Arun SAG <sagarun [AT] gmail dot com> - 2.6-2
- Fix broken deps

* Sun Jul 17 2011 Arun SAG <sagarun [AT] gmail dot com> - 2.6-1
- Updated to version 2.6

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.90-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Apr 02 2010 Arun SAG <sagarun [AT] gmail dot com> -  1.90-7
- Bumping release to fix previous CVS commit.

* Thu Mar 25 2010 Arun SAG <sagarun [AT] gmail dot com> - 1.90-6
- Bumping release to fix previous CVS commit.

* Tue Mar 9 2010 Arun SAG <sagarun [AT] gmail dot com> - 1.90-5
- Fixed mixed usage of capital letters and period in changelog. 
- Fixed install so that arpon.8 gets copied in correct directory.

* Sun Mar 7 2010 Arun SAG <sagarun [AT] gmail dot com> - 1.90-4
- Optflags used instead of RPM_OPT_FLAGS.
- Man dir corrected.

* Wed Jan 13 2010 Arun SAG <sagarun [AT] gmail dot com> - 1.90-3
- Source URL fixed.
- Install part rewrittern.

* Sat Jan 2 2010 Arun SAG <sagarun [AT] gmail dot com> - 1.90-2
- Removed insignificant INSTALL file from binary package.
- Changed build section to  use Fedora project flags.

* Sun Dec 20 2009 Arun SAG <sagarun [AT] gmail dot com> - 1.90-1
- My initial release.

* Tue Dec 01 2009 Sandro Mathys <red at fedoraproject.org> - 1.90-1
- Initial build.

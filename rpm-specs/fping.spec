%global _hardened_build 1

Name: fping
Version: 4.2
Release: 4%{?dist}
Summary: Scriptable, parallelized ping-like utility
License: BSD with advertising
URL: http://www.fping.org/
Source0: http://fping.org/dist/%{name}-%{version}.tar.gz
Patch0: fping-4.2-gcc10-extern.patch

BuildRequires: gcc

%description
fping is a ping-like program which can determine the accessibility of
multiple hosts using ICMP echo requests. fping is designed for parallelized
monitoring of large numbers of systems, and is developed with ease of
use in scripting in mind.

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install

%files
%doc CHANGELOG.md
%license COPYING
%attr(0755,root,root) %caps(cap_net_raw=ep) %{_sbindir}/fping
%{_mandir}/man8/*

%changelog
* Sun Feb  2 2020 Charles R. Anderson <cra@wpi.edu> - 4.2-4
- Patch for GCC 10 requirement to use extern in header files when declaring global variables

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb 27 2019 Charles R. Anderson <cra@wpi.edu> - 4.2-1
- update to 4.2
- use %%autosetup, %%make_build, %%make_install macros
- mark COPYING as %%license

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Sep 18 2018 Charles R. Anderson <cra@wpi.edu> - 4.1-1
- update to 4.1

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Feb 18 2018 Charles R. Anderson <cra@wpi.edu> - 4.0-6
- Add BR gcc
- Remove Group: and rm -rf in install section

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu May 04 2017 Charles R. Anderson <cra@wpi.edu> - 4.0-2
- remove obsolete CFLAGS

* Wed May 03 2017 Charles R. Anderson <cra@wpi.edu> - 4.0-1
- update to 4.0
- remove EL5 and old Fedora compatibility

* Mon Feb 20 2017 Charles R. Anderson <cra@wpi.edu> - 3.16-1
- update to 3.16 (rhbz#1420733)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 31 2017 Charles R. Anderson <cra@wpi.edu> - 3.15-1
- update to 3.15 (rhbz#1412003)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Oct 24 2015 Charles R. Anderson <cra@wpi.edu> - 3.13-1
- update to 3.13 (rhbz#1271420)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 21 2014 Charles R. Anderson <cra@wpi.edu> - 3.10-1
- update to 3.10 (rhbz#1094411)

* Wed Mar 12 2014 Charles R. Anderson <cra@wpi.edu> - 3.9-1
- update to 3.9 (rhbz#1074890)

* Sat Nov 16 2013 Charles R. Anderson <cra@wpi.edu> - 3.8-1
- update to 3.8 (rhbz#1018121)

* Tue Aug 13 2013 Charles R. Anderson <cra@wpi.edu> - 3.5-3
- enable _hardened_build for -fPIE (rhbz#983602)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri May 24 2013 Charles R. Anderson <cra@wpi.edu> - 3.5-1
- update to 3.5 (rhbz#925355, rhbz#966000)

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Sep 24 2012 Charles R. Anderson <cra@wpi.edu> - 3.4-1
- update to 3.4 which fixes rhbz#854572 by restoring previous behavior:
  * Revert "Output statistics to stdout instead of stderr", because it breaks
    tools assuming the output goes to stderr

* Thu Aug 30 2012 Charles R. Anderson <cra@wpi.edu> - 3.3-2
- use configure options to build ipv4 and ipv6 versions simultaneously
  so we can use the standard make install to get the fping6 man page,
  etc.
- build for el6 w/cap_net_raw (el5 still needs traditional setuid)
- use preferred Buildroot tag for el5
- make conditional build with/without ENABLE_F_OPTION actually work

* Thu Aug 30 2012 Charles R. Anderson <cra@wpi.edu> - 3.3-1
- update to 3.3

* Thu Jul 26 2012 Charles R. Anderson <cra@wpi.edu> - 3.2-1
- update to 3.2
- no longer need capnetraw patch

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Feb 18 2012 Charles R. Anderson <cra@wpi.edu> - 3.0-1
- fping-3.0 based on new upstream at http://www.fping.org/
  - Debian patches until version 2.4b2-to-ipv6-16.
  - Modifications by Tobias Oetiker for SmokePing (2.4b2-to4)
  - Reimplemented main loop for improved performance

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4b2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Sep 04 2011 Charles R. Anderson <cra@wpi.edu> - 2.4b2-12
- remove SUID and add CAP_NET_RAW instead on Fedora 15 and newer (rhbz#646466)
- allow -f option for non-root on Fedora 15 and newer
- remove read permissions on binaries for Fedora 14 and older

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4b2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4b2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4b2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 15 2008 Chris Ricker <kaboom@oobleck.net> 2.4b2-8
- Rebuild for GCC 4.3
- Fix license

* Mon Sep 11 2006 Chris Ricker <kaboom@oobleck.net> 2.4b2-7
- Bump and rebuild

* Tue Feb 14 2006 Chris Ricker <kaboom@oobleck.net> 2.4b2-6
- Bump and rebuild

* Wed Jun 29 2005 Chris Ricker <kaboom@oobleck.net> 2.4b2-5
- Clean up changelog and tags

* Wed Jun 01 2005 Chris Ricker <kaboom@oobleck.net> 2.4b2-4
- Bump release and build

* Wed Jun 01 2005 Chris Ricker <kaboom@oobleck.net> 2.4b2-3
- Add dist tag

* Mon May 16 2005 Chris Ricker <kaboom@oobleck.net> 2.4b2-3
- Simplify doc packaging (Matthias Saou)
- Simplify clean (Matthias Saou)
- Don't strip fping6 binary (Matthias Saou)
- Preserve timestamps

* Wed May 11 2005 Chris Ricker <kaboom@oobleck.net> 2.4b2-2
- Fix URL and Source locations

* Wed Mar 23 2005 Chris Ricker <kaboom@oobleck.net> 2.4b2-1
- Initial package for Fedora
- IPv6 patches from Herbert Xu (Debian)

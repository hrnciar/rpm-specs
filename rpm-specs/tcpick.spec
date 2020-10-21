Summary:	A tcp stream sniffer, tracker and capturer
Name: 		tcpick
Version: 	0.2.1
Release: 	38%{?dist}
License: 	GPLv2+
URL: 		http://tcpick.sourceforge.net/
Source:		http://downloads.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.gz
Patch0:		tcpick-0.2.1-CVE-2006-0048.patch
Patch1:		tcpick-0.2.1-ppc.patch
Patch2:		tcpick-0.2.1-pointers.patch
Patch3:		tcpick-0.2.1-cpu-loop.patch
Patch4:		tcpick-0.2.1-timezone.patch
Patch5:		tcpick-0.2.1-gcc5.patch
Patch6:		tcpick-0.2.1-gcc10.patch
BuildRequires:	gcc, libpcap-devel

%description
tcpick is a textmode sniffer that can track tcp streams and saves 
the data captured in files or displays them in the terminal. Useful 
for picking files in a passive way.

It can store all connections in different files, or it can display
all the stream on the terminal. It is useful to keep track of what
users of a network are doing, and is usable with textmode tools
like grep, sed and awk. It can handle eth and ppp interfaces.

%prep
%setup -q
%patch0 -p1 -b .CVE-2006-0048
%patch1 -p1 -b .ppc
%patch2 -p1 -b .pointers
%patch3 -p1 -b .cpu-loop
%patch4 -p1 -b .timezone
%patch5 -p1 -b .gcc5
%patch6 -p1

%build
%configure --bindir=%{_sbindir}
%make_build

%install
%make_install

# Move the Italian man page to its correct place
mkdir -p $RPM_BUILD_ROOT%{_mandir}/it/man8
mv -f $RPM_BUILD_ROOT%{_mandir}/man8/tcpick_italian.8 $RPM_BUILD_ROOT%{_mandir}/it/man8/tcpick.8

# Convert non-utf8 authors file into utf8
iconv -f iso-8859-1 -t utf-8 -o AUTHORS.utf8 AUTHORS
touch -c -r AUTHORS AUTHORS.utf8; mv -f AUTHORS.utf8 AUTHORS

%files 
%license COPYING
%doc AUTHORS ChangeLog EXAMPLES KNOWN-BUGS README THANKS
%{_sbindir}/%{name}
%{_mandir}/man8/%{name}.8*
%{_mandir}/it/man8/%{name}.8*

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Feb 02 2020 Robert Scheck <robert@fedoraproject.org> 0.2.1-37
- Added patch to declare structs as extern in header file

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 14 2019 Jeff Law <law@redhta.com> - 0.2.1-35
- Fix inline vs static inline issues for gcc-10

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jun 20 2015 Robert Scheck <robert@fedoraproject.org> 0.2.1-26
- Added patch to make rebuilding with GCC 5 working

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Mar 29 2009 Lubomir Rintel <lkundrak@v3.sk> 0.2.1-16
- Fix -t abort on 64bit (#492109)

* Mon Feb 23 2009 Robert Scheck <robert@fedoraproject.org> 0.2.1-15
- Rebuilt against gcc 4.4 and rpm 4.6

* Sun Feb 10 2008 Robert Scheck <robert@fedoraproject.org> 0.2.1-14
- Rebuilt against gcc 4.3

* Tue Aug 28 2007 Robert Scheck <robert@fedoraproject.org> 0.2.1-13
- Updated the license tag according to the guidelines
- Buildrequire %%{_includedir}/pcap.h instead of conditionals

* Mon May 07 2007 Robert Scheck <robert@fedoraproject.org> 0.2.1-12
- Rebuilt

* Wed Nov 29 2006 Robert Scheck <robert@fedoraproject.org> 0.2.1-11
- Rebuilt

* Sun Sep 10 2006 Robert Scheck <robert@fedoraproject.org> 0.2.1-10
- Better workaround for CVE-2006-0048 to make tcpick usable again
- Added patches for double-free, broken pointers and getopt on ppc

* Sun Sep 03 2006 Robert Scheck <robert@fedoraproject.org> 0.2.1-9
- Rebuild for Fedora Core 6

* Tue Jun 20 2006 Robert Scheck <robert@fedoraproject.org> 0.2.1-8
- Changes to match with Fedora Packaging Guidelines (#195764)

* Wed May 31 2006 Robert Scheck <robert@fedoraproject.org> 0.2.1-7
- Fixed CVE-2006-0048 (denial of service via fragmented packets)
- Added libpcap-devel as build requirement (#193189)

* Tue Mar 07 2006 Robert Scheck <robert@fedoraproject.org> 0.2.1-6
- Rebuilt against gcc 4.1 and glibc 2.4

* Fri Nov 11 2005 Robert Scheck <robert@fedoraproject.org> 0.2.1-5
- Rebuilt against libpcap 0.9.4

* Thu Jul 28 2005 Robert Scheck <robert@fedoraproject.org> 0.2.1-4
- Rebuilt against libpcap 0.9.3

* Fri Jul 15 2005 Robert Scheck <robert@fedoraproject.org> 0.2.1-3
- Rebuilt against libpcap 0.9.1

* Sun Mar 13 2005 Robert Scheck <robert@fedoraproject.org> 0.2.1-2
- Rebuilt against gcc 4.0

* Sun Jan 30 2005 Robert Scheck <robert@fedoraproject.org> 0.2.1-1
- Upgrade to 0.2.1

* Sun Jan 16 2005 Robert Scheck <robert@fedoraproject.org> 0.2.0-1
- Upgrade to 0.2.0

* Sat Aug 28 2004 Robert Scheck <robert@fedoraproject.org> 0.1.24-1
- Fixed a typo caused by the man page change
- Upgrade to 0.1.24

* Sat Jun 05 2004 Robert Scheck <robert@fedoraproject.org> 0.1.23-1
- Upgrade to 0.1.23

* Thu May 06 2004 Robert Scheck <robert@fedoraproject.org> 0.1.22-1
- Upgrade to 0.1.22

* Tue Mar 02 2004 Robert Scheck <robert@fedoraproject.org> 0.1.21-1
- Upgrade to 0.1.21

* Fri Feb 27 2004 Robert Scheck <robert@fedoraproject.org> 0.1.20-1
- Upgrade to 0.1.20
- Moved tcpick binary from /usr/bin to /usr/sbin
- Added more description about tcpick

* Fri Jan 30 2004 Robert Scheck <robert@fedoraproject.org> 0.1.19-1
- Upgrade to 0.1.19

* Tue Jan 13 2004 Robert Scheck <robert@fedoraproject.org> 0.1.18-1
- Upgrade to 0.1.18
- Added patch to solve problems with libpcap

* Wed Jan 07 2004 Robert Scheck <robert@fedoraproject.org> 0.1.17-1
- Upgrade to 0.1.17

* Fri Dec 12 2003 Robert Scheck <robert@fedoraproject.org> 0.1.13-1
- Upgrade to 0.1.13

* Thu Dec 04 2003 Robert Scheck <robert@fedoraproject.org> 0.1.10-1
- Upgrade to 0.1.10
- Initial spec file for Red Hat Linux and Fedora Core

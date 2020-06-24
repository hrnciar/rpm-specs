%global commit 258a27e5a47809f97c2b9f2751a88c2f94aae891
%global build_date 20151227

%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global posttag %{build_date}git%{shortcommit}

Summary: A port-knocking server/client
Name: knock
Version: 0.7.8
Release: 9.%{posttag}%{?dist}
License: GPLv2+
URL: http://www.zeroflux.org/projects/%{name}
Source0: https://github.com/jvinet/%{name}/archive/%{commit}/%{name}-%{commit}.tar.gz
Source1: %{name}d.sysconfig
Source2: %{name}d.conf
Source3: %{name}d.service
# Installs the helper executable in /usr/libexec instead of /usr/sbin
Patch0: knock_fix_knock_helper_ipt_location.patch
Requires: systemd
%{?systemd_requires}
BuildRequires:  gcc
BuildRequires: systemd
BuildRequires: libpcap
BuildRequires: libpcap-devel
BuildRequires: systemd-units
BuildRequires: autoconf
BuildRequires: automake

%description
This is a port-knocking server/client.  Port-knocking is a method where a
server can sniff one of its interfaces for a special "knock" sequence of
port-hits.  When detected, it will run a specified event bound to that port
knock sequence.  These port-hits need not be on open ports, since we use
libpcap to sniff the raw interface traffic. This package contains the
knock client.

%package server
Summary: A port-knocking server/client

%description server
Knock is a port-knocking server/client.  Port-knocking is a method where a
server can sniff one of its interfaces for a special "knock" sequence of
port-hits.  When detected, it will run a specified event bound to that port
knock sequence.  These port-hits need not be on open ports, since we use
libpcap to sniff the raw interface traffic. This package contains the
knockd server.

%prep
%setup -q -n %{name}-%{commit}
%patch0

%build
autoreconf -i
%{configure}
%{__make}
iconv -f iso8859-1 -t utf-8 ChangeLog > ChangeLog.conv && mv -f ChangeLog.conv ChangeLog

%install

%{__make} install DESTDIR=%{buildroot} INSTALL="install -p"
%{__install} -d %{buildroot}%{_sysconfdir}/sysconfig
%{__install} -d %{buildroot}%{_unitdir}

%{__install} -m 0644 -p %{SOURCE1} %{buildroot}%{_sysconfdir}/sysconfig/%{name}d
%{__install} -m 0644 -p %{SOURCE2} %{buildroot}%{_sysconfdir}/
%{__install} -m 0644 -p %{SOURCE3} %{buildroot}%{_unitdir}/%{name}d.service

# Added as license
%{__rm} -f %{buildroot}%{_docdir}/COPYING

%post server
%systemd_post knockd.service

%preun server
%systemd_preun knockd.service

%postun server
%systemd_postun_with_restart knockd.service

%files
%license COPYING
%doc %{_docdir}/%{name}
%{_bindir}/%{name}
%{_mandir}/man?/%{name}.*

%files server
%license COPYING
%doc %{_docdir}/%{name}
%{_sbindir}/%{name}d
%{_libexecdir}/knock_helper_ipt.sh
%{_unitdir}/%{name}d.service
%config(noreplace) %{_sysconfdir}/%{name}d.conf
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}d
%{_mandir}/man?/%{name}d.*

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.8-9.20151227git258a27e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.8-8.20151227git258a27e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.8-7.20151227git258a27e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.8-6.20151227git258a27e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.8-5.20151227git258a27e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.8-4.20151227git258a27e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.8-3.20151227git258a27e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.8-2.20151227git258a27e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Christos Triantafyllidis <christos.triantafyllidis@gmail.com> 0.7.8-1.20151227git258a27e
- Updated to version 0.7.8 from github

* Mon Dec 14 2015 Christos Triantafyllidis <christos.triatnafyllidis@gmail.com> 0.7.5-1.20151214git36efbdb
- Updated to version 0.7.5 from github

* Fri Mar 13 2015 Christos Triantafyllidis <christos.triantafyllidis@gmail.com> 0.7-1
- updated to version 0.7
- rebuild according to Fedora package guidelines

* Fri Apr 15 2011 Simon Matter <simon.matter@invoca.ch> 0.5-7
- mass rebuild

* Thu Aug 20 2009 Simon Matter <simon.matter@invoca.ch> 0.5-6
- change license tag to GPLv2+
- fix URL's
- fix CFLAGS
- cosmetic spec file changes

* Thu Aug 20 2009 Nik Conwell <nik@bu.edu> - 0.5-5
- Include limits.h in list.h to get to build on Fedora 11.
- Fix from datatek on forums.fedoraforum.org.

* Fri May 25 2007 Simon Matter <simon.matter@invoca.ch> 0.5-4
- autodetect whether libpcap-devel is required
- change to new pre/post-requires style

* Thu Mar 02 2006 Simon Matter <simon.matter@invoca.ch> 0.5-3
- add patch to change syslog facility to authpriv

* Tue Sep 06 2005 Simon Matter <simon.matter@invoca.ch> 0.5-2
- add libpcap to build requirements

* Mon Jul 18 2005 Simon Matter <simon.matter@invoca.ch>
- updated to version 0.5

* Wed Jan 12 2005 Simon Matter <simon.matter@invoca.ch>
- updated to version 0.4

* Wed Sep 15 2004 Simon Matter <simon.matter@invoca.ch>
- updated to version 0.3.1

* Wed Aug 04 2004 Simon Matter <simon.matter@invoca.ch>
- fixed pcap patch
- fixed build issue on Fedora Core

* Wed May 19 2004 Simon Matter <simon.matter@invoca.ch>
- updated to version 0.3

* Fri Apr 16 2004 Simon Matter <simon.matter@invoca.ch>
- updated to version 0.2.1

* Thu Apr 15 2004 Simon Matter <simon.matter@invoca.ch>
- splitted package into client and server part
- fixed build on RedHat 6.2
- updated to version 0.2

* Wed Apr 14 2004 Simon Matter <simon.matter@invoca.ch>
- initial build

Name: nuttcp
Version: 8.1.4
Release: 3%{?dist}
Source0: http://nuttcp.net/nuttcp/%{name}-%{version}.tar.bz2
Source1: %{name}@.service
Source2: %{name}.socket
URL: http://nuttcp.net/
Summary: Tool for testing TCP connections
License: Public Domain
BuildRequires:  gcc
BuildRequires:		systemd-units
Requires(post):		systemd-units
Requires(preun):	systemd-units
Requires(postun):	systemd-units

%description
nuttcp is a network performance measurement tool intended for use by
network and system managers.  Its most basic usage is to determine the
raw TCP (or UDP) network layer throughput by transferring memory buffers
from a source system across an interconnecting network to a destination
system, either transferring data for a specified time interval, or
alternatively transferring a specified number of buffers.  In addition
to reporting the achieved network throughput in Mbps, nuttcp also
provides additional useful information related to the data transfer
such as user, system, and wall-clock time, transmitter and receiver
CPU utilization, and loss percentage (for UDP transfers).

%prep
%autosetup

#sed -i -e "s,/usr/local/bin,%{_bindir},g;" \
#       -e  "s,disable\(.*\)no,disable\t\t= yes,g" xinetd.d/*

%build
make CFLAGS="$RPM_OPT_FLAGS"

%install
rm -fr $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT{%{_mandir}/man8,%{_bindir},%{_sysconfdir}/xinetd.d}
install -m755 %{name}-%{version} $RPM_BUILD_ROOT%{_bindir}/%{name}
install -pm644 %{name}.8 $RPM_BUILD_ROOT%{_mandir}/man8
mkdir -p %{buildroot}%{_unitdir}
install -m644 %{SOURCE1} $RPM_BUILD_ROOT%{_unitdir}
install -m644 %{SOURCE2} $RPM_BUILD_ROOT%{_unitdir}

%post
if [ $1 -eq 1 ] ; then
    # Initial installation
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%preun
if [ $1 -eq 0 ]; then
        #Package removal, not upgrade
        systemctl --no-reload disable %{name}@.service >/dev/null 2>&1 || :
        systemctl stop %{name}@.service >/dev/null 2>&1 || :
fi

%postun
if [ $1 -ge 1 ]; then
        #Package upgrade, not uninstall
        systemctl try-restart %{name}@.service >/dev/null 2>&1
fi


%files
%doc README examples.txt nuttcp.html xinetd.d/nuttcp4 xinetd.d/nuttcp6
%{_bindir}/%{name}
%{_mandir}/man8/*
%{_unitdir}/%{name}@.service
%{_unitdir}/%{name}.socket


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 10 2019 Nikos Mavrogiannopoulos <nmav@redhat.com> - 8.1.4-1
- New upstream release

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 6.1.2-19
- Escape macros in %%changelog

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.1.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.1.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Aug 01 2014 Nikos Mavrogiannopoulos <nmav@redhat.com> - 6.1.2-11
- provide fix for crash when /proc/sys/net/ipv4/tcp_adv_win_scale didn't exist (#1088932)
- provide fix for format-string issue

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov 23 2011 Radek Vokal <rvokal@redhat.com> - 6.1.2-5
- provide native systemd services (#737705)
- drop xinetd file

* Mon Feb 14 2011 Radek Vokal <rvokal@redhat.com> - 6.1.2-1
- upgrade to 6.1.2

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.5.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.5.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jul 18 2008 Radek Vokál <rvokal@redhat.com> - 5.5.5-1
- upgrade to 5.5.5
- remove pre1 from makefile

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 5.3.1-4
- Autorebuild for GCC 4.3

* Mon Jan 29 2007 Radek Vokál <rvokal@redhat.com> - 5.3.1-3
- fix CFLAGS (#225102)

* Mon Sep 11 2006 Radek Vokal <rvokal@redhat.com> - 5.3.1-2
- rebuilt

* Fri Jul 21 2006 Radek Vokál <rvokal@redhat.com> - 5.3.1-1
- upgrade to 5.3.1

* Wed Feb 22 2006 Radek Vokál <rvokal@redhat.com> - 5.1.11-6
- rebuilt 

* Wed Feb 08 2006 Radek Vokál <rvokal@redhat.com> - 5.1.11-5
- rebuilt

* Mon Nov 28 2005 Radek Vokal <rvokal@redhat.com> - 5.1.11-4
- remove debuglist files from tarball
- make gcc happier, warnings clean-up

* Tue Nov 22 2005 Radek Vokal <rvokal@redhat.com> - 5.1.11-3
- spec file clean up by Adrian Reber <adrian@lisas.de>
- added a URL
- removed wrong URL from Source
- fixed summary according to guidlines
- removed bogus build require
- disabled xinetd services
- using correct path in xinetd files
- removed unnecessary checks for BUILD_ROOT
- replaced /etc with macro
- added noreplace flag to %%config

* Mon Nov 21 2005 Radek Vokal <rvokal@redhat.com> - 5.1.11-2
- add xinetd.d service
- removed some unnecessary files from tarball

* Mon Nov 21 2005 Radek Vokal <rvokal@redhat.com> - 5.1.11-1
- initial built

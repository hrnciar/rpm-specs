Name:		node	
Version:	0.3.2
Release:	28%{?dist}
Summary:	Simple node front end, modelled after the node shells of TheNet and G8BPQ nodes

License:	GPLv2+
URL:		ftp://ftp.hes.iki.fi/pub/ham/linux/ax25/
Source0:	ftp://ftp.hes.iki.fi/pub/ham/linux/ax25/%{name}-%{version}.tar.gz
Source1:	node.xinetd
Patch0:		node-0.3.2-conf.patch
Patch1:		node-0.3.2-rose.patch
Patch2:		node-0.3.2-install.patch

Requires: /sbin/service
Requires: xinetd
BuildRequires:  gcc
BuildRequires:	zlib-devel
BuildRequires:	libax25-devel

%description
This is a simple node frontend for Linux kernel AX.25, NETROM,
ROSE and TCP. It's based on pms.c by Alan Cox (GW4PTS) but has been
heavily modified since.

%prep
%setup -q
%patch0 -p1 -b .conf
%patch1 -p1 -b .rose
%patch2 -p1 -b .install


%build
#this is no standard configure file just a custom script to setup things
sh configure
# populate CFLAGS, 
# which is internal build variable to accomodate Fedora opt flags
make %{?_smp_mflags} -e CFLAGS="%{optflags}"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_sbindir}
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/lib/ax25
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man{1,5,8}
make ETC_DIR=$RPM_BUILD_ROOT%{_sysconfdir}/ax25 SBIN_DIR=$RPM_BUILD_ROOT%{_sbindir} LIB_DIR=$RPM_BUILD_ROOT%{_datadir} MAN_DIR=$RPM_BUILD_ROOT%{_mandir} VAR_DIR=$RPM_BUILD_ROOT%{_localstatedir}/lib/ax25 install installconf
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/xinetd.d
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/xinetd.d/node
#rename some files to clear namespace
mv $RPM_BUILD_ROOT%{_sbindir}/node $RPM_BUILD_ROOT%{_sbindir}/ax25-node
mv $RPM_BUILD_ROOT%{_mandir}/man8/node.8 $RPM_BUILD_ROOT%{_mandir}/man8/ax25-node.8




%post
[ -f /var/lock/subsys/xinetd ] && /sbin/service xinetd reload > /dev/null 2>&1 || :

%postun
[ -f /var/lock/subsys/xinetd ] && /sbin/service xinetd reload > /dev/null 2>&1 || :


%files
%{_sbindir}/ax25-node
%{_sbindir}/nodeusers
%{_mandir}/man1/node*
%{_mandir}/man5/node*
%{_mandir}/man8/*node*
%{_datadir}/ax25/node/help/*
%{_localstatedir}/lib/ax25/node/loggedin
%config(noreplace) %attr(0644,root,root) %{_sysconfdir}/xinetd.d/node
%config(noreplace) %attr(0644,root,root) %{_sysconfdir}/ax25/node.conf
%config(noreplace) %attr(0644,root,root) %{_sysconfdir}/ax25/node.motd
%config(noreplace) %attr(0644,root,root) %{_sysconfdir}/ax25/node.perms
%doc AUTHORS COPYING HISTORY README



%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Oct 30 2015 Richard Shaw <hobbes1069@gmail.com> - 0.3.2-18
- Rebuild for updated libax25.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue May 21 2013 Lucian Langa <cooly@gnome.eu.org> - 0.3.2-13
- rename binary/man page to clear namespace

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat May 05 2012 Lucian Langa <cooly@gnome.eu.org> - 0.3.2-10
- add patch from Jeff Gustafson to fix build issues

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Aug 23 2008 Lucian Langa <cooly@gnome.eu.org> - 0.3.2-5
fix for #458818

* Mon Jun 23 2008 Lucian Langa <cooly@gnome.eu.org> - 0.3.2-4
- added fedora's compiler flags
- licence fix

* Mon Jun 23 2008 Lucian Langa <cooly@gnome.eu.org> - 0.3.2-3
- Fixed description
- change var/ax25 -> var/lib/ax25

* Wed Jun 18 2008 Lucian Langa <cooly@gnome.eu.org> - 0.3.2-2
- Added xinetd config file

* Mon Jun 16 2008 Lucian Langa <cooly@gnome.eu.org> - 0.3.2-1
- Initial spec file


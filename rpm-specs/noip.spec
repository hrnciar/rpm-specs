Name:		noip
Version:	2.1.9
Release:	29%{?dist}
Summary:	A dynamic DNS update client
License:	GPLv2+
URL:		http://www.no-ip.com
Source0:	http://www.no-ip.com/client/linux/noip-duc-linux.tar.gz
Source1:	noip.service
# Patch for Fedora specifics 
Patch0:		noip.patch

Requires(pre):		shadow-utils
%{?systemd_requires}
BuildRequires: systemd
BuildRequires: gcc

%description
Keep your current IP address in sync with your No-IP host or domain with 
this Dynamic Update Client (DUC). The client continually checks for IP 
address changes in the background and automatically updates the DNS at 
No-IP whenever it changes.

N.B. You need to run
	%# noip2 -C
before starting the service.

%prep
%setup -q -n %{name}-%{version}-1
%patch0 -p1
sed -i 's|@OPTFLAGS@|%{optflags}|g;s|@SBINDIR@|%{buildroot}%{_sbindir}|g;s|@SYSCONFDIR@|%{buildroot}%{_sysconfdir}|g' Makefile

%build
make %{?_smp_mflags}

%install
install -D -p -m 755 noip2 %{buildroot}/%{_sbindir}/noip2

# Make dummy config file 
mkdir -p %{buildroot}/%{_sysconfdir}
touch %{buildroot}/%{_sysconfdir}/no-ip2.conf

install -Dm644  %{SOURCE1} %{buildroot}%{_unitdir}/noip.service
# Install init script
#install -D -p -m 755 redhat.noip.sh %{buildroot}%{_initrddir}/noip

%pre
# Add noip user & group
getent group noip >/dev/null || groupadd -r noip
getent passwd noip >/dev/null || \
	useradd -r -g noip -d /var/run/noip -s /sbin/nologin \
	-c "No-ip daemon user" noip

%post
%systemd_post noip.service

%preun
%systemd_preun noip.service

%postun
%systemd_postun_with_restart noip.service

%files
%doc COPYING README.FIRST
%{_sbindir}/noip2
%attr(600,noip,noip) %config(noreplace) %{_sysconfdir}/no-ip2.conf
%{_unitdir}/noip.service

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.9-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.9-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.9-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.9-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild
- https://fedoraproject.org/wiki/Changes/Remove_GCC_from_BuildRoot

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.9-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.9-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.9-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Apr 23 2017 Sérgio Basto <sergio@serjux.com> - 2.1.9-22
- Try to fix issues on startup (#1431368)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.9-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Aug 23 2016 Sérgio Basto <sergio@serjux.com> - 2.1.9-20
- More improvements of systemd service

* Tue Aug 16 2016 Sérgio Basto <sergio@serjux.com> - 2.1.9-19
- Improvement of systemd service, based on
  https://bbs.archlinux.org/viewtopic.php?pid=1541224#p1541224

* Wed Aug 10 2016 Sérgio Basto <sergio@serjux.com> - 2.1.9-18
- Add Packaging:Systemd

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.9-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.9-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.9-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.9-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.9-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.9-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.9-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Dec 10 2010 Jussi Lehtola <jussilehtola@fedoraproject.org> - 2.1.9-8
- Drop unnecessary dir in /var/run.

* Fri Mar 12 2010 Jussi Lehtola <jussilehtola@fedoraproject.org> - 2.1.9-7
- Remove trailing space that caused %%pre scriptlet to fail.

* Sun Jan 10 2010 Jussi Lehtola <jussilehtola@fedoraproject.org> - 2.1.9-6
- Bump release.

* Sat Sep 26 2009 Jussi Lehtola <jussilehtola@fedoraproject.org> - 2.1.9-5
- Remove exit statement from %%pre.

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Mar 14 2009 Jussi Lehtola <jussilehtola@fedoraproject.org> - 2.1.9-3
- Fix initrd file.

* Thu Nov 27 2008 Jussi Lehtola <jussilehtola@fedoraproject.org> - 2.1.9-2
- Add forgotten init file patch.

* Tue Nov 25 2008 Jussi Lehtola <jussilehtola@fedoraproject.org> - 2.1.9-1
- Update to 2.1.9.

* Thu Nov 06 2008 Jussi Lehtola <jussilehtola@fedoraproject.org> - 2.1.7-1
- First release.

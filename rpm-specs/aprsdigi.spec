Name:           aprsdigi
Version:        3.5.1
Release:        16%{?dist}
Summary:        AX.25 Automatic Position Reporting System

License:        GPLv2
URL:            https://github.com/n2ygk/aprsdigi/releases
Source0:        https://github.com/n2ygk/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  libax25-devel
BuildRequires:  systemd
Requires:       kernel-modules-extra
Requires:       ax25-tools
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

%description
Aprsdigi is a specialized Amateur Packet Radio (AX.25) UI-frame digipeater for
the Automatic Position Reporting Systems, APRS(tm). It uses the Linux kernel
AX.25 network stack as well as the SOCK_PACKET facility to listen for packets
on one or more radio interfaces (ports) and repeat those packets -- with
several possible modifications -- on the same or other interfaces. Aprsdigi can
also use the Internet to tunnel connections among other APRS digipeaters and
nodes using IPv4 or IPv6 UDP unicast or multicast.


%prep
%autosetup


%build
%configure
%make_build


%install
%make_install

install -D -m 644 aprsdigi.service %{buildroot}%{_unitdir}/aprsdigi.service
install -D -m 644 aprsbeacon.service %{buildroot}%{_unitdir}/aprsbeacon.service
install -D -m 644 aprsdigi.logrotate %{buildroot}%{_sysconfdir}/logrotate.d/aprsdigi

# Create empty conf file directing the user where to look
mkdir -p %{buildroot}%{_sysconfdir}/ax25
echo > %{buildroot}%{_sysconfdir}/ax25/%{name}.conf << EOL
# See the following %{name} documentation for settings that belong here:
# README.examples
# aprsdigi.conf
EOL


%post
%systemd_post aprsdigi.service
%systemd_post aprsbeacon.service

%preun
%systemd_preun aprsdigi.service
%systemd_preun aprsbeacon.service

%postun
%systemd_postun_with_restart aprsdigi.service 
%systemd_postun_with_restart aprsbeacon.service 


%files
%doc AUTHORS ChangeLog NEWS README TODO *.html examples
%license COPYING
%{_sbindir}/aprsdigi
%{_sbindir}/aprsmon
%{_mandir}/man8/*
%{_unitdir}/aprsbeacon.service
%{_unitdir}/aprsdigi.service
%{_sysconfdir}/ax25/
%config(noreplace) %{_sysconfdir}/ax25/%{name}.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/aprsdigi


%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Oct 30 2015 Richard Shaw <hobbes1069@gmail> - 3.5.1-6
- Rebuild for updated libax25.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Jan 27 2014 Richard Shaw <hobbes1069@gmail.com> - 3.5.1-2
- Created dummy aprsdigi.conf file which points to documentation.
- Added ax25-tools as a requirement.
- Mark config files appropriately so they don't get overwritten on update.

* Thu Oct  3 2013 Richard Shaw <hobbes1069@gmail.com> - 3.5.1-1
- Initial packaging.

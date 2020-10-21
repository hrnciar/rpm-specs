%global realversion 1.0.23-9

Name:           udpxy
Version:        1.0.23
Release:        13%{?dist}
Summary:        UDP-to-HTTP multicast traffic relay daemon

License:        GPLv3+
URL:            http://www.udpxy.com
Source0:        http://www.udpxy.com/download/1_23/%{name}.%{realversion}-prod.tar.gz
Source1:        udpxy.service

BuildRequires:  gcc
BuildRequires:  systemd
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

%description
udpxy is a UDP-to-HTTP multicast traffic relay daemon:
it forwards UDP traffic from a given multicast subscription
to the requesting HTTP client.

%prep
%setup -q -n %{name}-%{realversion}

sed -i 's|@cp $(UDPXREC)|@cp -a $(UDPXREC)|g' Makefile

%build
make %{?_smp_mflags} CPPFLAGS="%{optflags}" rdebug


%install
make DESTDIR=%{buildroot} PREFIX=%{_prefix} install

install -D -p -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service

%post
%systemd_post udpxy.service

%preun
%systemd_preun udpxy.service

%postun
%systemd_postun_with_restart udpxy.service


%files
%doc README CHANGES gpl.txt
%{_bindir}/%{name}
%{_bindir}/udpxrec
%{_mandir}/man1/%{name}.1.gz
%{_mandir}/man1/udpxrec.1.gz
%{_unitdir}/%{name}.service


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.23-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.23-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.23-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.23-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.23-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.23-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.23-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.23-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.23-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.23-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.23-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 29 2014 Alexey Kurov <nucleo@fedoraproject.org> - 1.0.23-1
- udpxy 1.0.23-9

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.21-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.21-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.21-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Aug 24 2012 Alexey Kurov <nucleo@fedoraproject.org> - 1.0.21-4
- Introduce new systemd-rpm macros (#850349)

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.21-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Nov 25 2011 Alexey Kurov <nucleo@fedoraproject.org> - 1.0.21-1
- udpxy 1.0-Chipmunk-build21

* Mon Jun 20 2011 Alexey Kurov <nucleo@fedoraproject.org> - 1.0.20-1
- udpxy 1.0-Chipmunk-BLD20

* Sun May 22 2011 Alexey Kurov <nucleo@fedoraproject.org> - 1.0.19-1
- udpxy 1.0-Chipmunk-19
- service disabled by default
- SysV init script replaced with systemd unit
- options from sysconfdir moved to unit file

* Sun Aug  1 2010 Alexey Kurov <nucleo@fedoraproject.org> - 1.0.16-1
- Initial RPM release

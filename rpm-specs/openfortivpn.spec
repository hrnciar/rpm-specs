Name:           openfortivpn
Version:        1.14.1
Release:        1%{?dist}
Summary:        Client for PPP+SSL VPN tunnel services

License:        GPLv3+
URL:            https://github.com/adrienverge/openfortivpn
Source0:        https://github.com/adrienverge/openfortivpn/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  gcc autoconf automake
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(systemd)
Requires:       ppp

%description
openfortivpn is a client for PPP+SSL VPN tunnel services. It spawns a pppd
process and operates the communication between the gateway and this process.

It is compatible with Fortinet VPNs.


%prep
%setup -q


%build
autoreconf -fi
%configure --with-resolvconf=DISABLED --disable-resolvconf
make %{?_smp_mflags} V=1


%install
%make_install


%files
%{_bindir}/openfortivpn
%{_mandir}/man1/openfortivpn.1*
%{_datadir}/openfortivpn
%{_unitdir}/openfortivpn@.service
%dir %{_sysconfdir}/openfortivpn
%config(noreplace) %{_sysconfdir}/openfortivpn/config
%doc README.md
%license LICENSE LICENSE.OpenSSL


%changelog
* Mon Jun 01 2020 Adrien Vergé <adrienverge@gmail.com> - 1.14.1-1
- Update to latest upstream version
- Switch build requirements xyz-devel to pkgconfig(xyz)
- Add missing LICENSE.OpenSSL license file
- Package systemd service file

* Mon Apr 06 2020 Dimitri Papadopoulos <dpo@sfr.fr> - 1.13.3-1
- Update to latest upstream version
- Re-enable systemd

* Mon Mar 23 2020 Adrien Vergé <adrienverge@gmail.com> - 1.13.1-1
- Update to latest upstream version

* Wed Feb 26 2020 Adrien Vergé <adrienverge@gmail.com> - 1.12.0-1
- Update to latest upstream version

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 28 2019 Adrien Vergé <adrienverge@gmail.com> - 1.11.0-1
- Update to latest upstream version

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 16 2019 Lubomir Rintel <lkundrak@v3.sk> - 1.10.0-1
- Update to latest upstream version

* Wed Mar 20 2019 Lubomir Rintel <lkundrak@v3.sk> - 1.9.0-3
- Add pinentry support

* Wed Mar 20 2019 Lubomir Rintel <lkundrak@v3.sk> - 1.9.0-2
- Fix operations with the NetworkManager plugin

* Wed Mar 20 2019 Lubomir Rintel <lkundrak@v3.sk> - 1.9.0-1
- Update to latest upstream version

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Dec 16 2018 Adrien Vergé <adrienverge@gmail.com> - 1.8.1-1
- Update to latest upstream version

* Tue Dec 11 2018 Adrien Vergé <adrienverge@gmail.com> - 1.8.0-1
- Update to latest upstream version

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 21 2018 Adrien Vergé <adrienverge@gmail.com> - 1.6.0-2
- Add gcc to BuildRequires

* Wed Feb 21 2018 Lubomir Rintel <lkundrak@v3.sk> - 1.6.0-1
- Update to latest upstream version

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Aug 29 2017 Lubomir Rintel <lkundrak@v3.sk> - 1.5.0-1
- Update to latest upstream version

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Feb 7 2017 Adrien Vergé <adrienverge@gmail.com> - 1.3.0-2
- Fix compiler error, see https://github.com/adrienverge/openfortivpn/issues/81

* Tue Feb 7 2017 Adrien Vergé <adrienverge@gmail.com> - 1.3.0-1
- Update to latest upstream version

* Thu Sep 29 2016 Adrien Vergé <adrienverge@gmail.com> - 1.2.0-1
- Update to latest upstream version

* Sun Feb 14 2016 Adrien Vergé <adrienverge@gmail.com> - 1.1.4-1
- Update to latest upstream version

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Dec 26 2015 Adrien Vergé <adrienverge@gmail.com> - 1.1.3-1
- Update to latest upstream version

* Sat Dec 05 2015 Adrien Vergé <adrienverge@gmail.com> - 1.1.2-1
- Update to latest upstream version

* Mon Oct 05 2015 Lubomir Rintel <lkundrak@v3.sk> - 1.1.0-1
- Update to a new upstream release

* Fri Sep 18 2015 Lubomir Rintel <lkundrak@v3.sk> - 1.0.1-2.20150918gita31c599
- Update to latest pristine sources:
- Improve HTTP buffering
- Fix SSL verification

* Wed Sep 16 2015 Lubomir Rintel <lkundrak@v3.sk> - 1.0.1-2.20150914gitb22d9eb
- Mark configuration file as noreplace (Christopher Meng, #1263008)

* Mon Sep 14 2015 Lubomir Rintel <lkundrak@v3.sk> - 1.0.1-1.20150914gitb22d9eb
- Initial packaging

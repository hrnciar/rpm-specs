Name:       tlssled
Version:    1.3
Release:    17%{?dist}
Summary:    An evaluation tool for SSL/TLS (HTTPS) web server implementations

License:    GPLv3+
URL:        http://www.taddong.com/en/lab.html
Source:     http://www.taddong.com/tools/TLSSLed_v%{version}.sh
Patch0:     tlssled-preferred.patch
BuildArch:  noarch

Requires:   sslscan%{?_isa}
Requires:   openssl%{?_isa}

%description
TLSSLed is a Linux shell script whose purpose is to evaluate the security of
a target SSL/TLS (HTTPS) web server implementation. It is based on sslscan, a
thorough SSL/TLS scanner that is based on the openssl library, and on the
"openssl s_client" command line tool. The current tests include checking if
the target supports the SSLv2 protocol, the NULL cipher, weak ciphers based
on their key length (40 or 56 bits), the availability of strong ciphers
(like AES), if the digital certificate is MD5 signed, and the current SSL/TLS
renegotiation capabilities.

%prep
#%patch0 -p1 -b .perferred -R

%build
# nothing to build

%install
install -p -m 0755 -D %{SOURCE0} %{buildroot}%{_bindir}/tlssled
sed -i 's|#!/usr/bin/env bash|#!/usr/bin/bash|g' %{buildroot}%{_bindir}/tlssled

%files
%{_bindir}/%{name}

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Mar 30 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.3-16
- Fix FTBFS (rhbz#1800200)

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 03 2019 Fabian Affolter <mail@fabian-affolter.ch> - 1.3-14
- Add patch (rhbz#1740729)

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Nov 11 2014 Fabian Affolter <mail@fabian-affolter.ch> - 1.3-5
- Add isa

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 04 2014 Fabian Affolter <mail@fabian-affolter.ch> - 1.3-3
- Update shebang
- Again spaces

* Thu Feb 27 2014 Fabian Affolter <mail@fabian-affolter.ch> - 1.3-2
- Preserve time stamp
- Only spaces

* Wed Feb 26 2014 Fabian Affolter <mail@fabian-affolter.ch> - 1.3-1
- Initial spec for Fedora

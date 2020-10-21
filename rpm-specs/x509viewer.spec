Summary:          Simple tool to decode X.509 certificates
Name:             x509viewer
Version:          0.1.0
Release:          8%{?dist}
License:          GPLv2+
URL:              https://ftp.robert-scheck.de/linux/%{name}/
Source:           https://ftp.robert-scheck.de/linux/%{name}/%{name}-%{version}.tar.gz
Requires:         %{_bindir}/openssl
BuildRequires:    perl-generators
BuildArch:        noarch

%description
x509viewer is a simple command line application, written in Perl, that can be
used to decode one or multiple X.509 certificates per given file, such as e.g.
SSL certificates, CSRs (certificate signing requests), but also private keys.

%prep
%setup -q

%build

%install
%make_install

%files
%license COPYING
%doc ChangeLog README
%{_bindir}/%{name}

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Apr 30 2017 Robert Scheck <robert@fedoraproject.org> 0.1.0-1
- Upgrade to 0.1.0
- Initial spec file for Fedora and Red Hat Enterprise Linux

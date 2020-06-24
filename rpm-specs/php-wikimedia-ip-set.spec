
Name:		php-wikimedia-ip-set
Version:	2.1.0
Release:	1%{?dist}
Summary:	Library to match IP addresses against CIDR specifications

License:	GPLv2+
URL:		http://www.mediawiki.org/wiki/IPSet
Source0:	https://github.com/wikimedia/IPSet/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:	noarch

BuildRequires:	php-theseer-autoload

Requires:	php(language) >= 5.3.0
Requires:	php-ctype
Requires:	php-spl

Provides:	php-composer(wikimedia/ip-set) = %{version}


%description
IPSet is a PHP library to match IPs against CIDR specs.


%prep
%setup -q -n IPSet-%{version}


%build
phpab --output src/autoload.php src


%install
mkdir -pm 0755 %{buildroot}%{_datadir}/php/IPSet
cp -rp src/* %{buildroot}%{_datadir}/php/IPSet


%files
%license COPYING
%doc README.md
%{_datadir}/php/IPSet


%changelog
* Thu Mar 05 2020 Michael Cronenworth <mike@cchtml.com> - 2.1.0-1
- version update

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 13 2019 Michael Cronenworth <mike@cchtml.com> - 2.0.1-1
- version update

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 01 2019 Michael Cronenworth <mike@cchtml.com> - 1.3.0-1
- version update

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.20150917git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.20150917git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.20150917git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.20150917git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.20150917git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.20150917git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Sep 17 2015 Michael Cronenworth <mike@cchtml.com> - 0-0.1.20150917git
- Initial package


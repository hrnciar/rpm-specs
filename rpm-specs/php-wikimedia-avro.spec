
Name:		php-wikimedia-avro
Version:	1.9.0
Release:	1%{?dist}
Summary:	A library for using Avro with PHP

License:	ASL 2.0
URL:		https://avro.apache.org/
Source0:        https://github.com/wikimedia/avro-php/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:	noarch

BuildRequires:  php-theseer-autoload

Requires:	php(language) >= 5.3.0
Requires:	php-date
Requires:	php-gmp
Requires:	php-json
Requires:	php-pcre
Requires:	php-spl

Provides:	php-composer(wikimedia/avro) = %{version}


%description
A library for using Apache Avro with PHP. Avro is a data serialization system.


%prep
%setup -n avro-php-%{version}


%build
phpab --output lib/autoload.php lib


%install
mkdir -pm 0755 %{buildroot}%{_datadir}/php/avro
cp -rp lib/* %{buildroot}%{_datadir}/php/avro


%files
%license LICENSE.txt
%doc README.md NOTICE.txt
%{_datadir}/php/avro


%changelog
* Thu Mar 05 2020 Michael Cronenworth <mike@cchtml.com> - 1.9.0-1
- Version update

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 13 2019 Michael Cronenworth <mike@cchtml.com> - 1.8.0-1
- Version update

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Sep 17 2015 Michael Cronenworth <mike@cchtml.com> - 1.7.7-1
- Initial package


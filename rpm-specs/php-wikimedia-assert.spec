Name:		php-wikimedia-assert
Version:	0.2.2
Release:	9%{?dist}
Summary:	An alternative to PHP's assert

License:	MIT
URL:		https://github.com/wmde/Assert
Source0:	https://github.com/wmde/Assert/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:	noarch

BuildRequires:	php-phpunit-PHPUnit
BuildRequires:	php-theseer-autoload

Requires:	php(language) >= 5.3.0
Requires:	php-spl

Provides:	php-composer(wikimedia/assert) = %{version}


%description
This package provides an alternative to PHP's assert() that allows for a
simple and reliable way to check preconditions and postconditions in PHP
code. It was proposed as a MediaWiki RFC, but is completely generic and
can be used by any PHP program or library.


%prep
%setup -qn Assert-%{version}


%build
phpab --output src/autoload.php src


%install
mkdir -pm 0755 %{buildroot}%{_datadir}/php/Wikimedia/Assert
cp -rp src/* %{buildroot}%{_datadir}/php/Wikimedia/Assert


%check
phpunit -v --bootstrap %{buildroot}%{_datadir}/php/Wikimedia/Assert/autoload.php


%files
%license COPYING
%doc composer.json README.md
%{_datadir}/php/Wikimedia


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Oct 05 2015 Michael Cronenworth <mike@cchtml.com> - 0.2.2-1
- Initial package


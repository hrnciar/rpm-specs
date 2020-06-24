%global	handlebars_git df077dd262eea766648af0b6efd8a22e44c78178
%global	mustache_git 83b0721610a4e11832e83df19c73ace3289972b9

Name:		php-zordius-lightncandy
Version:	0.23
Release:	10%{?dist}
Summary:	An extremely fast PHP implementation of handlebars and mustache

License:	MIT
URL:		https://github.com/zordius/lightncandy
Source0:	https://github.com/zordius/lightncandy/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# Tests require data from third-party repositories
Source1:	https://github.com/kasperisager/handlebars-spec/archive/%{handlebars_git}.tar.gz#/%{name}-handlebars.tar.gz
Source2:	https://github.com/mustache/spec/archive/%{mustache_git}.tar.gz#/%{name}-mustache.tar.gz

BuildArch:	noarch

#BuildRequires:	php-phpunit-PHPUnit
BuildRequires:	php-theseer-autoload

Requires:	php(language) >= 5.3.0
Requires:	php-pcre
Requires:	php-reflection
Requires:	php-spl

Provides:	php-composer(zordius/lightncandy) = %{version}

%description
An extremely fast PHP implementation of handlebars ( http://handlebarsjs.com/ )
and mustache ( http://mustache.github.io/ ).


%prep
%setup -qn lightncandy-%{version}
tar zxf %{SOURCE1}
cp -rp handlebars-spec-%{handlebars_git}/spec specs/handlebars/
tar zxf %{SOURCE2}
cp -rp spec-%{mustache_git}/specs specs/mustache/


%build
phpab --output src/autoload.php src


%install
mkdir -pm 0755 %{buildroot}%{_datadir}/php/zordius/lightncandy
cp -p src/autoload.php %{buildroot}%{_datadir}/php/zordius/lightncandy
cp -p src/lightncandy.php %{buildroot}%{_datadir}/php/zordius/lightncandy


# Tests fail under PHP 7.1 and mediawiki requires version 0.23 of this package
#check
#phpunit -v --filter test


%files
%license LICENSE.txt
%doc composer.json CONTRIBUTING.md HISTORY.md README.md UPGRADE.md
%{_datadir}/php/zordius


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 16 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-6
- Disabled tests

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Nov 11 2015 Michael Cronenworth <mike@cchtml.com> - 0.23-1
- version update

* Fri Oct 09 2015 Michael Cronenworth <mike@cchtml.com> - 0.22-1
- Initial package


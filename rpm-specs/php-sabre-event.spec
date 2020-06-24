# remirepo/fedora spec file for php-sabre-event
#
# Copyright (c) 2013-2018 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global gh_commit    337b6f5e10ea6e0b21e22c7e5788dd3883ae73ff
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sabre-io
%global gh_project   event
%global with_tests   %{?_without_tests:0}%{!?_without_tests:1}

Name:           php-sabre-%{gh_project}
Summary:        Lightweight library for event-based programming
Version:        2.0.2
Release:        11%{?dist}

URL:            http://sabre.io/event
License:        BSD
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{name}-%{version}-%{gh_short}.tar.gz
Source1:        %{name}-autoload.php

BuildArch:      noarch
%if %{with_tests}
BuildRequires:  php(language) >= 5.4.1
BuildRequires:  php-composer(phpunit/phpunit)
# Autoloader
BuildRequires:  php-composer(fedora/autoloader)
%endif

# From composer.json, "require": {
#        "php": ">=5.4.1"
Requires:       php(language) >= 5.4.1
# From phpcompatinfo report for version 2.0.2
Requires:       php-spl
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(sabre/event) = %{version}


%description
A lightweight library for event management in PHP.
It's design is inspired by Node.js's EventEmitter. sabre/event requires PHP 5.4.

Autoloader: %{_datadir}/php/Sabre/Event/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}

cp %{SOURCE1} lib/autoload.php


%build
# nothing to build


%install

# Install as a PSR-0 library
mkdir -p %{buildroot}%{_datadir}/php/Sabre
cp -pr lib %{buildroot}%{_datadir}/php/Sabre/Event


%check
%if %{with_tests}
: Run upstream test suite against installed library
%{_bindir}/phpunit \
  --bootstrap=%{buildroot}%{_datadir}/php/Sabre/Event/autoload.php \
  --verbose
%else
: Skip upstream test suite
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc *md
%doc composer.json
%{_datadir}/php/Sabre


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun  5 2018 Remi Collet <remi@remirepo.net> - 2.0.2-7
- fix project URL

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Oct 29 2016 Remi Collet <remi@fedoraproject.org> - 2.0.2-3
- switch from symfony/class-loader to fedora/autoloader

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jul 20 2015 Remi Collet <remi@fedoraproject.org> - 2.0.2-1
- update to 2.0.2
- add autoloader

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 13 2014 Remi Collet <remi@fedoraproject.org> - 1.0.1-1
- update to 1.0.1
- add provides php-composer(sabre/event)
- change url to http://sabre.io/event

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Dec 31 2013 Remi Collet <remi@fedoraproject.org> - 1.0.0-1
- Initial packaging

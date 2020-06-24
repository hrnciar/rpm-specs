# remirepo/fedora spec file for php-solarium
#
# Copyright (c) 2013-2019 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global gh_commit    c353babec89fdbe8c64054bfec8e77bcb5da6705
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     solariumphp
%global gh_project   solarium
%global with_tests   0%{!?_without_tests:1}

Name:           php-%{gh_project}
Summary:        Solarium PHP Solr client library
Version:        3.8.1
Release:        11%{?dist}

URL:            http://www.solarium-project.org/
License:        BSD
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{gh_project}-%{version}-%{gh_short}.tar.gz
Source1:        %{name}-autoload.php

Patch0:         %{name}-php74.patch

BuildArch:      noarch
%if %{with_tests}
# For tests
BuildRequires:  php(language) >= 5.3.2
BuildRequires: (php-composer(symfony/event-dispatcher) > 2.3   with php-composer(symfony/event-dispatcher) < 4)
# From composer.json, "require-dev": {
#        "phpunit/phpunit": "~3.7",
#        "squizlabs/php_codesniffer": "~1.4",
#        "zendframework/zendframework1": "~1.12",
#        "satooshi/php-coveralls": "~1.0",
#        "guzzlehttp/guzzle": "^3.8 || ^6.2"
BuildRequires: (php-composer(guzzlehttp/guzzle)        > 6.2   with php-composer(guzzlehttp/guzzle)       < 7)
BuildRequires:  php-composer(fedora/autoloader)
BuildRequires:  php-composer(phpunit/phpunit) >= 3.7
%endif

# From composer.json, "require": {
#        "php": ">=5.3.2",
#        "symfony/event-dispatcher": "~2.3|~3.0"
Requires:       php(language) >= 5.3.2
Requires:      (php-composer(symfony/event-dispatcher) > 2.3   with php-composer(symfony/event-dispatcher) < 4)
# From composer.json, "suggest": {
#        "minimalcode/search": "Query builder compatible with Solarium, allows simplified solr-query handling"
%if 0%{?fedora}> 21 || 0%{?rhel} >= 8
Suggests:       php-composer(minimalcode/search)
%endif
# From phpcompatinfo report for version 3.7.0
Requires:       php-curl
Requires:       php-date
Requires:       php-json
Requires:       php-pcre
Requires:       php-spl
# php-http optional, and only v1 suppported.
# For our autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(solarium/solarium) = %{version}


%description
Solarium is a PHP Solr client library that accurately model Solr concepts.

Where many other Solr libraries only handle the communication with Solr,
Solarium also relieves you of handling all the complex Solr query parameters
using a well documented API.

Autoloader: %{_datadir}/php/Solarium/autoload.php

Documentation: http://wiki.solarium-project.org/


%prep
%setup -q -n %{gh_project}-%{gh_commit}
%patch0 -p0

rm examples/.gitignore

cp %{SOURCE1} library/Solarium/autoload.php


%build
# nothing to build


%install
mkdir -p %{buildroot}%{_datadir}/php
cp -pr library/Solarium %{buildroot}%{_datadir}/php/Solarium


%check
%if %{with_tests}
: Autoloader
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require_once '%{buildroot}%{_datadir}/php/Solarium/autoload.php';
\Fedora\Autoloader\Dependencies::required(array(
    array(
        '%{_datadir}/php/GuzzleHttp6/autoload.php',
        '%{_datadir}/php/Guzzle/autoload.php',
    ),
));
EOF

: Run upstream test suite against installed library
ret=0
for cmd in php php71 php72 php73 php74; do
   if which $cmd; then
      $cmd %{_bindir}/phpunit || ret=1
   fi
done
exit $ret
%else
: Skip upstream test suite
%endif


%files
%license COPYING
%doc composer.json *.md examples
%{_datadir}/php/Solarium


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct 16 2019 Remi Collet <remi@remirepo.net> - 3.8.1-10
- use range dependency
- add patch for PHP 7.4 from
  https://github.com/solariumphp/solarium/pull/711

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Oct  5 2017 Remi Collet <remi@remirepo.net> - 3.8.1-4
- fix autoloader for Symfony 3, FTBFS from Koschei

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb  2 2017 Remi Collet <remi@fedoraproject.org> - 3.8.1-1
- update to 3.8.1

* Fri Oct 28 2016 Remi Collet <remi@fedoraproject.org> - 3.7.0-1
- update to 3.7.0
- add optional dependency on minimalcode/search
- switch from symfony/class-loader to fedora/autoloader

* Tue May  3 2016 Remi Collet <remi@fedoraproject.org> - 3.6.0-1
- update to 3.6.0
- allow symfony 3

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Dec 26 2015 Remi Collet <remi@fedoraproject.org> - 3.5.1-1
- update to 3.5.1

* Tue Dec 15 2015 Remi Collet <remi@fedoraproject.org> - 3.5.0-1
- update to 3.5.0
- add autoloader
- run test suite with both php 5 and 7 when available

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 15 2015 Remi Collet <remi@fedoraproject.org> - 3.4.1-1
- update to 3.4.1

* Mon Nov 17 2014 Remi Collet <remi@fedoraproject.org> - 3.3.0-1
- update to 3.3.0
- provide php-composer(solarium/solarium)
- fix license handling
- don't run test suite with php 5.3 (EL-6)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Apr  6 2014 Remi Collet <remi@fedoraproject.org> - 3.2.0-1
- update to 3.2.0

* Sat Dec 28 2013 Remi Collet <remi@fedoraproject.org> - 3.1.2-2
- cleanups from review #1023879

* Mon Oct 28 2013 Remi Collet <remi@fedoraproject.org> - 3.1.2-1
- Initial packaging

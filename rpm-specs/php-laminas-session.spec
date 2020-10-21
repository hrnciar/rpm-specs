# remirepo/Fedora spec file for php-laminas-session
#
# Copyright (c) 2015-2020 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global bootstrap    0
%global gh_commit    519e8966146536cd97c1cc3d59a21b095fb814d7
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     laminas
%global gh_project   laminas-session
%global zf_name      zend-session
%global php_home     %{_datadir}/php
%global namespace    Laminas
%global library      Session
%if %{bootstrap}
%global with_tests   0%{?_with_tests:1}
%else
%global with_tests   0%{!?_without_tests:1}
%endif

Name:           php-%{gh_project}
Version:        2.9.3
Release:        2%{?dist}
Summary:        %{namespace} Framework %{library} component

License:        BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{gh_commit}/%{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
# Tests
%if %{with_tests}
BuildRequires:  php(language) >= 5.6
BuildRequires:  php-date
BuildRequires:  php-hash
BuildRequires:  php-pcre
BuildRequires:  php-session
BuildRequires:  php-spl
BuildRequires: (php-autoloader(%{gh_owner}/laminas-eventmanager)         >= 3.0     with php-autoloader(%{gh_owner}/laminas-eventmanager)         < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-stdlib)               >= 3.2.1   with php-autoloader(%{gh_owner}/laminas-stdlib)               < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.0     with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
# From composer, "require-dev": {
#        "container-interop/container-interop": "^1.1",
#        "laminas/laminas-cache": "^2.6.1",
#        "laminas/laminas-coding-standard": "~1.0.0",
#        "laminas/laminas-db": "^2.7",
#        "laminas/laminas-http": "^2.5.4",
#        "laminas/laminas-servicemanager": "^2.7.5 || ^3.0.3",
#        "laminas/laminas-validator": "^2.6",
#        "mongodb/mongodb": "^1.0.1",
#        "php-mock/php-mock-phpunit": "^1.1.2 || ^2.0",
#        "phpunit/phpunit": "^5.7.27 || ^6.5.14 || ^7.5.20"
BuildRequires: (php-composer(container-interop/container-interop)        >= 1.1    with php-composer(container-interop/container-interop)         < 2)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-cache)                >= 2.6.1  with php-autoloader(%{gh_owner}/laminas-cache)                 < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-db)                   >= 2.7    with php-autoloader(%{gh_owner}/laminas-db)                    < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-http)                 >= 2.5.4  with php-autoloader(%{gh_owner}/laminas-http)                  < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-servicemanager)       >= 3.0.3 with php-autoloader(%{gh_owner}/laminas-servicemanager)        < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-validator)            >= 2.6    with php-autoloader(%{gh_owner}/laminas-validator)             < 3)
BuildRequires:   phpunit7 >= 7.5.20
BuildRequires:   php-mock-phpunit2 >= 2.1.0
%endif
# Autoloader
BuildRequires:   php-fedora-autoloader-devel

# From composer, "require": {
#        "php": "^5.6 || ^7.0",
#        "laminas/laminas-eventmanager": "^2.6.2 || ^3.0",
#        "laminas/laminas-stdlib": "^3.2.1",
#        "laminas/laminas-zendframework-bridge": "^1.0"
Requires:       php(language) >= 5.6
%if ! %{bootstrap}
Requires:      (php-autoloader(%{gh_owner}/laminas-eventmanager)         >= 3.0     with php-autoloader(%{gh_owner}/laminas-eventmanager)         < 4)
Requires:      (php-autoloader(%{gh_owner}/laminas-stdlib)               >= 3.2.1   with php-autoloader(%{gh_owner}/laminas-stdlib)               < 4)
Requires:      (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.0     with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
# From composer, "suggest": {
#        "laminas/laminas-cache": "Laminas\\Cache component",
#        "laminas/laminas-db": "Laminas\\Db component",
#        "laminas/laminas-http": "Laminas\\Http component",
#        "laminas/laminas-servicemanager": "Laminas\\ServiceManager component",
#        "laminas/laminas-validator": "Laminas\\Validator component",
#        "mongodb/mongodb": "If you want to use the MongoDB session save handler"
Suggests:       php-autoloader(%{gh_owner}/laminas-cache)
Suggests:       php-autoloader(%{gh_owner}/laminas-db)
Suggests:       php-autoloader(%{gh_owner}/laminas-http)
Suggests:       php-autoloader(%{gh_owner}/laminas-servicemanager)
Suggests:       php-autoloader(%{gh_owner}/laminas-validator)
Suggests:       php-composer(mongodb/mongodb)
%endif
# Autoloader
Requires:       php-composer(fedora/autoloader)
# From phpcompatinfo report for version 2.9.1
Requires:       php-date
Requires:       php-hash
Requires:       php-pcre
Requires:       php-session
Requires:       php-spl

# Compatibily ensure by the bridge
Obsoletes:      php-zendframework-%{zf_name}              < 2.9.2
Provides:       php-zendframework-%{zf_name}              = %{version}
Provides:       php-composer(%{gh_owner}/%{gh_project})   = %{version}
Provides:       php-composer(zendframework/%{zf_name})    = %{version}
Provides:       php-autoloader(%{gh_owner}/%{gh_project}) = %{version}
Provides:       php-autoloader(zendframework/%{zf_name})  = %{version}


%description
%{namespace}\Session is a component to manage PHP session using an object
oriented interface.

Documentation: https://docs.laminas.dev/%{gh_project}/


%prep
%setup -q -n %{gh_project}-%{gh_commit}

mv LICENSE.md LICENSE


%build
: Generate autoloader
phpab --template fedora --output src/autoload.php src
cat << 'EOF' | tee -a src/autoload.php
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/%{namespace}/EventManager/autoload.php',
    '%{php_home}/%{namespace}/Stdlib/autoload.php',
]);
\Fedora\Autoloader\Dependencies::optional([
    '%{php_home}/MongoDB/autoload.php',
    '%{php_home}/%{namespace}/Cache/autoload.php',
    '%{php_home}/%{namespace}/Db/autoload.php',
    '%{php_home}/%{namespace}/Http/autoload.php',
    '%{php_home}/%{namespace}/ServiceManager/autoload.php',
    '%{php_home}/%{namespace}/Validator/autoload.php',
]);
EOF

cat << 'EOF' | tee zf.php
<?php
require_once '%{php_home}/Fedora/Autoloader/autoload.php';
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/%{namespace}/ZendFrameworkBridge/autoload.php',
    dirname(dirname(__DIR__)) . '/%{namespace}/%{library}/autoload.php',
 ]);
EOF


%install
: Laminas library
mkdir -p   %{buildroot}%{php_home}/%{namespace}/
cp -pr src %{buildroot}%{php_home}/%{namespace}/%{library}

: Zend equiv
mkdir -p      %{buildroot}%{php_home}/Zend/%{library}
cp -pr zf.php %{buildroot}%{php_home}/Zend/%{library}/autoload.php


%check
%if %{with_tests}
# this test requires a running MongoDB server
rm test/SaveHandler/MongoDBTest.php

mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require_once '%{buildroot}%{php_home}/%{namespace}/%{library}/autoload.php';
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/phpmock2/phpunit/autoload.php',
]);
\Fedora\Autoloader\Autoload::addPsr4('%{namespace}Test\\%{library}\\', dirname(__DIR__) . '/test');
require_once __DIR__ . '/../test/autoload.php';
EOF

: check compat autoloader
php -r '
require "%{buildroot}%{php_home}/Zend/%{library}/autoload.php";
exit (class_exists("\\Zend\\%{library}\\Container") ? 0 : 1);
'

: upstream test suite
# Need investifation: testResumeSessionThatFailsAValidatorShouldRaiseException (ok for ZF)
ret=0
for cmd in php php72 php73 php74; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit7 \
      --filter '^((?!(testResumeSessionThatFailsAValidatorShouldRaiseException)).)*$' \
      --verbose || ret=1
  fi
done
exit $ret
%else
: Test suite disabled
%endif


%files
%license LICENSE
%doc *.md
%doc composer.json
%{php_home}/Zend/%{library}
%{php_home}/%{namespace}/%{library}


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Mar 30 2020 Remi Collet <remi@remirepo.net> - 2.9.3-1
- update to 2.9.3 (no change)

* Fri Mar  6 2020 Remi Collet <remi@remirepo.net> - 2.9.2-1
- update to 2.9.2

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 14 2020 Remi Collet <remi@remirepo.net> - 2.9.1-1
- switch to Laminas

* Tue Oct 29 2019 Remi Collet <remi@remirepo.net> - 2.9.1-1
- update to 2.9.1

* Mon Sep 23 2019 Remi Collet <remi@remirepo.net> - 2.9.0-1
- update to 2.9.0
- raise dependency on zend-stdlib >= 3.2.1
- switch to phpunit7

* Fri Sep 20 2019 Remi Collet <remi@remirepo.net> - 2.8.7-2
- update to 2.8.7

* Tue Aug 20 2019 Remi Collet <remi@remirepo.net> - 2.8.6-2
- update to 2.8.6

* Thu Dec  6 2018 Remi Collet <remi@remirepo.net> - 2.8.5-3
- cleanup for EL-8

* Fri Mar 23 2018 Remi Collet <remi@remirepo.net> - 2.8.5-2
- switch to phpunit6 and php-mock2

* Fri Feb 23 2018 Remi Collet <remi@remirepo.net> - 2.8.5-1
- Update to 2.8.5 (no change)
- use range dependencies on F27+

* Thu Feb  1 2018 Remi Collet <remi@remirepo.net> - 2.8.4-1
- Update to 2.8.4

* Mon Dec 11 2017 Remi Collet <remi@remirepo.net> - 2.8.3-2
- switch from zend-loader to fedora/autoloader

* Mon Dec  4 2017 Remi Collet <remi@remirepo.net> - 2.8.3-1
- Update to 2.8.3

* Thu Nov 30 2017 Remi Collet <remi@remirepo.net> - 2.8.2-1
- Update to 2.8.2
- only use PHPUnit 5 and php-mock-phpunit v1
  as PHPUnit 6 requires php-mock-phpunit v2 not available

* Wed Nov 29 2017 Remi Collet <remi@remirepo.net> - 2.8.1-1
- Update to 2.8.1

* Wed Nov  8 2017 Remi Collet <remi@remirepo.net> - 2.8.0-3
- fix FTBFS from Koschei, ignore 1 test with PHP 7.2

* Tue Jun 20 2017 Remi Collet <remi@remirepo.net> - 2.8.0-1
- Update to 2.8.0
- raise dependency on PHP 5.6
- use phpunit6 on F26+

* Wed Nov 30 2016 Remi Collet <remi@fedoraproject.org> - 2.7.3-2
- fix FTBFS, ignore failed test with PHP 7.1
  open https://github.com/zendframework/zend-session/issues/68

* Wed Jul  6 2016 Remi Collet <remi@fedoraproject.org> - 2.7.3-1
- update to 2.7.3

* Sat Jun 25 2016 Remi Collet <remi@fedoraproject.org> - 2.7.2-1
- update to 2.7.2

* Wed May 11 2016 Remi Collet <remi@fedoraproject.org> - 2.7.1-1
- update to 2.7.1

* Tue Apr 12 2016 Remi Collet <remi@fedoraproject.org> - 2.7.0-1
- update to 2.7.0
- add optional dependency on mongodb/mongodb

* Fri Feb 26 2016 Remi Collet <remi@fedoraproject.org> - 2.6.2-1
- update to 2.6.2

* Wed Feb 24 2016 Remi Collet <remi@fedoraproject.org> - 2.6.1-1
- update to 2.6.1

* Tue Feb 23 2016 Remi Collet <remi@fedoraproject.org> - 2.6.0-1
- update to 2.6.0
- raise dependency on zend-eventmanager >= 2.6.2
- raise dependency on zend-stdlib >= 2.7

* Tue Aug  4 2015 Remi Collet <remi@fedoraproject.org> - 2.5.2-1
- initial package

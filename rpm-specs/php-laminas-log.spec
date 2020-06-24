# remirepo/Fedora spec file for php-laminas-log
#
# Copyright (c) 2015-2020 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global bootstrap    0
%global gh_commit    4e92d841b48868714a070b10866e94be80fc92ff
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     laminas
%global gh_project   laminas-log
%global zf_name      zend-log
%global php_home     %{_datadir}/php
%global namespace    Laminas
%global library      Log
%if %{bootstrap}
%global with_tests   0%{?_with_tests:1}
%else
%global with_tests   0%{!?_without_tests:1}
%endif

Name:           php-%{gh_project}
Version:        2.12.0
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
BuildRequires:  php-ctype
BuildRequires:  php-date
BuildRequires:  php-dom
BuildRequires:  php-json
BuildRequires:  php-pcre
BuildRequires:  php-spl
BuildRequires: (php-autoloader(%{gh_owner}/laminas-servicemanager)       >= 3.0.3   with php-autoloader(%{gh_owner}/laminas-servicemanager)       < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-stdlib)               >= 3.0     with php-autoloader(%{gh_owner}/laminas-stdlib)               < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.0     with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
BuildRequires: (php-composer(psr/log)                                    >= 1.1.2   with php-composer(psr/log)                                    < 2)
# From composer, "require-dev": {
#        "laminas/laminas-coding-standard": "~1.0.0",
#        "laminas/laminas-db": "^2.6",
#        "laminas/laminas-escaper": "^2.5",
#        "laminas/laminas-filter": "^2.5",
#        "laminas/laminas-mail": "^2.6.1",
#        "laminas/laminas-validator": "^2.10.1",
#        "mikey179/vfsstream": "^1.6.7",
#        "phpunit/phpunit": "^5.7.27 || ^6.5.14 || ^7.5.15"
BuildRequires: (php-autoloader(%{gh_owner}/laminas-db)                   >= 2.6     with php-autoloader(%{gh_owner}/laminas-db)                   < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-escaper)              >= 2.5     with php-autoloader(%{gh_owner}/laminas-escaper)              < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-filter)               >= 2.5     with php-autoloader(%{gh_owner}/laminas-filter)               < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-mail)                 >= 2.6.1   with php-autoloader(%{gh_owner}/laminas-mail)                 < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-validator)            >= 2.10.1  with php-autoloader(%{gh_owner}/laminas-validator)            < 3)
BuildRequires: (php-composer(mikey179/vfsstream)                         >= 1.6.6   with php-composer(mikey179/vfsstream)                         < 2)
%global phpunit %{_bindir}/phpunit7
BuildRequires:  phpunit7 >= 7.5.15
# Optional dep
BuildRequires:  php-autoloader(%{gh_owner}/laminas-mime)           >= 2.5
%endif
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer, "require": {
#        "php": "^5.6 || ^7.0",
#        "laminas/laminas-servicemanager": "^2.7.5 || ^3.0.3",
#        "laminas/laminas-stdlib": "^2.7 || ^3.0",
#        "laminas/laminas-zendframework-bridge": "^1.0",
#        "psr/log": "^1.1.2"
Requires:       php(language) >= 5.6
%if ! %{bootstrap}
Requires:      (php-autoloader(%{gh_owner}/laminas-servicemanager)       >= 3.0.3   with php-autoloader(%{gh_owner}/laminas-servicemanager)       < 4)
Requires:      (php-autoloader(%{gh_owner}/laminas-stdlib)               >= 3.0     with php-autoloader(%{gh_owner}/laminas-stdlib)               < 4)
Requires:      (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.0     with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
Requires:      (php-composer(psr/log)                                    >= 1.1.2   with php-composer(psr/log)                                    < 2)
# From composer, "suggest": {
#        "ext-mongo": "mongo extension to use Mongo writer",
#        "ext-mongodb": "mongodb extension to use MongoDB writer",
#        "laminas/laminas-db": "Laminas\\Db component to use the database log writer",
#        "laminas/laminas-escaper": "Laminas\\Escaper component, for use in the XML log formatter",
#        "laminas/laminas-mail": "Laminas\\Mail component to use the email log writer",
#        "laminas/laminas-validator": "Laminas\\Validator component to block invalid log messages"
Suggests:       php-pecl(mongodb)
Suggests:       php-autoloader(%{gh_owner}/laminas-console)
Suggests:       php-autoloader(%{gh_owner}/laminas-db)
Suggests:       php-autoloader(%{gh_owner}/laminas-escaper)
Suggests:       php-autoloader(%{gh_owner}/laminas-mail)
Suggests:       php-autoloader(%{gh_owner}/laminas-validator)
%endif
# Autoloader
Requires:       php-composer(fedora/autoloader)
# From phpcompatinfo report for version 2.12.0
Requires:       php-ctype
Requires:       php-date
Requires:       php-dom
Requires:       php-json
Requires:       php-pcre
Requires:       php-spl
# mongo is optional

# Compatibily ensure by the bridge
Obsoletes:      php-zendframework-%{zf_name}              < 2.12.0-99
Provides:       php-zendframework-%{zf_name}              = %{version}-99
Provides:       php-composer(%{gh_owner}/%{gh_project})   = %{version}
Provides:       php-composer(zendframework/%{zf_name})    = %{version}
Provides:       php-autoloader(%{gh_owner}/%{gh_project}) = %{version}
Provides:       php-autoloader(zendframework/%{zf_name})  = %{version}
Provides:       php-composer(psr/log-implementation) = 1.0.0


%description
%{namespace}\Log is a component for general purpose logging. It supports multiple
log backends, formatting messages sent to the log, and filtering messages
from being logged.

Documentation: https://docs.laminas.dev/%{gh_project}/


%prep
%setup -q -n %{gh_project}-%{gh_commit}

mv LICENSE.md LICENSE


%build
: Create autoloader
phpab --template fedora --output src/autoload.php src
cat << 'EOF' | tee -a src/autoload.php
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/%{namespace}/ServiceManager/autoload.php',
    '%{php_home}/%{namespace}/Stdlib/autoload.php',
    '%{php_home}/Psr/Log/autoload.php',
]);
\Fedora\Autoloader\Dependencies::optional([
    '%{php_home}/%{namespace}/Db/autoload.php',
    '%{php_home}/%{namespace}/Escaper/autoload.php',
    '%{php_home}/%{namespace}/Mail/autoload.php',
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
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require_once '%{buildroot}%{php_home}/%{namespace}/%{library}/autoload.php';
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/org/bovigo/vfs/autoload.php',
    '%{php_home}/%{namespace}/Filter/autoload.php',
]);
\Fedora\Autoloader\Autoload::addPsr4('%{namespace}Test\\%{library}\\', dirname(__DIR__) . '/test');

require __DIR__ . '/../test/Writer/TestAsset/chmod.php';
EOF

# ignore test requiring a MongoDB server
rm test/Writer/MongoDBTest.php

: check compat autoloader
php -r '
require "%{buildroot}%{php_home}/Zend/%{library}/autoload.php";
exit (class_exists("\\Zend\\%{library}\\Logger") ? 0 : 1);
'

: upstream test suite
ret=0
for cmdarg in "php %{phpunit}" php72 php73 php74; do
  if which $cmdarg; then
    set $cmdarg
    $1 ${2:-%{_bindir}/phpunit7} || ret=1
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
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 15 2020 Remi Collet <remi@remirepo.net> - 2.12.0-1
- switch to Laminas

* Fri Jan  3 2020 Remi Collet <remi@remirepo.net> - 2.12.0-2
- update to 2.12.0
- bump dependency on psr/log 1.1.2

* Mon Aug 26 2019 Remi Collet <remi@remirepo.net> - 2.11.0-2
- update to 2.11.0
- use range dependencies
- use phpunit7

* Wed Apr 11 2018 Remi Collet <remi@remirepo.net> - 2.10.0-2
- update to 2.10.0

* Tue Dec 12 2017 Remi Collet <remi@remirepo.net> - 2.9.2-4
- switch from zend-loader to fedora/autoloader

* Tue Oct 24 2017 Remi Collet <remi@remirepo.net> - 2.9.2-3
- fix FTBFS from Koschei, add patch for PHP 7.2 from
  https://github.com/zendframework/zend-log/pull/79

* Mon May 22 2017 Remi Collet <remi@remirepo.net> - 2.9.2-1
- Update to 2.9.2
- use phpunit6 on F26+

* Fri Aug 12 2016 Remi Collet <remi@fedoraproject.org> - 2.9.1-1
- update to 2.9.1

* Thu Jun 23 2016 Remi Collet <remi@fedoraproject.org> - 2.9.0-1
- update to 2.9.0
- provide php-composer(psr/log-implementation)
- raise dependency on PHP 5.6
- suggest mongodb instead of mongo extension

* Fri May 27 2016 Remi Collet <remi@fedoraproject.org> - 2.8.3-1
- update to 2.8.3

* Tue Apr 19 2016 Remi Collet <remi@fedoraproject.org> - 2.8.2-1
- update to 2.8.2

* Thu Apr  7 2016 Remi Collet <remi@fedoraproject.org> - 2.8.1-1
- update to 2.8.1

* Fri Feb 19 2016 Remi Collet <remi@fedoraproject.org> - 2.7.1-1
- update to 2.7.1

* Fri Feb 12 2016 Remi Collet <remi@fedoraproject.org> - 2.7.0-1
- update to 2.7.0
- raise dependency on zend-stdlib >= 2.7
- raise dependency on zend-servicemanager >= 2.7.5

* Thu Jan 28 2016 Remi Collet <remi@fedoraproject.org> - 2.6.0-1
- update to 2.6.0
- add dependency on psr/log

* Tue Aug  4 2015 Remi Collet <remi@fedoraproject.org> - 2.5.2-1
- initial package

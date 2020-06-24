# remirepo/Fedora spec file for php-laminas-db
#
# Copyright (c) 2015-2020 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global bootstrap    0
%global gh_commit    6c4238918b9204db1eb8cafae2c1940d40f4c007
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     laminas
%global gh_project   laminas-db
%global zf_name      zend-db
%global php_home     %{_datadir}/php
%global namespace    Laminas
%global library      Db
%if %{bootstrap}
%global with_tests   0%{?_with_tests:1}
%else
%global with_tests   0%{!?_without_tests:1}
%endif

Name:           php-%{gh_project}
Version:        2.11.3
Release:        1%{?dist}
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
BuildRequires:  php-pcre
BuildRequires:  php-pdo
BuildRequires:  php-spl
BuildRequires: (php-autoloader(%{gh_owner}/laminas-stdlib)               >= 3.0   with php-autoloader(%{gh_owner}/laminas-stdlib)               < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.0   with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
# From composer, "require-dev": {
#        "laminas/laminas-coding-standard": "~1.0.0",
#        "laminas/laminas-eventmanager": "^2.6.2 || ^3.0",
#        "laminas/laminas-hydrator": "^1.1 || ^2.1 || ^3.0",
#        "laminas/laminas-servicemanager": "^2.7.5 || ^3.0.3",
#        "phpunit/phpunit": "^5.7.27 || ^6.5.14"
BuildRequires: (php-autoloader(%{gh_owner}/laminas-eventmanager)         >= 3.0   with php-autoloader(%{gh_owner}/laminas-eventmanager)         < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-hydrator)             >= 2.1   with php-autoloader(%{gh_owner}/laminas-hydrator)             < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-servicemanager)       >= 3.0   with php-autoloader(%{gh_owner}/laminas-servicemanager)       < 4)
%global phpunit %{_bindir}/phpunit6
BuildRequires:  phpunit6 >= 6.5.14
%endif
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer, "require": {
#        "php": "^5.6 || ^7.0",
#        "laminas/laminas-stdlib": "^2.7 || ^3.0",
#        "laminas/laminas-zendframework-bridge": "^1.0"
Requires:       php(language) >= 5.6
%if ! %{bootstrap}
Requires:      (php-autoloader(%{gh_owner}/laminas-stdlib)               >= 3.0   with php-autoloader(%{gh_owner}/laminas-stdlib)               < 4)
Requires:      (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.0   with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
# From composer, "suggest": {
#        "laminas/laminas-eventmanager": "Laminas\\EventManager component",
#        "laminas/laminas-hydrator": "Laminas\\Hydrator component for using HydratingResultSets",
#        "laminas/laminas-servicemanager": "Laminas\\ServiceManager component"
Suggests:       php-autoloader(%{gh_owner}/laminas-eventmanager)
Suggests:       php-autoloader(%{gh_owner}/laminas-hydrator)
Suggests:       php-autoloader(%{gh_owner}/laminas-servicemanager)
%endif
# Autoloader
Requires:       php-composer(fedora/autoloader)
# From phpcompatinfo report for version 2.11.2
Requires:       php-date
Requires:       php-pcre
Requires:       php-pdo
Requires:       php-spl

# Compatibily ensure by the bridge
Obsoletes:      php-zendframework-%{zf_name}              < 2.11.1
Provides:       php-zendframework-%{zf_name}              = %{version}
Provides:       php-composer(%{gh_owner}/%{gh_project})   = %{version}
Provides:       php-composer(zendframework/%{zf_name})    = %{version}
Provides:       php-autoloader(%{gh_owner}/%{gh_project}) = %{version}
Provides:       php-autoloader(zendframework/%{zf_name})  = %{version}


%description
%{namespace}\Db is a component that abstract the access to a Database using an
object oriented API to build the queries. %{namespace}\Db consumes different
storage adapters to access different database vendors such as MySQL,
PostgreSQL, Oracle, IBM DB2, Microsoft Sql Server, PDO, etc.

Documentation: https://docs.laminas.dev/%{gh_project}/


%prep
%setup -q -n %{gh_project}-%{gh_commit}

mv LICENSE.md LICENSE


%build
: Generate autoloader
phpab --template fedora --output src/autoload.php src
cat << 'EOF' | tee -a src/autoload.php
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/%{namespace}/Stdlib/autoload.php',
]);
\Fedora\Autoloader\Dependencies::optional([
    '%{php_home}/%{namespace}/EventManager/autoload.php',
    [
        '%{php_home}/%{namespace}/Hydrator3/autoload.php',
        '%{php_home}/%{namespace}/Hydrator/autoload.php',
    ],
    '%{php_home}/%{namespace}/ServiceManager/autoload.php',
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
# comptibility layer before PSR-0 autoloader
require_once dirname(__DIR__) . '/test/autoload.php';
require_once '%{buildroot}%{php_home}/%{namespace}/%{library}/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('%{namespace}Test\\%{library}\\', dirname(__DIR__) . '/test/unit');
\Fedora\Autoloader\Autoload::addPsr4('%{namespace}IntegrationTest\\%{library}\\', dirname(__DIR__) . '/test/integration');
EOF

: check compat autoloader
php -r '
require "%{buildroot}%{php_home}/Zend/%{library}/autoload.php";
exit (class_exists("\\Zend\\%{library}\\ConfigProvider") ? 0 : 1);
'

: upstream test suite
ret=0
for cmdarg in "php %{phpunit}" php72 php73 php74; do
  if which $cmdarg; then
    set $cmdarg
    $1 ${2:-%{_bindir}/phpunit6} --verbose || ret=1
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
* Mon Mar 30 2020 Remi Collet <remi@remirepo.net> - 2.11.3-1
- update to 2.11.3 (no change)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 14 2020 Remi Collet <remi@remirepo.net> - 2.11.2-1
- switch to Laminas
- update to 2.11.2

* Thu Jan  2 2020 Remi Collet <remi@remirepo.net> - 2.11.0-2
- update to 2.11.0
- drop patch merged upstream
- add patch for PHP 7.4 from
  https://github.com/laminas/laminas-db/pull/32

* Wed Oct  9 2019 Remi Collet <remi@remirepo.net> - 2.10.0-4
- add patch for PHP 7.4 from
  https://github.com/zendframework/zend-db/pull/395

* Mon Feb 25 2019 Remi Collet <remi@remirepo.net> - 2.10.0-1
- update to 2.10.0
- use range dependencies

* Wed Apr 11 2018 Remi Collet <remi@remirepo.net> - 2.9.3-2
- update to 2.9.3
- only use phpunit6

* Tue Dec 12 2017 Remi Collet <remi@remirepo.net> - 2.9.2-1
- Update to 2.9.2

* Mon Dec 11 2017 Remi Collet <remi@remirepo.net> - 2.9.1-2
- switch from zend-loader to fedora/autoloader

* Fri Dec  8 2017 Remi Collet <remi@remirepo.net> - 2.9.1-1
- Update to 2.9.1

* Thu Dec  7 2017 Remi Collet <remi@remirepo.net> - 2.9.0-2
- use phpunit6 on F26+

* Thu Dec  7 2017 Remi Collet <remi@remirepo.net> - 2.9.0-1
- Update to 2.9.0
- raise dependency on PHP 5.6

* Tue Oct 31 2017 Remi Collet <remi@fedoraproject.org> - 2.8.2-4
- fix FTBFS from Koschei, add patch for PHP 7.2
  from https://github.com/zendframework/zend-db/pull/276

* Wed Aug 10 2016 Remi Collet <remi@fedoraproject.org> - 2.8.2-1
- update to 2.8.2

* Thu Apr 14 2016 Remi Collet <remi@fedoraproject.org> - 2.8.1-1
- update to 2.8.1

* Wed Apr 13 2016 Remi Collet <remi@fedoraproject.org> - 2.8.0-1
- update to 2.8.0
- ignore failed tests when no sql server configured
  open https://github.com/zendframework/zend-db/issues/97

* Tue Feb 23 2016 Remi Collet <remi@fedoraproject.org> - 2.7.0-1
- update to 2.7.0

* Thu Jan 28 2016 Remi Collet <remi@fedoraproject.org> - 2.6.2-1
- update to 2.6.2
- rasie dependency on zend-stdlib ~2.7
- add optional dependency on zend-hydrator

* Wed Sep 23 2015 Remi Collet <remi@fedoraproject.org> - 2.5.2-1
- update to 2.5.2
- raise dependency on php 5.5

* Tue Aug  4 2015 Remi Collet <remi@fedoraproject.org> - 2.5.1-1
- initial package

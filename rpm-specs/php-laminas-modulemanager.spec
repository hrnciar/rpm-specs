# remirepo/fedora spec file for php-laminas-modulemanager
#
# Copyright (c) 2015-2020 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
# When build without laminas-mvc
%bcond_with          bootstrap
%bcond_without       tests

%global gh_commit    637aaaf2c85d13694b096e253e5884653f93bb92
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     laminas
%global gh_project   laminas-modulemanager
%global zf_name      zend-modulemanager
%global php_home     %{_datadir}/php
%global namespace    Laminas
%global library      ModuleManager

Name:           php-%{gh_project}
Version:        2.10.1
Release:        1%{?dist}
Summary:        %{namespace} Framework %{library} component

License:        BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{gh_commit}/%{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
# Tests
%if %{with tests}
BuildRequires:  php(language) >= 7.3
BuildRequires:  php-spl
BuildRequires: (php-composer(brick/varexporter)                          >= 0.3.2   with php-composer(brick/varexporter)                          < 1)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-config)               >= 3.4     with php-autoloader(%{gh_owner}/laminas-config)               < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-eventmanager)         >= 3.3     with php-autoloader(%{gh_owner}/laminas-eventmanager)         < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-stdlib)               >= 3.3     with php-autoloader(%{gh_owner}/laminas-stdlib)               < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.1     with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
BuildRequires: (php-composer(webimpress/safe-writer)                     >= 2.1     with php-composer(webimpress/safe-writer)                     < 3)
# From composer, "require-dev": {
#        "laminas/laminas-coding-standard": "~1.0.0",
#        "laminas/laminas-console": "^2.8",
#        "laminas/laminas-di": "^2.6.1",
#        "laminas/laminas-loader": "^2.6.1",
#        "laminas/laminas-mvc": "^3.1.1",
#        "laminas/laminas-servicemanager": "^3.4.1",
#        "phpunit/phpunit": "^9.3.7"
BuildRequires: (php-autoloader(%{gh_owner}/laminas-console)              >= 2.8     with php-autoloader(%{gh_owner}/laminas-console)              < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-di)                   >= 2.6.1   with php-autoloader(%{gh_owner}/laminas-di)                   < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-loader)               >= 2.6.1   with php-autoloader(%{gh_owner}/laminas-loader)               < 3)
%if %{without bootstrap}
BuildRequires: (php-autoloader(%{gh_owner}/laminas-mvc)                  >= 3.1.1     with php-autoloader(%{gh_owner}/laminas-mvc)                < 4)
%endif
BuildRequires: (php-autoloader(%{gh_owner}/laminas-servicemanager)       >= 3.4.1   with php-autoloader(%{gh_owner}/laminas-servicemanager)       < 4)
%global phpunit %{_bindir}/phpunit9
BuildRequires:  phpunit9 >= 9.3.7
%endif
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer, "require": {
#        "php": "^7.3 || ^8.0",
#        "brick/varexporter": "^0.3.2",
#        "laminas/laminas-config": "^3.4",
#        "laminas/laminas-eventmanager": "^3.3",
#        "laminas/laminas-stdlib": "^3.3",
#        "laminas/laminas-zendframework-bridge": "^1.1",
#        "webimpress/safe-writer": "^1.0.2 || ^2.1"
Requires:       php(language) >= 7.3
Requires:      (php-composer(brick/varexporter)                          >= 0.3.2   with php-composer(brick/varexporter)                          < 1)
Requires:      (php-autoloader(%{gh_owner}/laminas-config)               >= 3.4     with php-autoloader(%{gh_owner}/laminas-config)               < 4)
Requires:      (php-autoloader(%{gh_owner}/laminas-eventmanager)         >= 3.3     with php-autoloader(%{gh_owner}/laminas-eventmanager)         < 4)
Requires:      (php-autoloader(%{gh_owner}/laminas-stdlib)               >= 3.3     with php-autoloader(%{gh_owner}/laminas-stdlib)               < 4)
Requires:      (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.1     with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
Requires:      (php-composer(webimpress/safe-writer)                     >= 2.1     with php-composer(webimpress/safe-writer)                     < 3)
# From composer, "suggest": {
#        "laminas/laminas-console": "Laminas\\Console component",
#        "laminas/laminas-loader": "Laminas\\Loader component if you are not using Composer autoloading for your modules",
#        "laminas/laminas-mvc": "Laminas\\Mvc component",
#        "laminas/laminas-servicemanager": "Laminas\\ServiceManager component"
Suggests:       php-autoloader(%{gh_owner}/laminas-console)
Suggests:       php-autoloader(%{gh_owner}/laminas-loader)
Suggests:       php-autoloader(%{gh_owner}/laminas-mvc)
Suggests:       php-autoloader(%{gh_owner}/laminas-servicemanager)
# Autoloader
Requires:       php-composer(fedora/autoloader)
# From phpcompatinfo report for version 2.8.4
Requires:       php-spl

# Compatibily ensure by the bridge
Obsoletes:      php-zendframework-%{zf_name}              < 2.8.5
Provides:       php-zendframework-%{zf_name}              = %{version}
Provides:       php-composer(%{gh_owner}/%{gh_project})   = %{version}
Provides:       php-composer(zendframework/%{zf_name})    = %{version}
Provides:       php-autoloader(%{gh_owner}/%{gh_project}) = %{version}
Provides:       php-autoloader(zendframework/%{zf_name})  = %{version}


%description
%{namespace} Framework introduces a new and powerful approach to modules.
This new module system is designed with flexibility, simplicity, and
re-usability in mind. A module may contain just about anything:
PHP code, including MVC functionality; library code; view scripts;
and/or public assets such as images, CSS, and JavaScript.
The possibilities are endless.

%{namespace}\ModuleManager is the component that enables the design of a module
architecture for PHP applications.

Documentation: https://docs.laminas.dev/%{gh_project}/


%prep
%setup -q -n %{gh_project}-%{gh_commit}

mv LICENSE.md LICENSE


%build
: Create autoloader
phpab --template fedora --output src/autoload.php src
cat << 'EOF' | tee -a src/autoload.php
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/Brick/VarExporter/autoload.php',
    '%{php_home}/%{namespace}/Config3/autoload.php',
    '%{php_home}/%{namespace}/EventManager/autoload.php',
    '%{php_home}/%{namespace}/Stdlib/autoload.php',
    '%{php_home}/Webimpress/SafeWriter/autoload.php',
]);
\Fedora\Autoloader\Dependencies::optional([
    '%{php_home}/%{namespace}/Console/autoload.php',
    '%{php_home}/%{namespace}/Loader/autoload.php',
    '%{php_home}/%{namespace}/Mvc/autoload.php',
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
%if %{with tests}
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require_once '%{buildroot}%{php_home}/%{namespace}/%{library}/autoload.php';
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/%{namespace}/Di/autoload.php',
]);
\Fedora\Autoloader\Autoload::addPsr4('ListenerTestModule', dirname(__DIR__) . '/test/TestAsset/ListenerTestModule');
\Fedora\Autoloader\Autoload::addPsr4('ModuleAsClass', dirname(__DIR__) . '/test/TestAsset/ModuleAsClass');
\Fedora\Autoloader\Autoload::addPsr4('%{namespace}Test\\%{library}\\', dirname(__DIR__) . '/test');
require_once __DIR__ . '/../test/autoload.php';
require_once __DIR__ . '/../test/TestAsset/ModuleAsClass.php';
EOF

: check compat autoloader
php -r '
require "%{buildroot}%{php_home}/Zend/%{library}/autoload.php";
exit (class_exists("\\Zend\\%{library}\\ModuleEvent") ? 0 : 1);
'

: upstream test suite
ret=0
for cmdarg in "php %{phpunit}" php73 php74 php80; do
  if which $cmdarg; then
    set $cmdarg
    $1 ${2:-%{_bindir}/phpunit9} --verbose || ret=1
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
* Wed Sep  2 2020 Remi Collet <remi@remirepo.net> - 2.10.1-1
- update to 2.10.1

* Tue Aug 25 2020 Remi Collet <remi@remirepo.net> - 2.10.0-1
- update to 2.10.0
- raise dependency on PHP 7.3
- add dependency on brick/varexporter
- raise dependency on laminas/laminas-config 3.4
- raise dependency on laminas/laminas-eventmanager 3.3
- raise dependency on laminas/laminas-stdlib 3.3
- raise dependency on laminas/laminas-zendframework-bridge 1.1
- switch to phpunit 9.3

* Tue Aug 25 2020 Remi Collet <remi@remirepo.net> - 2.9.0-1
- update to 2.9.0
- add dependency on webimpress/safe-writer

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 15 2020 Remi Collet <remi@remirepo.net> - 2.8.4-1
- switch to Laminas
- bootstrap build without laminas-mvc

* Mon Oct 28 2019 Remi Collet <remi@remirepo.net> - 2.8.4-1
- update to 2.8.4

* Mon Oct 21 2019 Remi Collet <remi@remirepo.net> - 2.8.3-2
- update to 2.8.3
- switch to phpunit7

* Thu Feb 28 2019 Remi Collet <remi@remirepo.net> - 2.8.2-6
- use range dependencies

* Tue Dec 12 2017 Remi Collet <remi@remirepo.net> - 2.8.2-2
- switch from zend-loader to fedora/autoloader

* Mon Dec  4 2017 Remi Collet <remi@remirepo.net> - 2.8.2-1
- Update to 2.8.2

* Thu Nov  2 2017 Remi Collet <remi@remirepo.net> - 2.8.1-1
- Update to 2.8.1

* Wed Jul 12 2017 Remi Collet <remi@remirepo.net> - 2.8.0-1
- Update to 2.8.0
- raise dependency on PHP 5.6
- use phpunit6 on F26+

* Wed Jul 12 2017 Remi Collet <remi@remirepo.net> - 2.7.3-1
- Update to 2.7.3

* Wed Feb 22 2017 Remi Collet <remi@fedoraproject.org> - 2.7.2-2
- add fix for tests against PHP 7.1, fix FTBFS #1424086
  from https://github.com/zendframework/zend-modulemanager/pull/55

* Tue May 17 2016 Remi Collet <remi@fedoraproject.org> - 2.7.2-1
- update to 2.7.2
- zend-config is now required

* Sun Feb 28 2016 Remi Collet <remi@fedoraproject.org> - 2.7.1-1
- update to 2.7.1
- https://github.com/zendframework/zend-modulemanager/pull/33

* Fri Feb 26 2016 Remi Collet <remi@fedoraproject.org> - 2.7.0-1
- update to 2.7.0
- raise dependency on zend-eventmanager >= 2.6.2

* Thu Jan 28 2016 Remi Collet <remi@fedoraproject.org> - 2.6.1-1
- update to 2.6.1
- raise dependency on zend-stdlib ~2.7

* Thu Sep 10 2015 Remi Collet <remi@fedoraproject.org> - 2.5.3-1
- update to 2.5.3
- raise minimum php version to 5.5

* Tue Aug  4 2015 Remi Collet <remi@fedoraproject.org> - 2.5.1-1
- initial package

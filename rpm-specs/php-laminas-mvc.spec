# remirepo/Fedora spec file for php-laminas-mvc
#
# Copyright (c) 2015-2020 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global bootstrap    0
%global gh_commit    ead09f8ab5ff0e562dbd0198c7f67523c2f61980
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     laminas
%global gh_project   laminas-mvc
%global zf_name      zend-mvc
%global php_home     %{_datadir}/php
%global namespace    Laminas
%global library      Mvc
%if %{bootstrap}
%global with_tests   0%{?_with_tests:1}
%else
%global with_tests   0%{!?_without_tests:1}
%endif

Name:           php-%{gh_project}
Version:        3.1.1
Release:        3%{?dist}
Summary:        %{namespace} Framework %{library} component

License:        BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{gh_commit}/%{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
# Tests
%if %{with_tests}
BuildRequires:  php(language) >= 5.6
BuildRequires:  php-reflection
BuildRequires:  php-json
BuildRequires:  php-pcre
BuildRequires:  php-spl
BuildRequires: (php-composer(container-interop/container-interop)        >= 1.2     with php-composer(container-interop/container-interop)        < 2)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-eventmanager)         >= 3.2     with php-autoloader(%{gh_owner}/laminas-eventmanager)         < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-http)                 >= 2.7     with php-autoloader(%{gh_owner}/laminas-http)                 < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-modulemanager)        >= 2.8     with php-autoloader(%{gh_owner}/laminas-modulemanager)        < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-router)               >= 3.0.2   with php-autoloader(%{gh_owner}/laminas-router)               < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-servicemanager)       >= 3.3     with php-autoloader(%{gh_owner}/laminas-servicemanager)       < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-stdlib)               >= 3.1     with php-autoloader(%{gh_owner}/laminas-stdlib)               < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-view)                 >= 2.9     with php-autoloader(%{gh_owner}/laminas-view)                 < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.0     with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
# from composer.json,  "require-dev": {
#        "http-interop/http-middleware": "^0.4.1",
#        "laminas/laminas-coding-standard": "~1.0.0",
#        "laminas/laminas-json": "^2.6.1 || ^3.0",
#        "laminas/laminas-psr7bridge": "^1.0",
#        "laminas/laminas-stratigility": "^2.0.1",
#        "phpunit/phpunit": "^6.4.4 || ^5.7.14"
BuildRequires: (php-composer(http-interop/http-middleware)               >= 0.4.1   with php-composer(http-interop/http-middleware)               < 1)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-json)                 >= 3.0     with php-autoloader(%{gh_owner}/laminas-json)                 < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-psr7bridge)           >= 1.0     with php-autoloader(%{gh_owner}/laminas-psr7bridge)           < 2)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-stratigility)         >= 2.0.1   with php-autoloader(%{gh_owner}/laminas-stratigility)         < 3)
%global phpunit %{_bindir}/phpunit6
BuildRequires:  phpunit6 >= 6.5
%endif
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer, "require": {
#        "php": "^5.6 || ^7.0",
#        "container-interop/container-interop": "^1.2",
#        "laminas/laminas-eventmanager": "^3.2",
#        "laminas/laminas-http": "^2.7",
#        "laminas/laminas-modulemanager": "^2.8",
#        "laminas/laminas-router": "^3.0.2",
#        "laminas/laminas-servicemanager": "^3.3",
#        "laminas/laminas-stdlib": "^3.1",
#        "laminas/laminas-view": "^2.9",
#        "laminas/laminas-zendframework-bridge": "^1.0"
Requires:       php(language) >= 5.6
Requires:      (php-composer(container-interop/container-interop)        >= 1.2     with php-composer(container-interop/container-interop)        < 2)
Requires:      (php-autoloader(%{gh_owner}/laminas-eventmanager)         >= 3.2     with php-autoloader(%{gh_owner}/laminas-eventmanager)         < 4)
Requires:      (php-autoloader(%{gh_owner}/laminas-http)                 >= 2.7     with php-autoloader(%{gh_owner}/laminas-http)                 < 3)
Requires:      (php-autoloader(%{gh_owner}/laminas-modulemanager)        >= 2.8     with php-autoloader(%{gh_owner}/laminas-modulemanager)        < 3)
Requires:      (php-autoloader(%{gh_owner}/laminas-router)               >= 3.0.2   with php-autoloader(%{gh_owner}/laminas-router)               < 4)
Requires:      (php-autoloader(%{gh_owner}/laminas-servicemanager)       >= 3.3     with php-autoloader(%{gh_owner}/laminas-servicemanager)       < 4)
Requires:      (php-autoloader(%{gh_owner}/laminas-stdlib)               >= 3.1     with php-autoloader(%{gh_owner}/laminas-stdlib)               < 4)
Requires:      (php-autoloader(%{gh_owner}/laminas-view)                 >= 2.9     with php-autoloader(%{gh_owner}/laminas-view)                 < 3)
Requires:      (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.0     with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
# From composer, "suggest": {
#        "http-interop/http-middleware": "^0.4.1 to be used together with laminas-stratigility",
#        "laminas/laminas-json": "(^2.6.1 || ^3.0) To auto-deserialize JSON body content in AbstractRestfulController extensions, when json_decode is unavailable",
#        "laminas/laminas-log": "^2.9.1  To provide log functionality via LogFilterManager, LogFormatterManager, and LogProcessorManager",
#        "laminas/laminas-mvc-console": "laminas-mvc-console provides the ability to expose laminas-mvc as a console application",
#        "laminas/laminas-mvc-i18n": "laminas-mvc-i18n provides integration with laminas-i18n, including a translation bridge and translatable route segments",
#        "laminas/laminas-mvc-plugin-fileprg": "To provide Post/Redirect/Get functionality around forms that container file uploads",
#        "laminas/laminas-mvc-plugin-flashmessenger": "To provide flash messaging capabilities between requests",
#        "laminas/laminas-mvc-plugin-identity": "To access the authenticated identity (per laminas-authentication) in controllers",
#        "laminas/laminas-mvc-plugin-prg": "To provide Post/Redirect/Get functionality within controllers",
#        "laminas/laminas-paginator": "^2.7 To provide pagination functionality via PaginatorPluginManager",
#        "laminas/laminas-psr7bridge": "(^0.2) To consume PSR-7 middleware within the MVC workflow",
#        "laminas/laminas-servicemanager-di": "laminas-servicemanager-di provides utilities for integrating laminas-di and laminas-servicemanager in your laminas-mvc application",
#        "laminas/laminas-stratigility": "laminas-stratigility is required to use middleware pipes in the MiddlewareListener"
Suggests:       php-composer(http-interop/http-middleware)
Suggests:       php-autoloader(%{gh_owner}/laminas-json)
Suggests:       php-autoloader(%{gh_owner}/laminas-log)
Suggests:       php-autoloader(%{gh_owner}/laminas-mvc-console)
Suggests:       php-autoloader(%{gh_owner}/laminas-mvc-i18n)
Suggests:       php-autoloader(%{gh_owner}/laminas-mvc-plugin-fileprg)
Suggests:       php-autoloader(%{gh_owner}/laminas-mvc-plugin-flashmessenger)
Suggests:       php-autoloader(%{gh_owner}/laminas-mvc-plugin-identity)
Suggests:       php-autoloader(%{gh_owner}/laminas-mvc-plugin-prg)
Suggests:       php-autoloader(%{gh_owner}/laminas-paginator)
Suggests:       php-autoloader(%{gh_owner}/laminas-psr7bridge)
Suggests:       php-autoloader(%{gh_owner}/laminas-servicemanager-di)
Suggests:       php-autoloader(%{gh_owner}/laminas-stratigility)
# Autoloader
Requires:       php-composer(fedora/autoloader)
# From phpcompatinfo report for version 3.1.1
Requires:       php-reflection
Requires:       php-json
Requires:       php-pcre
Requires:       php-spl

# Compatibily ensure by the bridge
Obsoletes:      php-zendframework-%{zf_name}              < 3.1.1-99
Provides:       php-zendframework-%{zf_name}              = %{version}-99
Provides:       php-composer(%{gh_owner}/%{gh_project})   = %{version}
Provides:       php-composer(zendframework/%{zf_name})    = %{version}
Provides:       php-autoloader(%{gh_owner}/%{gh_project}) = %{version}
Provides:       php-autoloader(zendframework/%{zf_name})  = %{version}


%description
%{namespace}\Mvc is a brand new MVC implementation designed from the ground up
for %{namespace} Framework, focusing on performance and flexibility.

The MVC layer is built on top of the following components:
* %{namespace}\ServiceManager - %{namespace} Framework provides a set of default service
  definitions set up at %{namespace}\Mvc\Service. The ServiceManager creates and
  configures your application instance and workflow.
* %{namespace}\EventManager - The MVC is event driven. This component is used
  everywhere from initial bootstrapping of the application, through returning
  response and request calls, to setting and retrieving routes and matched
  routes, as well as render views.
* %{namespace}\Http - specifically the request and response objects, used within:
  %{namespace}\Stdlib\DispatchableInterface. All “controllers” are simply
  dispatchable objects.

Documentation: https://docs.laminas.dev/%{gh_project}/


%prep
%setup -q -n %{gh_project}-%{gh_commit}

mv LICENSE.md LICENSE


%build
: Create autoloader
phpab --template fedora --output src/autoload.php src
cat << 'EOF' | tee -a src/autoload.php
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/Interop/Container/autoload.php',
    '%{php_home}/%{namespace}/EventManager/autoload.php',
    '%{php_home}/%{namespace}/Http/autoload.php',
    '%{php_home}/%{namespace}/ModuleManager/autoload.php',
    '%{php_home}/%{namespace}/Router/autoload.php',
    '%{php_home}/%{namespace}/ServiceManager/autoload.php',
    '%{php_home}/%{namespace}/Stdlib/autoload.php',
    '%{php_home}/%{namespace}/View/autoload.php',
]);
\Fedora\Autoloader\Dependencies::optional([
    '%{php_home}/%{namespace}/Json/autoload.php',
    '%{php_home}/%{namespace}/Log/autoload.php',
    '%{php_home}/%{namespace}/Mvc/Console/autoload.php',
    '%{php_home}/%{namespace}/Mvc/I18n/autoload.php',
    '%{php_home}/%{namespace}/Mvc/Plugin/FilePrg/autoload.php',
    '%{php_home}/%{namespace}/Mvc/Plugin/FlashMessenger/autoload.php',
    '%{php_home}/%{namespace}/Mvc/Plugin/Identity/autoload.php',
    '%{php_home}/%{namespace}/Mvc/Plugin/Prg/autoload.php',
    '%{php_home}/%{namespace}/Paginator/autoload.php',
    '%{php_home}/%{namespace}/Psr7Bridge/autoload.php',
    '%{php_home}/%{namespace}/ServiceManager/Di/autoload.php',
    '%{php_home}/%{namespace}/Stratigility/autoload.php',
    '%{php_home}/Interop/Http/Middleware/autoload.php',
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
\Fedora\Autoloader\Autoload::addPsr4('%{namespace}Test\\%{library}\\', dirname(__DIR__) . '/test');
require_once 'test/_autoload.php';
EOF

: check compat autoloader
php -r '
require "%{buildroot}%{php_home}/Zend/%{library}/autoload.php";
exit (class_exists("\\Zend\\%{library}\\Application") ? 0 : 1);
'

: Skip test which raise deprecation warning - stratigility
rm test/MiddlewareListenerTest.php

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
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 15 2020 Remi Collet <remi@remirepo.net> - 3.1.1-1
- switch to Laminas
- use range dependencies

* Tue Dec 12 2017 Remi Collet <remi@remirepo.net> - 3.1.1-2
- switch from zend-loader to fedora/autoloader

* Mon Nov 27 2017 Remi Collet <remi@remirepo.net> - 3.1.1-1
- Update to 3.1.1
- raise dependency on container-interop/container-interop 1.2
- raise dependency on zend-eventmanager 3.2
- raise dependency on zend-http 2.7
- raise dependency on zend-modulemanager 2.8
- raise dependency on zend-router 3.0.2
- raise dependency on zend-servicemanager 3.3
- raise dependency on zend-stdlib 3.1
- raise dependency on zend-view 2.9

* Tue May  2 2017 Remi Collet <remi@remirepo.net> - 3.1.0-1
- Update to 3.1.0
- use phpunit6

* Wed Dec 21 2016 Remi Collet <remi@fedoraproject.org> - 3.0.4-1
- update to 3.0.4

* Fri Sep  2 2016 Remi Collet <remi@fedoraproject.org> - 3.0.3-1
- update to 3.0.3

* Fri Jul  1 2016 Remi Collet <remi@fedoraproject.org> - 3.0.2-1
- update to 3.0.2

* Wed Jun 29 2016 Remi Collet <remi@fedoraproject.org> - 3.0.1-1
- update to 3.0.1 for ZendFramework 3
- raise dependency on PHP 5.6
- raise dependency on zend-eventmanager 3.0
- raise dependency on zend-stdlib 3.0
- raise dependency on zend-servicemanager 3.0.3
- add dependencies on zend-http, zend-modulemanager, zend-router, zend-view
- drop dependencies on zend-hydrator, zend-form, zend-psr7bridge
- add dependencies autoloader

* Tue Jun 14 2016 Remi Collet <remi@fedoraproject.org> - 2.7.10-1
- update to 2.7.10

* Wed Jun  1 2016 Remi Collet <remi@fedoraproject.org> - 2.7.8-1
- update to 2.7.8

* Wed Apr 13 2016 Remi Collet <remi@fedoraproject.org> - 2.7.7-1
- update to 2.7.7

* Thu Apr  7 2016 Remi Collet <remi@fedoraproject.org> - 2.7.6-1
- update to 2.7.6

* Wed Apr  6 2016 Remi Collet <remi@fedoraproject.org> - 2.7.5-1
- update to 2.7.5

* Mon Apr  4 2016 Remi Collet <remi@fedoraproject.org> - 2.7.4-1
- update to 2.7.4

* Wed Mar  9 2016 Remi Collet <remi@fedoraproject.org> - 2.7.3-1
- update to 2.7.3

* Thu Mar  3 2016 Remi Collet <remi@fedoraproject.org> - 2.7.1-1
- update to 2.7.1

* Wed Mar  2 2016 Remi Collet <remi@fedoraproject.org> - 2.7.0-1
- update to 2.7.0
- add dependency on zend-psr7bridge
- add dependency on container-interop
- raise dependency on zend-eventmanager >= 2.6.2
- raise dependency on zend-servicemanager >= 2.7.5
- raise dependency on zend-hydrator >= 1.1
- raise dependency on zend-form >= 2.7
- raise dependency on zend-stdlib >= 2.7.5

* Tue Feb 23 2016 Remi Collet <remi@fedoraproject.org> - 2.6.3-1
- update to 2.6.3

* Tue Feb 23 2016 Remi Collet <remi@fedoraproject.org> - 2.6.2-1
- update to 2.6.2

* Tue Feb 16 2016 Remi Collet <remi@fedoraproject.org> - 2.6.1-1
- update to 2.6.1
- raise dependency on zend-stdlib ^2.7.5

* Thu Jan 28 2016 Remi Collet <remi@fedoraproject.org> - 2.6.0-1
- update to 2.6.0
- raise dependencies on zend-form ^2.6 and zend-stdlib ^2.7
- add dependency on zend-hydrator ^1.0

* Thu Jan 28 2016 Remi Collet <remi@fedoraproject.org> - 2.6.0-0
- update to 2.6.0, bootstrap build

* Thu Sep 24 2015 Remi Collet <remi@fedoraproject.org> - 2.5.3-1
- version 2.5.3

* Tue Sep 15 2015 Remi Collet <remi@fedoraproject.org> - 2.5.2-1
- version 2.5.2

* Tue Aug  4 2015 Remi Collet <remi@fedoraproject.org> - 2.5.1-1
- initial package

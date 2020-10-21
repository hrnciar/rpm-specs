# remirepo/Fedora spec file for php-laminas-paginator
#
# Copyright (c) 2015-2020 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global bootstrap    0
%global gh_commit    f1cf5c29d8dd7d6aa77f490e322326b3b670e28c
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     laminas
%global gh_project   laminas-paginator
%global zf_name      zend-paginator
%global php_home     %{_datadir}/php
%global namespace    Laminas
%global library      Paginator
%if %{bootstrap}
%global with_tests   0%{?_with_tests:1}
%else
%global with_tests   0%{!?_without_tests:1}
%endif

Name:           php-%{gh_project}
Version:        2.9.0
Release:        1%{?dist}
Summary:        %{namespace} Framework %{library} component

License:        BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{gh_commit}/%{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
# Tests
%if %{with_tests}
BuildRequires:  php(language) >= 7.3
BuildRequires:  php-json
BuildRequires:  php-spl
BuildRequires: (php-autoloader(%{gh_owner}/laminas-stdlib)               >= 3.2.1   with php-autoloader(%{gh_owner}/laminas-stdlib)               < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.0.4   with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
# From composer, "require-dev": {
#        "laminas/laminas-cache": "^2.9.0",
#        "laminas/laminas-coding-standard": "~1.0.0",
#        "laminas/laminas-config": "^2.6.0",
#        "laminas/laminas-db": "^2.11.3",
#        "laminas/laminas-filter": "^2.9.4",
#        "laminas/laminas-json": "^2.6.1",
#        "laminas/laminas-servicemanager": "^3.4.1",
#        "laminas/laminas-view": "^2.11.4",
#        "phpunit/phpunit": "^8.5.8"
BuildRequires: (php-autoloader(%{gh_owner}/laminas-cache)                >= 2.9.0   with php-autoloader(%{gh_owner}/laminas-cache)                <  3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-config)               >= 2.6.0   with php-autoloader(%{gh_owner}/laminas-config)               <  3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-db)                   >= 2.11.3  with php-autoloader(%{gh_owner}/laminas-db)                   <  3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-filter)               >= 2.9.4   with php-autoloader(%{gh_owner}/laminas-filter)               <  3)
# ignore max version as test suite passes with 3.1.1
BuildRequires:  php-autoloader(%{gh_owner}/laminas-json)                 >= 2.6.1
BuildRequires: (php-autoloader(%{gh_owner}/laminas-servicemanager)       >= 3.4.1   with php-autoloader(%{gh_owner}/laminas-servicemanager)       <  4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-view)                 >= 2.11.4  with php-autoloader(%{gh_owner}/laminas-view)                 <  3)
BuildRequires:  phpunit8 >= 8.5.8
%endif
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer, "require": {
#        "php": "^7.3",
#        "laminas/laminas-stdlib": "^3.2.1",
#        "laminas/laminas-zendframework-bridge": "^1.0.4"
Requires:       php(language) >= 7.3
%if ! %{bootstrap}
Requires:      (php-autoloader(%{gh_owner}/laminas-stdlib)               >= 3.2.1   with php-autoloader(%{gh_owner}/laminas-stdlib)               < 4)
Requires:      (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.0.4   with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
# From composer, "suggest": {
#        "laminas/laminas-cache": "Laminas\\Cache component to support cache features",
#        "laminas/laminas-db": "Laminas\\Db component",
#        "laminas/laminas-filter": "Laminas\\Filter component",
#        "laminas/laminas-json": "Laminas\\Json component",
#        "laminas/laminas-servicemanager": "Laminas\\ServiceManager component",
#        "laminas/laminas-view": "Laminas\\View component"
Suggests:       php-autoloader(%{gh_owner}/laminas-cache)
Suggests:       php-autoloader(%{gh_owner}/laminas-db)
Suggests:       php-autoloader(%{gh_owner}/laminas-filter)
Suggests:       php-autoloader(%{gh_owner}/laminas-json)
Suggests:       php-autoloader(%{gh_owner}/laminas-servicemanager)
Suggests:       php-autoloader(%{gh_owner}/laminas-view)
%endif
# Autoloader
Requires:       php-composer(fedora/autoloader)
# From phpcompatinfo report for version 2.8.2
Requires:       php-json
Requires:       php-spl

# Compatibily ensure by the bridge
Obsoletes:      php-zendframework-%{zf_name}              < 2.8.3
Provides:       php-zendframework-%{zf_name}              = %{version}
Provides:       php-composer(%{gh_owner}/%{gh_project})   = %{version}
Provides:       php-composer(zendframework/%{zf_name})    = %{version}
Provides:       php-autoloader(%{gh_owner}/%{gh_project}) = %{version}
Provides:       php-autoloader(zendframework/%{zf_name})  = %{version}


%description
%{namespace}\Paginator is a flexible component for paginating
collections of data and presenting that data to users.

Documentation: https://docs.laminas.dev/%{gh_project}/


%prep
%setup -q -n %{gh_project}-%{gh_commit}

mv LICENSE.md LICENSE


%build
: Create autoloader
phpab --template fedora --output src/autoload.php src
cat << 'EOF' | tee -a src/autoload.php
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/%{namespace}/Stdlib/autoload.php',
]);
\Fedora\Autoloader\Dependencies::optional([
    '%{php_home}/%{namespace}/Cache/autoload.php',
    '%{php_home}/%{namespace}/Db/autoload.php',
    '%{php_home}/%{namespace}/Filter/autoload.php',
    '%{php_home}/%{namespace}/Json/autoload.php',
    '%{php_home}/%{namespace}/ServiceManager/autoload.php',
    '%{php_home}/%{namespace}/View/autoload.php',
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
    '%{php_home}/%{namespace}/Config/autoload.php',
]);
\Fedora\Autoloader\Autoload::addPsr4('%{namespace}Test\\%{library}\\', dirname(__DIR__) . '/test');
EOF

: check compat autoloader
php -r '
require "%{buildroot}%{php_home}/Zend/%{library}/autoload.php";
exit (class_exists("\\Zend\\%{library}\\Factory") ? 0 : 1);
'

: upstream test suite
ret=0
for cmd in php php72 php73 php74; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit8 --verbose || ret=1
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
* Fri Sep 11 2020 Remi Collet <remi@remirepo.net> - 2.9.0-1
- update to 2.9.0
- raise dependency to PHP 7.3
- raise dependency to laminas-stdlib 3.2.1
- raise dependency to laminas-zendframework-bridge 1.0.4
- switch to phpunit8

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Remi Collet <remi@remirepo.net> - 2.8.3-1
- update to 2.8.3

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 16 2020 Remi Collet <remi@remirepo.net> - 2.8.2-1
- switch to Laminas

* Wed Aug 21 2019 Remi Collet <remi@remirepo.net> - 2.8.2-2
- update to 2.8.2
- use range dependencies

* Wed Jan 31 2018 Remi Collet <remi@remirepo.net> - 2.8.1-1
- Update to 2.8.1

* Tue Dec 12 2017 Remi Collet <remi@remirepo.net> - 2.8.0-2
- switch from zend-loader to fedora/autoloader

* Thu Nov  2 2017 Remi Collet <remi@remirepo.net> - 2.8.0-1
- Update to 2.8.0
- raise dependency on PHP 5.6
- use phpunit6 on F26+

* Tue Apr 12 2016 Remi Collet <remi@fedoraproject.org> - 2.7.0-1
- update to 2.7.0

* Wed Feb 24 2016 Remi Collet <remi@fedoraproject.org> - 2.6.0-1
- update to 2.6.0
- raise dependency on PHP >= 5.5
- raise dependency on zend-stdlib >= 2.7

* Tue Aug  4 2015 Remi Collet <remi@fedoraproject.org> - 2.5.1-1
- initial package

# remirepo/Fedora spec file for php-laminas-config3
#
# Copyright (c) 2015-2020 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global bootstrap    0
%global gh_commit    0bce6f5abab41dc673196741883b19018a2b5994
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     laminas
%global gh_project   laminas-config
%global zf_name      zend-config
%global php_home     %{_datadir}/php
%global namespace    Laminas
%global library      Config
%global major        3
%if %{bootstrap}
%global with_tests   0%{?_with_tests:1}
%else
%global with_tests   0%{!?_without_tests:1}
%endif

Name:           php-%{gh_project}%{major}
Version:        3.4.0
Release:        1%{?dist}
Summary:        %{namespace} Framework %{library} component v%{major}

License:        BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{gh_commit}/%{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
# Tests
%if %{with_tests}
BuildRequires:  php(language) >= 7.3
BuildRequires:  php-json
BuildRequires:  php-libxml
BuildRequires:  php-pcre
BuildRequires:  php-spl
BuildRequires:  php-xmlreader
BuildRequires:  php-xmlwriter
BuildRequires: (php-autoloader(%{gh_owner}/laminas-stdlib)               >= 3.0    with php-autoloader(%{gh_owner}/laminas-stdlib)               < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.0    with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
BuildRequires: (php-composer(psr/container)                              >= 1.0    with php-composer(psr/container)                              < 2)
# From composer, "require-dev": {
#        "laminas/laminas-filter": "^2.7.2",
#        "laminas/laminas-i18n": "^2.10.3",
#        "laminas/laminas-servicemanager": "^3.4.1",
#        "malukenho/docheader": "^0.1.6",
#        "phpunit/phpunit": "^8.5.8"
BuildRequires: (php-autoloader(%{gh_owner}/laminas-filter)               >= 2.7.2  with php-autoloader(%{gh_owner}/laminas-filter)               < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-i18n)                 >= 2.10.3 with php-autoloader(%{gh_owner}/laminas-i18n)                 < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-servicemanager)       >= 3.4.1  with php-autoloader(%{gh_owner}/laminas-servicemanager)       < 4)
BuildRequires:  phpunit8 >= 8.5.8
%endif
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer, "require": {
#        "php": "^7.3 || ^8.0",
#        "ext-json": "*",
#        "laminas/laminas-stdlib": "^2.7.7 || ^3.1",
#        "laminas/laminas-zendframework-bridge": "^1.0",
#        "psr/container": "^1.0"
#        "laminas/laminas-stdlib": "^2.7 || ^3.0",
#        "laminas/laminas-zendframework-bridge": "^1.0"
Requires:       php(language) >= 7.3
Requires:       php-json
Requires:      (php-autoloader(%{gh_owner}/laminas-stdlib)               >= 3.1   with php-autoloader(%{gh_owner}/laminas-stdlib)               < 4)
Requires:      (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.0   with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
Requires:      (php-composer(psr/container)                              >= 1.0   with php-composer(psr/container)                              < 2)
# From composer, "suggest": {
#        "laminas/laminas-filter": "Laminas\\Filter component",
#        "laminas/laminas-i18n": "Laminas\\I18n component",
#        "laminas/laminas-servicemanager": "Laminas\\ServiceManager for use with the Config Factory to retrieve reader and writer instances"
Suggests:       php-autoloader(%{gh_owner}/laminas-filter)
Suggests:       php-autoloader(%{gh_owner}/laminas-i18n)
Suggests:       php-autoloader(%{gh_owner}/laminas-servicemanager)
# Autoloader
Requires:       php-composer(fedora/autoloader)
# From phpcompatinfo report for version 2.6.0
Requires:       php-libxml
Requires:       php-pcre
Requires:       php-spl
Requires:       php-xmlreader
Requires:       php-xmlwriter

Provides:       php-composer(%{gh_owner}/%{gh_project})   = %{version}
Provides:       php-composer(zendframework/%{zf_name})    = %{version}
Provides:       php-autoloader(%{gh_owner}/%{gh_project}) = %{version}
Provides:       php-autoloader(zendframework/%{zf_name})  = %{version}


%description
%{namespace}\Config is designed to simplify access to configuration data within
applications. It provides a nested object property-based user interface
for accessing this configuration data within application code. The
configuration data may come from a variety of media supporting hierarchical
data storage.

Documentation: https://docs.laminas.dev/%{gh_project}/


%prep
%setup -q -n %{gh_project}-%{gh_commit}

mv LICENSE.md LICENSE


%build
phpab --template fedora --output src/autoload.php src
cat << 'EOF' | tee -a src/autoload.php
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/%{namespace}/Stdlib/autoload.php',
    '%{php_home}/Psr/Container/autoload.php',
]);
\Fedora\Autoloader\Dependencies::optional([
    '%{php_home}/%{namespace}/Filter/autoload.php',
    '%{php_home}/%{namespace}/I18n/autoload.php',
    '%{php_home}/%{namespace}/ServiceManager/autoload.php',
]);
EOF

cat << 'EOF' | tee zf.php
<?php
require_once '%{php_home}/Fedora/Autoloader/autoload.php';
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/%{namespace}/ZendFrameworkBridge/autoload.php',
    dirname(dirname(__DIR__)) . '/%{namespace}/%{library}%{major}/autoload.php',
]);
EOF


%install
: Laminas library
mkdir -p   %{buildroot}%{php_home}/%{namespace}/
cp -pr src %{buildroot}%{php_home}/%{namespace}/%{library}%{major}

: Zend equiv
mkdir -p      %{buildroot}%{php_home}/Zend/%{library}%{major}
cp -pr zf.php %{buildroot}%{php_home}/Zend/%{library}%{major}/autoload.php


%check
%if %{with_tests}
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require_once '%{buildroot}%{php_home}/%{namespace}/%{library}%{major}/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('%{namespace}Test\\%{library}\\', dirname(__DIR__) . '/test');
EOF

: check compat autoloader
php -r '
require "%{buildroot}%{php_home}/Zend/%{library}%{major}/autoload.php";
exit (class_exists("\\Zend\\%{library}\\Config") ? 0 : 1);
'

: upstream test suite
ret=0
for cmd in php php72 php73 php74 php80; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit8 || ret=1
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
%{php_home}/Zend/%{library}%{major}
%{php_home}/%{namespace}/%{library}%{major}


%changelog
* Tue Aug 25 2020 Remi Collet <remi@remirepo.net> - 3.4.0-1
- update to 3.4.0
- raise dependency on PHP 7.3
- switch to phpunit8

* Mon Jan 20 2020 Remi Collet <remi@remirepo.net> - 3.3.0-1
- rename to php-laminas-config3
- install in /usr/share/php/Laminas/Config3
- update to 3.3.0
- raise dependency on PHP 5.6
- raise dependency on laminas-stdlib 3.1
- add dependency on psr/container
- add dependency on json extention
- drop dependency on laminas-json
- switch to phpunit7

* Fri Jan 17 2020 Remi Collet <remi@remirepo.net> - 2.6.0-2
- cleanup

* Thu Jan  9 2020 Remi Collet <remi@remirepo.net> - 2.6.0-1
- switch to Laminas

* Tue Feb  5 2019 Remi Collet <remi@remirepo.net> - 2.6.0-7
- fix FTBFS with PHP 7.3, patch from
  https://github.com/zendframework/zend-config/pull/54
- use range dependencies

* Thu Dec  7 2017 Remi Collet <remi@remirepo.net> - 2.6.0-4
- switch from zend-loader to fedora/autoloader

* Fri Feb  5 2016 Remi Collet <remi@fedoraproject.org> - 2.6.0-1
- update to 2.6.0
- raise dependency on PHP >= 5.5
- raise dependency on zend-stdlib >= 2.7

* Tue Aug  4 2015 Remi Collet <remi@fedoraproject.org> - 2.5.1-1
- initial package

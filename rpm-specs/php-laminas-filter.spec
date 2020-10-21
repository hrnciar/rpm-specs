# remirepo/Fedora spec file for php-laminas-filter
#
# Copyright (c) 2015-2020 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global bootstrap    0
%global gh_commit    3c4476e772a062cef7531c6793377ae585d89c82
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     laminas
%global gh_project   laminas-filter
%global zf_name      zend-filter
%global php_home     %{_datadir}/php
%global namespace    Laminas
%global library      Filter
%global with_tests   0%{!?_without_tests:1}

Name:           php-%{gh_project}
Version:        2.9.4
Release:        2%{?dist}
Summary:        %{namespace} Framework %{library} component

License:        BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{gh_commit}/%{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
# Tests
%if %{with_tests}
# 7.0 because of psr/http-factory
BuildRequires:  php(language) >= 7.0
BuildRequires:  php-date
BuildRequires:  php-iconv
BuildRequires:  php-mbstring
BuildRequires:  php-mcrypt
BuildRequires:  php-pcre
BuildRequires:  php-spl
BuildRequires:  php-zip
BuildRequires: (php-autoloader(%{gh_owner}/laminas-stdlib)               >= 3.1.0 with php-autoloader(%{gh_owner}/laminas-stdlib)               < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.0   with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
# From composer, "require-dev": {
#        "laminas/laminas-coding-standard": "~1.0.0",
#        "laminas/laminas-crypt": "^3.2.1",
#        "laminas/laminas-servicemanager": "^2.7.8 || ^3.3",
#        "laminas/laminas-uri": "^2.6",
#        "pear/archive_tar": "^1.4.3",
#        "phpunit/phpunit": "^5.7.23 || ^6.4.3",
#        "psr/http-factory": "^1.0"
BuildRequires: (php-autoloader(%{gh_owner}/laminas-crypt)                >= 3.2.1 with php-autoloader(%{gh_owner}/laminas-crypt)                < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-servicemanager)       >= 3.3   with php-autoloader(%{gh_owner}/laminas-servicemanager)       < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-uri)                  >= 2.6   with php-autoloader(%{gh_owner}/laminas-uri)                  < 3)
BuildRequires: (php-composer(psr/http-factory)                           >= 1.0   with php-composer(psr/http-factory)                           < 2)
BuildRequires:  php-autoloader(pear/archive_tar)                         >= 1.4.3
%global phpunit %{_bindir}/phpunit6
BuildRequires:  phpunit6 >= 6.4.3
%endif
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer, "require": {
#        "php": "^5.6 || ^7.0",
#        "laminas/laminas-stdlib": "^2.7.7 || ^3.1",
#        "laminas/laminas-zendframework-bridge": "^1.0"
Requires:       php(language) >= 5.6
Requires:      (php-autoloader(%{gh_owner}/laminas-stdlib)               >= 3.1.0 with php-autoloader(%{gh_owner}/laminas-stdlib)               < 4)
Requires:      (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.0   with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
# From composer, "suggest": {
#        "laminas/laminas-crypt": "Laminas\\Crypt component, for encryption filters",
#        "laminas/laminas-i18n": "Laminas\\I18n component for filters depending on i18n functionality",
#        "laminas/laminas-servicemanager": "Laminas\\ServiceManager component, for using the filter chain functionality",
#        "laminas/laminas-uri": "Laminas\\Uri component, for the UriNormalize filter",
#        "psr/http-factory-implementation": "psr/http-factory-implementation, for creating file upload instances when consuming PSR-7 in file upload filters"
Suggests:       php-autoloader(%{gh_owner}/laminas-crypt)
Suggests:       php-autoloader(%{gh_owner}/laminas-i18n)
Suggests:       php-autoloader(%{gh_owner}/laminas-servicemanager)
Suggests:       php-autoloader(%{gh_owner}/laminas-uri)
Suggests:       php-composer(psr/http-factory-implementation)
# optional compression extensions
Recommends:     php-bz2
Recommends:     php-zlib
Suggests:       php-lzf
Recommends:     php-zip
# Autoloader
Requires:       php-composer(fedora/autoloader)
# From phpcompatinfo report for version 2.9.3
Requires:       php-date
Requires:       php-iconv
Requires:       php-mbstring
Requires:       php-openssl
Requires:       php-pcre
Requires:       php-spl

# Compatibily ensure by the bridge
Obsoletes:      php-zendframework-%{zf_name}              < 2.9.3
Provides:       php-zendframework-%{zf_name}              = %{version}
Provides:       php-composer(%{gh_owner}/%{gh_project})   = %{version}
Provides:       php-composer(zendframework/%{zf_name})    = %{version}
Provides:       php-autoloader(%{gh_owner}/%{gh_project}) = %{version}
Provides:       php-autoloader(zendframework/%{zf_name})  = %{version}


%description
The %{namespace}\Filter component provides a set of commonly needed data filters.
It also provides a simple filter chaining mechanism by which multiple
filters may be applied to a single datum in a user-defined order.

Documentation: https://docs.laminas.dev/%{gh_project}/


%prep
%setup -q -n %{gh_project}-%{gh_commit}

mv LICENSE.md LICENSE


%build
phpab --template fedora --output src/autoload.php src
cat << 'EOF' | tee -a src/autoload.php
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/%{namespace}/Stdlib/autoload.php',
]);
\Fedora\Autoloader\Dependencies::optional([
    '%{php_home}/Psr/Http/Message/http-factory-autoload.php',
    '%{php_home}/%{namespace}/Crypt/autoload.php',
    '%{php_home}/%{namespace}/I18n/autoload.php',
    '%{php_home}/%{namespace}/ServiceManager/autoload.php',
    '%{php_home}/%{namespace}/Uri/autoload.php',
    '%{_datadir}/pear/Archive/Tar/autoload.php',
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
EOF

# Need investigation
rm test/Compress/SnappyTest.php

: check compat autoloader
php -r '
require "%{buildroot}%{php_home}/Zend/%{library}/autoload.php";
exit (class_exists("\\Zend\\%{library}\\ToInt") ? 0 : 1);
'

: upstream test suite
ret=0
for cmd in "php %{phpunit}" php72 php73 php74; do
  if which $cmd; then
    set $cmd
    $1 ${2:-%{_bindir}/phpunit6} || ret=1
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
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Mar 30 2020 Remi Collet <remi@remirepo.net> - 2.9.4-1
- update to 2.9.4 (no change)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Remi Collet <remi@remirepo.net> - 2.9.3-2
- cleanup

* Thu Jan  9 2020 Remi Collet <remi@remirepo.net> - 2.9.3-1
- switch to Laminas
- update to 2.9.3

* Tue Aug 20 2019 Remi Collet <remi@remirepo.net> - 2.9.2-1
- update to 2.9.2

* Tue Dec 18 2018 Remi Collet <remi@remirepo.net> - 2.9.1-1
- update to 2.9.1

* Thu Dec 13 2018 Remi Collet <remi@remirepo.net> - 2.9.0-1
- update to 2.9.0
- add optional dependency on psr/http-factory-implementation
- use range dependencies

* Thu Apr 12 2018 Remi Collet <remi@remirepo.net> - 2.8.0-1
- update to 2.8.0
- raise dependency on PHP 5.6
- raise dependency on zend-stdlib 3.1.0
- always use phpunit6
- compression extensions are optional

* Tue Dec 19 2017 Remi Collet <remi@remirepo.net> - 2.7.2-4
- use Archive_Tar autoloader

* Thu Dec  7 2017 Remi Collet <remi@remirepo.net> - 2.7.2-3
- switch from zend-loader to fedora/autoloader

* Mon May 22 2017 Remi Collet <remi@remirepo.net> - 2.7.2-1
- Update to 2.7.2
- use phpunit6 on F26+

* Wed Feb 22 2017 Remi Collet <remi@fedoraproject.org> - 2.7.1-3
- don't convertErrorsToExceptions, fix FTBFS #1424085

* Fri Nov 25 2016 Remi Collet <remi@fedoraproject.org> - 2.7.1-2
- fix FTBFS, disable E_DEPRECATED during test suite

* Tue Apr 19 2016 Remi Collet <remi@fedoraproject.org> - 2.7.1-1
- update to 2.7.1

* Wed Apr  6 2016 Remi Collet <remi@fedoraproject.org> - 2.7.0-1
- update to 2.7.0

* Fri Feb 12 2016 Remi Collet <remi@fedoraproject.org> - 2.6.1-1
- update to 2.6.1

* Fri Feb  5 2016 Remi Collet <remi@fedoraproject.org> - 2.6.0-1
- update to 2.6.0
- raise dependency on PHP >= 5.5
- raise dependency on zend-stdlib >= 2.7

* Tue Aug  4 2015 Remi Collet <remi@fedoraproject.org> - 2.5.1-1
- initial package

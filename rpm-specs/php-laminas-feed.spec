# remirepo/Fedora spec file for php-laminas-feed
#
# Copyright (c) 2015-2020 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global bootstrap    0
%global gh_commit    8a193ac96ebcb3e16b6ee754ac2a889eefacb654
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     laminas
%global gh_project   laminas-feed
%global zf_name      zend-feed
%global php_home     %{_datadir}/php
%global namespace    Laminas
%global library      Feed
%if %{bootstrap}
%global with_tests   0%{?_with_tests:1}
%else
%global with_tests   0%{!?_without_tests:1}
%endif

Name:           php-%{gh_project}
Version:        2.12.2
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
BuildRequires:  php-ctype
BuildRequires:  php-date
BuildRequires:  php-dom
BuildRequires:  php-hash
BuildRequires:  php-libxml
BuildRequires:  php-pcre
BuildRequires:  php-spl
BuildRequires:  php-tidy
# From composer, "require-dev": {
#        "laminas/laminas-cache": "^2.7.2",
#        "laminas/laminas-coding-standard": "~1.0.0",
#        "laminas/laminas-db": "^2.8.2",
#        "laminas/laminas-http": "^2.7",
#        "laminas/laminas-servicemanager": "^2.7.8 || ^3.3",
#        "laminas/laminas-validator": "^2.10.1",
#        "phpunit/phpunit": "^5.7.27 || ^6.5.14 || ^7.5.20",
#        "psr/http-message": "^1.0.1"
%global phpunit %{_bindir}/phpunit7
BuildRequires:  phpunit7 >= 7.5.20
BuildRequires: (php-composer(psr/http-message)                           >= 1.0.1   with php-composer(psr/http-message)                           < 2)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-escaper)              >= 2.5.2   with php-autoloader(%{gh_owner}/laminas-escaper)              < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-stdlib)               >= 3.2.1   with php-autoloader(%{gh_owner}/laminas-stdlib)               < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.0     with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-cache)                >= 2.7.2   with php-autoloader(%{gh_owner}/laminas-cache)                < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-db)                   >= 2.8.2   with php-autoloader(%{gh_owner}/laminas-db)                   < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-http)                 >= 2.7     with php-autoloader(%{gh_owner}/laminas-http)                 < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-servicemanager)       >= 3.3     with php-autoloader(%{gh_owner}/laminas-servicemanager)       < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-validator)            >= 2.10.1  with php-autoloader(%{gh_owner}/laminas-validator)            < 3)
%endif
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer, "require": {
#        "php": "^5.6 || ^7.0",
#        "ext-dom": "*",
#        "ext-libxml": "*",
#        "laminas/laminas-escaper": "^2.5.2",
#        "laminas/laminas-stdlib": "^3.2.1",
#        "laminas/laminas-zendframework-bridge": "^1.0"
Requires:       php(language) >= 5.6
Requires:       php-dom
Requires:       php-libxml
%if ! %{bootstrap}
Requires:      (php-composer(psr/http-message)                           >= 1.0.1   with php-composer(psr/http-message)                           < 2)
Requires:      (php-autoloader(%{gh_owner}/laminas-escaper)              >= 2.5.2   with php-autoloader(%{gh_owner}/laminas-escaper)              < 3)
Requires:      (php-autoloader(%{gh_owner}/laminas-stdlib)               >= 3.2.1   with php-autoloader(%{gh_owner}/laminas-stdlib)               < 4)
Requires:      (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.0     with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
# From composer, "suggest": {
#        "laminas/laminas-cache": "Laminas\\Cache component, for optionally caching feeds between requests",
#        "laminas/laminas-db": "Laminas\\Db component, for use with PubSubHubbub",
#        "laminas/laminas-http": "Laminas\\Http for PubSubHubbub, and optionally for use with Laminas\\Feed\\Reader",
#        "laminas/laminas-servicemanager": "Laminas\\ServiceManager component, for easily extending ExtensionManager implementations",
#        "laminas/laminas-validator": "Laminas\\Validator component, for validating email addresses used in Atom feeds and entries when using the Writer subcomponent",
#        "psr/http-message": "PSR-7 ^1.0.1, if you wish to use Laminas\\Feed\\Reader\\Http\\Psr7ResponseDecorator"
Suggests:       php-autoloader(%{gh_owner}/laminas-cache)
Suggests:       php-autoloader(%{gh_owner}/laminas-db)
Suggests:       php-autoloader(%{gh_owner}/laminas-http)
Suggests:       php-autoloader(%{gh_owner}/laminas-servicemanager)
Suggests:       php-autoloader(%{gh_owner}/laminas-validator)
%endif
# Autoloader
Requires:       php-composer(fedora/autoloader)
# From phpcompatinfo report for version 2.12.0
Requires:       php-ctype
Requires:       php-date
Requires:       php-hash
Requires:       php-pcre
Requires:       php-spl
Requires:       php-tidy

# Compatibily ensure by the bridge
Obsoletes:      php-zendframework-%{zf_name}              < 2.12.1
Provides:       php-zendframework-%{zf_name}              = %{version}
Provides:       php-composer(%{gh_owner}/%{gh_project})   = %{version}
Provides:       php-composer(zendframework/%{zf_name})    = %{version}
Provides:       php-autoloader(%{gh_owner}/%{gh_project}) = %{version}
Provides:       php-autoloader(zendframework/%{zf_name})  = %{version}


%description
%{namespace}\Feed provides functionality for consuming RSS and Atom feeds.
It provides a natural syntax for accessing elements of feeds, feed attributes,
and entry attributes. %{namespace}\Feed also has extensive support for modifying
feed and entry structure with the same natural syntax, and turning the result
back into XML.

Documentation: https://docs.laminas.dev/%{gh_project}/


%prep
%setup -q -n %{gh_project}-%{gh_commit}

mv LICENSE.md LICENSE


%build
: Generate autoloader
phpab --template fedora --output src/autoload.php src
cat << 'EOF' | tee -a src/autoload.php
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/%{namespace}/Escaper/autoload.php',
    '%{php_home}/%{namespace}/Stdlib/autoload.php',
    '%{php_home}/Psr/Http/Message/autoload.php',
]);
\Fedora\Autoloader\Dependencies::optional([
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
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require_once '%{buildroot}%{php_home}/%{namespace}/%{library}/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('%{namespace}Test\\%{library}\\', dirname(__DIR__) . '/test');
EOF

: check compat autoloader
php -r '
require "%{buildroot}%{php_home}/Zend/%{library}/autoload.php";
exit (class_exists("\\Zend\\%{library}\\Uri") ? 0 : 1);
'

: upstream test suite
ret=0
for cmdarg in "php %{phpunit}" php72 php73 php74; do
  if which $cmdarg; then
    set $cmdarg
    $1 -d memory_limit=1G ${2:-%{_bindir}/phpunit7} --verbose || ret=1
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
* Mon Mar 30 2020 Remi Collet <remi@remirepo.net> - 2.12.2-1
- update to 2.12.2 (no change)

* Mon Mar 23 2020 Remi Collet <remi@remirepo.net> - 2.12.1-1
- update to 2.12.1
- switch to phpunit7

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 14 2020 Remi Collet <remi@remirepo.net> - 2.12.0-1
- switch to Laminas

* Thu Mar  7 2019 Remi Collet <remi@remirepo.net> - 2.12.0-1
- update to 2.12.0

* Thu Mar  7 2019 Remi Collet <remi@remirepo.net> - 2.11.1-1
- update to 2.11.1

* Thu Jan 31 2019 Remi Collet <remi@remirepo.net> - 2.11.0-1
- update to 2.11.0
- raise dependency on zend-stdlib 3.2.1

* Thu Aug 02 2018 Shawn Iwinski <shawn@iwin.ski> - 2.10.3-1
- Update to 2.10.3 (ZF2018-01)

* Tue Jun 19 2018 Remi Collet <remi@remirepo.net> - 2.10.2-2
- update to 2.10.2

* Tue Jun  5 2018 Remi Collet <remi@remirepo.net> - 2.10.1-2
- update to 2.10.1

* Fri May 25 2018 Remi Collet <remi@remirepo.net> - 2.10.0-2
- update to 2.10.0

* Tue May 15 2018 Remi Collet <remi@remirepo.net> - 2.9.1-2
- update to 2.9.1
- use range dependencies on F27+

* Mon Dec 11 2017 Remi Collet <remi@remirepo.net> - 2.9.0-2
- switch from zend-loader to fedora/autoloader

* Tue Dec  5 2017 Remi Collet <remi@remirepo.net> - 2.9.0-1
- Update to 2.9.0
- raise dependency on zend-escaper 2.5.2
- raise dependency on zend-stdlib 2.7.7
- raise dependency on psr/http-message 1.0.1

* Tue Oct 24 2017 Remi Collet <remi@remirepo.net> - 2.8.0-4
- fix FTBFS from Koschei, add patch for PHP 7.2 from
  https://github.com/zendframework/zend-feed/pull/50

* Mon Apr  3 2017 Remi Collet <remi@remirepo.net> - 2.8.0-2
- change dependency on psr/http-message to required

* Sun Apr  2 2017 Remi Collet <remi@remirepo.net> - 2.8.0-1
- Update to 2.8.0
- raise dependency on PHP 5.6
- use phpunit6 on F26+

* Tue Nov 15 2016 Remi Collet <remi@fedoraproject.org> - 2.7.0-2
- add path for PHP 7.1
  open https://github.com/zendframework/zend-feed/pull/35

* Fri Feb 12 2016 Remi Collet <remi@fedoraproject.org> - 2.7.0-1
- update to 2.7.0
- raise dependency on zend-stdlib >= 2.7

* Thu Jan 28 2016 Remi Collet <remi@fedoraproject.org> - 2.6.0-1
- update to 2.6.0
- raise minimal php version to 5.5
- drop build dependency on zend-servicemanager
- add optional dependency on psr/http-message

* Tue Aug  4 2015 Remi Collet <remi@fedoraproject.org> - 2.5.2-1
- initial package

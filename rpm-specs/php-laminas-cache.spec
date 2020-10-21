# remirepo/Fedora spec file for php-laminas-cache
#
# Copyright (c) 2015-2020 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
# When buid without laminas-session
%global bootstrap    1
%global gh_commit    f4746a868c3e2f2da63c19d23efac12b9d1bb554
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     laminas
%global gh_project   laminas-cache
%global zf_name      zend-cache
%global php_home     %{_datadir}/php
%global namespace    Laminas
%global library      Cache
%global with_tests   0%{!?_without_tests:1}

Name:           php-%{gh_project}
Version:        2.9.0
Release:        4%{?dist}
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
BuildRequires:  php-date
BuildRequires:  php-pcre
BuildRequires:  php-spl
BuildRequires: (php-autoloader(%{gh_owner}/laminas-eventmanager)         >= 3.2   with php-autoloader(%{gh_owner}/laminas-eventmanager)         < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-servicemanager)       >= 3.3   with php-autoloader(%{gh_owner}/laminas-servicemanager)       < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-stdlib)               >= 3.2.1 with php-autoloader(%{gh_owner}/laminas-stdlib)               < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.0   with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
BuildRequires: (php-composer(psr/cache)                                  >= 1.0   with php-composer(psr/cache)                                  < 2)
BuildRequires: (php-composer(psr/simple-cache)                           >= 1.0   with php-composer(psr/simple-cache)                           < 2)
# From composer, "require-dev": {
#        "cache/integration-tests": "^0.16",
#        "laminas/laminas-coding-standard": "~1.0.0",
#        "laminas/laminas-serializer": "^2.6",
#        "laminas/laminas-session": "^2.7.4",
#        "phpbench/phpbench": "^0.13",
#        "phpunit/phpunit": "^5.7.27 || ^6.5.8 || ^7.1.2"
BuildRequires: (php-composer(cache/integration-tests)                    >= 0.16  with php-composer(cache/integration-tests)                    < 1)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-serializer)           >= 2.6   with php-autoloader(%{gh_owner}/laminas-serializer)           < 3)
%if ! %{bootstrap}
BuildRequires: (php-autoloader(%{gh_owner}/laminas-session)              >= 2.7.4 with php-autoloader(%{gh_owner}/laminas-session)              < 3)
%endif
%global phpunit %{_bindir}/phpunit7
BuildRequires:  phpunit7 >= 7.1.2
# Autoloader
BuildRequires:  php-fedora-autoloader-devel
%endif

# From composer, "require": {
#        "php": "^5.6 || ^7.0",
#        "laminas/laminas-eventmanager": "^2.6.3 || ^3.2",
#        "laminas/laminas-servicemanager": "^2.7.8 || ^3.3",
#        "laminas/laminas-stdlib": "^3.2.1",
#        "laminas/laminas-zendframework-bridge": "^1.0",
#        "psr/cache": "^1.0",
#        "psr/simple-cache": "^1.0"
Requires:       php(language) >= 5.6
Requires:      (php-autoloader(%{gh_owner}/laminas-eventmanager)         >= 3.2   with php-autoloader(%{gh_owner}/laminas-eventmanager)         < 4)
Requires:      (php-autoloader(%{gh_owner}/laminas-servicemanager)       >= 3.3   with php-autoloader(%{gh_owner}/laminas-servicemanager)       < 4)
Requires:      (php-autoloader(%{gh_owner}/laminas-stdlib)               >= 3.2.1 with php-autoloader(%{gh_owner}/laminas-stdlib)               < 4)
Requires:      (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.0   with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
Requires:      (php-composer(psr/cache)                                  >= 1.0   with php-composer(psr/cache)                                  < 2)
Requires:      (php-composer(psr/simple-cache)                           >= 1.0   with php-composer(psr/simple-cache)                           < 2)
# From composer, "suggest": {
#        "ext-apc": "APC or compatible extension, to use the APC storage adapter",
#        "ext-apcu": "APCU >= 5.1.0, to use the APCu storage adapter",
#        "ext-dba": "DBA, to use the DBA storage adapter",
#        "ext-memcache": "Memcache >= 2.0.0 to use the Memcache storage adapter",
#        "ext-memcached": "Memcached >= 1.0.0 to use the Memcached storage adapter",
#        "ext-mongo": "Mongo, to use MongoDb storage adapter",
#        "ext-mongodb": "MongoDB, to use the ExtMongoDb storage adapter",
#        "ext-redis": "Redis, to use Redis storage adapter",
#        "ext-wincache": "WinCache, to use the WinCache storage adapter",
#        "ext-xcache": "XCache, to use the XCache storage adapter",
#        "laminas/laminas-serializer": "Laminas\\Serializer component",
#        "laminas/laminas-session": "Laminas\\Session component",
#        "mongodb/mongodb": "Required for use with the ext-mongodb adapter",
#        "mongofill/mongofill": "Alternative to ext-mongo - a pure PHP implementation designed as a drop in replacement"
Suggests:       php-apcu
Suggests:       php-dba
Suggests:       php-memcache
Suggests:       php-memcached
Suggests:       php-redis
Suggests:       php-composer(%{gh_owner}/laminas-serializer)
Suggests:       php-composer(%{gh_owner}/laminas-session)
Suggests:       php-composer(mongodb/mongodb)
# From phpcompatinfo report for version 2.9.0
Requires:       php-reflection
Requires:       php-date
Requires:       php-pcre
Requires:       php-spl
# Autoloader
Requires:       php-composer(fedora/autoloader)

# Compatibily ensure by the bridge
Obsoletes:      php-zendframework-%{zf_name}              < 2.9.0-99
Provides:       php-zendframework-%{zf_name}              = %{version}-99
Provides:       php-composer(%{gh_owner}/%{gh_project})   = %{version}
Provides:       php-composer(zendframework/%{zf_name})    = %{version}
Provides:       php-autoloader(%{gh_owner}/%{gh_project}) = %{version}
Provides:       php-autoloader(zendframework/%{zf_name})  = %{version}
Provides:       php-composer(psr/cache-implementation)        = 1.0
Provides:       php-composer(psr/simple-cache-implementation) = 1.0


%description
%{namespace}\Cache provides a general cache system for PHP.
The %{namespace}\Cache component is able to cache different patterns
(class, object, output, etc) using different storage adapters
(DB, File, Memcache, etc).

Documentation: https://docs.laminas.dev/%{gh_project}/


%prep
%setup -q -n %{gh_project}-%{gh_commit}

mv LICENSE.md LICENSE

mv autoload/*.php src

%build
: Create autoloader
phpab --template fedora --output src/autoload.php src
cat << 'EOF' | tee -a src/autoload.php
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/Psr/Cache/autoload.php',
    '%{php_home}/Psr/SimpleCache/autoload.php',
    '%{php_home}/%{namespace}/Stdlib/autoload.php',
    '%{php_home}/%{namespace}/ServiceManager/autoload.php',
    '%{php_home}/%{namespace}/EventManager/autoload.php',
    __DIR__ . '/patternPluginManagerPolyfill.php',
]);
\Fedora\Autoloader\Dependencies::optional([
    '%{php_home}/%{namespace}/Serializer/autoload.php',
    '%{php_home}/%{namespace}/Session/autoload.php',
    '%{php_home}/MongoDB/autoload.php',
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
    '%{php_home}/Cache/IntegrationTests/autoload.php',
]);
\Fedora\Autoloader\Autoload::addPsr4('%{namespace}Test\\%{library}\\', dirname(__DIR__) . '/test');
EOF

# Try to slowdown tests with erratic results
sed -e '/unlinkDelay/s/5000/50000/' \
    -e '/usleep/s/1000/10000/' \
    -i test/Storage/Adapter/FilesystemTest.php

%if  %{bootstrap}
rm test/Storage/Adapter/SessionTest.php
%endif

: upstream test suite
ret=0
for cmdarg in "php %{phpunit}" php72 php73 php74; do
  if which $cmdarg; then
    set $cmdarg
    $1 ${2:-%{_bindir}/phpunit7} || ret=1
  fi
done

: check compat autoloader
php -r '
require "%{buildroot}%{php_home}/Zend/%{library}/autoload.php";
exit (class_exists("\\Zend\\%{library}\\StorageFactory") ? 0 : 1);
'

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
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Remi Collet <remi@remirepo.net> - 2.9.0-2
- cleanup

* Wed Jan  8 2020 Remi Collet <remi@remirepo.net> - 2.9.0-1
- switch to Laminas
- boostrap build without laminas-session

* Fri Aug 30 2019 Remi Collet <remi@remirepo.net> - 2.9.0-1
- update to 2.9.0
- raise dependency on zend-stdlib 3.2.1

* Thu Aug 29 2019 Remi Collet <remi@remirepo.net> - 2.8.3-2
- update to 2.8.3

* Sun Nov 25 2018 Remi Collet <remi@remirepo.net> - 2.8.2-4
- fix autoloader for psr/cache and psr/simple-cache

* Wed May  2 2018 Remi Collet <remi@remirepo.net> - 2.8.2-2
- update to 2.8.2

* Thu Apr 26 2018 Remi Collet <remi@remirepo.net> - 2.8.1-2
- update to 2.8.1

* Thu Apr 26 2018 Remi Collet <remi@remirepo.net> - 2.8.0-4
- add optional dependency on mongodb/mongodb

* Thu Apr 26 2018 Remi Collet <remi@remirepo.net> - 2.8.0-2
- update to 2.8.0
- raise dependency on PHP 5.6
- add dependency on psr/cache
- add dependency on psr/simple-cache
- raise dependency on zend-eventmanager 3.2
- raise dependency on zend-servicemanager 3.3
- raise dependency on zend-stdlib 3.1
- use range dependencies (F27+)
- switch to phpunit6 or phpunit7

* Fri Nov 24 2017 Remi Collet <remi@remirepo.net> - 2.7.2-6
- switch from zend-loader to fedora/autoloader

* Tue Nov 14 2017 Remi Collet <remi@fedoraproject.org> - 2.7.2-5
- try to slowdown tests with erratic result (FTBFS)

* Tue Oct 31 2017 Remi Collet <remi@fedoraproject.org> - 2.7.2-4
- fix FTBFS from Koschei, add upstream patch for PHP 7.2

* Fri Dec 16 2016 Remi Collet <remi@fedoraproject.org> - 2.7.2-1
- update to 2.7.2

* Fri May 13 2016 Remi Collet <remi@fedoraproject.org> - 2.7.1-1
- update to 2.7.1

* Wed Apr 13 2016 Remi Collet <remi@fedoraproject.org> - 2.7.0-1
- update to 2.7.0

* Sat Feb 13 2016 Remi Collet <remi@fedoraproject.org> - 2.6.1-1
- update to 2.6.1

* Fri Feb 12 2016 Remi Collet <remi@fedoraproject.org> - 2.6.0-1
- update to 2.6.0
- raise dependency on zend-stdlib >= 2.7
- raise dependency on zend-servicemanager >= 2.7.5
- raise dependency on zend-eventmanager >= 2.6.2

* Wed Sep 16 2015 Remi Collet <remi@fedoraproject.org> - 2.5.3-1
- update to 2.5.3
- zend-serializer is    optional

* Thu Aug  6 2015 Remi Collet <remi@fedoraproject.org> - 2.5.2-2
- add missing obsoletes

* Tue Aug  4 2015 Remi Collet <remi@fedoraproject.org> - 2.5.2-1
- initial package

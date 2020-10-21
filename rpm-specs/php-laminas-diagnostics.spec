# remirepo/Fedora spec file for php-laminas-diagnostics
#
# Copyright (c) 2019-2020 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global gh_commit    9434b93ca7fc66999e0a2f01400e7f20214169c4
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     laminas
%global gh_project   laminas-diagnostics
%global zf_name      zenddiagnostics
%global namespace    Laminas
%global library      Diagnostics
%global php_home     %{_datadir}/php
%global with_tests   0%{!?_without_tests:1}

Name:           php-%{gh_project}
Version:        1.6.0
Release:        4%{?dist}
Summary:        A set of components for performing diagnostic tests

License:        BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{gh_commit}/%{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
# Tests
%if %{with_tests}
BuildRequires:  php(language) >= 5.6
BuildRequires:  php-pdo
BuildRequires:  php-simplexml
BuildRequires:  php-json
BuildRequires:  php-pcre
BuildRequires:  php-spl
BuildRequires:  php-xmlreader
# From composer, "require-dev": {
#        "doctrine/migrations": "^1.0 || ^2.0",
#        "guzzlehttp/guzzle": "^5.3.3 || ^6.3.3",
#        "laminas/laminas-coding-standard": "~1.0.0",
#        "laminas/laminas-loader": "^2.0",
#        "mikey179/vfsstream": "^1.6",
#        "php-amqplib/php-amqplib": "^2.0",
#        "phpunit/phpunit": "^5.7.27 || 6.5.8 || ^7.1.2",
#        "predis/predis": "^1.0",
#        "sensiolabs/security-checker": "^5.0 || ^6.0.3",
#        "symfony/yaml": "^2.7 || ^3.0 || ^4.0 || ^5.0"
BuildRequires: (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.0   with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
BuildRequires: (php-composer(doctrine/migrations)                        >= 1.0   with php-composer(doctrine/migrations)                        < 3)
BuildRequires: (php-composer(guzzlehttp/guzzle)                          >= 5.3.3 with php-composer(guzzlehttp/guzzle)                          < 7)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-loader)               >= 2.0   with php-autoloader(%{gh_owner}/laminas-loader)               < 3)
BuildRequires: (php-composer(mikey179/vfsStream)                         >= 1.6   with php-composer(mikey179/vfsStream)                         < 2)
BuildRequires: (php-composer(php-amqplib/php-amqplib)                    >= 2.0   with php-composer(php-amqplib/php-amqplib)                    < 3)
BuildRequires: (php-composer(predis/predis)                              >= 1.0   with php-composer(predis/predis)                              < 2)
BuildRequires: (php-composer(sensiolabs/security-checker)                >= 5.0   with php-composer(sensiolabs/security-checker)                < 7)
BuildRequires: (php-composer(symfony/yaml)                               >= 2.7   with php-composer(symfony/yaml)                               < 6)
%global phpunit %{_bindir}/phpunit7
BuildRequires:  phpunit7 >= 7.1.2
BuildRequires:  /bin/ps
%endif
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer, "require": {
#        "php": "^5.6 || ^7.0",
#        "laminas/laminas-zendframework-bridge": "^1.0"
Requires:       php(language) >= 5.6
Requires:      (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.0 with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
#    "suggest": {
#        "ext-bcmath": "Required by Check\\CpuPerformance",
#        "sensiolabs/security-checker": "Required by Check\\SecurityAdvisory",
#        "symfony/yaml": "Required by Check\\YamlFile",
#        "guzzlehttp/guzzle": "Required by Check\\GuzzleHttpService",
#        "predis/predis": "Required by Check\\Redis",
#        "videlalvaro/php-amqplib": "Required by Check\\RabbitMQ",
#        "doctrine/migrations": "Required by Check\\DoctrineMigration"
Recommends:     php-bcmath
Recommends:    (php-composer(sensiolabs/security-checker) >= 5.0   with php-composer(sensiolabs/security-checker) < 7)
Recommends:    (php-composer(symfony/yaml)                >= 2.7   with php-composer(symfony/yaml)                < 6)
Recommends:    (php-composer(guzzlehttp/guzzle)           >= 5.3.3 with php-composer(guzzlehttp/guzzle)           < 7)
Recommends:    (php-composer(predis/predis)               >= 1.0   with php-composer(predis/predis)               < 2)
Recommends:    (php-composer(php-amqplib/php-amqplib)     >= 2.0   with php-composer(php-amqplib/php-amqplib)     < 3)
Recommends:    (php-composer(doctrine/migrations)         >= 1.0   with php-composer(doctrine/migrations)         < 3)
# Autoloader
Requires:       php-composer(fedora/autoloader)
# From phpcompatinfo report for version 1.6.0
Requires:       php-pdo
Requires:       php-simplexml
Requires:       php-json
Requires:       php-pcre
Requires:       php-spl
Requires:       php-xmlreader

# Compatibily ensure by the bridge
Obsoletes:      php-zendframework-%{zf_name}              < 1.6.0-99
Provides:       php-zendframework-%{zf_name}              = %{version}-99
Provides:       php-composer(%{gh_owner}/%{gh_project})   = %{version}
Provides:       php-composer(zendframework/%{zf_name})    = %{version}
Provides:       php-autoloader(%{gh_owner}/%{gh_project}) = %{version}
Provides:       php-autoloader(zendframework/%{zf_name})  = %{version}


%description
Perform diagnostic tests within real-world PHP applications.

Documentation: https://docs.laminas.dev/%{gh_project}/


%prep
%setup -q -n %{gh_project}-%{gh_commit}
mv LICENSE.md LICENSE


%build
: Create autoloader
mv src/autoload.php src/_autoload.php

phpab --template fedora --output src/autoload.php src
cat << 'EOF' | tee -a src/autoload.php
\Fedora\Autoloader\Dependencies::required([
   __DIR__ . '/_autoload.php',
]);
\Fedora\Autoloader\Dependencies::optional([
    '%{php_home}/SensioLabs/Security/autoload.php',
    [
        '%{php_home}/Symfony5/Component/Yaml/autoload.php',
        '%{php_home}/Symfony4/Component/Yaml/autoload.php',
        '%{php_home}/Symfony3/Component/Yaml/autoload.php',
        '%{php_home}/Symfony/Component/Yaml/autoload.php',
    ],
    '%{php_home}/GuzzleHttp6/autoload.php',
    '%{php_home}/PhpAmqpLib/autoload.php',
    [
        '%{php_home}/Doctrine/Migrations/autoload.php',
        '%{php_home}/Doctrine/DBAL/Migrations/autoload.php',
    ],
]);
if  (file_exists('/usr/share/pear/Predis/Autoloader.php')) {
    require_once '/usr/share/pear/Predis/Autoloader.php';
    Predis\Autoloader::register();
}
EOF

# Notice ZendDiagnostics instead of Zend/Diagnostics
cat << 'EOF' | tee zf.php
<?php
require_once '%{php_home}/Fedora/Autoloader/autoload.php';
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/%{namespace}/ZendFrameworkBridge/autoload.php',
    dirname(__DIR__) . '/%{namespace}/%{library}/autoload.php',
]);
EOF


%install
: Laminas library
mkdir -p   %{buildroot}%{php_home}/%{namespace}/
cp -pr src %{buildroot}%{php_home}/%{namespace}/%{library}

: Zend equiv
mkdir -p      %{buildroot}%{php_home}/Zend%{library}
cp -pr zf.php %{buildroot}%{php_home}/Zend%{library}/autoload.php


%check
%if %{with_tests}
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require_once '%{buildroot}%{php_home}/%{namespace}/%{library}/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('%{namespace}Test\\%{library}\\', dirname(__DIR__) . '/test');
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/org/bovigo/vfs/autoload.php',
    '%{php_home}/%{namespace}/Loader/autoload.php',
]);
EOF

: check compat autoloader
php -r '
require "%{buildroot}%{php_home}/Zend%{library}/autoload.php";
exit (class_exists("\\Zend%{library}\\Check\\IniFile") ? 0 : 1);
'

# testJitFreeSpace have erratic results as rely on free space in builder  /tmp
# testCheck have erratic results from reviewer
# test in GuzzleHttpServiceTest.php sometime fail in local build, ok in mock

: upstream test suite
ret=0
for cmdarg in "php %{phpunit}" php72 php73 php74; do
  if which $cmdarg; then
    set $cmdarg
    $1 ${2:-%{_bindir}/phpunit7} \
      --filter '^((?!(testJitFreeSpace|testCheck)).)*$' \
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
%{php_home}/Zend%{library}
%{php_home}/%{namespace}/%{library}


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Remi Collet <remi@remirepo.net> - 1.6.0-2
- cleanup

* Thu Jan 16 2020 Remi Collet <remi@remirepo.net> - 1.6.0-1
- switch to Laminas

* Mon Nov 25 2019 Remi Collet <remi@remirepo.net> - 1.6.0-1
- update to 1.6.0
- allow sensiolabs/security-checker 6
- allow symfony 5

* Wed Mar 27 2019 Remi Collet <remi@remirepo.net> - 1.5.0-1
- update to 1.5.0
- allow doctrine/migrations 2.0

* Thu Jan 10 2019 Remi Collet <remi@remirepo.net> - 1.4.0-2
- ignore tests with erratic results

* Thu Jan 10 2019 Remi Collet <remi@remirepo.net> - 1.4.0-1
- update to 1.4.0
- raise dependency on sensiolabs/security-checker 5.0

* Thu Jan  3 2019 Remi Collet <remi@remirepo.net> - 1.3.1-1
- initial package

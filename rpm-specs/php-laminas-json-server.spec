# remirepo/Fedora spec file for php-laminas-json-server
#
# Copyright (c) 2015-2020 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global bootstrap    0
%global gh_commit    5580959966a99bc110066566ca8965773ef49c13
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     laminas
%global gh_project   laminas-json-server
%global zf_name      zend-json-server
%global php_home     %{_datadir}/php
%global namespace    Laminas
%global library      Json
%global subproj      Server
%if %{bootstrap}
%global with_tests   0%{?_with_tests:1}
%else
%global with_tests   0%{!?_without_tests:1}
%endif

Name:           php-%{gh_project}
Version:        3.2.2
Release:        1%{?dist}
Summary:        %{namespace} Json-Server is a JSON-RPC server implementation

License:        BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{gh_commit}/%{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
# Tests
%if %{with_tests}
BuildRequires:  php(language) >= 5.6
BuildRequires:  php-pcre
BuildRequires:  php-reflection
BuildRequires:  php-spl
BuildRequires: (php-autoloader(%{gh_owner}/laminas-http)                 >= 2.7    with php-autoloader(%{gh_owner}/laminas-http)                 < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-json)                 >= 3.0    with php-autoloader(%{gh_owner}/laminas-json)                 < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-server)               >= 2.7    with php-autoloader(%{gh_owner}/laminas-server)               < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.0    with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
# From composer, "require-dev": {
#        "laminas/laminas-coding-standard": "~1.0.0",
#        "phpunit/phpunit": "^5.7.27 || ^6.5.8 || ^7.1.2"
%global phpunit %{_bindir}/phpunit7
BuildRequires:  phpunit7 >= 7.1.2
%endif
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer, "require": {
#        "php": "^5.6 || ^7.0",
#        "laminas/laminas-http": "^2.7",
#        "laminas/laminas-json": "^2.6.1 || ^3.0",
#        "laminas/laminas-server": "^2.7",
#        "laminas/laminas-zendframework-bridge": "^1.0"
Requires:       php(language) >= 5.6
Requires:      (php-autoloader(%{gh_owner}/laminas-http)                 >= 2.7    with php-autoloader(%{gh_owner}/laminas-http)                 < 3)
Requires:      (php-autoloader(%{gh_owner}/laminas-json)                 >= 3.0    with php-autoloader(%{gh_owner}/laminas-json)                 < 4)
Requires:      (php-autoloader(%{gh_owner}/laminas-server)               >= 2.7    with php-autoloader(%{gh_owner}/laminas-server)               < 4)
Requires:      (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.0    with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
# Autoloader
Requires:       php-composer(fedora/autoloader)
# From phpcompatinfo report for version 3.2.0
Requires:       php-pcre
Requires:       php-reflection
Requires:       php-spl

# Compatibily ensure by the bridge
Obsoletes:      php-zendframework-%{zf_name}              < 3.2.1
Provides:       php-zendframework-%{zf_name}              = %{version}
Provides:       php-composer(%{gh_owner}/%{gh_project})   = %{version}
Provides:       php-composer(zendframework/%{zf_name})    = %{version}
Provides:       php-autoloader(%{gh_owner}/%{gh_project}) = %{version}
Provides:       php-autoloader(zendframework/%{zf_name})  = %{version}


%description
Provides a JSON-RPC server implementation.

Documentation: https://docs.laminas.dev/%{gh_project}/


%prep
%setup -q -n %{gh_project}-%{gh_commit}

mv LICENSE.md LICENSE


%build
: Create autoloader
phpab --template fedora --output src/autoload.php src
cat << 'EOF' | tee -a src/autoload.php
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/%{namespace}/Json/autoload.php',
    '%{php_home}/%{namespace}/Http/autoload.php',
    '%{php_home}/%{namespace}/Server/autoload.php',
]);
EOF

cat << 'EOF' | tee zf.php
<?php
require_once '%{php_home}/Fedora/Autoloader/autoload.php';
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/%{namespace}/ZendFrameworkBridge/autoload.php',
    dirname(dirname(dirname(__DIR__))) . '/%{namespace}/%{library}/%{subproj}/autoload.php',
]);
EOF


%install
: Laminas library
mkdir -p   %{buildroot}%{php_home}/%{namespace}/%{library}/
cp -pr src %{buildroot}%{php_home}/%{namespace}/%{library}/%{subproj}

: Zend equiv
mkdir -p      %{buildroot}%{php_home}/Zend/%{library}/%{subproj}
cp -pr zf.php %{buildroot}%{php_home}/Zend/%{library}/%{subproj}/autoload.php


%check
%if %{with_tests}
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require_once '%{buildroot}%{php_home}/%{namespace}/%{library}/%{subproj}/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('%{namespace}Test\\%{library}\\%{subproj}\\', dirname(__DIR__) . '/test');
require_once __DIR__ . '/../test/TestAsset/FooFunc.php';
EOF

: check compat autoloader
php -r '
require "%{buildroot}%{php_home}/Zend/%{library}/%{subproj}/autoload.php";
exit (class_exists("\\Zend\\%{library}\\%{subproj}\\Response") ? 0 : 1);
'

: upstream test suite
ret=0
for cmdarg in "php %{phpunit}" php72 php73 php74; do
  if which $cmdarg; then
    set $cmdarg
    $1 ${2:-%{_bindir}/phpunit7} --verbose || ret=1
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
%{php_home}/Zend/%{library}/%{subproj}
%{php_home}/%{namespace}/%{library}/%{subproj}


%changelog
* Mon Mar 30 2020 Remi Collet <remi@remirepo.net> - 3.2.2-1
- update to 3.2.2

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 16 2020 Remi Collet <remi@remirepo.net> - 3.2.1-1
- update to 3.2.1

* Fri Jan 10 2020 Remi Collet <remi@remirepo.net> - 3.2.0-1
- switch to Laminas

* Fri Oct 18 2019 Remi Collet <remi@remirepo.net> - 3.2.0-1
- update to 3.2.0 (no change)

* Thu Apr 26 2018 Remi Collet <remi@remirepo.net> - 3.1.0-1
- update to 3.1.0
- raise dependency on PHP 5.6
- raise dependency on zend-http 2.7
- raise dependency on zend-server 2.7
- switch to phpunit6 or phpunit7
- use range dependencies on F27+

* Sat Dec  9 2017 Remi Collet <remi@remirepo.net> - 3.0.0-4
- switch from zend-loader to fedora/autoloader

* Wed Jun 29 2016 Remi Collet <remi@fedoraproject.org> - 3.0.0-1
- initial package

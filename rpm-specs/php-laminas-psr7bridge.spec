# remirepo/Fedora spec file for php-laminas-psr7bridge
#
# Copyright (c) 2016-2020 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global bootstrap    0
%global gh_commit    d310ce73aae9ff4723f7561539e33c79c38602fe
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     laminas
%global gh_project   laminas-psr7bridge
%global zf_name      zend-psr7bridge
%global php_home     %{_datadir}/php
%global namespace    Laminas
%global library      Psr7Bridge
%if %{bootstrap}
%global with_tests   0%{?_with_tests:1}
%else
%global with_tests   0%{!?_without_tests:1}
%endif

Name:           php-%{gh_project}
Version:        1.2.2
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
BuildRequires:  php-reflection
BuildRequires:  php-intl
BuildRequires:  php-pcre
BuildRequires:  php-spl
BuildRequires: (php-autoloader(%{gh_owner}/laminas-diactoros)            >= 1.7    with php-autoloader(%{gh_owner}/laminas-diactoros)            < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-http)                 >= 2.11   with php-autoloader(%{gh_owner}/laminas-http)                 < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.0    with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
BuildRequires: (php-composer(psr/http-message)                           >= 1.0    with php-composer(psr/http-message)                           < 2)
# From composer, "require-dev": {
#        "laminas/laminas-coding-standard": "~1.0.0",
#        "phpunit/phpunit": "^5.7.15 || ^6.5.6 || ^7.5.20"
BuildRequires:  phpunit7 >= 7.5.20
%endif
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer, "require": {
#        "php": "^5.6 || ^7.0",
#        "laminas/laminas-diactoros": "^1.7 || ^2.0",
#        "laminas/laminas-http": "^2.11",
#        "laminas/laminas-zendframework-bridge": "^1.0",
#        "psr/http-message": "^1.0"
Requires:       php(language) >= 5.6
Requires:      (php-autoloader(%{gh_owner}/laminas-diactoros)            >= 1.7    with php-autoloader(%{gh_owner}/laminas-diactoros)            < 3)
Requires:      (php-autoloader(%{gh_owner}/laminas-http)                 >= 2.11   with php-autoloader(%{gh_owner}/laminas-http)                 < 3)
Requires:      (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.0    with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
Requires:      (php-composer(psr/http-message)                           >= 1.0    with php-composer(psr/http-message)                           < 2)
# Autoloader
Requires:       php-composer(fedora/autoloader)
# From phpcompatinfo report for version 1.2.0
Requires:       php-pcre
Requires:       php-spl

# Compatibily ensure by the bridge
Obsoletes:      php-zendframework-%{zf_name}              < 1.2.1
Provides:       php-zendframework-%{zf_name}              = %{version}
Provides:       php-composer(%{gh_owner}/%{gh_project})   = %{version}
Provides:       php-composer(zendframework/%{zf_name})    = %{version}
Provides:       php-autoloader(%{gh_owner}/%{gh_project}) = %{version}
Provides:       php-autoloader(zendframework/%{zf_name})  = %{version}


%description
Code for converting PSR-7 messages to laminas-http messages, and vice versa.

Documentation: https://docs.laminas.dev/%{gh_project}/


%prep
%setup -q -n %{gh_project}-%{gh_commit}

mv LICENSE.md LICENSE


%build
: Create autoloader
phpab --template fedora --output src/autoload.php src
cat << 'EOF' | tee -a src/autoload.php
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/%{namespace}/Http/autoload.php',
    '%{php_home}/Psr/Http/Message/autoload.php',
    [
        '%{php_home}/%{namespace}/Diactoros2/autoload.php',
        '%{php_home}/%{namespace}/Diactoros/autoload.php',
    ],
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
exit (class_exists("\\Zend\\%{library}\\Psr7Response") ? 0 : 1);
'

: upstream test suite
ret=0
for cmd in php php72 php73 php74; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit7 || ret=1
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
* Mon Mar 30 2020 Remi Collet <remi@remirepo.net> - 1.2.2-1
- update to 1.2.2 (no change)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 25 2020 Remi Collet <remi@remirepo.net> - 1.2.1-1
- update to 1.2.1
- switch to phpunit7

* Fri Jan 10 2020 Remi Collet <remi@remirepo.net> - 1.2.0-1
- switch to Laminas
- update to 1.2.0
- raise dependency on PHP 5.6

* Sat Dec  9 2017 Remi Collet <remi@remirepo.net> - 0.2.2-4
- switch from zend-loader to fedora/autoloader

* Wed May 11 2016 Remi Collet <remi@fedoraproject.org> - 0.2.2-1
- update to 0.2.2

* Wed Mar  2 2016 Remi Collet <remi@fedoraproject.org> - 0.2.1-1
- initial package

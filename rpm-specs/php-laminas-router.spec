# remirepo/Fedora spec file for php-laminas-router
#
# Copyright (c) 2016-2020 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global bootstrap    0
%global gh_commit    01a6905202ad41a42ba63d60260eba32b89e18c7
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     laminas
%global gh_project   laminas-router
%global zf_name      zend-router
%global php_home     %{_datadir}/php
%global namespace    Laminas
%global library      Router
%if %{bootstrap}
%global with_tests   0%{?_with_tests:1}
%else
%global with_tests   0%{!?_without_tests:1}
%endif

Name:           php-%{gh_project}
Version:        3.3.2
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
BuildRequires:  php-pcre
BuildRequires:  php-spl
BuildRequires: (php-composer(container-interop/container-interop)        >= 1.2    with php-composer(container-interop/container-interop)        < 2)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-http)                 >= 2.8.1  with php-autoloader(%{gh_owner}/laminas-http)                 < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-servicemanager)       >= 3.3    with php-autoloader(%{gh_owner}/laminas-servicemanager)       < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-stdlib)               >= 3.2.1  with php-autoloader(%{gh_owner}/laminas-stdlib)               < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.0    with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
# From composer, "require-dev": {
#        "laminas/laminas-coding-standard": "~1.0.0",
#        "laminas/laminas-i18n": "^2.7.4",
#        "phpunit/phpunit": "^5.7.22 || ^6.4.1 || ^7.5.18"
BuildRequires: (php-autoloader(%{gh_owner}/laminas-i18n)                 >= 2.6    with php-autoloader(%{gh_owner}/laminas-i18n)                 < 3)
%global phpunit %{_bindir}/phpunit7
BuildRequires:  phpunit7 >= 7.5.18
%endif
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer, "require": {
#        "php": "^5.6 || ^7.0",
#        "container-interop/container-interop": "^1.2",
#        "laminas/laminas-http": "^2.8.1",
#        "laminas/laminas-servicemanager": "^2.7.8 || ^3.3",
#        "laminas/laminas-stdlib": "^3.2.1",
#        "laminas/laminas-zendframework-bridge": "^1.0"
Requires:       php(language) >= 5.6
%if ! %{bootstrap}
Requires:      (php-composer(container-interop/container-interop)        >= 1.2    with php-composer(container-interop/container-interop)        < 2)
Requires:      (php-autoloader(%{gh_owner}/laminas-http)                 >= 2.8.1  with php-autoloader(%{gh_owner}/laminas-http)                 < 3)
Requires:      (php-autoloader(%{gh_owner}/laminas-servicemanager)       >= 3.3    with php-autoloader(%{gh_owner}/laminas-servicemanager)       < 4)
Requires:      (php-autoloader(%{gh_owner}/laminas-stdlib)               >= 3.2.1  with php-autoloader(%{gh_owner}/laminas-stdlib)               < 4)
Requires:      (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.0    with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
# From composer, "suggest": {
#        "zendframework/zend-i18n": "^2.6, if defining translatable HTTP path segments"
Suggests:       php-autoloader(%{gh_owner}/laminas-i18n)
# From composer, "conflict": {
#       "laminas/laminas-mvc": "<3.0.0"
Conflicts:      php-composer(%{gh_owner}/laminas-mvc)                <  3
%endif
# Autoloader
Requires:       php-composer(fedora/autoloader)
# From phpcompatinfo report for version 3.3.1
Requires:       php-pcre
Requires:       php-spl

# Compatibily ensure by the bridge
Obsoletes:      php-zendframework-%{zf_name}              < 3.3.1
Provides:       php-zendframework-%{zf_name}              = %{version}
Provides:       php-composer(%{gh_owner}/%{gh_project})   = %{version}
Provides:       php-composer(zendframework/%{zf_name})    = %{version}
Provides:       php-autoloader(%{gh_owner}/%{gh_project}) = %{version}
Provides:       php-autoloader(zendframework/%{zf_name})  = %{version}


%description
%{gh_project} provides flexible HTTP routing.

Routing currently works against the laminas-http request and responses,
and provides capabilities around:

* Literal path matches
* Path segment matches (at path boundaries, and optionally validated
  using regex)
* Regular expression path matches
* HTTP request scheme
* HTTP request method
* Hostname

Additionally, it supports combinations of different route types in tree
structures, allowing for fast, b-tree lookups.

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
    '%{php_home}/%{namespace}/Http/autoload.php',
    '%{php_home}/%{namespace}/ServiceManager/autoload.php',
    '%{php_home}/%{namespace}/Stdlib/autoload.php',
]);
\Fedora\Autoloader\Dependencies::optional([
    '%{php_home}/%{namespace}/I18n/autoload.php',
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
exit (class_exists("\\Zend\\%{library}\\RouterFactory") ? 0 : 1);
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
* Mon Mar 30 2020 Remi Collet <remi@remirepo.net> - 3.3.2-1
- update to 3.3.2 (no change)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 10 2020 Remi Collet <remi@remirepo.net> - 3.3.1-1
- switch to Laminas
- update to 3.3.1

* Wed Feb 27 2019 Remi Collet <remi@remirepo.net> - 3.3.0-1
- update to 3.3.0 (no change)
- raise dependency on zendframework/zend-stdlib 3.2.1

* Mon Feb 11 2019 Remi Collet <remi@remirepo.net> - 3.2.1-1
- update to 3.2.1

* Mon Aug 20 2018 Remi Collet <remi@remirepo.net> - 3.2.0-1
- update to 3.2.0
- raise dependency on zendframework/zend-http 2.8.1

* Tue Jun 19 2018 Remi Collet <remi@remirepo.net> - 3.1.0-1
- update to 3.1.0
- raise dependency on PHP 5.6
- raise dependency on container-interop/container-interop 1.2
- raise dependency on zendframework/zend-http 2.6
- raise dependency on zendframework/zend-servicemanager 2.7.8
- raise dependency on zendframework/zend-stdlib 2.7.7

* Sat Dec  9 2017 Remi Collet <remi@remirepo.net> - 3.0.2-5
- switch from zend-loader to fedora/autoloader

* Tue Oct 24 2017 Remi Collet <remi@fedoraproject.org> - 3.0.2-4
- fix FTBFS from Koschei, add patch for PHP 7.2 from
  https://github.com/zendframework/zend-router/pull/39

* Wed Jun 29 2016 Remi Collet <remi@fedoraproject.org> - 3.0.2-1
- update to 3.0.2

* Tue Apr 19 2016 Remi Collet <remi@fedoraproject.org> - 3.0.1-1
- initial package


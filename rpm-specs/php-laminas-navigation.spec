# remirepo/Fedora spec file for php-laminas-navigation
#
# Copyright (c) 2015-2020 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
# when build without permission-acl
%global bootstrap    1
%global gh_commit    1b4210ea3afeffb8a69e502e169088180ba3275d
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     laminas
%global gh_project   laminas-navigation
%global zf_name      zend-navigation
%global php_home     %{_datadir}/php
%global namespace    Laminas
%global library      Navigation
%global with_tests   0%{!?_without_tests:1}

Name:           php-%{gh_project}
Version:        2.9.1
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
BuildRequires:  php-pcre
BuildRequires:  php-spl
# From composer, "require-dev": {
#        "laminas/laminas-coding-standard": "~1.0.0",
#        "laminas/laminas-config": "^2.6 || ^3.1",
#        "laminas/laminas-console": "^2.6",
#        "laminas/laminas-http": "^2.6",
#        "laminas/laminas-i18n": "^2.7.3",
#        "laminas/laminas-log": "^2.9.1",
#        "laminas/laminas-mvc": "^2.7.9 || ^3.0.4",
#        "laminas/laminas-permissions-acl": "^2.6",
#        "laminas/laminas-router": "^3.0.2",
#        "laminas/laminas-servicemanager": "^2.7.5 || ^3.0.3",
#        "laminas/laminas-uri": "^2.5.2",
#        "laminas/laminas-view": "^2.9",
#        "phpunit/phpunit": "^5.7.27 || ^6.5.8 || ^7.1.2"
BuildRequires: (php-autoloader(%{gh_owner}/laminas-stdlib)               >= 3.0     with php-autoloader(%{gh_owner}/laminas-stdlib)               < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.0     with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-config)               >= 2.6     with php-autoloader(%{gh_owner}/laminas-config)               < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-console)              >= 2.6     with php-autoloader(%{gh_owner}/laminas-console)              < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-http)                 >= 2.6     with php-autoloader(%{gh_owner}/laminas-http)                 < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-i18n)                 >= 2.7.3   with php-autoloader(%{gh_owner}/laminas-i18n)                 < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-log)                  >= 2.9.1   with php-autoloader(%{gh_owner}/laminas-log)                  < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-mvc)                  >= 3.0.4   with php-autoloader(%{gh_owner}/laminas-mvc)                  < 4)
%if ! %{bootstrap}
BuildRequires: (php-autoloader(%{gh_owner}/laminas-permissions-acl)      >= 2.6     with php-autoloader(%{gh_owner}/laminas-permissions-acl)      < 3)
%endif
BuildRequires: (php-autoloader(%{gh_owner}/laminas-router)               >= 3.0.2   with php-autoloader(%{gh_owner}/laminas-router)               < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-servicemanager)       >= 3.0.3   with php-autoloader(%{gh_owner}/laminas-servicemanager)       < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-uri)                  >= 2.5.2   with php-autoloader(%{gh_owner}/laminas-uri)                  < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-view)                 >= 2.9     with php-autoloader(%{gh_owner}/laminas-view)                 < 3)
%global phpunit %{_bindir}/phpunit7
BuildRequires:  phpunit7 >= 7.1.2
%endif
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer, "require": {
#        "php": "^5.6 || ^7.0",
#        "laminas/laminas-stdlib": "^2.7 || ^3.0",
#        "laminas/laminas-zendframework-bridge": "^1.0"
Requires:       php(language) >= 5.6
Requires:      (php-autoloader(%{gh_owner}/laminas-stdlib)               >= 3.0     with php-autoloader(%{gh_owner}/laminas-stdlib)               < 4)
Requires:      (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.0     with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
# From composer, "suggest": {
#        "laminas/laminas-config": "^2.6 || ^3.1, to provide page configuration (optional, as arrays and Traversables are also allowed)",
#        "laminas/laminas-permissions-acl": "^2.6, to provide ACL-based access restrictions to pages",
#        "laminas/laminas-router": "^3.0, to use router-based URI generation with Mvc pages",
#        "laminas/laminas-servicemanager": "^2.7.5 || ^3.0.3, to use the navigation factories",
#        "laminas/laminas-view": "^2.8.1, to use the navigation view helpers"
Suggests:       php-autoloader(%{gh_owner}/laminas-config)
Suggests:       php-autoloader(%{gh_owner}/laminas-permissions-acl)
Suggests:       php-autoloader(%{gh_owner}/laminas-servicemanager)
Suggests:       php-autoloader(%{gh_owner}/laminas-router)
Suggests:       php-autoloader(%{gh_owner}/laminas-view)
# Autoloader
Requires:       php-composer(fedora/autoloader)
# From phpcompatinfo report for version 2.9.1
Requires:       php-pcre
Requires:       php-reflection
Requires:       php-spl

# Compatibily ensure by the bridge
Obsoletes:      php-zendframework-%{zf_name}              < 2.9.1-99
Provides:       php-zendframework-%{zf_name}              = %{version}-99
Provides:       php-composer(%{gh_owner}/%{gh_project})   = %{version}
Provides:       php-composer(zendframework/%{zf_name})    = %{version}
Provides:       php-autoloader(%{gh_owner}/%{gh_project}) = %{version}
Provides:       php-autoloader(zendframework/%{zf_name})  = %{version}


%description
%{namespace}\Navigation is a component for managing trees of pointers to web pages.
Simply put: It can be used for creating menus, breadcrumbs, links,
and sitemaps, or serve as a model for other navigation related purposes.

Documentation: https://docs.laminas.dev/%{gh_project}/


%prep
%setup -q -n %{gh_project}-%{gh_commit}

mv LICENSE.md LICENSE


%build
: Generate autoloader
phpab --template fedora --output src/autoload.php src
cat << 'EOF' | tee -a src/autoload.php
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/%{namespace}/Stdlib/autoload.php',
]);
\Fedora\Autoloader\Dependencies::optional([
    [
        '%{php_home}/%{namespace}/Config3/autoload.php',
        '%{php_home}/%{namespace}/Config/autoload.php',
    ],
    '%{php_home}/%{namespace}/Permissions/Acl/autoload.php',
    '%{php_home}/%{namespace}/ServiceManager/autoload.php',
    '%{php_home}/%{namespace}/Router/autoload.php',
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
    '%{php_home}/%{namespace}/Console/autoload.php',
    '%{php_home}/%{namespace}/Http/autoload.php',
    '%{php_home}/%{namespace}/I18n/autoload.php',
    '%{php_home}/%{namespace}/Log/autoload.php',
    '%{php_home}/%{namespace}/Mvc/autoload.php',
    '%{php_home}/%{namespace}/Uri/autoload.php',
]);
\Fedora\Autoloader\Autoload::addPsr4('%{namespace}Test\\%{library}\\', dirname(__DIR__) . '/test');
EOF

: check compat autoloader
php -r '
require "%{buildroot}%{php_home}/Zend/%{library}/autoload.php";
exit (class_exists("\\Zend\\%{library}\\%{library}") ? 0 : 1);
'

# testProvidesExpectedConfiguration need fix after Laminas move
: upstream test suite
ret=0
for cmdarg in "php %{phpunit}" php72 php73 php74; do
  if which $cmdarg; then
    set $cmdarg
    $1 ${2:-%{_bindir}/phpunit7} \
%if %{bootstrap}
      --filter '^((?!(testProvidesExpectedConfiguration|testSetResourceInterface)).)*$' \
%else
      --filter '^((?!(testProvidesExpectedConfiguration)).)*$' \
%endif
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
%{php_home}/Zend/%{library}
%{php_home}/%{namespace}/%{library}


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 27 2020 Remi Collet <remi@remirepo.net> - 2.9.1-3
- bootstrap build without permissions-acl

* Mon Jan 20 2020 Remi Collet <remi@remirepo.net> - 2.9.1-2
- allow laminas-config v3

* Thu Jan 16 2020 Remi Collet <remi@remirepo.net> - 2.9.1-1
- switch to Laminas

* Wed Aug 21 2019 Remi Collet <remi@remirepo.net> - 2.9.1-2
- update to 2.9.1

* Thu Apr 26 2018 Remi Collet <remi@remirepo.net> - 2.9.0-2
- update to 2.9.0
- raise dependency to PHP 5.6
- switch to phpunit6 or phpunit7
- use range dependencies on F27+

* Wed Dec 13 2017 Remi Collet <remi@remirepo.net> - 2.8.2-3
- switch from zend-loader to fedora/autoloader

* Thu Mar 23 2017 Remi Collet <remi@remirepo.net> - 2.8.2-1
- Update to 2.8.2

* Tue Jun 14 2016 Remi Collet <remi@fedoraproject.org> - 2.8.1-1
- update to 2.8.1

* Fri Apr  8 2016 Remi Collet <remi@fedoraproject.org> - 2.7.1-1
- update to 2.7.1

* Mon Mar 21 2016 Remi Collet <remi@fedoraproject.org> - 2.6.1-1
- update to 2.6.1

* Thu Feb 25 2016 Remi Collet <remi@fedoraproject.org> - 2.6.0-1
- update to 2.6.0
- raise dependency on PHP >= 5.5
- raise dependency on zend-stdlib >= 2.7

* Tue Aug  4 2015 Remi Collet <remi@fedoraproject.org> - 2.5.1-1
- initial package

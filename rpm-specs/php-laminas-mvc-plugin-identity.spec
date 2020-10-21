# remirepo/Fedora spec file for php-laminas-mvc-plugin-identity
#
# Copyright (c) 2016-2020 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global bootstrap    0
%global gh_commit    0dc0c349be0faee67bbb4ae2a0206435a7a51516
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     laminas
%global gh_project   laminas-mvc-plugin-identity
%global zf_name      zend-mvc-plugin-identity
%global php_home     %{_datadir}/php
%global namespace    Laminas
%global library      Mvc
%global subproj      Plugin
%global subsubp      Identity
%if %{bootstrap}
%global with_tests   0%{?_with_tests:1}
%else
%global with_tests   0%{!?_without_tests:1}
%endif

Name:           php-%{gh_project}
Version:        1.1.1
Release:        3%{?dist}
Summary:        %{namespace} Framework %{library}/%{subproj}/%{subsubp} component

License:        BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{gh_commit}/%{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
# Tests
%if %{with_tests}
BuildRequires:  php(language) >= 5.6
BuildRequires:  php-spl
BuildRequires: (php-composer(container-interop/container-interop)        >= 1.1    with php-composer(container-interop/container-interop)        < 2)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-authentication)       >= 2.5.3  with php-autoloader(%{gh_owner}/laminas-authentication)       < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-mvc)                  >= 3.0    with php-autoloader(%{gh_owner}/laminas-mvc)                  < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-servicemanager)       >= 3.0.3  with php-autoloader(%{gh_owner}/laminas-servicemanager)       < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.0    with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
# From composer, "require-dev": {
#        "laminas/laminas-coding-standard": "~1.0.0",
#        "phpunit/phpunit": "^5.7.27 || ^6.5.8 || ^7.1.4"
%global phpunit %{_bindir}/phpunit7
BuildRequires:  phpunit7 >= 7.1.4
%endif
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer, "require": {
#        "php": "^5.6 || ^7.0",
#        "container-interop/container-interop": "^1.1",
#        "laminas/laminas-authentication": "^2.5.3",
#        "laminas/laminas-mvc": "^3.0",
#        "laminas/laminas-servicemanager": "^2.7.5 || ^3.0.3",
#        "laminas/laminas-zendframework-bridge": "^1.0"
Requires:       php(language) >= 5.6
Requires:      (php-composer(container-interop/container-interop)        >= 1.1    with php-composer(container-interop/container-interop)        < 2)
Requires:      (php-autoloader(%{gh_owner}/laminas-authentication)       >= 2.5.3  with php-autoloader(%{gh_owner}/laminas-authentication)       < 3)
Requires:      (php-autoloader(%{gh_owner}/laminas-mvc)                  >= 3.0    with php-autoloader(%{gh_owner}/laminas-mvc)                  < 4)
Requires:      (php-autoloader(%{gh_owner}/laminas-servicemanager)       >= 3.0.3  with php-autoloader(%{gh_owner}/laminas-servicemanager)       < 4)
Requires:      (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.0    with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
# Autoloader
Requires:       php-composer(fedora/autoloader)
# From phpcompatinfo report for version 1.1.1
Requires:       php-spl

# Compatibily ensure by the bridge
Obsoletes:      php-zendframework-%{zf_name}              < 1.1.1-99
Provides:       php-zendframework-%{zf_name}              = %{version}-99
Provides:       php-composer(%{gh_owner}/%{gh_project})   = %{version}
Provides:       php-composer(zendframework/%{zf_name})    = %{version}
Provides:       php-autoloader(%{gh_owner}/%{gh_project}) = %{version}
Provides:       php-autoloader(zendframework/%{zf_name})  = %{version}


%description
Provides a laminas-mvc plugin (for versions 3.0 and up) that allows retrieving
the current identity as provided by laminas-authentication.

Documentation: https://docs.laminas.dev/%{gh_project}/


%prep
%setup -q -n %{gh_project}-%{gh_commit}

mv LICENSE.md LICENSE


%build
: Generate autoloader
phpab --template fedora --output src/autoload.php src
cat << 'EOF' | tee -a src/autoload.php
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/Interop/Container/autoload.php',
    '%{php_home}/%{namespace}/Mvc/autoload.php',
    '%{php_home}/%{namespace}/Authentication/autoload.php',
    '%{php_home}/%{namespace}/ServiceManager/autoload.php',
]);
EOF

cat << 'EOF' | tee zf.php
<?php
require_once '%{php_home}/Fedora/Autoloader/autoload.php';
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/%{namespace}/ZendFrameworkBridge/autoload.php',
    dirname(dirname(dirname(dirname(__DIR__)))) . '/%{namespace}/%{library}/%{subproj}/%{subsubp}/autoload.php',
]);
EOF
 

%install
: Laminas library
mkdir -p   %{buildroot}%{php_home}/%{namespace}/%{library}/%{subproj}
cp -pr src %{buildroot}%{php_home}/%{namespace}/%{library}/%{subproj}/%{subsubp}
 
: Zend equiv
mkdir -p      %{buildroot}%{php_home}/Zend/%{library}/%{subproj}/%{subsubp}
cp -pr zf.php %{buildroot}%{php_home}/Zend/%{library}/%{subproj}/%{subsubp}/autoload.php


%check
%if %{with_tests}
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require_once '%{buildroot}%{php_home}/%{namespace}/%{library}/%{subproj}/%{subsubp}/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('%{namespace}Test\\%{library}\\%{subproj}\\%{subsubp}\\', dirname(__DIR__) . '/test');
EOF

: check compat autoloader
php -r '
require "%{buildroot}%{php_home}/Zend/%{library}/%{subproj}/%{subsubp}/autoload.php";
exit (class_exists("\\Zend\\%{library}\\%{subproj}\\%{subsubp}\\Module") ? 0 : 1);
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
%dir %{php_home}/Zend/%{library}/%{subproj}
     %{php_home}/Zend/%{library}/%{subproj}/%{subsubp}
%dir %{php_home}/%{namespace}/%{library}/%{subproj}
     %{php_home}/%{namespace}/%{library}/%{subproj}/%{subsubp}


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 16 2020 Remi Collet <remi@remirepo.net> - 1.1.1-1
- switch to Laminas

* Fri Oct 18 2019 Remi Collet <remi@remirepo.net> - 1.1.1-1
- update to 1.1.1 (no change)

* Thu May  3 2018 Remi Collet <remi@remirepo.net> - 1.1.0-1
- update to 1.1.0
- use range dependencies on F27+
- switch to phpunit6 or phpunit7

* Wed Dec 13 2017 Remi Collet <remi@remirepo.net> - 1.0.0-4
- switch from zend-loader to fedora/autoloader

* Wed Jun 29 2016 Remi Collet <remi@fedoraproject.org> - 1.0.0-1
- initial package


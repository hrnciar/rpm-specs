# remirepo/Fedora spec file for php-laminas-barcode
#
# Copyright (c) 2015-2020 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global bootstrap    0
%global gh_commit    7806b774328a32b1f121f2972c72a0ded85939e1
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     laminas
%global gh_project   laminas-barcode
%global zf_name      zend-barcode
%global php_home     %{_datadir}/php
%global namespace    Laminas
%global library      Barcode
%if %{bootstrap}
%global with_tests   0%{?_with_tests:1}
%else
%global with_tests   0%{!?_without_tests:1}
%endif

Name:           php-%{gh_project}
Version:        2.8.2
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

BuildRequires:  php-dom
BuildRequires:  php-gd
BuildRequires:  php-iconv
BuildRequires:  php-pcre
BuildRequires:  php-spl
BuildRequires: (php-autoloader(%{gh_owner}/laminas-servicemanager)       >= 3.3    with php-autoloader(%{gh_owner}/laminas-servicemanager)       < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-stdlib)               >= 3.1    with php-autoloader(%{gh_owner}/laminas-stdlib)               < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-validator)            >= 2.10.1 with php-autoloader(%{gh_owner}/laminas-validator)            < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.0    with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
# From composer, "require-dev": {
#        "laminas/laminas-coding-standard": "~1.0.0",
#        "laminas/laminas-config": "^2.6 || ^3.1",
#        "phpunit/phpunit": "^5.7.23 || ^6.4.3 || ^7.5.20",
#        "zendframework/zendpdf": "^2.0.2"
BuildRequires: (php-autoloader(%{gh_owner}/laminas-config)               >= 2.6    with php-autoloader(%{gh_owner}/laminas-config)               < 4)
BuildRequires: (php-autoloader(zendframework/zendpdf)                    >= 2.0.2  with php-autoloader(zendframework/zendpdf)                    < 3)
%global phpunit %{_bindir}/phpunit7
BuildRequires:  phpunit7 >= 7.5.20
%endif
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer, "require": {
#        "php": "^5.6 || ^7.0",
#        "laminas/laminas-servicemanager": "^2.7.8 || ^3.3",
#        "laminas/laminas-stdlib": "^2.7.7 || ^3.1",
#        "laminas/laminas-validator": "^2.10.1",
#        "laminas/laminas-zendframework-bridge": "^1.0"
Requires:       php(language) >= 5.6
Requires:      (php-autoloader(%{gh_owner}/laminas-servicemanager)       >= 3.3    with php-autoloader(%{gh_owner}/laminas-servicemanager)       < 4)
Requires:      (php-autoloader(%{gh_owner}/laminas-stdlib)               >= 3.1    with php-autoloader(%{gh_owner}/laminas-stdlib)               < 4)
Requires:      (php-autoloader(%{gh_owner}/laminas-validator)            >= 2.10.1 with php-autoloader(%{gh_owner}/laminas-validator)            < 3)
Requires:      (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.0    with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
# From composer, "suggest": {
#        "zendframework/zendpdf": "ZendPdf component"
Suggests:       php-autoloader(zendframework/zendpdf)
# Autoloader
Requires:       php-composer(fedora/autoloader)
# From phpcompatinfo report for version 2.8.0
Requires:       php-dom
Requires:       php-gd
Requires:       php-iconv
Requires:       php-pcre
Requires:       php-spl

# Compatibily ensure by the bridge
Obsoletes:      php-zendframework-%{zf_name}              < 2.8.1
Provides:       php-zendframework-%{zf_name}              = %{version}
Provides:       php-composer(%{gh_owner}/%{gh_project})   = %{version}
Provides:       php-composer(zendframework/%{zf_name})    = %{version}
Provides:       php-autoloader(%{gh_owner}/%{gh_project}) = %{version}
Provides:       php-autoloader(zendframework/%{zf_name})  = %{version}


%description
%{namespace}\Barcode provides a generic way to generate barcodes.
The %{namespace}\Barcode component is divided into two subcomponents:
barcode objects and renderers. Objects allow you to create barcodes
independently of the renderer. Renderer allow you to draw barcodes based
on the support required.

Documentation: https://docs.laminas.dev/%{gh_project}/


%prep
%setup -q -n %{gh_project}-%{gh_commit}

mv LICENSE.md LICENSE


%build
phpab --template fedora --output src/autoload.php src
cat << 'EOF' | tee -a src/autoload.php
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/%{namespace}/Stdlib/autoload.php',
    '%{php_home}/%{namespace}/Validator/autoload.php',
    '%{php_home}/%{namespace}/ServiceManager/autoload.php',
]);
\Fedora\Autoloader\Dependencies::optional([
    '%{php_home}/ZendPdf/autoload.php',
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
    [
        '%{php_home}/%{namespace}/Config3/autoload.php',
        '%{php_home}/%{namespace}/Config/autoload.php',
    ],
]);
\Fedora\Autoloader\Autoload::addPsr4('%{namespace}Test\\%{library}\\', dirname(__DIR__) . '/test');
EOF

: check compat autoloader
php -r '
require "%{buildroot}%{php_home}/Zend/%{library}/autoload.php";
exit (class_exists("\\Zend\\%{library}\\Barcode") ? 0 : 1);
'

: upstream test suite
export TESTS_LAMINAS_BARCODE_PDF_SUPPORT=1
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
%{php_home}/Zend/%{library}
%{php_home}/%{namespace}/%{library}


%changelog
* Mon Mar 30 2020 Remi Collet <remi@remirepo.net> - 2.8.2-1
- update to 2.8.2 (no change)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 25 2020 Remi Collet <remi@remirepo.net> - 2.8.1-1
- update to 2.8.1
- switch to phpunit7
- drop patch merged upstream

* Fri Jan 17 2020 Remi Collet <remi@remirepo.net> - 2.8.0-2
- cleanup

* Fri Jan 10 2020 Remi Collet <remi@remirepo.net> - 2.8.0-1
- switch to Laminas

* Thu Jan  2 2020 Remi Collet <remi@remirepo.net> - 2.8.0-1
- update to 2.8.0
- add patch for PHP 7.4 from
  https://github.com/laminas/laminas-barcode/pull/2

* Mon Sep 23 2019 Remi Collet <remi@remirepo.net> - 2.7.1-1
- update to 2.7.1

* Tue Dec 12 2017 Remi Collet <remi@remirepo.net> - 2.7.0-1
- Update to 2.7.0
- raise dependency on PHP 5.6
- raise dependency on zend-servicemanager 2.7.8
- raise dependency on zend-stdlib 2.7.7
- raise dependency on zend-validator 2.10.1
- use phpunit6 on F26+

* Thu Dec  7 2017 Remi Collet <remi@remirepo.net> - 2.6.0-5
- switch from zend-loader to fedora/autoloader
- run PDF tests

* Fri Oct 20 2017 Remi Collet <remi@fedoraproject.org> - 2.6.0-4
- fix FTBFS from Koschei, add patch for PHP 7.2 from
  https://github.com/zendframework/zend-barcode/pull/36

* Thu Feb 18 2016 Remi Collet <remi@fedoraproject.org> - 2.6.0-1
- update to 2.6.0
- raise dependency on zend-stdlib ^2.7
- raise dependency on zend-servicemanager ^2.7.5

* Thu Aug  6 2015 Remi Collet <remi@fedoraproject.org> - 2.5.2-2
- add optional dependency on zendframework/zendpdf

* Tue Aug  4 2015 Remi Collet <remi@fedoraproject.org> - 2.5.2-1
- initial package

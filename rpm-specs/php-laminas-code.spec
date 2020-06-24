# remirepo/Fedora spec file for php-laminas-code
#
# Copyright (c) 2015-2020 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global bootstrap    0
%global gh_commit    1cb8f203389ab1482bf89c0e70a04849bacd7766
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     laminas
%global gh_project   laminas-code
%global zf_name      zend-code
%global php_home     %{_datadir}/php
%global namespace    Laminas
%global library      Code
%if %{bootstrap}
%global with_tests   0%{?_with_tests:1}
%else
%global with_tests   0%{!?_without_tests:1}
%endif

Name:           php-%{gh_project}
Version:        3.4.1
Release:        3%{?dist}
Summary:        Laminas Framework %{library} component

License:        BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{gh_commit}/%{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
# Tests
%if %{with_tests}
BuildRequires:  php(language) >= 7.2
BuildRequires:  php-pcre
BuildRequires:  php-reflection
BuildRequires:  php-spl
BuildRequires:  php-tokenizer
BuildRequires: (php-autoloader(%{gh_owner}/laminas-eventmanager)       >= 3.0   with php-autoloader(%{gh_owner}/laminas-eventmanager)       < 4)
BuildRequires: (php-composer(%{gh_owner}/laminas-zendframework-bridge) >= 1.0   with php-composer(%{gh_owner}/laminas-zendframework-bridge) < 2)
# From composer, "require-dev": {
#        "ext-phar": "*",
#        "doctrine/annotations": "^1.7",
#        "laminas/laminas-coding-standard": "^1.0",
#        "laminas/laminas-stdlib": "^2.7 || ^3.0",
#        "phpunit/phpunit": "^7.5.16 || ^8.4"
BuildRequires: (php-composer(doctrine/annotations)                     >= 1.7    with php-composer(doctrine/annotations)                    < 2)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-stdlib)             >= 3.0    with php-autoloader(%{gh_owner}/laminas-stdlib)            < 4)
BuildRequires:  phpunit8 >= 8.4
%endif
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer, "require": {
#        "php": "^7.1",
#        "laminas/laminas-eventmanager": "^2.6 || ^3.0",
#        "laminas/laminas-zendframework-bridge": "^1.0"
Requires:       php(language) >= 7.1
%if ! %{bootstrap}
Requires:      (php-autoloader(%{gh_owner}/laminas-eventmanager)       >= 3.0   with php-autoloader(%{gh_owner}/laminas-eventmanager)       < 4)
Requires:      (php-composer(%{gh_owner}/laminas-zendframework-bridge) >= 1.0   with php-composer(%{gh_owner}/laminas-zendframework-bridge) < 2)
# From composer, "suggest": {
#         "doctrine/annotations": "Doctrine\\Common\\Annotations >=1.0 for annotation features",
#         "laminas/laminas-stdlib": "Laminas\\Stdlib component"
Suggests:       php-composer(doctrine/annotations)
Suggests:       php-autoloader(%{gh_owner}/laminas-stdlib)
# Autoloader
Requires:       php-composer(fedora/autoloader)
%endif
# From phpcompatinfo report for version 3.4.1
Requires:       php-pcre
Requires:       php-reflection
Requires:       php-spl
Requires:       php-tokenizer

# Compatibily ensure by the bridge
Obsoletes:      php-zendframework-%{zf_name}              < 3.4.1-99
Provides:       php-zendframework-%{zf_name}              = %{version}-99
Provides:       php-composer(%{gh_owner}/%{gh_project})   = %{version}
Provides:       php-composer(zendframework/%{zf_name})    = %{version}
Provides:       php-autoloader(%{gh_owner}/%{gh_project}) = %{version}
Provides:       php-autoloader(zendframework/%{zf_name})  = %{version}


%description
%{gh_project} provides facilities to generate arbitrary code using
an object-oriented interface, both to create new code as well as to update
existing code. While the current implementation is limited to generating
PHP code, you can easily extend the base class in order to provide code
generation for other tasks: JavaScript, configuration files, apache vhosts,
etc.

Documentation: https://docs.laminas.dev/%{gh_project}/


%prep
%setup -q -n %{gh_project}-%{gh_commit}

mv LICENSE.md LICENSE


%build
: Create autoloader
phpab --template fedora --output src/autoload.php src
cat << 'EOF' | tee -a src/autoload.php
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/%{namespace}/EventManager/autoload.php',
]);
\Fedora\Autoloader\Dependencies::optional([
    '%{php_home}/Doctrine/Common/Annotations/autoload.php',
    '%{php_home}/%{namespace}/Stdlib/autoload.php',
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

ret=0
for cmd in php php72 php73 php74; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit8 --verbose || ret=1
  fi
done

: check compat autoloader
php -r '
require "%{buildroot}%{php_home}/Zend/%{library}/autoload.php";
exit (class_exists("\\Zend\\%{library}\\NameInformation") ? 0 : 1);
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
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Remi Collet <remi@remirepo.net> - 3.4.1-2
- cleanup

* Tue Jan  7 2020 Remi Collet <remi@remirepo.net> - 3.4.1-1
- switch to Laminas

* Wed Dec 11 2019 Remi Collet <remi@remirepo.net> - 3.4.1-1
- update to 3.4.1

* Mon Oct  7 2019 Remi Collet <remi@remirepo.net> - 3.4.0-1
- update to 3.4.0
- drop patch merged upstream
- use phpunit8

* Mon Sep  2 2019 Remi Collet <remi@remirepo.net> - 3.3.2-2
- update to 3.3.2
- use phpunit7
- use range dependencies
- add patch for PHP 7.4 from
  https://github.com/zendframework/zend-code/pull/172

* Mon Aug 20 2018 Remi Collet <remi@remirepo.net> - 3.3.1-1
- update to 3.3.1

* Tue Nov 28 2017 Remi Collet <remi@remirepo.net> - 3.3.0-2
- switch from zend-loader to fedora/autoloader

* Sat Oct 21 2017 Remi Collet <remi@remirepo.net> - 3.3.0-1
- Update to 3.3.0

* Fri Aug  4 2017 Remi Collet <remi@remirepo.net> - 3.2.0-1
- Update to 3.2.0
- raise dependency on PHP 7.1
- switch to phpunit6

* Tue Oct 25 2016 Remi Collet <remi@fedoraproject.org> - 3.1.0-1
- update to 3.1.0
- raise dependency on PHP 5.6

* Fri Jul  1 2016 Remi Collet <remi@fedoraproject.org> - 3.0.4-1
- update to 3.0.4

* Wed Jun 29 2016 Remi Collet <remi@fedoraproject.org> - 3.0.3-2
- add patch for ocramius/proxy-manager
  https://github.com/zendframework/zend-code/pull/80

* Wed Jun 29 2016 Remi Collet <remi@fedoraproject.org> - 3.0.3-1
- update to 3.0.0 for ZendFramework 3

* Thu Apr 21 2016 Remi Collet <remi@fedoraproject.org> - 2.6.3-1
- update to 2.6.3

* Thu Jan 28 2016 Remi Collet <remi@fedoraproject.org> - 2.6.2-1
- update to 2.6.2
- dependency on doctrine/annotations instrad of doctrine/common
- raise dependency on zend-stdlib ~2.7
- raise dependency on zend-eventmanager ~2.6

* Thu Nov 19 2015 Remi Collet <remi@fedoraproject.org> - 2.5.3-1
- update to 2.5.3
- run test suite with both PHP 5 and 7 when available

* Tue Aug  4 2015 Remi Collet <remi@fedoraproject.org> - 2.5.2-1
- initial package
- open https://github.com/zendframework/zend-code/pull/5
  avoid using 'vendor' path

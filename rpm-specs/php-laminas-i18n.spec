# remirepo/Fedora spec file for php-laminas-i18n
#
# Copyright (c) 2015-2020 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
# When buid without config, filter, validator an view
%global bootstrap    0
%global gh_commit    94ff957a1366f5be94f3d3a9b89b50386649e3ae
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     laminas
%global gh_project   laminas-i18n
%global zf_name      zend-i18n
%global php_home     %{_datadir}/php
%global namespace    Laminas
%global library      I18n
%global with_tests   0%{!?_without_tests:1}

Name:           php-%{gh_project}
Version:        2.10.3
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
BuildRequires:  php-intl
BuildRequires:  php-pcre
BuildRequires:  php-spl
# From composer, "require-dev": {
#        "laminas/laminas-cache": "^2.6.1",
#        "laminas/laminas-coding-standard": "~1.0.0",
#        "laminas/laminas-config": "^2.6",
#        "laminas/laminas-eventmanager": "^2.6.2 || ^3.0",
#        "laminas/laminas-filter": "^2.6.1",
#        "laminas/laminas-servicemanager": "^2.7.5 || ^3.0.3",
#        "laminas/laminas-validator": "^2.6",
#        "laminas/laminas-view": "^2.6.3",
#        "phpunit/phpunit": "^5.7.27 || ^6.5.14 || ^7.5.16"
BuildRequires: (php-autoloader(%{gh_owner}/laminas-stdlib)               >= 3.0   with php-autoloader(%{gh_owner}/laminas-stdlib)               < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.0   with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-cache)                >= 2.6.1 with php-autoloader(%{gh_owner}/laminas-cache)                < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-eventmanager)         >= 3.0   with php-autoloader(%{gh_owner}/laminas-eventmanager)         < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-servicemanager)       >= 3.0.3 with php-autoloader(%{gh_owner}/laminas-servicemanager)       < 4)
%if ! %{bootstrap}
BuildRequires: (php-autoloader(%{gh_owner}/laminas-config)               >= 2.6   with php-autoloader(%{gh_owner}/laminas-config)               < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-filter)               >= 2.5   with php-autoloader(%{gh_owner}/laminas-filter)               < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-validator)            >= 2.6   with php-autoloader(%{gh_owner}/laminas-validator)            < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-view)                 >= 2.6.3 with php-autoloader(%{gh_owner}/laminas-view)                 < 3)
%endif
%global phpunit %{_bindir}/phpunit7
BuildRequires:  phpunit7 >= 7.5.16
%endif
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer, "require": {
#        "php": "^5.6 || ^7.0",
#        "ext-intl": "*",
#        "laminas/laminas-stdlib": "^2.7 || ^3.0",
#        "laminas/laminas-zendframework-bridge": "^1.0"
Requires:       php(language) >= 5.6
Requires:       php-intl
Requires:      (php-autoloader(%{gh_owner}/laminas-stdlib)               >= 3.0   with php-autoloader(%{gh_owner}/laminas-stdlib)               < 4)
Requires:      (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.0   with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
# From composer, "suggest": {
#        "laminas/laminas-cache": "Laminas\\Cache component",
#        "laminas/laminas-config": "Laminas\\Config component",
#        "laminas/laminas-eventmanager": "You should install this package to use the events in the translator",
#        "laminas/laminas-filter": "You should install this package to use the provided filters",
#        "laminas/laminas-i18n-resources": "Translation resources",
#        "laminas/laminas-servicemanager": "Laminas\\ServiceManager component",
#        "laminas/laminas-validator": "You should install this package to use the provided validators",
#        "laminas/laminas-view": "You should install this package to use the provided view helpers"
Suggests:       php-autoloader(%{gh_owner}/laminas-cache)
Suggests:       php-autoloader(%{gh_owner}/laminas-config)
Suggests:       php-autoloader(%{gh_owner}/laminas-eventmanager)
Suggests:       php-autoloader(%{gh_owner}/laminas-filter)
Suggests:       php-autoloader(%{gh_owner}/laminas-i18n-resources)
Suggests:       php-autoloader(%{gh_owner}/laminas-servicemanager)
Suggests:       php-autoloader(%{gh_owner}/laminas-validator)
Suggests:       php-autoloader(%{gh_owner}/laminas-view)
# From phpcompatinfo report for version 2.10.1
Requires:       php-ctype
Requires:       php-date
Requires:       php-pcre
Requires:       php-spl
# Autoloader
Requires:       php-composer(fedora/autoloader)

# Compatibily ensure by the bridge
Obsoletes:      php-zendframework-%{zf_name}              < 2.10.2
Provides:       php-zendframework-%{zf_name}              = %{version}
Provides:       php-composer(%{gh_owner}/%{gh_project})   = %{version}
Provides:       php-composer(zendframework/%{zf_name})    = %{version}
Provides:       php-autoloader(%{gh_owner}/%{gh_project}) = %{version}
Provides:       php-autoloader(zendframework/%{zf_name})  = %{version}


%description
%{namespace}\I18n comes with a complete translation suite which supports all major
formats and includes popular features like plural translations and text
domains. The Translator component is mostly dependency free, except for
the fallback to a default locale, where it relies on the Intl PHP extension.

The translator itself is initialized without any parameters, as any
configuration to it is optional. A translator without any translations
will actually do nothing but just return the given message IDs.

Documentation: https://docs.laminas.dev/%{gh_project}/


%prep
%setup -q -n %{gh_project}-%{gh_commit}

mv LICENSE.md LICENSE


%build
: Create autoloader
phpab --template fedora --output src/autoload.php src

cat << 'EOF' | tee -a src/autoload.php
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/%{namespace}/Stdlib/autoload.php',
]);
\Fedora\Autoloader\Dependencies::optional([
    '%{php_home}/%{namespace}/Cache/autoload.php',
    '%{php_home}/%{namespace}/Config/autoload.php',
    '%{php_home}/%{namespace}/EventManager/autoload.php',
    '%{php_home}/%{namespace}/Filter/autoload.php',
    '%{php_home}/%{namespace}/ServiceManager/autoload.php',
    '%{php_home}/%{namespace}/Validator/autoload.php',
    '%{php_home}/%{namespace}/View/autoload.php',
    '%{php_home}/%{namespace}/I18n/Translator/Resources.php',
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
exit (class_exists("\\Zend\\%{library}\\ConfigProvider") ? 0 : 1);
'

%if %{bootstrap}
rm -rf test/Filter/
rm -rf test/Translator/Loader/IniTest.php
rm -rf test/View/
rm -rf test/Validator/
%endif

: upstream test suite
ret=0
for cmdarg in "php %{phpunit}" php72 php73 php74; do
  if which $cmdarg; then
    set $cmdarg
    $1 ${2:-%{_bindir}/phpunit7} \
%if 0%{?fedora} >= 29 || 0%{?rhel} >= 8
      --filter '^((?!(testSettersProvideDefaults|testBasic)).)*$' \
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
* Mon Mar 30 2020 Remi Collet <remi@remirepo.net> - 2.10.3-1
- update to 2.10.3 (no change)

* Fri Mar 20 2020 Remi Collet <remi@remirepo.net> - 2.10.2-1
- update to 2.10.2

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Remi Collet <remi@remirepo.net> - 2.10.1-2
- cleanup

* Thu Jan  9 2020 Remi Collet <remi@remirepo.net> - 2.10.1-1
- switch to Laminas
- boostrap build without config, filter, validator and view

* Fri Dec 13 2019 Remi Collet <remi@remirepo.net> - 2.10.1-2
- update to 2.10.1

* Tue Nov 19 2019 Remi Collet <remi@remirepo.net> - 2.10.0-2
- update to 2.10.0

* Mon Sep 30 2019 Remi Collet <remi@remirepo.net> - 2.9.2-1
- update to 2.9.2

* Thu Sep 26 2019 Remi Collet <remi@remirepo.net> - 2.9.1-2
- update to 2.9.1
- drop patch merged upstream

* Fri Sep 13 2019 Remi Collet <remi@remirepo.net> - 2.9.0-6
- add patch for 7.4 from
  https://github.com/zendframework/zend-i18n/pull/114

* Wed May 23 2018 Remi Collet <remi@remirepo.net> - 2.9.0-2
- update to 2.9.0
- skip test failing with libicu 61, reported as
  https://github.com/zendframework/zend-i18n/issues/97

* Thu Apr 26 2018 Remi Collet <remi@remirepo.net> - 2.8.0-2
- update to 2.8.0
- switch to phpunit6 or phpunit7
- use range dependencies on F27+

* Tue Feb 13 2018 Remi Collet <remi@remirepo.net> - 2.7.4-4
- fix FTBFS from Koschei, path from
  https://github.com/zendframework/zend-i18n/pull/91
- always use phpunit6

* Fri Nov 24 2017 Remi Collet <remi@remirepo.net> - 2.7.4-3
- switch from zend-loader to fedora/autoloader

* Mon May 22 2017 Remi Collet <remi@remirepo.net> - 2.7.4-1
- Update to 2.7.4
- raise dependency on PHP 5.6
- use phpunit6 on F26+

* Fri Jun 10 2016 Remi Collet <remi@fedoraproject.org> - 2.7.3-1
- update to 2.7.3

* Tue Apr 19 2016 Remi Collet <remi@fedoraproject.org> - 2.7.2-1
- update to 2.7.2

* Thu Mar 31 2016 Remi Collet <remi@fedoraproject.org> - 2.7.1-1
- update to 2.7.1

* Wed Mar 30 2016 Remi Collet <remi@fedoraproject.org> - 2.7.0-1
- update to 2.7.0

* Fri Feb 12 2016 Remi Collet <remi@fedoraproject.org> - 2.6.0-1
- update to 2.6.0
- raise dependency on PHP >= 5.5
- raise dependency on zend-stdlib >= 2.7
- ignore failed test with ICU 56

* Tue Aug  4 2015 Remi Collet <remi@fedoraproject.org> - 2.5.1-1
- initial package

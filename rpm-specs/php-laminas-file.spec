# remirepo/Fedora spec file for php-laminas-file
#
# Copyright (c) 2015-2020 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global bootstrap    0
%global gh_commit    cb0bf270cc3e7a4d7dd780b573e2481a09951993
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     laminas
%global gh_project   laminas-file
%global zf_name      zend-file
%global php_home     %{_datadir}/php
%global namespace    Laminas
%global library      File
%if %{bootstrap}
%global with_tests   0%{?_with_tests:1}
%else
%global with_tests   0%{!?_without_tests:1}
%endif

Name:           php-%{gh_project}
Version:        2.8.3
Release:        2%{?dist}
Summary:        %{namespace} Framework %{library} component

License:        BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{gh_commit}/%{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
# Tests
%if %{with_tests}
BuildRequires:  php(language) >= 5.6
BuildRequires:  php-fileinfo
BuildRequires:  php-hash
BuildRequires:  php-pcre
BuildRequires:  php-spl
BuildRequires:  php-tokenizer
BuildRequires: (php-autoloader(%{gh_owner}/laminas-stdlib)               >= 3.1     with php-autoloader(%{gh_owner}/laminas-stdlib)               < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.0     with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
# From composer, "require-dev": {
#        "laminas/laminas-coding-standard": "~1.0.0",
#        "laminas/laminas-filter": "^2.7.2",
#        "laminas/laminas-i18n": "^2.7.4",
#        "laminas/laminas-progressbar": "^2.5.2",
#        "laminas/laminas-servicemanager": "^2.7.8 || ^3.3",
#        "laminas/laminas-session": "^2.8",
#        "laminas/laminas-validator": "^2.10.1",
#        "phpunit/phpunit": "^5.7.27 || ^6.5.8 || ^7.1.2"
BuildRequires: (php-autoloader(%{gh_owner}/laminas-filter)               >= 2.7.2   with php-autoloader(%{gh_owner}/laminas-filter)               < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-i18n)                 >= 2.7.4   with php-autoloader(%{gh_owner}/laminas-i18n)                 < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-progressbar)          >= 2.5.2   with php-autoloader(%{gh_owner}/laminas-progressbar)          < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-servicemanager)       >= 3.3     with php-autoloader(%{gh_owner}/laminas-servicemanager)       < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-session)              >= 2.8     with php-autoloader(%{gh_owner}/laminas-session)              < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-validator)            >= 2.10.1  with php-autoloader(%{gh_owner}/laminas-validator)            < 3)
%global phpunit %{_bindir}/phpunit7
BuildRequires:  phpunit7 >= 7.1.2
%endif
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer, "require": {
#        "php": "^5.6 || ^7.0",
#        "laminas/laminas-stdlib": "^2.7.7 || ^3.1",
#        "laminas/laminas-zendframework-bridge": "^1.0"
Requires:       php(language) >= 5.6
%if ! %{bootstrap}
Requires:      (php-autoloader(%{gh_owner}/laminas-stdlib)               >= 3.1     with php-autoloader(%{gh_owner}/laminas-stdlib)               < 4)
Requires:      (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.0     with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
# From composer, "suggest": {
#        "laminas/laminas-filter": "Laminas\\Filter component",
#        "laminas/laminas-i18n": "Laminas\\I18n component",
#        "laminas/laminas-validator": "Laminas\\Validator component"
Suggests:       php-autoloader(%{gh_owner}/laminas-filter)
Suggests:       php-autoloader(%{gh_owner}/laminas-i18n)
Suggests:       php-autoloader(%{gh_owner}/laminas-validator)
%endif
# Autoloader
Requires:       php-composer(fedora/autoloader)
# From phpcompatinfo report for version 2.8.3
Requires:       php-fileinfo
Requires:       php-hash
Requires:       php-pcre
Requires:       php-reflection
Requires:       php-spl
Requires:       php-tokenizer

# Compatibily ensure by the bridge
Obsoletes:      php-zendframework-%{zf_name}              < 2.8.3-99
Provides:       php-zendframework-%{zf_name}              = %{version}-99
Provides:       php-composer(%{gh_owner}/%{gh_project})   = %{version}
Provides:       php-composer(zendframework/%{zf_name})    = %{version}
Provides:       php-autoloader(%{gh_owner}/%{gh_project}) = %{version}
Provides:       php-autoloader(zendframework/%{zf_name})  = %{version}


%description
%{namespace}\File is a component used to manage file transfer and class
autoloading.

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
    '%{php_home}/%{namespace}/ProgressBar/autoload.php',
    '%{php_home}/%{namespace}/I18n/autoload.php',
    '%{php_home}/%{namespace}/Validator/autoload.php',
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
    '%{php_home}/%{namespace}/Filter/autoload.php',
    '%{php_home}/%{namespace}/ServiceManager/autoload.php',
    '%{php_home}/%{namespace}/Session/autoload.php',
]);
\Fedora\Autoloader\Autoload::addPsr4('%{namespace}Test\\%{library}\\', dirname(__DIR__) . '/test');
EOF

: check compat autoloader
php -r '
require "%{buildroot}%{php_home}/Zend/%{library}/autoload.php";
exit (class_exists("\\Zend\\%{library}\\PhpClassFile") ? 0 : 1);
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
%{php_home}/Zend/%{library}
%{php_home}/%{namespace}/%{library}


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 14 2020 Remi Collet <remi@remirepo.net> - 2.8.3-1
- switch to Laminas

* Thu Feb  7 2019 Remi Collet <remi@remirepo.net> - 2.8.3-1
- update to 2.8.3 (no change)

* Tue Feb  5 2019 Remi Collet <remi@remirepo.net> - 2.8.2-3
- fix FTBFS with zend-validator 2.11, patch from
  https://github.com/zendframework/zend-file/pull/46

* Mon Oct 15 2018 Remi Collet <remi@remirepo.net> - 2.8.2-2
- update to 2.8.2
- drop patch merged upstream

* Mon Oct 15 2018 Remi Collet <remi@remirepo.net> - 2.8.1-4
- add patch for PHP 7.3 from
  https://github.com/zendframework/zend-file/pull/45

* Wed May  2 2018 Remi Collet <remi@remirepo.net> - 2.8.1-2
- update to 2.8.1

* Thu Apr 26 2018 Remi Collet <remi@remirepo.net> - 2.8.0-2
- update to 2.8.0
- raise dependency on PHP 5.6
- raise dependency on zend-stdlib 2.7.7
- switch to phpunit7
- use range dependencies

* Mon Dec 11 2017 Remi Collet <remi@remirepo.net> - 2.7.1-4
- switch from zend-loader to fedora/autoloader

* Wed Jan 11 2017 Remi Collet <remi@fedoraproject.org> - 2.7.1-1
- update to 2.7.1

* Fri Apr 29 2016 Remi Collet <remi@fedoraproject.org> - 2.7.0-1
- update to 2.7.0

* Thu Mar  3 2016 Remi Collet <remi@fedoraproject.org> - 2.6.1-1
- update to 2.6.1

* Thu Feb 18 2016 Remi Collet <remi@fedoraproject.org> - 2.6.0-1
- update to 2.6.0
- raise dependency on zend-stdlib >= 2.7

* Wed Feb 17 2016 Remi Collet <remi@fedoraproject.org> - 2.5.2-1
- update to 2.5.2
- raise dependency on PHP >= 5.5

* Sun Feb 14 2016 Remi Collet <remi@fedoraproject.org> - 2.5.1-3
- add patch for newer zend-filter

* Tue Aug  4 2015 Remi Collet <remi@fedoraproject.org> - 2.5.1-1
- initial package

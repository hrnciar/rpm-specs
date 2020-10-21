# remirepo/Fedora spec file for php-laminas-inputfilter
#
# Copyright (c) 2015-2020 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global bootstrap    0
%global gh_commit    b29ce8f512c966468eee37ea4873ae5fb545d00a
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     laminas
%global gh_project   laminas-inputfilter
%global zf_name      zend-inputfilter
%global php_home     %{_datadir}/php
%global namespace    Laminas
%global library      InputFilter
%if %{bootstrap}
%global with_tests   0%{?_with_tests:1}
%else
%global with_tests   0%{!?_without_tests:1}
%endif

Name:           php-%{gh_project}
Version:        2.10.1
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
BuildRequires:  php-spl
BuildRequires: (php-autoloader(%{gh_owner}/laminas-filter)               >= 2.9.1  with php-autoloader(%{gh_owner}/laminas-filter)               < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-servicemanager)       >= 3.3.1  with php-autoloader(%{gh_owner}/laminas-servicemanager)       < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-stdlib)               >= 3.0    with php-autoloader(%{gh_owner}/laminas-stdlib)               < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-validator)            >= 2.11   with php-autoloader(%{gh_owner}/laminas-validator)            < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.0    with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
# From composer, "require-dev": {
#        "laminas/laminas-coding-standard": "~1.0.0",
#        "phpunit/phpunit": "^5.7.27 || ^6.5.14 || ^7.5.15",
#        "psr/http-message": "^1.0"
BuildRequires: (php-composer(psr/http-message)                           >= 1.0   with php-composer(psr/http-message)                           <  2)
BuildRequires:  phpunit7 >= 7.5
%endif
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer, "require": {
#        "php": "^5.6 || ^7.0",
#        "laminas/laminas-filter": "^2.9.1",
#        "laminas/laminas-servicemanager": "^2.7.10 || ^3.3.1",
#        "laminas/laminas-stdlib": "^2.7 || ^3.0",
#        "laminas/laminas-validator": "^2.11",
#        "laminas/laminas-zendframework-bridge": "^1.0"
Requires:       php(language) >= 5.6
%if ! %{bootstrap}
Requires:      (php-autoloader(%{gh_owner}/laminas-filter)               >= 2.9.1  with php-autoloader(%{gh_owner}/laminas-filter)               < 3)
Requires:      (php-autoloader(%{gh_owner}/laminas-servicemanager)       >= 3.3.1  with php-autoloader(%{gh_owner}/laminas-servicemanager)       < 4)
Requires:      (php-autoloader(%{gh_owner}/laminas-stdlib)               >= 3.0    with php-autoloader(%{gh_owner}/laminas-stdlib)               < 4)
Requires:      (php-autoloader(%{gh_owner}/laminas-validator)            >= 2.11   with php-autoloader(%{gh_owner}/laminas-validator)            < 3)
Requires:      (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.0    with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
%endif
# Autoloader
Requires:       php-composer(fedora/autoloader)
# From phpcompatinfo report for version 2.10.1
Requires:       php-spl

# Compatibily ensure by the bridge
Obsoletes:      php-zendframework-%{zf_name}              < 2.10.1-99
Provides:       php-zendframework-%{zf_name}              = %{version}-99
Provides:       php-composer(%{gh_owner}/%{gh_project})   = %{version}
Provides:       php-composer(zendframework/%{zf_name})    = %{version}
Provides:       php-autoloader(%{gh_owner}/%{gh_project}) = %{version}
Provides:       php-autoloader(zendframework/%{zf_name})  = %{version}


%description
The %{namespace}\InputFilter component can be used to filter and validate generic
sets of input data. For instance, you could use it to filter $_GET or $_POST
values, CLI arguments, etc.

Documentation: https://docs.laminas.dev/%{gh_project}/


%prep
%setup -q -n %{gh_project}-%{gh_commit}

mv LICENSE.md LICENSE


%build
phpab --template fedora --output src/autoload.php src
cat << 'EOF' | tee -a src/autoload.php
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/%{namespace}/Filter/autoload.php',
    '%{php_home}/%{namespace}/Stdlib/autoload.php',
    '%{php_home}/%{namespace}/Validator/autoload.php',
]);
\Fedora\Autoloader\Dependencies::optional([
    '%{php_home}/%{namespace}/ServiceManager/autoload.php',
    '%{php_home}/Psr/Http/Message/autoload.php',
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
exit (class_exists("\\Zend\\%{library}\\Input") ? 0 : 1);
'

: upstream test suite
ret=0
for cmd in php php72 php73 php74; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit7 \
      --filter '^((?!(testProvidesExpectedConfiguration)).)*$' \
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
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Remi Collet <remi@remirepo.net> - 2.10.1-2
- cleanup

* Fri Jan 10 2020 Remi Collet <remi@remirepo.net> - 2.10.1-1
- switch to Laminas

* Thu Aug 29 2019 Remi Collet <remi@remirepo.net> - 2.10.1-1
- update to 2.10.1
- switch to phpunit7

* Thu Jan 31 2019 Remi Collet <remi@remirepo.net> - 2.10.0-1
- update to 2.10.0

* Tue Jan  8 2019 Remi Collet <remi@remirepo.net> - 2.9.1-1
- update to 2.9.1

* Tue Dec 18 2018 Remi Collet <remi@remirepo.net> - 2.9.0-1
- update to 2.9.0
- raise dependency on zend-filter 2.9.1
- raise dependency on zend-validator 2.11

* Fri Dec 14 2018 Remi Collet <remi@remirepo.net> - 2.8.3-2
- update to 2.8.3

* Tue May 15 2018 Remi Collet <remi@remirepo.net> - 2.8.2-2
- update to 2.8.2
- use range dependencies on F27+

* Tue Jan 23 2018 Remi Collet <remi@remirepo.net> - 2.8.1-2
- Update to 2.8.1
- add dependency on zend-servicemanager
- only use phpunit6

* Thu Dec  7 2017 Remi Collet <remi@remirepo.net> - 2.8.0-2
- switch from zend-loader to fedora/autoloader

* Tue Dec  5 2017 Remi Collet <remi@remirepo.net> - 2.8.0-1
- Update to 2.8.0
- raise dependency on zend-validator 2.10.1

* Wed Nov  8 2017 Remi Collet <remi@remirepo.net> - 2.7.5-1
- Update to 2.7.5

* Tue Oct 24 2017 Remi Collet <remi@remirepo.net> - 2.7.4-1
- fix FTBFS from Koschei, add patch for PHP 7.2 from
  https://github.com/zendframework/zend-inputfilter/pull/150

* Mon May 22 2017 Remi Collet <remi@remirepo.net> - 2.7.4-1
- Update to 2.7.4
- raise dependency on PHP 5.6
- use phpunit6 on F26+
- open https://github.com/zendframework/zend-inputfilter/pull/141
  fix for PHPUnit 6

* Fri Sep  2 2016 Remi Collet <remi@fedoraproject.org> - 2.7.3-1
- update to 2.7.3

* Sun Jun 12 2016 Remi Collet <remi@fedoraproject.org> - 2.7.2-1
- update to 2.7.2

* Tue Apr 19 2016 Remi Collet <remi@fedoraproject.org> - 2.7.1-1
- update to 2.7.1

* Fri Apr  8 2016 Remi Collet <remi@fedoraproject.org> - 2.7.0-1
- update to 2.7.0

* Thu Apr  7 2016 Remi Collet <remi@fedoraproject.org> - 2.6.1-1
- update to 2.6.1

* Fri Feb 19 2016 Remi Collet <remi@fedoraproject.org> - 2.6.0-1
- update to 2.6.0
- raise dependency on zend-stdlib >= 2.7
- skip test suite with PHPUnit >= 5

* Fri Sep  4 2015 Remi Collet <remi@fedoraproject.org> - 2.5.5-1
- update to 2.5.5
- raise dependency on zend-validator ^2.5.3
- raise build dependency on PHPUnit ^4.5

* Wed Aug 12 2015 Remi Collet <remi@fedoraproject.org> - 2.5.4-1
- update to 2.5.4

* Tue Aug  4 2015 Remi Collet <remi@fedoraproject.org> - 2.5.3-1
- initial package

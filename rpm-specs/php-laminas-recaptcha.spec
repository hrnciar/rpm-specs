# remirepo/Fedora spec file for php-laminas-recaptcha
#
# Copyright (c) 2015-2020 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global gh_commit    f84222c958c9784db8bcc5b37a8021e5ffcb9557
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     laminas
%global gh_project   laminas-recaptcha
%global zf_name      zendservice-recaptcha
%global php_home     %{_datadir}/php
%global namespace    Laminas
%global library      ReCaptcha
%global with_tests   0%{!?_without_tests:1}

Name:           php-%{gh_project}
Version:        3.2.0
Release:        3%{?dist}
Summary:        %{namespace} Framework %{library} component

License:        BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{gh_commit}/%{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
# Tests
%if %{with_tests}
BuildRequires:  php(language) >= 5.6
BuildRequires:  php-json
BuildRequires: (php-autoloader(%{gh_owner}/laminas-http)                 >= 2.5.4  with php-autoloader(%{gh_owner}/laminas-http)                 < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-json)                 >= 3.0    with php-autoloader(%{gh_owner}/laminas-json)                 < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-stdlib)               >= 3.2.1  with php-autoloader(%{gh_owner}/laminas-stdlib)               < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.0    with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
# From composer.json, "require-dev": {
#        "laminas/laminas-coding-standard": "~1.0.0",
#        "laminas/laminas-config": "^2.0",
#        "laminas/laminas-validator": "^2.8.2",
#        "phpunit/phpunit": "^5.7.27 || ^6.5.8 || ^7.1.5"
BuildRequires: (php-autoloader(%{gh_owner}/laminas-config)               >= 2.0    with php-autoloader(%{gh_owner}/laminas-config)               < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-validator)            >= 2.8.2  with php-autoloader(%{gh_owner}/laminas-validator)            < 3)
%global phpunit %{_bindir}/phpunit7
BuildRequires:  phpunit7 >= 7.1.5
%endif
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer, "require": {
#        "php": "^5.6 || ^7.0",
#        "laminas/laminas-http": "^2.5.4",
#        "laminas/laminas-json": "^2.6.1 || ^3.0",
#        "laminas/laminas-stdlib": "^3.2.1",
#        "laminas/laminas-zendframework-bridge": "^1.0"
Requires:       php(language) >= 5.6
Requires:      (php-autoloader(%{gh_owner}/laminas-http)                 >= 2.5.4  with php-autoloader(%{gh_owner}/laminas-http)                 < 3)
Requires:      (php-autoloader(%{gh_owner}/laminas-json)                 >= 3.0    with php-autoloader(%{gh_owner}/laminas-json)                 < 4)
Requires:      (php-autoloader(%{gh_owner}/laminas-stdlib)               >= 3.2.1  with php-autoloader(%{gh_owner}/laminas-stdlib)               < 4)
Requires:      (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.0    with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
# From composer, "suggest": {
#        "laminas/laminas-validator": "~2.0, if using ReCaptcha's Mailhide API"
Suggests:       php-autoloader(%{gh_owner}/laminas-validator)
# Autoloader
Requires:       php-composer(fedora/autoloader)
# From phpcompatinfo report for version 3.2.0 (mcrypt is optional)
Requires:       php-json

# Compatibily ensure by the bridge
Obsoletes:      php-zendframework-%{zf_name}              < 3.2.0-99
Provides:       php-zendframework-%{zf_name}              = %{version}-99
Provides:       php-composer(%{gh_owner}/%{gh_project})   = %{version}
Provides:       php-composer(zendframework/%{zf_name})    = %{version}
Provides:       php-autoloader(%{gh_owner}/%{gh_project}) = %{version}
Provides:       php-autoloader(zendframework/%{zf_name})  = %{version}


%description
%{summary}.

OOP wrapper for the ReCaptcha web service.

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
    '%{php_home}/%{namespace}/Json/autoload.php',
    '%{php_home}/%{namespace}/Stdlib/autoload.php',
]);
\Fedora\Autoloader\Dependencies::optional([
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
mkdir -p      %{buildroot}%{php_home}/ZendService/%{library}
cp -pr zf.php %{buildroot}%{php_home}/ZendService/%{library}/autoload.php


%check
%if %{with_tests}
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require_once '%{buildroot}%{php_home}/%{namespace}/%{library}/autoload.php';
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/%{namespace}/Config/autoload.php',
    '%{php_home}/%{namespace}/Validator/autoload.php',
]);
\Fedora\Autoloader\Autoload::addPsr4('%{namespace}Test\\%{library}\\', dirname(__DIR__) . '/test');
EOF

: check compat autoloader
php -r '
require "%{buildroot}%{php_home}/ZendService/%{library}/autoload.php";
exit (class_exists("\\ZendService\\%{library}\\ReCaptcha") ? 0 : 1);
'

: upstream test suite
ret=0
for cmdarg in "php %{phpunit}" php72 php73 php74; do
  if which $cmdarg; then
    set $cmdarg
    $1 ${2:-%{_bindir}/phpunit7} --exclude online --verbose || ret=1
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
%dir %{php_home}/ZendService
     %{php_home}/ZendService/%{library}
     %{php_home}/%{namespace}/%{library}


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 13 2020 Remi Collet <remi@remirepo.net> - 3.2.0-1
- switch to Laminas

* Fri Feb  8 2019 Remi Collet <remi@remirepo.net> - 3.2.0-1
- update to 3.2.0
- add dependency on zend-stdlib 3.2.1

* Mon May 14 2018 Remi Collet <remi@remirepo.net> - 3.1.0-2
- update to 3.1.0
- use range dependencies on F27+
- switch to phpunit6 or phpunit7

* Mon Dec 11 2017 Remi Collet <remi@remirepo.net> - 3.0.0-6
- fix virtual provide

* Sat Dec  9 2017 Remi Collet <remi@remirepo.net> - 3.0.0-5
- switch from zend-loader to fedora/autoloader

* Thu Mar  2 2017 Remi Collet <remi@fedoraproject.org> - 3.0.0-3
- add patch to skip online tests, from
  https://github.com/zendframework/ZendService_ReCaptcha/pull/12

* Fri Feb 24 2017 Remi Collet <remi@fedoraproject.org> - 3.0.0-2
- rewrite autoloader as framework extension

* Mon Feb 20 2017 Remi Collet <remi@fedoraproject.org> - 3.0.0-1
- update to 3.0.0

* Thu Aug  6 2015 Remi Collet <remi@fedoraproject.org> - 2.0.1-1
- initial package

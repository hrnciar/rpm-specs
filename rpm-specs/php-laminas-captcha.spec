# remirepo/Fedora spec file for php-laminas-captcha
#
# Copyright (c) 2015-2020 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global bootstrap    0
%global gh_commit    b88f650f3adf2d902ef56f6377cceb5cd87b9876
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     laminas
%global gh_project   laminas-captcha
%global zf_name      zend-captcha
%global php_home     %{_datadir}/php
%global namespace    Laminas
%global library      Captcha
%if %{bootstrap}
%global with_tests   0%{?_with_tests:1}
%else
%global with_tests   0%{!?_without_tests:1}
%endif

Name:           php-%{gh_project}
Version:        2.9.0
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
BuildRequires:  php-date
BuildRequires:  php-gd
BuildRequires:  php-spl
BuildRequires: (php-autoloader(%{gh_owner}/laminas-math)                 >= 2.7     with php-autoloader(%{gh_owner}/laminas-math)                 < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-stdlib)               >= 3.2.1   with php-autoloader(%{gh_owner}/laminas-stdlib)               < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.0     with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
# From composer, "require-dev": {
#        "laminas/laminas-coding-standard": "~1.0.0",
#        "laminas/laminas-recaptcha": "^3.0",
#        "laminas/laminas-session": "^2.8",
#        "laminas/laminas-text": "^2.6",
#        "laminas/laminas-validator": "^2.10.1",
#        "phpunit/phpunit": "^5.7.27 || ^6.5.8 || ^7.1.2"
BuildRequires: (php-autoloader(%{gh_owner}/laminas-recaptcha)            >= 3.0     with php-autoloader(%{gh_owner}/laminas-recaptcha)            < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-session)              >= 2.8     with php-autoloader(%{gh_owner}/laminas-session)              < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-text)                 >= 2.6     with php-autoloader(%{gh_owner}/laminas-text)                 < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-validator)            >= 2.10.1  with php-autoloader(%{gh_owner}/laminas-validator)            < 3)
%global phpunit %{_bindir}/phpunit7
BuildRequires:  phpunit7 >= 7.1.2
%endif
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer, "require": {
#        "php": "^5.6 || ^7.0",
#        "laminas/laminas-math": "^2.7 || ^3.0",
#        "laminas/laminas-stdlib": "^3.2.1",
#        "laminas/laminas-zendframework-bridge": "^1.0"
Requires:       php(language) >= 5.6
%if ! %{bootstrap}
Requires:      (php-autoloader(%{gh_owner}/laminas-math)                 >= 2.7     with php-autoloader(%{gh_owner}/laminas-math)                 < 4)
Requires:      (php-autoloader(%{gh_owner}/laminas-stdlib)               >= 3.2.1   with php-autoloader(%{gh_owner}/laminas-stdlib)               < 4)
Requires:      (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.0     with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
# From composer, "suggest": {
#        "laminas/laminas-i18n-resources": "Translations of captcha messages",
#        "laminas/laminas-recaptcha": "Laminas\\ReCaptcha component",
#        "laminas/laminas-session": "Laminas\\Session component",
#        "laminas/laminas-text": "Laminas\\Text component",
#        "laminas/laminas-validator": "Laminas\\Validator component"
Suggests:       php-autoloader(%{gh_owner}/laminas-i18n-resources)
Suggests:       php-autoloader(%{gh_owner}/laminas-recaptcha)
Suggests:       php-autoloader(%{gh_owner}/laminas-session)
Suggests:       php-autoloader(%{gh_owner}/laminas-text)
Suggests:       php-autoloader(%{gh_owner}/laminas-validator)
%endif
# Autoloader
Requires:       php-composer(fedora/autoloader)
# From phpcompatinfo report for version 2.9.0
Requires:       php-date
Requires:       php-gd
Requires:       php-spl

# Compatibily ensure by the bridge
Obsoletes:      php-zendframework-%{zf_name}              < 2.9.0-99
Provides:       php-zendframework-%{zf_name}              = %{version}-99
Provides:       php-composer(%{gh_owner}/%{gh_project})   = %{version}
Provides:       php-composer(zendframework/%{zf_name})    = %{version}
Provides:       php-autoloader(%{gh_owner}/%{gh_project}) = %{version}
Provides:       php-autoloader(zendframework/%{zf_name})  = %{version}


%description
%{namespace}\Captcha component is able to manage “Completely Automated Public
Turing test to tell Computers and Humans Apart” (CAPTCHA); it is used
as a challenge-response to ensure that the individual submitting
information is a human and not an automated process. Typically, a captcha
is used with form submissions where authenticated users are not necessary,
but you want to prevent spam submissions.

Documentation: https://docs.laminas.dev/%{gh_project}/


%prep
%setup -q -n %{gh_project}-%{gh_commit}

mv LICENSE.md LICENSE


%build
: Generate autoloader
phpab --template fedora --output src/autoload.php src
cat << 'EOF' | tee -a src/autoload.php
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/%{namespace}/Math/autoload.php',
    '%{php_home}/%{namespace}/Stdlib/autoload.php',
]);
\Fedora\Autoloader\Dependencies::optional([
    '%{php_home}/%{namespace}/I18n/Translator/autoload.php',
    '%{php_home}/%{namespace}/Session/autoload.php',
    '%{php_home}/%{namespace}/Text/autoload.php',
    '%{php_home}/%{namespace}/Validator/autoload.php',
    '%{php_home}/%{namespace}/ReCaptcha/autoload.php',
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
exit (class_exists("\\Zend\\%{library}\\Image") ? 0 : 1);
'

# No TESTS_LAMINAS_CAPTCHA_RECAPTCHA_SUPPORT as online

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
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 14 2020 Remi Collet <remi@remirepo.net> - 2.9.0-1
- switch to Laminas

* Tue Jun 18 2019 Remi Collet <remi@remirepo.net> - 2.9.0-1
- update to 2.9.0 (no change)
- raise dependency on zend-stdlib 3.2.1

* Thu Apr 26 2018 Remi Collet <remi@remirepo.net> - 2.8.0-2
- update to 2.8.0
- raise dependency on zend-math 2.7
- raise dependency on zend-stdlib 2.7.7
- switch to phpunit6 or phpunit7
- use range dependencies on F27+

* Mon Dec 11 2017 Remi Collet <remi@remirepo.net> - 2.7.1-3
- switch from zend-loader to fedora/autoloader

* Thu Feb 23 2017 Remi Collet <remi@fedoraproject.org> - 2.7.1-1
- update to 2.7.1

* Mon Feb 20 2017 Remi Collet <remi@fedoraproject.org> - 2.7.0-1
- update to 2.7.0

* Wed Jun 22 2016 Remi Collet <remi@fedoraproject.org> - 2.6.0-1
- update to 2.6.0
- raise dependency on PHP 5.6

* Tue Feb 23 2016 Remi Collet <remi@fedoraproject.org> - 2.5.4-1
- update to 2.5.4
- raise dependency on zend-math >= 2.6
- raise dependency on zend-stdlib >= 2.7

* Tue Feb 23 2016 Remi Collet <remi@fedoraproject.org> - 2.5.3-1
- update to 2.5.3

* Wed Nov 25 2015 Remi Collet <remi@fedoraproject.org> - 2.5.2-1
- update to 2.5.2
- raise dependency on PHP 5.5

* Tue Aug  4 2015 Remi Collet <remi@fedoraproject.org> - 2.5.1-1
- initial package

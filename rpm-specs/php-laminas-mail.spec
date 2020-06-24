# remirepo/Fedora spec file for php-laminas-mail
#
# Copyright (c) 2015-2020 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global bootstrap    0
%global gh_commit    cfe0711446c8d9c392e9fc664c9ccc180fa89005
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     laminas
%global gh_project   laminas-mail
%global zf_name      zend-mail
%global php_home     %{_datadir}/php
%global namespace    Laminas
%global library      Mail
%if %{bootstrap}
%global with_tests   0%{?_with_tests:1}
%else
%global with_tests   0%{!?_without_tests:1}
%endif

Name:           php-%{gh_project}
Version:        2.10.1
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
BuildRequires:  php-iconv
BuildRequires:  php-pcre
BuildRequires:  php-spl
BuildRequires: (php-autoloader(%{gh_owner}/laminas-loader)               >= 2.5    with php-autoloader(%{gh_owner}/laminas-loader)               < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-mime)                 >= 2.5    with php-autoloader(%{gh_owner}/laminas-mime)                 < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-stdlib)               >= 3.0    with php-autoloader(%{gh_owner}/laminas-stdlib)               < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-validator)            >= 2.10.2 with php-autoloader(%{gh_owner}/laminas-validator)            < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.0    with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
BuildRequires: (php-composer(true/punycode)                              >= 2.1    with php-composer(true/punycode)                              < 3)
# From composer, "require-dev": {
#        "laminas/laminas-coding-standard": "~1.0.0",
#        "laminas/laminas-config": "^2.6",
#        "laminas/laminas-crypt": "^2.6 || ^3.0",
#        "laminas/laminas-servicemanager": "^2.7.10 || ^3.3.1",
#        "phpunit/phpunit": "^5.7.25 || ^6.4.4 || ^7.1.4"
BuildRequires: (php-autoloader(%{gh_owner}/laminas-config)               >= 2.6    with php-autoloader(%{gh_owner}/laminas-config)               < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-crypt)                >= 3.0    with php-autoloader(%{gh_owner}/laminas-crypt)                < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-servicemanager)       >= 3.3.1  with php-autoloader(%{gh_owner}/laminas-servicemanager)       < 4)
BuildRequires:  phpunit7 >= 7.1.4
%global phpunit %{_bindir}/phpunit7
%endif
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer, "require": {
#        "php": "^5.6 || ^7.0",
#        "ext-iconv": "*",
#        "laminas/laminas-loader": "^2.5",
#        "laminas/laminas-mime": "^2.5",
#        "laminas/laminas-stdlib": "^2.7 || ^3.0",
#        "laminas/laminas-validator": "^2.10.2",
#        "laminas/laminas-zendframework-bridge": "^1.0",
#        "true/punycode": "^2.1"
Requires:       php(language) >= 5.6
Requires:       php-iconv
Requires:      (php-autoloader(%{gh_owner}/laminas-loader)               >= 2.5    with php-autoloader(%{gh_owner}/laminas-loader)               < 3)
Requires:      (php-autoloader(%{gh_owner}/laminas-mime)                 >= 2.5    with php-autoloader(%{gh_owner}/laminas-mime)                 < 3)
Requires:      (php-autoloader(%{gh_owner}/laminas-stdlib)               >= 3.0    with php-autoloader(%{gh_owner}/laminas-stdlib)               < 4)
Requires:      (php-autoloader(%{gh_owner}/laminas-validator)            >= 2.10.2 with php-autoloader(%{gh_owner}/laminas-validator)            < 3)
Requires:      (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.0    with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
Requires:      (php-composer(true/punycode)                              >= 2.1    with php-composer(true/punycode)                              < 3)
# From composer, "suggest": {
#        "laminas/laminas-crypt": "Crammd5 support in SMTP Auth",
#        "laminas/laminas-servicemanager": "^2.7.10 || ^3.3.1 when using SMTP to deliver messages"
Suggests:       php-autoloader(%{gh_owner}/laminas-crypt)
Suggests:       php-autoloader(%{gh_owner}/laminas-servicemanager)
# From phpcompatinfo report
Recommends:     php-imap
# Autoloader
Requires:       php-composer(fedora/autoloader)
# From phpcompatinfo report for version 2.10.0
Requires:       php-ctype
Requires:       php-date
Requires:       php-pcre
Requires:       php-spl

# Compatibily ensure by the bridge
Obsoletes:      php-zendframework-%{zf_name}              < 2.10.1
Provides:       php-zendframework-%{zf_name}              = %{version}
Provides:       php-composer(%{gh_owner}/%{gh_project})   = %{version}
Provides:       php-composer(zendframework/%{zf_name})    = %{version}
Provides:       php-autoloader(%{gh_owner}/%{gh_project}) = %{version}
Provides:       php-autoloader(zendframework/%{zf_name})  = %{version}


%description
%{namespace}\Mail provides generalized functionality to compose and send both text
and MIME-compliant multipart email messages. Mail can be sent with %{namespace}\Mail
via the Mail\Transport\Sendmail, Mail\Transport\Smtp or the
Mail\Transport\File transport. Of course, you can also implement your own
transport by implementing the Mail\Transport\TransportInterface.

Documentation: https://docs.laminas.dev/%{gh_project}/


%prep
%setup -q -n %{gh_project}-%{gh_commit}

mv LICENSE.md LICENSE


%build
: Create autoloader
phpab --template fedora --output src/autoload.php src
cat << 'EOF' | tee -a src/autoload.php
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/%{namespace}/Loader/autoload.php',
    '%{php_home}/%{namespace}/Mime/autoload.php',
    '%{php_home}/%{namespace}/Stdlib/autoload.php',
    '%{php_home}/%{namespace}/Validator/autoload.php',
    '%{php_home}/TrueBV/autoload.php',
]);
\Fedora\Autoloader\Dependencies::optional([
    '%{php_home}/%{namespace}/ServiceManager/autoload.php',
    '%{php_home}/%{namespace}/Crypt/autoload.php',
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
    '%{php_home}/%{namespace}/Config/autoload.php',
]);
\Fedora\Autoloader\Autoload::addPsr4('%{namespace}Test\\%{library}\\', dirname(__DIR__) . '/test');
EOF

: check compat autoloader
php -r '
require "%{buildroot}%{php_home}/Zend/%{library}/autoload.php";
exit (class_exists("\\Zend\\%{library}\\Message") ? 0 : 1);
'

: upstream test suite
ret=0
for cmdarg in "php %{phpunit}" php72 php73 php74; do
  if which $cmdarg; then
    set $cmdarg
    $1 ${2:-%{_bindir}/phpunit7} \
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
* Wed Apr 22 2020 Remi Collet <remi@remirepo.net> - 2.10.1-1
- update to 2.10.1

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Remi Collet <remi@remirepo.net> - 2.10.0-2
- cleanup

* Thu Jan  9 2020 Remi Collet <remi@remirepo.net> - 2.10.0-1
- switch to Laminas

* Wed Oct  9 2019 Remi Collet <remi@remirepo.net> - 2.10.0-6
- add patch for PHP 7.4 from
  https://github.com/zendframework/zend-mail/pull/244

* Thu Jun  7 2018 Remi Collet <remi@remirepo.net> - 2.10.0-2
- update to 2.10.0
- lower dependency on PHP 5.6
- raise dependency on zend-validator 2.10.2
- add dependency on true/punycode
- switch to phpunit7

* Fri Mar  2 2018 Remi Collet <remi@remirepo.net> - 2.9.0-1
- Update to 2.9.0
- raise dependency on PHP 7.1
- raise dependency on zend-validator 2.10.2
- always use phpunit6
- use range dependencies on F27+

* Tue Dec 12 2017 Remi Collet <remi@remirepo.net> - 2.8.0-4
- switch from zend-loader to fedora/autoloader
- fix FTBFS from Koschei, ignore 1 test, reported as
  https://github.com/zendframework/zend-mail/issues/183

* Fri Oct 20 2017 Remi Collet <remi@remirepo.net> - 2.8.0-3
- fix FTBFS from Koschei
- add patch for latest PHPUnit from
  https://github.com/zendframework/zend-mail/pull/174

* Fri Jun  9 2017 Remi Collet <remi@remirepo.net> - 2.8.0-1
- Update to 2.8.0
- raise dependency on PHP 5.6
- use phpunit6 on F26+

* Wed Apr 12 2017 Remi Collet <remi@fedoraproject.org> - 2.7.3-2
- add upstream patch to fix FTBFS (from Koschei)
  https://github.com/zendframework/zend-mail/issues/136

* Wed Feb 15 2017 Remi Collet <remi@fedoraproject.org> - 2.7.3-1
- update to 2.7.3

* Wed Dec 21 2016 Remi Collet <remi@fedoraproject.org> - 2.7.2-1
- update to 2.7.2

* Wed May 11 2016 Remi Collet <remi@fedoraproject.org> - 2.7.1-1
- update to 2.7.1

* Tue Apr 12 2016 Remi Collet <remi@fedoraproject.org> - 2.7.0-1
- update to 2.7.0
- zend-crypt is now optional

* Thu Feb 25 2016 Remi Collet <remi@fedoraproject.org> - 2.6.1-1
- update to 2.6.1

* Fri Feb 19 2016 Remi Collet <remi@fedoraproject.org> - 2.6.0-1
- update to 2.6.0
- raise dependency on zend-crypt >= 2.6
- raise dependency on zend-stdlib >= 2.7
- raise dependency on zend-validator >= 2.6

* Fri Sep 11 2015 Remi Collet <remi@fedoraproject.org> - 2.5.2-1
- update to 2.5.2
- raise minimum PHP version to 5.5

* Tue Aug  4 2015 Remi Collet <remi@fedoraproject.org> - 2.5.1-1
- initial package

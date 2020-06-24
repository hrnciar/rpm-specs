# remirepo/Fedora spec file for php-laminas-http
#
# Copyright (c) 2015-2020 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global bootstrap    0
%global gh_commit    8c66963b933c80da59433da56a44dfa979f3ec88
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     laminas
%global gh_project   laminas-http
%global zf_name      zend-http
%global php_home     %{_datadir}/php
%global namespace    Laminas
%global library      Http
%if %{bootstrap}
%global with_tests   0%{?_with_tests:1}
%else
%global with_tests   0%{!?_without_tests:1}
%endif

Name:           php-%{gh_project}
Version:        2.11.2
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
BuildRequires:  php-ctype
BuildRequires:  php-curl
BuildRequires:  php-date
BuildRequires:  php-fileinfo
BuildRequires:  php-openssl
BuildRequires:  php-pcre
BuildRequires:  php-spl
BuildRequires:  php-zlib
BuildRequires: (php-autoloader(%{gh_owner}/laminas-loader)               >= 2.5.1  with php-autoloader(%{gh_owner}/laminas-loader)               < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-stdlib)               >= 3.2.1  with php-autoloader(%{gh_owner}/laminas-stdlib)               < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-uri)                  >= 2.5.2  with php-autoloader(%{gh_owner}/laminas-uri)                  < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-validator)            >= 2.10.1 with php-autoloader(%{gh_owner}/laminas-validator)            < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.0    with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
# From composer, "require-dev": {
#        "laminas/laminas-coding-standard": "~1.0.0",
#        "laminas/laminas-config": "^3.1 || ^2.6",
#        "phpunit/phpunit": "^5.7.27 || ^6.5.8 || ^7.1.3"
BuildRequires: (php-autoloader(%{gh_owner}/laminas-config)               >= 2.6    with php-autoloader(%{gh_owner}/laminas-config)               < 4)
%global phpunit %{_bindir}/phpunit7
BuildRequires:  phpunit7 >= 7.1.2
%endif
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer, "require": {
#        "php": "^5.6 || ^7.0",
#        "laminas/laminas-loader": "^2.5.1",
#        "laminas/laminas-stdlib": "^3.2.1",
#        "laminas/laminas-uri": "^2.5.2",
#        "laminas/laminas-validator": "^2.10.1",
#        "laminas/laminas-zendframework-bridge": "^1.0"
Requires:       php(language) >= 5.6
%if ! %{bootstrap}
Requires:      (php-autoloader(%{gh_owner}/laminas-loader)               >= 2.5.1  with php-autoloader(%{gh_owner}/laminas-loader)               < 3)
Requires:      (php-autoloader(%{gh_owner}/laminas-stdlib)               >= 3.2.1  with php-autoloader(%{gh_owner}/laminas-stdlib)               < 4)
Requires:      (php-autoloader(%{gh_owner}/laminas-uri)                  >= 2.5.2  with php-autoloader(%{gh_owner}/laminas-uri)                  < 3)
Requires:      (php-autoloader(%{gh_owner}/laminas-validator)            >= 2.10.1 with php-autoloader(%{gh_owner}/laminas-validator)            < 3)
Requires:      (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.0    with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
%endif
# Autoloader
Requires:       php-composer(fedora/autoloader)
# From phpcompatinfo report for version 2.11.2
Requires:       php-ctype
Requires:       php-curl
Requires:       php-date
Requires:       php-fileinfo
Requires:       php-openssl
Requires:       php-pcre
Requires:       php-spl
Requires:       php-zlib

# Compatibily ensure by the bridge
Obsoletes:      php-zendframework-%{zf_name}              < 2.11.2-99
Provides:       php-zendframework-%{zf_name}              = %{version}-99
Provides:       php-composer(%{gh_owner}/%{gh_project})   = %{version}
Provides:       php-composer(zendframework/%{zf_name})    = %{version}
Provides:       php-autoloader(%{gh_owner}/%{gh_project}) = %{version}
Provides:       php-autoloader(zendframework/%{zf_name})  = %{version}


%description
%{namespace}\Http is a primary foundational component of %{namespace} Framework.
Since much of what PHP does is web-based, specifically HTTP,
it makes sense to have a performant, extensible, concise and
consistent API to do all things HTTP.

Documentation: https://docs.laminas.dev/%{gh_project}/


%prep
%setup -q -n %{gh_project}-%{gh_commit}

mv LICENSE.md LICENSE


%build
phpab --template fedora --output src/autoload.php src
cat << 'EOF' | tee -a src/autoload.php
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/%{namespace}/Loader/autoload.php',
    '%{php_home}/%{namespace}/Stdlib/autoload.php',
    '%{php_home}/%{namespace}/Uri/autoload.php',
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
exit (class_exists("\\Zend\\%{library}\\Client") ? 0 : 1);
'

: upstream test suite
# testStreamCompression: online test
ret=0
for cmdarg in "php %{phpunit}" php72 php73 php74; do
  if which $cmdarg; then
    set $cmdarg
    $1 ${2:-%{_bindir}/phpunit7} \
       --filter '^((?!(testStreamCompression)).)*$' \
       || ret=1
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
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Remi Collet <remi@remirepo.net> - 2.11.2-2
- cleanup

* Fri Jan 10 2020 Remi Collet <remi@remirepo.net> - 2.11.2-1
- switch to Laminas

* Fri Jan  3 2020 Remi Collet <remi@remirepo.net> - 2.11.2-1
- update to 2.11.2

* Thu Dec  5 2019 Remi Collet <remi@remirepo.net> - 2.11.1-1
- update to 2.11.1

* Tue Dec  3 2019 Remi Collet <remi@remirepo.net> - 2.11.0-1
- update to 2.11.0

* Tue Dec  3 2019 Remi Collet <remi@remirepo.net> - 2.10.1-1
- update to 2.10.1

* Wed Feb 20 2019 Remi Collet <remi@remirepo.net> - 2.10.0-1
- update to 2.10.0

* Wed Jan 23 2019 Remi Collet <remi@remirepo.net> - 2.9.1-1
- update to 2.9.1

* Wed Jan  9 2019 Remi Collet <remi@remirepo.net> - 2.9.0-1
- update to 2.9.0
- raise dependency on zend-stdlib 3.2.1

* Thu Dec  6 2018 Remi Collet <remi@remirepo.net> - 2.8.2-3
- skip 2 failing tests with recent PHP

* Fri Aug 17 2018 Remi Collet <remi@remirepo.net> - 2.8.2-1
- update to 2.8.2

* Thu Aug 02 2018 Shawn Iwinski <shawn@iwin.ski> - 2.8.1-1
- Update to 2.8.1 (ZF2018-01)

* Fri Apr 27 2018 Remi Collet <remi@remirepo.net> - 2.8.0-2
- update to 2.8.0
- use range dependencies on F27+
- switch to phpunit6 or phpunit7

* Thu Dec  7 2017 Remi Collet <remi@remirepo.net> - 2.7.0-2
- switch from zend-loader to fedora/autoloader

* Thu Nov  2 2017 Remi Collet <remi@remirepo.net> - 2.7.0-1
- Update to 2.7.0
- use phpunit6 on F26+
- raise dependency on PHP 5.6
- raise dependency on zendframework/zend-loader 2.5.1
- raise dependency on zendframework/zend-stdlib 2.7.7
- raise dependency on zendframework/zend-uri 2.5.2
- raise dependency on zendframework/zend-validator 2.10.1

* Wed Feb  1 2017 Remi Collet <remi@fedoraproject.org> - 2.6.0-1
- version 2.6.0

* Mon Aug  8 2016 Remi Collet <remi@fedoraproject.org> - 2.5.5-1
- version 2.5.5

* Fri Feb  5 2016 Remi Collet <remi@fedoraproject.org> - 2.5.4-1
- version 2.5.4

* Tue Sep 15 2015 Remi Collet <remi@fedoraproject.org> - 2.5.3-1
- version 2.5.3

* Thu Aug  6 2015 Remi Collet <remi@fedoraproject.org> - 2.5.2-1
- version 2.5.2

* Tue Aug  4 2015 Remi Collet <remi@fedoraproject.org> - 2.5.1-1
- initial package

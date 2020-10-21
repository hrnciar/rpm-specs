# remirepo/Fedora spec file for php-laminas-xmlrpc
#
# Copyright (c) 2015-2020 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global bootstrap    0
%global gh_commit    1461f9777ec59f6c5dcbd727e23548ea1cbe4dcc
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     laminas
%global gh_project   laminas-xmlrpc
%global zf_name      zend-xmlrpc
%global php_home     %{_datadir}/php
%global namespace    Laminas
%global library      XmlRpc
%if %{bootstrap}
%global with_tests   0%{?_with_tests:1}
%else
%global with_tests   0%{!?_without_tests:1}
%endif

Name:           php-%{gh_project}
Version:        2.9.0
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
BuildRequires:  php-simplexml
BuildRequires:  php-date
BuildRequires:  php-dom
BuildRequires:  php-iconv
BuildRequires:  php-libxml
BuildRequires:  php-pcre
BuildRequires:  php-spl
BuildRequires:  php-xmlwriter
BuildRequires: (php-autoloader(%{gh_owner}/laminas-http)                 >= 2.5.4  with php-autoloader(%{gh_owner}/laminas-http)                 < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-math)                 >= 3.0    with php-autoloader(%{gh_owner}/laminas-math)                 < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-server)               >= 2.7    with php-autoloader(%{gh_owner}/laminas-server)               < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-stdlib)               >= 3.2.1  with php-autoloader(%{gh_owner}/laminas-stdlib)               < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-xml)                  >= 1.0.2  with php-autoloader(%{gh_owner}/laminas-xml)                  < 2)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.0    with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
# From composer, "require-dev": {
#        "laminas/laminas-coding-standard": "~1.0.0",
#        "phpunit/phpunit": "^5.7.27 || ^6.5.8 || ^7.1.2"
%global phpunit %{_bindir}/phpunit7
BuildRequires:  phpunit7 >= 7.1.2
%endif
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer, "require": {
#        "php": "^5.6 || ^7.0",
#        "laminas/laminas-http": "^2.5.4",
#        "laminas/laminas-math": "^2.7 || ^3.0",
#        "laminas/laminas-server": "^2.7",
#        "laminas/laminas-stdlib": "^3.2.1",
#        "laminas/laminas-xml": "^1.0.2",
#        "laminas/laminas-zendframework-bridge": "^1.0"
Requires:       php(language) >= 5.6
%if ! %{bootstrap}
Requires:      (php-autoloader(%{gh_owner}/laminas-http)                 >= 2.5.4   with php-autoloader(%{gh_owner}/laminas-http)                 < 3)
Requires:      (php-autoloader(%{gh_owner}/laminas-math)                 >= 3.0     with php-autoloader(%{gh_owner}/laminas-math)                 < 4)
Requires:      (php-autoloader(%{gh_owner}/laminas-server)               >= 2.7     with php-autoloader(%{gh_owner}/laminas-server)               < 3)
Requires:      (php-autoloader(%{gh_owner}/laminas-stdlib)               >= 3.2.1   with php-autoloader(%{gh_owner}/laminas-stdlib)               < 4)
Requires:      (php-autoloader(%{gh_owner}/laminas-xml)                  >= 1.0.2   with php-autoloader(%{gh_owner}/laminas-xml)                  < 2)
Requires:      (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.0     with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
# From composer, "suggest": {
#        "laminas/laminas-cache": "To support Laminas\\XmlRpc\\Server\\Cache usage"
Suggests:       php-autoloader(%{gh_owner}/laminas-cache)
%endif
# Autoloader
Requires:       php-composer(fedora/autoloader)
# From phpcompatinfo report for version 2.9.0
Requires:       php-simplexml
Requires:       php-date
Requires:       php-dom
Requires:       php-iconv
Requires:       php-libxml
Requires:       php-pcre
Requires:       php-spl
Requires:       php-xmlwriter

# Compatibily ensure by the bridge
Obsoletes:      php-zendframework-%{zf_name}              < 2.9.0-99
Provides:       php-zendframework-%{zf_name}              = %{version}-99
Provides:       php-composer(%{gh_owner}/%{gh_project})   = %{version}
Provides:       php-composer(zendframework/%{zf_name})    = %{version}
Provides:       php-autoloader(%{gh_owner}/%{gh_project}) = %{version}
Provides:       php-autoloader(zendframework/%{zf_name})  = %{version}


%description
From its home page, XML-RPC is described as a ”...remote procedure calling
using HTTP as the transport and XML as the encoding. XML-RPC is designed
to be as simple as possible, while allowing complex data structures to be
transmitted, processed and returned.”

%{namespace}\XmlRpc provides support for both consuming remote XML-RPC services
and building new XML-RPC servers.

Documentation: https://docs.laminas.dev/%{gh_project}/


%prep
%setup -q -n %{gh_project}-%{gh_commit}

mv LICENSE.md LICENSE


%build
: Generate autoloader
phpab --template fedora --output src/autoload.php src
cat << 'EOF' | tee -a src/autoload.php
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/%{namespace}/Http/autoload.php',
    '%{php_home}/%{namespace}/Math/autoload.php',
    '%{php_home}/%{namespace}/Server/autoload.php',
    '%{php_home}/%{namespace}/Stdlib/autoload.php',
    '%{php_home}/%{namespace}/Xml/autoload.php',
]);
\Fedora\Autoloader\Dependencies::optional([
    '%{php_home}/%{namespace}/Cache/autoload.php',
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
require_once 'test/autoload.php';
require_once 'test/TestAsset/functions.php';
EOF

: check compat autoloader
php -r '
require "%{buildroot}%{php_home}/Zend/%{library}/autoload.php";
exit (class_exists("\\Zend\\%{library}\\Server") ? 0 : 1);
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
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 14 2020 Remi Collet <remi@remirepo.net> - 2.9.0-1
- switch to Laminas

* Fri Jan  3 2020 Remi Collet <remi@remirepo.net> - 2.9.0-1
- update to 2.9.0

* Mon Oct 21 2019 Remi Collet <remi@remirepo.net> - 2.8.0-1
- update to 2.8.0 (no change)
- raise dependency on zend-stdlib 3.2.1

* Tue May 15 2018 Remi Collet <remi@remirepo.net> - 2.7.0-1
- update to 2.7.0
- use range dependencies on F27+
- switch to phpunit6 or phpunit7

* Fri Jan 26 2018 Remi Collet <remi@remirepo.net> - 2.6.2-1
- Update to 2.6.2
- switch to phpunit6

* Mon Dec 11 2017 Remi Collet <remi@remirepo.net> - 2.6.1-2
- switch from zend-loader to fedora/autoloader

* Fri Aug 11 2017 Remi Collet <remi@remirepo.net> - 2.6.1-1
- Update to 2.6.1

* Tue Jun 21 2016 Remi Collet <remi@fedoraproject.org> - 2.6.0-1
- update to 2.6.0
- raise dependency on PHP 5.6
- raise dependency on zend-server 2.7

* Fri Apr 22 2016 Remi Collet <remi@fedoraproject.org> - 2.5.2-1
- update to 2.5.2
- raise dependency on PHP >= 5.5
- raise dependency on zend-http >= 2.5.4
- raise dependency on zend-math >= 2.7
- raise dependency on zend-server >= 2.6.1
- raise dependency on zend-stdlib >= 2.7

* Tue Aug  4 2015 Remi Collet <remi@fedoraproject.org> - 2.5.1-1
- initial package

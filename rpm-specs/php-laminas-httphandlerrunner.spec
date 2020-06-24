# remirepo/Fedora spec file for php-laminas-httphandlerrunner
#
# Copyright (c) 2020 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global bootstrap    0
%global gh_commit    e1a5dad040e0043135e8095ee27d1fbf6fb640e1
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     laminas
%global gh_project   laminas-httphandlerrunner
%global zf_name      zend-httphandlerrunner
%global php_home     %{_datadir}/php
%global namespace    Laminas
%global library      HttpHandlerRunner
%if %{bootstrap}
%global with_tests   0%{?_with_tests:1}
%else
%global with_tests   0%{!?_without_tests:1}
%endif

Name:           php-%{gh_project}
Version:        1.2.0
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
BuildRequires: (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.0    with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
BuildRequires: (php-composer(psr/http-message)                           >= 1.0    with php-composer(psr/http-message)                           < 2)
BuildRequires: (php-composer(psr/http-server-handler)                    >= 1.0    with php-composer(psr/http-server-handler)                    < 2)
# From composer, "require-dev": {
#        "laminas/laminas-coding-standard": "~1.0.0",
#        "laminas/laminas-diactoros": "^1.7 || ^2.1.1",
#        "phpunit/phpunit": "^7.0.2"
BuildRequires: (php-autoloader(%{gh_owner}/laminas-diactoros)            >= 1.7    with php-autoloader(%{gh_owner}/laminas-diactoros)            < 3)
%global phpunit %{_bindir}/phpunit7
BuildRequires:  phpunit7 >= 7.0.2
BuildRequires:  php-pcre
BuildRequires:  php-spl
%endif
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer, "require": {
#        "php": "^7.1",
#        "laminas/laminas-zendframework-bridge": "^1.0",
#        "psr/http-message": "^1.0",
#        "psr/http-message-implementation": "^1.0",
#        "psr/http-server-handler": "^1.0"
Requires:       php(language) >= 7.1
Requires:      (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.0    with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
Requires:      (php-composer(psr/http-message)                           >= 1.0    with php-composer(psr/http-message)                           < 2)
Requires:      (php-composer(psr/http-server-handler)                    >= 1.0    with php-composer(psr/http-server-handler)                    < 2)
# Autoloader
Requires:       php-composer(fedora/autoloader)
# From phpcompatinfo report for version 1.1.0
Requires:       php-pcre
Requires:       php-spl

Provides:       php-composer(%{gh_owner}/%{gh_project})   = %{version}
Provides:       php-composer(zendframework/%{zf_name})    = %{version}
Provides:       php-autoloader(%{gh_owner}/%{gh_project}) = %{version}
Provides:       php-autoloader(zendframework/%{zf_name})  = %{version}


%description
This library provides utilities for:

* Emitting PSR-7 responses.
* Running PSR-15 server request handlers, which involves marshaling a PSR-7
  ServerRequestInterface, handling exceptions due to request creation,
  and emitting the response returned by the composed request handler.

The RequestHandlerRunner will be used in the bootstrap of your application
to fire off the RequestHandlerInterface representing your application.

Documentation: https://docs.laminas.dev/%{gh_project}/


%prep
%setup -q -n %{gh_project}-%{gh_commit}

mv LICENSE.md LICENSE


%build
: Generate autoloader
phpab --template fedora --output src/autoload.php src
cat << 'EOF' | tee -a src/autoload.php
\Fedora\Autoloader\Dependencies::optional([
    '%{php_home}/Psr/Http/Message/autoload.php',
    '%{php_home}/Psr/Http/Server/autoload.php',
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
        '%{php_home}/%{namespace}/Diactoros2/autoload.php',
        '%{php_home}/%{namespace}/Diactoros/autoload.php',
    ],
]);
\Fedora\Autoloader\Autoload::addPsr4('%{namespace}Test\\%{library}\\', dirname(__DIR__) . '/test');
EOF

: check compat autoloader
php -r '
require "%{buildroot}%{php_home}/Zend/%{library}/autoload.php";
exit (class_exists("\\Zend\\%{library}\\RequestHandlerRunner") ? 0 : 1);
'

: failing with 'headers already sent'
rm -r test/Emitter/

: upstream test suite
ret=0
for cmdarg in "php %{phpunit}" php72 php73 php74; do
  if which $cmdarg; then
    set $cmdarg
    $1 ${2:-%{_bindir}/phpunit7} || ret=1
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
* Thu Jun  4 2020 Remi Collet <remi@remirepo.net> - 1.2.0-1
- update to 1.2.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 22 2020 Remi Collet <remi@remirepo.net> - 1.1.0-1
- initial package

# remirepo/fedora spec file for php-nyholm-psr7
#
# Copyright (c) 2019 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global bootstrap    0
# github
%global gh_commit    c17f4f73985f62054a331cbc4ffdf9868c4ef256
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     Nyholm
%global gh_project   psr7
# packagist
%global pk_vendor    nyholm
%global pk_project   %{gh_project}
%global major        %nil
# namespace
%global php_home     %{_datadir}/php
%global ns_vendor    Nyholm
%global ns_project   Psr7
%if %{bootstrap}
%global with_tests   0%{?_with_tests:1}
%else
%global with_tests   0%{!?_without_tests:1}
%endif

# php-http/psr7-integration-tests
%global psr7_integration_tests_commit c3bb79ca4a276df57364ff45bf2f619f769ded4a
%global psr7_integration_tests_short  %(c=%{psr7_integration_tests_commit}; echo ${c:0:7})
# http-interop/http-factory-tests
%global http_factory_tests_commit     92d8b91e7236957d7512ef93e8a237d241671ce7
%global http_factory_tests_short      %(c=%{http_factory_tests_commit}; echo ${c:0:7})

Name:           php-%{pk_vendor}-%{pk_project}%{major}
Version:        1.3.0
Release:        1%{?dist}
Summary:        A fast PHP7 implementation of PSR-7

License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
# git snapshot for skip .gitattributes
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh
# Only used for tests and no version released (dev-master required)
Source2:        https://github.com/php-http/psr7-integration-tests/archive/%{psr7_integration_tests_commit}/%{name}-integration-tests-%{psr7_integration_tests_short}.tar.gz
Source3:        https://github.com/http-interop/http-factory-tests/archive/%{http_factory_tests_commit}/%{name}-factory-tests-%{http_factory_tests_short}.tar.gz

BuildArch:      noarch
BuildRequires:  php(language) >= 7.1
BuildRequires:  php-pcre
BuildRequires:  php-spl
BuildRequires: (php-composer(psr/http-message)          >= 1.0 with php-composer(psr/http-message)         < 2)
BuildRequires: (php-composer(php-http/message-factory)  >= 1.0 with php-composer(php-http/message-factory) < 2)
BuildRequires: (php-composer(psr/http-factory)          >= 1.0 with php-composer(psr/http-factory)         < 2)
BuildRequires: (php-composer(symfony/error-handler)     >= 4.4 with php-composer(symfony/error-handler)    < 5)
# Autoloader
BuildRequires:  php-fedora-autoloader-devel >= 1.0.0
%if %{with_tests}
# from composer.json, "require-dev": {
#        "phpunit/phpunit": "^7.5",
#        "php-http/psr7-integration-tests": "^1.0",
#        "http-interop/http-factory-tests": "dev-master",
#        "symfony/error-handler": "^4.4"
BuildRequires:  phpunit7 > 7.5
%endif

# from composer.json, "require": {
#        "php": "^7.1",
#        "psr/http-message": "^1.0",
#        "php-http/message-factory": "^1.0",
#        "psr/http-factory": "^1.0"
Requires:       php(language) >= 7.1
Requires:      (php-composer(psr/http-message)          >= 1.0 with php-composer(psr/http-message)         < 2)
Requires:      (php-composer(php-http/message-factory)  >= 1.0 with php-composer(php-http/message-factory) < 2)
Requires:      (php-composer(psr/http-factory)          >= 1.0 with php-composer(psr/http-factory)         < 2)
# from phpcompatinfo report for version 1.1.0
Requires:       php-pcre
Requires:       php-spl
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}
Provides:       php-composer(psr/http-message-implementation) = 1.0
Provides:       php-composer(psr/http-factory-implementation) = 1.0


%description
A super lightweight PSR-7 implementation. Very strict and very fast..

Autoloader: %{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit} -a2 -a3


%build
# Generate the Autoloader
phpab --template fedora --output src/autoload.php src

cat << 'EOF' | tee -a src/autoload.php
\Fedora\Autoloader\Dependencies::required([
    '%{_datadir}/php/Psr/Http/Message/autoload.php',
    '%{_datadir}/php/Http/Message/autoload.php',
    '%{_datadir}/php/Psr/Http/Message/http-factory-autoload.php',
]);
EOF

# Generate test Autoloader
phpab --template fedora --output test-autoload.php \
    psr7-integration-tests-%{psr7_integration_tests_commit} \
    http-factory-tests-%{http_factory_tests_commit}


%install
mkdir -p   %{buildroot}%{php_home}/%{ns_vendor}
cp -pr src %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}


%check
%if %{with_tests}
mkdir vendor
cat <<EOF | tee vendor/autoload.php
<?php
require_once '%{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php';
require_once '%{php_home}/Symfony4/Component/ErrorHandler/autoload.php';
require_once dirname(__DIR__) . '/test-autoload.php';
EOF

: Run upstream test suite
: Ignore online tests
# TODO testCanDetachStream may fail on local build (extension conflicts ?)
ret=0
for cmd in php php71 php72 php73 php74; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit7 \
      --filter '^((?!(testIsNotSeekable|testIsNotWritable|testIsNotReadable|testRewindNotSeekable)).)*$' \
      --verbose || ret=1
  fi
done
exit $ret
%else
: bootstrap build with test suite disabled
%endif


%files
%license LICENSE
%doc *.md
%doc composer.json
%{php_home}/%{ns_vendor}


%changelog
* Mon May 25 2020 Remi Collet <remi@remirepo.net> - 1.3.0-1
- update to 1.3.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep  6 2019 Remi Collet <remi@remirepo.net> - 1.2.1-1
- update to 1.2.1 (no change)

* Fri Aug 23 2019 Remi Collet <remi@remirepo.net> - 1.2.0-1
- update to 1.2.0

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 28 2019 Remi Collet <remi@remirepo.net> - 1.1.0-2
- License is MIT

* Fri Jun 28 2019 Remi Collet <remi@remirepo.net> - 1.1.0-1
- initial package, version 1.1.0

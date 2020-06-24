#
# Fedora spec file for php-google-auth
#
# Copyright (c) 2017-2019 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     google
%global github_name      google-auth-library-php
%global github_version   1.5.1
%global github_commit    0f75e20e7392e863f5550ed2c2d3d50af21710fb

%global composer_vendor  google
%global composer_project auth

# "php": ">=5.4"
%global php_min_ver 5.4
# "firebase/php-jwt": "~2.0|~3.0|~4.0|~5.0"
%global firebase_jwt_min_ver 2.0
%global firebase_jwt_max_ver 6.0
# "guzzlehttp/guzzle": "~5.3.1|~6.0"
#     NOTE: Min version not 5.3.1 to force version 6
%global guzzle_min_ver 6.0
%global guzzle_max_ver 7.0
# "guzzlehttp/psr7": "^1.2"
%global guzzle_psr7_min_ver 1.2
%global guzzle_psr7_max_ver 2.0
# "guzzlehttp/promises": "0.1.1|^1.3"
%global guzzle_promises_min_ver 0.1.1
%global guzzle_promises_max_ver 2.0
# "phpseclib/phpseclib": "^2"
%global phpseclib_min_ver 2.0
%global phpseclib_max_ver 3.0
# "psr/cache": "^1.0"
%global psr_cache_min_ver 1.0
%global psr_cache_max_ver 2.0
# "psr/http-message": "^1.0"
%global psr_http_message_min_ver 1.0
%global psr_http_message_max_ver 2.0

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       3%{?github_release}%{?dist}
Summary:       Google Auth Library for PHP

License:       ASL 2.0
URL:           https://github.com/%{github_owner}/%{github_name}
Source0:       %{url}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
# Tests
%if %{with_tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: php-composer(phpunit/phpunit)
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
BuildRequires: (php-composer(firebase/php-jwt) >= %{firebase_jwt_min_ver} with php-composer(firebase/php-jwt) < %{firebase_jwt_max_ver})
BuildRequires: (php-composer(guzzlehttp/guzzle) >= %{guzzle_min_ver} with php-composer(guzzlehttp/guzzle) < %{guzzle_max_ver})
BuildRequires: (php-composer(guzzlehttp/promises) >= %{guzzle_promises_min_ver} with php-composer(guzzlehttp/promises) < %{guzzle_promises_max_ver})
BuildRequires: (php-composer(guzzlehttp/psr7) >= %{guzzle_psr7_min_ver} with php-composer(guzzlehttp/psr7) < %{guzzle_psr7_max_ver})
BuildRequires: (php-composer(phpseclib/phpseclib) >= %{phpseclib_min_ver} with php-composer(phpseclib/phpseclib) < %{phpseclib_max_ver})
BuildRequires: (php-composer(psr/cache) >= %{psr_cache_min_ver} with php-composer(psr/cache) < %{psr_cache_max_ver})
BuildRequires: (php-composer(psr/http-message) >= %{psr_http_message_min_ver} with php-composer(psr/http-message) < %{psr_http_message_max_ver})
%else
BuildRequires: php-composer(firebase/php-jwt) <  %{firebase_jwt_max_ver}
BuildRequires: php-composer(firebase/php-jwt) >= %{firebase_jwt_min_ver}
BuildRequires: php-composer(guzzlehttp/guzzle) <  %{guzzle_max_ver}
BuildRequires: php-composer(guzzlehttp/guzzle) >= %{guzzle_min_ver}
BuildRequires: php-composer(guzzlehttp/promises) <  %{guzzle_promises_max_ver}
BuildRequires: php-composer(guzzlehttp/promises) >= %{guzzle_promises_min_ver}
BuildRequires: php-composer(guzzlehttp/psr7) <  %{guzzle_psr7_max_ver}
BuildRequires: php-composer(guzzlehttp/psr7) >= %{guzzle_psr7_min_ver}
BuildRequires: php-composer(phpseclib/phpseclib) <  %{phpseclib_max_ver}
BuildRequires: php-composer(phpseclib/phpseclib) >= %{phpseclib_min_ver}
BuildRequires: php-composer(psr/cache) <  %{psr_cache_max_ver}
BuildRequires: php-composer(psr/cache) >= %{psr_cache_min_ver}
BuildRequires: php-composer(psr/http-message) <  %{psr_http_message_max_ver}
BuildRequires: php-composer(psr/http-message) >= %{psr_http_message_min_ver}
%endif
## phpcompatinfo (computed from version 1.5.1)
BuildRequires: php-date
BuildRequires: php-hash
BuildRequires: php-json
BuildRequires: php-openssl
BuildRequires: php-pcre
BuildRequires: php-reflection
BuildRequires: php-spl
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:     php(language) >= %{php_min_ver}
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
Requires:     (php-composer(firebase/php-jwt) >= %{firebase_jwt_min_ver} with php-composer(firebase/php-jwt) < %{firebase_jwt_max_ver})
Requires:     (php-composer(guzzlehttp/guzzle) >= %{guzzle_min_ver} with php-composer(guzzlehttp/guzzle) < %{guzzle_max_ver})
Requires:     (php-composer(guzzlehttp/psr7) >= %{guzzle_psr7_min_ver} with php-composer(guzzlehttp/psr7) < %{guzzle_psr7_max_ver})
Requires:     (php-composer(psr/cache) >= %{psr_cache_min_ver} with php-composer(psr/cache) < %{psr_cache_max_ver})
Requires:     (php-composer(psr/http-message) >= %{psr_http_message_min_ver} with php-composer(psr/http-message) < %{psr_http_message_max_ver})
%else
Requires:     php-composer(firebase/php-jwt) <  %{firebase_jwt_max_ver}
Requires:     php-composer(firebase/php-jwt) >= %{firebase_jwt_min_ver}
Requires:     php-composer(guzzlehttp/guzzle) <  %{guzzle_max_ver}
Requires:     php-composer(guzzlehttp/guzzle) >= %{guzzle_min_ver}
Requires:     php-composer(guzzlehttp/psr7) <  %{guzzle_psr7_max_ver}
Requires:     php-composer(guzzlehttp/psr7) >= %{guzzle_psr7_min_ver}
Requires:     php-composer(psr/cache) <  %{psr_cache_max_ver}
Requires:     php-composer(psr/cache) >= %{psr_cache_min_ver}
Requires:     php-composer(psr/http-message) <  %{psr_http_message_max_ver}
Requires:     php-composer(psr/http-message) >= %{psr_http_message_min_ver}
%endif
# phpcompatinfo (computed from version 1.5.1)
Requires:      php-date
Requires:      php-hash
Requires:      php-json
Requires:      php-openssl
Requires:      php-pcre
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Weak dependencies
## composer.json: optional
Suggests:      php-composer(phpseclib/phpseclib)
Conflicts:     php-composer(phpseclib/phpseclib) < 2
Conflicts:     php-composer(phpseclib/phpseclib) >= 3

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

Conflicts:     php-google-apiclient < 2

%description
This is Google's officially supported PHP client library for using OAuth 2.0
authorization and authentication with Google APIs.

Autoloader: %{phpdir}/Google/Auth/autoload.php


%prep
%setup -qn %{github_name}-%{github_commit}


%build
: Create autoloader
cat <<'AUTOLOAD' | tee src/autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 */
require_once '%{phpdir}/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('Google\\Auth\\', __DIR__);

\Fedora\Autoloader\Dependencies::required([
    '%{phpdir}/Firebase/JWT/autoload.php',
    '%{phpdir}/GuzzleHttp/Psr7/autoload.php',
    '%{phpdir}/GuzzleHttp6/autoload.php',
    '%{phpdir}/Psr/Cache/autoload.php',
    '%{phpdir}/Psr/Http/Message/autoload.php',
]);

\Fedora\Autoloader\Dependencies::optional([
    '%{phpdir}/phpseclib/autoload.php',
]);
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}/Google
cp -rp src %{buildroot}%{phpdir}/Google/Auth


%check
%if %{with_tests}
: Create mock Composer autoloader
mkdir vendor
cat <<'BOOTSTRAP' | tee vendor/autoload.php
<?php

require_once '%{buildroot}%{phpdir}/Google/Auth/autoload.php';

\Fedora\Autoloader\Dependencies::required([
    '%{phpdir}/GuzzleHttp/Promise/autoload.php',
]);
BOOTSTRAP

: Skip test requiring network access
sed 's/function testMakeHttpClient/function SKIP_testMakeHttpClient/'\
    -i tests/FetchAuthTokenTest.php

: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which phpunit)
for PHP_EXEC in php %{?rhel:php55} php56 php70 php71 php72 php73 php74; do
    if which $PHP_EXEC; then
        $PHP_EXEC $PHPUNIT --verbose || RETURN_CODE=1
    fi
done
exit $RETURN_CODE
%else
: Tests skipped
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc *.md
%doc composer.json
%dir %{phpdir}/Google
     %{phpdir}/Google/Auth


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 24 2019 Shawn Iwinski <shawn@iwin.ski> - 1.5.1-1
- Update to 1.5.1 (RHBZ #1461830)
- Add range version dependencies for Fedora >= 27 || RHEL >= 8

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Mar 11 2017 Shawn Iwinski <shawn@iwin.ski> - 0.11.1-1
- Initial package

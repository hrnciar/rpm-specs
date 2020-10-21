#
# Fedora spec file for php-aws-sdk3
#
# Copyright (c) 2016-2020 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     aws
%global github_name      aws-sdk-php
%global github_version   3.152.0
%global github_commit    c5b43109dc0ecf77c4a18a8504ca3023f705b306

%global composer_vendor  aws
%global composer_project aws-sdk-php

# "php": ">=5.5"
%global php_min_ver 5.5
# "andrewsville/php-token-reflection": "^1.4"
%global tokenreflection_min_ver 1.4
%global tokenreflection_max_ver 2.0
# "aws/aws-php-sns-message-validator": "~1.0"
%global aws_sns_message_validator_min_ver 1.0
%global aws_sns_message_validator_max_ver 2.0
# "doctrine/cache": "~1.4"
#     NOTE: Min version not 1.4 because autoloader required
%global doctrine_cache_min_ver 1.4.1
%global doctrine_cache_max_ver 2.0
# "guzzlehttp/guzzle": "^5.3.3|^6.2.1|^7.0"
%global guzzle_min_ver 5.3.3
%global guzzle_max_ver 8.0
# "guzzlehttp/promises": "^1.0"
%global guzzle_promises_min_ver 1.0
%global guzzle_promises_max_ver 2.0
# "guzzlehttp/psr7": "^1.4.1"
%global guzzle_psr7_min_ver 1.4.1
%global guzzle_psr7_max_ver 2.0
# "mtdowling/jmespath.php": "^2.5"
%global jmespath_min_ver 2.5
%global jmespath_max_ver 3.0
# "paragonie/random_compat": ">= 2"
#     NOTE: Max version added to prevent issues if v3 is ever released for some reason
%global paragonie_random_compat_min_ver 2.0
%global paragonie_random_compat_max_ver 3.0
# "psr/cache": "^1.0"
%global psr_cache_min_ver 1.0
%global psr_cache_max_ver 2.0
# "psr/simple-cache": "^1.0"
%global psr_simple_cache_min_ver 1.0
%global psr_simple_cache_max_ver 2.0

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

# Range dependencies supported?
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
%global with_range_dependencies 1
%else
%global with_range_dependencies 0
%endif

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-aws-sdk3
Version:       %{github_version}
Release:       1%{?dist}
Summary:       Amazon Web Services framework for PHP

License:       ASL 2.0
URL:           http://aws.amazon.com/sdkforphp

# GitHub export does not include tests.
# Run php-aws-sdk3-get-source.sh to create full source.
Source0:       %{name}-%{github_version}-%{github_commit}.tar.gz
Source1:       %{name}-get-source.sh

BuildArch:     noarch
# Library version value and autoloader check
BuildRequires: php-cli
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
%if %{with_range_dependencies}
BuildRequires: (php-composer(guzzlehttp/guzzle) >= %{guzzle_min_ver} with php-composer(guzzlehttp/guzzle) < %{guzzle_max_ver})
BuildRequires: (php-composer(guzzlehttp/promises) >= %{guzzle_promises_min_ver} with php-composer(guzzlehttp/promises) < %{guzzle_promises_max_ver})
BuildRequires: (php-composer(guzzlehttp/psr7) >= %{guzzle_psr7_min_ver} with php-composer(guzzlehttp/psr7) < %{guzzle_psr7_max_ver})
BuildRequires: (php-composer(mtdowling/jmespath.php) >= %{jmespath_min_ver} with php-composer(mtdowling/jmespath.php) < %{jmespath_max_ver})
%else
BuildRequires: php-composer(guzzlehttp/guzzle) <  %{guzzle_max_ver}
BuildRequires: php-composer(guzzlehttp/guzzle) >= %{guzzle_min_ver}
BuildRequires: php-composer(guzzlehttp/promises) <  %{guzzle_promises_max_ver}
BuildRequires: php-composer(guzzlehttp/promises) >= %{guzzle_promises_min_ver}
BuildRequires: php-composer(guzzlehttp/psr7) <  %{guzzle_psr7_max_ver}
BuildRequires: php-composer(guzzlehttp/psr7) >= %{guzzle_psr7_min_ver}
BuildRequires: php-composer(mtdowling/jmespath.php) <  %{jmespath_max_ver}
BuildRequires: php-composer(mtdowling/jmespath.php) >= %{jmespath_min_ver}
%endif
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
# Tests
%if %{with_tests}
## Classmap
BuildRequires: php-composer(theseer/autoload)
## composer.json
BuildRequires: php-composer(phpunit/phpunit)
%if %{with_range_dependencies}
BuildRequires: (php-composer(andrewsville/php-token-reflection) >= %{tokenreflection_min_ver} with php-composer(andrewsville/php-token-reflection) < %{tokenreflection_max_ver})
BuildRequires: (php-composer(aws/aws-php-sns-message-validator) >= %{aws_sns_message_validator_min_ver} with php-composer(aws/aws-php-sns-message-validator) < %{aws_sns_message_validator_max_ver})
BuildRequires: (php-composer(doctrine/cache) >= %{doctrine_cache_min_ver} with php-composer(doctrine/cache) < %{doctrine_cache_max_ver})
BuildRequires: (php-composer(paragonie/random_compat) >= %{paragonie_random_compat_min_ver} with php-composer(paragonie/random_compat) < %{paragonie_random_compat_max_ver})
BuildRequires: (php-composer(psr/cache) >= %{psr_cache_min_ver} with php-composer(psr/cache) < %{psr_cache_max_ver})
BuildRequires: (php-composer(psr/simple-cache) >= %{psr_simple_cache_min_ver} with php-composer(psr/simple-cache) < %{psr_simple_cache_max_ver})
%else
BuildRequires: php-composer(andrewsville/php-token-reflection) <  %{tokenreflection_max_ver}
BuildRequires: php-composer(andrewsville/php-token-reflection) >= %{tokenreflection_min_ver}
BuildRequires: php-composer(aws/aws-php-sns-message-validator) <  %{aws_sns_message_validator_max_ver}
BuildRequires: php-composer(aws/aws-php-sns-message-validator) >= %{aws_sns_message_validator_min_ver}
BuildRequires: php-composer(doctrine/cache) <  %{doctrine_cache_max_ver}
BuildRequires: php-composer(doctrine/cache) >= %{doctrine_cache_min_ver}
BuildRequires: php-composer(paragonie/random_compat) <  %{paragonie_random_compat_max_ver}
BuildRequires: php-composer(paragonie/random_compat) >= %{paragonie_random_compat_min_ver}
BuildRequires: php-composer(psr/cache) <  %{psr_cache_max_ver}
BuildRequires: php-composer(psr/cache) >= %{psr_cache_min_ver}
BuildRequires: php-composer(psr/simple-cache) <  %{psr_simple_cache_max_ver}
BuildRequires: php-composer(psr/simple-cache) >= %{psr_simple_cache_min_ver}
%endif
BuildRequires: php-curl
BuildRequires: php-dom
BuildRequires: php-json
BuildRequires: php-openssl
BuildRequires: php-pcntl
BuildRequires: php-pcre
BuildRequires: php-simplexml
BuildRequires: php-sockets
## phpcompatinfo (computed from version 3.152.0)
BuildRequires: php-date
BuildRequires: php-filter
BuildRequires: php-hash
BuildRequires: php-iconv
BuildRequires: php-libxml
BuildRequires: php-mbstring
BuildRequires: php-posix
BuildRequires: php-reflection
BuildRequires: php-session
BuildRequires: php-soap
BuildRequires: php-spl
BuildRequires: php-tidy
BuildRequires: php-xmlwriter
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
%if %{with_range_dependencies}
Requires:      (php-composer(guzzlehttp/guzzle) >= %{guzzle_min_ver} with php-composer(guzzlehttp/guzzle) < %{guzzle_max_ver})
Requires:      (php-composer(guzzlehttp/promises) >= %{guzzle_promises_min_ver} with php-composer(guzzlehttp/promises) < %{guzzle_promises_max_ver})
Requires:      (php-composer(guzzlehttp/psr7) >= %{guzzle_psr7_min_ver} with php-composer(guzzlehttp/psr7) < %{guzzle_psr7_max_ver})
Requires:      (php-composer(mtdowling/jmespath.php) >= %{jmespath_min_ver} with php-composer(mtdowling/jmespath.php) < %{jmespath_max_ver})
%else
Requires:      php-composer(guzzlehttp/guzzle) <  %{guzzle_max_ver}
Requires:      php-composer(guzzlehttp/guzzle) >= %{guzzle_min_ver}
Requires:      php-composer(guzzlehttp/promises) <  %{guzzle_promises_max_ver}
Requires:      php-composer(guzzlehttp/promises) >= %{guzzle_promises_min_ver}
Requires:      php-composer(guzzlehttp/psr7) <  %{guzzle_psr7_max_ver}
Requires:      php-composer(guzzlehttp/psr7) >= %{guzzle_psr7_min_ver}
Requires:      php-composer(mtdowling/jmespath.php) <  %{jmespath_max_ver}
Requires:      php-composer(mtdowling/jmespath.php) >= %{jmespath_min_ver}
%endif
Requires:      php-json
Requires:      php-pcre
Requires:      php-simplexml
# phpcompatinfo (computed from version 3.152.0)
Requires:      php-date
Requires:      php-filter
Requires:      php-hash
Requires:      php-iconv
Requires:      php-libxml
Requires:      php-mbstring
Requires:      php-reflection
Requires:      php-session
Requires:      php-spl
Requires:      php-tidy
Requires:      php-xmlwriter
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Weak dependencies
## composer.json: optional
Suggests:      php-curl
Suggests:      php-openssl
Suggests:      php-sockets
Suggests:      php-composer(doctrine/cache)
Suggests:      php-composer(aws/aws-php-sns-message-validator)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
The AWS SDK for PHP makes it easy for developers to access Amazon Web
Services [1] in their PHP code, and build robust applications and software
using services like Amazon S3, Amazon DynamoDB, Amazon Glacier, etc.

Autoloader: %{phpdir}/Aws3/autoload.php

[1] http://aws.amazon.com/


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

\Fedora\Autoloader\Autoload::addPsr4('Aws\\', __DIR__);

\Fedora\Autoloader\Dependencies::required([
    __DIR__.'/functions.php',
    [
        '%{phpdir}/GuzzleHttp7/autoload.php',
        '%{phpdir}/GuzzleHttp6/autoload.php',
        '%{phpdir}/GuzzleHttp/autoload.php',
    ],
    '%{phpdir}/GuzzleHttp/Promise/autoload.php',
    '%{phpdir}/GuzzleHttp/Psr7/autoload.php',
    '%{phpdir}/JmesPath/autoload.php',
]);

\Fedora\Autoloader\Dependencies::optional([
    '%{phpdir}/Aws/Sns/autoload.php',
    '%{phpdir}/Doctrine/Common/Cache/autoload.php',
]);
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}/Aws3
cp -pr src/* %{buildroot}%{phpdir}/Aws3/


%check
: Library version value and autoloader check
%{_bindir}/php -r '
    require_once "%{buildroot}%{phpdir}/Aws3/autoload.php";
    $version = \Aws\Sdk::VERSION;
    echo "Version $version (expected %{version})\n";
    exit(version_compare("%{version}", "$version", "=") ? 0 : 1);
'

%if %{with_tests}
: Create tests classmap
%{_bindir}/phpab --nolower --output bootstrap.classmap.php build/

: Create tests bootstrap
cat <<'BOOTSTRAP' | tee bootstrap.php
<?php
error_reporting(-1);
date_default_timezone_set('UTC');

require_once '%{buildroot}%{phpdir}/Aws3/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('Aws\\Test\\', __DIR__.'/tests');
\Fedora\Autoloader\Autoload::addPsr4('TokenReflection\\', '%{phpdir}/TokenReflection');

\Fedora\Autoloader\Dependencies::required([
    __DIR__.'/bootstrap.classmap.php',
    '%{phpdir}/Psr/Cache/autoload.php',
    '%{phpdir}/Psr/SimpleCache/autoload.php',
    '%{phpdir}/random_compat/autoload.php',
]);

class_alias('PHPUnit_Framework_Error_Warning', 'PHPUnit\\Framework\\Error\\Warning');
class_alias('PHPUnit_Framework_Constraint_Callback', 'PHPUnit\\Framework\\Constraint\\Callback');
BOOTSTRAP

: Skip tests known to fail
sed 's/function testValidatesInput/function SKIP_testValidatesInput/' \
    -i tests/Api/ValidatorTest.php
sed -e 's/function testUserAgentAlwaysStartsWithSdkAgentString/function SKIP_testUserAgentAlwaysStartsWithSdkAgentString/' \
    -e 's/function testValidatesCallables/function SKIP_testValidatesCallables/' \
    -e 's/function testValidatesInput/function SKIP_testValidatesInput/' \
    -i tests/ClientResolverTest.php
sed 's/function testEmitsDebugInfo/function SKIP_testEmitsDebugInfo/' \
    -i tests/TraceMiddlewareTest.php
sed -e 's/function testTracksAwsSpecificExceptions/function SKIP_testTracksAwsSpecificExceptions/' \
    -e 's/function testTracksExceptions/function SKIP_testTracksExceptions/' \
    -i tests/TraceMiddlewareTest.php
rm -f \
    tests/Integ/GuzzleV5HandlerTest.php \
    tests/Integ/GuzzleV6StreamHandlerTest.php \
    tests/S3/Crypto/S3EncryptionClientTest.php

: Skip tests that include 64-bit format codes on 32-bit PHP
if [ $(php -r 'echo PHP_INT_SIZE === 4 ? 32 : 64;') == 32 ]
then
    sed -e 's/function testPassesComplianceTest/function SKIP_testPassesComplianceTest/' \
        -e 's/function testEmitsEvents/function SKIP_testEmitsEvents/' \
        -e 's/function testThrowsOnUnknownEventType/function SKIP_testThrowsOnUnknownEventType/' \
        -i tests/Api/Parser/DecodingEventStreamIteratorTest.php
    sed -e 's/function testEmitsEvents/function SKIP_testEmitsEvents/' \
        -e 's/function testThrowsOnUnknownEventType/function SKIP_testThrowsOnUnknownEventType/' \
        -i tests/Api/Parser/EventParsingIteratorTest.php
fi

export AWS_ACCESS_KEY_ID=foo
export AWS_SECRET_ACCESS_KEY=bar

: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which phpunit)
for PHP_EXEC in "" php56 php70 php71 php72 php73 php74; do
    if [ -z "$PHP_EXEC" ] || which $PHP_EXEC; then
        $PHP_EXEC $PHPUNIT -d memory_limit=1G --verbose  --testsuite=unit \
            --bootstrap bootstrap.php || RETURN_CODE=1
    fi
done
exit $RETURN_CODE
%else
: Tests skipped
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE.md
%doc CHANGELOG.md
%doc composer.json
%doc README.md
%doc UPGRADING.md
%{phpdir}/Aws3


%changelog
* Fri Sep 04 2020 Shawn Iwinski <shawn@iwin.ski> - 3.152.0-1
- Update to 3.152.0 (RHBZ #1819948)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.134.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Mar 31 2020 Shawn Iwinski <shawn@iwin.ski> - 3.134.0-1
- Update to 3.134.0 (RHBZ #1806756)

* Sat Feb 22 2020 Shawn Iwinski <shawn@iwin.ski> - 3.133.20-1
- Update to 3.133.20 (RHBZ #1750925)
- Fix FTBFS (RHBZ #1799865)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.111.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 09 2019 Shawn Iwinski <shawn@iwin.ski> - 3.111.0-1
- Update to 3.111.0 (RHBZ #1714768)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.95.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 24 2019 Shawn Iwinski <shawn@iwin.ski> - 3.95.0-1
- Update to 3.95.0 (RHBZ #1695281)

* Mon Apr 01 2019 Shawn Iwinski <shawn@iwin.ski> - 3.91.0-1
- Update to 3.91.0 (RHBZ #1680149)

* Thu Feb 21 2019 Shawn Iwinski <shawn@iwin.ski> - 3.87.15-1
- Update to 3.87.15 (RHBZ #1599469)
- Remove php-composer(nette/neon) dependency

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.62.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.62.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jul 07 2018 Shawn Iwinski <shawn@iwin.ski> - 3.62.10-1
- Update to 3.62.10 (RHBZ #1563020)

* Sat Mar 31 2018 Shawn Iwinski <shawn@iwin.ski> - 3.53.0-1
- Update to 3.53.0 (RHBZ #1525280)
- Add range version dependencies for Fedora >= 27 || RHEL >= 8

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.46.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Dec 11 2017 Shawn Iwinski <shawn@iwin.ski> - 3.46.0-1
- Update to 3.46.0 (RHBZ #1503361)

* Thu Oct 05 2017 Shawn Iwinski <shawn@iwin.ski> - 3.36.20-1
- Update to 3.36.20 (RHBZ #1484590)

* Tue Aug 22 2017 Shawn Iwinski <shawn@iwin.ski> - 3.34.0-1
- Update to 3.34.0 (RHBZ #1476044)

* Thu Jul 27 2017 Shawn Iwinski <shawn@iwin.ski> - 3.32.0-1
- Update to 3.32.0 (RHBZ #1472012)
- Remove patch to fix PHP 7.2 failures

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.31.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 17 2017 Shawn Iwinski <shawn@iwin.ski> - 3.31.5-1
- Updated to 3.31.5 (RHBZ #1468058)

* Sun Jul 02 2017 Shawn Iwinski <shawn@iwin.ski> - 3.31.0-1
- Updated to 3.31.0 (RHBZ #1464279)

* Sat Jun 24 2017 Shawn Iwinski <shawn@iwin.ski> - 3.30.0-2
- Add patch to fix PHP 7.2 failures
- Add php72 to SCL tests
- Add max versions to some additional BuildRequires dependencies

* Wed Jun 21 2017 Shawn Iwinski <shawn@iwin.ski> - 3.30.0-1
- Updated to 3.30.0 (RHBZ #1449422)

* Fri May 05 2017 Shawn Iwinski <shawn@iwin.ski> - 3.27.0-1
- Updated to 3.27.0 (RHBZ #1444239)

* Thu Apr 20 2017 Shawn Iwinski <shawn@iwin.ski> - 3.26.0-1
- Updated to 3.26.0 (RHBZ #1438105)

* Fri Mar 31 2017 Shawn Iwinski <shawn@iwin.ski> - 3.25.0-1
- Updated to 3.25.0 (RHBZ #1431302)

* Fri Mar 10 2017 Shawn Iwinski <shawn@iwin.ski> - 3.24.1-1
- Updated to 3.24.1 (RHBZ #1415013)
- Added max versions to BuildRequires
- Removed conflicts for weak dependencies' version constraints

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.21.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 18 2017 Shawn Iwinski <shawn@iwin.ski> - 3.21.0-1
- Updated to 3.21.0 (RHBZ #1405254)

* Mon Dec 26 2016 Shawn Iwinski <shawn@iwin.ski> - 3.20.11-1
- Updated to 3.20.11 (RHBZ #1405254)
- Run upstream tests with SCLs if they are available

* Thu Dec 15 2016 Shawn Iwinski <shawn@iwin.ski> - 3.20.6-1
- Updated to 3.20.6 (RHBZ #1402170)

* Thu Dec 01 2016 Shawn Iwinski <shawn@iwin.ski> - 3.20.0-1
- Updated to 3.20.0 (RHBZ #1397218)

* Wed Nov 23 2016 Remi Collet <remi@fedoraproject.org> - 3.19.32-1
- Updated to 3.19.32, fix FTBFS

* Mon Nov 21 2016 Shawn Iwinski <shawn@iwin.ski> - 3.19.30-1
- Updated to 3.19.30 (RHBZ #1380046)
- Switched autoloader from php-composer(symfony/class-loader) to
  php-composer(fedora/autoloader)

* Sun Sep 25 2016 Shawn Iwinski <shawn@iwin.ski> - 3.19.10-1
- Updated to 3.19.10 (RHBZ #1376241)

* Sun Sep 11 2016 Shawn Iwinski <shawn@iwin.ski> - 3.19.6-1
- Updated to 3.19.6 (RHBZ #1365099)

* Fri Jul 29 2016 Shawn Iwinski <shawn@iwin.ski> - 3.18.35-1
- Updated to 3.18.24 (RHBZ #1353056)

* Mon Jul 04 2016 Shawn Iwinski <shawn@iwin.ski> - 3.18.24-1
- Updated to 3.18.24 (RHBZ #1342771)

* Wed Apr 20 2016 Shawn Iwinski <shawn@iwin.ski> - 3.18.0-1
- Updated to 3.18.0
- Modified autoloader to not use @include_once for optional dependencies
- Set test memory_limit because build issues on certain systems

* Tue Apr 12 2016 Shawn Iwinski <shawn@iwin.ski> - 3.17.6-1
- Initial package

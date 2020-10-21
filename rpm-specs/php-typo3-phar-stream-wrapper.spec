#
# Fedora spec file for php-typo3-phar-stream-wrapper
#
# Copyright (c) 2019 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     TYPO3
%global github_name      phar-stream-wrapper
%global github_version   3.1.3
%global github_commit    586ff60beea128e069a5dc271d3d8133a9bc460a

%global composer_vendor  typo3
%global composer_project phar-stream-wrapper

# "php": "^7.0"
%global php_min_ver 7.0

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       3%{?github_release}%{?dist}
Summary:       Interceptors for PHP's native phar:// stream handling

License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}

# GitHub export does not include tests.
# Run php-typo3-phar-stream-wrapper2-get-source.sh to create full source.
Source0:       %{name}-%{github_version}-%{github_commit}.tar.gz
Source1:       %{name}-get-source.sh

BuildArch:     noarch
# Tests
%if %{with_tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: php-composer(phpunit/phpunit)
BuildRequires: php-fileinfo
BuildRequires: php-json
## phpcompatinfo for version 3.1.2
BuildRequires: php-pcre
BuildRequires: php-pecl(opcache)
BuildRequires: php-reflection
BuildRequires: php-spl
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
Requires:      php-json
# phpcompatinfo for version 3.1.2
Requires:      php-pcre
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Weak dependencies
%if 0%{?fedora} >= 21 || 0%{?rhel} >= 8
Suggests:      php-fileinfo
Suggests:      php-pecl(opcache)
%endif

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
%{summary}.

Autoloader: %{phpdir}/TYPO3/PharStreamWrapper/autoload.php


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

\Fedora\Autoloader\Autoload::addPsr4('TYPO3\\PharStreamWrapper\\', __DIR__);
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}/TYPO3
cp -rp src %{buildroot}%{phpdir}/TYPO3/PharStreamWrapper


%check
%if %{with_tests}
: Create tests bootstrap
cat <<'BOOTSTRAP' | tee bootstrap.php
<?php
require '%{buildroot}%{phpdir}/TYPO3/PharStreamWrapper/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('TYPO3\\PharStreamWrapper\\Tests\\', __DIR__.'/tests');

if (!class_exists('PHPUnit\\Framework\\Error\\Warning')) {
  class_alias('PHPUnit_Framework_Error_Warning', 'PHPUnit\\Framework\\Error\\Warning');
}
BOOTSTRAP

: Skip tests known to fail in rpmbuild mock env
rm -f tests/Functional/Interceptor/PharExtensionInterceptorTest.php

: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which phpunit)
for PHP_EXEC in php php71 php72 php73 php74; do
    if [ "php" == "$PHP_EXEC" ] || which $PHP_EXEC; then
        $PHP_EXEC $PHPUNIT --verbose --bootstrap bootstrap.php || RETURN_CODE=1
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
%dir %{phpdir}/TYPO3
     %{phpdir}/TYPO3/PharStreamWrapper


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Nov 16 2019 Shawn Iwinski <shawn@iwin.ski> - 3.1.3-1
- Update to 3.1.3 (RHBZ #1763201)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 16 2019 Shawn Iwinski <shawn@iwin.ski> - 3.1.2-1
- Update to 3.1.2

* Wed May 08 2019 Shawn Iwinski <shawn@iwin.ski> - 3.1.1-1
- Update to 3.1.1 (RHBZ #1708651, #1708646, #1708649)
- https://typo3.org/security/advisory/typo3-psa-2019-007/
- https://nvd.nist.gov/vuln/detail/CVE-2019-11831
- https://typo3.org/security/advisory/typo3-psa-2019-008/
- https://nvd.nist.gov/vuln/detail/CVE-2019-11830

* Sat Feb 23 2019 Shawn Iwinski <shawn@iwin.ski> - 3.0.1-1
- Initial package

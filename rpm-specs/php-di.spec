#
# Fedora spec file for php-di
#
# Copyright (c) 2016-2019 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     PHP-DI
%global github_name      PHP-DI
%global github_version   6.0.11
%global github_commit    9bdcc2f41f5fb700ddd01bc4fa8d5bd7b3f94620

%global composer_vendor  php-di
%global composer_project php-di

# "php": ">=7.0.0"
%global php_min_ver 7.0.0
# "doctrine/annotations": "~1.2"
%global doctrine_annotations_min_ver 1.2
%global doctrine_annotations_max_ver 2.0
# "jeremeamia/superclosure": "^2.0"
%global jeremeamia_superclosure_min_ver 2.0
%global jeremeamia_superclosure_max_ver 3.0
# "mnapoli/phpunit-easymock": "~1.0"
%global phpunit_easymock_min_ver 1.0
%global phpunit_easymock_max_ver 2.0
# "nikic/php-parser": "^2.0|^3.0|^4.0"
%global nikic_php_parser_min_ver 2.0
%global nikic_php_parser_max_ver 5.0
# "ocramius/proxy-manager": "~2.0.2"
%global proxy_manager_min_ver 2.0.2
%global proxy_manager_max_ver 3.0
# "php-di/invoker": "^2.0"
%global di_invoker_min_ver 2.0
%global di_invoker_max_ver 3.0
# "php-di/phpdoc-reader": "^2.0.1"
%global di_phpdoc_reader_min_ver 2.0.1
%global di_phpdoc_reader_max_ver 3.0
# "psr/container": "^1.0"
%global psr_container_min_ver 1.0
%global psr_container_max_ver 2.0

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          %{composer_project}
Version:       %{github_version}
Release:       2%{?github_release}%{?dist}
Summary:       The dependency injection container for humans

License:       MIT
URL:           http://php-di.org/

# GitHub export does not include tests.
# Run php-di-get-source.sh to create full source.
Source0:       %{name}-%{github_version}-%{github_commit}.tar.gz
Source1:       %{name}-get-source.sh

BuildArch:     noarch
# Tests
%if %{with_tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: phpunit6
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
BuildRequires: (php-composer(doctrine/annotations) >= %{doctrine_annotations_min_ver} with php-composer(doctrine/annotations) < %{doctrine_annotations_max_ver})
BuildRequires: (php-composer(jeremeamia/superclosure) >= %{jeremeamia_superclosure_min_ver} with php-composer(jeremeamia/superclosure) < %{jeremeamia_superclosure_max_ver})
BuildRequires: (php-composer(mnapoli/phpunit-easymock) >= %{phpunit_easymock_min_ver} with php-composer(mnapoli/phpunit-easymock) < %{phpunit_easymock_max_ver})
BuildRequires: (php-composer(nikic/php-parser) >= %{nikic_php_parser_min_ver} with php-composer(nikic/php-parser) < %{nikic_php_parser_max_ver})
BuildRequires: (php-composer(ocramius/proxy-manager) >= %{proxy_manager_min_ver} with php-composer(ocramius/proxy-manager) < %{proxy_manager_max_ver})
BuildRequires: (php-composer(php-di/invoker) >= %{di_invoker_min_ver} with php-composer(php-di/invoker) < %{di_invoker_max_ver})
BuildRequires: (php-composer(php-di/phpdoc-reader) >= %{di_phpdoc_reader_min_ver} with php-composer(php-di/phpdoc-reader) < %{di_phpdoc_reader_max_ver})
BuildRequires: (php-composer(psr/container) >= %{psr_container_min_ver} with php-composer(psr/container) < %{psr_container_max_ver})
%else
BuildRequires: php-composer(doctrine/annotations) <  %{doctrine_annotations_max_ver}
BuildRequires: php-composer(doctrine/annotations) >= %{doctrine_annotations_min_ver}
BuildRequires: php-composer(jeremeamia/superclosure) <  %{jeremeamia_superclosure_max_ver}
BuildRequires: php-composer(jeremeamia/superclosure) >= %{jeremeamia_superclosure_min_ver}
BuildRequires: php-composer(mnapoli/phpunit-easymock) <  %{phpunit_easymock_max_ver}
BuildRequires: php-composer(mnapoli/phpunit-easymock) >= %{phpunit_easymock_min_ver}
BuildRequires: php-composer(nikic/php-parser) <  %{nikic_php_parser_max_ver}
BuildRequires: php-composer(nikic/php-parser) >= %{nikic_php_parser_min_ver}
BuildRequires: php-composer(ocramius/proxy-manager) <  %{proxy_manager_max_ver}
BuildRequires: php-composer(ocramius/proxy-manager) >= %{proxy_manager_min_ver}
BuildRequires: php-composer(php-di/invoker) <  %{di_invoker_max_ver}
BuildRequires: php-composer(php-di/invoker) >= %{di_invoker_min_ver}
BuildRequires: php-composer(php-di/phpdoc-reader) <  %{di_phpdoc_reader_max_ver}
BuildRequires: php-composer(php-di/phpdoc-reader) >= %{di_phpdoc_reader_min_ver}
BuildRequires: php-composer(psr/container) <  %{psr_container_max_ver}
BuildRequires: php-composer(psr/container) >= %{psr_container_min_ver}
%endif
## phpcompatinfo (computed from version 6.0.8)
BuildRequires: php-date
BuildRequires: php-json
BuildRequires: php-pcre
BuildRequires: php-reflection
BuildRequires: php-spl
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
Requires:      (php-composer(jeremeamia/superclosure) >= %{jeremeamia_superclosure_min_ver} with php-composer(jeremeamia/superclosure) < %{jeremeamia_superclosure_max_ver})
Requires:      (php-composer(nikic/php-parser) >= %{nikic_php_parser_min_ver} with php-composer(nikic/php-parser) < %{nikic_php_parser_max_ver})
Requires:      (php-composer(php-di/invoker) >= %{di_invoker_min_ver} with php-composer(php-di/invoker) < %{di_invoker_max_ver})
Requires:      (php-composer(php-di/phpdoc-reader) >= %{di_phpdoc_reader_min_ver} with php-composer(php-di/phpdoc-reader) < %{di_phpdoc_reader_max_ver})
Requires:      (php-composer(psr/container) >= %{psr_container_min_ver} with php-composer(psr/container) < %{psr_container_max_ver})
%else
Requires:      php-composer(jeremeamia/superclosure) <  %{jeremeamia_superclosure_max_ver}
Requires:      php-composer(jeremeamia/superclosure) >= %{jeremeamia_superclosure_min_ver}
Requires:      php-composer(nikic/php-parser) <  %{nikic_php_parser_max_ver}
Requires:      php-composer(nikic/php-parser) >= %{nikic_php_parser_min_ver}
Requires:      php-composer(php-di/invoker) <  %{di_invoker_max_ver}
Requires:      php-composer(php-di/invoker) >= %{di_invoker_min_ver}
Requires:      php-composer(php-di/phpdoc-reader) <  %{di_phpdoc_reader_max_ver}
Requires:      php-composer(php-di/phpdoc-reader) >= %{di_phpdoc_reader_min_ver}
Requires:      php-composer(psr/container) <  %{psr_container_max_ver}
Requires:      php-composer(psr/container) >= %{psr_container_min_ver}
%endif
# phpcompatinfo (computed from version 5.4.6)
Requires:      php-json
Requires:      php-pcre
Requires:      php-reflection
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Weak dependencies
%if 0%{?fedora} >= 21 || 0%{?rhel} >= 8
Suggests:      php-composer(doctrine/annotations)
Suggests:      php-composer(ocramius/proxy-manager)
Suggests:      php-pecl(apcu)
%endif

# php-{COMPOSER_VENDOR}-{COMPOSER_PROJECT}
Provides:      php-%{composer_vendor}-%{composer_project} = %{version}-%{release}
# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}
Provides:      php-composer(psr/container-implementation) = 1.0

%description
%{summary}.

Autoloader: %{phpdir}/DI/autoload.php


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

\Fedora\Autoloader\Autoload::addPsr4('DI\\', __DIR__);
require_once __DIR__.'/functions.php';

\Fedora\Autoloader\Dependencies::required([
    [
        '%{phpdir}/PhpParser4/autoload.php',
        '%{phpdir}/PhpParser3/autoload.php',
        '%{phpdir}/PhpParser2/autoload.php',
    ],
    '%{phpdir}/Invoker/autoload.php',
    '%{phpdir}/PhpDocReader/autoload.php',
    '%{phpdir}/Psr/Container/autoload.php',
    '%{phpdir}/SuperClosure/autoload.php',
]);

\Fedora\Autoloader\Dependencies::optional([
    '%{phpdir}/Doctrine/Common/Annotations/autoload.php',
    '%{phpdir}/ProxyManager/autoload.php',
]);
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}
cp -rp src %{buildroot}%{phpdir}/DI


%check
%if %{with_tests}
: Create tests bootstrap
cat <<'BOOTSTRAP' | tee bootstrap.php
<?php
require '%{buildroot}%{phpdir}/DI/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('DI\\Test\\IntegrationTest\\', __DIR__.'/tests/IntegrationTest');
\Fedora\Autoloader\Autoload::addPsr4('DI\\Test\\UnitTest\\', __DIR__.'/tests/UnitTest');

require_once '%{phpdir}/EasyMock/autoload.php';
BOOTSTRAP

: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which phpunit6)
for PHP_EXEC in "" php71 php72 php73 php74; do
    if [ -z "$PHP_EXEC" ] || which $PHP_EXEC; then
        $PHP_EXEC $PHPUNIT --verbose --bootstrap bootstrap.php \
            || RETURN_CODE=1
    fi
done
exit $RETURN_CODE
%else
: Tests skipped
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc change-log.md
%doc composer.json
%doc README.md
%{phpdir}/DI


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 14 2019 Shawn Iwinski <shawn@iwin.ski> - 6.0.11-1
- Update to 6.0.11 (RHBZ #1763756)
- Use PHPUnit 6

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun May 26 2019 Shawn Iwinski <shawn@iwin.ski> - 6.0.8-1
- Update to 6.0.8 (RHBZ #1442587)

* Tue May 14 2019 Shawn Iwinski <shawn@iwin.ski> - 5.4.6-7
- Add range version dependencies for Fedora >= 27 || RHEL >= 8

* Fri May 10 2019 Shawn Iwinski <shawn@iwin.ski> - 5.4.6-6
- Update to 5.4.6

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Oct 31 2017 Remi Collet <remi@remirepo.net> - 5.4.3-2
- fix FTBFS from Koschei, add upstream patch for PHP 7.2

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Apr 14 2017 Shawn Iwinski <shawn@iwin.ski> - 5.4.3-1
- Update to 5.4.3 (RHBZ #1442382)

* Sun Apr 02 2017 Shawn Iwinski <shawn@iwin.ski> - 5.4.2-1
- Update to 5.4.2 (RHBZ #1435627)
- Add max versions to BuildRequires
- Remove conflicts for weak dependencies' version constraints
- Switch autoloader to php-composer(fedora/autoloader)
- Test with SCLs and both phpunit and phpunit6 if available

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Oct 28 2016 Remi Collet <remi@fedoraproject.org> - 5.4.0-1
- update to 5.4.0
- raise dependency on php-di/invoker >= 1.3.2
- raise dependency on php >=5.5.0
- allow ocramius/proxy-manager 2.0

* Sun Jul 31 2016 Shawn Iwinski <shawn@iwin.ski> - 5.2.2-3
- Updated autoloader to not use `@include_once`
- Skipped tests known to fail with "php-composer(php-di/invoker)" >= 1.3.2
-- See https://github.com/PHP-DI/Invoker/issues/13

* Sun Mar 13 2016 Shawn Iwinski <shawn@iwin.ski> - 5.2.2-2
- Fix weak dependency version constraints

* Fri Mar 11 2016 Shawn Iwinski <shawn@iwin.ski> - 5.2.2-1
- Updated to 5.2.2 (RHBZ #1298928)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 03 2016 Shawn Iwinski <shawn@iwin.ski> - 5.2.0-1
- Initial package

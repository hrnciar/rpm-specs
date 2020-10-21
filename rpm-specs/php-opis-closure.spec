#
# Fedora spec file for php-opis-closure
#
# Copyright (c) 2020 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner      opis
%global github_name       closure
%global github_version    3.6.0
%global github_commit     c547f8262a5fa9ff507bd06cc394067b83a75085

%global composer_vendor   opis
%global composer_project  closure

%global namespace_vendor  Opis
%global namespace_project Closure

# "php": "^5.4 || ^7.0 || ^8.0"
%global php_min_ver 5.4
# "jeremeamia/superclosure": "^2.0"
%global jeremeamia_superclosure_min_ver 2.0
%global jeremeamia_superclosure_max_ver 3.0

# PHPUnit
## v9 (PHP 7.3)
%if 0%{?fedora} >= 30 || 0%{?rhel} >= 9
%global phpunit_require phpunit9
%global phpunit_exec    phpunit9
%else
## v8 (PHP 7.2)
%if 0%{?fedora} >= 28 || 0%{?rhel} >= 8
%global phpunit_require phpunit8
%global phpunit_exec    phpunit8
%else
## Pre-v8
%global phpunit_require php-composer(phpunit/phpunit)
%global phpunit_exec    phpunit
%endif
%endif

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

# Range dependencies supported?
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
%global with_range_dependencies 1
%else
%global with_range_dependencies 0
%endif

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}%{?namespace_version}
Version:       %{github_version}
Release:       1%{?github_release}%{?dist}
Summary:       A library that can be used to serialize closures and arbitrary objects

License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}

# GitHub export does not include tests
# Run php-opis-closure-get-source.sh to create full source
Source0:       %{name}-%{github_version}-%{github_commit}.tar.gz
Source1:       %{name}-get-source.sh

BuildArch:     noarch
# Tests
%if %{with_tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: %{phpunit_require}
%if %{with_range_dependencies}
BuildRequires: (php-composer(jeremeamia/superclosure) >= %{jeremeamia_superclosure_min_ver} with php-composer(jeremeamia/superclosure) < %{jeremeamia_superclosure_max_ver})
%else
BuildRequires: php-composer(jeremeamia/superclosure) <  %{jeremeamia_superclosure_max_ver}
BuildRequires: php-composer(jeremeamia/superclosure) >= %{jeremeamia_superclosure_min_ver}
%endif
## phpcompatinfo (computed from version 3.5.6)
BuildRequires: php-date
BuildRequires: php-hash
BuildRequires: php-iconv
BuildRequires: php-json
BuildRequires: php-reflection
BuildRequires: php-spl
BuildRequires: php-tokenizer
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
# phpcompatinfo (computed from version 3.5.6)
Requires:      php-reflection
Requires:      php-date
Requires:      php-hash
Requires:      php-json
Requires:      php-spl
Requires:      php-tokenizer
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
Opis Closure is a library that aims to overcome PHP's limitations regarding
closure serialization by providing a wrapper that will make all closures
serializable.

Autoloader: %{phpdir}/%{namespace_vendor}/%{namespace_project}%{?namespace_version}/autoload.php


%prep
%setup -qn %{github_name}-%{github_commit}
cp functions.php src/


%build
: Create autoloader
cat <<'AUTOLOAD' | tee src/autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 */
require_once '%{phpdir}/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('%{namespace_vendor}\\%{namespace_project}\\', __DIR__);

\Fedora\Autoloader\Dependencies::required([
    __DIR__.'/functions.php',
]);
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}/%{namespace_vendor}
cp -rp src %{buildroot}%{phpdir}/%{namespace_vendor}/%{namespace_project}%{?namespace_version}


%check
%if %{with_tests}
: Create tests bootstrap
cat <<'BOOTSTRAP' | tee bootstrap.php
<?php
require '%{buildroot}%{phpdir}/%{namespace_vendor}/%{namespace_project}%{?namespace_version}/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('%{namespace_vendor}\\%{namespace_project}\\Test\\', __DIR__.'/tests');
BOOTSTRAP

: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which %{phpunit_exec})
for PHP_EXEC in "" %{?rhel:php55 php56 php70 php71 php72} php73 php74 php80; do
    if [ -z "$PHP_EXEC" ] || which $PHP_EXEC; then
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
%license NOTICE
%doc *.md
%doc composer.json
%dir %{phpdir}/%{namespace_vendor}
     %{phpdir}/%{namespace_vendor}/%{namespace_project}%{?namespace_version}


%changelog
* Mon Oct 12 2020 Remi Collet <remi@remirepo.net> - 3.6.0-1
- update to 3.6.0
- switch to phpunit9

* Fri Aug 21 2020 Shawn Iwinski <shawn@iwin.ski> - 3.5.6-2
- Update SCL tests per review (RHBZ #1869433)

* Mon Aug 17 2020 Shawn Iwinski <shawn@iwin.ski> - 3.5.6-1
- Initial package

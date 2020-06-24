#
# Fedora spec file for php-phpdocumentor-type-resolver
#
# Copyright (c) 2017 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     phpDocumentor
%global github_name      TypeResolver
%global github_version   0.4.0
%global github_commit    9c977708995954784726e25d0cd1dddf4e65b0f7

%global composer_vendor  phpdocumentor
%global composer_project type-resolver

# "php": "^5.5 || ^7.0"
%global php_min_ver 5.5
# "mockery/mockery": "^0.9.4"
%global mockery_min_ver 0.9.4
%global mockery_max_ver 1.0
# "phpdocumentor/reflection-common": "^1.0"
%global reflection_common_min_ver 1.0
%global reflection_common_max_ver 2.0

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       8%{?github_release}%{?dist}
Summary:       A PSR-5 based resolver of Class names, Types and Structural Element Names

License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}

# GitHub export does not include tests.
# Run php-phpdocumentor-type-resolver-get-source.sh to create full source.
Source0:       %{name}-%{github_version}-%{github_commit}.tar.gz
Source1:       %{name}-get-source.sh

BuildArch:     noarch
# Tests
%if %{with_tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: php-composer(phpunit/phpunit)
BuildRequires: (php-composer(phpdocumentor/reflection-common) >= %{reflection_common_min_ver} with php-composer(phpdocumentor/reflection-common) <  %{reflection_common_max_ver})
BuildRequires: (php-composer(mockery/mockery) >= %{mockery_min_ver} with php-composer(mockery/mockery) <  %{mockery_max_ver})
## phpcompatinfo (computed from version 0.4.0)
BuildRequires: php-reflection
BuildRequires: php-spl
BuildRequires: php-tokenizer
## Autoloader
BuildRequires: php-fedora-autoloader-devel
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
Requires:     (php-composer(phpdocumentor/reflection-common) >= %{reflection_common_min_ver} with php-composer(phpdocumentor/reflection-common) <  %{reflection_common_max_ver})
# phpcompatinfo (computed from version 0.4.0)
Requires:      php-spl
Requires:      php-tokenizer
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
The specification on types in DocBlocks (PSR-5) describes various keywords
and special constructs but also how to statically resolve the partial name
of a Class into a Fully Qualified Class Name (FQCN).

PSR-5 also introduces an additional way to describe deeper elements than
Classes, Interfaces and Traits called the Fully Qualified Structural Element
Name (FQSEN). Using this it is possible to refer to methods, properties and
class constants but also functions and global constants.

This package provides two Resolvers that are capable of:
1. Returning a series of Value Object for given expression while resolving any
  partial class names, and
2. Returning an FQSEN object after resolving any partial Structural Element
  Names into Fully Qualified Structural Element names.

Autoloader: %{phpdir}/phpDocumentor/Reflection/autoload-type-resolver.php


%prep
%setup -qn %{github_name}-%{github_commit}

: Update examples autoload require
sed "s#.*require.*vendor.*/autoload.php.*#require_once '%{phpdir}/phpDocumentor/Reflection/autoload-type-resolver.php';#" \
    -i examples/*


%build
: Create autoloader
%{_bindir}/phpab --template fedora --output src/autoload-type-resolver.php src
cat <<'AUTOLOAD' | tee -a src/autoload-type-resolver.php

\Fedora\Autoloader\Dependencies::required([
    '%{phpdir}/phpDocumentor/Reflection/autoload-common.php',
]);
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}/phpDocumentor/Reflection
cp -rp src/* %{buildroot}%{phpdir}/phpDocumentor/Reflection/


%check
%if %{with_tests}
: Create tests bootstrap
cat <<'BOOTSTRAP' | tee bootstrap.php
<?php
require '%{buildroot}%{phpdir}/phpDocumentor/Reflection/autoload-type-resolver.php';

\Fedora\Autoloader\Autoload::addPsr4('phpDocumentor\\Reflection\\', __DIR__.'/tests/unit');

\Fedora\Autoloader\Dependencies::required([
    '%{phpdir}/Mockery/autoload.php',
]);
BOOTSTRAP

: Adjust listener path
sed 's#vendor/mockery/mockery/library#%{phpdir}#' phpunit.xml.dist > phpunit.xml

: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which phpunit)
for PHP_EXEC in php php56 php70 php71 php72 php73; do
    if [ "php" == "$PHP_EXEC" ] || which $PHP_EXEC; then
        $PHP_EXEC -d auto_prepend_file=$PWD/bootstrap.php \
            $PHPUNIT --verbose --bootstrap bootstrap.php \
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
%doc *.md
%doc composer.json
%doc examples
%{phpdir}/phpDocumentor/Reflection/autoload-type-resolver.php
%{phpdir}/phpDocumentor/Reflection/FqsenResolver.php
%{phpdir}/phpDocumentor/Reflection/Type.php
%{phpdir}/phpDocumentor/Reflection/TypeResolver.php
%{phpdir}/phpDocumentor/Reflection/Types


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Dec  7 2018 Remi Collet <remi@remirepo.net> - 0.4.0-5
- use range dependencies

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 17 2017 Shawn Iwinski <shawn@iwin.ski> - 0.4.0-1
- Update to 0.4.0 (RHBZ #1460503)
- Add "get source" script because upstream attributes removed tests from snapshot

* Sat Mar 11 2017 Shawn Iwinski <shawn@iwin.ski> - 0.2.1-1
- Initial package

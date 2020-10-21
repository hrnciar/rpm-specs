# remirepo/fedora spec file for php-phpdocumentor-type-resolver1
#
# Copyright (c) 2017-2020 Remi Collet, Shawn Iwinski
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     phpDocumentor
%global github_name      TypeResolver
%global github_version   1.4.0
%global github_commit    6a467b8989322d92aa1c8bf2bebcc6e5c2ba55c0

%global composer_vendor  phpdocumentor
%global composer_project type-resolver

%global major            1
# Install in reflection-common tree
%global ns_major         2

# "php": "^7.2 || ^8.0"
%global php_min_ver 7.2
# "phpdocumentor/reflection-common": "^2.0"
%global reflection_common_min_ver 2.0
%global reflection_common_max_ver 3

# Build using "--without tests" to disable tests
%bcond_without tests

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}%{major}
Version:       %{github_version}
Release:       1%{?github_release}%{?dist}
Summary:       A PSR-5 based resolver of Class names, Types and Structural Element Names

Group:         Development/Libraries
License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}

# GitHub export does not include tests.
# Run makesrc.sh to create full source.
Source0:       %{name}-%{github_version}-%{github_commit}.tar.gz
Source1:       makesrc.sh

BuildArch:     noarch
# Tests
%if %{with tests}
## composer.json
BuildRequires:  php(language) >= %{php_min_ver}
%if 0%{?fedora} >= 31 || 0%{?rhel} >= 9
%global phpunit %{_bindir}/phpunit9
BuildRequires:  phpunit9
%else
%global phpunit %{_bindir}/phpunit8
BuildRequires:  phpunit8
%endif
BuildRequires: (php-composer(phpdocumentor/reflection-common) >= %{reflection_common_min_ver} with php-composer(phpdocumentor/reflection-common) <  %{reflection_common_max_ver})
## phpcompatinfo (computed from version 1.0.0)
BuildRequires:  php-reflection
BuildRequires:  php-pcre
BuildRequires:  php-spl
BuildRequires:  php-tokenizer
## Autoloader
BuildRequires:  php-fedora-autoloader-devel
%endif

# composer.json
Requires:       php(language) >= %{php_min_ver}
Requires:      (php-composer(phpdocumentor/reflection-common) >= %{reflection_common_min_ver} with php-composer(phpdocumentor/reflection-common) <  %{reflection_common_max_ver})
# phpcompatinfo (computed from version 1.0.0)
Requires:       php-pcre
Requires:       php-spl
Requires:       php-tokenizer
# Autoloader
Requires:       php-composer(fedora/autoloader)

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

Autoloader: %{phpdir}/phpDocumentor/Reflection%{ns_major}/autoload-type-resolver.php


%prep
%setup -qn %{github_name}-%{github_commit}

: Update examples autoload require
sed "s#.*require.*vendor.*/autoload.php.*#require_once '%{phpdir}/phpDocumentor/Reflection%{ns_major}/autoload-type-resolver.php';#" \
    -i examples/*


%build
: Create autoloader
%{_bindir}/phpab --template fedora --output src/autoload-type-resolver.php src
cat <<'AUTOLOAD' | tee -a src/autoload-type-resolver.php

\Fedora\Autoloader\Dependencies::required([
    '%{phpdir}/phpDocumentor/Reflection%{ns_major}/autoload-common.php',
]);
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}/phpDocumentor/Reflection%{ns_major}
cp -rp src/* %{buildroot}%{phpdir}/phpDocumentor/Reflection%{ns_major}/


%check
%if %{with tests}
: Create tests bootstrap
cat <<'BOOTSTRAP' | tee bootstrap.php
<?php
require '%{buildroot}%{phpdir}/phpDocumentor/Reflection%{ns_major}/autoload-type-resolver.php';

\Fedora\Autoloader\Autoload::addPsr4('phpDocumentor\\Reflection\\', __DIR__.'/tests/unit');
BOOTSTRAP

: Upstream tests
RETURN_CODE=0
for cmdarg in "php %{phpunit}" "php72 %{_bindir}/phpunit8" php73 php74 php80; do
    if which $cmdarg; then
        set $cmdarg
        $1 -d auto_prepend_file=$PWD/bootstrap.php \
            ${2:-%{_bindir}/phpunit9} --verbose --no-coverage --bootstrap bootstrap.php \
            || RETURN_CODE=1
    fi
done
exit $RETURN_CODE
%else
: Tests skipped
%endif


%files
%license LICENSE
%doc *.md
%doc composer.json
%doc examples
%{phpdir}/phpDocumentor/Reflection%{ns_major}/autoload-type-resolver.php
%{phpdir}/phpDocumentor/Reflection%{ns_major}/FqsenResolver.php
%{phpdir}/phpDocumentor/Reflection%{ns_major}/Type*
%{phpdir}/phpDocumentor/Reflection%{ns_major}/PseudoType*


%changelog
* Fri Sep 18 2020 Remi Collet <remi@remirepo.net> - 1.4.0-1
- update to 1.4.0
- switch to phpunit9

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 29 2020 Remi Collet <remi@remirepo.net> - 1.3.0-1
- update to 1.3.0

* Tue Jun 23 2020 Remi Collet <remi@remirepo.net> - 1.2.0-1
- update to 1.2.0

* Tue Mar  3 2020 Remi Collet <remi@remirepo.net> - 1.1.0-1
- update to 1.1.0
- raise dependency on PHP 7.2
- switch to phpunit8

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 13 2019 Remi Collet <remi@remirepo.net> - 1.0.1-1
- update to 1.0.1
- rename to php-phpdocumentor-type-resolver1
- move to /usr/share/php/phpDocumentor/Reflection2
- raise dependency on PHP 7.1
- raise dependency on reflection-common 2.0
- use phpunit7

* Fri Dec  7 2018 Remi Collet <remi@remirepo.net> - 0.4.0-5
- use range dependencies

* Mon Jul 17 2017 Shawn Iwinski <shawn@iwin.ski> - 0.4.0-1
- Update to 0.4.0 (RHBZ #1460503)
- Add "get source" script because upstream attributes removed tests from snapshot

* Sat Mar 11 2017 Shawn Iwinski <shawn@iwin.ski> - 0.2.1-1
- Initial package

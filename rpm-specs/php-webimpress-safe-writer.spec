#
# Fedora spec file for php-webimpress-safe-writer
#
# Copyright (c) 2020 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     webimpress
%global github_name      safe-writer
%global github_version   2.0.0
%global github_commit    d03bea3b98abe1d4c8b24cbebf524361ffaafee4

%global composer_vendor  webimpress
%global composer_project safe-writer

# "php": "^7.2"
%global php_min_ver 7.2

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       1%{?github_release}%{?dist}
Summary:       Tool to write files safely, to avoid race conditions

License:       BSD
URL:           https://github.com/%{github_owner}/%{github_name}

# GitHub export does not include tests
# Run php-webimpress-safe-writer-get-source.sh to create full source
Source0:       %{name}-%{github_version}-%{github_commit}.tar.gz
Source1:       %{name}-get-source.sh

BuildArch:     noarch
# Tests
%if %{with_tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: phpunit8
## phpcompatinfo for version 2.0.0
BuildRequires: php-json
BuildRequires: php-spl
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
# phpcompatinfo for version 2.0.0
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
Write files safely to avoid race conditions when the same file is written
multiple times in a short time period.

Autoloader: %{phpdir}/Webimpress/SafeWriter/autoload.php


%prep
%setup -qn %{github_name}-%{github_commit}

mv LICENSE.md LICENSE


%build
: Create autoloader
cat <<'AUTOLOAD' | tee src/autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 */
require_once '%{phpdir}/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('Webimpress\\SafeWriter\\', __DIR__);
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}/Webimpress
cp -rp src %{buildroot}%{phpdir}/Webimpress/SafeWriter


%check
%if %{with_tests}
: Skip test known to fail in mock environment
sed 's/function testMultipleWriters/function SKIP_testMultipleWriters/' \
    -i test/FileWriterTest.php

: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which phpunit8)
for PHP_EXEC in php php70 php71 php72 php73 php74; do
    if [ "php" == "$PHP_EXEC" ] || which $PHP_EXEC; then
        $PHP_EXEC $PHPUNIT --verbose \
            --bootstrap %{buildroot}%{phpdir}/Webimpress/SafeWriter/autoload.php \
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
%dir %{phpdir}/Webimpress
     %{phpdir}/Webimpress/SafeWriter


%changelog
* Sun Feb 23 2020 Shawn Iwinski <shawn@iwin.ski> - 2.0.0-1
- Initial package

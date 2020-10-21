# remirepo/fedora spec file for php-doctrine-migrations
#
# Copyright (c) 2019-2020 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%global bootstrap    0
%global gh_commit    a3987131febeb0e9acb3c47ab0df0af004588934
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     doctrine
%global gh_project   migrations
# packagist
%global pk_vendor    %{gh_owner}
%global pk_project   %{gh_project}
# Namespace
%global ns_vendor    Doctrine
%global ns_project   Migrations
%if %{bootstrap}
%global with_tests   0%{?_with_tests:1}
%else
%global with_tests   0%{!?_without_tests:1}
%endif

Name:           php-%{pk_vendor}-%{pk_project}
Version:        2.2.1
Release:        3%{?dist}
Summary:        PHP Doctrine Migrations project

License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

# get rid of ocramius/package-versions
Patch0:         %{name}-rpm.patch

BuildArch:      noarch
BuildRequires:  php-fedora-autoloader-devel
%if %{with_tests}
BuildRequires:  php(language) >= 7.1
BuildRequires:  php-reflection
BuildRequires:  php-simplexml
BuildRequires:  php-date
BuildRequires:  php-dom
BuildRequires:  php-json
BuildRequires:  php-libxml
BuildRequires:  php-pcre
BuildRequires:  php-phar
BuildRequires:  php-spl
BuildRequires: (php-composer(doctrine/dbal)          >= 2.9   with php-composer(doctrine/dbal)          < 3)
BuildRequires: (php-composer(symfony/console)        >= 3.4   with php-composer(symfony/console)        < 6)
BuildRequires: (php-composer(symfony/stopwatch)      >= 3.4   with php-composer(symfony/stopwatch)      < 6)
BuildRequires: (php-composer(ocramius/proxy-manager) >= 2.0.2 with php-composer(ocramius/proxy-manager) < 3)
# From composer.json
#    "require-dev": {
#        "ext-pdo_sqlite": "*",
#        "doctrine/coding-standard": "^6.0",
#        "doctrine/orm": "^2.6",
#        "jdorn/sql-formatter": "^1.1",
#        "mikey179/vfsstream": "^1.6",
#        "phpstan/phpstan": "^0.10",
#        "phpstan/phpstan-deprecation-rules": "^0.10",
#        "phpstan/phpstan-phpunit": "^0.10",
#        "phpstan/phpstan-strict-rules": "^0.10",
#        "phpunit/phpunit": "^7.0",
#        "symfony/process": "^3.4||^4.0||^5.0",
#        "symfony/yaml": "^3.4||^4.0||^5.0"
BuildRequires:  php-pdo_sqlite
BuildRequires: (php-composer(doctrine/orm)           >= 2.6   with php-composer(doctrine/orm)           < 3)
BuildRequires: (php-composer(symfony/process)        >= 3.4   with php-composer(symfony/process)        < 6)
BuildRequires: (php-composer(symfony/yaml)           >= 3.4   with php-composer(symfony/yaml)           < 6)
BuildRequires: (php-composer(jdorn/sql-formatter)    >= 1.1   with php-composer(jdorn/sql-formatter)    < 2)
BuildRequires: (php-composer(mikey179/vfsstream)     >= 1.6   with php-composer(mikey179/vfsstream)     < 2)
BuildRequires:  phpunit7
%endif

# From composer.json
#    "require": {
#        "php": "^7.1",
#        "doctrine/dbal": "^2.9",
#        "ocramius/package-versions": "^1.3",
#        "ocramius/proxy-manager": "^2.0.2",
#        "symfony/console": "^3.4||^4.0||^5.0",
#        "symfony/stopwatch": "^3.4||^4.0||^5.0"
#    "suggest": {
#        "jdorn/sql-formatter": "Allows to generate formatted SQL with the diff command.",
#        "symfony/yaml": "Allows the use of yaml for migration configuration files."

Requires:       php(language) >= 7.1
Requires:      (php-composer(doctrine/dbal)          >= 2.9   with php-composer(doctrine/dbal)          < 3)
Requires:      (php-composer(symfony/console)        >= 3.4   with php-composer(symfony/console)        < 6)
Requires:      (php-composer(symfony/stopwatch)      >= 3.4   with php-composer(symfony/stopwatch)      < 6)
Requires:      (php-composer(ocramius/proxy-manager) >= 2.0.2 with php-composer(ocramius/proxy-manager) < 3)
Recommends:    (php-composer(mikey179/vfsStream)     >= 1.6   with php-composer(mikey179/vfsStream)     < 2)
Recommends:    (php-composer(symfony/yaml)           >= 3.3   with php-composer(symfony/yaml)           < 6)
# From phpcompatinfo report for version 1.8.1
Requires:       php-simplexml
Requires:       php-date
Requires:       php-dom
Requires:       php-json
Requires:       php-libxml
Requires:       php-pcre
Requires:       php-spl

# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}


%description
PHP Doctrine Migrations project offer additional functionality on top of the
database abstraction layer (DBAL) for versioning your database schema and
easily deploying changes to it. It is a very easy to use and a powerful tool.

Documentation: https://www.doctrine-project.org/projects/migrations.html

Autoloader: %{_datadir}/php/%{ns_vendor}/%{ns_project}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}

: Cleanup to get rid of ocramius/package-versions
%patch0 -p1 -b .rpm
sed -e 's/@VERSION@/%{version}/' -i \
  lib/%{ns_vendor}/%{ns_project}/Tools/Console/ConsoleRunner.php \
  tests/%{ns_vendor}/%{ns_project}/Tests/Functional/CliTest.php
grep 'new Application' lib/%{ns_vendor}/%{ns_project}/Tools/Console/ConsoleRunner.php
find lib -name \*.rpm -delete -print


%build
: Generate a simple autoloader
%{_bindir}/phpab \
    --output lib/%{ns_vendor}/%{ns_project}/autoload.php \
    --template fedora \
    lib/%{ns_vendor}
cat << 'EOF' | tee -a lib/%{ns_vendor}/%{ns_project}/autoload.php

// Dependencies
\Fedora\Autoloader\Dependencies::required([
    '%{_datadir}/php/%{ns_vendor}/DBAL/autoload.php',
    [
        '%{_datadir}/php/Symfony5/Component/Console/autoload.php',
        '%{_datadir}/php/Symfony4/Component/Console/autoload.php',
        '%{_datadir}/php/Symfony3/Component/Console/autoload.php',
    ],
    [
        '%{_datadir}/php/Symfony5/Component/Stopwatch/autoload.php',
        '%{_datadir}/php/Symfony4/Component/Stopwatch/autoload.php',
        '%{_datadir}/php/Symfony3/Component/Stopwatch/autoload.php',
    ],
    '%{_datadir}/php/ProxyManager/autoload.php',
]);
\Fedora\Autoloader\Dependencies::optional([
    '%{_datadir}/php/jdorn-sql-formatter/autoload.php',
    [
        '%{_datadir}/php/Symfony5/Component/Process/autoload.php',
        '%{_datadir}/php/Symfony4/Component/Process/autoload.php',
        '%{_datadir}/php/Symfony3/Component/Process/autoload.php',
    ],
    [
        '%{_datadir}/php/Symfony5/Component/Yaml/autoload.php',
        '%{_datadir}/php/Symfony4/Component/Yaml/autoload.php',
        '%{_datadir}/php/Symfony3/Component/Yaml/autoload.php',
    ],
]);
EOF


%install
mkdir -p                              %{buildroot}%{_datadir}/php/%{ns_vendor}
cp -pr lib/%{ns_vendor}/%{ns_project} %{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}


%check
%if %{with_tests}
: Generate autoloader
mkdir vendor
%{_bindir}/phpab \
    --output vendor/autoload.php \
    --template fedora \
    tests

cat << 'EOF' | tee -a vendor/autoload.php
\Fedora\Autoloader\Dependencies::required([
    '%{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}/autoload.php',
    '%{_datadir}/php/%{ns_vendor}/ORM/autoload.php',
    '%{_datadir}/php/org/bovigo/vfs/autoload.php',
]);
EOF

# need investigation (migrations directory deleted during test suite?)
chmod -w tests/Doctrine/Migrations/Tests/Functional/_files

# testMigrationLifecycleFromCommandLine fails with some symfony versions (4.2) ok with newer (4.3)
: Run test suite
ret=0
for cmd in php php71 php72 php73 php74; do
  TMP=$(mktemp -d)
  if which $cmd; then
    TMPDIR=$TMP $cmd %{_bindir}/phpunit7 \
        --bootstrap vendor/autoload.php \
        --filter '^((?!(testMigrationLifecycleFromCommandLine)).)*$' \
        --verbose || ret=1
    rm -rf $TMP
  fi
done

# restore
chmod +w tests/Doctrine/Migrations/Tests/Functional/_files

exit $ret
%else
: Test suite disabled
%endif


%files
%license LICENSE
%doc *.md
%doc composer.json
%{_datadir}/php/%{ns_vendor}/%{ns_project}/


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 10 2020 Remi Collet <remi@remirepo.net> - 2.2.1-1
- update to 2.2.1

* Wed Nov 13 2019 Remi Collet <remi@remirepo.net> - 2.2.0-1
- update to 2.2.0
- allow Symfony 5 (not yet available)

* Thu Aug  1 2019 Remi Collet <remi@remirepo.net> - 2.1.1-1
- update to 2.1.1

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun  7 2019 Remi Collet <remi@remirepo.net> - 2.1.0-1
- update to 2.1.0
- raise dependency on doctrine/dbal 2.9

* Fri Apr 26 2019 Remi Collet <remi@remirepo.net> - 2.0.2-1
- update to 2.0.2

* Wed Apr 24 2019 Remi Collet <remi@remirepo.net> - 2.0.1-1
- update to 2.0.1
- drop patch merged upstream

* Thu Mar 28 2019 Remi Collet <remi@remirepo.net> - 2.0.0-2
- add patch for 32-bit from
  https://github.com/doctrine/migrations/pull/803

* Wed Mar 27 2019 Remi Collet <remi@remirepo.net> - 2.0.0-1
- update to 2.0.0
- raise dependency on symfony 3.4
- add dependency on symfony/stopwatch 3.4
- open https://github.com/doctrine/migrations/pull/802 32-bit tests

* Thu Jan  3 2019 Remi Collet <remi@remirepo.net> - 1.8.1-2
- move autoloader in Doctrine/DBAL/Migration
  for compatibility with version 1.5.0

* Thu Jan  3 2019 Remi Collet <remi@remirepo.net> - 1.8.1-1
- initial package, version 1.8.1

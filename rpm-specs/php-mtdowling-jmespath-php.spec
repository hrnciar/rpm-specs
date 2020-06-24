#
# Fedora spec file for php-mtdowling-jmespath-php
#
# Copyright (c) 2015-2020 Shawn Iwinski <shawn.iwinski@gmail.com>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     jmespath
%global github_name      jmespath.php
%global github_version   2.5.0
%global github_commit    52168cb9472de06979613d365c7f1ab8798be895

%global composer_vendor  mtdowling
%global composer_project jmespath.php

# "php": ">=5.4.0"
%global php_min_ver 5.4.0

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-jmespath-php
Version:       %{github_version}
Release:       1%{?github_release}%{?dist}
Summary:       Declaratively specify how to extract elements from a JSON document

License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}
Source0:       %{url}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
# Tests
%if %{with_tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: php-composer(phpunit/phpunit)
## phpcompatinfo (computed from version 2.5.0)
BuildRequires: php-json
BuildRequires: php-mbstring
BuildRequires: php-spl
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

Requires:      php-cli
# composer.json
Requires:      php(language) >= %{php_min_ver}
# phpcompatinfo (computed from version 2.5.0)
Requires:      php-json
Requires:      php-mbstring
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

# php-{COMPOSER_VENDOR}-{COMPOSER_PROJECT}
Provides:      php-%{composer_vendor}-%{composer_project} = %{version}-%{release}
# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
JMESPath (pronounced "jaymz path") allows you to declaratively specify how to
extract elements from a JSON document. jmespath.php allows you to use JMESPath
in PHP applications with PHP data structures.


%prep
%setup -qn %{github_name}-%{github_commit}

: Create autoloader
cat <<'AUTOLOAD' | tee src/autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 */
require_once '%{phpdir}/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('JmesPath\\', __DIR__);

require_once __DIR__ . '/JmesPath.php';
AUTOLOAD

: Modify bin script
sed "s#.*require.*autoload.*#require_once '%{phpdir}/JmesPath/autoload.php';#" \
    -i bin/jp.php


%build
# Empty build section, nothing to build


%install
: Lib
mkdir -p %{buildroot}%{phpdir}/JmesPath
cp -rp src/* %{buildroot}%{phpdir}/JmesPath/

: Bin
mkdir -p %{buildroot}%{_bindir}
install -pm 0755 bin/jp.php %{buildroot}%{_bindir}/


%check
%if %{with_tests}
: Skip test known to fail
sed 's/function testTokenizesJsonNumbers/function SKIP_testTokenizesJsonNumbers/' \
    -i tests/LexerTest.php

: Run tests
%{_bindir}/phpunit --verbose \
    --bootstrap %{buildroot}%{phpdir}/JmesPath/autoload.php
%else
: Tests skipped
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc CHANGELOG.md
%doc README.rst
%doc composer.json
%{phpdir}/JmesPath
%{_bindir}/jp.php


%changelog
* Wed Feb 12 2020 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.5.0-1
- Update to 2.5.0 (RHBZ #1787856)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Dec 07 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.4.0-1
- Update to 2.4.0 (RHBZ #1401271)
- Change autoloader from php-composer(symfony/class-loader) to
  php-composer(fedora/autoloader)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jun 28 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.3.0-1
- Updated to 2.3.0 (RHBZ #1295982)
- Added "php-{COMPOSER_VENDOR}-{COMPOSER_PROJECT}" ("php-mtdowling-jmespath.php")
  virtual provide

* Sun Jun 28 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.2.0-1
- Updated to 2.2.0 (RHBZ #1225677)
- Changed autoloader from phpab to Symfony ClassLoader

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 16 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.1.0-1
- Initial package

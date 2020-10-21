#
# Fedora spec file for php-stecman-symfony-console-completion
#
# Copyright (c) 2017-2019 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     stecman
%global github_name      symfony-console-completion
%global github_version   0.10.1
%global github_commit    7bfa9b93e216896419f2f8de659935d7e04fecd8

%global composer_vendor  stecman
%global composer_project symfony-console-completion

# "php": ">=5.3.2"
%global php_min_ver 5.3.2
# "symfony/console": "~2.3 || ~3.0 || ~4.0"
#     NOTE: Min version not 2.3 because autoloader required
%global symfony_min_ver %{?el6:2.3.31}%{!?el6:2.7.1}
%global symfony_max_ver 5.0

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       5%{?github_release}%{?dist}
Summary:       Automatic BASH completion for Symfony Console based applications

License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}
Source0:       %{url}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
# Tests
%if %{with_tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: php-composer(phpunit/phpunit)
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
BuildRequires: (php-composer(symfony/console) >= %{symfony_min_ver} with php-composer(symfony/console) < %{symfony_max_ver})
%else
BuildRequires: php-composer(symfony/console) <  %{symfony_max_ver}
BuildRequires: php-composer(symfony/console) >= %{symfony_min_ver}
%endif
## phpcompatinfo for version 0.10.1
BuildRequires: php-pcre
BuildRequires: php-reflection
BuildRequires: php-spl
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
Requires:      (php-composer(symfony/console) >= %{symfony_min_ver} with php-composer(symfony/console) < %{symfony_max_ver})
%else
Requires:      php-composer(symfony/console) <  %{symfony_max_ver}
Requires:      php-composer(symfony/console) >= %{symfony_min_ver}
%endif
# phpcompatinfo for version 0.10.1
Requires:      php-pcre
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
This package provides automatic (tab) completion in BASH and ZSH for Symfony
Console Component based applications. With zero configuration, this package
allows completion of available command names and the options they provide.
User code can define custom completion behaviour for argument and option values.

Autoloader:
%{phpdir}/Stecman/Component/Symfony/Console/BashCompletion/autoload.php


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

\Fedora\Autoloader\Autoload::addPsr4(
    'Stecman\\Component\\Symfony\\Console\\BashCompletion\\',
    __DIR__
);

\Fedora\Autoloader\Dependencies::required(array(
    array(
        '%{phpdir}/Symfony4/Component/Console/autoload.php',
        '%{phpdir}/Symfony3/Component/Console/autoload.php',
        '%{phpdir}/Symfony/Component/Console/autoload.php',
    ),
));
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}/Stecman/Component/Symfony/Console
cp -rp src %{buildroot}%{phpdir}/Stecman/Component/Symfony/Console/BashCompletion


%check
%if %{with_tests}
: Create tests bootstrap
cat <<'BOOTSTRAP' | tee -a bootstrap.php
<?php
require_once '%{buildroot}%{phpdir}/Stecman/Component/Symfony/Console/BashCompletion/autoload.php';
if (!class_exists('PHPUnit\\Framework\\TestCase')) {
    class_alias('PHPUnit_Framework_TestCase', 'PHPUnit\\Framework\\TestCase');
}
BOOTSTRAP

%if 0%{?el6}
: Skip tests requiring PHPUnit >= 4.4
sed \
    -e 's/function testCompleteDoubleDash/function SKIP_testCompleteDoubleDash/' \
    -e 's/function testCompleteOptionFull/function SKIP_testCompleteOptionFull/' \
    -e 's/function testCompleteOptionShortcutFirst/function SKIP_testCompleteOptionShortcutFirst/' \
    -i tests/Stecman/Component/Symfony/Console/BashCompletion/CompletionHandlerTest.php
%endif

: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which phpunit)
for PHP_EXEC in "" %{?rhel:php54 php55} php56 php70 php71 php72 php73 php74; do
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
%license LICENCE
%doc *.md
%doc composer.json
%dir %{phpdir}/Stecman
%dir %{phpdir}/Stecman/Component
%dir %{phpdir}/Stecman/Component/Symfony
%dir %{phpdir}/Stecman/Component/Symfony/Console
     %{phpdir}/Stecman/Component/Symfony/Console/BashCompletion


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 14 2019 Shawn Iwinski <shawn@iwin.ski> - 0.10.1-2
- Fix EPEL6 build

* Tue May 14 2019 Shawn Iwinski <shawn@iwin.ski> - 0.10.1-1
- Update to 0.10.1 (RHBZ #1562562)
- Add range version dependencies for Fedora >= 27 || RHEL >= 8

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Nov 03 2017 Shawn Iwinski <shawn@iwin.ski> - 0.7.0-2
- Remove rename of license file

* Thu Oct 26 2017 Shawn Iwinski <shawn@iwin.ski> - 0.7.0-1
- Initial package

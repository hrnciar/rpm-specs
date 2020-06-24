#
# Fedora spec file for psysh
#
# Copyright (c) 2016-2019 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     bobthecow
%global github_name      psysh
%global github_version   0.9.11
%global github_commit    75d9ac1c16db676de27ab554a4152b594be4748e

%global composer_vendor  psy
%global composer_project psysh

# "php": ">=5.4.0"
%global php_min_ver 5.4.0
# "dnoegel/php-xdg-base-dir": "0.1"
%global php_xdg_base_dir_min_ver 0.1
%global php_xdg_base_dir_max_ver 0.2
# "jakub-onderka/php-console-highlighter": "0.3.*|0.4.*"
%global php_console_highlighter_min_ver 0.3.0
%global php_console_highlighter_max_ver 0.5.0
# "nikic/php-parser": "~1.3|~2.0|~3.0|~4.0"
#     NOTE: Min version not 1.2.1 to force 2.x so 1.x is not
#           a dependency so it could possibly be retired
%global php_parser_min_ver 2.0
%global php_parser_max_ver 5.0
# "symfony/console": "~2.3.10|^2.4.2|~3.0|~4.0|~5.0"
# "symfony/var-dumper": "~2.7|~3.0|~4.0|~5.0"
#     NOTE: Min version not 2.7.0 because autoloader required
%global symfony_min_ver 2.7.1
%global symfony_max_ver 6.0

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          psysh
Version:       %{github_version}
Release:       2%{?github_release}%{?dist}
Summary:       A runtime developer console, interactive debugger and REPL for PHP

License:       MIT
URL:           http://psysh.org
Source0:       https://github.com/%{github_owner}/%{github_name}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

# Update bin script to use generated autoloader
Patch0:        %{name}-bin-autoload.patch

BuildArch:     noarch
# Tests
%if %{with_tests}
BuildRequires: php-cli
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: php-composer(phpunit/phpunit)
BuildRequires: php-composer(dnoegel/php-xdg-base-dir) <  %{php_xdg_base_dir_max_ver}
BuildRequires: php-composer(dnoegel/php-xdg-base-dir) >= %{php_xdg_base_dir_min_ver}
BuildRequires: php-composer(jakub-onderka/php-console-highlighter) <  %{php_console_highlighter_max_ver}
BuildRequires: php-composer(jakub-onderka/php-console-highlighter) >= %{php_console_highlighter_min_ver}
BuildRequires: php-composer(nikic/php-parser) <  %{php_parser_max_ver}
BuildRequires: php-composer(nikic/php-parser) >= %{php_parser_min_ver}
BuildRequires: php-composer(symfony/console) <  %{symfony_max_ver}
BuildRequires: php-composer(symfony/console) >= %{symfony_min_ver}
BuildRequires: php-composer(symfony/var-dumper) <  %{symfony_max_ver}
BuildRequires: php-composer(symfony/var-dumper) >= %{symfony_min_ver}
BuildRequires: php-json
BuildRequires: php-tokenizer
## composer.json: optional
BuildRequires: php-pcntl
BuildRequires: php-posix
BuildRequires: php-readline
BuildRequires: php-sqlite3
## phpcompatinfo (computed from version 0.9.11)
BuildRequires: php-date
BuildRequires: php-dom
BuildRequires: php-pcre
BuildRequires: php-pdo
BuildRequires: php-reflection
BuildRequires: php-spl
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

Requires:      php-cli
# composer.json
Requires:      php(language) >= %{php_min_ver}
Requires:      php-composer(dnoegel/php-xdg-base-dir) <  %{php_xdg_base_dir_max_ver}
Requires:      php-composer(dnoegel/php-xdg-base-dir) >= %{php_xdg_base_dir_min_ver}
Requires:      php-composer(jakub-onderka/php-console-highlighter) <  %{php_console_highlighter_max_ver}
Requires:      php-composer(jakub-onderka/php-console-highlighter) >= %{php_console_highlighter_min_ver}
Requires:      php-composer(nikic/php-parser) <  %{php_parser_max_ver}
Requires:      php-composer(nikic/php-parser) >= %{php_parser_min_ver}
Requires:      php-composer(symfony/console) <  %{symfony_max_ver}
Requires:      php-composer(symfony/console) >= %{symfony_min_ver}
Requires:      php-composer(symfony/var-dumper) <  %{symfony_max_ver}
Requires:      php-composer(symfony/var-dumper) >= %{symfony_min_ver}
Requires:      php-json
Requires:      php-tokenizer
# composer.json: optional
Requires:      php-pcntl
Requires:      php-posix
Requires:      php-readline
Requires:      php-sqlite3
# phpcompatinfo (computed from version 0.9.11)
Requires:      php-date
Requires:      php-pcre
Requires:      php-pdo
Requires:      php-reflection
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Standard "php-{COMPOSER_VENDOR}-{COMPOSER_PROJECT}" naming
Provides:      php-%{composer_vendor}-%{composer_project} = %{version}-%{release}
# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
%{summary}.

Autoloader: %{phpdir}/Psy/autoload.php


%prep
%setup -qn %{github_name}-%{github_commit}

: Update bin script to use generated autoloader
%patch0 -p1
sed 's#__PHPDIR__#%{phpdir}#' -i bin/psysh


%build
: Create autoloader
cat <<'AUTOLOAD' | tee src/autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 */
require_once '%{phpdir}/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('Psy\\', __DIR__);
require_once __DIR__.'/functions.php';

\Fedora\Autoloader\Dependencies::required([
    '%{phpdir}/JakubOnderka/PhpConsoleHighlighter/autoload.php',
    '%{phpdir}/XdgBaseDir/autoload.php',
    [
        '%{phpdir}/Symfony5/Component/Console/autoload.php',
        '%{phpdir}/Symfony4/Component/Console/autoload.php',
        '%{phpdir}/Symfony3/Component/Console/autoload.php',
        '%{phpdir}/Symfony/Component/Console/autoload.php',
    ],
    [
        '%{phpdir}/Symfony5/Component/VarDumper/autoload.php',
        '%{phpdir}/Symfony4/Component/VarDumper/autoload.php',
        '%{phpdir}/Symfony3/Component/VarDumper/autoload.php',
        '%{phpdir}/Symfony/Component/VarDumper/autoload.php',
    ],
    [
        '%{phpdir}/PhpParser4/autoload.php',
        '%{phpdir}/PhpParser3/autoload.php',
        '%{phpdir}/PhpParser2/autoload.php',
    ],
]);
AUTOLOAD


%install
: Library
mkdir -p %{buildroot}%{phpdir}
cp -rp src %{buildroot}%{phpdir}/Psy

: Bin
mkdir -p %{buildroot}%{_bindir}
install -pm 0755 bin/psysh %{buildroot}%{_bindir}/


%check
%if %{with_tests}
: Create tests bootstrap
cat <<'BOOTSTRAP' | tee bootstrap.php
<?php
require '%{buildroot}%{phpdir}/Psy/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('Psy\\Test\\', __DIR__.'/test');
BOOTSTRAP

: Skip tests known to fail
sed 's/function testFilesAndDirectories/function SKIP_testFilesAndDirectories/' \
    -i test/ConfigurationTest.php

: Skip tests known to fail in a mock env
sed 's/function testFormat/function SKIP_testFormat/' \
    -i test/Formatter/CodeFormatterTest.php
sed 's/function testWriteReturnValue/function SKIP_testWriteReturnValue/' \
    -i test/ShellTest.php

: Drop unneeded test as readline is always there
rm test/Readline/HoaConsoleTest.php

: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which phpunit)
for PHP_EXEC in "" %{?rhel:php55} php56 php70 php71 php72 php73 php74; do
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
%doc *.md
%doc composer.json
%{phpdir}/Psy
%{_bindir}/psysh


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Dec 01 2019 Shawn Iwinski <shawn@iwin.ski> - 0.9.11-1
- Update to 0.9.11 (RHBZ #1529814)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Dec 13 2017 Shawn Iwinski <shawn@iwin.ski> - 0.8.16-1
- Update to 0.8.16 (RHBZ #1468827)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 25 2017 Shawn Iwinski <shawn@iwin.ski> - 0.8.8-1
- Update to 0.8.8 (RHBZ #1464772)

* Fri Jun 23 2017 Shawn Iwinski <shawn@iwin.ski> - 0.8.7-1
- Update to 0.8.7 (RHBZ #1450707)
- Fix autoloader for PHP < 5.4

* Sat Apr 08 2017 Shawn Iwinski <shawn@iwin.ski> - 0.8.3-1
- Update to 0.8.3 (RHBZ #1433813)
- Allow Symfony 3

* Sat Mar 04 2017 2017 Shawn Iwinski <shawn@iwin.ski> - 0.8.2-1
- Update to 0.8.2 (RHBZ #1413429)
- Test with SCLs if available

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Dec 11 2016 Shawn Iwinski <shawn@iwin.ski> - 0.8.0-1
- Update to 0.8.0 (RHBZ #1403040)
- Switch autoloader from php-composer(symfony/class-loader) to
  php-composer(fedora/autoloader)

* Wed Jul 20 2016 Shawn Iwinski <shawn@iwin.ski> - 0.7.2-2
- Add explicit php-cli dependency (bin script uses "#!/usr/bin/env php")

* Fri Jul 15 2016 Shawn Iwinski <shawn@iwin.ski> - 0.7.2-1
- Initial package

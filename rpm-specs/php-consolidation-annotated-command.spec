#
# Fedora spec file for php-consolidation-annotated-command
#
# Copyright (c) 2016-2020 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     consolidation
%global github_name      annotated-command
%global github_version   4.1.0
%global github_commit    33e472d3cceb0f22a527d13ccfa3f76c4d21c178

%global composer_vendor  consolidation
%global composer_project annotated-command

# "php": ">=7.1.3"
%global php_min_ver 7.1.3
# "consolidation/output-formatters": "^4.1"
%global consolidation_output_formatters_min_ver 4.1
%global consolidation_output_formatters_max_ver 5.0
# "psr/log": "^1|^2"
#     NOTE: Min version not 1.0 because autoloader required
#     NOTE: Max version not 3.0 because there is no version 2 at this time
%global psr_log_min_ver 1.0.1
%global psr_log_max_ver 2.0
# "symfony/console": "^4|^5"
# "symfony/event-dispatcher": "^4|^5"
# "symfony/finder": "^4|^5"
%global symfony_min_ver 4.0
%global symfony_max_ver 6.0

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

# Range dependencies supported?
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
%global with_range_dependencies 1
%else
%global with_range_dependencies 0
%endif

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       1%{?github_release}%{?dist}
Summary:       Initialize Symfony Console commands from annotated command class methods

License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}

# GitHub export does not include tests
# Run php-consolidation-annotated-command-get-source.sh to create full source
Source0:       %{name}-%{github_version}-%{github_commit}.tar.gz
Source1:       %{name}-get-source.sh

BuildArch:     noarch
# Tests
%if %{with_tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: phpunit6
%if %{with_range_dependencies}
BuildRequires: (php-composer(consolidation/output-formatters) >= %{consolidation_output_formatters_min_ver} with php-composer(consolidation/output-formatters) < %{consolidation_output_formatters_max_ver})
BuildRequires: (php-composer(psr/log) >= %{psr_log_min_ver} with php-composer(psr/log) < %{psr_log_max_ver})
BuildRequires: (php-composer(symfony/console) >= %{symfony_min_ver} with php-composer(symfony/console) < %{symfony_max_ver})
BuildRequires: (php-composer(symfony/event-dispatcher) >= %{symfony_min_ver} with php-composer(symfony/event-dispatcher) < %{symfony_max_ver})
BuildRequires: (php-composer(symfony/finder) >= %{symfony_min_ver} with php-composer(symfony/finder) < %{symfony_max_ver})
%else
BuildRequires: php-composer(consolidation/output-formatters) <  %{consolidation_output_formatters_max_ver}
BuildRequires: php-composer(consolidation/output-formatters) >= %{consolidation_output_formatters_min_ver}
BuildRequires: php-composer(phpunit/phpunit)
BuildRequires: php-composer(psr/log) <  %{psr_log_max_ver}
BuildRequires: php-composer(psr/log) >= %{psr_log_min_ver}
BuildRequires: php-composer(symfony/console) <  %{symfony_max_ver}
BuildRequires: php-composer(symfony/console) >= %{symfony_min_ver}
BuildRequires: php-composer(symfony/event-dispatcher) <  %{symfony_max_ver}
BuildRequires: php-composer(symfony/event-dispatcher) >= %{symfony_min_ver}
BuildRequires: php-composer(symfony/finder) <  %{symfony_max_ver}
BuildRequires: php-composer(symfony/finder) >= %{symfony_min_ver}
%endif
## phpcompatinfo (computed from version 4.1.0)
BuildRequires: php-dom
BuildRequires: php-pcre
BuildRequires: php-reflection
BuildRequires: php-spl
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
%if %{with_range_dependencies}
Requires:      (php-composer(consolidation/output-formatters) >= %{consolidation_output_formatters_min_ver} with php-composer(consolidation/output-formatters) < %{consolidation_output_formatters_max_ver})
Requires:      (php-composer(psr/log) >= %{psr_log_min_ver} with php-composer(psr/log) < %{psr_log_max_ver})
Requires:      (php-composer(symfony/console) >= %{symfony_min_ver} with php-composer(symfony/console) < %{symfony_max_ver})
Requires:      (php-composer(symfony/event-dispatcher) >= %{symfony_min_ver} with php-composer(symfony/event-dispatcher) < %{symfony_max_ver})
Requires:      (php-composer(symfony/finder) >= %{symfony_min_ver} with php-composer(symfony/finder) < %{symfony_max_ver})
%else
Requires:      php-composer(consolidation/output-formatters) <  %{consolidation_output_formatters_max_ver}
Requires:      php-composer(consolidation/output-formatters) >= %{consolidation_output_formatters_min_ver}
Requires:      php-composer(psr/log) <  %{psr_log_max_ver}
Requires:      php-composer(psr/log) >= %{psr_log_min_ver}
Requires:      php-composer(symfony/console) <  %{symfony_max_ver}
Requires:      php-composer(symfony/console) >= %{symfony_min_ver}
Requires:      php-composer(symfony/event-dispatcher) <  %{symfony_max_ver}
Requires:      php-composer(symfony/event-dispatcher) >= %{symfony_min_ver}
Requires:      php-composer(symfony/finder) <  %{symfony_max_ver}
Requires:      php-composer(symfony/finder) >= %{symfony_min_ver}
%endif
# phpcompatinfo (computed from version 4.1.0)
Requires:      php-dom
Requires:      php-pcre
Requires:      php-reflection
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
%{summary}.

Autoloader: %{phpdir}/Consolidation/AnnotatedCommand/autoload.php


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

\Fedora\Autoloader\Autoload::addPsr4('Consolidation\\AnnotatedCommand\\', __DIR__);

\Fedora\Autoloader\Dependencies::required([
    '%{phpdir}/Consolidation/OutputFormatters/autoload.php',
    '%{phpdir}/Psr/Log/autoload.php',
    [
        '%{phpdir}/Symfony5/Component/Console/autoload.php',
        '%{phpdir}/Symfony4/Component/Console/autoload.php',
    ],
    [
        '%{phpdir}/Symfony5/Component/EventDispatcher/autoload.php',
        '%{phpdir}/Symfony4/Component/EventDispatcher/autoload.php',
    ],
    [
        '%{phpdir}/Symfony5/Component/Finder/autoload.php',
        '%{phpdir}/Symfony4/Component/Finder/autoload.php',
    ]
]);
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}/Consolidation
cp -rp src %{buildroot}%{phpdir}/Consolidation/AnnotatedCommand


%check
%if %{with_tests}
: Create tests bootstrap
cat <<'BOOTSTRAP' | tee bootstrap.php
<?php
require_once '%{buildroot}%{phpdir}/Consolidation/AnnotatedCommand/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('Consolidation\\TestUtils\\', __DIR__.'/tests/src');
BOOTSTRAP

: Skip test known to fail
sed 's/function testInteractAndValidate/function SKIP_testInteractAndValidate/' \
    -i tests/AnnotatedCommandFactoryTest.php

: Update tests if symfony/var-dumper is installed
if \
    [ $(php -r 'require_once __DIR__."/bootstrap.php"; echo class_exists("Symfony\\Component\\VarDumper\\VarDumper") ? 1 : 0;') -eq 1 ]
then
    grep -r --files-with-matches --null ',var_export' tests | xargs -0 sed -i 's/,var_export/,var_dump,var_export/g'
fi

: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which phpunit6)
for PHP_EXEC in "" php72 php73 php74; do
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
%dir %{phpdir}/Consolidation
     %{phpdir}/Consolidation/AnnotatedCommand


%changelog
* Mon Feb 24 2020 Shawn Iwinski <shawn@iwin.ski> - 4.1.0-1
- Update to 4.1.0
- Use PHPUnit 6

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 01 2019 Shawn Iwinski <shawn@iwin.ski> - 2.12.0-1
- Update to 2.12.0 (RHBZ #1582689)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 30 2018 Shawn Iwinski <shawn@iwin.ski> - 2.8.3-1
- Update to 2.8.3 (RHBZ #1492447)
- Add range version dependencies for Fedora >= 27 || RHEL >= 8

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 30 2017 Shawn Iwinski <shawn@iwin.ski> - 2.4.13-1
- Update to 2.4.13 (RHBZ #1485331)

* Sat Aug 05 2017 Shawn Iwinski <shawn@iwin.ski> - 2.4.11-1
- Update to 2.4.11 (RHBZ #1473682)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Apr 08 2017 Shawn Iwinski <shawn@iwin.ski> - 2.4.8-1
- Update to 2.4.8 (RHBZ #1433641)
- Allow Symfony 3
- Prepare for php-phpdocumentor-reflection-docblock =>
  php-phpdocumentor-reflection-docblock2 dependency rename

* Tue Feb 28 2017 Shawn Iwinski <shawn@iwin.ski> - 2.4.4-1
- Update to 2.4.4 (RHBZ #1415385)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jan 15 2017 Shawn Iwinski <shawn@iwin.ski> - 2.2.2-1
- Update to 2.2.2 (RHBZ #1395001)
- Use php-composer(fedora/autoloader)
- Run upstream tests with SCLs if they are available

* Tue Nov 01 2016 Shawn Iwinski <shawn@iwin.ski> - 2.0.1-2
- Skip test known to fail

* Tue Nov 01 2016 Shawn Iwinski <shawn@iwin.ski> - 2.0.1-1
- Updated to 2.0.1 (RHBZ #1370772)

* Mon Aug 08 2016 Shawn Iwinski <shawn@iwin.ski> - 1.2.1-1
- Updated to 1.2.1 (RHBZ #1359450)

* Tue Jul 19 2016 Shawn Iwinski <shawn@iwin.ski> - 1.0.1-1
- Initial package

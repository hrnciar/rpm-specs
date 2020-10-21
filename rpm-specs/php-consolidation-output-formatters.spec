#
# Fedora spec file for php-consolidation-output-formatters
#
# Copyright (c) 2016-2020 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     consolidation
%global github_name      output-formatters
%global github_version   4.1.1
%global github_commit    9deeddd6a916d0a756b216a8b40ce1016e17c0b9

%global composer_vendor  consolidation
%global composer_project output-formatters

# "php": ">=7.1.3"
%global php_min_ver 7.1.3
# "dflydev/dot-access-data": "^1.1.0"
%global dflydev_dot_access_data_min_ver 1.1.0
%global dflydev_dot_access_data_max_ver 2.0
# "symfony/console": "^4|^5"
# "symfony/finder": "^4|^5"
# "symfony/var-dumper": "^4"
# "symfony/yaml": "^4"
%global symfony_min_ver 4.0
%global symfony_max_ver 6.0

# "phpunit/phpunit": "^6"
%global phpunit_require phpunit6
%global phpunit_min_ver 6
%global phpunit_exec    phpunit6

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
Summary:       Format text by applying transformations provided by plug-in formatters

License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}

# GitHub export does not include tests
# Run php-consolidation-output-formatters-get-source.sh to create full source
Source0:       %{name}-%{github_version}-%{github_commit}.tar.gz
Source1:       %{name}-get-source.sh

BuildArch:     noarch
# Tests
%if %{with_tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: %{phpunit_require} >= %{phpunit_min_ver}
%if %{with_range_dependencies}
BuildRequires: (php-composer(dflydev/dot-access-data) >= %{dflydev_dot_access_data_min_ver} with php-composer(dflydev/dot-access-data) < %{dflydev_dot_access_data_max_ver})
BuildRequires: (php-composer(symfony/console) >= %{symfony_min_ver} with php-composer(symfony/console) < %{symfony_max_ver})
BuildRequires: (php-composer(symfony/finder) >= %{symfony_min_ver} with php-composer(symfony/finder) < %{symfony_max_ver})
BuildRequires: (php-composer(symfony/var-dumper) >= %{symfony_min_ver} with php-composer(symfony/var-dumper) < %{symfony_max_ver})
BuildRequires: (php-composer(symfony/yaml) >= %{symfony_min_ver} with php-composer(symfony/yaml) < %{symfony_max_ver})
%else
BuildRequires: php-composer(dflydev/dot-access-data) <  %{dflydev_dot_access_data_max_ver}
BuildRequires: php-composer(dflydev/dot-access-data) >= %{dflydev_dot_access_data_min_ver}
BuildRequires: php-composer(symfony/console) <  %{symfony_max_ver}
BuildRequires: php-composer(symfony/console) >= %{symfony_min_ver}
BuildRequires: php-composer(symfony/finder) <  %{symfony_max_ver}
BuildRequires: php-composer(symfony/finder) >= %{symfony_min_ver}
BuildRequires: php-composer(symfony/var-dumper) <  %{symfony_max_ver}
BuildRequires: php-composer(symfony/var-dumper) >= %{symfony_min_ver}
BuildRequires: php-composer(symfony/yaml) <  %{symfony_max_ver}
BuildRequires: php-composer(symfony/yaml) >= %{symfony_min_ver}
%endif
## phpcompatinfo (computed from version 4.1.1)
BuildRequires: php-dom
BuildRequires: php-json
BuildRequires: php-pcre
BuildRequires: php-reflection
BuildRequires: php-spl
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
%if %{with_range_dependencies}
Requires:      (php-composer(dflydev/dot-access-data) >= %{dflydev_dot_access_data_min_ver} with php-composer(dflydev/dot-access-data) < %{dflydev_dot_access_data_max_ver})
Requires:      (php-composer(symfony/console) >= %{symfony_min_ver} with php-composer(symfony/console) < %{symfony_max_ver})
Requires:      (php-composer(symfony/finder) >= %{symfony_min_ver} with php-composer(symfony/finder) < %{symfony_max_ver})
%else
Requires:      php-composer(dflydev/dot-access-data) <  %{dflydev_dot_access_data_max_ver}
Requires:      php-composer(dflydev/dot-access-data) >= %{dflydev_dot_access_data_min_ver}
Requires:      php-composer(symfony/console) <  %{symfony_max_ver}
Requires:      php-composer(symfony/console) >= %{symfony_min_ver}
Requires:      php-composer(symfony/finder) <  %{symfony_max_ver}
Requires:      php-composer(symfony/finder) >= %{symfony_min_ver}
%endif
# phpcompatinfo (computed from version 4.1.1)
Requires:      php-dom
Requires:      php-json
Requires:      php-pcre
Requires:      php-reflection
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

%if %{with_range_dependencies}
# Weak dependencies
Suggests:      (php-composer(symfony/var-dumper) >= %{symfony_min_ver} with php-composer(symfony/var-dumper) < %{symfony_max_ver})
%endif

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
%{summary}.

Autoloader: %{phpdir}/Consolidation/OutputFormatters/autoload.php


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

\Fedora\Autoloader\Autoload::addPsr4('Consolidation\\OutputFormatters\\', __DIR__);

\Fedora\Autoloader\Dependencies::required([
    '%{phpdir}/Dflydev/DotAccessData/autoload.php',
    [
        '%{phpdir}/Symfony5/Component/Console/autoload.php',
        '%{phpdir}/Symfony4/Component/Console/autoload.php',
    ],
    [
        '%{phpdir}/Symfony5/Component/Finder/autoload.php',
        '%{phpdir}/Symfony4/Component/Finder/autoload.php',
    ],
]);

\Fedora\Autoloader\Dependencies::optional([
    [
        '%{phpdir}/Symfony5/Component/VarDumper/autoload.php',
        '%{phpdir}/Symfony4/Component/VarDumper/autoload.php',
    ],
]);
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}/Consolidation
cp -rp src %{buildroot}%{phpdir}/Consolidation/OutputFormatters


%check
%if %{with_tests}
: Create tests bootstrap
cat <<'BOOTSTRAP' | tee bootstrap.php
<?php
require_once '%{buildroot}%{phpdir}/Consolidation/OutputFormatters/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('Consolidation\\TestUtils\\', __DIR__.'/tests/src');

\Fedora\Autoloader\Dependencies::required([
    [
        '%{phpdir}/Symfony5/Component/Yaml/autoload.php',
        '%{phpdir}/Symfony4/Component/Yaml/autoload.php',
    ],
]);
BOOTSTRAP

: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which %{phpunit_exec})
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
     %{phpdir}/Consolidation/OutputFormatters


%changelog
* Mon Sep 07 2020 Shawn Iwinski <shawn@iwin.ski> - 4.1.1-1
- Update to 4.1.1 (RHBZ #1851299)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 24 2020 Shawn Iwinski <shawn@iwin.ski> - 4.1.0-1
- Update to 4.1.0
- Use PHPUnit 6

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 01 2019 Shawn Iwinski <shawn@iwin.ski> - 3.5.0-2
- Fix sources

* Sat Jun 01 2019 Shawn Iwinski <shawn@iwin.ski> - 3.5.0-1
- Update to 3.5.0 (RHBZ #1582691)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 30 2018 Shawn Iwinski <shawn@iwin.ski> - 3.2.0-1
- Update to 3.2.0 (RHBZ #1505200)

* Fri Mar 30 2018 Shawn Iwinski <shawn@iwin.ski> - 3.1.13-2
- Update range dependencies' conditional to include RHEL8+

* Wed Feb 21 2018 Shawn Iwinski <shawn@iwin.ski> - 3.1.13-1
- Update to 3.1.13 (RHBZ #1505200)
- Add range version dependencies for Fedora >= 27

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 30 2017 Shawn Iwinski <shawn@iwin.ski> - 3.1.11-1
- Update to 3.1.11 (RHBZ #1482728)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jul 08 2017 Shawn Iwinski <shawn@iwin.ski> - 3.1.10-1
- Update to 3.1.10 (RHBZ #1449852)

* Sat Apr 08 2017 Shawn Iwinski <shawn@iwin.ski> - 3.1.8-1
- Update to 3.1.8 (RHBZ #1428197)
- Allow Symfony 3

* Tue Feb 28 2017 Shawn Iwinski <shawn@iwin.ski> - 3.1.7-1
- Update to 3.1.7 (RHBZ #1415386)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 16 2017 Remi Collet <remi@fedoraproject.org> - 3.1.6-2
- fix autoloader dependency

* Sun Jan 15 2017 Shawn Iwinski <shawn@iwin.ski> - 3.1.6-1
- Update to 3.1.6 (RHBZ #1392720)
- Use php-composer(fedora/autoloader)
- Run upstream tests with SCLs if they are available

* Tue Nov 01 2016 Shawn Iwinski <shawn@iwin.ski> - 2.0.1-1
- Update to 2.0.1 (RHBZ #1376274)

* Tue Jul 19 2016 Shawn Iwinski <shawn@iwin.ski> - 1.0.0-1
- Initial package

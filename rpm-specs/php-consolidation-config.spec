#
# Fedora spec file for php-consolidation-config
#
# Copyright (c) 2017-2020 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     consolidation
%global github_name      config
%global github_version   1.2.1
%global github_commit    cac1279bae7efb5c7fb2ca4c3ba4b8eb741a96c1

%global composer_vendor  consolidation
%global composer_project config

%if 0%{?fedora} >= 32 || 0%{?rhel} >= 8
%global with_symfony2 0
%else
%global with_symfony2 1
%endif

# "php": ">=5.4.0"
%global php_min_ver 5.4.0
# "dflydev/dot-access-data": "^1.1.0"
%global dflydev_dot_access_data_min_ver 1.1.0
%global dflydev_dot_access_data_max_ver 2.0
# "grasmash/expander": "^1"
%global grasmash_expander_min_ver 1.0
%global grasmash_expander_max_ver 2.0
# "symfony/console": "^2.5|^3|^4"
# "symfony/yaml": "^2.8.11|^3|^4"
%if %{with_symfony2}
%global symfony_min_ver 2.8.11
%else
%global symfony_min_ver 3.0
%endif
%global symfony_max_ver 5.0

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
Release:       4%{?github_release}%{?dist}
Summary:       Provide configuration services for a command-line tool

License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}

# GitHub export does not include tests
# Run php-consolidation-config-get-source.sh to create full source
Source0:       %{name}-%{github_version}-%{github_commit}.tar.gz
Source1:       %{name}-get-source.sh

BuildArch:     noarch
# Tests
%if %{with_tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: php-composer(phpunit/phpunit)
%if %{with_range_dependencies}
BuildRequires: (php-composer(dflydev/dot-access-data) >= %{dflydev_dot_access_data_min_ver} with php-composer(dflydev/dot-access-data) < %{dflydev_dot_access_data_max_ver})
BuildRequires: (php-composer(grasmash/expander) >= %{grasmash_expander_min_ver} with php-composer(grasmash/expander) < %{grasmash_expander_max_ver})
BuildRequires: (php-composer(symfony/console) >= %{symfony_min_ver} with php-composer(symfony/console) < %{symfony_max_ver})
BuildRequires: (php-composer(symfony/yaml) >= %{symfony_min_ver} with php-composer(symfony/yaml) < %{symfony_max_ver})
### phpcompatinfo
BuildRequires: (php-composer(symfony/event-dispatcher) >= %{symfony_min_ver} with php-composer(symfony/event-dispatcher) < %{symfony_max_ver})
%else
BuildRequires: php-composer(dflydev/dot-access-data) <  %{dflydev_dot_access_data_max_ver}
BuildRequires: php-composer(dflydev/dot-access-data) >= %{dflydev_dot_access_data_min_ver}
BuildRequires: php-composer(grasmash/expander) <  %{grasmash_expander_max_ver}
BuildRequires: php-composer(grasmash/expander) >= %{grasmash_expander_min_ver}
BuildRequires: php-composer(symfony/console) <  %{symfony_max_ver}
BuildRequires: php-composer(symfony/console) >= %{symfony_min_ver}
BuildRequires: php-composer(symfony/yaml) <  %{symfony_max_ver}
BuildRequires: php-composer(symfony/yaml) >= %{symfony_min_ver}
### phpcompatinfo
BuildRequires: php-composer(symfony/event-dispatcher) <  %{symfony_max_ver}
BuildRequires: php-composer(symfony/event-dispatcher) >= %{symfony_min_ver}
%endif
## phpcompatinfo for version 1.2.1
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
Requires:      (php-composer(grasmash/expander) >= %{grasmash_expander_min_ver} with php-composer(grasmash/expander) < %{grasmash_expander_max_ver})
## phpcompatinfo
Requires:      (php-composer(symfony/console) >= %{symfony_min_ver} with php-composer(symfony/console) < %{symfony_max_ver})
Requires:      (php-composer(symfony/event-dispatcher) >= %{symfony_min_ver} with php-composer(symfony/event-dispatcher) < %{symfony_max_ver})
%else
Requires:      php-composer(dflydev/dot-access-data) <  %{dflydev_dot_access_data_max_ver}
Requires:      php-composer(dflydev/dot-access-data) >= %{dflydev_dot_access_data_min_ver}
Requires:      php-composer(grasmash/expander) <  %{grasmash_expander_max_ver}
Requires:      php-composer(grasmash/expander) >= %{grasmash_expander_min_ver}
## phpcompatinfo
Requires:      php-composer(symfony/console) <  %{symfony_max_ver}
Requires:      php-composer(symfony/console) >= %{symfony_min_ver}
Requires:      php-composer(symfony/event-dispatcher) <  %{symfony_max_ver}
Requires:      php-composer(symfony/event-dispatcher) >= %{symfony_min_ver}
%endif
## suggest (weak dependencies)
Recommends:    php-composer(symfony/yaml)
# phpcompatinfo for version 1.2.1
Requires:      php-pcre
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
Manage configuration for a command-line tool.

This component is designed to provide the components needed to manage
configuration options from different sources, including:
* Commandline options
* Configuration files
* Alias files (special configuration files that identify a specific target site)
* Default values (provided by command)

Symfony Console is used to provide the framework for the command-line tool, and
the Symfony Configuration component is used to load and merge configuration
files. This project provides the glue that binds the components together in an
easy-to-use package.

Autoloader: %{phpdir}/Consolidation/Config/autoload.php


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

\Fedora\Autoloader\Autoload::addPsr4('Consolidation\\Config\\', __DIR__);

\Fedora\Autoloader\Dependencies::required([
    '%{phpdir}/Dflydev/DotAccessData/autoload.php',
    '%{phpdir}/Grasmash/Expander/autoload.php',
    [
        '%{phpdir}/Symfony4/Component/Console/autoload.php',
        '%{phpdir}/Symfony3/Component/Console/autoload.php',
%if %{with_symfony2}
        '%{phpdir}/Symfony/Component/Console/autoload.php',
%endif
    ],
    [
        '%{phpdir}/Symfony4/Component/EventDispatcher/autoload.php',
        '%{phpdir}/Symfony3/Component/EventDispatcher/autoload.php',
%if %{with_symfony2}
        '%{phpdir}/Symfony/Component/EventDispatcher/autoload.php',
%endif
    ],
]);

\Fedora\Autoloader\Dependencies::optional([
    [
        '%{phpdir}/Symfony4/Component/Yaml/autoload.php',
        '%{phpdir}/Symfony3/Component/Yaml/autoload.php',
%if %{with_symfony2}
        '%{phpdir}/Symfony/Component/Yaml/autoload.php',
%endif
    ]
]);
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}/Consolidation
cp -rp src %{buildroot}%{phpdir}/Consolidation/Config


%check
%if %{with_tests}
: Create tests bootstrap
cat <<'BOOTSTRAP' | tee bootstrap.php
<?php
require '%{buildroot}%{phpdir}/Consolidation/Config/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('Consolidation\\TestUtils\\', __DIR__.'/tests/src');
BOOTSTRAP

: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which phpunit)
for PHP_EXEC in "" php70 php71 php72 php73 php74; do
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
%doc *.md
%doc composer.json
%dir %{phpdir}/Consolidation
     %{phpdir}/Consolidation/Config


%changelog
* Mon Feb 24 2020 Shawn Iwinski <shawn@iwin.ski> - 1.2.1-4
- Drop Symfony 2 interoperability
- Add get source script

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 15 2019 Shawn Iwinski <shawn@iwin.ski> - 1.2.1-1
- Update to 1.2.1 (RHBZ #1508224)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Oct 08 2017 Shawn Iwinski <shawn@iwin.ski> - 1.0.3-1
- Update to 1.0.3

* Sun Oct 01 2017 Shawn Iwinski <shawn@iwin.ski> - 1.0.2-1
- Update to 1.0.2

* Mon Aug 21 2017 Shawn Iwinski <shawn@iwin.ski> - 1.0.1-1
- Initial package

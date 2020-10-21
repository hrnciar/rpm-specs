#
# Fedora spec file for php-composer-installers
#
# Copyright (c) 2015-2018 Shawn Iwinski <shawn.iwinski@gmail.com>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     composer
%global github_name      installers
%global github_version   1.5.0
%global github_commit    049797d727261bf27f2690430d935067710049c2

%global composer_vendor  composer
%global composer_project installers

# "composer-plugin-api": "^1.0"
%global composer_plugin_min_ver 1.0
%global composer_plugin_max_ver 2.0
# "composer/composer": "1.0.*@dev"
%global composer_min_ver 1.0
%global composer_max_ver 2.0

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       6%{?github_release}%{?dist}
Summary:       A multi-framework Composer library installer

License:       MIT
URL:           http://composer.github.io/installers/
Source0:       https://github.com/%{github_owner}/%{github_name}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
# Tests
%if %{with_tests}
## composer.json
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
BuildRequires: (php-composer(composer/composer) >= %{composer_min_ver} with php-composer(composer/composer) <  %{composer_max_ver})
BuildRequires: (php-composer(composer-plugin-api) >= %{composer_plugin_min_ver} with php-composer(composer-plugin-api) <  %{composer_plugin_max_ver})
%else
BuildRequires: php-composer(composer/composer) <  %{composer_max_ver}
BuildRequires: php-composer(composer/composer) >= %{composer_min_ver}
BuildRequires: php-composer(composer-plugin-api) <  %{composer_plugin_max_ver}
BuildRequires: php-composer(composer-plugin-api) >= %{composer_plugin_min_ver}
%endif
BuildRequires: php-composer(phpunit/phpunit)
## phpcompatinfo (computed from version 1.5.0)
BuildRequires: php(language) >= 5.3.0
BuildRequires: php-pcre
BuildRequires: php-spl
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
Requires:      (php-composer(composer-plugin-api) >= %{composer_plugin_min_ver} with php-composer(composer-plugin-api) <  %{composer_plugin_max_ver})
%else
Requires:      php-composer(composer-plugin-api) >= %{composer_plugin_min_ver}
Requires:      php-composer(composer-plugin-api) <  %{composer_plugin_max_ver}
%endif
# phpcompatinfo (computed from version 1.5.0)
Requires:      php(language) >= 5.3.0
Requires:      php-pcre
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
This is for PHP package authors to require in their composer.json. It will
install their package to the correct location based on the specified package
type.

The goal of installers is to be a simple package type to install path map.
Users can also customize the install path per package and package authors
can modify the package name upon installing.

installers isn't intended on replacing all custom installers. If your package
requires special installation handling then by all means, create a custom
installer to handle it.

Autoloader: %{phpdir}/Composer/Installers/autoload.php


%prep
%setup -qn %{github_name}-%{github_commit}


%build
: Create autoloader
cat <<'AUTOLOAD' | tee src/Composer/Installers/autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 */
require_once '%{phpdir}/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('Composer\\Installers\\', __DIR__);

\Fedora\Autoloader\Dependencies::required(array(
    '%{phpdir}/Composer/autoload.php',
));
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}
cp -rp src/Composer %{buildroot}%{phpdir}/


%check
%if %{with_tests}
: Create tests bootstrap
cat <<'BOOTSTRAP' | tee bootstrap.php
<?php
require_once '%{buildroot}%{phpdir}/Composer/Installers/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('Composer\\Installers\\Test\\', __DIR__.'/tests/Composer/Installers/Test');
BOOTSTRAP

: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which phpunit)
for PHP_EXEC in "" %{?rhel:php55 php56} php70 php71 php72; do
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
%{phpdir}/Composer/Installers


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Apr 20 2018 Remi Collet <remi@remirepo.net> - 1.5.0-1
- update to 1.5.0
- use range dependencies on F27+

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Oct 08 2017 Shawn Iwinski <shawn@iwin.ski> - 1.4.0-1
- Updated to 1.4.0 (RHBZ #1479799)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Apr 29 2017 Shawn Iwinski <shawn@iwin.ski> - 1.3.0-1
- Updated to 1.3.0 (RHBZ #1444845)
- Added max version constraint to php-composer(composer/composer) dependency
- Switched autoloader to php-composer(fedora/autoloader)
- Test with SCLs if available

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Sep 11 2016 Shawn Iwinski <shawn@iwin.ski> - 1.2.0-1
- Updated to 1.2.0 (RHBZ #1372115)

* Sat Jul 23 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.1.0-1
- Updated to 1.1.0 (RHBZ #1352896)
- Updated URL

* Fri Apr 15 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.0.25-1
- Updated to 1.0.25 (RHBZ #1326974)

* Tue Apr 12 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.0.24-1
- Updated to 1.0.24 (RHBZ #1325590)

* Sat Mar 12 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.0.23-1
- Updated to 1.0.23 (RHBZ #1302488)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.22-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Nov 04 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.0.22-2
- Dependency updates

* Wed Nov 04 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.0.22-1
- Updated to 1.0.22 (RHBZ #1276816)

* Thu Aug 20 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.0.21-1
- Initial package

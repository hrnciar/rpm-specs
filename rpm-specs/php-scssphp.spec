#
# Fedora spec file for php-scssphp
#
# Copyright (c) 2012-2019 Shawn Iwinski <shawn.iwinski@gmail.com>
#                         Remi Collet <remi@fedoraproject.org>
#                         Christian Glombek <christian.glombek@rwth-aachen.de>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     leafo
%global github_name      scssphp
%global github_version   0.8.4
%global github_commit    b9cdea3e42c3bcb1a9faafd04ccce4e8ec860ad9

%global composer_vendor  leafo
%global composer_project scssphp

# "php": "^5.4.0 || ^7"
%global php_min_ver 5.4.0

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{github_name}
Version:       %{github_version}
Release:       2%{?dist}
Summary:       A compiler for SCSS written in PHP
License:       MIT
URL:           http://leafo.github.io/scssphp

# GitHub export does not include tests.
# Run php-scssphp-get-source.sh to create full source.
Source0:       %{name}-%{github_version}-%{github_commit}.tar.gz
Source1:       %{name}-get-source.sh

Patch0:        https://patch-diff.githubusercontent.com/raw/leafo/scssphp/pull/710.patch

BuildArch:     noarch
# Library version check
BuildRequires: php-cli
# Tests
%if %{with_tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: php-composer(phpunit/phpunit)
## phpcompatinfo (computed from version 0.8.3)
BuildRequires: php-ctype
BuildRequires: php-date
BuildRequires: php-json
BuildRequires: php-mbstring
BuildRequires: php-pcre
BuildRequires: php-spl
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

Requires:      php-cli
# composer.json
Requires:      php(language) >= %{php_min_ver}
# phpcompatinfo (computed from version 0.8.3)
Requires:      php-ctype
Requires:      php-date
Requires:      php-json
Requires:      php-mbstring
Requires:      php-pcre
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Standard "php-{COMPOSER_VENDOR}-{COMPOSER_PROJECT}" naming
Provides:      php-%{composer_vendor}-%{composer_project} = %{version}-%{release}
# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}


%description
SCSS (http://sass-lang.com/) is a CSS preprocessor that adds many features like
variables, mixins, imports, color manipulation, functions, and tons of other
powerful features.

The entire compiler comes in a single class file ready for including in any kind
of project in addition to a command line tool for running the compiler from the
terminal.

scssphp implements SCSS. It does not implement the SASS syntax, only the SCSS
syntax.

Autoloader: %{phpdir}/Leafo/ScssPhp/autoload.php


%prep
%setup -qn %{github_name}-%{github_commit}
%patch0 -p1

: Adjust bin autoload require
sed "/scss.inc.php/s#.*#require_once '%{phpdir}/Leafo/ScssPhp/autoload.php';#" \
    -i bin/pscss


%build
: Create autoloader
cat <<'AUTOLOAD' | tee src/autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 */
require_once '%{phpdir}/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('Leafo\\ScssPhp\\', __DIR__);
AUTOLOAD


%install
: Lib
mkdir -p %{buildroot}%{phpdir}/Leafo/ScssPhp
cp -pr src/* %{buildroot}%{phpdir}/Leafo/ScssPhp/

: Bin
mkdir -p %{buildroot}%{_bindir}
install -pm 0755 bin/pscss %{buildroot}%{_bindir}/


%check
: Library version value and autoloader check
%{_bindir}/php -r '
    require_once "%{buildroot}%{phpdir}/Leafo/ScssPhp/autoload.php";
    $version = ltrim(\Leafo\ScssPhp\Version::VERSION, "v");
    echo "Version $version (expected %{version})\n";
    exit(version_compare("%{version}", "$version", "=") ? 0 : 1);
'

: Skip tests requiring non-resolved dependencies
rm -f tests/FrameworkTest.php

: Skip flapping/flakey test
sed '/2147483647/d' -i tests/Base64VLQTest.php

%if %{with_tests}
RETURN_CODE=0
PHPUNIT=$(which phpunit)
for PHP_EXEC in "" %{?rhel:php55 php56 php70} php71 php72 php73 php74
do
    if [ -z "$PHP_EXEC" ] || which $PHP_EXEC
    then
        $PHP_EXEC $PHPUNIT --verbose \
            --bootstrap %{buildroot}%{phpdir}/Leafo/ScssPhp/autoload.php \
            || RETURN_CODE=1
    fi
done
exit $RETURN_CODE
%else
: Tests skipped
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE.md
%doc composer.json
%doc README.md
%{phpdir}/Leafo/ScssPhp
%{_bindir}/pscss


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 13 2019 Remi Collet <remi@remirepo.net> - 0.8.4-1
- update to 0.8.4
- add patch for PHP 7.4 from
  https://github.com/leafo/scssphp/pull/710

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 03 2019 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.8.3-1
- Update to 0.8.3 (RHBZ #1716011)

* Fri May 10 2019 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.8.2-1
- Update to 0.8.2 (RHBZ #1703256)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Dec 21 2018 Remi Collet <remi@remirepo.net> - 0.7.7-1
- update to 0.7.7

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon May 28 2018 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.7.6-1
- Update to 0.7.6 (RHBZ #1582167)
- Add composer.json to repo

* Sun Mar 25 2018 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.7.5-2
- Update get source script to save in spec directory
- Update phpcompatinfo computed dependencies
- Remove code sniffer dependency and test
- Modify upstream test run

* Tue Feb 13 2018 Christian Glombek <christian.glombek@rwth-aachen.de> - 0.7.5-1
- Updated to 0.7.5 (RHBZ #1504394)
- Use php_condesniffer for testing

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Mar 04 2017 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.6.7-1
- Updated to 0.6.7 (RHBZ #1426927)
- Switch autoloader to php-composer(fedora/autoloader)
- Test with SCLs if available

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Sep 25 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.6.6-1
- Updated to 0.6.6 (RHBZ #1376293)

* Sat Jul 23 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.6.5-1
- Updated to 0.6.5 (RHBZ #1347068)
- Dropped pre-0.1.0 compat

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 20 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.4.0-1
- Updated to 0.4.0 (RHBZ #1274939)
- Removed php-json dependency

* Sun Oct 11 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.3.2-1
- Updated to 0.3.2 (RHBZ #1268709)

* Sun Sep 20 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.3.1-1
- Updated to 0.3.1 (RHBZ #1256168)
- Updated URL
- Added standard "php-{COMPOSER_VENDOR}-{COMPOSER_PROJECT}" naming provides
- Added library version value check

* Thu Aug 13 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.1.9-1
- Updated to 0.1.9 (RHBZ #1238727)
- As of version 0.1.7 license is just MIT (i.e. GPLv3 removed)

* Sun Jun 28 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.1.6-1
- Updated to 0.1.6 (RHBZ #1226748)
- Added autoloader

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jan 02 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.1.1-2
- Bump release for Koji/Bodhi

* Thu Oct 30 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.1.1-1
- Updated to 0.1.1 (BZ #1126612)
- Removed man page
- %%license usage

* Tue Aug 19 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.0.15-1
- Updated to 0.0.15 (BZ #1126612)

* Mon Jul 07 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.0.12-1
- Updated to 0.0.12 (BZ #1116615)
- Added option to build without tests ("--without tests")

* Sun Jun 08 2014 Remi Collet <remi@fedoraproject.org> - 0.0.10-2
- fix FTBFS, ignore max version of PHPUnit
- provides php-composer(leafo/scssphp)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Apr 21 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.0.10-1
- Updated to 0.0.10 (BZ #1087738)

* Sun Dec 29 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.0.9-1
- Updated to 0.0.9 (BZ #1046671)
- Spec cleanup

* Fri Nov 15 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.0.8-1
- Updated to 0.0.8 (BZ #1009564)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 07 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.0.7-1
- Updated to 0.0.7 (BZ #967834)

* Sat Mar 16 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.0.5-1
- Updated to version 0.0.5
- php-cli => php(language)
- %%{__php} => %%{_bindir}/php

* Sat Mar 09 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.0.4-2.20130301git3463d7d
- Updated to latest snapshot
- php-common => php-cli
- Added man page
- Removed tests from package

* Tue Nov 27 2012 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.0.4-1
- Initial package

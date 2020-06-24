#
# Fedora spec file for php-doctrine-orm
#
# Copyright (c) 2013-2020 Shawn Iwinski <shawn.iwinski@gmail.com>
#                         Remi Collet <remi@fedoraproject.org>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     doctrine
%global github_name      orm
%global github_version   2.7.3
%global github_commit    d95e03ba660d50d785a9925f41927fef0ee553cf

%global composer_vendor  doctrine
%global composer_project orm

# "php": "^7.1"
%global php_min_ver 7.1
# "doctrine/annotations": "^1.8",
%global annotations_min_ver 1.8
%global annotations_max_ver 2
# "doctrine/cache": "^1.9.1"
%global cache_min_ver 1.9.1
%global cache_max_ver 2
# "doctrine/collections": "^1.5"
%global collections_min_ver 1.5
%global collections_max_ver 2
# "doctrine/common": "^2.11 || ^3.0"
%global common_min_ver 2.11
%global common_max_ver 4
# "doctrine/dbal": "^2.9.3"
%global dbal_min_ver 2.9.3
%global dbal_max_ver 3
# "doctrine/inflector": "^1.0"
%global inflector_min_ver 1.0
%global inflector_max_ver 2
# "doctrine/instantiator": "^1.3"
%global instantiator_min_ver 1.3
%global instantiator_max_ver 2
# "doctrine/lexer": "^1.0"
%global lexer_min_ver 1.0
%global lexer_max_ver 2
# "doctrine/persistence": "^1.3.3 || ^2.0"
%global persistence_min_ver 1.3.3
%global persistence_max_ver 3
# "doctrine/event-manager": "^1.1"
%global event_min_ver 1.1
%global event_max_ver 2
# "symfony/console": "^3.0|^4.0|^5.0"
# "symfony/yaml": "~^3.4|^4.0|^5.0"
%global symfony_min_ver 3.4
%global symfony_max_ver 6

%{!?phpdir:  %global phpdir  %{_datadir}/php}

# Build using "--without tests" to disable tests
%global with_tests %{?_without_tests:0}%{!?_without_tests:1}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       1%{?dist}
Summary:       Doctrine Object-Relational-Mapper (ORM)

License:       MIT
URL:           https://www.doctrine-project.org/projects/orm.html

# Run "php-doctrine-orm-get-source.sh" to create source
Source0:       %{name}-%{version}-%{github_commit}.tar.gz
Source1:       %{name}-get-source.sh

# Update bin script:
# 1) Add she-bang
# 2) Auto-load using Doctrine\Common\ClassLoader
Patch0:        %{name}-bin.patch
# get rid of ocramius/package-versions
Patch1:        %{name}-version.patch

BuildArch: noarch
# Tests
%if %{with_tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: (php-composer(doctrine/annotations)   >= %{annotations_min_ver}  with php-composer(doctrine/annotations)   < %{annotations_max_ver})
BuildRequires: (php-composer(doctrine/cache)         >= %{cache_min_ver}        with php-composer(doctrine/cache)         < %{cache_max_ver})
BuildRequires: (php-composer(doctrine/collections)   >= %{collections_min_ver}  with php-composer(doctrine/collections)   < %{collections_max_ver})
BuildRequires: (php-composer(doctrine/common)        >= %{common_min_ver}       with php-composer(doctrine/common)        < %{common_max_ver})
BuildRequires: (php-composer(doctrine/dbal)          >= %{dbal_min_ver}         with php-composer(doctrine/dbal)          < %{dbal_max_ver})
BuildRequires: (php-composer(doctrine/inflector)     >= %{inflector_min_ver}    with php-composer(doctrine/inflector)     < %{inflector_max_ver})
BuildRequires: (php-composer(doctrine/instantiator)  >= %{instantiator_min_ver} with php-composer(doctrine/instantiator)  < %{instantiator_max_ver})
BuildRequires: (php-composer(doctrine/event-manager) >= %{event_min_ver}        with php-composer(doctrine/event-manager) < %{event_max_ver})
BuildRequires: (php-composer(doctrine/lexer)         >= %{lexer_min_ver}        with php-composer(doctrine/lexer)         < %{lexer_max_ver})
BuildRequires: (php-composer(doctrine/persistence)   >= %{persistence_min_ver}  with php-composer(doctrine/persistence)   < %{persistence_max_ver})
BuildRequires: (php-composer(symfony/console)        >= %{symfony_min_ver}      with php-composer(symfony/console)        < %{symfony_max_ver})
BuildRequires: (php-composer(symfony/yaml)           >= %{symfony_min_ver}      with php-composer(symfony/yaml)           < %{symfony_max_ver})
BuildRequires: phpunit7 >= 7.5
BuildRequires: php-pdo
# phpcompatinfo (computed from version 2.5.11)
BuildRequires: php-ctype
BuildRequires: php-date
BuildRequires: php-dom
BuildRequires: php-json
BuildRequires: php-pcre
BuildRequires: php-reflection
BuildRequires: php-simplexml
BuildRequires: php-spl
BuildRequires: php-tokenizer
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
Requires:      (php-composer(doctrine/annotations)   >= %{annotations_min_ver}  with php-composer(doctrine/annotations)   < %{annotations_max_ver})
Requires:      (php-composer(doctrine/cache)         >= %{cache_min_ver}        with php-composer(doctrine/cache)         < %{cache_max_ver})
Requires:      (php-composer(doctrine/collections)   >= %{collections_min_ver}  with php-composer(doctrine/collections)   < %{collections_max_ver})
Requires:      (php-composer(doctrine/common)        >= %{common_min_ver}       with php-composer(doctrine/common)        < %{common_max_ver})
Requires:      (php-composer(doctrine/dbal)          >= %{dbal_min_ver}         with php-composer(doctrine/dbal)          < %{dbal_max_ver})
Requires:      (php-composer(doctrine/inflector)     >= %{inflector_min_ver}    with php-composer(doctrine/inflector)     < %{inflector_max_ver})
Requires:      (php-composer(doctrine/instantiator)  >= %{instantiator_min_ver} with php-composer(doctrine/instantiator)  < %{instantiator_max_ver})
Requires:      (php-composer(doctrine/event-manager) >= %{event_min_ver}        with php-composer(doctrine/event-manager) < %{event_max_ver})
Requires:      (php-composer(doctrine/lexer)         >= %{lexer_min_ver}        with php-composer(doctrine/lexer)         < %{lexer_max_ver})
Requires:      (php-composer(doctrine/persistence)   >= %{persistence_min_ver}  with php-composer(doctrine/persistence)   < %{persistence_max_ver})
Requires:      (php-composer(symfony/console)        >= %{symfony_min_ver}      with php-composer(symfony/console)        < %{symfony_max_ver})
# composer.json: suggest
Recommends:    (php-composer(symfony/yaml)           >= %{symfony_min_ver}      with php-composer(symfony/yaml)           < %{symfony_max_ver})
Requires:      php-pdo
# phpcompatinfo (computed from version 2.5.11)
Requires:      php-ctype
Requires:      php-date
Requires:      php-dom
Requires:      php-json
Requires:      php-pcre
Requires:      php-reflection
Requires:      php-simplexml
Requires:      php-spl
Requires:      php-tokenizer
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Weak dependencies
%if 0%{?fedora} >= 21
## Optional caches (see Doctrine\ORM\Tools\Setup::createConfiguration())
Suggests:      php-pecl(apcu)
Suggests:      php-pecl(memcache)
Suggests:      php-pecl(redis)
Suggests:      php-xcache
%endif

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}
# PEAR
Provides:      php-pear(pear.doctrine-project.org/DoctrineORM) = %{version}
# Rename
Obsoletes:     php-doctrine-DoctrineORM < %{version}
Provides:      php-doctrine-DoctrineORM = %{version}

%description
Object relational mapper (ORM) for PHP that sits on top of a powerful database
abstraction layer (DBAL). One of its' key features is the option to write
database queries in a proprietary object oriented SQL dialect called Doctrine
Query Language (DQL), inspired by Hibernate's HQL. This provides developers
with a powerful alternative to SQL that maintains flexibility without requiring
unnecessary code duplication.

Autoloader: %{phpdir}/Doctrine/ORM/autoload.php


%prep
%setup -qn %{github_name}-%{github_commit}

: Patch bin script
%patch0 -p1 -b .rpm
sed -e 's#__PHPDIR__#%{phpdir}#g' -i \
    bin/doctrine.php

%patch1 -p1 -b .rpm
sed -e 's/@VERSION@/%{version}/' -i \
    lib/Doctrine/ORM/Tools/Console/ConsoleRunner.php \
    tests/Doctrine/Tests/ORM/Tools/Console/ConsoleRunnerTest.php
find lib -name \*.rpm -delete

: Remove empty file
rm -f lib/Doctrine/ORM/README.markdown


%build
: Create autoloader
cat <<'AUTOLOAD' | tee lib/Doctrine/ORM/autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 */
require_once '%{phpdir}/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('Doctrine\\ORM\\', __DIR__);

\Fedora\Autoloader\Dependencies::required([
    [
        '%{phpdir}/Doctrine/Common3/autoload.php',
        '%{phpdir}/Doctrine/Common/autoload.php',
    ],
    '%{phpdir}/Doctrine/Common/Cache/autoload.php',
    '%{phpdir}/Doctrine/Common/Collections/autoload.php',
    '%{phpdir}/Doctrine/Common/Inflector/autoload.php',
    '%{phpdir}/Doctrine/Common/EventManager/autoload.php',
    '%{phpdir}/Doctrine/Common/Lexer/autoload.php',
    [
        '%{phpdir}/Doctrine/Persistence2/autoload.php',
        '%{phpdir}/Doctrine/Persistence/autoload.php',
    ],
    '%{phpdir}/Doctrine/DBAL/autoload.php',
    '%{phpdir}/Doctrine/Instantiator/autoload.php',
    [
      '%{phpdir}/Symfony5/Component/Console/autoload.php',
      '%{phpdir}/Symfony4/Component/Console/autoload.php',
      '%{phpdir}/Symfony3/Component/Console/autoload.php',
    ],
]);

\Fedora\Autoloader\Dependencies::optional([
  [
    '%{phpdir}/Symfony5/Component/Yaml/autoload.php',
    '%{phpdir}/Symfony4/Component/Yaml/autoload.php',
    '%{phpdir}/Symfony3Component/Yaml/autoload.php',
  ],
]);
AUTOLOAD


%install
: Lib
mkdir -p %{buildroot}%{phpdir}
cp -rp lib/Doctrine %{buildroot}%{phpdir}/

: Bin
mkdir -p %{buildroot}/%{_bindir}
install -pm 0755 bin/doctrine.php %{buildroot}/%{_bindir}/doctrine


%check
%if %{with_tests}
: Remove load of TestInit
mv tests/Doctrine/Tests/TestInit.php tests/Doctrine/Tests/TestInit.php.dist
grep -r --files-with-matches 'TestInit' tests \
    | xargs sed '/TestInit/d' -i

: Load annotation register file from buildroot
sed 's#__DIR__\s*\.\s*"/\(\.\./\)*lib#"%{buildroot}%{phpdir}#' \
    -i tests/Doctrine/Tests/OrmTestCase.php

: Create tests bootstrap
cat > bootstrap.php <<'BOOTSTRAP'
<?php
require_once '%{buildroot}%{phpdir}/Doctrine/ORM/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('Doctrine\\Tests\\', __DIR__.'/tests/Doctrine/Tests');
\Fedora\Autoloader\Autoload::addPsr4('Doctrine\\Performance\\', __DIR__.'/tests/Doctrine/Performance');
BOOTSTRAP

: Upstream tests
RETURN_CODE=0
for PHP_EXEC in "" php72 php73 php74; do
    if [ -z "$PHP_EXEC" ] || which $PHP_EXEC; then
        $PHP_EXEC %{_bindir}/phpunit7 --verbose -d memory_limit="512M" --bootstrap bootstrap.php \
            || RETURN_CODE=1
    fi
done
exit $RETURN_CODE
%else
: Tests skipped
%endif


%files
%license LICENSE
%doc *.md
%doc composer.json
%{phpdir}/Doctrine/ORM
%{_bindir}/doctrine


%changelog
* Wed May 27 2020 Remi Collet <remi@remirepo.net> - 2.7.3-1
- update to 2.7.3
- allow doctrine/common v3
- allow doctrine/persistence v2
- add dependency on doctrine/inflector
- add dependency on doctrine/lexer

* Wed Mar 25 2020 Remi Collet <remi@remirepo.net> - 2.7.2-1
- update to 2.7.2

* Mon Feb 17 2020 Remi Collet <remi@remirepo.net> - 2.7.1-1
- update to 2.7.1

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 19 2019 Remi Collet <remi@remirepo.net> - 2.7.0-1
- update to 2.7.0
- add dependency on doctrine/event-manager
- add dependency on doctrine/persistence
- raise dependency on doctrine/annotations 1.8
- raise dependency on doctrine/cache 1.9.1
- raise dependency on doctrine/collections 1.5
- raise dependency on doctrine/common 2.11
- raise dependency on doctrine/dbal 2.9.3
- raise dependency on doctrine/instantiator 1.3
- allow Symfony 5
- symfony/yaml is optional

* Tue Nov 19 2019 Remi Collet <remi@remirepo.net> - 2.6.6-1
- update to 2.6.6

* Mon Nov 18 2019 Remi Collet <remi@remirepo.net> - 2.6.5-1
- update to 2.6.5

* Mon Sep 30 2019 Remi Collet <remi@remirepo.net> - 2.6.4-1
- update to 2.6.4
- switch to phpunit7

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 22 2018 Remi Collet <remi@remirepo.net> - 2.6.3-1
- update to 2.6.3

* Wed Oct 17 2018 Remi Collet <remi@remirepo.net> - 2.6.2-1
- update to 2.6.2
- raise dependency on PHP 7.1
- add dependency on doctrine/annotations
- raise dependency on doctrine/cache 1.6
- raise dependency on doctrine/collections 1.4
- raise dependency on doctrine/common 2.7.1
- raise dependency on doctrine/dbal 2.6
- raise dependency on doctrine/instantiator 1.1
- switch to symfony 3 and 4
- switch to phpunit6

* Tue Oct 16 2018 Remi Collet <remi@remirepo.net> - 2.5.14-1
- update to 2.5.14
- fix FTBFS from Koschei add patch for PHP 7.3 from
  https://github.com/doctrine/doctrine2/pull/7431
- use range dependencies

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Nov 10 2017 Remi Collet <remi@remirepo.net> - 2.5.12-2
- fix more tests failing since 7.1

* Fri Nov 10 2017 Remi Collet <remi@remirepo.net> - 2.5.12-1
- Update to 2.5.12
- fix FTBFS from Koschei add patch for PHP 7.2 from
  https://github.com/doctrine/doctrine2/pull/6821

* Wed Sep 20 2017 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.5.11-1
- Updated to 2.5.11 (RHBZ #1207905)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 25 2017 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.4.8-3
- Fix FTBFS in rawhide (RHBZ #1424060)
- Use php-composer(fedora/autoloader)
- Test SCLs if available

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jul 09 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.4.8-1
- Updated to 2.4.8 (RHBZ #1347926 / CVE-2015-5723)
- Added autoloader

* Mon Jun 13 2016 Remi Collet <remi@fedoraproject.org> - 2.4.7-5
- add workaround for test suite with PHPUnit 5.4

* Sun Feb 28 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.4.7-4
- Skip additional tests known to fail (RHBZ #1307857)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Dec 28 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.4.7-1
- Updated to 2.4.7 (BZ #1175217)
- %%license usage

* Mon Nov 03 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.4.6-2
- Ensure 512M of memory (instead of default 128M) so mock x86_64
  builds pass (BZ #1159650)

* Tue Oct 14 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.4.6-1
- Updated to 2.4.6 (BZ #1108129)
- Manual git clone source instead of GitHub archive URL (to include tests)
- Removed Patch1 (%%{name}-upstream.patch)
- Added tests

* Sat Jun 21 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.4.2-4
- Added php-composer(%%{composer_vendor}/%%{composer_project}) virtual provide
- Updated Doctrine dependencies to use php-composer virtual provides

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 30 2014 Remi Collet <remi@fedoraproject.org> - 2.4.2-2
- upstream fix for latest PHP (#1103219)

* Wed Feb 12 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.4.2-1
- Updated to 2.4.2 (BZ #1063021)

* Sat Jan 04 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.4.1-2
- Conditional %%{?dist}
- Bin script patch instead of inline update and use Doctrine Common classloader
- Updated optional cache information in %%description
- Removed empty file
- Removed unnecessary executable bit

* Sat Dec 28 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.4.1-1
- Initial package

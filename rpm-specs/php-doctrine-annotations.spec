#
# Fedora spec file for php-doctrine-annotations
#
# Copyright (c) 2013-2020 Shawn Iwinski <shawn.iwinski@gmail.com>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

# Build using "--without tests" to disable tests
%bcond_without tests

%global github_owner     doctrine
%global github_name      annotations
%global github_version   1.10.4
%global github_commit    bfe91e31984e2ba76df1c1339681770401ec262f

%global composer_vendor  doctrine
%global composer_project annotations

# "php": "^7.1 || ^8.0"
%global php_min_ver      7.1
# "doctrine/cache": "1.*"
#     NOTE: Min version not 1.0 because autoloader required
%global cache_min_ver    1.4.1
%global cache_max_ver    2.0
# "doctrine/lexer": "1.*"
#     NOTE: Min version not 1.0 because autoloader required
%global lexer_min_ver    1.0.1
%global lexer_max_ver    2.0


%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       1%{?github_release}%{?dist}
Summary:       PHP docblock annotations parser library

License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}

# GitHub export does not include tests.
# Run php-doctrine-annotations-get-source.sh to create full source.
Source0:       %{name}-%{version}-%{github_commit}.tar.gz
Source1:       %{name}-get-source.sh

BuildArch:     noarch
# Tests
%if %{with tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
BuildRequires:(php-composer(doctrine/cache) >= %{cache_min_ver} with php-composer(doctrine/cache) < %{cache_max_ver})
BuildRequires:(php-composer(doctrine/lexer) >= %{lexer_min_ver} with php-composer(doctrine/lexer) < %{lexer_max_ver})
# "phpunit/phpunit": "^7.5 || ^9.1.5"
%global phpunit %{_bindir}/phpunit9
BuildRequires: phpunit9 >= 9.1.5
%else
BuildRequires: php-composer(doctrine/cache) <  %{cache_max_ver}
BuildRequires: php-composer(doctrine/cache) >= %{cache_min_ver}
BuildRequires: php-composer(doctrine/lexer) <  %{lexer_max_ver}
BuildRequires: php-composer(doctrine/lexer) >= %{lexer_min_ver}
%global phpunit %{_bindir}/phpunit7
BuildRequires: phpunit7 >= 7.5
%endif

## phpcompatinfo (computed from version 1.10.0)
BuildRequires: php-ctype
BuildRequires: php-date
BuildRequires: php-json
BuildRequires: php-mbstring
BuildRequires: php-pcre
BuildRequires: php-reflection
BuildRequires: php-spl
BuildRequires: php-tokenizer
# Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
Requires:      php-tokenizer
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
Requires:     (php-composer(doctrine/lexer) >= %{lexer_min_ver} with php-composer(doctrine/lexer) < %{lexer_max_ver})
%else
Requires:      php-composer(doctrine/lexer) <  %{lexer_max_ver}
Requires:      php-composer(doctrine/lexer) >= %{lexer_min_ver}
%endif
# phpcompatinfo (computed from version 1.10.0)
Requires:      php-ctype
Requires:      php-date
Requires:      php-json
Requires:      php-pcre
Requires:      php-reflection
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

# Extracted from Doctrine Common as of version 2.4
Conflicts:     php-pear(pear.doctrine-project.org/DoctrineCommon) < 2.4

%description
%{summary} (extracted from Doctrine Common).

Autoloader: %{phpdir}/Doctrine/Common/Annotations/autoload.php


%prep
%setup -qn %{github_name}-%{github_commit}


%build
: Create autoloader
cat <<'AUTOLOAD' | tee lib/Doctrine/Common/Annotations/autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 */
require_once '%{phpdir}/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('Doctrine\\Common\\Annotations\\', __DIR__);

\Fedora\Autoloader\Dependencies::required(array(
    '%{phpdir}/Doctrine/Common/Lexer/autoload.php',
));
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}
cp -rp lib/* %{buildroot}%{phpdir}/


%check
%if %{with tests}
: Modify tests init
sed "s#require.*autoload.*#require_once '%{buildroot}%{phpdir}/Doctrine/Common/Annotations/autoload.php';#" \
    -i tests/Doctrine/Tests/TestInit.php

: Create tests bootstrap
cat <<'BOOTSTRAP' | tee bootstrap.php
<?php
require_once '%{phpdir}/Doctrine/Common/Cache/autoload.php';
require_once __DIR__.'/tests/Doctrine/Tests/TestInit.php';
BOOTSTRAP

: Upstream tests
RETURN_CODE=0
for CMD in "php %{phpunit}" "php72 %{_bindir}/phpunit8" php73 php74 php80; do
    if which $CMD; then
        set $CMD
        $1 ${2:-%{_bindir}/phpunit9} --verbose \
            -d pcre.recursion_limit=10000 \
            --bootstrap bootstrap.php \
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
%{phpdir}/Doctrine/Common/Annotations


%changelog
* Wed Aug 12 2020 Remi Collet <remi@remirepo.net> - 1.10.4-1
- update to 1.10.4
- switch to phpunit9

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Remi Collet <remi@remirepo.net> - 1.10.3-1
- update to 1.10.3 (no change)

* Mon Apr 20 2020 Remi Collet <remi@remirepo.net> - 1.10.2-1
- update to 1.10.2

* Thu Apr  2 2020 Remi Collet <remi@remirepo.net> - 1.10.1-1
- update to 1.10.1

* Thu Apr  2 2020 Remi Collet <remi@remirepo.net> - 1.10.0-1
- update to 1.10.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct  2 2019 Remi Collet <remi@remirepo.net> - 1.8.0-1
- update to 1.8.0

* Mon Aug 19 2019 Remi Collet <remi@remirepo.net> - 1.7.0-1
- update to 1.7.0
- switch to phpunit7

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 26 2019 Remi Collet <remi@remirepo.net> - 1.6.1-1
- update to 1.6.1

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Remi Collet <remi@remirepo.net> - 1.6.0-1
- update to 1.6.0
- raise dependency on PHP 7.1
- use phpunit6
- use range dependencies

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri May 12 2017 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.2.7-4
- Switch autoloader to php-composer(fedora/autoloader)
- Add max versions to build dependencies
- Test with SCLs if available

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Sep 05 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.2.7-1
- Updated to 1.2.7 (RHBZ #1258669 / CVE-2015-5723)
- Updated autoloader to load dependencies after self registration

* Sat Jun 27 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.2.6-2
- Updated autoloader with trailing separator

* Wed Jun 24 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.2.6-1
- Updated to 1.2.6 (RHBZ #1211816)
- Added autoloader

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Dec 28 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.2.3-1
- Updated to 1.2.3 (BZ #1176942)

* Sun Oct 19 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.2.1-1
- Updated to 1.2.1 (BZ #1146910)
- %%license usage

* Thu Jul 17 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.2.0-2
- Removed skipping of test (php-phpunit-PHPUnit-MockObject patched to fix issue)

* Tue Jul 15 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.2.0-1
- Updated to 1.2.0 (BZ #1116887)

* Fri Jun 20 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.1.2-5.20131220gita11349d
- Added php-composer(%%{composer_vendor}/%%{composer_project}) virtual provide
- Added option to build without tests ("--without tests")
- Updated dependencies to use php-composer virtual provides

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-4.20131220gita11349d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Jan 06 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.1.2-3.20131220gita11349d
- Minor syntax changes

* Fri Jan 03 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.1.2-2.20131220gita11349d
- Conditional %%{?dist}
- Added conflict w/ PEAR-based DoctrineCommon pkg (version < 2.4)

* Mon Dec 23 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.1.2-1.20131220gita11349d
- Initial package

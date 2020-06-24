#
# Fedora spec file for php-doctrine-collections
#
# Copyright (c) 2013-2019 Shawn Iwinski <shawn.iwinski@gmail.com>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     doctrine
%global github_name      collections
%global github_version   1.6.5
%global github_commit    fc0206348e17e530d09463fef07ba8968406cd6d

%global composer_vendor  doctrine
%global composer_project collections

# "php": "^7.1.3 || ^8.0"
%global php_min_ver 7.1.3

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       1%{?github_release}%{?dist}
Summary:       Collections abstraction library

License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}

# GitHub export does not include tests.
# Run php-doctrine-collections-get-source.sh to create full source.
Source0:       %{name}-%{github_version}-%{github_commit}.tar.gz
Source1:       %{name}-get-source.sh

BuildArch:     noarch
# Tests
%if %{with_tests}
## composer.json
BuildRequires: phpunit7
BuildRequires: php(language) >= %{php_min_ver}
## phpcompatinfo (computed from version 1.6.0)
BuildRequires: php-pcre
BuildRequires: php-spl
# Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
# phpcompatinfo (computed from version 1.6.0)
Requires:      php-pcre
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

# Extracted from Doctrine Common as of version 2.4
Conflicts:     php-pear(pear.doctrine-project.org/DoctrineCommon) < 2.4

%description
%{summary}.

Autoloader: %{phpdir}/Doctrine/Common/Collections/autoload.php


%prep
%setup -qn %{github_name}-%{github_commit}


%build
: Create autoloader
cat <<'AUTOLOAD' | tee lib/Doctrine/Common/Collections/autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 */
require_once '%{phpdir}/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('Doctrine\\Common\\Collections\\', __DIR__);
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}
cp -rp lib/* %{buildroot}%{phpdir}/


%check
%if %{with_tests}
: Create tests bootstrap
cat <<'BOOTSTRAP' | tee bootstrap.php
<?php
require_once '%{buildroot}%{phpdir}/Doctrine/Common/Collections/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('Doctrine\\Tests\\', __DIR__.'/tests/Doctrine/Tests');
BOOTSTRAP

: Upstream tests
SCL_RETURN_CODE=0
for SCL in php php71 php72 php73 php74 php80; do
    if which $SCL; then
        $SCL %{_bindir}/phpunit7 --verbose --bootstrap bootstrap.php \
            || SCL_RETURN_CODE=1
    fi
done
exit $SCL_RETURN_CODE
%else
: Tests skipped
%endif


%files
%license LICENSE
%doc *.md
%doc composer.json
%dir %{phpdir}/Doctrine
%dir %{phpdir}/Doctrine/Common
     %{phpdir}/Doctrine/Common/Collections


%changelog
* Tue May 26 2020 Remi Collet <remi@remirepo.net> - 1.6.5-1
- update to 1.6.5

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 13 2019 Remi Collet <remi@remirepo.net> - 1.6.4-1
- update to 1.6.4

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 11 2019 Remi Collet <remi@remirepo.net> - 1.6.2-1
- update to 1.6.2

* Tue Mar 26 2019 Remi Collet <remi@remirepo.net> - 1.6.1-1
- update to 1.6.1

* Mon Mar 25 2019 Remi Collet <remi@remirepo.net> - 1.6.0-1
- update to 1.6.0
- raise dependency on PHP 7.1.3
- use PHPUnit 7 for test suite

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 05 2017 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.5.0-1
- Update to 1.5.0 (RHBZ #1473990)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Mar 04 2017 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.4.0-1
- Updated to 1.4.0 (RHBZ #1415530)
- Switched autoloader to php-composer(fedora/autoloader)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jun 27 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.3.0-3
- Updated autoloader with trailing separator

* Wed Jun 24 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.3.0-2
- Added autoloader dependencies

* Wed Jun 24 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.3.0-1
- Updated to 1.3.0 (RHBZ #1211818)
- Added autoloader
- %%license usage

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 20 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.2-3
- Added php-composer(%%{composer_vendor}/%%{composer_project}) virtual provide
- Added option to build without tests ("--without tests")

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Feb 12 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.2-1
- Updated to 1.2 (BZ #1061117)

* Mon Jan 06 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.1-3.20131221git8198717
- Minor syntax changes

* Fri Jan 03 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.1-2.20131221git8198717
- Conditional %%{?dist}
- Added conflict w/ PEAR-based DoctrineCommon pkg (version < 2.4)

* Mon Dec 23 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.1-1.20131221git8198717
- Initial package

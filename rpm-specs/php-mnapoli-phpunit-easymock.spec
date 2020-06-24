#
# Fedora spec file for php-mnapoli-phpunit-easymock
#
# Copyright (c) 2016-2020 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     mnapoli
%global github_name      phpunit-easymock
%global github_version   1.2.0
%global github_commit    11b754737e25c27bb2591c9e21959cd80b03a1aa

%global composer_vendor  mnapoli
%global composer_project phpunit-easymock

# "php": "^7.2"
%global php_min_ver 7.2
# "phpunit/phpunit": "^8.5"
%global phpunit8_min_ver 8.5

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       1%{?github_release}%{?dist}
Summary:       Helpers to build PHPUnit mocks

License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}

# GitHub export does not include tests.
# Run php-mnapoli-phpunit-easymock-get-source.sh to create full source.
Source0:       %{name}-%{github_version}-%{github_commit}.tar.gz
Source1:       %{name}-get-source.sh

BuildArch:     noarch
# Tests
%if %{with_tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: phpunit8 >= %{phpunit8_min_ver}
## phpcompatinfo (computed from version 1.2.0)
BuildRequires: php-reflection
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
Requires:      phpunit8 >= %{phpunit8_min_ver}
# phpcompatinfo (computed from version 1.2.0)
#     <none>
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
%{summary}.

Autoloader: %{phpdir}/EasyMock/autoload.php


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

\Fedora\Autoloader\Autoload::addPsr4('EasyMock\\', __DIR__);

\Fedora\Autoloader\Dependencies::required([
    '%{phpdir}/PHPUnit8/autoload.php',
]);
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}/EasyMock
cp -rp src/* %{buildroot}%{phpdir}/EasyMock/


%check
%if %{with_tests}
: Create tests bootstrap
cat <<'BOOTSTRAP' | tee bootstrap.php
<?php
require_once '%{buildroot}%{phpdir}/EasyMock/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('EasyMock\\Test\\', __DIR__.'/tests');
BOOTSTRAP

: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which phpunit8)
for PHP_EXEC in "" php73 php74; do
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
%{phpdir}/EasyMock


%changelog
* Thu Apr 09 2020 Shawn Iwinski <shawn@iwin.ski> - 1.2.0-1
- Update to 1.2.0 (RHBZ #1784948)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun May 26 2019 Shawn Iwinski <shawn@iwin.ski> - 1.1.0-1
- Update to 1.1.0 (RHBZ #1512241)
- Add range version dependencies for Fedora >= 27 || RHEL >= 8

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Shawn Iwinski <shawn@iwin.ski> - 0.2.3-3
- Switch autoloader to php-composer(fedora/autoloader)
- Add max versions to build dependencies
- Test with SCLs if available

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jun 13 2016 Remi Collet <remi@fedoraproject.org> - 0.2.3-1
- Updated to 0.2.3 (no change)
- drop patch merged upstream

* Mon Jun 13 2016 Remi Collet <remi@fedoraproject.org> - 0.2.2-2
- add patch to fix test suite with latest PHPUnit
  open https://github.com/mnapoli/phpunit-easymock/pull/5

* Sun Jun 05 2016 Shawn Iwinski <shawn@iwin.ski> - 0.2.2-1
- Updated to 0.2.2 (RHBZ #1342738)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 04 2016 Shawn Iwinski <shawn@iwin.ski> - 0.2.1-1
- Updated to 0.2.1
- Fixed directory ownership in %%files

* Sun Jan 03 2016 Shawn Iwinski <shawn@iwin.ski> - 0.2.0-1
- Initial package

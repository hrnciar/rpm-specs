#
# Fedora spec file for php-google-apiclient-services
#
# Copyright (c) 2017-2020 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     googleapis
%global github_name      google-api-php-client-services
%global github_version   0.144
%global github_commit    74c5fc850d9ce441c6b3e52af11b986cd11d379a

%global composer_vendor  google
%global composer_project apiclient-services

# "php": ">=5.4"
%global php_min_ver 5.4

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       2%{?github_release}%{?dist}
Summary:       Google PHP API Client Services

License:       ASL 2.0
URL:           https://github.com/%{github_owner}/%{github_name}

# GitHub export does not include tests
# Run php-google-apiclient-services-get-source.sh to create full source
Source0:       %{name}-%{github_version}-%{github_commit}.tar.gz
Source1:       %{name}-get-source.sh

BuildArch:     noarch
# Tests
%if %{with_tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: php-composer(phpunit/phpunit)
## phpcompatinfo (computed from version 0.144)
##     <none>
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
# phpcompatinfo (computed from version 0.144)
#     <none>
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

Conflicts:     php-google-apiclient < 2

%description
%{summary}.

Autoloader: %{phpdir}/Google/Service/autoload.php


%prep
%setup -qn %{github_name}-%{github_commit}


%build
: Create autoloader
cat <<'AUTOLOAD' | tee src/Google/Service/autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 */
require_once '%{phpdir}/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr0('Google_Service_', dirname(dirname(__DIR__)));
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}
cp -rp src/* %{buildroot}%{phpdir}/


%check
%if %{with_tests}
sed -e '/require_once/d' \
    -e 's#$path\s*=.*#$path="%{buildroot}%{phpdir}/Google/Service/";#' \
    -i tests/ServiceTest.php

: Create tests bootstrap
cat <<'BOOTSTRAP' | tee bootstrap.php
<?php
require '%{buildroot}%{phpdir}/Google/Service/autoload.php';

// Mock "Google_Service_autoload" class for Google_Service_ServiceTest
// @see Google_Service_ServiceTest::serviceProvider()
class Google_Service_autoload {}
BOOTSTRAP

: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which phpunit)
for PHP_EXEC in "" php70 php71 php72 php73 php74; do
    if [ -z "$PHP_EXEC" ] || which $PHP_EXEC; then
        $PHP_EXEC $PHPUNIT --bootstrap bootstrap.php --verbose \
            -d memory_limit="512M" || RETURN_CODE=1
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
%dir %{phpdir}/Google
     %{phpdir}/Google/Service


%changelog
* Sun Sep 06 2020 Shawn Iwinski <shawn@iwin.ski> - 0.144-2
- Fix source

* Sun Sep 06 2020 Shawn Iwinski <shawn@iwin.ski> - 0.144-1
- Update to 0.144 (RHBZ #1720970)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.102-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.102-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.102-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 16 2019 Shawn Iwinski <shawn@iwin.ski> - 0.102-1
- Update to 0.102 (RHBZ #1584457)

* Tue Feb 26 2019 Shawn Iwinski <shawn@iwin.ski> - 0.87-1
- Update to 0.87 (RHBZ #1584457)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.60-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.60-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat May 26 2018 Shawn Iwinski <shawn@iwin.ski> - 0.60-1
- Update to 0.60 (RHBZ #1527508)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.38-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Dec 13 2017 Shawn Iwinski <shawn@iwin.ski> - 0.38-1
- Update to 0.38 (RHBZ #1505203)

* Sun Oct 08 2017 Shawn Iwinski <shawn@iwin.ski> - 0.29-1
- Update to 0.29 (RHBZ #1490369)

* Sun Sep 10 2017 Shawn Iwinski <shawn@iwin.ski> - 0.22-1
- Update to 0.22 (RHBZ #1481241)

* Sat Aug 05 2017 Shawn Iwinski <shawn@iwin.ski> - 0.17-1
- Update to 0.17 (RHBZ #1469105)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jul 08 2017 Shawn Iwinski <shawn@iwin.ski> - 0.13-1
- Update to 0.13 (RHBZ #1461829)

* Mon Apr 03 2017 Shawn Iwinski <shawn@iwin.ski> - 0.11-1
- Update to 0.11
- Raise tests' memory limit to 512M

* Sat Mar 11 2017 Shawn Iwinski <shawn@iwin.ski> - 0.10-1
- Initial package

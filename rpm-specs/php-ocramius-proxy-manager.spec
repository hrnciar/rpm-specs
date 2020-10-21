#
# Fedora spec file for php-ocramius-proxy-manager
#
# Copyright (c) 2015-2020 Shawn Iwinski <shawn.iwinski@gmail.com>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner      Ocramius
%global github_name       ProxyManager
%global github_version    2.2.2
%global github_commit     14b137b06b0f911944132df9d51e445a35920ab1
%global github_short      %(c=%{github_commit}; echo ${c:0:7})

%global composer_vendor   ocramius
%global composer_project  proxy-manager

# "php": "^7.2.0"
%global php_min_ver 7.2
# "zendframework/zend-code": "^3.3.0"
%global zf_min_ver  3.3
%global zf_max_ver  4

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       4%{?github_release}%{?dist}
Summary:       OOP proxy wrappers utilities

License:       MIT
URL:           http://ocramius.github.io/ProxyManager/
Source0:       %{name}-%{github_version}-%{github_short}.tgz
# git snapshot to retrieve test suite
Source1:       makesrc.sh

# Hardcode library version
# drop dependency on ocramius/package-versions
Patch0:        %{name}-rpm.patch

BuildArch:     noarch
# Autoloader
BuildRequires: php-fedora-autoloader-devel
%if %{with_tests}
# Tests
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: (php-autoloader(zendframework/zend-code) >= %{zf_min_ver}  with php-autoloader(zendframework/zend-code) <  %{zf_max_ver})
BuildRequires: php-composer(ocramius/generated-hydrator) >= 2
## phpcompatinfo (computed from version 2.2.0)
BuildRequires: php-pcre
BuildRequires: php-reflection
BuildRequires: php-spl
BuildRequires: phpunit6 >= 6.4.3
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
Requires:     (php-autoloader(zendframework/zend-code) >= %{zf_min_ver}  with php-autoloader(zendframework/zend-code) <  %{zf_max_ver})
# phpcompatinfo (computed from version 2.2.0)
Requires:      php-pcre
Requires:      php-reflection
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Weak dependencies
%if 0%{?fedora} >= 21
Suggests:      php-composer(ocramius/generated-hydrator)
Suggests:      php-autoloader(zendframework/zend-json)
Suggests:      php-autoloader(zendframework/zend-soap)
Suggests:      php-autoloader(zendframework/zend-stdlib)
Suggests:      php-autoloader(zendframework/zend-xmlrpc)
%endif
# For autoloader
Conflicts:     php-ocramius-generated-hydrator < 2

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}


%description
This library aims at providing abstraction for generating various kinds
of proxy classes.

Autoloader: %{phpdir}/ProxyManager/autoload.php


%prep
%setup -qn %{github_name}-%{github_commit}

%patch0 -p0
sed -e 's/@VERSION@/%{version}/' \
    -e 's/@COMMIT@/%{github_commit}/' \
    -i src/ProxyManager/Version.php
grep ' return' src/ProxyManager/Version.php


%build
: Generate autoloader
%{_bindir}/phpab --template fedora --output src/ProxyManager/autoload.php src/ProxyManager

cat <<'AUTOLOAD' | tee -a src/ProxyManager/autoload.php

\Fedora\Autoloader\Dependencies::required([
    '%{phpdir}/Zend/Code/autoload.php',
]);
\Fedora\Autoloader\Dependencies::optional([
    '%{phpdir}/GeneratedHydrator/autoload.php',
    '%{phpdir}/Zend/Json/autoload.php',
    '%{phpdir}/Zend/Soap/autoload.php',
    '%{phpdir}/Zend/Stdlib/autoload.php',
    '%{phpdir}/Zend/XmlRpc/autoload.php',
]);
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}
cp -rp src/* %{buildroot}%{phpdir}/


%check
%if %{with_tests}
: Create tests autoload
mkdir vendor
%{_bindir}/phpab --output vendor/autoload.php tests
cat << 'EOF' | tee -a vendor/autoload.php
require_once '%{buildroot}%{phpdir}/ProxyManager/autoload.php';
EOF

%if 0%{?fedora} >= 32 || 0%{?rhel} >= 9
: Zend => Laminas
sed -i "s/'Zend/'Laminas/" \
    tests/ProxyManagerTest/ProxyGenerator/RemoteObject/MethodGenerator/RemoteObjectMethodTest.php
%endif

: Run tests
# TODO 7.4
RETURN_CODE=0
for PHP_EXEC in php php72 php73; do
    if [ "php" == "$PHP_EXEC" ] || which $PHP_EXEC; then
        $PHP_EXEC %{_bindir}/phpunit6 --verbose \
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
%{phpdir}/ProxyManager


%changelog
* Fri Jul 31 2020 Merlin Mathesius <mmathesi@redhat.com> - 2.2.2-4
- Minor conditional fix for ELN

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Feb 23 2020 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.2.2-3
- Fix FTBFS (RHDB #1799874)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Aug 29 2019 Remi Collet <remi@remirepo.net> - 2.2.2-1
- update to 2.2.2
- raise dependency on PHP 7.2
- raise dependency on zend-code 3.3
- use zendframework component autoloaders instead of framework one

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu May  4 2017 Remi Collet <remi@remirepo.net> - 2.1.1-1
- Update to 2.1.1

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Nov 30 2016 Remi Collet <remi@fedoraproject.org> - 2.1.0-1
- update to 2.1.0
- raise dependency on php 7.1
- raise dependency on zendframework/zend-code 3.1
- raise dependency on ocramius/generated-hydrator 2

* Sun Oct 30 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.0.2-2
- Remove test file completely instead of skipping only test in it

* Tue Oct 18 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.0.2-1
- Update to 1.0.2 (RHBZ #1251784)
- Add weak dependencies
- Use dependencies' autoloaders
- Temporarily skip tests on Fedora 25+ (RHBZ #1350615)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 29 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.0.0-2
- Fix autoloader to load all optional pkgs
- Some spec cleanup

* Sat May 16 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.0.0-1
- Initial package

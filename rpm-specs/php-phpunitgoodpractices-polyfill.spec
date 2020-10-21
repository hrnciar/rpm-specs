# remirepo/fedora spec file for php-phpunitgoodpractices-polyfill
#
# Copyright (c) 2018-2020 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

# Polyfill
# https://github.com/PHPUnitGoodPractices/polyfill/releases
%global gh_commit    0e3754f1e31b0051eeb5a7223f9b45ba6442af0d
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     PHPUnitGoodPractices
%global gh_project   polyfill
# Packagist
%global pk_vendor    phpunitgoodpractices
%global pk_project   %{gh_project}
# Namespace
%global ns_vendor    PHPUnitGoodPractices
%global ns_project   Polyfill
%global php_home     %{_datadir}/php
%global with_tests   0%{!?_without_tests:1}
# Traits
# https://github.com/PHPUnitGoodPractices/Traits/releases
%global tr_commit    1f56f643aaa3e98f22acf71129109479afb9ef33
%global tr_short     %(c=%{tr_commit}; echo ${c:0:7})
%global tr_version   1.9.1

Name:           php-%{pk_vendor}-%{pk_project}
Version:        1.4.0
Release:        1%{?dist}
Summary:        Lacking future-compat polyfills for PHPUnit

License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
# git snapshot to get upstream test suite (none for now)
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        php-%{pk_vendor}-traits-%{tr_version}-%{tr_short}.tgz
Source2:        makesrc.sh

BuildArch:      noarch
%if %{with_tests}
# For tests
BuildRequires:  php(language) >= 5.5
BuildRequires:  %{_bindir}/phpunit
# From composer.json,     "require-dev": {
#        "friendsofphp/php-cs-fixer": "^2.11"
# Autoloader
BuildRequires:  php-fedora-autoloader-devel
%endif

# From composer.json,     "require": {
#        "php": "^5.5 || ^7.0 || ^8.0",
#        "phpunit/phpunit": "^4.8.36 || ^5.7.27 || ^6.5.14 || ^7.5.20 || ^8.0 || ^9.0"
Requires:       php(language) >= 5.5
Requires:      (phpunit9 or phpunit8 or phpunit7 or phpunit6 or php-phpunit-PHPUnit)
# From phpcompatinfo report for version polyfill 1.4.0 and traits1.9.1
# nothing
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-%{pk_vendor}-traits = %{tr_version}-%{release}
Provides:       php-composer(%{pk_vendor}/traits) = %{tr_version}
Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}


%description
Lacking future-compat polyfills for PHPUnit.

Autoloader: %{php_home}/%{ns_vendor}/%{ns_project}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit} -a 1
mv composer.json composer-polyfill.json
mv LICENSE LICENSE-polyfill

mv Traits-%{tr_commit}/src           src2
mv Traits-%{tr_commit}/composer.json composer-traits.json
mv Traits-%{tr_commit}/LICENSE       LICENSE-traits

cat << 'EOF' | tee src/autoload.php
<?php
/* autoloader for %{name} */

require_once '%{php_home}/Fedora/Autoloader/autoload.php';
if (!class_exists('PHPUnit\\Framework\\TestCase')) { // Call outside of phpunit command
    \Fedora\Autoloader\Dependencies::required([
        [
            '%{php_home}/PHPUnit9/autoload.php',
            '%{php_home}/PHPUnit8/autoload.php',
            '%{php_home}/PHPUnit7/autoload.php',
            '%{php_home}/PHPUnit6/autoload.php',
            '%{php_home}/PHPUnit/Autoload.php',
        ],
    ]);
}
\Fedora\Autoloader\Autoload::addPsr4('PHPUnitGoodPractices\\Polyfill\\', __DIR__);
\Fedora\Autoloader\Autoload::addPsr4('PHPUnitGoodPractices\\Traits\\', dirname(__DIR__) . '/Traits');
require_once __DIR__ . '/aliases.php';
EOF


%build
# Empty build section, most likely nothing required.


%install
: Library
mkdir -p    %{buildroot}%{php_home}/%{ns_vendor}
cp -pr src  %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}
cp -pr src2 %{buildroot}%{php_home}/%{ns_vendor}/Traits


%check
%if %{with_tests}
: Minimal check for our autoloader
php -r '
require "%{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}/autoload.php";
var_dump(PHPUnit\Runner\Version::id());
if (!trait_exists("PHPUnitGoodPractices\\Polyfill\\PolyfillTrait")) {
   echo("PolyfillTrait missing\n");
   exit(1);
}
if (!class_exists("PHPUnitGoodPractices\\Traits\\PHPUnitVersionRetriever")) {
   echo("PHPUnitVersionRetriever missing\n");
   exit(1);
}
'
%else
: Test suite disabled
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE-*
%doc composer-*.json
%dir %{php_home}/%{ns_vendor}
     %{php_home}/%{ns_vendor}/%{ns_project}
     %{php_home}/%{ns_vendor}/Traits


%changelog
* Tue Oct 20 2020 Remi Collet <remi@remirepo.net> - 1.4.0-1
- update phpunitgoodpractices/polyfill to 1.4.0
- update phpunitgoodpractices/traits to 1.9.1
- allow PHPUnit 9

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 26 2019 Remi Collet <remi@remirepo.net> - 1.2.0-1
- update phpunitgoodpractices/polyfill to 1.2.0
- update phpunitgoodpractices/traits to 1.8.0
- allow PHPUnit 8

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Dec 29 2018 Remi Collet <remi@remirepo.net> - 1.1.0-5
- update phpunitgoodpractices/traits to 1.7.0

* Tue Sep  4 2018 Remi Collet <remi@remirepo.net> - 1.1.0-4
- update phpunitgoodpractices/traits to 1.6.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 25 2018 Remi Collet <remi@remirepo.net> - 1.1.0-2
- add mandatory dependency on one PHPUnit version
- add phpunitgoodpractices/traits 1.5.1
- fix autoloader #1594663

* Mon Jun 11 2018 Remi Collet <remi@remirepo.net> - 1.1.0-1
- update to 1.1.0 (no change)
- add LICENSE file

* Mon Jun  4 2018 Remi Collet <remi@remirepo.net> - 1.0.0-1
- initial package, version 1.0.0
- open https://github.com/PHPUnitGoodPractices/polyfill/issues/1 - LICENSE file

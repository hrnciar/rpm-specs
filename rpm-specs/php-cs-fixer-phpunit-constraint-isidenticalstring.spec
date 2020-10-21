# remirepo/fedora spec file for php-cs-fixer-phpunit-constraint-isidenticalstring
#
# Copyright (c) 2018-2020 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global gh_commit    2bd63d705ff5db3892da10f4df768abaffa8c1e2
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
#global gh_date      20150717
%global gh_owner     PHP-CS-Fixer
%global gh_project   phpunit-constraint-isidenticalstring
%global pk_vendor    php-cs-fixer
%global pk_project   %{gh_project}
%global ns_vendor    PhpCsFixer
%global ns_project   PhpunitConstraintIsIdenticalString
%global php_home     %{_datadir}/php
%global with_tests   0%{!?_without_tests:1}

Name:           %{pk_vendor}-%{pk_project}
Version:        1.2.0
Release:        2%{?dist}
Summary:        Constraint for testing strings considering not-same line endings

License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
# git snapshot to get upstream test suite
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
%if %{with_tests}
# For tests
BuildRequires:  php(language) >= 5.5
BuildRequires:  php-pcre
# From composer.json,     "require-dev": {
#        "johnkary/phpunit-speedtrap": "^1.1 || ^2.0 || ^3.0",
#        "symfony/phpunit-bridge": "^3.2.2 || ^4.0"
# ignore phpunit listeners
BuildRequires: (php-composer(phpunitgoodpractices/polyfill) >= 1.4   with php-composer(phpunitgoodpractices/polyfill) < 2)
%if 0%{?fedora} >= 31 || 0%{?rhel} >= 9
BuildRequires:  phpunit9
%endif
BuildRequires:  phpunit8
BuildRequires:  phpunit7 >= 7.5.20
BuildRequires:  phpunit6 >= 6.5.14
BuildRequires:  phpunit  >= 5.7.27
# Autoloader
BuildRequires:  php-fedora-autoloader-devel
%endif

# From composer.json,     "require": {
#        "php": "^5.5 || ^7.0 || ^8.0",
#        "phpunit/phpunit": "^5.7.27 || ^6.5.14 || ^7.5.20 || ^8.0 || ^9.0",
#        "phpunitgoodpractices/polyfill": "^1.4"
Requires:       php(language) >= 5.5
Requires:      (php-composer(phpunitgoodpractices/polyfill) >= 1.4   with php-composer(phpunitgoodpractices/polyfill) < 2)
# ignore phpunit dep, package using it will run the proper phpunit command (and autoloader)
# From phpcompatinfo report for version 1.0.0
Requires:       php-pcre
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}


%description
Constraint for testing strings considering not-same line endings.

Autoloader: %{php_home}/%{ns_vendor}/%{ns_project}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}


%build
: Generate a simple classmap autoloader
phpab --template fedora --output src/autoload.php src
cat << 'EOF' | tee -a src/autoload.php

\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/PHPUnitGoodPractices/Polyfill/autoload.php',
    __DIR__ . '/Constraint/IsIdenticalString.php',
]);
EOF


%install
: Library
mkdir -p   %{buildroot}%{php_home}/%{ns_vendor}
cp -pr src %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}


%check
%if %{with_tests}
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require '%{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}/autoload.php';
EOF

: Disable the listeners
sed -e '/<listeners>/,/<\/listeners>/d' phpunit.xml.dist >phpunit.xml

: Run upstream test suite with each available phpunit version
ret=0
if [ -x %{_bindir}/phpunit ]; then
  for cmd in php php72 php73 php74; do
    if which $cmd; then
      $cmd %{_bindir}/phpunit --verbose || ret=1
    fi
  done
fi
if [ -x %{_bindir}/phpunit6 ]; then
  for cmd in php php72 php73 php74; do
    if which $cmd; then
      $cmd %{_bindir}/phpunit6 --verbose || ret=1
    fi
  done
fi
if [ -x %{_bindir}/phpunit7 ]; then
  for cmd in php php72 php73 php74; do
    if which $cmd; then
      $cmd %{_bindir}/phpunit7 --verbose || ret=1
    fi
  done
fi
if [ -x %{_bindir}/phpunit8 ]; then
  for cmd in php php72 php73 php74; do
    if which $cmd; then
      $cmd %{_bindir}/phpunit8 --verbose || ret=1
    fi
  done
fi
if [ -x %{_bindir}/phpunit9 ]; then
  for cmd in php php73 php74 php80; do
    if which $cmd; then
      $cmd %{_bindir}/phpunit9 --verbose || ret=1
    fi
  done
fi
exit $ret
%else
: Test suite disabled
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc composer.json
%dir %{php_home}/%{ns_vendor}
     %{php_home}/%{ns_vendor}/%{ns_project}


%changelog
* Tue Oct 20 2020 Remi Collet <remi@remirepo.net> - 1.2.0-2
- update to 1.2.0
- raise dependency on phpunitgoodpractices/polyfill 1.4
- allow PHPUnit 9
- switch to classmap autoloader

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 26 2019 Remi Collet <remi@remirepo.net> - 1.1.0-1
- update to 1.1.0
- raise dependency on phpunitgoodpractices/polyfill 1.1
- allow PHPUnit 8

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 11 2018 Remi Collet <remi@remirepo.net> - 1.0.1-1
- update to 1.0.1 (no change)

* Mon Jun  4 2018 Remi Collet <remi@remirepo.net> - 1.0.0-1
- initial package, version 1.0.0
- https://github.com/PHP-CS-Fixer/phpunit-constraint-isidenticalstring/issues/1
  phpunit schema

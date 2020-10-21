# remirepo/fedora spec file for php-gecko-packages-gecko-php-unit3
#
# Copyright (c) 2016-2018 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global gh_commit    8b0320158e34c3d85e5133c341d55c4d6ec5e927
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
#global gh_date      20150717
%global gh_owner     GeckoPackages
%global gh_project   GeckoPHPUnit
%global pk_owner     gecko-packages
%global pk_project   gecko-php-unit
%global php_home     %{_datadir}/php
%global major        3
%global with_tests   0%{!?_without_tests:1}

Name:           php-%{pk_owner}-%{pk_project}%{major}
Version:        3.1.1
Release:        6%{?gh_date:.%{gh_date}git%{gh_short}}%{?dist}
Summary:        Additional PHPUnit asserts and constraints

License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
# git snapshot to get upstream test suite
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
%if %{with_tests}
# For tests
BuildRequires:  php(language) >= 7.0
BuildRequires:  php-dom
BuildRequires:  php-libxml
BuildRequires:  php-pcre
BuildRequires:  php-spl
# From composer.json,     "require-dev": {
#        "phpunit/phpunit": "^6.0"
BuildRequires:  phpunit6
# Autoloader
BuildRequires:  php-composer(fedora/autoloader)
%endif

# From composer.json,     "require": {
#        "php": "^7.0"
Requires:       php(language) >= 7.0
# From phpcompatinfo report for version 3.0
Requires:       php-dom
Requires:       php-libxml
Requires:       php-pcre
Requires:       php-spl
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_owner}/%{pk_project}) = %{version}


%description
Provides additional asserts to be used in PHPUnit tests.
The asserts are provided using Traits so no changes are needed
in the hierarchy of test classes.

Autoloader: %{php_home}/GeckoPackages/PHPUnit%{major}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}

cat << 'EOF' | tee src/PHPUnit/autoload.php
<?php
/* Autoloader for friendsofphp/php-cs-fixer and its dependencies */

require_once '%{php_home}/Fedora/Autoloader/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('GeckoPackages\\PHPUnit\\', __DIR__);

EOF


%build
# Empty build section, most likely nothing required.


%install
mkdir -p           %{buildroot}%{php_home}/GeckoPackages
cp -pr src/PHPUnit %{buildroot}%{php_home}/GeckoPackages/PHPUnit%{major}


%check
%if %{with_tests}
mkdir vendor
ln -s %{buildroot}%{php_home}/GeckoPackages/PHPUnit%{major}/autoload.php vendor/autoload.php

: Fix paths in unit tests
for unit in $(find tests -name \*Test.php -print); do
  sed -e 's:PHPUnit/tests:tests:' -i $unit
done

ret=0
for cmd in php php70 php71 php72; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit6 --verbose || ret=1
  fi
done
exit $ret
%else
: Test suite disabled
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc composer.json
%doc *.md
%dir %{php_home}/GeckoPackages
     %{php_home}/GeckoPackages/PHPUnit%{major}


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Feb  6 2018 Remi Collet <remi@remirepo.net> - 3.1.1-1
- Update to 3.1.1

* Thu Jan 25 2018 Remi Collet <remi@remirepo.net> - 3.1-1
- Update to 3.1

* Fri Nov  3 2017 Remi Collet <remi@remirepo.net> - 3.0-1
- Update to 3.0
- rename to php-gecko-packages-gecko-php-unit3
- raise dependency on PHP 7.0
- raise dependency on PHPUnit 6

* Thu Aug 24 2017 Remi Collet <remi@remirepo.net> - 2.2-1
- Update to 2.2

* Wed Jun 28 2017 Remi Collet <remi@remirepo.net> - 2.1-1
- Update to 2.1

* Thu Dec  1 2016 Remi Collet <remi@fedoraproject.org> - 2.0.0-1
- initial package, version 2.0.0


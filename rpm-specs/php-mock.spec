# remirepo/fedora spec file for php-mock
#
# Copyright (c) 2016-2017 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global gh_commit    bfa2d17d64dbf129073a7ba2051a96ce52749570
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     php-mock
%global gh_project   php-mock
%global with_tests   0%{!?_without_tests:1}

Name:           php-mock
Version:        1.0.1
Release:        10%{?dist}
Summary:        PHP-Mock can mock built-in PHP functions

License:        WTFPL
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{gh_project}-%{version}-%{gh_short}.tar.gz

BuildArch:      noarch
BuildRequires:  php(language) >= 5.5
%if %{with_tests}
# from composer.json, "require-dev": {
#        "phpunit/phpunit": "^4|^5"
BuildRequires:  php-composer(phpunit/php-text-template) <  2
BuildRequires:  php-composer(phpunit/php-text-template) >= 1
BuildRequires:  php-composer(phpunit/phpunit) > 4
%endif
# For autoloader
BuildRequires: php-composer(fedora/autoloader)

# from composer.json, "require": {
#        "php": ">=5.5",
#        "phpunit/php-text-template": "^1"
Requires:       php(language) >= 5.5
Requires:       php-composer(phpunit/php-text-template) >= 1
Requires:       php-composer(phpunit/php-text-template) <  2
# From phpcompatinfo report from version 1.0.1
Requires:       php-date
Requires:       php-reflection
Requires:       php-spl
# For autoloader
Requires:       php-composer(fedora/autoloader)
%if 0%{?fedora} > 21
# from composer.json, "suggest": {
#        "php-mock/php-mock-phpunit": "Allows integration into PHPUnit testcase with the trait PHPMock.",
#        "php-mock/php-mock-mockery": "Allows using PHPMockery for Mockery integration"
Suggests:       php-composer(php-mock/php-mock-phpunit)
Suggests:       php-composer(php-mock/php-mock-mockery)
%endif

Provides:       php-composer(%{gh_owner}/%{gh_project}) = %{version}


%description
PHP-Mock can mock built-in PHP functions (e.g. time()).
PHP-Mock relies on PHP's namespace fallback policy.
No further extension is needed.

Autoloader: %{_datadir}/php/phpmock/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}

: Create autoloader
cat << 'AUTOLOAD' | tee classes/autoload.php
<?php
/* Autoloader for %{name} and its dependencies */
require_once '%{_datadir}/php/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('phpmock\\', __DIR__);
\Fedora\Autoloader\Dependencies::required(array(
    '%{_datadir}/php/Text/Template/Autoload.php',
));
AUTOLOAD

cat << 'AUTOLOAD' | tee tests/unit/autoload.php
<?php
/* Autoloader for %{name} tests */

require_once '%{_datadir}/php/phpmock/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('phpmock\\', __DIR__);
AUTOLOAD


%build
# Nothing


%install
# Library
mkdir -p          %{buildroot}%{_datadir}/php/
cp -pr classes    %{buildroot}%{_datadir}/php/phpmock

# Unit tests
mkdir -p          %{buildroot}%{_datadir}/tests
cp -pr tests/unit %{buildroot}%{_datadir}/tests/phpmock


%check
%if %{with_tests}
# TODO: local build fails, build in mock is ok
ret=0
for cmd in php php56 php70 php71 php72; do
  if which $cmd; then
    %{_bindir}/phpunit --bootstrap %{buildroot}%{_datadir}/php/phpmock/autoload.php --verbose || ret=1
  fi
done
exit $ret
%else
: bootstrap build with test suite disabled
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc composer.json
%doc *.md
%{_datadir}/php/phpmock
%{_datadir}/tests/phpmock


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu May 11 2017 Remi Collet <remi@remirepo.net> - 1.0.1-4
- switch to fedora/autoloader

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Feb 22 2016 Remi Collet <remi@fedoraproject.org> - 1.0.1-2
- Fix: license is WTFPL, from review #1306968

* Fri Feb 12 2016 Remi Collet <remi@fedoraproject.org> - 1.0.1-1
- initial package
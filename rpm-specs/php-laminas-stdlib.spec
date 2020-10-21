# remirepo/Fedora spec file for php-laminas-stdlib
#
# Copyright (c) 2015-2020 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%bcond_with          bootstrap
%if %{with bootstrap}
%bcond_with          tests
%else
%bcond_without       tests
%endif

%global gh_commit    b9d84eaa39fde733356ea948cdef36c631f202b6
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     laminas
%global gh_project   laminas-stdlib
%global zf_name      zend-stdlib
%global php_home     %{_datadir}/php
%global namespace    Laminas
%global library      Stdlib

Name:           php-%{gh_project}
Version:        3.3.0
Release:        1%{?dist}
Summary:        Laminas Framework %{library} component

License:        BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{gh_commit}/%{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
# Tests
%if %{with tests}
BuildRequires:  php(language) >= 7.3
BuildRequires: (php-composer(%{gh_owner}/laminas-zendframework-bridge) >= 1.0 with php-composer(%{gh_owner}/laminas-zendframework-bridge) < 2)
BuildRequires:  php-iconv
BuildRequires:  php-intl
BuildRequires:  php-mbstring
BuildRequires:  php-pcre
BuildRequires:  php-posix
BuildRequires:  php-spl
# From composer, "require-dev": {
#        "laminas/laminas-coding-standard": "~1.0.0",
#        "phpbench/phpbench": "^0.17.1",
#        "phpunit/phpunit": "^9.3.7"
%global phpunit %{_bindir}/phpunit9
BuildRequires:  phpunit9 >= 9.3.7
# Autoloader
BuildRequires:  php-fedora-autoloader-devel
%endif

# From composer, "require": {
#        "php": "^7.3 || ^8.0",
#        "laminas/laminas-zendframework-bridge": "^1.0"
Requires:       php(language) >= 7.3
Requires:      (php-composer(%{gh_owner}/laminas-zendframework-bridge) >= 1.0 with php-composer(%{gh_owner}/laminas-zendframework-bridge) < 2)
# From phpcompatinfo report for version 3.2.1
Requires:       php-iconv
Requires:       php-intl
Requires:       php-mbstring
Requires:       php-pcre
Requires:       php-posix
Requires:       php-spl
# Autoloader
Requires:       php-composer(fedora/autoloader)

# Compatibily ensure by the bridge
Obsoletes:      php-zendframework-%{zf_name}              < 3.2.2
Provides:       php-zendframework-%{zf_name}              = %{version}
Provides:       php-composer(%{gh_owner}/%{gh_project})   = %{version}
Provides:       php-composer(zendframework/%{zf_name})    = %{version}
Provides:       php-autoloader(%{gh_owner}/%{gh_project}) = %{version}
Provides:       php-autoloader(zendframework/%{zf_name})  = %{version}


%description
%{gh_project} is a set of components that implements general purpose utility
class for different scopes like:
* array utilities functions;
* general messaging systems;
* string wrappers;
* etc.

https://docs.laminas.dev/%{gh_project}/


%prep
%setup -q -n %{gh_project}-%{gh_commit}

mv LICENSE.md LICENSE


%build
phpab --template fedora --output src/autoload.php src

cat << 'EOF' | tee zf.php
<?php
require_once '%{php_home}/Fedora/Autoloader/autoload.php';
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/%{namespace}/ZendFrameworkBridge/autoload.php',
    dirname(dirname(__DIR__)) . '/%{namespace}/%{library}/autoload.php',
]);
EOF


%install
: Laminas library
mkdir -p   %{buildroot}%{php_home}/%{namespace}/
cp -pr src %{buildroot}%{php_home}/%{namespace}/%{library}

: Zend equiv
mkdir -p      %{buildroot}%{php_home}/Zend/%{library}
cp -pr zf.php %{buildroot}%{php_home}/Zend/%{library}/autoload.php


%check
%if %{with tests}
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require_once '%{buildroot}%{php_home}/%{namespace}/%{library}/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('%{namespace}Test\\%{library}\\', dirname(__DIR__) . '/test');
EOF

: upstream test suite
ret=0
for cmdarg in "php %{phpunit}" php73 php74 php80; do
  if which $cmdarg; then
    set $cmdarg
    $1 ${2:-%{_bindir}/phpunit9} --verbose || ret=1
  fi
done

: check compat autoloader
php -r '
require "%{buildroot}%{php_home}/Zend/%{library}/autoload.php";
exit (class_exists("\\Zend\\Stdlib\\ConsoleHelper") ? 0 : 1);
'

exit $ret
%else
: Test suite disabled
%endif


%files
%license LICENSE
%doc *.md
%doc composer.json
%{php_home}/Zend/%{library}
%{php_home}/%{namespace}/%{library}


%changelog
* Tue Aug 25 2020 Remi Collet <remi@remirepo.net> - 3.3.0-1
- update to 3.3.0
- raise dependency on PHP 7.3
- switch to phpunit 9.3

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Remi Collet <remi@remirepo.net> - 3.2.1-3
- cleanup

* Mon Jan  6 2020 Remi Collet <remi@remirepo.net> - 3.2.1-2
- switch to Laminas

* Wed Aug 29 2018 Remi Collet <remi@remirepo.net> - 3.2.1-1
- update to 3.2.1

* Mon Aug 27 2018 Remi Collet <remi@remirepo.net> - 3.2.0-2
- add patch for PHP 7.3 from
  https://github.com/zendframework/zend-stdlib/pull/93

* Wed May  2 2018 Remi Collet <remi@remirepo.net> - 3.2.0-1
- update to 3.2.0
- switch to phpunit6 or phpunit7

* Mon Apr 16 2018 Remi Collet <remi@remirepo.net> - 3.1.1-1
- update to 3.1.1

* Thu Nov 23 2017 Remi Collet <remi@fedoraproject.org> - 3.1.0-6
- provide php-autoloader(zendframework/zend-stdlib)

* Thu Nov 23 2017 Remi Collet <remi@fedoraproject.org> - 3.1.0-5
- switch from zend-loader to fedora/autoloader

* Tue Oct 24 2017 Remi Collet <remi@fedoraproject.org> - 3.1.0-4
- fix FTBFS from Koschei, add patch for PHP 7.2 from
  https://github.com/zendframework/zend-stdlib/pull/81

* Tue Sep 13 2016 Remi Collet <remi@fedoraproject.org> - 3.1.0-1
- update to 3.1.0
- raise dependency on PHP >= 5.6

* Wed Jun 29 2016 Remi Collet <remi@fedoraproject.org> - 3.0.1-1
- update to 3.0.1 for ZendFramework 3
- drop dependency on zend-hydrator

* Wed Apr 13 2016 Remi Collet <remi@fedoraproject.org> - 2.7.7-1
- update to 2.7.7

* Fri Feb 19 2016 Remi Collet <remi@fedoraproject.org> - 2.7.6-1
- update to 2.7.6
- raise dependency on zendframework/zend-hydrator >= 1.1

* Tue Feb 16 2016 Remi Collet <remi@fedoraproject.org> - 2.7.5-1
- update to 2.7.5

* Thu Jan 28 2016 Remi Collet <remi@fedoraproject.org> - 2.7.4-1
- update to 2.7.4
- add dependency on zendframework/zend-hydrator ^1.0.0

* Tue Aug  4 2015 Remi Collet <remi@fedoraproject.org> - 2.5.2-1
- initial package

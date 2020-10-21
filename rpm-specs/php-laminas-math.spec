# remirepo/Fedora spec file for php-laminas-math
#
# Copyright (c) 2015-2020 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global bootstrap    0
%global gh_commit    dd603c7d151d46eafd243a405d5b7eefa4222d74
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     laminas
%global gh_project   laminas-math
%global zf_name      zend-math
%global php_home     %{_datadir}/php
%global namespace    Laminas
%global library      Math
%if %{bootstrap}
%global with_tests   0%{?_with_tests:1}
%else
%global with_tests   0%{!?_without_tests:1}
%endif

Name:           php-%{gh_project}
Version:        3.2.0
Release:        4%{?dist}
Summary:        Laminas Framework %{library} component

License:        BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{gh_commit}/%{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

Patch0:         https://patch-diff.githubusercontent.com/raw/laminas/laminas-math/pull/2.patch

BuildArch:      noarch
# Tests
%if %{with_tests}
BuildRequires:  php(language) >= 5.6
BuildRequires:  php-mbstring
BuildRequires: (php-composer(%{gh_owner}/laminas-zendframework-bridge) >= 1.0 with php-composer(%{gh_owner}/laminas-zendframework-bridge) < 2)
BuildRequires: (php-composer(paragonie/random_compat)                  >= 2.0.11 with php-composer(paragonie/random_compat)               < 3)
BuildRequires:  php-bcmath
BuildRequires:  php-gmp
BuildRequires:  php-pcre
BuildRequires:  php-spl
# test suite hangs without (need investigation)
BuildRequires:  php-mcrypt
# From composer, "require-dev": {
#        "laminas/laminas-coding-standard": "~1.0.0",
#        "phpunit/phpunit": "^5.7.27 || ^6.5.8 || ^7.1.2"
%global phpunit %{_bindir}/phpunit7
BuildRequires:  phpunit7 >= 7.1.2
# Autoloader
BuildRequires:  php-fedora-autoloader-devel
%endif

# From composer, "require": {
#        "php": "^5.6 || ^7.0",
#        "ext-mbstring": "*",
#        "laminas/laminas-zendframework-bridge": "^1.0",
#        "paragonie/random_compat": "^2.0.11 || 9.99.99"
Requires:       php(language) >= 5.6
Requires:       php-mbstring
Requires:      (php-composer(%{gh_owner}/laminas-zendframework-bridge) >= 1.0 with php-composer(%{gh_owner}/laminas-zendframework-bridge) < 2)
Requires:      (php-composer(paragonie/random_compat)                  >= 2.0.11 with php-composer(paragonie/random_compat)               < 3)
# From phpcompatinfo report for version 3.2.0
Requires:       php-pcre
Requires:       php-spl
%if ! %{bootstrap}
# From composer, "suggest": {
#        "ext-bcmath": "If using the bcmath functionality",
#        "ext-gmp": "If using the gmp functionality",
Requires:       php-bcmath
Requires:       php-gmp
# Autoloader
Requires:       php-composer(fedora/autoloader)
%endif

# Compatibily ensure by the bridge
Obsoletes:      php-zendframework-%{zf_name}              < 3.2.0-99
Provides:       php-zendframework-%{zf_name}              = %{version}-99
Provides:       php-composer(%{gh_owner}/%{gh_project})   = %{version}
Provides:       php-composer(zendframework/%{zf_name})    = %{version}
Provides:       php-autoloader(%{gh_owner}/%{gh_project}) = %{version}
Provides:       php-autoloader(zendframework/%{zf_name})  = %{version}


%description
%{gh_project} provides general mathematical functions.
So far the supported functionalities are:
* Laminas\Math\Rand, a random number generator;
* Laminas\Math\BigInteger, a library to manage big integers.

Documentation: https://docs.laminas.dev/%{gh_project}/


%prep
%setup -q -n %{gh_project}-%{gh_commit}
%patch0 -p1 -b .pr2

mv LICENSE.md LICENSE


%build
: Create autoloader
phpab --template fedora --output src/autoload.php src
cat << 'EOF' | tee -a src/autoload.php
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/random_compat/autoload.php',
]);
EOF

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
%if %{with_tests}
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require_once '%{buildroot}%{php_home}/%{namespace}/%{library}/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('%{namespace}Test\\%{library}\\', dirname(__DIR__) . '/test');
require_once dirname(__DIR__) . '/test/TestAsset/random_bytes.php';
EOF

ret=0
for cmdarg in "php %{phpunit}" php72 php73 php74; do
  if which $cmdarg; then
    set $cmdarg
    $1 ${2:-%{_bindir}/phpunit7} --verbose || ret=1
  fi
done

: check compat autoloader
php -r '
require "%{buildroot}%{php_home}/Zend/%{library}/autoload.php";
exit (class_exists("\\Zend\\%{library}\\Rand") ? 0 : 1);
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
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Remi Collet <remi@remirepo.net> - 3.2.0-2
- cleanup

* Mon Jan  6 2020 Remi Collet <remi@remirepo.net> - 3.2.0-1
- switch to Laminas
- add patch to fix test suite from
  https://github.com/laminas/laminas-math/pull/2

* Tue Dec 11 2018 Remi Collet <remi@remirepo.net> - 3.2.0-1
- update to 3.2.0 (no change)

* Wed Jul 11 2018 Remi Collet <remi@remirepo.net> - 3.1.1-1
- update to 3.1.1

* Fri Apr 27 2018 Remi Collet <remi@remirepo.net> - 3.1.0-1
- update to 3.1.0
- raise dependency on PHP 5.6
- raise dependency on paragonie/random_compat 2.0.11
- add dependency on mbstring
- use range dependencies on F27+
- switch to phpunit6 or phpunit7

* Thu Nov 23 2017 Remi Collet <remi@fedoraproject.org> - 3.0.0-4
- switch from zend-loader to fedora/autoloader

* Wed Jun 29 2016 Remi Collet <remi@fedoraproject.org> - 3.0.0-1
- update to 3.0.0 for ZendFramework 3
- add dependencies autoloader
- add dependency on paragonie/random_compat
- drop dependency on ircmaxell/random-lib

* Fri Apr  8 2016 Remi Collet <remi@fedoraproject.org> - 2.7.0-1
- update to 2.7.0
- add mandatory dependency on ircmaxell/random-lib

* Wed Feb  3 2016 Remi Collet <remi@fedoraproject.org> - 2.6.0-1
- update to 2.6.0
- drop dependency on zend-servicemanager

* Thu Dec 17 2015 Remi Collet <remi@fedoraproject.org> - 2.5.2-1
- update to 2.5.2
- raise minimal php version to 5.5

* Tue Aug  4 2015 Remi Collet <remi@fedoraproject.org> - 2.5.1-1
- initial package

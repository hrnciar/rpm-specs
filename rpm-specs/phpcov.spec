# fedora/remirepo spec file for phpcov
#
# Copyright (c) 2013-2019 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

# For compatibility with SCL
%undefine __brp_mangle_shebangs

%global gh_commit    b91ef1640a7571f32e2eb58b107865f4c87a2eef
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sebastianbergmann
%global gh_project   phpcov
%global php_home     %{_datadir}/php
%global with_tests   0%{!?_without_tests:1}
# Packagist
%global pk_vendor    phpunit
%global pk_project   phpcov
# Namespace
%global ns_vendor    SebastianBergmann
%global ns_project   PHPCOV


Name:           %{pk_project}
Version:        7.0.2
Release:        1%{?dist}
Summary:        CLI frontend for PHP_CodeCoverage

License:        BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{name}-%{version}-%{gh_short}.tar.gz

# Fix autoload for RPM
Patch0:         %{gh_project}-rpm.patch

BuildArch:      noarch
BuildRequires:  php(language) >= 7.3
BuildRequires:  php-fedora-autoloader-devel
%if %{with_tests}
BuildRequires:  phpunit9
BuildRequires:  (php-composer(phpunit/php-code-coverage) >= 8.0   with php-composer(phpunit/php-code-coverage) < 9)
BuildRequires:  (php-composer(sebastian/diff)            >= 4     with php-composer(sebastian/diff)            < 5)
BuildRequires:  (php-composer(sebastian/finder-facade)   >= 2.0   with php-composer(sebastian/finder-facade)   < 3)
BuildRequires:  (php-composer(sebastian/version)         >= 3.0   with php-composer(sebastian/version)         < 4)
BuildRequires:  (php-composer(symfony/console)           >= 3.0   with php-composer(symfony/console)           < 6)
BuildRequires:  php-pecl(Xdebug)
%endif

# from composer.json
#        "php": "^7.3",
#        "phpunit/phpunit": "^9.0",
#        "phpunit/php-code-coverage": "^8.0",
#        "sebastian/diff": "^4.0",
#        "sebastian/finder-facade": "^2.0",
#        "sebastian/version": "^3.0",
#        "symfony/console": "^3.0 || ^4.0 || ^5.0"
Requires:       php(language) >= 7.3
Requires:       phpunit9
Requires:       (php-composer(phpunit/php-code-coverage) >= 8.0   with php-composer(phpunit/php-code-coverage) < 9)
Requires:       (php-composer(sebastian/diff)            >= 4     with php-composer(sebastian/diff)            < 5)
Requires:       (php-composer(sebastian/finder-facade)   >= 2.0   with php-composer(sebastian/finder-facade)   < 3)
Requires:       (php-composer(sebastian/version)         >= 3.0   with php-composer(sebastian/version)         < 4)
Requires:       (php-composer(symfony/console)           >= 3.0   with php-composer(symfony/console)           < 6)
# from phpcompatinfo report for version 4.0.0
# none

Obsoletes:      php-phpunit-phpcov < 4
Provides:       php-phpunit-phpcov = %{version}
Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}


%description
%{pk_project} is a command-line frontend for the PHP_CodeCoverage library.


%prep
%setup -q -n %{gh_project}-%{gh_commit}

%patch0 -p0 -b .rpm


%build
phpab \
  --template fedora \
  --output   src/autoload.php \
  src

cat << 'EOF' | tee -a src/autoload.php
// Dependencies
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/PHPUnit9/autoload.php',
    '%{php_home}/%{ns_vendor}/CodeCoverage8/autoload.php',
    '%{php_home}/%{ns_vendor}/Diff4/autoload.php',
    '%{php_home}/%{ns_vendor}/FinderFacade2/autoload.php',
    '%{php_home}/%{ns_vendor}/Version3/autoload.php',
    [
        '%{php_home}/Symfony5/Component/Console/autoload.php',
        '%{php_home}/Symfony4/Component/Console/autoload.php',
        '%{php_home}/Symfony3/Component/Console/autoload.php',
    ]
]);
EOF


%install
mkdir -p   %{buildroot}%{php_home}/%{ns_vendor}
cp -pr src %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}

install -D -p -m 755 %{pk_project} %{buildroot}%{_bindir}/%{pk_project}


%check
%if %{with_tests}
mkdir vendor
ln -s %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}/autoload.php vendor/autoload.php

if ! php -v | grep Xdebug
then EXT="-d zend_extension=xdebug.so"
fi

ret=0
for cmd in php php73 php74; do
  if which $cmd; then
    $cmd $EXT %{_bindir}/phpunit9 --verbose || ret=1
  fi
done
exit $ret;
%else
: Test suite skipped
%endif


%files
%license LICENSE
%doc README.md
%doc composer.json
%{php_home}/%{ns_vendor}/%{ns_project}
%{_bindir}/%{pk_project}


%changelog
* Thu Mar  5 2020 Remi Collet <remi@remirepo.net> - 7.0.2-1
- update to 7.0.2
- raise dependency on PHP 7.3
- raise dependency on phpunit/phpunit 9
- raise dependency on phpunit/php-code-coverage 8
- raise dependency on sebastian/diff 4
- raise dependency on sebastian/finder-facade 2
- raise dependency on sebastian/version 3
- allow Symfony 5

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 18 2019 Remi Collet <remi@remirepo.net> - 6.0.1-1
- update to 6.0.1 (no change)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb 20 2019 Remi Collet <remi@remirepo.net> - 6.0.0-1
- update to 6.0.0
- raise dependency on PHP 7.2
- raise dependency on phpunit/php-code-coverage 7
- switch from phpunit7 to phpunit8
- ensure XDebug is enabled to run the test suite

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Feb  6 2018 Remi Collet <remi@remirepo.net> - 5.0.0-1
- Update to 5.0.0
- raise dependency on PHP 7.1
- only for phpunit7
- raise dependency on phpunit/php-code-coverage 6
- raise dependency on sebastian/diff 3

* Fri Feb  2 2018 Remi Collet <remi@remirepo.net> - 4.0.5-1
- Update to 4.0.5
- allow phpunit7
- use package names on EL and Fedora < 27

* Thu Jan 18 2018 Remi Collet <remi@remirepo.net> - 4.0.4-1
- Update to 4.0.4 (no change)
- raise dependency on symfony/console 3
- use range dependency on F27

* Sun Nov 19 2017 Remi Collet <remi@remirepo.net> - 4.0.3-1
- Update to 4.0.3
- Allow Symfony 4

* Sun Oct 22 2017 Remi Collet <remi@remirepo.net> - 4.0.2-1
- Update to 4.0.2
- raise dependency on phpunit/php-code-coverage 5.2.1
- drop dependency on php-phpunit-diff
- add dependency on php-sebastian-diff2

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Apr 28 2017 Remi Collet <remi@remirepo.net> - 4.0.1-1
- Update to 4.0.1

* Mon Apr 24 2017 Remi Collet <remi@remirepo.net> - 4.0.0-2
- fix composer provide (from review #1420384)
- fix composer.json perm

* Wed Feb  8 2017 Remi Collet <remi@fedoraproject.org> - 4.0.0-1
- rename to phpcov
- update to 4.0.0
- change dependencies to PHPUnit v6

* Fri Jun  3 2016 Remi Collet <remi@fedoraproject.org> - 3.1.0-1
- Update to 3.1.0
- raise dependency on phpunit/php-code-coverage >= 4.0
- drop the autoloader template, simply generate it

* Mon Apr 18 2016 Remi Collet <remi@fedoraproject.org> - 3.0.0-3
- allow sebastian/version 2.0

* Sat Jan  9 2016 Remi Collet <remi@fedoraproject.org> - 3.0.0-1
- update to 3.0.0
- raise minimal PHP version to 5.6
- raise dependencies on phpunit ~5.0, php-code-coverage ~3.0
- allow symfony 3
- run test suite with both PHP 6 and 7 when available

* Mon Oct  5 2015 Remi Collet <remi@fedoraproject.org> - 2.0.2-1
- update to 2.0.2
- allow PHPUnit 5

* Wed Jun 25 2014 Remi Collet <remi@fedoraproject.org> - 2.0.1-1
- update to 2.0.1
- composer dependencies

* Wed Apr 30 2014 Remi Collet <remi@fedoraproject.org> - 2.0.0-1
- update to 2.0.0
- sources from github

* Thu Sep 12 2013 Remi Collet <remi@fedoraproject.org> - 1.1.0-1
- initial package

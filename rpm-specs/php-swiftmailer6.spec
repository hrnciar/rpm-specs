# remirepo/fedora spec file for php-swiftmailer6
#
# Copyright (c) 2016-2020 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please preserve changelog entries
#
%global gh_commit    149cfdf118b169f7840bbe3ef0d4bc795d1780c9
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     swiftmailer
%global gh_project   swiftmailer
# don't change major version used in package name
%global major        6
%if 0%{?fedora} >= 32 || 0%{?rhel} >= 8
# disable test by default, without mockery < 1
%global with_tests   0%{?_with_tests:1}
%else
%global with_tests   0%{!?_without_tests:1}
%endif
%global php_home     %{_datadir}/php

Name:           php-%{gh_project}%{major}
Version:        6.2.3
Release:        4%{?dist}
Summary:        Free Feature-rich PHP Mailer

License:        MIT
URL:            https://swiftmailer.symfony.com/
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{gh_project}-%{version}-%{gh_short}.tar.gz

BuildArch:      noarch
%if %{with_tests}
BuildRequires:  php(language) >= 7.0.0
BuildRequires: (php-composer(egulias/email-validator) >= 2.0  with php-composer(egulias/email-validator) <  3)
BuildRequires:  php-intl
BuildRequires:  php-reflection
BuildRequires:  php-simplexml
BuildRequires:  php-bcmath
BuildRequires:  php-date
BuildRequires:  php-filter
BuildRequires:  php-hash
BuildRequires:  php-iconv
BuildRequires:  php-mbstring
BuildRequires:  php-mhash
BuildRequires:  php-openssl
BuildRequires:  php-pcre
BuildRequires:  php-spl
BuildRequires:  phpunit6
# From composer.json, "require-dev": {
#        "mockery/mockery": "~0.9.1",
#        "symfony/phpunit-bridge": "^3.4.19|^4.1.8"
BuildRequires: (php-composer(mockery/mockery) >= 0.9.1         with php-composer(mockery/mockery) <  1)
BuildRequires: (php-composer(symfony/phpunit-bridge) >= 3.4.19 with php-composer(symfony/phpunit-bridge) <  4)
%endif
BuildRequires:  php-fedora-autoloader-devel

# From composer.json, "require": {
#        "php": ">=7.0.0",
#        "egulias/email-validator": "~2.0",
#        "symfony/polyfill-iconv": "^1.0",
#        "symfony/polyfill-mbstring": "^1.0",
#        "symfony/polyfill-intl-idn": "^1.10"
Requires:       php(language) >= 7.0.0
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
Requires:      (php-composer(egulias/email-validator) >= 2.0  with php-composer(egulias/email-validator) <  3)
%endif
# From composer.json,     "suggest": {
#        "ext-intl": "Needed to support internationalized email addresses",
#        "true/punycode": "Needed to support internationalized email addresses, if ext-intl is not installed"
Requires:       php-intl
# from phpcompatinfo report on version 6.2.0
Requires:       php-reflection
Requires:       php-simplexml
Requires:       php-bcmath
Requires:       php-date
Requires:       php-filter
Requires:       php-hash
Requires:       php-iconv
Requires:       php-mbstring
Requires:       php-mhash
Requires:       php-openssl
Requires:       php-pcre
Requires:       php-spl

Provides:       php-composer(%{gh_owner}/%{gh_project}) = %{version}


%description
Swift Mailer integrates into any web app written in PHP, offering a 
flexible and elegant object-oriented approach to sending emails with 
a multitude of features.

Autoloader: %{php_home}/Swift%{major}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}

cat << 'EOF' | tee lib/autoload.php
<?php
/* Autoloader for %{name} and its' dependencies */
require_once '%{php_home}/Egulias/EmailValidator2/autoload.php';
require_once __DIR__ . '/swift_required.php';
EOF


%build
# Empty build section, most likely nothing required.


%install
mkdir -p                   %{buildroot}/%{php_home}/Swift%{major}
cp -p  lib/*.php           %{buildroot}/%{php_home}/Swift%{major}/
cp -pr lib/classes         %{buildroot}/%{php_home}/Swift%{major}/
cp -pr lib/dependency_maps %{buildroot}/%{php_home}/Swift%{major}/


%check
%if %{with_tests}
: Use installed tree and autoloader
mkdir vendor
%{_bindir}/phpab --format fedora --output vendor/autoload.php tests
cat << 'EOF' | tee -a vendor/autoload.php
require_once '%{buildroot}/%{php_home}/Swift%{major}/autoload.php';
require_once '%{php_home}/Mockery/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('Symfony\\Bridge\\PhpUnit\\', '%{php_home}/Symfony3/Bridge/PhpUnit');
EOF

: Avoid duplicated classes
find tests -name \*.php -exec sed -e '/swift_required/d' -i {} \;

TMPDIR=$(mktemp -d $PWD/rpmtests-XXXXXXXX)
cat << EOF | tee tests/acceptance.conf.php
<?php
define('SWIFT_TMP_DIR', '$TMPDIR');
EOF

: Run upstream test suite
ret=0
for cmd in php php71 php72 php73; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit6 --exclude smoke --verbose || ret=1
  fi
done
rm -r $TMPDIR
exit $ret
%endif


%files
%license LICENSE
%doc CHANGES README.md
%doc doc
%doc composer.json
%{php_home}/Swift%{major}


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 24 2020 Remi Collet <remi@remirepo.net> - 6.2.3-3
- disable test suite where mockery < 1 is broken

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 12 2019 Remi Collet <remi@remirepo.net> - 6.2.3-1
- update to 6.2.3

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 23 2019 Remi Collet <remi@remirepo.net> - 6.2.1-1
- update to 6.2.1

* Mon Mar 11 2019 Remi Collet <remi@remirepo.net> - 6.2.0-1
- update to 6.2.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Sep 11 2018 Remi Collet <remi@remirepo.net> - 6.1.3-1
- update to 6.1.3

* Fri Jul 13 2018 Remi Collet <remi@remirepo.net> - 6.1.2-1
- update to 6.1.2

* Wed Jul  4 2018 Remi Collet <remi@remirepo.net> - 6.1.1-1
- update to 6.1.1

* Tue Jul  3 2018 Remi Collet <remi@remirepo.net> - 6.1.0-1
- update to 6.1.0
- add dependency on intl extension
- use range dependencies

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Oct  4 2017 Remi Collet <remi@remirepo.net> - 6.0.2-1
- Update to 6.0.2
- rename to php-swiftmailer6
- raise dependency on PHP 7.0
- add dependency on egulias/email-validator 2.0
- use phpunit6 for test suite

* Wed Oct  4 2017 Remi Collet <remi@remirepo.net> - 5.4.8-3
- drop unneeded dependency on php-mcrypt

* Wed May 10 2017 Remi Collet <remi@remirepo.net> - 5.4.8-1
- Update to 5.4.8

* Fri Apr 21 2017 Remi Collet <remi@remirepo.net> - 5.4.7-1
- Update to 5.4.7

* Mon Feb 13 2017 Remi Collet <remi@fedoraproject.org> - 5.4.6-1
- update to 5.4.6

* Thu Dec 29 2016 Remi Collet <remi@fedoraproject.org> - 5.4.5-1
- update to 5.4.5
- fix Remote Code Execution CVE-2016-10074

* Thu Nov 24 2016 Remi Collet <remi@fedoraproject.org> - 5.4.4-1
- update to 5.4.4

* Fri Jul  8 2016 Remi Collet <remi@fedoraproject.org> - 5.4.3-1
- update to 5.4.3
- drop patch merged upstream

* Tue Jun 14 2016 Remi Collet <remi@fedoraproject.org> - 5.4.2-2
- add patch to allow mockery 0.9.x
  open https://github.com/swiftmailer/swiftmailer/pull/769

* Mon May  2 2016 Remi Collet <remi@fedoraproject.org> - 5.4.2-1
- update to 5.4.2

* Fri Mar 25 2016 Remi Collet <remi@fedoraproject.org> - 5.4.1-2
- rebuild for remi repository

* Fri Oct 16 2015 Remi Collet <remi@fedoraproject.org> - 5.4.1-1
- initial rpm, version 5.4.1
- sources from github, pear channel is dead


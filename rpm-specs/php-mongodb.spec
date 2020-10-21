# remirepo/fedora spec file for php-mongodb
#
# Copyright (c) 2015-2019 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
# disabled for https://fedoraproject.org/wiki/Changes/MongoDB_Removal
%bcond_with          tests

%global gh_commit    b35af66631a11ee730ff1fde295f71e89f01f121
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     mongodb
#global gh_date      20151102
%global gh_project   mongo-php-library
%global psr0         MongoDB
#global prever       beta2

Name:           php-%{gh_owner}
Version:        1.7.1
%if 0%{?gh_date}
Release:        1%{gh_date}git%{gh_short}%{?dist}
%else
Release:        1%{?dist}
%endif
Summary:        MongoDB driver library

License:        ASL 2.0
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{gh_project}-%{version}%{?prever}-%{?gh_short}.tar.gz

# Autoloader
Source1:        %{name}-autoload.php
# Get rid of jean85/pretty-package-versions
Patch0:         %{name}-rpm.patch

BuildArch:      noarch
BuildRequires:  php(language) >= 7.0
BuildRequires:  php-cli
BuildRequires:  php-date
BuildRequires:  php-hash
BuildRequires:  php-json
BuildRequires:  php-spl
BuildRequires:  php-pecl(mongodb) >= 1.8
%if %{with tests}
BuildRequires:  mongodb-server >= 2.4
# From composer.json, "require-dev": {
#        "phpunit/phpunit": "^6.4 || ^8.3",
#        "sebastian/comparator": "^2.0 || ^3.0",
#        "squizlabs/php_codesniffer": "^3.5, <3.5.5",
#        "symfony/phpunit-bridge": "^4.4@dev"
%global phpunit %{_bindir}/phpunit8
BuildRequires:  %{phpunit}
%endif
# For autoloader
BuildRequires:  php-composer(fedora/autoloader)

# From composer.json, "require": {
#        "php": "^7.0"
#        "ext-hash": "*",
#        "ext-json": "*",
#        "ext-mongodb": "^1.7"
#        "jean85/pretty-package-versions": "^1.2"
Requires:       php(language) >= 7.0
Requires:       php-hash
Requires:       php-json
Requires:       php-pecl(mongodb) >= 1.8
# From phpcompatinfo report for 1.5.0
Requires:       php-date
Requires:       php-spl
# For autoloader
Requires:       php-composer(fedora/autoloader)

# Composer
Provides:       php-composer(%{gh_owner}/%{gh_owner}) = %{version}%{?prever}


%description
This library provides a high-level abstraction around the lower-level drivers
for PHP and HHVM (i.e. the mongodb extension).

While the extension provides a limited API for executing commands, queries,
and write operations, this library implements an API similar to that of the
legacy PHP driver. It contains abstractions for client, database, and
collection objects, and provides methods for CRUD operations and common
commands (e.g. index and collection management).

Autoloader: %{_datadir}/php/%{psr0}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}

cp %{SOURCE1} src/autoload.php

# Get rid of jean85/pretty-package-versions
%patch0 -p1 -b .rpm
sed -e 's/@VERSION@/%{version}/' -i src/Client.php
find src -name \*.rpm -delete
grep -F '%{version}' src/Client.php


%build
# Nothing


%install
mkdir -p   %{buildroot}%{_datadir}/php
cp -pr src %{buildroot}%{_datadir}/php/%{psr0}


%check
: Check autoloader
php -r '
require_once "%{buildroot}%{_datadir}/php/%{psr0}/autoload.php";
exit (class_exists("%{psr0}\\Client") ? 0 : 1);
'

%if %{with tests}
: Run a server
mkdir dbtest

: Choose a port to allow parallel build
port=$(php -r 'echo (27010+PHP_INT_SIZE+%{?fedora}%{?rhel});')

mongod \
  --journal \
  --logpath     $PWD/server.log \
  --pidfilepath $PWD/server.pid \
  --dbpath      $PWD/dbtest \
  --port        $port \
  --smallfiles \
  --fork

sed -e "s/27017/$port/" phpunit.xml.dist >phpunit.xml
cat << 'EOF' | tee tests/bootstrap.php
<?php
// Library
require_once '%{buildroot}%{_datadir}/php/%{psr0}/autoload.php';
// Test suite
\Fedora\Autoloader\Autoload::addPsr4('MongoDB\\Tests\\', __DIR__);
EOF

: Run the test suite
ret=0
for cmdarg in "php %{phpunit}" "php56 %{_bindir}/phpunit" php70 php71 php72; do
  if which $cmdarg; then
    set $cmdarg
    $1 ${2:-%{_bindir}/phpunit8} --verbose || ret=1
  fi
done

: Cleanup
[ -s server.pid ] && kill $(cat server.pid)

exit $ret
%else
: Test suite disabled
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc composer.json
%doc *.md
%doc docs
%{_datadir}/php/%{psr0}


%changelog
* Mon Oct 12 2020 Remi Collet <remi@remirepo.net> - 1.7.1-1
- update to 1.7.1

* Mon Aug 10 2020 Remi Collet <remi@remirepo.net> - 1.7.0-1
- update to 1.7.0
- raise dependency on PHP 7.0
- raise dependency on mongodb extension 1.8

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Feb  5 2020 Remi Collet <remi@remirepo.net> - 1.6.0-1
- update to 1.6.0
- raise dependency on mongodb extension 1.7

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 14 2020 Remi Collet <remi@remirepo.net> - 1.5.2-1
- update to 1.5.2

* Thu Nov 14 2019 Remi Collet <remi@remirepo.net> - 1.5.1-1
- update to 1.5.1

* Mon Sep  9 2019 Remi Collet <remi@remirepo.net> - 1.5.0-1
- update to 1.5.0
- raise dependency on PHP 5.6
- raise dependency on mongodb extension 1.6

* Mon Aug 19 2019 Remi Collet <remi@remirepo.net> - 1.4.3-1
- update to 1.4.3

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb  5 2019 Remi Collet <remi@remirepo.net> - 1.4.2-3
- disable test suite and so mongodb-server build dependency
  for https://fedoraproject.org/wiki/Changes/MongoDB_Removal

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Aug 24 2018 Remi Collet <remi@remirepo.net> - 1.4.2-1
- update to 1.4.2

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Remi Collet <remi@remirepo.net> - 1.4.1-1
- update to 1.4.1

* Thu Jun 28 2018 Remi Collet <remi@remirepo.net> - 1.4.0-1
- update to 1.4.0
- raise dependency on mongodb extension 1.5.0

* Fri Apr 20 2018 Remi Collet <remi@remirepo.net> - 1.3.2-1
- update to 1.3.2

* Wed Apr  4 2018 Remi Collet <remi@remirepo.net> - 1.3.1-1
- update to 1.3.1

* Fri Feb  9 2018 Remi Collet <remi@remirepo.net> - 1.3.0-1
- Update to 1.3.0
- raise dependency on mongodb extension 1.4.0

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Nov 14 2017 Remi Collet <remi@remirepo.net> - 1.2.0-1
- Update to 1.2.0
- raise dependency on PHP 5.5
- raise dependency on mongodb extension 1.3.0

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun May 14 2017 Remi Collet <remi@remirepo.net> - 1.1.2-2
- ensure fedora/autoloader is used

* Fri Feb 17 2017 Remi Collet <remi@remirepo.net> - 1.1.2-1
- update to 1.1.2

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 19 2017 Remi Collet <remi@fedoraproject.org> - 1.1.1-1
- update to 1.1.1

* Wed Dec  7 2016 Remi Collet <remi@fedoraproject.org> - 1.1.0-1
- update to 1.1.0
- raise dependency on php-pecl-mongodb 1.2.0
- switch to fedora/autoloader

* Tue Dec  6 2016 Remi Collet <remi@fedoraproject.org> - 1.0.4-1
- update to 1.0.4

* Tue Sep 27 2016 Remi Collet <remi@fedoraproject.org> - 1.0.3-1
- update to 1.0.3

* Thu Jul 28 2016 Remi Collet <remi@fedoraproject.org> - 1.0.2-2
- only run upstream test suite when build --with tests

* Thu Mar 31 2016 Remi Collet <remi@fedoraproject.org> - 1.0.2-1
- update to 1.0.2

* Sat Mar  5 2016 Remi Collet <remi@fedoraproject.org> - 1.0.1-1
- update to 1.0.1

* Fri Jan 22 2016 Remi Collet <remi@fedoraproject.org> - 1.0.0-1
- update to 1.0.0

* Mon Jan  4 2016 Remi Collet <remi@fedoraproject.org> - 1.0.0-0.4.beta2
- update to 1.0.0beta2
- raise dependency on pecl/mongodb ^1.1.1
- run test suite with both PHP 5 and 7 when available

* Tue Nov  3 2015 Remi Collet <remi@fedoraproject.org> - 1.0.0-0.3.beta1
- update to 1.0.0beta1

* Mon Nov  2 2015 Remi Collet <remi@fedoraproject.org> - 1.0.0-0.2.20151102gita3c0b97
- git snapshot

* Sat Oct 31 2015 Remi Collet <remi@fedoraproject.org> - 1.0.0-0.1.alpha1
- initial package

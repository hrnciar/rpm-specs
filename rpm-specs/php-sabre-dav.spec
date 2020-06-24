# remirepo/fedora spec file for php-sabre-dav
#
# Copyright (c) 2013-2019 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global gh_commit    a9780ce4f35560ecbd0af524ad32d9d2c8954b80
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sabre-io
%global gh_project   dav
%if 0%{?rhel} == 5
%global with_tests   0%{?_with_tests:1}
%else
%global with_tests   0%{!?_without_tests:1}
%endif

Name:           php-sabre-%{gh_project}
Summary:        WebDAV Framework for PHP
Version:        3.2.3
Release:        6%{?dist}

URL:            https://github.com/%{gh_owner}/%{gh_project}
License:        BSD
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{name}-%{version}-%{gh_short}.tar.gz
Source1:        %{name}-autoload.php

# replace composer autoloader
Patch0:         %{name}-autoload.patch
# For PHP 7.2
Patch1:         https://patch-diff.githubusercontent.com/raw/fruux/sabre-dav/pull/1006.patch
# For PHP 7.3
Patch2:         https://github.com/sabre-io/dav/commit/5eb5d74514230b11c80b67c7e147242757ccc660.patch
# For PHP 7.4
Patch3:         %{name}-php74.patch

BuildArch:      noarch
%if %{with_tests}
BuildRequires:  php(language) >= 5.5
BuildRequires: (php-composer(sabre/vobject)   >= 4.1.0  with php-composer(sabre/vobject)  < 5)
BuildRequires: (php-composer(sabre/event)     >= 2.0    with php-composer(sabre/event)    < 3)
BuildRequires: (php-composer(sabre/xml)       >= 1.4.0  with php-composer(sabre/xml)      < 2)
BuildRequires: (php-composer(sabre/http)      >= 4.2.1  with php-composer(sabre/http)     < 5)
BuildRequires: (php-composer(sabre/uri)       >= 1.0.1  with php-composer(sabre/uri)      < 2)
BuildRequires: (php-composer(psr/log)         >= 1.0.1  with php-composer(psr/log)        < 2)
BuildRequires: (php-composer(psr/log)         >= 1.0.1  with php-composer(psr/log)        < 2)
BuildRequires: (php-composer(phpunit/phpunit) >= 4.8    with php-composer(phpunit/phpunit) < 6)
BuildRequires: (php-composer(monolog/monolog) >= 1.18 with php-composer(monolog/monolog)  < 2)
BuildRequires:  php-dom
BuildRequires:  php-pcre
BuildRequires:  php-spl
BuildRequires:  php-simplexml
BuildRequires:  php-mbstring
BuildRequires:  php-ctype
BuildRequires:  php-date
BuildRequires:  php-iconv
BuildRequires:  php-libxml
BuildRequires:  php-curl
BuildRequires:  php-pdo
# From composer.json, "require-dev" : {
#        "phpunit/phpunit" : "> 4.8, <6.0.0",
#        "evert/phpdoc-md" : "~0.1.0",
#        "squizlabs/php_codesniffer": "~1.5.3"
#        "sabre/cs"        : "^1.0.0",
#        "monolog/monolog": "^1.18"

# Autoloader
BuildRequires:  php-composer(fedora/autoloader)
BuildRequires:  php-pdo_sqlite
%endif

# From composer.json,    "require": {
#        "php": ">=5.5.0",
#        "sabre/vobject": "^4.1.0",
#        "sabre/event" : ">=2.0.0, <4.0.0",
#        "sabre/xml"  : "^1.4.0",
#        "sabre/http" : "^4.2.1",
#        "sabre/uri" : "^1.0.1",
#        "ext-dom": "*",
#        "ext-pcre": "*",
#        "ext-spl": "*",
#        "ext-simplexml": "*",
#        "ext-mbstring" : "*",
#        "ext-ctype" : "*",
#        "ext-date" : "*",
#        "ext-iconv" : "*",
#        "lib-libxml" : ">=2.7.0",
#        "psr/log": "^1.0"
Requires:       php(language) >= 5.5
Requires:      (php-composer(sabre/vobject) >= 4.1.0  with php-composer(sabre/vobject) < 5)
Requires:      (php-composer(sabre/event)   >= 2.0    with php-composer(sabre/event)   < 3)
Requires:      (php-composer(sabre/xml)     >= 1.4.0  with php-composer(sabre/xml)     < 2)
Requires:      (php-composer(sabre/http)    >= 4.2.1  with php-composer(sabre/http)    < 5)
Requires:      (php-composer(sabre/uri)     >= 1.0.1  with php-composer(sabre/uri)     < 2)
Requires:      (php-composer(psr/log)       >= 1.0.1  with php-composer(psr/log)       < 2)
Requires:       php-dom
Requires:       php-pcre
Requires:       php-spl
Requires:       php-simplexml
Requires:       php-mbstring
Requires:       php-ctype
Requires:       php-date
Requires:       php-iconv
Requires:       php-libxml
# From composer.json, "suggest" : {
#        "ext-curl" : "*",
#        "ext-pdo" : "*"
Requires:       php-curl
Requires:       php-pdo
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(sabre/dav) = %{version}


%description
What is SabreDAV

SabreDAV allows you to easily add WebDAV support to a PHP application.
SabreDAV is meant to cover the entire standard, and attempts to allow
integration using an easy to understand API.

Feature list:
* Fully WebDAV compliant
* Supports Windows XP, Windows Vista, Mac OS/X, DavFSv2, Cadaver, Netdrive,
  Open Office, and probably more.
* Passing all Litmus tests.
* Supporting class 1, 2 and 3 Webdav servers.
* Locking support.
* Custom property support.
* CalDAV (tested with Evolution, iCal, iPhone and Lightning).
* CardDAV (tested with OS/X addressbook, the iOS addressbook and Evolution).
* Over 97% unittest code coverage.

Autoloader: %{_datadir}/php/Sabre/DAV/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}

%patch0 -p1 -b .rpm
%patch1 -p1
%patch2 -p1
%patch3 -p1

cp %{SOURCE1} lib/DAV/autoload.php

# drop executable as only provided as doc
chmod -x bin/*


%build
# nothing to build


%install
# Install as a PSR-0 library
mkdir -p %{buildroot}%{_datadir}/php
cp -pr lib %{buildroot}%{_datadir}/php/Sabre


%check
%if %{with_tests}
%if 0%{?rhel} == 5
sed -e 's/testMove/SKIP_testMove/' \
    -i tests/Sabre/DAV/PropertyStorage/Backend/AbstractPDOTest.php
%endif

: Fix bootstrap
cd tests
sed -e 's:@BUILDROOT@:%{buildroot}:' -i bootstrap.php

: Run upstream test suite against installed library
ret=0
for cmd in php php71 php72 php73 php74; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit \
       --filter '^((?!(testRequireAuth)).)*$'  \
       || ret=1
  fi
done
exit $ret
%else
: Skip upstream test suite
%endif


%files
%license LICENSE
%doc *md
%doc composer.json
%doc examples bin
%{_datadir}/php/Sabre/DAV
%{_datadir}/php/Sabre/DAVACL
%{_datadir}/php/Sabre/CalDAV
%{_datadir}/php/Sabre/CardDAV


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Oct 11 2019 Remi Collet <remi@remirepo.net> - 3.2.3-5
- add patch for PHP 7.4 backported from v4

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul  1 2019 Remi Collet <remi@remirepo.net> - 3.2.3-3
- change autoloader order to ensure same versions are used

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan  9 2019 Remi Collet <remi@remirepo.net> - 3.2.3-1
- update to 3.2.3

* Mon Oct 15 2018 Remi Collet <remi@remirepo.net> - 3.2.2-7
- add upstream patch for PHP 7.3

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun  5 2018 Remi Collet <remi@remirepo.net> - 3.2.2-5
- use range dependencies on F27+
- ignore 1 test failing with sabre/http 4.2.4
- fix project URL

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Oct  6 2017 Remi Collet <remi@remirepo.net> - 3.2.2-3
- add patch for PHP 7.2 from https://github.com/fruux/sabre-dav/pull/1006

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Feb 15 2017 Remi Collet <remi@fedoraproject.org> - 3.2.2-1
- update to 3.2.2
- raise dependency on PHP version 5.5
- raise dependency on sabre/vobject version 4.1
- raise dependency on sabre/xml version 1.4
- raise dependency on sabre/http version 4.2.1
- raise dependency on sabre/uri version 1.0.1
- add dependency on psr/log

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Nov 23 2016 Remi Collet <remi@fedoraproject.org> - 3.0.9-3
- add upstream patch to fix FTBFS with php 7.1

* Sat Oct 29 2016 Remi Collet <remi@fedoraproject.org> - 3.0.9-2
- switch from symfony/class-loader to fedora/autoloader

* Thu Apr  7 2016 Remi Collet <remi@fedoraproject.org> - 3.0.9-1
- update to 3.0.9

* Wed Mar 23 2016 Remi Collet <remi@fedoraproject.org> - 3.0.8-1
- update to 3.0.8

* Mon Mar 21 2016 Remi Collet <remi@fedoraproject.org> - 3.0.7-2
- provide missing php-composer(sabre/dav)

* Fri Mar 11 2016 Remi Collet <remi@fedoraproject.org> - 3.0.7-1
- update to 3.0.7
- add dependency on sabre/xml
- add dependency on sabre/uri
- raise dependency on sabre/http >= 4
- run test suite with both PHP 5 and 7 when available

* Wed Feb 24 2016 James Hogarth <james.hogarth@gmail.com> - 2.1.6-1
- update to 2.1.6

* Wed Feb 24 2016 Remi Collet <remi@fedoraproject.org> - 2.1.5-1
- update to 2.1.5

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Mar 06 2015 Adam Williamson <awilliam@redhat.com> - 1.8.12-1
- update to 1.8.12 (bugfix release, no bc breaks)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 22 2014 Remi Collet <remi@fedoraproject.org> - 1.8.10-1
- update to 1.8.10

* Sun Mar  2 2014 Remi Collet <remi@fedoraproject.org> - 1.8.9-1
- update to 1.8.9

* Thu Feb 20 2014 Remi Collet <remi@fedoraproject.org> - 1.8.8-2
- drop max version for VObject

* Tue Feb 11 2014 Remi Collet <remi@fedoraproject.org> - 1.8.8-1
- update to 1.8.8

* Tue Dec 31 2013 Remi Collet <remi@fedoraproject.org> - 1.8.7-1
- Initial packaging

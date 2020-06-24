# remirepo/fedora spec file for php-sabre-http
#
# Copyright (c) 2013-2019 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global gh_commit    acccec4ba863959b2d10c1fa0fb902736c5c8956
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sabre-io
%global gh_project   http
#global prever       alpha6
%global with_tests   %{?_without_tests:0}%{!?_without_tests:1}

Name:           php-sabre-%{gh_project}
Summary:        Library for dealing with http requests and responses
Version:        4.2.4
Release:        8%{?dist}

URL:            https://github.com/%{gh_owner}/%{gh_project}
License:        BSD
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{name}-%{version}-%{gh_short}.tar.gz
Source1:        %{name}-autoload.php

Patch0:         %{name}-php74.patch

BuildArch:      noarch
%if %{with_tests}
BuildRequires:  php(language) > 5.4
BuildRequires:  php-mbstring
BuildRequires:  php-ctype
BuildRequires:  php-composer(phpunit/phpunit)
BuildRequires: (php-composer(sabre/event) >= 2.0.2 with php-composer(sabre/event) < 4)
BuildRequires: (php-composer(sabre/uri)   >= 1.0   with php-composer(sabre/uri)   < 2)
BuildRequires:  php-curl
BuildRequires:  php-date
BuildRequires:  php-hash
BuildRequires:  php-pcre
BuildRequires:  php-spl
BuildRequires:  php-xml
# Autoloader
BuildRequires:  php-composer(fedora/autoloader)
%endif

# From composer.json, "require" : {
#        "php"          : ">=5.4",
#        "ext-mbstring" : "*",
#        "ext-ctype"    : "*",
#        "sabre/event"  : ">=1.0.0,<4.0.0",
# => use 2.0.2 for autoloader
#        "sabre/uri"    : "~1.0"
Requires:       php(language) > 5.4
Requires:       php-mbstring
Requires:       php-ctype
Requires:      (php-composer(sabre/event) >= 2.0.2 with php-composer(sabre/event) < 4)
Requires:      (php-composer(sabre/uri)   >= 1.0   with php-composer(sabre/uri)   < 2)
# From composer.json, "suggest" : {
#        "ext-curl" : " to make http requests with the Client class"
Requires:       php-curl
# From phpcompatinfo report for version 3.0.5
Requires:       php-date
Requires:       php-hash
Requires:       php-pcre
Requires:       php-spl
Requires:       php-xml
# Autoloader
Requires:       php-composer(fedora/autoloader)

# Was split from php-sabre-dav in version 1.9
Conflicts:      php-sabre-dav < 1.9

Provides:       php-composer(sabre/http) = %{version}


%description
This library provides a toolkit to make working with the HTTP protocol easier.

Most PHP scripts run within a HTTP request but accessing information about
the HTTP request is cumbersome at least, mainly do to superglobals and the
CGI standard.

There's bad practices, inconsistencies and confusion.
This library is effectively a wrapper around the following PHP constructs:

For Input:
    $_GET
    $_POST
    $_SERVER
    php://input or $HTTP_RAW_POST_DATA.

For output:
    php://output or echo.
    header()

What this library provides, is a Request object, and a Response object.
The objects are extendable and easily mockable.

Autoloader: %{_datadir}/php/Sabre/HTTP/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}
%patch0 -p1

cp %{SOURCE1} lib/autoload.php


%build
# nothing to build


%install
# Install as a PSR-0 library
mkdir -p %{buildroot}%{_datadir}/php/Sabre
cp -pr lib %{buildroot}%{_datadir}/php/Sabre/HTTP


%check
%if %{with_tests}
cd tests

: Run upstream test suite against installed library
ret=0
for cmd in php php71 php72 php73 php74; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit --bootstrap=%{buildroot}%{_datadir}/php/Sabre/HTTP/autoload.php --verbose || ret=1
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
%{_datadir}/php/Sabre/HTTP


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Oct 11 2019 Remi Collet <remi@remirepo.net> - 4.2.4-7
- improve patch for PHP 7.4

* Thu Oct 10 2019 Remi Collet <remi@remirepo.net> - 4.2.4-6
- add patch for PHP 7.4

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul  5 2019 Remi Collet <remi@remirepo.net> - 4.2.4-4
- fix autoloader

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun  5 2018 Remi Collet <remi@remirepo.net> - 4.2.4-1
- update to 4.2.4
- use range dependencies on F27+

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 12 2017 Remi Collet <remi@remirepo.net> - 4.2.3-1
- Update to 4.2.3

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan  4 2017 Remi Collet <remi@fedoraproject.org> - 4.2.2-1
- update to 4.2.2

* Sat Oct 29 2016 Remi Collet <remi@fedoraproject.org> - 4.2.1-2
- switch from symfony/class-loader to fedora/autoloader

* Fri Mar 11 2016 Remi Collet <remi@fedoraproject.org> - 4.2.1-1
- update to 4.2.1
- add dependency on sabre/uri
- run test suite with both PHP 5 and 7 when available

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jul 20 2015 Remi Collet <remi@fedoraproject.org> - 3.0.5-1
- update to 3.0.5
- add autoloader

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jul 16 2014 Remi Collet <remi@fedoraproject.org> - 2.0.4-1
- update to 2.0.4
- composer dependencies

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May  6 2014 Remi Collet <remi@fedoraproject.org> - 2.0.3-1
- update to 2.0.3

* Tue Feb 11 2014 Remi Collet <remi@fedoraproject.org> - 2.0.2-1
- update to 2.0.2

* Sat Jan 11 2014 Remi Collet <remi@fedoraproject.org> - 2.0.1-1
- update to 2.0.1

* Tue Jan  7 2014 Remi Collet <remi@fedoraproject.org> - 2.0.0-0.2.alpha6
- update to 2.0.0alpha6
- add explicit conflicts with php-sabre-dav < 1.9

* Tue Dec 31 2013 Remi Collet <remi@fedoraproject.org> - 2.0.0-0.1.alpha5
- Initial packaging

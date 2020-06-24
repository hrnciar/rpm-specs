# remirepo/fedora spec file for php-sabre-uri
#
# Copyright (c) 2016-2019 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global gh_commit    ada354d83579565949d80b2e15593c2371225e61
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sabre-io
%global gh_project   uri
%global with_tests   0%{!?_without_tests:1}

Name:           php-sabre-%{gh_project}
Summary:        Functions for making sense out of URIs
Version:        1.2.1
Release:        9%{?dist}

URL:            https://github.com/%{gh_owner}/%{gh_project}
License:        BSD
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{name}-%{version}-%{gh_short}.tar.gz
Source1:        %{name}-autoload.php

BuildArch:      noarch
%if %{with_tests}
BuildRequires:  php(language) > 5.4.7
# From composer.json, "require-dev": {
#        "sabre/cs": "~1.0.0",
#        "phpunit/phpunit" : ">=4.0,<6.0"
BuildRequires:  php-pcre
BuildRequires:  php-composer(phpunit/phpunit)
# Autoloader
BuildRequires:  php-composer(fedora/autoloader)
%endif

# From composer.json, "require" : {
#        "php": ">=5.4.7"
Requires:       php(language) > 5.4.7
# From phpcompatinfo report for version 1.1.0
Requires:       php-pcre
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(sabre/uri) = %{version}


%description
sabre/uri is a lightweight library that provides several functions for
working with URIs, staying true to the rules of RFC3986.

Partially inspired by Node.js URL library, and created to solve real
problems in PHP applications. 100% unitested and many tests are based
on examples from RFC3986.

The library provides the following functions:
* resolve to resolve relative urls.
* normalize to aid in comparing urls.
* parse, which works like PHP's parse_url.
* build to do the exact opposite of parse.
* split to easily get the 'dirname' and 'basename' of a URL without
  all the problems those two functions have.

Autoloader: %{_datadir}/php/Sabre/Uri/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}

cp %{SOURCE1} lib/autoload.php


%build
# nothing to build


%install
# Install as a PSR-0 library
mkdir -p %{buildroot}%{_datadir}/php/Sabre
cp -pr lib %{buildroot}%{_datadir}/php/Sabre/Uri


%check
%if %{with_tests}
: Run upstream test suite against installed library
cd tests
ret=0
for cmd in php php71 php72 php73 php74; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit \
      --bootstrap=%{buildroot}%{_datadir}/php/Sabre/Uri/autoload.php \
      --verbose || ret=1
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
%dir %{_datadir}/php/Sabre
     %{_datadir}/php/Sabre/Uri


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul  5 2019 Remi Collet <remi@remirepo.net> - 1.2.1-7
- fix autoloader

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun  5 2018 Remi Collet <remi@remirepo.net> - 1.2.1-4
- fix project URL

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Feb 21 2017 Remi Collet <remi@fedoraproject.org> - 1.2.1-1
- update to 1.2.1

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Oct 29 2016 Remi Collet <remi@fedoraproject.org> - 1.1.1-2
- switch from symfony/class-loader to fedora/autoloader

* Thu Oct 27 2016 Remi Collet <remi@fedoraproject.org> - 1.1.1-1
- update to 1.1.1

* Fri Mar 11 2016 Remi Collet <remi@fedoraproject.org> - 1.1.0-1
- Initial packaging

* Fri Mar 11 2016 Remi Collet <remi@fedoraproject.org> - 1.1.0-1
- Initial packaging


# remirepo/fedora spec file for php-sabre-uri2
#
# Copyright (c) 2016-2020 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%bcond_without       tests

# Github
%global gh_commit    f502edffafea8d746825bd5f0b923a60fd2715ff
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sabre-io
%global gh_project   uri
# Packagist
%global pk_vendor    sabre
%global pk_project   %{gh_project}
# Namespace
%global ns_vendor    Sabre
%global ns_project   Uri
%global major        2

Name:           php-%{pk_vendor}-%{pk_project}%{major}
Summary:        Functions for making sense out of URIs
Version:        2.2.1
Release:        1%{?dist}

URL:            https://github.com/%{gh_owner}/%{gh_project}
License:        BSD
# Git snapshot with tests, because of .gitattributes
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
%if %{with tests}
BuildRequires:  php(language) >= 7.1
# From composer.json, "require-dev": {
#        "friendsofphp/php-cs-fixer": "~2.16.1",
#        "phpstan/phpstan": "^0.12",
#        "phpunit/phpunit" : "^7.5 || ^8.5 || ^9.0"
BuildRequires:  php-pcre
%if 0%{?fedora} >= 31 || 0%{?rhel} >= 9
BuildRequires:  phpunit9
%global phpunit %{_bindir}/phpunit9
%else
BuildRequires:  phpunit8 >= 8.5
%global phpunit %{_bindir}/phpunit8
%endif
%endif
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer.json, "require" : {
#        "php": "^7.1 || ^8.0"
Requires:       php(language) > 7.1
# From phpcompatinfo report for version 2.1.2
Requires:       php-pcre
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}


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

Autoloader: %{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}

phpab -t fedora -o lib/autoload.php lib
cat << 'EOF' | tee -a lib/autoload.php

// Functions
if (!function_exists('Sabre\\Uri\\resolve')) {
    require_once __DIR__ . '/functions.php';
}
EOF

%build
# nothing to build


%install
# Install as a PSR-0 library
mkdir -p %{buildroot}%{_datadir}/php/%{ns_vendor}
cp -pr lib %{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}


%check
%if %{with tests}
: Run upstream test suite against installed library
mkdir vendor
ln -s %{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}/autoload.php vendor/autoload.php

cd tests
for cmdarg in "php %{phpunit}" "php72 %{_bindir}/phpunit8" php73 php74 php80
do
  if which $cmdarg; then
    set $cmdarg
    $1 ${2:-%{_bindir}/phpunit9} --verbose || ret=1
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
%dir %{_datadir}/php/%{ns_vendor}
     %{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}


%changelog
* Mon Oct  5 2020 Remi Collet <remi@remirepo.net> - 2.2.1-1
- update to 2.2.1
- switch to phpunit9

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Feb  1 2020 Remi Collet <remi@remirepo.net> - 2.2.0-1
- update to 2.2.0
- raise dependency on PHP 7.1
- switch to phpunit8

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 10 2019 Remi Collet <remi@remirepo.net> - 2.1.3-1
- update to 2.1.3

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul  5 2019 Remi Collet <remi@remirepo.net> - 2.1.2-2
- fix autoloader

* Mon Jul  1 2019 Remi Collet <remi@remirepo.net> - 2.1.2-1
- update to 2.1.2
- rename to php-sabre-uri2
- move to /usr/share/php/Sabre/Uri2
- raise dependency on PHP 7
- switch to classmap autoloader

* Tue Jun  5 2018 Remi Collet <remi@remirepo.net> - 1.2.1-4
- fix project URL

* Tue Feb 21 2017 Remi Collet <remi@fedoraproject.org> - 1.2.1-1
- update to 1.2.1

* Sat Oct 29 2016 Remi Collet <remi@fedoraproject.org> - 1.1.1-2
- switch from symfony/class-loader to fedora/autoloader

* Thu Oct 27 2016 Remi Collet <remi@fedoraproject.org> - 1.1.1-1
- update to 1.1.1

* Fri Mar 11 2016 Remi Collet <remi@fedoraproject.org> - 1.1.0-1
- Initial packaging


# remirepo/fedora spec file for php-webimpress-http-middleware-compatibility
#
# Copyright (c) 2020 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%global with_tests   0%{!?_without_tests:1}
# Github
%global gh_commit    8ed1c2c7523dce0035b98bc4f3a73ca9cd1d3717
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     webimpress
%global gh_project   http-middleware-compatibility
# Packagist
%global pk_vendor    %{gh_owner}
%global pk_project   %{gh_project}
%global major        %nil

Name:           php-%{pk_vendor}-%{pk_project}%{major}
Version:        0.1.4
Release:        4%{?dist}
Summary:        Compatibility library for Draft PSR-15 HTTP Middleware

License:        BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{?gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
%if %{with_tests}
BuildRequires:  php(language) >= 5.4
BuildRequires: (php-composer(http-interop/http-middleware) > 0.1.1 with php-composer(http-interop/http-middleware) < 0.6)
# For tests, from composer.json "require-dev": {
#        "phpunit/phpunit": "^5.7.23 || ^6.4.3"
BuildRequires:  phpunit6 > 6.4.3
%global phpunit %{_bindir}/phpunit6
%endif

# From composer.json, "require": {
#        "php": "^5.6 || ^7.0",
#        "http-interop/http-middleware": "^0.1.1 || ^0.2 || ^0.3 || ^0.4.1 || ^0.5",
#        "webimpress/composer-extra-dependency": "^0.2.2"
Requires:       php(language) >= 5.6
Requires:      (php-composer(http-interop/http-middleware) > 0.1.1 with php-composer(http-interop/http-middleware) < 0.6)
# From phpcompatinfo report for 0.1.4
# Only core

# Composer
Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}


%description
The purpose of the library is to deliver consistent interface for
different versions of http-interop/http-middleware which implements
Draft of PSR-15 HTTP Middleware.

Many projects currently use different version of library
http-interop/http-middleware and updating to newest version requires
usually major release. The library lets consumers of your component
decide what version of http-interop/http-middleware they want to use
and allow them to migrate to the latest version at any time.

Autoloader: %{_datadir}/php/%{pk_vendor}/%{pk_project}%{major}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}

mv LICENSE.md LICENSE


%build
cat << 'EOF' | tee autoload/autoload.php
<?php
require_once '%{_datadir}/php/Interop/Http/Middleware/autoload.php';
require_once __DIR__ . '/http-middleware.php';
EOF


%install
: Library
mkdir -p        %{buildroot}%{_datadir}/php/%{pk_vendor}/
cp -pr autoload %{buildroot}%{_datadir}/php/%{pk_vendor}/%{pk_project}%{major}


%check
%if %{with_tests}
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require '%{buildroot}%{_datadir}/php/%{pk_vendor}/%{pk_project}%{major}/autoload.php';
EOF

ret=0
for cmd in php php71 php72 php73 php74; do
   if which $cmd; then
      $cmd %{phpunit} --no-coverage --verbose || ret=1
   fi
done
exit $ret
%else
: Test suite disabled
%endif


%files
%license LICENSE
%doc composer.json
%doc *.md
%dir %{_datadir}/php/%{pk_vendor}/
     %{_datadir}/php/%{pk_vendor}/%{pk_project}%{major}


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 14 2020 Remi Collet <remi@remirepo.net> - 0.1.4-2
- own /usr/share/php/webimpress #1789783

* Fri Jan 10 2020 Remi Collet <remi@remirepo.net> - 0.1.4-1
- initial package

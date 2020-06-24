# remirepo/fedora spec file for php-sebastian-type2
#
# Copyright (c) 2019-2020 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global bootstrap    0
# github
%global gh_commit    bad49207c6f854e7a25cef0ea948ac8ebe3ef9d8
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sebastianbergmann
%global gh_project   type
# packagist
%global pk_vendor    sebastian
%global pk_project   %{gh_project}
%global major        2
# namespace
%global php_home     %{_datadir}/php
%global ns_vendor    SebastianBergmann
%global ns_project   Type
%if %{bootstrap}
%global with_tests   0%{?_with_tests:1}
%else
%global with_tests   0%{!?_without_tests:1}
%endif

Name:           php-%{pk_vendor}-%{pk_project}%{major}
Version:        2.1.0
Release:        1%{?dist}
Summary:        Collection of value objects that represent the types of the PHP type system

License:        BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
BuildRequires:  php(language) >= 7.3
BuildRequires:  php-reflection
# Autoloader
BuildRequires:  php-fedora-autoloader-devel >= 1.0.0
%if %{with_tests}
# from composer.json, "require-dev": {
#        "phpunit/phpunit": "^9.2"
# ignore min version, test suite passes with 9.1
BuildRequires:  phpunit9
%endif

# from composer.json, "require": {
#        "php": "^7.3",
Requires:       php(language) >= 7.3
# from phpcompatinfo report for version 1.0.0
Requires:       php-reflection
Requires:       php-spl
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}


%description
Collection of value objects that represent the types of the PHP type system.


%prep
%setup -q -n %{gh_project}-%{gh_commit}


%build
# Generate the Autoloader
phpab --template fedora --output src/autoload.php src

# For the test suite
phpab --template fedora --output tests/autoload.php tests/_fixture/


%install
mkdir -p   %{buildroot}%{php_home}/%{ns_vendor}
cp -pr src %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}


%check
%if %{with_tests}
mkdir vendor
cat <<EOF | tee vendor/autoload.php
<?php
require_once 'tests/autoload.php';
require_once 'tests/_fixture/callback_function.php';
EOF

: Run upstream test suite
ret=0
for cmd in php php73 php74 php80; do
  if which $cmd; then
   $cmd -d auto_prepend_file=%{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php \
     %{_bindir}/phpunit9 --verbose || ret=1
  fi
done
exit $ret
%else
: bootstrap build with test suite disabled
%endif


%files
%license LICENSE
%doc *.md
%doc composer.json
%dir %{php_home}/%{ns_vendor}
     %{php_home}/%{ns_vendor}/%{ns_project}%{major}


%changelog
* Tue Jun  2 2020 Remi Collet <remi@remirepo.net> - 2.1.0-1
- update to 2.1.0
- sources from git snapshot
- switch to phpunit9

* Fri Feb  7 2020 Remi Collet <remi@remirepo.net> - 2.0.0-1
- update to 2.0.0
- raise dependency on PHP 7.3
- rename to php-sebastian-type2
- move to /usr/share/php/SebastianBergmann/Type2

* Tue Jul  2 2019 Remi Collet <remi@remirepo.net> - 1.1.3-1
- update to 1.1.3

* Wed Jun 19 2019 Remi Collet <remi@remirepo.net> - 1.1.2-1
- update to 1.1.2

* Sat Jun  8 2019 Remi Collet <remi@remirepo.net> - 1.1.1-1
- update to 1.1.1

* Sat Jun  8 2019 Remi Collet <remi@remirepo.net> - 1.1.0-1
- update to 1.1.0

* Fri Jun  7 2019 Remi Collet <remi@remirepo.net> - 1.0.0-1
- initial package

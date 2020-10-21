# remirepo/fedora spec file for php-sebastian-code-unit
#
# Copyright (c) 2020 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%bcond_without       tests

# Sources
%global gh_commit    59236be62b1bb9919e6d7f60b0b832dc05cef9ab
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sebastianbergmann
%global gh_project   code-unit
# Packagist
%global pk_vendor    sebastian
%global pk_project   %{gh_project}
# Namespace
%global major        %nil
%global php_home     %{_datadir}/php
%global ns_vendor    SebastianBergmann
%global ns_project   CodeUnit

Name:           php-%{pk_vendor}-%{pk_project}%{major}
Version:        1.0.7
Release:        1%{?dist}
Summary:        Collection of value objects that represent the PHP code units

License:        BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
BuildRequires:  php(language) >= 7.3
BuildRequires:  php-reflection
BuildRequires:  php-spl
# Autoloader
BuildRequires:  php-fedora-autoloader-devel
%if %{with tests}
# from composer.json, "require-dev": {
#        "phpunit/phpunit": "^9.3"
BuildRequires:  phpunit9 >= 9.3
%endif

# from composer.json, "require": {
#        "php": ">=7.3"
Requires:       php(language) >= 7.3
# From phpcompatinfo report for 1.0.0
Requires:       php-reflection
Requires:       php-spl
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}


%description
Collection of value objects that represent the PHP code units.

Autoloader: %{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}


%build
# Generate the library Autoloader
%{_bindir}/phpab \
   --template fedora \
   --output src/autoload.php \
   src

# Generate the fixture Autoloader
%{_bindir}/phpab \
   --template fedora \
   --output tests/_fixture/autoload.php \
   tests/_fixture


%install
mkdir -p   %{buildroot}%{php_home}/%{ns_vendor}
cp -pr src %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}


%if %{with tests}
%check
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php

require_once dirname(__DIR__) . '/tests/_fixture/autoload.php';
require_once dirname(__DIR__) . '/tests/_fixture/file_with_multiple_code_units.php';
require_once dirname(__DIR__) . '/tests/_fixture/function.php';
EOF

: Run tests
ret=0
for cmd in php php73 php74 php80; do
  if which $cmd; then
   $cmd -d auto_prepend_file=%{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php \
     %{_bindir}/phpunit9 --verbose || ret=1
  fi
done
exit $ret
%endif


%files
%license LICENSE
%doc README.md composer.json
%dir %{php_home}/%{ns_vendor}
     %{php_home}/%{ns_vendor}/%{ns_project}%{major}


%changelog
* Sat Oct  3 2020 Remi Collet <remi@remirepo.net> - 1.0.7-1
- update to 1.0.7

* Mon Sep 28 2020 Remi Collet <remi@remirepo.net> - 1.0.6-1
- update to 1.0.6 (no change)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 29 2020 Remi Collet <remi@remirepo.net> - 1.0.5-1
- update to 1.0.5

* Tue Jun 16 2020 Remi Collet <remi@remirepo.net> - 1.0.3-1
- update to 1.0.3 (no change)
- sources from git snapshot

* Thu Apr 30 2020 Remi Collet <remi@remirepo.net> - 1.0.2-1
- update to 1.0.2

* Mon Apr 27 2020 Remi Collet <remi@remirepo.net> - 1.0.1-1
- update to 1.0.1

* Fri Apr  3 2020 Remi Collet <remi@remirepo.net> - 1.0.0-1
- initial package

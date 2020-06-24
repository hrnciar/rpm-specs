# remirepo/fedora spec file for php-phpmyadmin-twig-i18n-extension
#
# Copyright (c) 2020 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%global gh_commit    00250be43cc33e174077614807025e9e9bfc3171
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     phpmyadmin
#global gh_date      20150820
%global gh_project   twig-i18n-extension
%global with_tests   0%{!?_without_tests:1}
%global ns_vendor    PhpMyAdmin
%global ns_project   Twig
%global ns_sub       Extensions
%global major        %nil

Name:           php-%{gh_owner}-%{gh_project}%{major}
Version:        2.0.0
Release:        1%{?dist}
Summary:        Internationalization support for Twig via the gettext library

License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{name}-%{version}-%{?gh_short}.tar.gz

BuildArch:      noarch
%if %{with_tests}
BuildRequires:  php(language) >= 5.5
BuildRequires: (php-composer(twig/twig) >= 1.42.3 with php-composer(twig/twig) < 3)
# For tests, from composer.json "require-dev": {
#        "symfony/phpunit-bridge": "^4.2|^5.0"
# NOTICE: symfony/phpunit-bridge only used to pull phpunit
BuildRequires:  phpunit8
%global phpunit %{_bindir}/phpunit8
%endif
# For autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer.json, "require": {
#        "php": ">=5.5.0",
#        "twig/twig": "^1.42.3|^2.0"
Requires:       php(language) >= 5.5
Requires:      (php-composer(twig/twig) >= 1.42.3 with php-composer(twig/twig) < 3)
# From phpcompatinfo report for 2.0.0
# Only Core and standard
# For generated autoloader
Requires:       php-composer(fedora/autoloader)

# Composer
Provides:       php-composer(%{gh_owner}/%{gh_project}) = %{version}


%description
The i18n extension adds gettext support to Twig.
It defines one tag, trans.

Autoloader: %{_datadir}/php/%{ns_vendor}/%{ns_project}/%{ns_sub}%{major}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}


%build
: Create autoloader
phpab --template fedora -o src/autoload.php src
cat <<'AUTOLOAD' | tee -a src/autoload.php

\Fedora\Autoloader\Dependencies::required(array(
    [
        '%{_datadir}/php/Twig2/autoload.php',
        '%{_datadir}/php/Twig/autoload.php',
    ],
));
AUTOLOAD


%install
: Library
mkdir -p      %{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}
cp -pr src    %{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}/%{ns_sub}%{major}


%check
%if %{with_tests}
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require '%{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}/%{ns_sub}%{major}/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('%{ns_vendor}\\Tests\\%{ns_project}\\%{ns_sub}\\', dirname(__DIR__).'/tests');
EOF

: fix commands
ret=0
for cmdarg in "php %{phpunit}" php72 php73 php74; do
   if which $cmdarg; then
      set $cmdarg
      $1 ${2:-%{_bindir}/phpunit8} --no-coverage --verbose || ret=1
   fi
done
exit $ret
%else
: Test suite disabled
%endif


%files
%license LICENSE
%doc composer.json
%doc README.rst
%dir %{_datadir}/php/%{ns_vendor}
%dir %{_datadir}/php/%{ns_vendor}/%{ns_project}
     %{_datadir}/php/%{ns_vendor}/%{ns_project}/%{ns_sub}%{major}


%changelog
* Tue Jan 28 2020 Remi Collet <remi@remirepo.net> - 2.0.0-1
- initial package

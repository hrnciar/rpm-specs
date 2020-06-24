# remirepo/fedora spec file for php-phpmyadmin-motranslator5
#
# Copyright (c) 2017-2020 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%global gh_commit    d1982c7e468df332b6ff0d73fb599519140d393f
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     phpmyadmin
%global gh_project   motranslator
%global with_tests   0%{!?_without_tests:1}
%global ns_vendor    PhpMyAdmin
%global ns_project   MoTranslator
%global major        5

%global sym_min_ver 4.0
%global sym_max_ver 6

Name:           php-%{gh_owner}-%{gh_project}%{major}
Version:        5.0.0
Release:        1%{?dist}
Summary:        Translation API for PHP using Gettext MO files

Group:          Development/Libraries
License:        GPLv2+
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{name}-%{version}-%{?gh_short}.tar.gz

BuildArch:      noarch
%if %{with_tests}
BuildRequires:  php(language) >= 7.1
BuildRequires:  php-pcre
BuildRequires: (php-composer(symfony/expression-language) >= %{sym_min_ver} with php-composer(symfony/expression-language) < %{sym_max_ver})
# For tests, from composer.json "require-dev": {
#        "phpunit/php-code-coverage": "*",
#        "phpunit/phpunit": "^7.4 || ^8"
%global phpunit %{_bindir}/phpunit8
BuildRequires:  %{phpunit}
%endif
# For autoloader
BuildRequires:  php-composer(fedora/autoloader)

# From composer.json, "require": {
#        "php": "^7.1",
#        "symfony/expression-language": ""^4.0 || ^5.0"
Requires:      (php-composer(symfony/expression-language) >= %{sym_min_ver} with php-composer(symfony/expression-language) < %{sym_max_ver})
Requires:       php(language) >= 7.1
# From phpcompatinfo report for 5.0.0
Requires:       php-pcre
# For generated autoloader
Requires:       php-composer(fedora/autoloader)

# Composer
Provides:       php-composer(%{gh_owner}/%{gh_project}) = %{version}


%description
Translation API for PHP using Gettext MO files.

Features

* All strings are stored in memory for fast lookup
* Fast loading of MO files
* Low level API for reading MO files
* Emulation of Gettext API
* No use of eval() for plural equation

Limitations

* Not suitable for huge MO files which you don't want to store in memory
* Input and output encoding has to match (preferably UTF-8)

Autoloader: %{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}


%build
: Create autoloader
cat <<'AUTOLOAD' | tee src/autoload.php
<?php
/* Autoloader for %{name} and its dependencies */
require_once '%{_datadir}/php/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('%{ns_vendor}\\%{ns_project}\\', __DIR__);
\Fedora\Autoloader\Dependencies::required(array(array(
    '%{_datadir}/php/Symfony5/Component/ExpressionLanguage/autoload.php',
    '%{_datadir}/php/Symfony4/Component/ExpressionLanguage/autoload.php',
)));
AUTOLOAD


%install
: Library
mkdir -p   %{buildroot}%{_datadir}/php/%{ns_vendor}
cp -pr src %{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}


%check
%if %{with_tests}
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require '%{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}/autoload.php';
EOF

ret=0
for cmd in "php %{phpunit}" php72 php73 "php74 %{_bindir}/phpunit9"; do
  if which $cmd; then
    set $cmd
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
%doc *.md
%dir %{_datadir}/php/%{ns_vendor}/
     %{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}


%changelog
* Wed Mar  4 2020 Remi Collet <remi@remirepo.net> - 5.0.0-1
- update to 5.0.0
- rename to php-phpmyadmin-motranslator5
- move to /usr/share/php/PhpMyAdmin/MoTranslator5
- raise dependency on PHP 7.1
- raise dependency on Symfony 4 and allow Symfony 5
- switch to phpunit8

* Fri Dec  7 2018 Remi Collet <remi@remirepo.net> - 4.0-3
- use range dependencies

* Wed Feb 21 2018 Remi Collet <remi@remirepo.net> - 4.0-1
- Update to 4.0

* Mon Dec 18 2017 Remi Collet <remi@remirepo.net> - 3.4-1
- Update to 3.4
- allow Symfony 4 on F27+
- use phpunit6 on F26+

* Fri Jun  2 2017 Remi Collet <remi@remirepo.net> - 3.3-1
- Update to 3.3

* Tue May 23 2017 Remi Collet <remi@remirepo.net> - 3.2-1
- Update to 3.2

* Mon May 15 2017 Remi Collet <remi@remirepo.net> - 3.1-1
- Update to 3.1 (documentation and cleanup only)
- allow Symfony 3

* Mon Jan 23 2017 Remi Collet <remi@remirepo.net> - 3.0-1
- update to 3.0 with vendor namespace

* Sat Jan 21 2017 Remi Collet <remi@remirepo.net> - 2.2-1
- initial package


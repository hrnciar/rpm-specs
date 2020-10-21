# remirepo/fedora spec file for php-phpmyadmin-motranslator
#
# Copyright (c) 2017-2018 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%global gh_commit    fcb370254998fda7eeccfd7c787b4deb71b0d77c
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     phpmyadmin
%global gh_project   motranslator
%global with_tests   0%{!?_without_tests:1}
%global ns_vendor    PhpMyAdmin
%global ns_project   MoTranslator

%global sym_min_ver 2.8
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
%global sym_max_ver 5
%else
%global sym_max_ver 4
%endif

Name:           php-%{gh_owner}-%{gh_project}
Version:        4.0
Release:        7%{?dist}
Summary:        Translation API for PHP using Gettext MO files

License:        GPLv2+
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{name}-%{version}-%{?gh_short}.tar.gz

BuildArch:      noarch
%if %{with_tests}
BuildRequires:  php(language) >= 5.3
BuildRequires:  php-pcre
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
BuildRequires: (php-composer(symfony/expression-language) >= %{sym_min_ver} with php-composer(symfony/expression-language) < %{sym_max_ver})
%else
BuildRequires:  php-composer(symfony/expression-language) < %{sym_max_ver}
%endif
# For tests, from composer.json "require-dev": {
#        "phpunit/php-code-coverage": "*",
#        "phpunit/phpunit": "~4.8 || ~5.7 || ~6.5"
%if 0%{?fedora} >= 26 || 0%{?rhel} >= 8
%global phpunit %{_bindir}/phpunit6
%else
%global phpunit %{_bindir}/phpunit
%endif
BuildRequires:  %{phpunit}
%endif
# For autoloader
BuildRequires:  php-composer(fedora/autoloader)

# From composer.json, "require": {
#        "php": ">=5.3.0",
#        "symfony/expression-language": ""^4.0 || ^3.2 || ^2.8"
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
Requires:      (php-composer(symfony/expression-language) >= %{sym_min_ver} with php-composer(symfony/expression-language) < %{sym_max_ver})
%else
Requires:       php-composer(symfony/expression-language) < %{sym_max_ver}
%endif
Requires:       php(language) >= 5.3
# From phpcompatinfo report for 1.2
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

Autoloader: %{_datadir}/php/%{ns_vendor}/%{ns_project}/autoload.php


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
    '%{_datadir}/php/Symfony4/Component/ExpressionLanguage/autoload.php',
    '%{_datadir}/php/Symfony3/Component/ExpressionLanguage/autoload.php',
    '%{_datadir}/php/Symfony/Component/ExpressionLanguage/autoload.php',
)));
AUTOLOAD


%install
: Library
mkdir -p   %{buildroot}%{_datadir}/php/%{ns_vendor}
cp -pr src %{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}


%check
%if %{with_tests}
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require '%{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}/autoload.php';
EOF

ret=0
for cmd in "php %{phpunit}" php71 php72 php73; do
  if which $cmd; then
    set $cmd
    $1 ${2:-%{_bindir}/phpunit6} --no-coverage --verbose || ret=1
  fi
done
exit $ret
%else
: Test suite disabled
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc composer.json
%doc *.md
%dir %{_datadir}/php/%{ns_vendor}/
     %{_datadir}/php/%{ns_vendor}/%{ns_project}


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Dec  7 2018 Remi Collet <remi@remirepo.net> - 4.0-3
- use range dependencies

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 21 2018 Remi Collet <remi@remirepo.net> - 4.0-1
- Update to 4.0

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Dec 18 2017 Remi Collet <remi@remirepo.net> - 3.4-1
- Update to 3.4
- allow Symfony 4 on F27+
- use phpunit6 on F26+

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

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


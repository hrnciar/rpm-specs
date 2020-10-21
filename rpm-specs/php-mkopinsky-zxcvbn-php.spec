# remirepo/fedora spec file for php-mkopinsky-zxcvbn-php
#
# Copyright (c) 2019-2020 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
# Github
%global gh_commit    30be8030c8a3a3cfef9ec28e7210aba95a43007c
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     mkopinsky
%global gh_project   zxcvbn-php
# Packagist
%global pk_vendor    %{gh_owner}
%global pk_name      %{gh_project}
# PSR-0 namespace
#global ns_vendor    none
%global ns_project   ZxcvbnPhp
%global with_tests 0%{!?_without_tests:1}

Name:           php-%{pk_vendor}-%{pk_name}
Version:        4.4.2
Release:        4%{?dist}
Summary:        Realistic password strength estimation PHP library

License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
# Create git snapshot as tests are excluded from official tarball
Source1:        makesrc.sh

BuildArch:      noarch
BuildRequires:  php(language) >= 5.6
%if %{with_tests}
BuildRequires:  php-reflection
BuildRequires:  php-ctype
BuildRequires:  php-date
BuildRequires:  php-json
BuildRequires:  php-mbstring
BuildRequires:  php-pcre
BuildRequires:  php-spl
BuildRequires: (php-composer(symfony/polyfill-mbstring) >= 1.3.1  with php-composer(symfony/polyfill-mbstring) < 2)
# From composer.json, "require-dev": {
#        "phpunit/phpunit": "< 6.0",
#        "php-coveralls/php-coveralls": "*",
#        "squizlabs/php_codesniffer": "3.*"
BuildRequires:  php-composer(phpunit/phpunit)
%endif
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer.json, "require": {
#        "php": "^5.6 || ^7.0",
#        "symfony/polyfill-mbstring": ">=1.3.1"
Requires:       php(language) >= 5.6
# Needed for PHP < 7.2
Requires:      (php-composer(symfony/polyfill-mbstring) >= 1.3.1  with php-composer(symfony/polyfill-mbstring) < 2)
# From phpcompatifo report for 4.4.2
Requires:       php-ctype
Requires:       php-date
Requires:       php-json
Requires:       php-mbstring
Requires:       php-pcre
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_vendor}/%{pk_name}) = %{version}


%description
Zxcvbn-PHP is a password strength estimator using pattern matching and minimum
entropy calculation. Zxcvbn-PHP is based on the the Javascript zxcvbn project
from Dropbox and @lowe. "zxcvbn" is bad password, just like "qwerty" and
"123456".

Autoloader: %{_datadir}/php/%{ns_project}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}


%build
: Generate a simple autoloader
%{_bindir}/phpab -t fedora -o src/autoload.php src
cat << 'EOF' | tee -a src/autoload.php
\Fedora\Autoloader\Dependencies::required([
    '%{_datadir}/php/Symfony/Polyfill/autoload.php',
]);
EOF


%install
mkdir -p   %{buildroot}%{_datadir}/php
cp -pr src %{buildroot}%{_datadir}/php/%{ns_project}


%check
%if %{with_tests}
: Generate a simple autoloader
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
// Installed library
require '%{buildroot}%{_datadir}/php/%{ns_project}/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('ZxcvbnPhp\\Test\\', dirname(__DIR__).'/test');
EOF

: Skip known failed test
sed -e '/h1dden_26191/d' -i test/ZxcvbnTest.php
sed -e '/ertghjm/d;/qwerfdsazxcv/d' -i test/Matchers/SpatialTest.php

: Run upstream test suite
ret=0
for cmd in php php72 php73 php74; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit --verbose || ret=1
  fi
done
exit $ret
%endif


%files
%license LICENSE.txt
%doc *.md
%doc composer.json
%{_datadir}/php/%{ns_project}


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Mar  1 2019 Remi Collet <remi@remirepo.net> - 4.4.2-1
- initial package, version 4.4.2

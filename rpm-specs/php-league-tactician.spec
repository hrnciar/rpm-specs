# remirepo/fedora spec file for php-league-tactician
#
# Copyright (c) 2019 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
# Github
%global gh_commit    d0339e22fd9252fb0fa53102b488d2c514483b8a
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     thephpleague
%global gh_project   tactician
# Packagist
%global pk_vendor    league
%global pk_name      tactician
# PSR-0 namespace
%global ns_vendor    League
%global ns_project   Tactician

Name:           php-%{pk_vendor}-%{pk_name}
Version:        1.0.3
Release:        3%{?dist}
Summary:        A small, flexible command bus

License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
# Create git snapshot as tests are excluded from official tarball
Source1:        makesrc.sh

BuildArch:      noarch
BuildRequires:  php(language) >= 5.5
BuildRequires:  php-date
BuildRequires:  php-spl
# From composer.json, "require-dev": {
#        "mockery/mockery": "~0.9",
#        "phpunit/phpunit": "^4.8.35",
#        "squizlabs/php_codesniffer": "~2.3"
BuildRequires: (php-composer(mockery/mockery) >= 0.9   with php-composer(mockery/mockery) < 1)
BuildRequires:  php-composer(phpunit/phpunit) >= 4.0
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer.json, "require": {
#        "php":  ">=5.5"
Requires:       php(language) >= 5.5
# From phpcompatifo report for 1.0.3
Requires:       php-spl
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_vendor}/%{pk_name}) = %{version}


%description
A small, flexible command bus. Handy for building service layers.

Documentation: http://tactician.thephpleague.com/

Autoloader: %{_datadir}/php/%{ns_vendor}/%{ns_project}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}


%build
: Generate a simple autoloader
%{_bindir}/phpab -t fedora -o src/autoload.php src


%install
mkdir -p   %{buildroot}%{_datadir}/php/%{ns_vendor}
cp -pr src %{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}


%check
: Generate a simple autoloader
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
// Installed library
require '%{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('League\\Tactician\\Tests\\', dirname(__DIR__).'/tests');
\Fedora\Autoloader\Dependencies::required([
    dirname(__DIR__).'/tests/Fixtures/Command/CommandWithoutNamespace.php',
    '%{_datadir}/php/Mockery/autoload.php',
]);
EOF

: Run upstream test suite
ret=0
for cmd in php php70 php72 php73; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit --verbose || ret=1
  fi
done
exit $ret


%files
%license LICENSE
%doc *.md
%doc composer.json
%{_datadir}/php/%{ns_vendor}


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan  3 2019 Remi Collet <remi@remirepo.net> - 1.0.3-1
- initial package, version 1.0.3


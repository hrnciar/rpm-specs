# remirepo/fedora spec file for php-league-plates
#
# Copyright (c) 2016 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
# Github
%global gh_commit    b1684b6f127714497a0ef927ce42c0b44b45a8af
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     thephpleague
%global gh_project   plates
# Packagist
%global pk_vendor    league
%global pk_name      plates
# PSR-0 namespace
%global ns_vendor    League
%global ns_project   Plates

Name:           php-%{pk_vendor}-%{pk_name}
Version:        3.3.0
Release:        9%{?dist}
Summary:        Native PHP template system

License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
# Create git snapshot as tests are excluded from official tarball
Source1:        makesrc.sh
# Autoloader
Source2:        %{name}-autoload.php

BuildArch:      noarch
BuildRequires:  php(language) >= 5.3
BuildRequires:  php-pcre
BuildRequires:  php-spl
# From composer.json, "require-dev": {
#        "mikey179/vfsStream": "^1.4",
#        "phpunit/phpunit": "~4.0",
#        "squizlabs/php_codesniffer": "~1.5"
BuildRequires:  php-composer(mikey179/vfsStream) >= 1.4
BuildRequires:  php-composer(phpunit/phpunit) >= 4.0
# Autoloader
BuildRequires:  php-composer(fedora/autoloader)

# From composer.json, "require": {
#        "php": "^5.3 | ^7.0"
Requires:       php(language) >= 5.3
# From phpcompatifo report for 3.1.1
Requires:       php-pcre
Requires:       php-spl
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_vendor}/%{pk_name}) = %{version}


%description
Plates is a native PHP template system that's fast, easy to use and easy
to extend. It's inspired by the excellent Twig template engine and strives
to bring modern template language functionality to native PHP templates.
Plates is designed for developers who prefer to use native PHP templates
over compiled template languages, such as Twig or Smarty.

Autoloader: %{_datadir}/php/%{ns_vendor}/%{ns_project}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}

install -pm 644 %{SOURCE2} src/autoload.php


%build
# Nothing


%install

# Restore PSR-0 tree
mkdir -p   %{buildroot}%{_datadir}/php/%{ns_vendor}
cp -pr src %{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}


%check
: Generate a simple autoloader
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
// Installed library
require '%{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}/autoload.php';

// Dependency
require_once '%{_datadir}/php/org/bovigo/vfs/autoload.php';
EOF

: Run upstream test suite
%{_bindir}/phpunit --verbose


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc *.md
%doc composer.json
%{_datadir}/php/%{ns_vendor}


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Dec 28 2016 Remi Collet <remi@fedoraproject.org> - 3.3.0-2
- update to 3.3.0
- switch to fedora/autoloader

* Thu Apr  7 2016 Remi Collet <remi@fedoraproject.org> - 3.1.1-1
- initial package, version 3.1.1


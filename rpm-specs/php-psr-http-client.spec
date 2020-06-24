# remirepo/fedora spec file for php-psr-http-client
#
# Copyright (c) 2019 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

# Github
%global gh_commit    496a823ef742b632934724bf769560c2a5c7c44e
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     php-fig
%global gh_project   http-client
# Packagist
%global pk_vendor    psr
%global pk_project   %{gh_project}
# Namespace
%global ns_vendor    Psr
%global ns_project   Http
%global ns_sub       Client

Name:           php-%{pk_vendor}-%{pk_project}
Version:        1.0.0
Release:        2%{?dist}
Summary:        Common interface for HTTP clients

License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{url}/archive/%{gh_commit}/%{name}-%{version}-%{gh_commit}.tar.gz

BuildArch:      noarch
# For tests
BuildRequires:  php(language) >= 7.0
BuildRequires:  php-cli
BuildRequires: (php-composer(%{pk_vendor}/http-message) >= 1.0  with php-composer(%{pk_vendor}/http-message) < 2)
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer.json,    "require": {
#        "php": "^7.0",
#        "psr/http-message": "^1.0"
Requires:       php(language) >= 7.0
Requires:      (php-composer(%{pk_vendor}/http-message) >= 1.0  with php-composer(%{pk_vendor}/http-message) < 2)
# phpcompatinfo (computed from version 1.0.0)
#     only core
# Autoloader
Requires:       php-composer(fedora/autoloader)

# Composer
Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}


%description
This repository holds all the common code related to PSR-18 (HTTP Client).

Please refer to the specification for a description:
https://www.php-fig.org/psr/psr-18/


Autoloader: %{_datadir}/php/%{ns_vendor}/%{ns_project}/%{ns_sub}/autoload.php


%prep
%setup -qn %{gh_project}-%{gh_commit}


%build
: Generate autoloader
%{_bindir}/phpab --template fedora --output src/autoload.php src
cat << 'EOF' | tee -a src/autoload.php
\Fedora\Autoloader\Dependencies::required([
    '%{_datadir}/php/Psr/Http/Message/autoload.php',
]);
EOF


%install
mkdir -p   %{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}
cp -rp src %{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}/%{ns_sub}


%check
: Test autoloader
php -nr '
require "%{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}/%{ns_sub}/autoload.php";
exit (interface_exists("%{ns_vendor}\\%{ns_project}\\%{ns_sub}\\ClientInterface") ? 0 : 1);
'


%files
%license LICENSE
%doc *.md
%doc composer.json
%{_datadir}/php/%{ns_vendor}/%{ns_project}/%{ns_sub}


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov  6 2019 Remi Collet <remi@remirepo.net> - 1.0.0-1
- Initial package, version 1.0.0

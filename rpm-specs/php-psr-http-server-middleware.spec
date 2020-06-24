# remirepo/fedora spec file for php-psr-http-server-middleware
#
# Copyright (c) 2020 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

# Github
%global gh_commit    2296f45510945530b9dceb8bcedb5cb84d40c5f5
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     php-fig
%global gh_project   http-server-middleware
# Packagist
%global pk_vendor    psr
%global pk_project   %{gh_project}
# Namespace
%global ns_vendor    Psr
%global ns_project   Http
%global ns_sub       Server

Name:           php-%{pk_vendor}-%{pk_project}
Version:        1.0.1
Release:        2%{?dist}
Summary:        Common interface for HTTP server-side middleware

License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{url}/archive/%{gh_commit}/%{name}-%{version}-%{gh_commit}.tar.gz

BuildArch:      noarch
# For tests
BuildRequires:  php(language) >= 7.0
BuildRequires:  php-cli
BuildRequires: (php-composer(%{pk_vendor}/http-message)        >= 1.0  with php-composer(%{pk_vendor}/http-message)        < 2)
BuildRequires: (php-composer(%{pk_vendor}/http-server-handler) >= 1.0  with php-composer(%{pk_vendor}/http-server-handler) < 2)
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer.json,    "require": {
#        "php": ">=7.0",
#        "psr/http-message": "^1.0",
#        "psr/http-server-handler": "^1.0"
Requires:       php(language) >= 7.0
Requires:      (php-composer(%{pk_vendor}/http-message)        >= 1.0  with php-composer(%{pk_vendor}/http-message)        < 2)
Requires:      (php-composer(%{pk_vendor}/http-server-handler) >= 1.0  with php-composer(%{pk_vendor}/http-server-handler) < 2)
# phpcompatinfo (computed from version 1.0.1)
#     only core
# Autoloader
Requires:       php-composer(fedora/autoloader)

# Composer
Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}


%description
This repository holds the MiddlewareInterface related to PSR-15
(HTTP Server Request Handlers).

Note that this is not a Middleware implementation of its own.
It is merely the interface that describe a Middleware.

Please refer to the specification for a description:
https://www.php-fig.org/psr/psr-15/


Autoloader: %{_datadir}/php/%{ns_vendor}/%{ns_project}/%{ns_sub}/middleware-autoload.php


%prep
%setup -qn %{gh_project}-%{gh_commit}


%build
: Generate autoloader
%{_bindir}/phpab --template fedora --output src/middleware-autoload.php src
cat << 'EOF' | tee -a src/middleware-autoload.php
\Fedora\Autoloader\Dependencies::required([
    '%{_datadir}/php/Psr/Http/Message/autoload.php',
    '%{_datadir}/php/Psr/Http/Server/autoload.php',
]);
EOF


%install
mkdir -p   %{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}
cp -rp src %{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}/%{ns_sub}


%check
: Test autoloader
php -nr '
require "%{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}/%{ns_sub}/middleware-autoload.php";
exit (interface_exists("%{ns_vendor}\\%{ns_project}\\%{ns_sub}\\MiddlewareInterface") ? 0 : 1);
'


%files
%license LICENSE
%doc *.md
%doc composer.json
%{_datadir}/php/%{ns_vendor}/%{ns_project}/%{ns_sub}/*


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan  2 2020 Remi Collet <remi@remirepo.net> - 1.0.1-1
- Initial package, version 1.0.1

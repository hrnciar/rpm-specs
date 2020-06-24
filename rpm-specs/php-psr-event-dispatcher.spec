# remirepo/fedora spec file for php-psr-event-dispatcher
#
# Copyright (c) 2019 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

# Github
%global gh_commit    dbefd12671e8a14ec7f180cab83036ed26714bb0
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     php-fig
%global gh_project   event-dispatcher
# Packagist
%global pk_vendor    psr
%global pk_project   %{gh_project}
# Namespace
%global ns_vendor    Psr
%global ns_project   EventDispatcher

Name:      php-%{pk_vendor}-%{pk_project}
Version:   1.0.0
Release:   3%{?dist}
Summary:   Standard interfaces for event handling

License:   MIT
URL:       https://github.com/%{gh_owner}/%{gh_project}
Source0:   %{url}/archive/%{gh_commit}/%{name}-%{version}-%{gh_commit}.tar.gz

BuildArch: noarch
# For tests
BuildRequires: php(language) >= 7.2
BuildRequires: php-cli
BuildRequires: php-fedora-autoloader-devel

# From composer.json,    "require": {
#       "php": ">=7.2.0",
Requires:  php(language) >= 7.2
# phpcompatinfo (computed from version 1.0.0)
#     only core
# Autoloader
Requires:  php-composer(fedora/autoloader)

# Composer
Provides:  php-composer(%{pk_vendor}/%{pk_project}) = %{version}


%description
This repository holds all interfaces related to PSR-14 (Event Dispatcher).

Please refer to the specification for a description:
https://www.php-fig.org/psr/psr-14/


Autoloader: %{_datadir}/php/%{ns_vendor}/%{ns_project}/autoload.php


%prep
%setup -qn %{gh_project}-%{gh_commit}


%build
: Generate autoloader
%{_bindir}/phpab --template fedora --output src/autoload.php src


%install
mkdir -p   %{buildroot}%{_datadir}/php/%{ns_vendor}
cp -rp src %{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}


%check
: Test autoloader
php -nr '
require "%{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}/autoload.php";
exit (interface_exists("%{ns_vendor}\\%{ns_project}\\EventDispatcherInterface") ? 0 : 1);
'


%files
%license LICENSE
%doc *.md
%doc composer.json
%dir %{_datadir}/php/%{ns_vendor}
     %{_datadir}/php/%{ns_vendor}/%{ns_project}


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Nov 30 2019 Remi Collet <remi@remirepo.net> - 1.0.0-2
- own /usr/share/php/Psr, from review #1768893

* Tue Nov  5 2019 Remi Collet <remi@remirepo.net> - 1.0.0-1
- Initial package, version 1.0.0

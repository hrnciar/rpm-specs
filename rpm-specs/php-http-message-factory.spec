# remirepo/fedora spec file for php-http-message-factory
#
# Copyright (c) 2019 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

# Github
%global gh_commit    a478cb11f66a6ac48d8954216cfed9aa06a501a1
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     php-http
%global gh_project   message-factory
# Packagist
%global pk_vendor    %{gh_owner}
%global pk_project   %{gh_project}
# Namespace
%global ns_vendor    Http
%global ns_project   Message

# skip duplicated php prefix
Name:      %{pk_vendor}-%{pk_project}
Version:   1.0.2
Release:   4%{?dist}
Summary:   Factory interfaces for PSR-7 HTTP Message

License:   MIT
URL:       https://github.com/%{gh_owner}/%{gh_project}
# git snapshot for skip .gitattributes
Source0:   %{name}-%{version}-%{gh_short}.tgz
Source1:   makesrc.sh

BuildArch: noarch
# For tests
BuildRequires:  php(language) >= 5.4
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
BuildRequires: (php-composer(psr/http-message) >= 1.0   with php-composer(psr/http-message) < 2)
%else
BuildRequires:  php-psr-http-message
%endif
BuildRequires:  php-cli
BuildRequires:  php-fedora-autoloader-devel

# From composer.json,    "require": {
#        "php": ">=5.4",
#        "psr/http-message": "^1.0"
Requires:  php(language) >= 5.4
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
Requires: (php-composer(psr/http-message) >= 1.0   with php-composer(psr/http-message) < 2)
%else
Requires:  php-psr-http-message
%endif
# phpcompatinfo (computed from version 1.0.2)
#     only Core
# Autoloader
Requires:   php-composer(fedora/autoloader)

# Composer
Provides:   php-composer(%{pk_vendor}/%{pk_project}) = %{version}


%description
Factory interfaces for PSR-7 HTTP Message.

Documentation: http://docs.php-http.org/

Autoloader: %{_datadir}/php/%{ns_vendor}/%{ns_project}/autoload.php


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
mkdir -p   %{buildroot}%{_datadir}/php/%{ns_vendor}
cp -rp src %{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}


%check
: Test autoloader
php -nr '
require "%{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}/autoload.php";
exit (interface_exists("%{ns_vendor}\\%{ns_project}\\RequestFactory") ? 0 : 1);
'


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc *.md
%doc composer.json
%{_datadir}/php/%{ns_vendor}


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 28 2019 Remi Collet <remi@remirepo.net> - 1.0.2-1
- Initial package, version 1.0.2

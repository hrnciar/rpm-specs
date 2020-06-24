# remirepo/fedora spec file for php-icewind-searchdav
#
# Copyright (c) 2017 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
# Github information
%global gh_commit    3071937c64a5e45d23c2600e5524538694e03042
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     icewind1991
%global gh_project   SearchDAV
# Packagist information
%global pk_vendor    icewind
%global pk_name      searchdav
# Namespace information (vendor added to make a better tree)
%global ns_vendor    Icewind
%global ns_name      SearchDAV

Name:           php-%{pk_vendor}-%{pk_name}
Version:        0.3.1
Release:        6%{?dist}
Summary:        A sabre/dav plugin to implement rfc5323 SEARCH

License:        AGPL
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{url}/archive/%{gh_commit}/%{name}-%{version}-%{gh_short}.tar.gz

BuildArch:      noarch
# For tests
BuildRequires:  php(language) >= 5.6
BuildRequires:  php-composer(sabre/dav) <  4
BuildRequires:  php-composer(sabre/dav) >= 3.2
# From composer.json, "require-dev": {
#        "phpunit/phpunit": "^4.8"
BuildRequires:  php-composer(phpunit/phpunit) >= 4.8
# Autoloader
BuildRequires:  php-composer(fedora/autoloader)

# From composer.json, "require": {
#       "php": ">=5.6",
#       "sabre/dav": "^3.2.0"
Requires:       php(language) >= 5.6
Requires:       php-composer(sabre/dav) <  4
Requires:       php-composer(sabre/dav) >= 3.2
# From phpcompatinfo report for version 0.3.1
Requires:       php-spl
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_vendor}/%{pk_name}) = %{version}


%description
A sabre/dav plugin to implement rfc5323 SEARCH.

See: https://tools.ietf.org/search/rfc5323

Autoloader: %{_datadir}/php/%{ns_vendor}/%{ns_name}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}

cat << 'EOF' | tee src/autoload.php
<?php
/* Autoloader for %{name} and its dependencies */

require_once '%{_datadir}/php/Fedora/Autoloader/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('SearchDAV\\', __DIR__);
\Fedora\Autoloader\Dependencies::required([
    '%{_datadir}/php/Sabre/DAV/autoload.php',
]);
EOF


%build
# Empty build section, most likely nothing required.


%install
mkdir -p   %{buildroot}%{_datadir}/php/%{ns_vendor}
cp -pr src %{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_name}



%check
mkdir vendor
ln -s %{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_name}/autoload.php vendor/autoload.php

cd tests

: Run the test suite
ret=0
for cmd in php php56 php70 php71 php72; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit || ret=1
  fi
done
exit $ret


%files
%{!?_licensedir:%global license %%doc}
# https://github.com/icewind1991/SearchDAV/issues/2
#license LICENCE
%doc composer.json
%doc *.md
%dir %{_datadir}/php/%{ns_vendor}
     %{_datadir}/php/%{ns_vendor}/%{ns_name}


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov  1 2017 Remi Collet <remi@remirepo.net> - 0.3.1-1
- initial package, version 0.3.1
- open https://github.com/icewind1991/SearchDAV/issues/2 - LICENSE

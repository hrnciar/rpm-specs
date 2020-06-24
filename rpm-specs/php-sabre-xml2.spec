# remirepo/fedora spec file for php-sabre-xml2
#
# Copyright (c) 2016-2020 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
# Github
%global gh_commit    41c6ba148966b10cafd31d1a4e5feb1e2138d95c
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sabre-io
%global gh_project   xml
# Packagist
%global pk_vendor    sabre
%global pk_project   %{gh_project}
# Namespace
%global ns_vendor    Sabre
%global ns_project   Xml
%global major        2
%global with_tests   0%{!?_without_tests:1}

Name:           php-%{pk_vendor}-%{pk_project}%{major}
Summary:        XML library that you may not hate
Version:        2.2.1
Release:        1%{?dist}

URL:            https://github.com/%{gh_owner}/%{gh_project}
License:        BSD
# Git snapshot with tests, because of .gitattributes
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
%if %{with_tests}
BuildRequires:  php(language) >= 7.1
BuildRequires:  php-xmlwriter
BuildRequires:  php-xmlreader
BuildRequires:  php-dom
BuildRequires: (php-composer(sabre/uri) >= 1.0   with  php-composer(sabre/uri) <  3)
BuildRequires:  php-libxml
BuildRequires:  php-pcre
BuildRequires:  php-spl
# From composer.json, "require-dev": {
#        "phpstan/phpstan": "^0.12",
#        "phpunit/phpunit" : "^7.5 || ^8.5 || ^9.0"
BuildRequires:  phpunit8 >= 8.5
%endif
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer.json, "require" : {
#        "php" : "^7.1",
#        "ext-xmlwriter" : "*",
#        "ext-xmlreader" : "*",
#        "ext-dom" : "*",
#        "lib-libxml" : ">=2.6.20",
#        "sabre/uri" : ">=1.0,<3.0.0"
Requires:       php(language) >= 7.1
Requires:       php-xmlwriter
Requires:       php-xmlreader
Requires:       php-dom
Requires:      (php-composer(sabre/uri) >= 1.0   with  php-composer(sabre/uri) <  3)
# From phpcompatinfo report for version 2.1.2
Requires:       php-libxml
Requires:       php-pcre
Requires:       php-spl
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}


%description
The sabre/xml library is a specialized XML reader and writer.

Autoloader: %{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}

phpab -t fedora -o lib/autoload.php lib
cat << 'EOF' | tee -a lib/autoload.php

// Dependencies
\Fedora\Autoloader\Dependencies::required([
    [
        '%{_datadir}/php/Sabre/Uri2/autoload.php',
        '%{_datadir}/php/Sabre/Uri/autoload.php',
    ],
]);

// Functions
if (!function_exists('Sabre\\Xml\\Serializer\\enum')) {
    require_once __DIR__ . '/Deserializer/functions.php';
    require_once __DIR__ . '/Serializer/functions.php';
}
EOF


%build
# nothing to build


%install
# Install as a PSR-0 library
mkdir -p %{buildroot}%{_datadir}/php/%{ns_vendor}
cp -pr lib %{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}


%check
%if %{with_tests}
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require_once '%{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('Sabre\\Xml\\', dirname(__DIR__).'/tests/Sabre/Xml/');
EOF
cd tests

: Run upstream test suite against installed library
ret=0
for cmd in php php72 php73 php74 php80; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit8 || ret=1
  fi
done
exit $ret
%else
: Skip upstream test suite
%endif


%files
%license LICENSE
%doc *md
%doc composer.json
%{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}


%changelog
* Mon May 11 2020 Remi Collet <remi@remirepo.net> - 2.2.1-1
- update to 2.2.1

* Sat Feb  1 2020 Remi Collet <remi@remirepo.net> - 2.2.0-1
- update to 2.2.0
- raise dependency on PHP 7.1
- switch to phpunit8

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 19 2019 Remi Collet <remi@remirepo.net> - 2.1.3-1
- update to 2.1.3

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul  5 2019 Remi Collet <remi@remirepo.net> - 2.1.2-3
- fix autoloader

* Fri Jul  5 2019 Remi Collet <remi@remirepo.net> - 2.1.2-2
- fix autoloader for sabre/uri v1 and v2

* Mon Jul  1 2019 Remi Collet <remi@remirepo.net> - 2.1.2-1
- update to 2.1.2
- rename to php-sabre-xml2
- move to /usr/share/php/Sabre/Xml2
- raise dependency on PHP 7
- switch to classmap autoloader

* Wed Jan  9 2019 Remi Collet <remi@remirepo.net> - 1.5.1-1
- update to 1.5.1

* Tue Jun  5 2018 Remi Collet <remi@remirepo.net> - 1.5.0-6
- fix project URL

* Sat Oct 29 2016 Remi Collet <remi@fedoraproject.org> - 1.5.0-2
- switch from symfony/class-loader to fedora/autoloader

* Mon Oct 10 2016 Remi Collet <remi@fedoraproject.org> - 1.5.0-1
- update to 1.5.0
- raise dependency on PHP 5.5

* Fri May 20 2016 Remi Collet <remi@fedoraproject.org> - 1.4.2-1
- update to 1.4.2

* Tue Mar 29 2016 Remi Collet <remi@fedoraproject.org> - 1.4.1-1
- update to 1.4.1

* Fri Mar 11 2016 Remi Collet <remi@fedoraproject.org> - 1.4.0-1
- Initial packaging


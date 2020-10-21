# remirepo/fedora spec file for php-bacon-qr-code
#
# Copyright (c) 2017 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global gh_commit    5a91b62b9d37cee635bbf8d553f4546057250bee
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     Bacon
%global gh_project   BaconQrCode

%global pk_vendor    bacon
%global pk_project   bacon-qr-code

%global ns_vendor    %nil
%global ns_project   %{gh_project}
%global php_home     %{_datadir}/php
%global with_tests   0%{!?_without_tests:1}

Name:           php-%{pk_project}
Version:        1.0.3
Release:        7%{?dist}
Summary:        QR code generator for PHP

License:        BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{name}-%{version}-%{gh_short}.tar.gz

BuildArch:      noarch
%if %{with_tests}
# For tests
BuildRequires:  php(language) >= 5.4
BuildRequires:  php-gd
BuildRequires:  php-reflection
BuildRequires:  php-simplexml
BuildRequires:  php-ctype
BuildRequires:  php-iconv
BuildRequires:  php-spl
BuildRequires:  php-composer(phpunit/phpunit)
# Required by autoloader
BuildRequires:  php-composer(fedora/autoloader)
%endif

# From composer.json, "require": {
#        "php": ">=5.3.3"
Requires:       php(language) >= 5.3.3
Requires:       php-iconv
# From composer.json, "suggest": {
#        "ext-gd": "to generate QR code images"
Requires:       php-gd
# From phpcompatinfo report for version 1.0.1
Requires:       php-reflection
Requires:       php-simplexml
Requires:       php-ctype
Requires:       php-spl
# Required by autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}


%description
BaconQrCode is a port of QR code portion of the ZXing library.
It currently only features the encoder part, but could later
receive the decoder part as well.

As the Reed Solomon codec implementation of the ZXing library
performs quite slow in PHP, it was exchanged with the implementation
by Phil Karn.

Autoloader: %{php_home}/%{ns_project}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}

cat << 'EOF' | tee src/%{ns_project}/autoload.php
<?php
/* Autoloader for %{name} and its dependencies */
require_once '/usr/share/php/Fedora/Autoloader/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('%{ns_project}\\', __DIR__);
EOF


%build
# Empty build section, most likely nothing required.


%install
: Library
mkdir -p                 %{buildroot}%{php_home}
cp -pr src/%{ns_project} %{buildroot}%{php_home}/%{ns_project}


%check
%if %{with_tests}
if php -r 'exit(PHP_INT_SIZE<8 ? 0 : 1);'
then
  : ignore test suite because of https://github.com/Bacon/BaconQrCode/issues/31
  exit 0
fi

cd tests
cat << 'EOF' | tee bootstrap.php
<?php
require '%{buildroot}%{php_home}/%{ns_project}/autoload.php';
EOF

ret=0
for cmd in php php56 php70 php71 php72; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit --verbose || ret=1
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
%doc README.md
%{php_home}/%{ns_project}


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Oct 19 2017 Remi Collet <remi@remirepo.net> - 1.0.3-1
- Update to 1.0.3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul  3 2017 Remi Collet <remi@remirepo.net> - 1.0.1-4
- run test suite only on 64-bit arch

* Mon Jul  3 2017 Remi Collet <remi@remirepo.net> - 1.0.1-2
- fix directory ownership, from review #1465313

* Tue Jun 27 2017 Remi Collet <remi@remirepo.net> - 1.0.1-1
- initial package, version 1.0.1
- open https://github.com/Bacon/BaconQrCode/pull/29 - phpunit

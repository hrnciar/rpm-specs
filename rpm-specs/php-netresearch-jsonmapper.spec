# remirepo/fedora spec file for php-netresearch-jsonmapper
#
# Copyright (c) 2017-2020 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global gh_commit    e0f1e33a71587aca81be5cffbb9746510e1fe04e
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     cweiske
%global gh_project   jsonmapper

%global pk_vendor    netresearch
%global pk_project   jsonmapper

%global php_home     %{_datadir}/php
%global with_tests   0%{!?_without_tests:1}

Name:           php-%{pk_vendor}-%{pk_project}
Version:        2.1.0
Release:        1%{?dist}
Summary:        Map nested JSON structures onto PHP classes

License:        OSL 3.0
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
# Git snapshot with tests
Source1:        makesrc.sh

BuildArch:      noarch
%if %{with_tests}
# For tests
BuildRequires:  php(language) >= 5.6
BuildRequires:  php-spl
BuildRequires:  php-json
BuildRequires:  php-pcre
BuildRequires:  php-reflection
# From composer.json, "require-dev": {
#        "phpunit/phpunit": "~4.8.35 || ~5.7 || ~6.4 || ~7.0",
#        "squizlabs/php_codesniffer": "~3.5"
%global phpunit %{_bindir}/phpunit7
BuildRequires: phpunit7
# Required by autoloader
BuildRequires:  php-fedora-autoloader-devel
%endif

# From composer.json, "require": {
#        "php": ">=5.6",
#        "ext-spl": "*",
#        "ext-json": "*",
#        "ext-pcre": "*",
#        "ext-reflection": "*"
Requires:       php(language) >= 5.6
Requires:       php-spl
Requires:       php-json
Requires:       php-pcre
Requires:       php-reflection
# From phpcompatinfo report for version 1.6.0
# none
# Required by autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}


%description
Takes data retrieved from a JSON web service and converts them into nested
object and arrays - using your own model classes.

Starting from a base object, it maps JSON data on class properties, converting
them into the correct simple types or objects.

It's a bit like the native SOAP parameter mapping PHP's SoapClient gives you,
but for JSON. It does not rely on any schema, only your PHP class definitions.

Type detection works by parsing @var docblock annotations of class properties,
as well as type hints in setter methods.

You do not have to modify your model classes by adding JSON specific code;
it works automatically by parsing already-existing docblocks.

Autoloader: %{php_home}/%{pk_vendor}/%{pk_project}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}


%build
phpab --template fedora --output src/autoload.php src


%install
: Library
mkdir -p   %{buildroot}%{php_home}/%{pk_vendor}
cp -pr src %{buildroot}%{php_home}/%{pk_vendor}/%{pk_project}


%check
%if %{with_tests}
mkdir vendor

: Run upstream test suite
ret=0
for cmd in "php %{phpunit}" php72 php73 php74 php80; do
  if which $cmd; then
    set $cmd
    $1 ${2:-%{_bindir}/phpunit7} \
      --bootstrap %{buildroot}%{php_home}/%{pk_vendor}/%{pk_project}/autoload.php \
      --no-coverage \
      --verbose . || ret=1
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
%doc ChangeLog README.rst
%dir %{php_home}/%{pk_vendor}
     %{php_home}/%{pk_vendor}/%{pk_project}


%changelog
* Fri Apr 17 2020 Remi Collet <remi@remirepo.net> - 2.1.0-1
- update to 2.1.0

* Sat Mar 14 2020 Remi Collet <remi@remirepo.net> - 2.0.0-1
- update to 2.0.0
- switch to phpunit7

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 19 2019 Remi Collet <remi@remirepo.net> - 1.6.0-1
- update to 1.6.0
- drop patch merged upstream

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul  9 2019 Remi Collet <remi@remirepo.net> - 1.5.1-1
- update to 1.5.1

* Mon Jul  8 2019 Remi Collet <remi@remirepo.net> - 1.5.0-1
- update to 1.5.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 22 2018 Remi Collet <remi@remirepo.net> - 1.4.0-1
- Update to 1.4.0
- use phpunit6 on F26+
- sources from git snapshot

* Sat Oct 21 2017 Remi Collet <remi@remirepo.net> - 1.3.0-1
- initial package, version 1.3.0

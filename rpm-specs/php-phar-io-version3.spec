# remirepo/fedora spec file for php-phar-io-version3
#
# Copyright (c) 2017-2020 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%bcond_with          bootstrap
%if %{with bootstrap}
%bcond_with          tests
%else
%bcond_without       tests
%endif

%global gh_commit    c6bb6825def89e0a32220f88337f8ceaf1975fa0
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     phar-io
%global gh_project   version
%global pk_vendor    %{gh_owner}
%global pk_project   %{gh_project}
%global ns_vendor    PharIo
%global ns_project   Version
%global major        3
%global php_home     %{_datadir}/php

Name:           php-%{pk_vendor}-%{pk_project}%{major}
Version:        3.0.2
Release:        2%{?dist}
Summary:        Library for handling version information and constraints

License:        BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
BuildRequires:  php(language) >= 7.2
BuildRequires:  php-pcre
BuildRequires:  php-spl
BuildRequires:  php-fedora-autoloader-devel >= 1.0.0
%if %{with tests}
%if 0%{?fedora} >= 32
%global phpunit %{_bindir}/phpunit9
%else
%global phpunit %{_bindir}/phpunit8
%endif
BuildRequires:  %{phpunit}
%endif

# from composer.json
#    "php": "^7.2 || ^8.0",
Requires:       php(language) >= 7.2
# from phpcompatinfo report for version 3.0.0
Requires:       php-pcre
Requires:       php-spl
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}


%description
Library for handling version information and constraints.

Autoloader: %{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}


%build
# Generate the Autoloader
%{_bindir}/phpab --template fedora --output src/autoload.php src


%install
mkdir -p   %{buildroot}%{php_home}/%{ns_vendor}
cp -pr src %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}


%check
%if %{with tests}
: Run upstream test suite
ret=0
BS=%{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php
for cmd in "php %{phpunit}" "php72 %{_bindir}/phpunit8" php73 php74 php80; do
  if which $cmd; then
    set $cmd
    $1 -d auto_prepend_file=$BS \
      ${2:-%{_bindir}/phpunit9} \
        --bootstrap $BS --verbose || ret=1
  fi
done
exit $ret
%else
: bootstrap build with test suite disabled
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc README.md composer.json
%dir %{php_home}/%{ns_vendor}
     %{php_home}/%{ns_vendor}/%{ns_project}%{major}


%changelog
* Tue Aug 11 2020 Remi Collet <remi@remirepo.net> - 3.0.2-2
- switch to phpunit9

* Mon Jun 29 2020 Remi Collet <remi@remirepo.net> - 3.0.2-1
- update to 3.0.2 (no change)
- sources from git snapshot

* Mon May 11 2020 Remi Collet <remi@remirepo.net> - 3.0.1-1
- update to 3.0.1

* Thu May  7 2020 Remi Collet <remi@remirepo.net> - 3.0.0-1
- update to 3.0.0
- rename to php-phar-io-version3
- move to /usr/share/php/PharIo/Version3
- raise dependency on PHP 7.2
- switch to phpunit8

* Mon Jul 16 2018 Remi Collet <remi@remirepo.net> - 2.0.1-1
- update to 2.0.1

* Fri Apr  7 2017 Remi Collet <remi@remirepo.net> - 1.0.1-1
- initial package


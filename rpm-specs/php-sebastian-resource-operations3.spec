# remirepo/fedora spec file for php-sebastian-resource-operations3
#
# Copyright (c) 2015-2020 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%bcond_without       tests

%global gh_commit    0f4443cb3a1d92ce809899753bc0d5d5a8dd19a8
#global gh_date      20150728
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sebastianbergmann
%global gh_project   resource-operations
%global php_home     %{_datadir}/php
# Packagist
%global pk_vendor    sebastian
%global pk_project   %{gh_project}
# Namespace
%global ns_vendor    SebastianBergmann
%global ns_project   ResourceOperations
%global major        3

Name:           php-%{pk_vendor}-%{pk_project}%{major}
Version:        3.0.3
%global specrel 1
Release:        %{?gh_date:1%{specrel}.%{?prever}%{!?prever:%{gh_date}git%{gh_short}}}%{!?gh_date:%{specrel}}%{?dist}
Summary:        Provides a list of PHP built-in functions that operate on resources, version %{major}

License:        BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
BuildRequires:  php(language) >= 7.3
BuildRequires:  php-fedora-autoloader-devel
%if %{with tests}
# from composer.json
#        "phpunit/phpunit": "^9.0"
BuildRequires:  phpunit9
%endif

# from composer.json
#        "php": ">=7.3"
Requires:       php(language) >= 7.3
# Autoloader
Requires:       php-composer(fedora/autoloader)
# from phpcompatinfo report for version 3.0.0: nothing

Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}


%description
%{summary}.

This package provides version %{major}.

Autoloader: %{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}


%build
# Generate the Autoloader
phpab --template fedora --output src/autoload.php src


%install
mkdir -p   %{buildroot}%{php_home}/%{ns_vendor}
cp -pr src %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}


%check
%if %{with tests}
mkdir vendor
touch vendor/autoload.php

: Run upstream test suite
ret=0
for cmd in php php73 php74 php80; do
  if which $cmd; then
    $cmd -d auto_prepend_file=%{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php \
      %{_bindir}/phpunit9  --verbose tests || ret=1
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
* Mon Sep 28 2020 Remi Collet <remi@remirepo.net> - 3.0.3-1
- update to 3.0.3 (no change)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 29 2020 Remi Collet <remi@remirepo.net> - 3.0.2-1
- update to 3.0.2 (no change)

* Tue Jun 16 2020 Remi Collet <remi@remirepo.net> - 3.0.1-1
- update to 3.0.1 (no change)
- sources from git snapshot

* Fri Feb  7 2020 Remi Collet <remi@remirepo.net> - 3.0.0-1
- update to 3.0.0
- raise dependency on PHP 7.3
- rename to php-sebastian-resource-operations3
- move to /usr/share/php/SebastianBergmann/ResourceOperations3

* Thu Oct  4 2018 Remi Collet <remi@remirepo.net> - 2.0.1-1
- update to 2.0.1
- drop patch merged upstream

* Fri Sep 28 2018 Remi Collet <remi@remirepo.net> - 2.0.0-1
- update to 2.0.0
- raise dependency on PHP 7.1
- rename to php-sebastian-resource-operations2
- move to /usr/share/php/SebastianBergmann/ResourceOperations2

* Mon Oct 31 2016 Remi Collet <remi@fedoraproject.org> - 1.0.0-2
- switch to fedora/autoloader

* Fri Oct  2 2015 Remi Collet <remi@fedoraproject.org> - 1.0.0-1
- Update to 1.0.0 (no change)

* Tue Sep 29 2015 Remi Collet <remi@fedoraproject.org> - 1.0.0-0.1.20150728gitce990bb
- initial package

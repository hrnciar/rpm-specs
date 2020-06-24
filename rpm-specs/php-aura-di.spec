# remirepo/Fedora spec file for php-aura-di
#
# Copyright (c) 2015-2017 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global bootstrap    0
%global gh_commit    f676b38a0d1c3b0d7897b0a082f4811eb8b08faa
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     auraphp
%global gh_project   Aura.Di
%global pk_owner     aura
%global pk_project   di
%global ns_owner     Aura
%global ns_project   Di
%global php_home     %{_datadir}/php
%global with_tests   0%{!?_without_tests:1}

Name:           php-%{pk_owner}-%{pk_project}
Version:        3.4.0
Release:        6%{?dist}
Summary:        A serializable dependency injection container

License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{name}-%{version}-%{gh_short}.tar.gz

BuildArch:      noarch
BuildRequires:  php-composer(fedora/autoloader)
# Tests
%if %{with_tests}
BuildRequires:  php(language) >= 5.5.0
BuildRequires:  php-composer(container-interop/container-interop) >= 1.0
BuildRequires:  php-reflection
BuildRequires:  php-spl
BuildRequires:  php-composer(phpunit/phpunit)
# From composer.json, "require-dev": {
#        "mouf/picotainer": "~1.0",
#        "acclimate/container": "~1.0",
#        "phpunit/phpunit": "~5.7 || ~4.8"
%endif

# From composer, "require": {
#        "php": ">=5.5.0"
#        "container-interop/container-interop": "~1.0"
Requires:       php(language) >= 5.5.0
Requires:       php-composer(container-interop/container-interop) >= 1.0
Requires:       php-composer(container-interop/container-interop) <  2
# From phpcompatinfo report for version 3.2.0
Requires:       php-reflection
Requires:       php-spl
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_owner}/%{pk_project}) = %{version}
Provides:       php-composer(container-interop/container-interop-implementation) = 1.0


%description
A serializable dependency injection container with constructor and setter
injection, interface and trait awareness, configuration inheritance, and
much more.

Autoloader: %{php_home}/%{ns_owner}/%{ns_project}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}


%build
cat << 'EOF' | tee -a src/autoload.php
<?php
/* Autoloader for %{pk_owner}/%{pk_project} and its dependencies */

require_once '%{_datadir}/php/Fedora/Autoloader/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('Aura\\Di\\', __DIR__);
\Fedora\Autoloader\Dependencies::required(array(
    '%{php_home}/Interop/Container/autoload.php',
));
EOF


%install
mkdir -p   %{buildroot}%{php_home}/%{ns_owner}
cp -pr src %{buildroot}%{php_home}/%{ns_owner}/%{ns_project}


%check
%if %{with_tests}
: Ignore test using not available dependency
rm tests/ContainerTest.php

mkdir vendor
cat << 'EOF' | tee -a vendor/autoload.php
<?php
require '%{buildroot}/%{php_home}/%{ns_owner}/%{ns_project}/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('Aura\\Di\\', dirname(__DIR__) . '/tests');
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
%doc *.md
%doc composer.json
%dir %{php_home}/%{ns_owner}/
     %{php_home}/%{ns_owner}/%{ns_project}/


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Aug  8 2017 Remi Collet <remi@remirepo.net> - 3.4.0-1
- Update to 3.4.0

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 15 2016 Remi Collet <remi@fedoraproject.org> - 3.2.0-1
- update to 3.2.0
- License is now MIT
- update package Summary and Description
- raise dependency on PHP 5.5
- add dependency on container-interop/container-interop
- provide container-interop/container-interop-implementation
- switch to fedora/autoloader

* Fri Jul  1 2016 Remi Collet <remi@fedoraproject.org> - 2.2.4-1
- initial package


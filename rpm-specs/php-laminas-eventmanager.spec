# remirepo/Fedora spec file for php-laminas-eventmanager
#
# Copyright (c) 2015-2020 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global bootstrap    0
%global gh_commit    ce4dc0bdf3b14b7f9815775af9dfee80a63b4748
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     laminas
%global gh_project   laminas-eventmanager
%global zf_name      zend-eventmanager
%global php_home     %{_datadir}/php
%global namespace    Laminas
%global library      EventManager
%if %{bootstrap}
%global with_tests   0%{?_with_tests:1}
%else
%global with_tests   0%{!?_without_tests:1}
%endif

Name:           php-%{gh_project}
Version:        3.2.1
Release:        3%{?dist}
Summary:        Trigger and listen to events within a PHP application

License:        BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{gh_commit}/%{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
# Tests
%if %{with_tests}
BuildRequires:  php(language) >= 5.6
BuildRequires: (php-composer(%{gh_owner}/laminas-zendframework-bridge) >= 1.0 with php-composer(%{gh_owner}/laminas-zendframework-bridge) < 2)
BuildRequires:  php-reflection
BuildRequires:  php-spl
# From composer, "require-dev": {
#        "athletic/athletic": "^0.1",
#        "container-interop/container-interop": "^1.1.0",
#        "laminas/laminas-coding-standard": "~1.0.0",
#        "laminas/laminas-stdlib": "^2.7.3 || ^3.0",
#        "phpunit/phpunit": "^5.7.27 || ^6.5.8 || ^7.1.2"
BuildRequires: (php-composer(container-interop/container-interop) >= 1.1.0 with php-composer(container-interop/container-interop) < 2)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-stdlib)        >= 3.0   with php-autoloader(%{gh_owner}/laminas-stdlib)        < 4)
%global phpunit %{_bindir}/phpunit7
BuildRequires:  phpunit7 >= 7.1.2
# Autoloader
BuildRequires:  php-fedora-autoloader-devel
%endif

# From composer, "require": {
#        "php": "^5.6 || ^7.0",
#        "laminas/laminas-zendframework-bridge": "^1.0"
Requires:       php(language) >= 5.6
Requires:      (php-composer(%{gh_owner}/laminas-zendframework-bridge) >= 1.0 with php-composer(%{gh_owner}/laminas-zendframework-bridge) < 2)
%if ! %{bootstrap}
# From composer, "suggest": {
#        "container-interop/container-interop": "^1.1.0, to use the lazy listeners feature",
#        "laminas/laminas-stdlib": "^2.7.3 || ^3.0, to use the FilterChain feature"
Suggests:       php-composer(container-interop/container-interop)
Suggests:       php-composer(%{gh_owner}/laminas-stdlib)
%endif
# From phpcompatinfo report for version 3.2.1
Requires:       php-reflection
Requires:       php-spl
# Autoloader
Requires:       php-composer(fedora/autoloader)

# Compatibily ensure by the bridge
Obsoletes:      php-zendframework-%{zf_name}              < 3.2.1-99
Provides:       php-zendframework-%{zf_name}              = %{version}-99
Provides:       php-composer(%{gh_owner}/%{gh_project})   = %{version}
Provides:       php-composer(zendframework/%{zf_name})    = %{version}
Provides:       php-autoloader(%{gh_owner}/%{gh_project}) = %{version}
Provides:       php-autoloader(zendframework/%{zf_name})  = %{version}


%description
The %{gh_project} is a component designed for the following use cases:

* Implementing simple subject/observer patterns.
* Implementing Aspect-Oriented designs.
* Implementing event-driven architectures.

The basic architecture allows you to attach and detach listeners to named
events, both on a per-instance basis as well as via shared collections;
trigger events; and interrupt execution of listeners.

Documentation: https://docs.laminas.dev/%{gh_project}/


%prep
%setup -q -n %{gh_project}-%{gh_commit}

mv LICENSE.md LICENSE


%build
phpab --template fedora --output src/autoload.php src
cat << 'EOF' | tee -a src/autoload.php
\Fedora\Autoloader\Dependencies::optional([
    '%{php_home}/Interop/Container/autoload.php',
    '%{php_home}/%{namespace}/Stdlib/autoload.php',
]);
EOF

cat << 'EOF' | tee zf.php
<?php
require_once '%{php_home}/Fedora/Autoloader/autoload.php';
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/%{namespace}/ZendFrameworkBridge/autoload.php',
    dirname(dirname(__DIR__)) . '/%{namespace}/%{library}/autoload.php',
]);
EOF


%install
: Laminas library
mkdir -p   %{buildroot}%{php_home}/%{namespace}/
cp -pr src %{buildroot}%{php_home}/%{namespace}/%{library}

: Zend equiv
mkdir -p      %{buildroot}%{php_home}/Zend/%{library}
cp -pr zf.php %{buildroot}%{php_home}/Zend/%{library}/autoload.php


%check
%if %{with_tests}
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require_once '%{buildroot}%{php_home}/%{namespace}/%{library}/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('%{namespace}Test\\%{library}\\', dirname(__DIR__) . '/test');
require_once __DIR__ . '/../test/_autoload.php';
EOF

ret=0
for cmdarg in "php %{phpunit}" php72 php73 php74; do
  if which $cmdarg; then
    set $cmdarg
    $1 ${2:-%{_bindir}/phpunit7} --verbose || ret=1
  fi
done

: check compat autoloader
php -r '
require "%{buildroot}%{php_home}/Zend/%{library}/autoload.php";
exit (class_exists("\\Zend\\%{library}\\%{library}") ? 0 : 1);
'

exit $ret
%else
: Test suite disabled
%endif


%files
%license LICENSE
%doc *.md
%doc composer.json
%{php_home}/Zend/%{library}
%{php_home}/%{namespace}/%{library}


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Remi Collet <remi@remirepo.net> - 3.2.1-2
- cleanup

* Tue Jan  7 2020 Remi Collet <remi@remirepo.net> - 3.2.1-1
- switch to Laminas

* Thu Apr 26 2018 Remi Collet <remi@remirepo.net> - 3.2.1-1
- update to 3.2.1 (no change)
- switch to phpunit6 or phpunit7

* Thu Nov 23 2017 Remi Collet <remi@fedoraproject.org> - 3.2.0-3
- switch from zend-loader to fedora/autoloader

* Wed Jul 12 2017 Remi Collet <remi@remirepo.net> - 3.2.0-1
- Update to 3.2.0
- use phpunit6 on F26+

* Tue Dec 20 2016 Remi Collet <remi@fedoraproject.org> - 3.1.0-1
- update to 3.1.0
- raise dependency on PHP 5.6

* Wed Jun 29 2016 Remi Collet <remi@fedoraproject.org> - 3.0.1-1
- update to 3.0.1 for ZendFramework 3
- dependency on zend-stdlib is optional

* Fri Feb 19 2016 Remi Collet <remi@fedoraproject.org> - 2.6.3-1
- update to 2.6.3
- raise dependency on zend-stdlib >= 2.7

* Thu Jan 28 2016 Remi Collet <remi@fedoraproject.org> - 2.6.2-1
- update to 2.6.2

* Tue Aug  4 2015 Remi Collet <remi@fedoraproject.org> - 2.5.2-1
- initial package

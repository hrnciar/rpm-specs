# remirepo/Fedora spec file for php-php-laminas-serializer
#
# Copyright (c) 2015-2020 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global bootstrap    0
%global gh_commit    c1c9361f114271b0736db74e0083a919081af5e0
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     laminas
%global gh_project   laminas-serializer
%global zf_name      zend-serializer
%global php_home     %{_datadir}/php
%global namespace    Laminas
%global library      Serializer
%if %{bootstrap}
%global with_tests   0%{?_with_tests:1}
%else
%global with_tests   0%{!?_without_tests:1}
%endif

Name:           php-%{gh_project}
Version:        2.9.1
Release:        4%{?dist}
Summary:        Laminas Framework %{library} component

License:        BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{gh_commit}/%{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
# Tests
%if %{with_tests}
BuildRequires:  php(language) >= 5.6
BuildRequires:  php-dom
BuildRequires:  php-libxml
BuildRequires:  php-pcre
BuildRequires:  php-simplexml
BuildRequires:  php-spl
# From composer, "require-dev": {
#        "laminas/laminas-coding-standard": "~1.0.0",
#        "laminas/laminas-math": "^2.6 || ^3.0",
#        "laminas/laminas-servicemanager": "^2.7.5 || ^3.0.3",
#        "phpunit/phpunit": "^5.7.27 || ^6.5.14 || ^7.5.16"
BuildRequires: (php-autoloader(%{gh_owner}/laminas-json)               >= 3.0    with php-autoloader(%{gh_owner}/laminas-json)               < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-stdlib)             >= 3.0    with php-autoloader(%{gh_owner}/laminas-stdlib)             < 4)
BuildRequires: (php-composer(%{gh_owner}/laminas-zendframework-bridge) >= 1.0    with php-composer(%{gh_owner}/laminas-zendframework-bridge) < 2)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-math)               >= 3.0    with php-autoloader(%{gh_owner}/laminas-math)               < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-servicemanager)     >= 3.0.3  with php-autoloader(%{gh_owner}/laminas-servicemanager)     < 4)
BuildRequires:  phpunit7 >= 7.5.16
%endif
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer, "require": {
#        "php": "^5.6 || ^7.0",
#        "laminas/laminas-json": "^2.5 || ^3.0",
#        "laminas/laminas-stdlib": "^2.7 || ^3.0",
#        "laminas/laminas-zendframework-bridge": "^1.0"
Requires:       php(language) >= 5.6
%if ! %{bootstrap}
Requires:      (php-autoloader(%{gh_owner}/laminas-json)               >= 3.0    with php-autoloader(%{gh_owner}/laminas-json)               < 4)
Requires:      (php-autoloader(%{gh_owner}/laminas-stdlib)             >= 3.0    with php-autoloader(%{gh_owner}/laminas-stdlib)             < 4)
Requires:      (php-composer(%{gh_owner}/laminas-zendframework-bridge) >= 1.0    with php-composer(%{gh_owner}/laminas-zendframework-bridge) < 2)
# From composer, "suggest": {
#        "laminas/laminas-math": "(^2.6 || ^3.0) To support Python Pickle serialization",
#        "laminas/laminas-servicemanager": "(^2.7.5 || ^3.0.3) To support plugin manager support"
Suggests:       php-autoloader(%{gh_owner}/laminas-math)
Suggests:       php-autoloader(%{gh_owner}/laminas-servicemanager)
Suggests:       php-pecl(igbinary)
Suggests:       php-pecl(msgpack)
%endif
# From phpcompatinfo report for version 2.9.1
Requires:       php-dom
Requires:       php-libxml
Requires:       php-pcre
Requires:       php-simplexml
Requires:       php-spl
# Autoloader
Requires:       php-composer(fedora/autoloader)

# Compatibily ensure by the bridge
Obsoletes:      php-zendframework-%{zf_name}              < 2.9.1-99
Provides:       php-zendframework-%{zf_name}              = %{version}-99
Provides:       php-composer(%{gh_owner}/%{gh_project})   = %{version}
Provides:       php-composer(zendframework/%{zf_name})    = %{version}
Provides:       php-autoloader(%{gh_owner}/%{gh_project}) = %{version}
Provides:       php-autoloader(zendframework/%{zf_name})  = %{version}


%description
The %{gh_project} component provides an adapter based interface
to simply generate storable representation of PHP types by different
facilities, and recover.

Documentation: https://docs.laminas.dev/%{gh_project}/


%prep
%setup -q -n %{gh_project}-%{gh_commit}

mv LICENSE.md LICENSE


%build
phpab --template fedora --output src/autoload.php src
cat << 'EOF' | tee -a src/autoload.php
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/%{namespace}/Stdlib/autoload.php',
    '%{php_home}/%{namespace}/Json/autoload.php',
]);
\Fedora\Autoloader\Dependencies::optional([
    '%{php_home}/%{namespace}/Math/autoload.php',
    '%{php_home}/%{namespace}/ServiceManager/autoload.php',
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
EOF

ret=0
for cmd in php php71 php72 php73 php74; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit7 --verbose || ret=1
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
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Remi Collet <remi@remirepo.net> - 2.9.1-2
- cleanup

* Tue Jan  7 2020 Remi Collet <remi@remirepo.net> - 2.9.1-1
- switch to Laminas

* Mon Oct 21 2019 Remi Collet <remi@remirepo.net> - 2.9.1-1
- update to 2.9.1 (no change)
- switch to phpunit7

* Tue May 15 2018 Remi Collet <remi@remirepo.net> - 2.9.0-2
- update to 2.9.0
- use range dependencies on F27+
- switch to phpunit6

* Thu Nov 23 2017 Remi Collet <remi@remirepo.net> - 2.8.1-2
- switch from zend-loader to fedora/autoloader

* Tue Nov 21 2017 Remi Collet <remi@remirepo.net> - 2.8.1-1
- Update to 2.8.1

* Thu Nov  9 2017 Remi Collet <remi@fedoraproject.org> - 2.8.0-4
- fix FTBFS from Koschei, add patch for bigendian from
  https://github.com/zendframework/zend-serializer/pull/31

* Tue Jun 21 2016 Remi Collet <remi@fedoraproject.org> - 2.8.0-1
- update to 2.8.0
- raise dependency on PHP 5.6

* Wed May 11 2016 Remi Collet <remi@fedoraproject.org> - 2.7.2-1
- update to 2.7.2
- dependency to zend-math is now optional

* Tue Apr 19 2016 Remi Collet <remi@fedoraproject.org> - 2.7.1-1
- update to 2.7.1

* Thu Apr  7 2016 Remi Collet <remi@fedoraproject.org> - 2.7.0-1
- update to 2.7.0

* Thu Feb  4 2016 Remi Collet <remi@fedoraproject.org> - 2.6.1-1
- update to 2.6.1

* Wed Feb  3 2016 Remi Collet <remi@fedoraproject.org> - 2.6.0-1
- update to 2.6.0
- raise dependency on PHP >= 5.5
- raise dependency on zend-stdlib ~2.7
- raise dependency on zend-math ~2.6
- raise dependency on zend-servicemanager ~2.7.5

* Tue Aug  4 2015 Remi Collet <remi@fedoraproject.org> - 2.5.1-1
- initial package

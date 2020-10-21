# remirepo/Fedora spec file for php-laminas-mvc-plugin-flashmessenger
#
# Copyright (c) 2016-2020 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global bootstrap    0
%global gh_commit    f5a522c3aab215a9b89a0630beb91582f4a3f202
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     laminas
%global gh_project   laminas-mvc-plugin-flashmessenger
%global zf_name      zend-mvc-plugin-flashmessenger
%global php_home     %{_datadir}/php
%global namespace    Laminas
%global library      Mvc
%global subproj      Plugin
%global subsubp      FlashMessenger
%if %{bootstrap}
%global with_tests   0%{?_with_tests:1}
%else
%global with_tests   0%{!?_without_tests:1}
%endif

Name:           php-%{gh_project}
Version:        1.2.0
Release:        3%{?dist}
Summary:        %{namespace} Framework %{library}/%{subproj}/%{subsubp} component

License:        BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{gh_commit}/%{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
# Tests
%if %{with_tests}
BuildRequires:  php(language) >= 5.6
BuildRequires:  php-spl
BuildRequires: (php-autoloader(%{gh_owner}/laminas-mvc)                  >= 3.0    with php-autoloader(%{gh_owner}/laminas-mvc)                  < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-session)              >= 2.8.5  with php-autoloader(%{gh_owner}/laminas-session)              < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-stdlib)               >= 3.2.1  with php-autoloader(%{gh_owner}/laminas-stdlib)               < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-view)                 >= 2.10   with php-autoloader(%{gh_owner}/laminas-view)                 < 3)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.0    with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
# From composer, "require-dev": {
#        "laminas/laminas-coding-standard": "~1.0.0",
#        "laminas/laminas-i18n": "^2.8",
#        "phpunit/phpunit": "^5.7.27 || ^6.5.8 || ^7.1.4"
BuildRequires: (php-autoloader(%{gh_owner}/laminas-i18n)                 >= 2.8    with php-autoloader(%{gh_owner}/laminas-i18n)                 <  3)
%global phpunit %{_bindir}/phpunit7
BuildRequires:  phpunit7 >= 7.1.4
%endif
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer, "require": {
#        "php": "^5.6 || ^7.0",
#        "laminas/laminas-mvc": "^3.0",
#        "laminas/laminas-session": "^2.8.5",
#        "laminas/laminas-stdlib": "^3.2.1",
#        "laminas/laminas-view": "^2.10",
#        "laminas/laminas-zendframework-bridge": "^1.0"
Requires:       php(language) >= 5.6
Requires:      (php-autoloader(%{gh_owner}/laminas-mvc)                  >= 3.0    with php-autoloader(%{gh_owner}/laminas-mvc)                  < 4)
Requires:      (php-autoloader(%{gh_owner}/laminas-session)              >= 2.8.5  with php-autoloader(%{gh_owner}/laminas-session)              < 3)
Requires:      (php-autoloader(%{gh_owner}/laminas-stdlib)               >= 3.2.1  with php-autoloader(%{gh_owner}/laminas-stdlib)               < 4)
Requires:      (php-autoloader(%{gh_owner}/laminas-view)                 >= 2.10   with php-autoloader(%{gh_owner}/laminas-view)                 < 3)
Requires:      (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.0    with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
# From composer, "suggests": {
#        "laminas/laminas-i18n": "Laminas\\I18n component"
Suggests:       php-autoloader(%{gh_owner}/laminas-i18n)
# Autoloader
Requires:       php-composer(fedora/autoloader)
# From phpcompatinfo report for version 1.2.0
Requires:       php-spl

# Compatibily ensure by the bridge
Obsoletes:      php-zendframework-%{zf_name}              < 1.2.0-99
Provides:       php-zendframework-%{zf_name}              = %{version}-99
Provides:       php-composer(%{gh_owner}/%{gh_project})   = %{version}
Provides:       php-composer(zendframework/%{zf_name})    = %{version}
Provides:       php-autoloader(%{gh_owner}/%{gh_project}) = %{version}
Provides:       php-autoloader(zendframework/%{zf_name})  = %{version}


%description
Flash messages derive from Rails, and are used to expose messages from one
action to the next, after which they are cleared; a typical use case is with
Post/Redirect/Get, where they are created in the POST handler, and then
displayed by the GET handler to indicate success or failure to the end-user.

This component provides a flash messenger controller plugin for laminas-mvc
versions 3.0 and up.

Documentation: https://docs.laminas.dev/%{gh_project}/


%prep
%setup -q -n %{gh_project}-%{gh_commit}

mv LICENSE.md LICENSE


%build
: Generate autoloader
phpab --template fedora --output src/autoload.php src
cat << 'EOF' | tee -a src/autoload.php
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/%{namespace}/Mvc/autoload.php',
    '%{php_home}/%{namespace}/Session/autoload.php',
    '%{php_home}/%{namespace}/Stdlib/autoload.php',
    '%{php_home}/%{namespace}/View/autoload.php',
]);
\Fedora\Autoloader\Dependencies::optional([
    '%{php_home}/%{namespace}/I18n/autoload.php',
]);
EOF

cat << 'EOF' | tee zf.php
<?php
require_once '%{php_home}/Fedora/Autoloader/autoload.php';
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/%{namespace}/ZendFrameworkBridge/autoload.php',
    dirname(dirname(dirname(dirname(__DIR__)))) . '/%{namespace}/%{library}/%{subproj}/%{subsubp}/autoload.php',
]);
EOF


%install
: Laminas library
mkdir -p   %{buildroot}%{php_home}/%{namespace}/%{library}/%{subproj}
cp -pr src %{buildroot}%{php_home}/%{namespace}/%{library}/%{subproj}/%{subsubp}
 
: Zend equiv
mkdir -p      %{buildroot}%{php_home}/Zend/%{library}/%{subproj}/%{subsubp}
cp -pr zf.php %{buildroot}%{php_home}/Zend/%{library}/%{subproj}/%{subsubp}/autoload.php


%check
%if %{with_tests}
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require_once '%{buildroot}%{php_home}/%{namespace}/%{library}/%{subproj}/%{subsubp}/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('%{namespace}Test\\%{library}\\%{subproj}\\%{subsubp}\\', dirname(__DIR__) . '/test');
EOF

: check compat autoloader
php -r '
require "%{buildroot}%{php_home}/Zend/%{library}/%{subproj}/%{subsubp}/autoload.php";
exit (class_exists("\\Zend\\%{library}\\%{subproj}\\%{subsubp}\\Module") ? 0 : 1);
'

: upstream test suite
ret=0
for cmdarg in "php %{phpunit}" php72 php73 php74; do
  if which $cmdarg; then
    set $cmdarg
    $1 ${2:-%{_bindir}/phpunit7} --verbose || ret=1
  fi
done
exit $ret
%else
: Test suite disabled
%endif


%files
%license LICENSE
%doc *.md
%doc composer.json
%dir %{php_home}/Zend/%{library}/%{subproj}
     %{php_home}/Zend/%{library}/%{subproj}/%{subsubp}
%dir %{php_home}/%{namespace}/%{library}/%{subproj}
     %{php_home}/%{namespace}/%{library}/%{subproj}/%{subsubp}


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 16 2020 Remi Collet <remi@remirepo.net> - 1.2.0-1
- switch to Laminas

* Mon Oct 21 2019 Remi Collet <remi@remirepo.net> - 1.2.0-1
- update to 1.2.0
- raise dependency on zend-stdlib 3.2.1

* Thu May  3 2018 Remi Collet <remi@remirepo.net> - 1.1.0-1
- update to 1.1.0
- raise dependency on zend-session 2.8.5
- add dependency on zend-view
- use range dependencies on F27+
- switch to phpunit6 or phpunit7

* Wed Dec 13 2017 Remi Collet <remi@remirepo.net> - 1.0.0-4
- switch from zend-loader to fedora/autoloader

* Wed Jun 29 2016 Remi Collet <remi@fedoraproject.org> - 1.0.0-1
- initial package


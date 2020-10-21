# remirepo/Fedora spec file for php-laminas-mvc-plugins
#
# Copyright (c) 2016-2020 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global gh_commit    896104a57c3898c2ca932c1ec10c6a3afea2f815
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     laminas
%global gh_project   laminas-mvc-plugins
%global zf_name      zend-mvc-plugins
%global php_home     %{_datadir}/php
%global namespace    Laminas
%global library      Mvc
%global subproj      Plugin

Name:           php-%{gh_project}
Version:        1.0.1
Release:        3%{?dist}
Summary:        %{namespace} Framework %{library}/%{subproj} component

License:        BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{name}-%{version}-%{gh_short}.tar.gz

BuildArch:      noarch
# For test
BuildRequires:  php-cli
BuildRequires: (php-autoloader(%{gh_owner}/laminas-mvc-plugin-fileprg)        >= 1.0    with php-autoloader(%{gh_owner}/laminas-mvc-plugin-fileprg)        < 2)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-mvc-plugin-flashmessenger) >= 1.0    with php-autoloader(%{gh_owner}/laminas-mvc-plugin-flashmessenger) < 2)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-mvc-plugin-identity)       >= 1.0    with php-autoloader(%{gh_owner}/laminas-mvc-plugin-identity)       < 2)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-mvc-plugin-prg)            >= 1.0    with php-autoloader(%{gh_owner}/laminas-mvc-plugin-prg)            < 2)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-zendframework-bridge)      >= 1.0    with php-autoloader(%{gh_owner}/laminas-zendframework-bridge)      < 2)

# From composer, "require": {
#        "php": "^5.6 || ^7.0",
#        "laminas/laminas-mvc-plugin-fileprg": "^1.0",
#        "laminas/laminas-mvc-plugin-flashmessenger": "^1.0",
#        "laminas/laminas-mvc-plugin-identity": "^1.0",
#        "laminas/laminas-mvc-plugin-prg": "^1.0",
#        "laminas/laminas-zendframework-bridge": "^1.0"
Requires:       php(language) >= 5.6
Requires:      (php-autoloader(%{gh_owner}/laminas-mvc-plugin-fileprg)        >= 1.0    with php-autoloader(%{gh_owner}/laminas-mvc-plugin-fileprg)        < 2)
Requires:      (php-autoloader(%{gh_owner}/laminas-mvc-plugin-flashmessenger) >= 1.0    with php-autoloader(%{gh_owner}/laminas-mvc-plugin-flashmessenger) < 2)
Requires:      (php-autoloader(%{gh_owner}/laminas-mvc-plugin-identity)       >= 1.0    with php-autoloader(%{gh_owner}/laminas-mvc-plugin-identity)       < 2)
Requires:      (php-autoloader(%{gh_owner}/laminas-mvc-plugin-prg)            >= 1.0    with php-autoloader(%{gh_owner}/laminas-mvc-plugin-prg)            < 2)
Requires:      (php-autoloader(%{gh_owner}/laminas-zendframework-bridge)      >= 1.0    with php-autoloader(%{gh_owner}/laminas-zendframework-bridge)      < 2)

# Compatibily ensure by the bridge
Obsoletes:      php-zendframework-%{zf_name}              < 1.0.1-99
Provides:       php-zendframework-%{zf_name}              = %{version}-99
Provides:       php-composer(%{gh_owner}/%{gh_project})   = %{version}
Provides:       php-composer(zendframework/%{zf_name})    = %{version}
Provides:       php-autoloader(%{gh_owner}/%{gh_project}) = %{version}
Provides:       php-autoloader(zendframework/%{zf_name})  = %{version}


%description
%{gh_project} is a metapackage that provides a single package for
installing all official laminas-mvc plugins shipped as separate packages
under the laminas organization. Currently, these include:

* laminas/laminas-mvc-plugin-fileprg
* laminas/laminas-mvc-plugin-flashmessenger
* laminas/laminas-mvc-plugin-identity
* laminas/laminas-mvc-plugin-prg


%prep
%setup -q -n %{gh_project}-%{gh_commit}

mv LICENSE.md LICENSE


%build
: Create autoloader
cat << 'EOF' | tee autoload.php
<?php
require_once '/usr/share/php/Fedora/Autoloader/autoload.php';
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/%{namespace}/Mvc/Plugin/FilePrg/autoload.php',
    '%{php_home}/%{namespace}/Mvc/Plugin/FlashMessenger/autoload.php',
    '%{php_home}/%{namespace}/Mvc/Plugin/Identity/autoload.php',
    '%{php_home}/%{namespace}/Mvc/Plugin/Prg/autoload.php',
]);
EOF

cat << 'EOF' | tee zf.php
<?php
require_once '%{php_home}/Fedora/Autoloader/autoload.php';
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/%{namespace}/ZendFrameworkBridge/autoload.php',
    dirname(dirname(dirname(__DIR__))) . '/%{namespace}/%{library}/%{subproj}/autoload.php',
]);
EOF


%install
: Laminas library
install -Dpm 644 autoload.php %{buildroot}%{php_home}/%{namespace}/%{library}/%{subproj}/autoload.php

: Zend equiv
install -Dpm 644 zf.php %{buildroot}%{php_home}/Zend/%{library}/%{subproj}/autoload.php


%check
: Ensure autoloader works
php -r '
require "%{buildroot}%{php_home}/%{namespace}/%{library}/%{subproj}/autoload.php";
exit (class_exists("\\%{namespace}\\%{library}\\%{subproj}\\Prg\\Module") ? 0 : 1);
'

: check compat autoloader
php -r '
require "%{buildroot}%{php_home}/Zend/%{library}/%{subproj}/autoload.php";
exit (class_exists("\\Zend\\%{library}\\%{subproj}\\FilePrg\\Module") ? 0 : 1);
'


%files
%license LICENSE
%doc *.md
%doc composer.json
%{php_home}/Zend/%{library}/%{subproj}/autoload.php
%{php_home}/%{namespace}/%{library}/%{subproj}/autoload.php


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 15 2020 Remi Collet <remi@remirepo.net> - 1.0.1-1
- switch to Laminas
- use range dependencies

* Tue Dec 12 2017 Remi Collet <remi@remirepo.net> - 1.0.1-5
- switch to fedora/autoloader

* Tue Jul 26 2016 Remi Collet <remi@fedoraproject.org> - 1.0.1-2
- fix summary and description

* Wed Jun 29 2016 Remi Collet <remi@fedoraproject.org> - 1.0.1-1
- initial package


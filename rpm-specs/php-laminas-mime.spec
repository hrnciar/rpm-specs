# remirepo/Fedora spec file for php-laminas-mime
#
# Copyright (c) 2015-2020 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
# When build without laminas-mail
%global bootstrap    0
%global gh_commit    e45a7d856bf7b4a7b5bd00d6371f9961dc233add
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     laminas
%global gh_project   laminas-mime
%global zf_name      zend-mime
%global php_home     %{_datadir}/php
%global namespace    Laminas
%global library      Mime
%global with_tests   0%{!?_without_tests:1}

Name:           php-%{gh_project}
Version:        2.7.4
Release:        1%{?dist}
Summary:        %{namespace} Framework %{library} component

License:        BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{gh_commit}/%{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
# Tests
%if %{with_tests}
BuildRequires:  php(language) >= 5.6
BuildRequires:  php-iconv
BuildRequires:  php-pcre
BuildRequires:  php-spl
# From composer, "require-dev": {
#        "laminas/laminas-coding-standard": "~1.0.0",
#        "laminas/laminas-mail": "^2.6",
#        "phpunit/phpunit": "^5.7.27 || ^6.5.14 || ^7.5.20"
BuildRequires: (php-autoloader(%{gh_owner}/laminas-stdlib)               >= 3.0   with php-autoloader(%{gh_owner}/laminas-stdlib)               < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.0   with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
%if ! %{bootstrap}
BuildRequires: (php-autoloader(%{gh_owner}/laminas-mail)                 >= 2.6   with php-autoloader(%{gh_owner}/laminas-mail)                 < 3)
%endif
%global phpunit %{_bindir}/phpunit7
BuildRequires:  phpunit7 >= 7.5.20
%endif
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer, "require": {
#        "php": "^5.6 || ^7.0",
#        "laminas/laminas-stdlib": "^2.7 || ^3.0",
#        "laminas/laminas-zendframework-bridge": "^1.0"
Requires:       php(language) >= 5.6
Requires:      (php-autoloader(%{gh_owner}/laminas-stdlib)               >= 3.0    with php-autoloader(%{gh_owner}/laminas-stdlib)              < 4)
Requires:      (php-autoloader(%{gh_owner}/laminas-zendframework-bridge) >= 1.0   with php-autoloader(%{gh_owner}/laminas-zendframework-bridge) < 2)
# From composer, "suggest": {
#        "laminas/laminas-mail": "Laminas\\Mail component"
Suggests:       php-composer(%{gh_owner}/laminas-mail)
# Autoloader
Requires:       php-composer(fedora/autoloader)
# From phpcompatinfo report for version 2.7.2
Requires:       php-iconv
Requires:       php-pcre
Requires:       php-spl

# Compatibily ensure by the bridge
Obsoletes:      php-zendframework-%{zf_name}              < 2.7.3
Provides:       php-zendframework-%{zf_name}              = %{version}
Provides:       php-composer(%{gh_owner}/%{gh_project})   = %{version}
Provides:       php-composer(zendframework/%{zf_name})    = %{version}
Provides:       php-autoloader(%{gh_owner}/%{gh_project}) = %{version}
Provides:       php-autoloader(zendframework/%{zf_name})  = %{version}


%description
%{namespace}\Mime is a support class for handling multipart MIME messages.
It is used by %{namespace}\Mail and %{namespace}\Mime\Message and may be used by
applications requiring MIME support.

Documentation: https://docs.laminas.dev/%{gh_project}/


%prep
%setup -q -n %{gh_project}-%{gh_commit}

mv LICENSE.md LICENSE


%build
: Create autoloader
phpab --template fedora --output src/autoload.php src
cat << 'EOF' | tee -a src/autoload.php
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/%{namespace}/Stdlib/autoload.php',
]);
\Fedora\Autoloader\Dependencies::optional([
    '%{php_home}/%{namespace}/Mail/autoload.php',
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

: check compat autoloader
php -r '
require "%{buildroot}%{php_home}/Zend/%{library}/autoload.php";
exit (class_exists("\\Zend\\%{library}\\Mime") ? 0 : 1);
'

%if %{bootstrap}
rm test/MessageTest.php
rm test/DecodeTest.php
%endif

: upstream test suite
ret=0
for cmd in "php %{phpunit}" php72 php73 php74; do
  if which $cmd; then
    set $cmd
    $1 ${2:-%{_bindir}/phpunit7} \
%if %{bootstrap}
      --filter '^((?!(testFromMessageDecode|testFromMessageMultiPart)).)*$' \
%endif
      --verbose || ret=1
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
%{php_home}/Zend/%{library}
%{php_home}/%{namespace}/%{library}


%changelog
* Mon Mar 30 2020 Remi Collet <remi@remirepo.net> - 2.7.4-1
- update to 2.7.4 (no change)
- not bootstrap build

* Fri Mar  6 2020 Remi Collet <remi@remirepo.net> - 2.7.3-1
- update to 2.7.3
- switch to phpunit7

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Remi Collet <remi@remirepo.net> - 2.7.2-2
- cleanup

* Thu Jan  9 2020 Remi Collet <remi@remirepo.net> - 2.7.2-1
- switch to Laminas
- bootstrap build without mail

* Thu Oct 17 2019 Remi Collet <remi@remirepo.net> - 2.7.2-1
- update to 2.7.2

* Tue May 15 2018 Remi Collet <remi@remirepo.net> - 2.7.1-2
- update to 2.7.1
- use range dependencies on F27+

* Mon Dec 11 2017 Remi Collet <remi@remirepo.net> - 2.7.0-2
- switch from zend-loader to fedora/autoloader

* Wed Nov 29 2017 Remi Collet <remi@remirepo.net> - 2.7.0-1
- Update to 2.7.0
- raise dependency on PHP 5.6
- use phpunit6 on F26+

* Mon Jan 16 2017 Remi Collet <remi@fedoraproject.org> - 2.6.1-1
- update to 2.6.1

* Thu Apr 21 2016 Remi Collet <remi@fedoraproject.org> - 2.6.0-1
- update to 2.6.0
- raise dependency on PHP >= 5.5
- raise dependency on zend-stdlib >= 2.7

* Tue Aug  4 2015 Remi Collet <remi@fedoraproject.org> - 2.5.1-1
- initial package

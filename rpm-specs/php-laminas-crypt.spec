# remirepo/Fedora spec file for php-laminas-crypt
#
# Copyright (c) 2015-2020 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global bootstrap    0
%global gh_commit    5f5dfe3ca08c965cc1f44f95831a83a81a93bf78
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     laminas
%global gh_project   laminas-crypt
%global zf_name      zend-crypt
%global php_home     %{_datadir}/php
%global namespace    Laminas
%global library      Crypt
%if %{bootstrap}
%global with_tests   0%{?_with_tests:1}
%else
%global with_tests   0%{!?_without_tests:1}
%endif

Name:           php-%{gh_project}
Version:        3.3.1
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
BuildRequires:  php-mbstring
BuildRequires:  php-hash
BuildRequires:  php-openssl
BuildRequires:  php-pcre
BuildRequires:  php-spl
# From composer, "require-dev": {
#        "laminas/laminas-coding-standard": "~1.0.0",
#        "phpunit/phpunit": "^5.7.27 || ^6.5.8 || ^7.1.2"
BuildRequires: (php-composer(container-interop/container-interop)      >= 1.2   with php-composer(container-interop/container-interop)      < 2)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-math)               >= 3.0   with php-autoloader(%{gh_owner}/laminas-math)               < 4)
BuildRequires: (php-autoloader(%{gh_owner}/laminas-stdlib)             >= 3.1   with php-autoloader(%{gh_owner}/laminas-stdlib)             < 4)
BuildRequires: (php-composer(%{gh_owner}/laminas-zendframework-bridge) >= 1.0   with php-composer(%{gh_owner}/laminas-zendframework-bridge) < 2)
%global phpunit %{_bindir}/phpunit7
BuildRequires:  phpunit7 >= 7.1.2
%endif
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer, "require": {
#        "php": "^5.6 || ^7.0",
#        "ext-mbstring": "*",
#        "container-interop/container-interop": "^1.2",
#        "laminas/laminas-math": "^3.0",
#        "laminas/laminas-stdlib": "^2.7.7 || ^3.1",
#        "laminas/laminas-zendframework-bridge": "^1.0"
Requires:       php(language) >= 5.6
Requires:       php-mbstring
%if ! %{bootstrap}
Requires:      (php-composer(container-interop/container-interop)      >= 1.2   with php-composer(container-interop/container-interop)      < 2)
Requires:      (php-autoloader(%{gh_owner}/laminas-math)               >= 3.0   with php-autoloader(%{gh_owner}/laminas-math)               < 4)
Requires:      (php-autoloader(%{gh_owner}/laminas-stdlib)             >= 3.1   with php-autoloader(%{gh_owner}/laminas-stdlib)             < 4)
Requires:      (php-composer(%{gh_owner}/laminas-zendframework-bridge) >= 1.0   with php-composer(%{gh_owner}/laminas-zendframework-bridge) < 2)
# From composer, "suggest": {
#        "ext-openssl": "Required for most features of Laminas\\Crypt"
Requires:       php-openssl
# Autoloader
Requires:       php-composer(fedora/autoloader)
%endif
# From phpcompatinfo report for version 3.3.1
Requires:       php-hash
Requires:       php-pcre
Requires:       php-spl

# Compatibily ensure by the bridge
Obsoletes:      php-zendframework-%{zf_name}              < 3.3.1-99
Provides:       php-zendframework-%{zf_name}              = %{version}-99
Provides:       php-composer(%{gh_owner}/%{gh_project})   = %{version}
Provides:       php-composer(zendframework/%{zf_name})    = %{version}
Provides:       php-autoloader(%{gh_owner}/%{gh_project}) = %{version}
Provides:       php-autoloader(zendframework/%{zf_name})  = %{version}


%description
%{gh_project} provides support of some cryptographic tools.
The available features are:
* encrypt-then-authenticate using symmetric ciphers
  (the authentication step is provided using HMAC);
* encrypt/decrypt using symmetric and public key algorithm
  (e.g. RSA algorithm);
* generate digital sign using public key algorithm (e.g. RSA algorithm);
* key exchange using the Diffie-Hellman method;
* key derivation function (e.g. using PBKDF2 algorithm);
* secure password hash (e.g. using Bcrypt algorithm);
* generate Hash values;
* generate HMAC values;

The main scope of this component is to offer an easy and secure way
to protect and authenticate sensitive data in PHP.

Documentation: https://docs.laminas.dev/%{gh_project}/


%prep
%setup -q -n %{gh_project}-%{gh_commit}

mv LICENSE.md LICENSE

%build
: Create autoloader
phpab --template fedora --output src/autoload.php src
cat << 'EOF' | tee -a src/autoload.php
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/%{namespace}/Math/autoload.php',
    '%{php_home}/%{namespace}/Stdlib/autoload.php',
    '%{php_home}/Interop/Container/autoload.php',
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
for cmdarg in "php %{phpunit}" php72 php73 php74; do
  if which $cmdarg; then
    set $cmdarg
    $1 ${2:-%{_bindir}/phpunit7} \
      --filter '^((?!(testCcmEncryptWithTagSize|testIsSupportedAndCache)).)*$' \
      --verbose || ret=1
  fi
done

: check compat autoloader
php -r '
require "%{buildroot}%{php_home}/Zend/%{library}/autoload.php";
exit (class_exists("\\Zend\\%{library}\\Hash") ? 0 : 1);
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
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Remi Collet <remi@remirepo.net> - 3.3.1-2
- cleanup

* Tue Jan  7 2020 Remi Collet <remi@remirepo.net> - 3.3.1-1
- switch to Laminas

* Wed May 15 2019 Remi Collet <remi@remirepo.net> - 3.3.1-1
- update to 3.3.1

* Thu Apr 26 2018 Remi Collet <remi@remirepo.net> - 3.3.0-1
- update to 3.3.0
- raise dependency on container-interop/container-interop 1.2
- switch to phpunit6 or phpunit7
- use range dependencies on F27+

* Mon Dec  4 2017 Remi Collet <remi@remirepo.net> - 3.2.1-3
- switch from zend-loader to fedora/autoloader

* Wed Nov  8 2017 Remi Collet <remi@remirepo.net> - 3.2.1-2
- fix erratic FTBFS from Koschei, ignore 1 failed test on arm
  https://github.com/zendframework/zend-crypt/issues/53

* Fri Aug  4 2017 Remi Collet <remi@remirepo.net> - 3.2.1-1
- Update to 3.2.1

* Wed Dec  7 2016 Remi Collet <remi@fedoraproject.org> - 3.2.0-1
- update to 3.2.0

* Fri Aug 12 2016 Remi Collet <remi@fedoraproject.org> - 3.1.0-1
- update to 3.1.0

* Wed Jun 29 2016 Remi Collet <remi@fedoraproject.org> - 3.0.0-1
- update to 3.0.0 for ZendFramework 3
- add dependencies autoloader
- raise dependency on PHP 5.6
- raise dependency on zend-math 3.0

* Thu Feb  4 2016 Remi Collet <remi@fedoraproject.org> - 2.6.0-1
- update to 2.6.0
- raise dependency on zend-math ~2.6
- raise dependency on zend-stdlib ~2.7
- drop dependency on zend-servicemanager
- add dependency on container-interop/container-interop

* Wed Nov 25 2015 Remi Collet <remi@fedoraproject.org> - 2.5.2-1
- update to 2.5.2
- raise dependency on PHP 5.5

* Wed Aug  5 2015 Remi Collet <remi@fedoraproject.org> - 2.5.1-2
- fix dependencies

* Tue Aug  4 2015 Remi Collet <remi@fedoraproject.org> - 2.5.1-1
- initial package

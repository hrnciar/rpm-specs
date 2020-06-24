# remirepo/fedora spec file for php-composer-ca-bundle
#
# Copyright (c) 2016-2019 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global gh_commit    95c63ab2117a72f48f5a55da9740a3273d45b7fd
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     composer
%global gh_project   ca-bundle
%global php_home     %{_datadir}/php
%global with_tests   0%{!?_without_tests:1}

Name:           php-composer-ca-bundle
Version:        1.2.7
Release:        1%{?dist}
Summary:        Lets you find a path to the system CA

License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
# git snapshot to get everything, despite .gitattributes
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

# Never bundle a CA file
Patch0:         %{name}-rpm.patch

BuildArch:      noarch
%if %{with_tests}
BuildRequires:  php(language) >= 5.3.2
BuildRequires:  php-openssl
BuildRequires:  php-pcre
BuildRequires:  php-cli
# From composer.json, "require": {
#        "phpunit/phpunit": "^4.8.35 || ^5.7 || 6.5 - 8",
#        "psr/log": "^1.0",
#        "symfony/process": "^2.5 || ^3.0 || ^4.0 || ^5.0"
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
BuildRequires:  phpunit6
%global phpunit %{_bindir}/phpunit8
BuildRequires: (php-composer(psr/log)         >= 1.0   with php-composer(psr/log)         < 2)
BuildRequires: (php-composer(symfony/process) >= 2.5   with php-composer(symfony/process) < 6)
%else
BuildRequires:  phpunit
%global phpunit %{_bindir}/phpunit
BuildRequires:  php-PsrLog
BuildRequires:  php-symfony-process
%endif
# Autoloader
BuildRequires:  php-composer(fedora/autoloader)
# ca-certificates
BuildRequires:  %{_sysconfdir}/pki/tls/certs/ca-bundle.crt
%endif

# From composer.json, "require": {
#        "ext-openssl": "*",
#        "ext-pcre": "*",
#        "php": "^5.3.2 || ^7.0 || ^8.0"
Requires:       php(language) >= 5.3.2
Requires:       php-openssl
Requires:       php-pcre
# From phpcompatinfo report for version 1.0.3
#nothing
# Autoloader
Requires:       php-composer(fedora/autoloader)
# ca-certificates
Requires:       %{_sysconfdir}/pki/tls/certs/ca-bundle.crt

Provides:       php-composer(%{gh_owner}/%{gh_project}) = %{version}


%description
Small utility library that lets you find a path to the system CA bundle.

Autoloader: %{php_home}/Composer/CaBundle/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}

%patch0 -p0 -b .rpm
find src -name \*.rpm -exec rm {} \;

cat << 'EOF' | tee src/autoload.php
<?php
/* Autoloader for %{gh_owner}/%{gh_project} and its dependencies */

require_once '%{php_home}/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('Composer\\CaBundle\\', __DIR__);
EOF


%build
# Empty build section, most likely nothing required.


%install
: Library
mkdir -p   %{buildroot}%{php_home}/Composer/
cp -pr src %{buildroot}%{php_home}/Composer/CaBundle


%check
%if %{with_tests}
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require_once '%{buildroot}%{php_home}/Composer/CaBundle/autoload.php';
\Fedora\Autoloader\Dependencies::required(array(
    array(
        '%{php_home}/Symfony5/Component/Process/autoload.php',
        '%{php_home}/Symfony4/Component/Process/autoload.php',
        '%{php_home}/Symfony3/Component/Process/autoload.php',
        '%{php_home}/Symfony/Component/Process/autoload.php',
    ),
    '%{php_home}/Psr/Log/autoload.php',
));
EOF

ret=0
for cmdarg in "php %{phpunit}" "php56 %{_bindir}/phpunit" "php70  %{_bindir}/phpunit6" "php71  %{_bindir}/phpunit7" php72 php73 php74; do
  if which $cmdarg; then
    set $cmdarg
    $1 ${2:-%{_bindir}/phpunit8} --verbose || ret=1
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
%doc *.md
%dir %{php_home}/Composer
     %{php_home}/Composer/CaBundle


%changelog
* Wed Apr  8 2020 Remi Collet <remi@remirepo.net> - 1.2.7-1
- update to 1.2.7

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 14 2020 Remi Collet <remi@remirepo.net> - 1.2.6-1
- update to 1.2.6

* Thu Dec 12 2019 Remi Collet <remi@remirepo.net> - 1.2.5-1
- update to 1.2.5

* Sun Sep  1 2019 Remi Collet <remi@remirepo.net> - 1.2.4-1
- update to 1.2.4 (no change)

* Sat Aug  3 2019 Remi Collet <remi@remirepo.net> - 1.2.3-1
- update to 1.2.3

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 29 2019 Remi Collet <remi@remirepo.net> - 1.1.4-1
- update to 1.1.4 (no change)

* Thu Oct 18 2018 Remi Collet <remi@remirepo.net> - 1.1.3-1
- update to 1.1.3 (no change)

* Thu Aug  9 2018 Remi Collet <remi@remirepo.net> - 1.1.2-1
- update to 1.1.2 (no change)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 30 2018 Remi Collet <remi@remirepo.net> - 1.1.1-1
- update to 1.1.1 (no change)
- use range dependencies on F27+
- use phpunit6 on F27+

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov 30 2017 Remi Collet <remi@remirepo.net> - 1.1.0-1
- Update to 1.1.0
- allow Symfony 2, 3 and 4

* Tue Nov 14 2017 Remi Collet <remi@remirepo.net> - 1.0.9-1
- Update to 1.0.9 (no change)

* Mon Sep 11 2017 Remi Collet <remi@remirepo.net> - 1.0.8-1
- Update to 1.0.8 (no change)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Mar  6 2017 Remi Collet <remi@remirepo.net> - 1.0.7-1
- Update to 1.0.7
- run upstream test suite

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Nov  3 2016 Remi Collet <remi@fedoraproject.org> - 1.0.6-1
- update to 1.0.6 (no change)

* Wed Nov  2 2016 Remi Collet <remi@fedoraproject.org> - 1.0.5-1
- update to 1.0.5 (no change)

* Thu Oct 20 2016 Remi Collet <remi@fedoraproject.org> - 1.0.4-2
- switch from symfony/class-loader to fedora/autoloader

* Mon Sep  5 2016 Remi Collet <remi@fedoraproject.org> - 1.0.4-1
- update to 1.0.4 (no change)

* Tue Jul 19 2016 Remi Collet <remi@fedoraproject.org> - 1.0.3-1
- update to 1.0.3

* Sat Apr 30 2016 Remi Collet <remi@fedoraproject.org> - 1.0.2-1
- initial package, version 1.0.2


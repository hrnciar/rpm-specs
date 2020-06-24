# remirepo/fedora spec file for php-cs-fixer-accessible-object
#
# Copyright (c) 2017 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global gh_commit    9ef12f98c49e3b2a78a47bef74ecb37c5b6d4ea6
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
#global gh_date      20150717
%global gh_owner     PHP-CS-Fixer
%global gh_project   AccessibleObject
%global pk_vendor    php-cs-fixer
%global pk_project   accessible-object
%global ns_vendor    PhpCsFixer
%global ns_project   AccessibleObject
%global php_home     %{_datadir}/php
%global with_tests   0%{!?_without_tests:1}

Name:           %{pk_vendor}-%{pk_project}
Version:        1.0.0
Release:        9%{?dist}
Summary:        A library to reveal object internals

License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
# git snapshot to get upstream test suite
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
%if %{with_tests}
# For tests
BuildRequires:  php(language) >= 5.3
BuildRequires:  php-reflection
BuildRequires:  php-spl
# From composer.json,     "require-dev": {
#        "phpunit/phpunit": "^4.8.35 || ^5.4.3",
#        "symfony/phpunit-bridge": "^3.2.2"
BuildRequires:  php-composer(phpunit/phpunit) >= 5.4.3
BuildRequires:  php-symfony3-phpunit-bridge >= 3.2.2
# Autoloader
BuildRequires:  php-fedora-autoloader-devel
%endif

# From composer.json,     "require": {
#        "php": "^5.3 || ^7.0"
Requires:       php(language) >= 5.3
# From phpcompatinfo report for version 1.0.0
Requires:       php-reflection
Requires:       php-spl
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}


%description
AccessibleObject is small class allowing you to easily access internals
of any object. In general, it's bad practice to do so. While we strongly
discourage you to using it, it may be helpful in debugging or testing
old, sad, legacy projects.

Autoloader: %{php_home}/%{ns_vendor}/%{ns_project}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}

cat << 'EOF' | tee src/autoload.php
<?php
/* autoloader for %{name} */

\Fedora\Autoloader\Autoload::addPsr4('PhpCsFixer\\AccessibleObject\\', __DIR__);
EOF


%build
# Empty build section, most likely nothing required.


%install
: Library
mkdir -p   %{buildroot}%{php_home}/%{ns_vendor}
cp -pr src %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}


%check
%if %{with_tests}
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require '%{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}/autoload.php';

\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/Symfony3/Bridge/PhpUnit/autoload.php',
]);
\Fedora\Autoloader\Autoload::addPsr4('PhpCsFixer\\AccessibleObject\\Tests\\', dirname(__DIR__) . '/tests');
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
%doc composer.json
%doc *.md
%dir %{php_home}/%{ns_vendor}
     %{php_home}/%{ns_vendor}/%{ns_project}


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov  8 2017 Remi Collet <remi@remirepo.net> - 1.0.0-4
- fix FTBFS from Koschei
- use package name for symfony/phpunit-bridge

* Wed Aug 23 2017 Remi Collet <remi@remirepo.net> - 1.0.0-3
- fix PHP minimal version

* Wed Aug 23 2017 Remi Collet <remi@remirepo.net> - 1.0.0-2
- fix dependency

* Wed Aug 23 2017 Remi Collet <remi@remirepo.net> - 1.0.0-1
- initial package, version 1.0.0

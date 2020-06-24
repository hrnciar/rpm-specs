# remirepo/fedora spec file for php-jeremeamia-superclosure
#
# Copyright (c) 2015-2018 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
# Github
%global gh_commit    5707d5821b30b9a07acfb4d76949784aaa0e9ce9
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     jeremeamia
%global gh_project   super_closure
# Packagist
%global pk_vendor    jeremeamia
%global pk_name      superclosure
# PSR-0 namespace
%global namespace    SuperClosure

Name:           php-%{pk_vendor}-%{pk_name}
Version:        2.4.0
Release:        5%{?dist}
Summary:        Serialize Closure objects, including their context and binding

License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
# Create git snapshot as tests are excluded from official tarball
Source1:        makesrc.sh
# Autoloader
Source2:        %{name}-autoload.php

BuildArch:      noarch
BuildRequires:  php(language) >= 5.4
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
BuildRequires:  (php-composer(nikic/php-parser)       >= 1.4  with php-composer(nikic/php-parser) < 5)
BuildRequires:  (php-composer(symfony/polyfill-php56) >= 1.0  with php-composer(symfony/polyfill-php56) < 2)
%else
BuildRequires:  php-nikic-php-parser3
BuildRequires:  php-symfony-polyfill
%endif
# From composer.json, "require-dev": {
#        "phpunit/phpunit": "^4.0|^5.0",
BuildRequires:  php-composer(phpunit/phpunit)  >= 4.0
# Autoloader
BuildRequires:  php-composer(fedora/autoloader)

# From composer.json, "require": {
#        "php": ">=5.4",
#        "nikic/php-parser": "^1.2|^2.0|^3.0|^4.0",
#        "symfony/polyfill-php56": "^1.0"
# php-parser 1.4 for autoloader
Requires:       php(language) >= 5.4
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
Requires:       (php-composer(nikic/php-parser)       >= 1.4  with php-composer(nikic/php-parser) < 5)
Requires:       (php-composer(symfony/polyfill-php56) >= 1.0  with php-composer(symfony/polyfill-php56) < 2)
%else
Requires:       php-nikic-php-parser3
Requires:       php-symfony-polyfill
%endif
# From phpcompatifo report for 2.1.0
Requires:       php-hash
Requires:       php-reflection
Requires:       php-spl
Requires:       php-tokenizer
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_vendor}/%{pk_name}) = %{version}


%description
Even though serializing closures is "not allowed" by PHP,
the SuperClosure library makes it possible

To use this library, you just have to add, in your project:
  require-once '%{_datadir}/php/%{namespace}/autoload.php';


%prep
%setup -q -n %{gh_project}-%{gh_commit}
install -pm 644 %{SOURCE2} src/autoload.php


%build
# Nothing


%install
# Restore PSR-0 tree
mkdir -p   %{buildroot}%{_datadir}/php
cp -pr src %{buildroot}%{_datadir}/php/%{namespace}


%check
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require '%{buildroot}%{_datadir}/php/%{namespace}/autoload.php';
require dirname(__DIR__) . '/tests/Integ/Fixture/Collection.php';
require dirname(__DIR__) . '/tests/Integ/Fixture/Foo.php';
EOF

: Run the test suite
ret=0
for cmd in php php70 php71 php72; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit || ret=1
  fi
done
exit $ret


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE.md
%doc README.md composer.json
%{_datadir}/php/%{namespace}


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 22 2018 Remi Collet <remi@remirepo.net> - 2.4.0-1
- update to 2.4.0
- use range dependencies on F27+ else package names
- allow nikic/php-parser v4 (not yet available)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Dec  7 2016 Remi Collet <remi@fedoraproject.org> - 2.3.0-1
- update to 2.3.0
- switch to fedora/autoloader
- allow nikic/php-parser v3

* Sat May 21 2016 Remi Collet <remi@fedoraproject.org> - 2.2.0-3
- use nikic/php-parser v2 when available

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Dec  6 2015 Remi Collet <remi@fedoraproject.org> - 2.2.0-1
- update to 2.2.0
- add dependency on symfony/polyfill-php56

* Tue Sep  1 2015 Remi Collet <remi@fedoraproject.org> - 2.1.0-1
- initial package

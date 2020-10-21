# remirepo/Fedora spec file for php-zendframework-zendpdf
#
# Copyright (c) 2015-2018 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global gh_commit    041f90c339cff63a3c4d03a28ef1ea5188059793
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     zendframework
%global gh_project   zendpdf
%global php_home     %{_datadir}/php
%global library      ZendPdf
%global with_tests   0%{!?_without_tests:1}

Name:           php-%{gh_owner}-%{gh_project}
Version:        2.0.2
Release:        13%{?dist}
Summary:        Zend Framework %{library} component

License:        BSD
URL:            https://framework.zend.com/
Source0:        %{gh_commit}/%{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

Patch0:         https://github.com/zendframework/ZendPdf/commit/ded3ffc0a0485d3b34e440a293fe1fbbe14a01ff.patch

BuildArch:      noarch
# Tests
%if %{with_tests}
BuildRequires:  php(language) >= 5.3.3
BuildRequires:  php-ctype
BuildRequires:  php-date
BuildRequires:  php-gd
BuildRequires:  php-iconv
BuildRequires:  php-mbstring
BuildRequires:  php-pcre
BuildRequires:  php-spl
BuildRequires:  php-zlib
BuildRequires:  php-composer(phpunit/phpunit)
BuildRequires:  php-autoloader(%{gh_owner}/zend-memory)         >= 2.0.0
BuildRequires:  php-autoloader(%{gh_owner}/zend-stdlib)         >= 2.0.0
%endif
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer, "require": {
#        "php": ">=5.3.3",
#        "zendframework/zend-memory": ">=2.0.0",
#        "zendframework/zend-stdlib": ">=2.0.0"
Requires:       php(language) >= 5.3.3
Requires:       php-autoloader(%{gh_owner}/zend-memory)         >= 2.0.0
Requires:       php-autoloader(%{gh_owner}/zend-stdlib)         >= 2.0.0
# Autoloader
Requires:       php-composer(fedora/autoloader)
# From phpcompatinfo report for version 1.0.1
Requires:       php-ctype
Requires:       php-date
Requires:       php-gd
Requires:       php-iconv
Requires:       php-mbstring
Requires:       php-pcre
Requires:       php-spl
Requires:       php-zlib

Provides:       php-composer(%{gh_owner}/%{gh_project}) = %{version}
Provides:       php-autoloader(%{gh_owner}/%{gh_project}) = %{version}


%description
%{summary}.


%prep
%setup -q -n %{gh_project}-%{gh_commit}
%patch0 -p1

mv LICENSE.txt LICENSE

%build
: Generate autoloader for this framework extension - deprecated
cat << 'EOF' | tee autoload.php
<?php
Zend\Loader\AutoloaderFactory::factory(array(
    'Zend\Loader\StandardAutoloader' => array(
        'namespaces' => array(
            '%{library}' => dirname(__DIR__) . '/%{library}',
))));
EOF

: Create autoloader
phpab --template fedora --output library/%{library}/autoload.php library/%{library}
cat << 'EOF' | tee -a library/%{library}/autoload.php
\Fedora\Autoloader\Dependencies::optional([
    '%{php_home}/Zend/Memory/autoload.php',
    '%{php_home}/Zend/Stdlib/autoload.php',
]);
EOF


%install
mkdir -p   %{buildroot}%{php_home}
cp -pr library/%{library} %{buildroot}%{php_home}/%{library}

install -Dpm 644 autoload.php %{buildroot}%{php_home}/Zend/%{library}-autoload.php


%check
%if %{with_tests}
mkdir vendor
cat << EOF | tee vendor/autoload.php
<?php
require_once '%{buildroot}%{php_home}/%{library}/autoload.php';
EOF

cd tests
ret=0
for cmd in php php56 php70 php71 php72 php73; do
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
%{php_home}/%{library}
%{php_home}/Zend/%{library}-autoload.php


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 15 2018 Remi Collet <remi@remirepo.net> - 2.0.2-9
- add patch for PHP 7.3 from
  https://github.com/zendframework/ZendPdf/pull/35

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Dec  6 2017 Remi Collet <remi@remirepo.net> - 2.0.2-6
- switch from zend-loader to fedora/autoloader

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 24 2017 Remi Collet <remi@fedoraproject.org> - 2.0.2-4
- rewrite autoloader as framework extension

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Aug  6 2015 Remi Collet <remi@fedoraproject.org> - 2.0.2-1
- initial package
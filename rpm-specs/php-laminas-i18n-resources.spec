# remirepo/Fedora spec file for php-laminas-i18n-resources
#
# Copyright (c) 2015-2020 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global bootstrap    0
%global gh_commit    7585cd3a4f9656814425b35689919a220c73834b
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     laminas
%global gh_project   laminas-i18n-resources
%global zf_name      zend-i18n-resources
%global php_home     %{_datadir}/php
%global namespace    Laminas
%global library      Translator
%if %{bootstrap}
%global with_tests   0%{?_with_tests:1}
%else
%global with_tests   0%{!?_without_tests:1}
%endif

Name:           php-%{gh_project}
Version:        2.6.1
Release:        3%{?dist}
Summary:        Laminas Framework %{library} component

License:        BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{gh_commit}/%{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
# Tests
%if %{with_tests}
BuildRequires:  php(language) >= 5.6
BuildRequires: (php-composer(%{gh_owner}/laminas-zendframework-bridge) >= 1.0 with php-composer(%{gh_owner}/laminas-zendframework-bridge) < 2)
# From composer, "require-dev": {
#        "laminas/laminas-coding-standard": "~1.0.0",
#        "phpunit/phpunit": "^5.7.27 || ^6.5.8 || ^7.1.5"
%global phpunit %{_bindir}/phpunit7
BuildRequires:  phpunit7 >= 7.1.2
%endif
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer, "require": {
#        "php": "^5.6 || ^7.0",
#        "laminas/laminas-zendframework-bridge": "^1.0"
Requires:       php(language) >= 5.6
Requires:      (php-composer(%{gh_owner}/laminas-zendframework-bridge) >= 1.0 with php-composer(%{gh_owner}/laminas-zendframework-bridge) < 2)
# Autoloader
Requires:       php-composer(fedora/autoloader)
# From phpcompatinfo report for version 2.6.1
# None

# Compatibily ensure by the bridge
Obsoletes:      php-zendframework-%{zf_name}              < 2.6.1-99
Provides:       php-zendframework-%{zf_name}              = %{version}-99
Provides:       php-composer(%{gh_owner}/%{gh_project})   = %{version}
Provides:       php-composer(zendframework/%{zf_name})    = %{version}
Provides:       php-autoloader(%{gh_owner}/%{gh_project}) = %{version}
Provides:       php-autoloader(zendframework/%{zf_name})  = %{version}


%description
%{gh_project} provides translation resources, specifically
for laminas-validate and laminas-captcha,
for use with laminas-i18n's Translator subcomponent.

Documentation: https://docs.laminas.dev/%{gh_project}/


%prep
%setup -q -n %{gh_project}-%{gh_commit}

mv LICENSE.md LICENSE


%build
: Create autoloader
phpab --template fedora --output src/autoload.php src

cat << 'EOF' | tee zf.php
<?php
require_once '%{php_home}/Fedora/Autoloader/autoload.php';
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/%{namespace}/ZendFrameworkBridge/autoload.php',
    dirname(dirname(dirname(__DIR__))) . '/%{namespace}/I18n/%{library}/autoload.php',
]);
EOF


%install
: Laminas library
mkdir -p         %{buildroot}%{php_home}/%{namespace}/I18n
cp -pr src       %{buildroot}%{php_home}/%{namespace}/I18n/%{library}
cp -pr languages %{buildroot}%{php_home}/%{namespace}/I18n/languages

: Zend equiv
mkdir -p      %{buildroot}%{php_home}/Zend/I18n/%{library}
cp -pr zf.php %{buildroot}%{php_home}/Zend/I18n/%{library}/autoload.php
 

%check
%if %{with_tests}
mkdir vendor
cat << EOF | tee vendor/autoload.php
<?php
require_once '%{buildroot}%{php_home}/%{namespace}/I18n/%{library}/autoload.php';
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
require "%{buildroot}%{php_home}/Zend/I18n/%{library}/autoload.php";
exit (class_exists("\\Zend\\I18n\\%{library}\\Resources") ? 0 : 1);
'

exit $ret
%else
: Test suite disabled
%endif


%files
%license LICENSE
%doc *.md
%doc composer.json
%dir %{php_home}/Zend/I18n
     %{php_home}/Zend/I18n/%{library}
%dir %{php_home}/%{namespace}/I18n
     %{php_home}/%{namespace}/I18n/%{library}
     %{php_home}/%{namespace}/I18n/languages


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Remi Collet <remi@remirepo.net> - 2.6.1-2
- cleanup

* Tue Jan  7 2020 Remi Collet <remi@remirepo.net> - 2.6.1-1
- switch to Laminas

* Tue Jun 25 2019 Remi Collet <remi@remirepo.net> - 2.6.1-1
- update to 2.6.1

* Wed May  2 2018 Remi Collet <remi@remirepo.net> - 2.6.0-1
- update to 2.6.0
- raise dependency on PHP 5.6
- run upstream test suite

* Tue Dec  5 2017 Remi Collet <remi@remirepo.net> - 2.5.2-5
- switch from zend-loader to fedora/autoloader

* Thu Aug  6 2015 Remi Collet <remi@fedoraproject.org> - 2.5.2-1
- version 2.5.2

* Tue Aug  4 2015 Remi Collet <remi@fedoraproject.org> - 2.5.1-1
- initial package

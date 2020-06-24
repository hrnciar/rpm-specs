# remirepo/fedora spec file for php-cs-fixer-phpunit-constraint-xmlmatchesxsd
#
# Copyright (c) 2018-2019 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global gh_commit    92e0ca8fd30b257a993a66511198267ca7d9d8eb
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
#global gh_date      20150717
%global gh_owner     PHP-CS-Fixer
%global gh_project   phpunit-constraint-xmlmatchesxsd
%global pk_vendor    php-cs-fixer
%global pk_project   %{gh_project}
%global ns_vendor    PhpCsFixer
%global ns_project   PhpunitConstraintXmlMatchesXsd
%global php_home     %{_datadir}/php
%global with_tests   0%{!?_without_tests:1}

Name:           %{pk_vendor}-%{pk_project}
Version:        1.1.0
Release:        3%{?dist}
Summary:        Constraint for testing XML against XSD

License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
# git snapshot to get upstream test suite
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
%if %{with_tests}
# For tests
BuildRequires:  php(language) >= 5.5
BuildRequires:  php-dom
BuildRequires:  php-libxml
# From composer.json,     "require-dev": {
#        "johnkary/phpunit-speedtrap": "^1.1 || ^2.0 || ^3.0",
#        "symfony/phpunit-bridge": "^3.2.2 || ^4.0"
# ignore phpunit listeners
%if 0%{?fedora} >= 29 || 0%{?rhel} >= 8
BuildRequires:  phpunit8
%endif
%if 0%{?fedora} >= 28 || 0%{?rhel} >= 8
BuildRequires:  phpunit7
%endif
BuildRequires: (php-composer(phpunitgoodpractices/polyfill) >= 1.1   with php-composer(phpunitgoodpractices/polyfill) < 2)
BuildRequires:  phpunit6 >= 6.4.3
BuildRequires:  php-composer(phpunit/phpunit) >= 5.7.23
# Autoloader
BuildRequires:  php-fedora-autoloader-devel
%endif

# From composer.json,     "require": {
#        "php": "^5.5 || ^7.0",
#        "ext-dom": "*",
#        "ext-libxml": "*",
#        "phpunit/phpunit": "^5.7.23 || ^6.4.3 || ^7.0 || ^8.0",
#        "phpunitgoodpractices/polyfill": "^1.1"
Requires:       php(language) >= 5.5
Requires:       php-dom
Requires:       php-libxml
Requires:      (php-composer(phpunitgoodpractices/polyfill) >= 1.1   with php-composer(phpunitgoodpractices/polyfill) < 2)
# ignore phpunit dep, package using it will run the proper phpunit command (and autoloader)
# From phpcompatinfo report for version 1.0.0
# nothing
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}


%description
Constraint for testing XML against XSD.

Autoloader: %{php_home}/%{ns_vendor}/%{ns_project}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}

cat << 'EOF' | tee src/autoload.php
<?php
/* autoloader for %{name} */

\Fedora\Autoloader\Autoload::addPsr4('%{ns_vendor}\\%{ns_project}\\', __DIR__);
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/PHPUnitGoodPractices/Polyfill/autoload.php',
    __DIR__ . '/Constraint/XmlMatchesXsd.php',
]);
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
EOF

: Disable the listeners
sed -e '/<listeners>/,/<\/listeners>/d' phpunit.xml.dist >phpunit.xml

: Run upstream test suite with each available phpunit version
ret=0
if [ -x %{_bindir}/phpunit ]; then
  for cmd in php php56 php70 php71 php72; do
    if which $cmd; then
      $cmd %{_bindir}/phpunit --verbose || ret=1
    fi
  done
fi
if [ -x %{_bindir}/phpunit6 ]; then
  for cmd in php php70 php71 php72; do
    if which $cmd; then
      $cmd %{_bindir}/phpunit6 --verbose || ret=1
    fi
  done
fi
if [ -x %{_bindir}/phpunit7 ]; then
  for cmd in php php71 php72; do
    if which $cmd; then
      $cmd %{_bindir}/phpunit7 --verbose || ret=1
    fi
  done
fi
if [ -x %{_bindir}/phpunit8 ]; then
  for cmd in php php72; do
    if which $cmd; then
      $cmd %{_bindir}/phpunit8 --verbose || ret=1
    fi
  done
fi
exit $ret
%else
: Test suite disabled
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc composer.json
%dir %{php_home}/%{ns_vendor}
     %{php_home}/%{ns_vendor}/%{ns_project}


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 26 2019 Remi Collet <remi@remirepo.net> - 1.1.0-1
- update to 1.1.0
- raise dependency on phpunitgoodpractices/polyfill 1.1
- allow PHPUnit 8

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 11 2018 Remi Collet <remi@remirepo.net> - 1.0.1-1
- update to 1.0.1 (no change)

* Mon Jun  4 2018 Remi Collet <remi@remirepo.net> - 1.0.0-1
- initial package, version 1.0.0
- https://github.com/PHP-CS-Fixer/phpunit-constraint-xmlmatchesxsd/issues/2
  phpunit schema

# spec file for php-sebastian-global-state2
#
# Copyright (c) 2014-2017 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global bootstrap    0
%global gh_commit    e8ba02eed7bbbb9e59e43dedd3dddeff4a56b0c4
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sebastianbergmann
%global gh_project   global-state
%global pk_vendor    sebastian
%global pk_project   %{gh_project}
%global major        2
%global php_home     %{_datadir}/php
%global ns_vendor    SebastianBergmann
%global ns_project   GlobalState
%if %{bootstrap}
%global with_tests   %{?_with_tests:1}%{!?_with_tests:0}
%else
%global with_tests   %{?_without_tests:0}%{!?_without_tests:1}
%endif

Name:           php-%{pk_vendor}-%{pk_project}%{major}
Version:        2.0.0
Release:        8%{?dist}
Summary:        Snapshotting of global state

License:        BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{name}-%{version}-%{gh_short}.tar.gz

BuildArch:      noarch
BuildRequires:  php(language) >= 7.0
BuildRequires:  php-reflection
BuildRequires:  php-spl
# Autoloader
BuildRequires:  php-fedora-autoloader-devel >= 1.0.0
%if %{with_tests}
# from composer.json, "require-dev": {
#        "phpunit/phpunit": "^6.0"
BuildRequires:  phpunit6
%endif

# from composer.json, "require": {
#        "php": "^7.0"
Requires:       php(language) >= 7.0
# from phpcompatinfo report for version 2.0.0
Requires:       php-reflection
Requires:       php-spl
# from composer.json, "suggest": {
#        "ext-uopz": "*"
%if 0%{?fedora} > 21
Suggests:       php-uopz
%endif
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}


%description
Snapshotting of global state,
factored out of PHPUnit into a stand-alone component.


%prep
%setup -q -n %{gh_project}-%{gh_commit}


%build
# Generate the Autoloader
phpab --template fedora2 --output src/autoload.php src

# For the test suite
phpab --template fedora2 --output tests/autoload.php tests/_fixture/


%install
mkdir -p   %{buildroot}%{php_home}/%{ns_vendor}
cp -pr src %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}


%check
%if %{with_tests}
mkdir vendor
cat <<EOF | tee vendor/autoload.php
<?php
require_once '%{ns_vendor}/%{ns_project}%{major}/autoload.php';
require_once 'tests/autoload.php';
require_once 'tests/_fixture/SnapshotFunctions.php';
EOF

: Run upstream test suite
ret=0
for cmd in php php70 php71 php72; do
  if which $cmd; then
   $cmd -d include_path=.:%{buildroot}%{php_home}:%{php_home} \
   %{_bindir}/phpunit6 --verbose || ret=1
  fi
done
exit $ret

%else
: bootstrap build with test suite disabled
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc README.md
%doc composer.json
%dir %{php_home}/%{ns_vendor}
     %{php_home}/%{ns_vendor}/%{ns_project}%{major}


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Apr 28 2017 Remi Collet <remi@fedoraproject.org> - 2.0.0-1
- rename to php-sebastian-global-state2
- update to 2.0.0
- raise dependency on PHP 7.0

* Fri Oct 21 2016 Remi Collet <remi@fedoraproject.org> - 1.1.1-4
- switch to fedora/autoloader

* Thu Oct 13 2016 Remi Collet <remi@fedoraproject.org> - 1.1.1-3
- add optional dependency on uopz extension

* Mon Oct 12 2015 Remi Collet <remi@fedoraproject.org> - 1.1.1-1
- update to 1.1.1

* Fri Dec  5 2014 Remi Collet <remi@fedoraproject.org> - 1.0.0-1
- initial package

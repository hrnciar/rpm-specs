# remirepo/fedora spec file for php-mock-integration
#
# Copyright (c) 2016-2017 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global gh_commit    e83fb65dd20cd3cf250d554cbd4682b96b684f4b
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     php-mock
%global gh_project   php-mock-integration
%global with_tests   0%{!?_without_tests:1}

Name:           php-mock-integration
Version:        1.0.0
Release:        11%{?dist}
Summary:        Integration package for PHP-Mock

License:        WTFPL
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{gh_project}-%{version}-%{gh_short}.tar.gz

BuildArch:      noarch
BuildRequires:  php(language) >= 5.5
%if %{with_tests}
# from composer.json, "require-dev": {
#        "phpunit/phpunit": "^4|^5"
BuildRequires:  php-composer(php-mock/php-mock)         <  2
BuildRequires:  php-composer(php-mock/php-mock)         >= 1
BuildRequires:  php-composer(phpunit/php-text-template) <  2
BuildRequires:  php-composer(phpunit/php-text-template) >= 1
BuildRequires:  php-composer(phpunit/phpunit) > 4
# For autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# from composer.json, "require": {
#        "php": ">=5.5",
#        "php-mock/php-mock": "^1",
#        "phpunit/php-text-template": "^1"
Requires:       php(language) >= 5.5
Requires:       php-composer(php-mock/php-mock)         >= 1
Requires:       php-composer(php-mock/php-mock)         <  2
Requires:       php-composer(phpunit/php-text-template) >= 1
Requires:       php-composer(phpunit/php-text-template) <  2
# From phpcompatinfo report from version 1.0.1
# only standard

Provides:       php-composer(%{gh_owner}/%{gh_project}) = %{version}


%description
This is a support package for PHP-Mock integration into other frameworks.


%prep
%setup -q -n %{gh_project}-%{gh_commit}

# Same namespace than php-mock, not specific autoloader needed


%build
# Nothing


%install
mkdir -p       %{buildroot}%{_datadir}/php/
mkdir -p       %{buildroot}%{_datadir}/php/phpmock
cp -pr classes %{buildroot}%{_datadir}/php/phpmock/integration


%check
%if %{with_tests}
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require_once '%{_datadir}/php/Fedora/Autoloader/autoload.php';
require_once '%{_datadir}/tests/phpmock/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('phpmock\\', '%{buildroot}%{_datadir}/php/phpmock');
EOF

ret=0
for cmd in php php56 php70 php71 php72; do
  if which $cmd; then
    %{_bindir}/phpunit --verbose || ret=1
  fi
done
exit $ret
%else
: bootstrap build with test suite disabled
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc composer.json
%doc *.md
%{_datadir}/php/phpmock/integration


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu May 11 2017 Remi Collet <remi@remirepo.net> - 1.0.0-4
- switch to fedora/autoloader

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Feb 22 2016 Remi Collet <remi@fedoraproject.org> - 1.0.0-2
- Fix: license is WTFPL

* Fri Feb 12 2016 Remi Collet <remi@fedoraproject.org> - 1.0.0-1
- initial package

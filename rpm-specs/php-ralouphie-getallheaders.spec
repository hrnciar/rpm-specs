#
# Fedora spec file for php-ralouphie-getallheaders
#
# Copyright (c) 2019 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     ralouphie
%global github_name      getallheaders
%global github_version   3.0.3
%global github_commit    120b605dfeb996808c31b6477290a714d356e822

%global composer_vendor  ralouphie
%global composer_project getallheaders

# "php": ">=5.6"
%global php_min_ver 5.6

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       3%{?github_release}%{?dist}
Summary:       A polyfill for getallheaders

License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}

# GitHub export does not include tests.
# Run php-ralouphie-getallheaders-get-source.sh to create full source.
Source0:       %{name}-%{github_version}-%{github_commit}.tar.gz
Source1:       %{name}-get-source.sh

BuildArch:     noarch
# Tests
%if %{with_tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: phpunit6
## phpcompatinfo for version 3.0.3
##     <none>
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
# phpcompatinfo for version 3.0.3
#     <none>

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
%{summary}.

https://www.php.net/manual/function.getallheaders.php

Autoloader: %{phpdir}/%{composer_vendor}-%{composer_project}/autoload.php


%prep
%setup -qn %{github_name}-%{github_commit}


%build
: Common autoloader
ln -s getallheaders.php src/autoload.php


%install
mkdir -p %{buildroot}%{phpdir}
cp -rp src %{buildroot}%{phpdir}/%{composer_vendor}-%{composer_project}


%check
%if %{with_tests}
: Mock Composer autoloader
mkdir vendor
ln -s %{buildroot}%{phpdir}/%{composer_vendor}-%{composer_project}/autoload.php vendor/autoload.php

: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which phpunit6)
for PHP_EXEC in php php70 php71 php72 php73 php74; do
    if [ "php" == "$PHP_EXEC" ] || which $PHP_EXEC; then
        $PHP_EXEC $PHPUNIT --verbose || RETURN_CODE=1
    fi
done
exit $RETURN_CODE
%else
: Tests skipped
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc *.md
%doc composer.json
%{phpdir}/%{composer_vendor}-%{composer_project}


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 16 2019 Shawn Iwinski <shawn@iwin.ski> - 3.0.3-1
- Update to 3.0.3
- Use PHPUnit 6

* Sun Dec 01 2019 Shawn Iwinski <shawn@iwin.ski> - 2.0.5-1
- Initial package

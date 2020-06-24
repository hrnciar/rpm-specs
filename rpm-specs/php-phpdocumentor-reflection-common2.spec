# remirepo/fedora spec file for php-phpdocumentor-reflection-common2
#
# Copyright (c) 2017-2019 Remi Collet, Shawn Iwinski
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     phpDocumentor
%global github_name      ReflectionCommon
%global github_version   2.1.0
%global github_commit    6568f4687e5b41b054365f9ae03fcb1ed5f2069b

%global composer_vendor  phpdocumentor
%global composer_project reflection-common

%global major            2

# "php": ">=7.1"
%global php_min_ver 7.1

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}%{major}
Version:       %{github_version}
Release:       1%{?github_release}%{?dist}
Summary:       Common reflection classes used by phpdocumentor

Group:         Development/Libraries
License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}
# GitHub export does not include tests.
# Run makesrc.sh to create full source.
Source0:       %{name}-%{github_version}-%{github_commit}.tar.gz
Source1:       makesrc.sh

BuildArch:     noarch
# Tests
%if %{with_tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: phpunit6
## phpcompatinfo (computed from version 2.0.0)
BuildRequires: php-pcre
BuildRequires: php-spl
## Autoloader
BuildRequires: php-fedora-autoloader-devel
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
# phpcompatinfo (computed from version 2.0.0)
Requires:      php-pcre
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
Common reflection classes used by phpdocumentor to reflect the code structure.

Autoloader: %{phpdir}/phpDocumentor/Reflection%{major}/autoload-common.php


%prep
%setup -qn %{github_name}-%{github_commit}


%build
: Create autoloader
%{_bindir}/phpab --template fedora --output src/autoload-common.php src


%install
mkdir -p %{buildroot}%{phpdir}/phpDocumentor
cp -rp src %{buildroot}%{phpdir}/phpDocumentor/Reflection%{major}


%check
%if %{with_tests}
BOOTSTRAP=%{buildroot}%{phpdir}/phpDocumentor/Reflection%{major}/autoload-common.php
mkdir vendor
touch vendor/autoload.php

: Upstream tests
RETURN_CODE=0
for PHP_EXEC in php php71 php72 php73 php74 php80; do
    if which $PHP_EXEC; then
        $PHP_EXEC -d auto_prepend_file=$BOOTSTRAP \
            %{_bindir}/phpunit6 --verbose || RETURN_CODE=1
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
%dir %{phpdir}/phpDocumentor
%dir %{phpdir}/phpDocumentor/Reflection%{major}
     %{phpdir}/phpDocumentor/Reflection%{major}/autoload-common.php
     %{phpdir}/phpDocumentor/Reflection%{major}/Element.php
     %{phpdir}/phpDocumentor/Reflection%{major}/File.php
     %{phpdir}/phpDocumentor/Reflection%{major}/Fqsen.php
     %{phpdir}/phpDocumentor/Reflection%{major}/Location.php
     %{phpdir}/phpDocumentor/Reflection%{major}/Project.php
     %{phpdir}/phpDocumentor/Reflection%{major}/ProjectFactory.php


%changelog
* Mon Apr 27 2020 Remi Collet <remi@remirepo.net> - 2.1.0-1
- update to 2.1.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 13 2019 Remi Collet <remi@remirepo.net> - 2.0.0-2
- fix autoloader path in description

* Fri Sep 13 2019 Remi Collet <remi@remirepo.net> - 2.0.0-1
- update to 2.0.0
- rename to php-phpdocumentor-reflection-common2
- move to /usr/share/php/phpDocumentor/Reflection2
- raise dependency on PHP 7.1
- use phpunit6

* Sat Nov 18 2017 Remi Collet <remi@remirepo.net> - 1.0.1-1
- Update to 1.0.1
- ensure current version is used during the test
- use git snapshot as sources for tests

* Sat Mar 11 2017 Shawn Iwinski <shawn@iwin.ski> - 1.0-1
- Initial package

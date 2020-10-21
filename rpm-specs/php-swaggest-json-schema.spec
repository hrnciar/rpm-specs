# remirepo/fedora spec file for php-swaggest-json-schema
#
# Copyright (c) 2019-2020 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%bcond_without       tests

# Github
%global gh_commit    a4adcdbb38f38a19d3f1801150822172cf1c4853
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     swaggest
%global gh_project   php-json-schema
# Packagist
%global pk_vendor    %{gh_owner}
%global pk_project   json-schema
# Namespace
%global ns_vendor    Swaggest
%global ns_project   JsonSchema
%global major        %nil

Name:           php-%{pk_vendor}-%{pk_project}%{major}
Version:        0.12.31
Release:        1%{?gh_date?%{gh_date}git%{gh_short}}%{?dist}
Summary:        High definition PHP structures with JSON-schema based validation

License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{?gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
%if %{with tests}
BuildRequires:  php(language) >= 5.4
BuildRequires:  php-json
BuildRequires:  php-mbstring
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
BuildRequires: (php-composer(phplang/scope-exit)    >= 1.0   with php-composer(phplang/scope-exit)    < 2)
BuildRequires: (php-composer(swaggest/json-diff)    >= 3.5.1 with php-composer(swaggest/json-diff)    < 4)
%else
BuildRequires:  php-phplang-scope-exit              >= 1.0
BuildRequires:  php-swaggest-json-diff              >= 3.5.1
%endif
# For tests, from composer.json "require-dev": {
#    "phpunit/phpunit": "^4.8.23",
#    "phpunit/php-code-coverage": "2.2.4",
#    "codeclimate/php-test-reporter": "^0.4.0"
BuildRequires:  php-composer(phpunit/phpunit) >= 4.8.23
%global phpunit %{_bindir}/phpunit
BuildRequires:  php-date
BuildRequires:  php-filter
BuildRequires:  php-pcre
BuildRequires:  php-spl
# For autoloader
BuildRequires:  php-fedora-autoloader-devel
%endif

# From composer.json, "require": {
#    "php": ">=5.4",
#    "ext-json": "*",
#    "ext-mbstring": "*",
#    "phplang/scope-exit": "^1.0",
#    "swaggest/json-diff": "^3.5.1"
Requires:       php(language) >= 5.4
Requires:       php-json
Requires:       php-mbstring
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
Requires:      (php-composer(phplang/scope-exit)    >= 1.0   with php-composer(phplang/scope-exit)    < 2)
Requires:      (php-composer(swaggest/json-diff)    >= 3.5.1 with php-composer(swaggest/json-diff)    < 4)
%else
Requires:       php-phplang-scope-exit              >= 1.0
Requires:       php-swaggest-json-diff              >= 3.5.1
%endif
# From phpcompatinfo report for 0.12.17
Requires:       php-date
Requires:       php-filter
Requires:       php-pcre
Requires:       php-spl
# For generated autoloader
Requires:       php-composer(fedora/autoloader)

# Composer
Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}


%description
High definition PHP structures with JSON-schema based validation.

Autoloader: %{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}

: Fix layout
mkdir src/spec
cp -p spec/*.json src/spec/
sed -e 's:/../spec/:/spec/:' -i src/RemoteRef/Preloaded.php


%build
: Create autoloader
%{_bindir}/phpab -t fedora -o src/autoload.php src
cat << 'EOF' | tee -a src/autoload.php

\Fedora\Autoloader\Dependencies::required([
    '%{_datadir}/php/PhpLang/scope-exit-autoload.php',
    '%{_datadir}/php/Swaggest/JsonDiff/autoload.php',
]);
EOF


%install
: Library
mkdir -p         %{buildroot}%{_datadir}/php/%{ns_vendor}
cp -pr src       %{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}


%check
%if %{with tests}
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require '%{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('%{ns_vendor}\\%{ns_project}\\Tests\\', dirname(__DIR__).'/tests/src');
EOF

ret=0
for cmd in php php71 php72 php73 php74; do
   if which $cmd; then
      $cmd %{phpunit} --no-coverage --verbose || ret=1
   fi
done
exit $ret
%else
: Test suite disabled
%endif


%files
%license LICENSE
%doc composer.json
%doc README.md
%doc CHANGELOG.md
%{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}


%changelog
* Mon Sep 21 2020 Remi Collet <remi@remirepo.net> - 0.12.31-1
- update to 0.12.31

* Thu Sep 10 2020 Remi Collet <remi@remirepo.net> - 0.12.30-1
- update to 0.12.30

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.29-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Mar 19 2020 Remi Collet <remi@remirepo.net> - 0.12.29-1
- update to 0.12.29

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 27 2020 Remi Collet <remi@remirepo.net> - 0.12.28-1
- update to 0.12.28

* Tue Jan  7 2020 Remi Collet <remi@remirepo.net> - 0.12.25-1
- update to 0.12.25

* Wed Dec  4 2019 Remi Collet <remi@remirepo.net> - 0.12.24-1
- update to 0.12.24

* Tue Dec  3 2019 Remi Collet <remi@remirepo.net> - 0.12.23-1
- update to 0.12.23

* Tue Oct 22 2019 Remi Collet <remi@remirepo.net> - 0.12.22-1
- update to 0.12.22

* Wed Oct  2 2019 Remi Collet <remi@remirepo.net> - 0.12.21-1
- update to 0.12.21

* Mon Sep 23 2019 Remi Collet <remi@remirepo.net> - 0.12.20-1
- update to 0.12.20

* Tue Sep 17 2019 Remi Collet <remi@remirepo.net> - 0.12.19-1
- update to 0.12.19

* Thu Sep 12 2019 Remi Collet <remi@remirepo.net> - 0.12.17-1
- initial package

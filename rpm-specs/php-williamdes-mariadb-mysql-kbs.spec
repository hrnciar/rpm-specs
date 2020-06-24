# remirepo/fedora spec file for php-williamdes-mariadb-mysql-kbs
#
# Copyright (c) 2019-2020 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%global with_tests   0%{!?_without_tests:1}
# Github
%global gh_commit    152fa144bd5f9fbdd3b5e764a506e239a730df83
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     williamdes
%global gh_project   mariadb-mysql-kbs
# Packagist
%global pk_vendor    %{gh_owner}
%global pk_project   %{gh_project}
# Namespace
%global ns_vendor    Williamdes
%global ns_project   MariaDBMySQLKBS
%global major        %nil

Name:           php-%{pk_vendor}-%{pk_project}%{major}
Version:        1.2.10
Release:        1%{?gh_date?%{gh_date}git%{gh_short}}%{?dist}
Summary:        An index of the MariaDB and MySQL Knowledge bases

License:        MPLv2.0
URL:            https://github.com/%{gh_owner}/%{gh_project}
# pull from github to retrieve full data
Source0:        %{name}-%{version}-%{?gh_short}.tgz
Source1:        makesrc.sh

Patch0:         %{name}-layout.patch

BuildArch:      noarch
%if %{with_tests}
BuildRequires:  php(language) >= 7.1
BuildRequires:  php-json
BuildRequires:  php-pcre
# For tests, from composer.json "require-dev": {
#        "phpunit/phpunit": "^7 || ^8",
#        "phpstan/phpstan": "^0.12",
#        "slevomat/coding-standard": "^6.0",
#        "squizlabs/php_codesniffer": "^3.3",
#        "swaggest/json-schema": "^0.12.9"
BuildRequires:  phpunit8
%global phpunit %{_bindir}/phpunit8
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
BuildRequires: (php-composer(swaggest/json-schema)    >  0.12.9 with php-composer(swaggest/json-schema)    < 1)
%else
BuildRequires:  php-composer(swaggest/json-schema)    <  1
BuildRequires:  php-composer(swaggest/json-schema)    >= 0.12.9
%endif
# For autoloader
BuildRequires:  php-composer(fedora/autoloader)
%endif

# From composer.json, "require": {
#        "php": "^7.1"
Requires:       php(language) >= 7.1
# From phpcompatinfo report for 1.2.7
Requires:       php-json
Requires:       php-pcre
# For generated autoloader
Requires:       php-composer(fedora/autoloader)

# Composer
Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}


%description
An index of the MariaDB and MySQL Knowledge bases.


Autoloader: %{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}
%patch0 -p1 -b .rpm
find src -name \*.rpm -delete

: Create autoloader
cat <<'AUTOLOAD' | tee src/autoload.php
<?php
/* Autoloader for %{name} and its dependencies */
require_once '%{_datadir}/php/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('%{ns_vendor}\\%{ns_project}\\', __DIR__);
AUTOLOAD


%build
: Generate merged data
%{_bindir}/php -d auto_prepend_file=src/autoload.php src/merge.php


%install
: Library
mkdir -p       %{buildroot}%{_datadir}/php/%{ns_vendor}
cp -pr src     %{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}

: Data
mkdir -p       %{buildroot}%{_datadir}/%{name}
# only dist is used at runtime
cp -pr dist    %{buildroot}%{_datadir}/%{name}/dist
cp -pr data    %{buildroot}%{_datadir}/%{name}/data
cp -pr schemas %{buildroot}%{_datadir}/%{name}/schemas


%check
%if %{with_tests}
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require '%{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('%{ns_vendor}\\%{ns_project}\\Test\\', dirname(__DIR__).'/test');
require '%{_datadir}/php/Swaggest/JsonSchema/autoload.php';
EOF

export RPM_BUILDROOT=%{buildroot}

ret=0
for cmd in php php72 php73 php74; do
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
%doc *.md
%dir     %{_datadir}/php/%{ns_vendor}/
         %{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}
%exclude %{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}/merge.php
%exclude %{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}/*.js
%dir     %{_datadir}/%{name}/
         %{_datadir}/%{name}/dist
%doc     %{_datadir}/%{name}/data
%doc     %{_datadir}/%{name}/schemas


%changelog
* Thu Feb 27 2020 Remi Collet <remi@remirepo.net> - 1.2.10-1
- update to 1.2.10
- sources from git snapshot

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 27 2020 Remi Collet <remi@remirepo.net> - 1.2.9-1
- update to 1.2.9
- switch to phpunit8

* Tue Nov 12 2019 Remi Collet <remi@remirepo.net> - 1.2.8-1
- update to 1.2.8

* Thu Sep 12 2019 Remi Collet <remi@remirepo.net> - 1.2.7-1
- initial package

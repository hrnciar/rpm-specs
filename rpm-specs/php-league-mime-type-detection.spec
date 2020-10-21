# remirepo/fedora spec file for php-league-mime-type-detection
#
# Copyright (c) 2020 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
# Github
%global gh_commit    353f66d7555d8a90781f6f5e7091932f9a4250aa
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     thephpleague
%global gh_project   mime-type-detection
# Packagist
%global pk_vendor    league
%global pk_name      mime-type-detection
# Namespace
%global ns_vendor    League
%global ns_project   MimeTypeDetection

Name:           php-%{pk_vendor}-%{pk_name}
Version:        1.5.1
Release:        1%{?dist}
Summary:        Mime-type detection for Flysystem

License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
# Create git snapshot as tests are excluded from official tarball
Source1:        makesrc.sh

Patch1:         https://patch-diff.githubusercontent.com/raw/thephpleague/mime-type-detection/pull/3.patch

BuildArch:      noarch

BuildRequires:  php(language) >= 7.2
BuildRequires:  php-fileinfo
BuildRequires:  php-json
# From composer.json, "require-dev": {
#        "phpunit/phpunit": "^8.5.8",
#        "phpstan/phpstan": "^0.12.36"
%if 0%{?fedora} >= 31 || 0%{?rhel} >= 9
BuildRequires:  phpunit9 >= 9.3
%global phpunit %{_bindir}/phpunit9
%else
BuildRequires:  phpunit8 >= 8.5.8
%global phpunit %{_bindir}/phpunit8
%endif
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer.json, "require": {
#        "php": "^7.2 || ^8.0",
#        "ext-fileinfo": "*"
Requires:       php(language) >= 7.2
Requires:       php-fileinfo
# From phpcompatifo report for 1.4.0
Requires:       php-json
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_vendor}/%{pk_name}) = %{version}


%description
This package supplies a generic mime-type detection interface with a finfo
based implementation.

Autoloader: %{_datadir}/php/%{ns_vendor}/%{ns_project}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}
%patch1 -p1


%build
: Create classmap autoloader
phpab \
  --template fedora \
  --output src/autoload.php \
  src


%install
# Restore PSR-0 tree
mkdir -p   %{buildroot}%{_datadir}/php/%{ns_vendor}
cp -pr src %{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}


%check
: Generate a simple autoloader
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
// Installed library
require '%{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}/autoload.php';
EOF

: Run upstream test suite
# the_generated_map_should_be_up_to_date is online
ret=0
for cmdarg in "php %{phpunit}" "php72 %{_bindir}/phpunit8" php73 php74 php80; do
  if which $cmdarg; then
    set $cmdarg
    $1 ${2:-%{_bindir}/phpunit9} \
      --filter '^((?!(the_generated_map_should_be_up_to_date)).)*$' \
      --no-coverage \
      --verbose || ret=1
  fi
done
exit $ret


%files
%license LICENSE
%doc *.md
%doc composer.json
%{_datadir}/php/%{ns_vendor}
%exclude %{_datadir}/php/%{ns_vendor}/%{ns_project}/*Test.php


%changelog
* Mon Oct 19 2020 Remi Collet <remi@remirepo.net> - 1.5.1-1
- update to 1.5.1

* Tue Sep 22 2020 Remi Collet <remi@remirepo.net> - 1.5.0-1
- update to 1.5.0
- add patch for test suite from upstream and from
  https://github.com/thephpleague/mime-type-detection/pull/3
- open https://github.com/thephpleague/mime-type-detection/pull/4 phpunit 9
- switch to phpunit9

* Mon Aug 24 2020 Remi Collet <remi@remirepo.net> - 1.4.0-1
- initial package

# remirepo/fedora spec file for php-brick-varexporter
#
# Copyright (c) 2020 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
# Github
%global gh_commit    411110b797c6b1ecf947a0eec17ffaa59284f5a0
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     brick
%global gh_project   varexporter
# Packagist
%global pk_vendor    %{gh_owner}
%global pk_name      %{gh_project}
# Namespace
%global ns_vendor    Brick
%global ns_project   VarExporter

Name:           php-%{pk_vendor}-%{pk_name}
Version:        0.3.2
Release:        1%{?dist}
Summary:        A powerful alternative to var_export

License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
# Create git snapshot as tests are excluded from official tarball
Source1:        makesrc.sh

BuildArch:      noarch

BuildRequires:  php(language) >= 7.2
BuildRequires: (php-composer(nikic/php-parser) >= 4.0   with php-composer(nikic/php-parser) < 5)
BuildRequires:  php-reflection
BuildRequires:  php-date
BuildRequires:  php-pcre
BuildRequires:  php-spl
# From composer.json, "require-dev": {
#    "phpunit/phpunit": "^7.0",
#    "php-coveralls/php-coveralls": "^2.0"
BuildRequires:  phpunit7
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer.json, "require": {
#    "php": ">=7.2",
#    "nikic/php-parser": "^4.0"
Requires:       php(language) >= 7.2
Requires:      (php-composer(nikic/php-parser) >= 4.0   with php-composer(nikic/php-parser) < 5)
# From phpcompatifo report for 0.3.2
Requires:       php-reflection
Requires:       php-pcre
Requires:       php-spl
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_vendor}/%{pk_name}) = %{version}


%description
This library aims to provide a prettier, safer, and powerful alternative
to var_export(). The output is valid and standalone PHP code, that does
not depend on the brick/varexporter library.

Autoloader: %{_datadir}/php/%{ns_vendor}/%{ns_project}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}


%build
: Create classmap autoloader
phpab \
  --template fedora \
  --output src/autoload.php \
  src

cat << 'EOF' | tee -a src/autoload.php

\Fedora\Autoloader\Dependencies::required([
    '/usr/share/php/PhpParser4/autoload.php',
]);

EOF

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
\Fedora\Autoloader\Autoload::addPsr4('Brick\\VarExporter\\Tests\\', dirname(__DIR__) . '/tests');
EOF

: Run upstream test suite
ret=0
for cmd in php php72 php73 php74 php80; do
  if which $cmd; then
   $cmd %{_bindir}/phpunit7 \
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


%changelog
* Tue Aug 25 2020 Remi Collet <remi@remirepo.net> - 0.3.2-1
- initial package

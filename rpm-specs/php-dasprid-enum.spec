# remirepo/fedora spec file for php-dasprid-enum
#
# Copyright (c) 2019 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%bcond_without       tests

%global gh_commit    5abf82f213618696dda8e3bf6f64dd042d8542b2
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     DASPRiD
%global gh_project   Enum

%global pk_vendor    dasprid
%global pk_project   enum

%global ns_vendor    %{gh_owner}
%global ns_project   %{gh_project}
%global php_home     %{_datadir}/php
%global major        %nil

Name:           php-%{pk_vendor}-%{pk_project}%{major}
Version:        1.0.3
Release:        1%{?dist}
Summary:        PHP enum implementation

License:        BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{name}-%{version}-%{gh_short}.tar.gz

BuildArch:      noarch
%if %{with tests}
# For tests
BuildRequires:  php(language)
BuildRequires:  php-reflection
BuildRequires:  php-spl
# From composer.json, "require-dev": {
#        "phpunit/phpunit": "^7 | ^8 | ^9",
#        "squizlabs/php_codesniffer": "^3.4"
%global phpunit %{_bindir}/phpunit9
BuildRequires:  %{phpunit}
# Required by autoloader
BuildRequires:  php-composer(fedora/autoloader)
%endif

# From composer.json, "require": {
# nothing
Requires:       php(language)
# From phpcompatinfo report for version 1.0.0
Requires:       php-reflection
Requires:       php-spl
# Required by autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}


%description
It is a well known fact that PHP is missing a basic enum type, ignoring the
rather incomplete SplEnum implementation which is only available as a PECL
extension. There are also quite a few other userland enum implementations
around, but all of them have one or another compromise. This library tries to
close that gap as far as PHP allows it to.

Autoloader: %{php_home}/%{ns_vendor}/%{ns_project}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}

cat << 'EOF' | tee src/autoload.php
<?php
/* Autoloader for %{name} and its dependencies */
require_once '/usr/share/php/Fedora/Autoloader/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('%{ns_vendor}\\%{ns_project}\\', __DIR__);
EOF


%build
# Empty build section, most likely nothing required.


%install
: Library
mkdir -p   %{buildroot}%{php_home}/%{ns_vendor}
cp -pr src %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}


%check
%if %{with tests}
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require '%{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('%{ns_vendor}\\EnumTest\\', dirname( __DIR__).'/test');
EOF

ret=0
for cmd in "php %{phpunit}" "php72 %{_bindir}/phpunit8" php73 php74 php80; do
  if which $cmd; then
    set $cmd
    $1 ${2:-%{_bindir}/phpunit9} --verbose || ret=1
  fi
done
exit $ret
%else
: Test suite disabled
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc composer.json
%doc README.md
%dir %{php_home}/%{ns_vendor}
     %{php_home}/%{ns_vendor}/%{ns_project}


%changelog
* Mon Oct  5 2020 Remi Collet <remi@remirepo.net> - 1.0.3-1
- update to 1.0.3

* Tue Aug 11 2020 Remi Collet <remi@remirepo.net> - 1.0.2-1
- update to 1.0.2
- switch to phpunit9
- drop patch merged upstream

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 19 2017 Remi Collet <remi@remirepo.net> - 1.0.0-1
- initial package, version 1.0.0
- add license file from
  https://github.com/DASPRiD/Enum/pull/2

# remirepo/fedora spec file for php-scssphp-scssphp
#
# Copyright (c) 2019-2020 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

# For compatibility with SCL
#undefine __brp_mangle_shebangs

%global with_tests   0%{!?_without_tests:1}
# Github
%global gh_commit    20d661952d19d4d75508180c453a594423b4f10b
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     scssphp
%global gh_project   scssphp
# Packagist
%global pk_vendor    %{gh_owner}
%global pk_project   %{gh_project}
# Namespace
%global ns_vendor    ScssPhp
%global ns_project   ScssPhp
%global major        %nil

Name:           php-%{pk_vendor}-%{pk_project}%{major}
Version:        1.0.8
Release:        1%{?gh_date?%{gh_date}git%{gh_short}}%{?dist}
Summary:        Compiler for SCSS

License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{?gh_short}.tgz
# Create a git snapshot with test suite
Source1:        makesrc.sh

# Use our autoloader
Patch0:         %{name}-rpm.patch

BuildArch:      noarch
BuildRequires:  php(language) >= 5.6.0
BuildRequires:  php-cli
%if %{with_tests}
BuildRequires:  php-ctype
BuildRequires:  php-date
BuildRequires:  php-json
BuildRequires:  php-mbstring
BuildRequires:  php-pcre
BuildRequires:  php-spl
# For tests, from composer.json "require-dev": {
#        "squizlabs/php_codesniffer": "~2.5",
#        "phpunit/phpunit": "^5.7 || ^6.5 || ^7.5 || ^8.3",
#        "twbs/bootstrap": "~4.3",
#        "zurb/foundation": "~6.5"
BuildRequires:  phpunit8 >= 8.3
%global phpunit %{_bindir}/phpunit8
%endif
# For autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer.json, "require": {
#        "php": ">=5.6.0",
#        "ext-json": "*",
#        "ext-ctype": "*"
Requires:       php(language) >= 5.6.0
Requires:       php-cli
Requires:       php-ctype
Requires:       php-json
# From phpcompatinfo report for 1.0.4
Requires:       php-date
Requires:       php-mbstring
Requires:       php-pcre
Requires:       php-spl
# For generated autoloader
Requires:       php-composer(fedora/autoloader)

# Composer
Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}


%description
%{name} is a compiler for SCSS written in PHP.

Autoloader: %{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}
%patch0 -p1 -b .rpm

mv LICENSE.md LICENSE


%build
: Create autoloader
%{_bindir}/phpab -t fedora -o src/autoload.php src


%install
: Library
mkdir -p      %{buildroot}%{_datadir}/php/%{ns_vendor}
cp -pr src    %{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}

: Command
mkdir -p %{buildroot}%{_bindir}
install -pm 0755 bin/pscss %{buildroot}%{_bindir}/%{name}


%check
php -r '
  require "%{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}/autoload.php";
  printf("Project version: %s\n", ScssPhp\ScssPhp\Version::VERSION);
  exit(ScssPhp\ScssPhp\Version::VERSION === "v%{version}" ? 0 : 1);
'

%if %{with_tests}
mkdir -p vendor/
cat << 'EOF' | tee vendor/autoload.php
<?php
require '%{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('%{ns_vendor}\\%{ns_project}\\Tests\\', dirname(__DIR__).'/tests');
EOF

: Ignore tests for non-packaged frameworks
rm tests/FrameworkTest.php

ret=0
for cmdarg in "php %{phpunit}" php72 php73 php74; do
   if which $cmdarg; then
      set $cmdarg
      if [ $(php -r 'echo PHP_INT_SIZE;') -lt 8 ] ; then
        # see https://github.com/scssphp/scssphp/issues/51
        $1 ${2:-%{_bindir}/phpunit8} --filter '^((?!(testTests|testEncode)).)*$' --no-coverage --verbose || ret=1
      else
        $1 ${2:-%{_bindir}/phpunit8} --no-coverage --verbose || ret=1
      fi
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
%{_bindir}/%{name}
%dir %{_datadir}/php/%{ns_vendor}
     %{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}


%changelog
* Fri Feb 21 2020 Remi Collet <remi@remirepo.net> - 1.0.8-1
- update to 1.0.8

* Sat Feb  1 2020 Remi Collet <remi@remirepo.net> - 1.0.7-1
- update to 1.0.7

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 12 2019 Remi Collet <remi@remirepo.net> - 1.0.6-1
- update to 1.0.6

* Fri Oct  4 2019 Remi Collet <remi@remirepo.net> - 1.0.5-1
- update to 1.0.5

* Thu Sep 12 2019 Remi Collet <remi@remirepo.net> - 1.0.4-1
- initial package

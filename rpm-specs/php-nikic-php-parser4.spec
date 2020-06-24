# remirepo/fedora spec file for php-nikic-php-parser4
#
# Copyright (c) 2016-2020 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

# For compatibility with SCL
%undefine __brp_mangle_shebangs

%global gh_commit    53c2753d756f5adb586dca79c2ec0e2654dd9463
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     nikic
%global gh_project   PHP-Parser
%global pk_project   php-parser
%global php_home     %{_datadir}/php
%global ns_project   PhpParser
%global with_tests   0%{!?_without_tests:1}
%global major        4

Name:           php-%{gh_owner}-%{pk_project}%{major}
Version:        4.5.0
Release:        1%{?dist}
Summary:        A PHP parser written in PHP - version %{major}

License:        BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

# Autoloader
Patch0:         %{name}-rpm.patch

BuildArch:      noarch
%if %{with_tests}
# For tests
BuildRequires:  php(language) >= 7.0
BuildRequires:  php-tokenizer
BuildRequires:  php-reflection
BuildRequires:  php-ctype
BuildRequires:  php-json
BuildRequires:  php-pcre
BuildRequires:  php-spl
# From composer.json, "require-dev": {
#        "phpunit/phpunit": "^6.5 || ^7.0 || ^8.0",
#        "ircmaxell/php-yacc": "0.0.5"
%global phpunit %{_bindir}/phpunit8
BuildRequires:  phpunit8
# Autoloader
BuildRequires:  php-composer(fedora/autoloader)
%endif

# From composer.json, "require": {
#        "php": ">=7.0",
#        "ext-tokenizer": "*"
Requires:       php(language) >= 7.0
Requires:       php-tokenizer
# From phpcompatinfo report for version 4.0.0
Requires:       php-reflection
Requires:       php-ctype
Requires:       php-json
Requires:       php-pcre
Requires:       php-spl
Requires:       php-cli
# Autoloader
BuildRequires:  php-composer(fedora/autoloader)

Provides:       php-composer(%{gh_owner}/%{pk_project}) = %{version}


%description
This is a PHP 5.2 to PHP 7.4 parser written in PHP.
Its purpose is to simplify static code analysis and manipulation.

This package provides the library version %{major} and the php-parse%{major} command.

Documentation: https://github.com/nikic/PHP-Parser/tree/master/doc

Autoloader: %{php_home}/%{ns_project}%{major}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}

%patch0 -p1 -b .rpm


%build
: Generate an simple PSR-4 autoloader
cat << 'AUTOLOAD' | tee lib/%{ns_project}/autoload.php
<?php
/* Autoloader for %{name} and its dependencies */
require_once '%{_datadir}/php/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('%{ns_project}\\', __DIR__);
AUTOLOAD


%install
: Library
mkdir -p                 %{buildroot}%{php_home}
cp -pr lib/%{ns_project} %{buildroot}%{php_home}/%{ns_project}%{major}

: Command
install -Dpm 0755 bin/php-parse %{buildroot}%{_bindir}/php-parse%{major}


%check
%if %{with_tests}
: Test the command
sed -e 's:%{php_home}:%{buildroot}%{php_home}:' \
    bin/php-parse > bin/php-parse-test
php bin/php-parse-test --help

: Test suite autoloader
mkdir vendor
cat << 'AUTOLOAD' | tee vendor/autoload.php
<?php
require_once '%{buildroot}/%{php_home}/%{ns_project}%{major}/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('%{ns_project}\\', dirname(__DIR__).'/test/PhpParser/');
AUTOLOAD

: Upstream test suite
# ignore test failing on 32-bit (in koji)
ret=0
for cmdarg in "php %{phpunit}" "php71 %{_bindir}/phpunit7" php72 php73 php74 php80; do
  if which $cmdarg; then
    set $cmdarg
    $1 ${2:-%{_bindir}/phpunit8} \
      --filter '^((?!(testParse|testLexNewFeatures)).)*$' \
      --verbose || ret=1
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
%{_bindir}/php-parse%{major}
%{php_home}/%{ns_project}%{major}


%changelog
* Wed Jun  3 2020 Remi Collet <remi@remirepo.net> - 4.5.0-1
- update to 4.5.0

* Mon Apr 13 2020 Remi Collet <remi@remirepo.net> - 4.4.0-1
- update to 4.4.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 12 2019 Remi Collet <remi@remirepo.net> - 4.3.0-1
- update to 4.3.0

* Mon Oct 28 2019 Remi Collet <remi@remirepo.net> - 4.2.5-1
- update to 4.2.5
- sources from git snapshot

* Mon Sep  2 2019 Remi Collet <remi@remirepo.net> - 4.2.4-1
- update to 4.2.4

* Mon Aug 19 2019 Remi Collet <remi@remirepo.net> - 4.2.3-1
- update to 4.2.3
- use phpunit8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 27 2019 Remi Collet <remi@remirepo.net> - 4.2.2-1
- update to 4.2.2

* Mon Feb 18 2019 Remi Collet <remi@remirepo.net> - 4.2.1-1
- update to 4.2.1

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jan 13 2019 Remi Collet <remi@remirepo.net> - 4.2.0-1
- update to 4.2.0

* Thu Dec 27 2018 Remi Collet <remi@remirepo.net> - 4.1.1-1
- update to 4.1.1

* Wed Oct 10 2018 Remi Collet <remi@remirepo.net> - 4.1.0-1
- update to 4.1.0
- https://github.com/nikic/PHP-Parser/issues/539 - PHP 7.3

* Tue Sep 18 2018 Remi Collet <remi@remirepo.net> - 4.0.4-1
- update to 4.0.4

* Mon Jul 16 2018 Remi Collet <remi@remirepo.net> - 4.0.3-1
- update to 4.0.3

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun  4 2018 Remi Collet <remi@remirepo.net> - 4.0.2-1
- update to 4.0.2

* Mon Mar 26 2018 Remi Collet <remi@remirepo.net> - 4.0.1-1
- update to 4.0.1

* Thu Mar 22 2018 Remi Collet <remi@remirepo.net> - 4.0.0-1
- Update to 4.0.0
- rename to php-nikic-php-parser4 and move to /usr/share/php/PhpParser4
- raise dependency on PHP 7
- use phpunit6 or phpunit7 (F28+)

* Thu Mar  1 2018 Remi Collet <remi@remirepo.net> - 3.1.5-1
- Update to 3.1.5

* Fri Jan 26 2018 Remi Collet <remi@remirepo.net> - 3.1.4-1
- Update to 3.1.4

* Wed Dec 27 2017 Remi Collet <remi@remirepo.net> - 3.1.3-1
- Update to 3.1.3

* Mon Nov  6 2017 Remi Collet <remi@remirepo.net> - 3.1.2-1
- Update to 3.1.2

* Mon Sep  4 2017 Remi Collet <remi@remirepo.net> - 3.1.1-1
- Update to 3.1.1

* Sat Aug  5 2017 Remi Collet <remi@remirepo.net> - 3.1.0-1
- Update to 3.1.0

* Thu Jun 29 2017 Remi Collet <remi@remirepo.net> - 3.0.6-1
- Update to 3.0.6

* Mon Mar  6 2017 Remi Collet <remi@remirepo.net> - 3.0.5-1
- Update to 3.0.5
- always provide the command, with version suffix

* Sat Feb 11 2017 Remi Collet <remi@fedoraproject.org> - 3.0.4-1
- update to 3.0.4

* Sat Feb  4 2017 Remi Collet <remi@fedoraproject.org> - 3.0.3-1
- update to 3.0.3

* Wed Dec 7  2016 Remi Collet <remi@fedoraproject.org> - 3.0.2-1
- new package for library version 3


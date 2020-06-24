# remirepo/fedora spec file for php-nikic-php-parser3
#
# Copyright (c) 2016-2020 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

# For compatibility with SCL
%undefine __brp_mangle_shebangs

%global gh_commit    bb87e28e7d7b8d9a7fda231d37457c9210faf6ce
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     nikic
%global gh_project   PHP-Parser
%global pk_project   php-parser
%global php_home     %{_datadir}/php
%global with_tests   0%{!?_without_tests:1}
%global major        3

%global eolv1   0
%global eolv2   0

Name:           php-%{gh_owner}-%{pk_project}%{major}
Version:        3.1.5
Release:        5%{?dist}
Summary:        A PHP parser written in PHP - version %{major}

License:        BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source:         https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{name}-%{version}-%{gh_short}.tar.gz

# Autoloader
Patch0:         %{name}-rpm.patch

BuildArch:      noarch
%if %{with_tests}
# For tests
BuildRequires:  php(language) >= 5.5
BuildRequires:  php-tokenizer
BuildRequires:  php-filter
BuildRequires:  php-json
BuildRequires:  php-pcre
BuildRequires:  php-spl
BuildRequires:  php-xmlreader
BuildRequires:  php-xmlwriter
# From composer.json, "require-dev": {
#        "phpunit/phpunit": "~4.0|~5.0"
BuildRequires:  php-composer(phpunit/phpunit) >= 4.0
%endif

# From composer.json, "require": {
#        "php": ">=5.5",
#        "ext-tokenizer": "*"
Requires:       php(language) >= 5.5
Requires:       php-tokenizer
# From phpcompatinfo report for version 3.0.2
Requires:       php-filter
Requires:       php-json
Requires:       php-pcre
Requires:       php-spl
Requires:       php-xmlreader
Requires:       php-xmlwriter
%if %{eolv1}
Obsoletes:      php-PHPParser < %{major}
%endif
%if %{eolv2}
Obsoletes:      php-%{gh_owner}-%{pk_project} < %{major}
%endif
Requires:       php-cli

Provides:       php-composer(%{gh_owner}/%{pk_project}) = %{version}


%description
This is a PHP 5.2 to PHP 7.1 parser written in PHP.
Its purpose is to simplify static code analysis and manipulation.

This package provides the library version %{major} and the php-parse%{major} command.

Documentation: https://github.com/nikic/PHP-Parser/tree/master/doc

Autoloader: %{php_home}/PhpParser%{major}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}

%patch0 -p1 -b .rpm


%build
# Empty build section, most likely nothing required.


%install
: Library
mkdir -p                 %{buildroot}%{php_home}
cp -pr lib/PhpParser     %{buildroot}%{php_home}/PhpParser%{major}
cp -p  lib/bootstrap.php %{buildroot}%{php_home}/PhpParser%{major}/autoload.php

: Command
install -Dpm 0755 bin/php-parse %{buildroot}%{_bindir}/php-parse%{major}


%check
%if %{with_tests}
: Test the command
sed -e 's:%{php_home}:%{buildroot}%{php_home}:' \
    bin/php-parse > bin/php-parse-test
php bin/php-parse-test --help

: Test suite autoloader
sed -e 's:@BUILDROOT@:%{buildroot}:' -i test/bootstrap.php

: Upstream test suite
ret=0
for cmd in php php72 php73 php74; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit \
      --filter '^((?!(testResolveLocations|testParse|testError)).)*$' \
      --verbose || ret=1
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
%doc *.md
%{_bindir}/php-parse%{major}
%{php_home}/PhpParser%{major}


%changelog
* Tue Feb  4 2020 Remi Collet <remi@fedoraproject.org> - 1.4.1-11
- skip failed tests with 7.4

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar  1 2018 Remi Collet <remi@remirepo.net> - 3.1.5-1
- Update to 3.1.5

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

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

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 29 2017 Remi Collet <remi@remirepo.net> - 3.0.6-1
- Update to 3.0.6

* Mon Mar  6 2017 Remi Collet <remi@remirepo.net> - 3.0.5-1
- Update to 3.0.5
- always provide the command, with version suffix

* Sat Feb 11 2017 Remi Collet <remi@fedoraproject.org> - 3.0.4-1
- update to 3.0.4

* Sat Feb 4  2017 Remi Collet <remi@fedoraproject.org> - 3.0.3-1
- update to 3.0.3

* Wed Dec 7  2016 Remi Collet <remi@fedoraproject.org> - 3.0.2-1
- new package for library version 3


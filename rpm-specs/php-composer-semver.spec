# remirepo/fedora spec file for php-composer-semver
#
# Copyright (c) 2015-2020 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global gh_commit    c6bea70230ef4dd483e6bbcab6005f682ed3a8de
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
#global gh_date      20150717
%global gh_owner     composer
%global gh_project   semver
%global php_home     %{_datadir}/php
%global with_tests   0%{!?_without_tests:1}

Name:           php-composer-semver
Version:        1.5.1
Release:        2%{?gh_date:.%{gh_date}git%{gh_short}}%{?dist}
Summary:        Semver library that offers utilities, version constraint parsing and validation

License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
# git snapshot to get upstream test suite
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh
Source2:        %{name}-autoload.php

BuildArch:      noarch
%if %{with_tests}
# For tests
BuildRequires:  php(language) >= 5.3.2
BuildRequires:  php-pcre
BuildRequires:  php-spl
# From composer.json,     "require-dev": {
#        "phpunit/phpunit": "^4.5 || ^5.0.5"
BuildRequires:  php-composer(phpunit/phpunit) >= 4.5
# Autoloader
BuildRequires:  php-composer(fedora/autoloader)
%endif

# From composer.json, "require": {
#        "php": "^5.3.2 || ^7.0",
Requires:       php(language) >= 5.3.2
# From phpcompatinfo report for version 1.5.0
Requires:       php-pcre
Requires:       php-spl
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{gh_owner}/%{gh_project}) = %{version}


%description
Semver library that offers utilities, version constraint parsing
and validation.

Originally written as part of composer/composer, now extracted and
made available as a stand-alone library.

Autoloader: %{_datadir}/php/Composer/Semver/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}

cp %{SOURCE2} src/autoload.php


%build
# Empty build section, most likely nothing required.


%install
: Library
mkdir -p   %{buildroot}%{php_home}/Composer/
cp -pr src %{buildroot}%{php_home}/Composer/Semver


%check
%if %{with_tests}
ret=0
for cmd in php php72 php73 php74; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit \
      --bootstrap %{buildroot}%{php_home}/Composer/Semver/autoload.php \
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
%dir %{php_home}/Composer
     %{php_home}/Composer/Semver


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 14 2020 Remi Collet <remi@remirepo.net> - 1.5.1-1
- update to 1.5.1

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Mar 20 2019 Remi Collet <remi@remirepo.net> - 1.5.0-1
- update to 1.5.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Oct 20 2016 Remi Collet <remi@fedoraproject.org> - 1.4.2-2
- switch from symfony/class-loader to fedora/autoloader

* Thu Sep  1 2016 Remi Collet <remi@fedoraproject.org> - 1.4.2-1
- update to 1.4.2

* Thu Jun  2 2016 Remi Collet <remi@fedoraproject.org> - 1.4.1-1
- update to 1.4.1

* Wed Mar 30 2016 Remi Collet <remi@fedoraproject.org> - 1.4.0-1
- update to 1.4.0

* Fri Feb 26 2016 Remi Collet <remi@fedoraproject.org> - 1.3.0-1
- update to 1.3.0
- run test suite with both PHP 5 and 7 when available

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Remi Collet <remi@fedoraproject.org> - 1.2.0-1
- update to 1.2.0

* Wed Nov  4 2015 Remi Collet <remi@fedoraproject.org> - 1.1.0-1
- update to 1.1.0

* Sun Oct  4 2015 Remi Collet <remi@fedoraproject.org> - 1.0.0-1
- initial package, version 1.0.0
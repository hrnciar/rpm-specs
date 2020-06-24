# remirepo/fedora spec file for php-hamcrest
#
# Copyright (c) 2015-2018 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global gh_commit    776503d3a8e85d4f9a1148614f95b7a608b046ad
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     hamcrest
%global gh_project   hamcrest-php
%global ns_project   Hamcrest
%global major        2
%global with_tests   0%{!?_without_tests:1}

Name:           php-hamcrest2
Version:        2.0.0
Release:        4%{?dist}
Summary:        PHP port of Hamcrest Matchers

License:        BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{name}-%{version}-%{gh_short}.tar.gz

# Use generated autoloader instead of composer one
Patch0:         bootstrap-autoload.patch

BuildArch:      noarch
BuildRequires:  php-fedora-autoloader-devel
%if %{with_tests}
# From composer.json, require-dev:
#               "satooshi/php-coveralls": "^1.0",
#               "phpunit/php-file-iterator": "1.3.3",
#               "phpunit/phpunit": "~4.0"
BuildRequires:  php-composer(phpunit/phpunit)
# composer.json, require:
#      "php": "^5.3|^7.0"
BuildRequires:  php(language) >= 5.3
# From phpcompatinfo report for 2.0.0
BuildRequires:  php-reflection
BuildRequires:  php-ctype
BuildRequires:  php-dom
BuildRequires:  php-pcre
BuildRequires:  php-spl
%endif

Requires:       php(language) >= 5.3
# From phpcompatinfo report for 2.0.0
Requires:       php-ctype
Requires:       php-dom
Requires:       php-pcre
Requires:       php-spl
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(hamcrest/hamcrest-php) = %{version}


%description
Hamcrest is a matching library originally written for Java,
but subsequently ported to many other languages.

%{name} is the official PHP port of Hamcrest and essentially follows
a literal translation of the original Java API for Hamcrest,
with a few Exceptions, mostly down to PHP language barriers.

Autoloader: %{_datadir}/php/%{ns_project}%{major}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}

%patch0 -p0 -b .rpm
find . -name \*.rpm -exec rm {} \;

# Move to Library tree
mv hamcrest/%{ns_project}.php hamcrest/%{ns_project}/%{ns_project}.php


%build
# Library autoloader
%{_bindir}/phpab \
    --template fedora \
    --output hamcrest/%{ns_project}/autoload.php \
    hamcrest/%{ns_project}

# Test suite autoloader
%{_bindir}/phpab \
    --output tests/autoload.php \
    --exclude '*Test.php' \
    tests generator


%install
mkdir -p %{buildroot}%{_datadir}/php
cp -pr hamcrest/%{ns_project} %{buildroot}%{_datadir}/php/%{ns_project}%{major}


%check
%if %{with_tests}
cd tests
ret=0
for cmd in php php56 php70 php71 php72 php73; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit --verbose || ret=1
  fi
done
exit $ret
%else
: Test suite disabled
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE.txt
%doc CHANGES.txt README.md TODO.txt
%doc composer.json
%{_datadir}/php/%{ns_project}%{major}


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 22 2018 Remi Collet <remi@remirepo.net> - 2.0.0-1
- Update to 2.0.0
- rename to php-hamcrest2

* Fri Feb 17 2017 Remi Collet <remi@fedoraproject.org> - 1.2.2-4
- add upstream patch for PHP 7, fix FTBFS
- switch to fedora/autoloader

* Thu Oct 15 2015 Remi Collet <remi@fedoraproject.org> - 1.2.2-1
- update to 1.2.2

* Mon Jan  5 2015 Remi Collet <remi@fedoraproject.org> - 1.2.0-1
- initial package

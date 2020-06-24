# remirepo/fedora spec file for php-elvanto-litemoji
#
# Copyright (c) 2018-2019 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global gh_commit    2cba2c87c505fe1d3a6e06ff4cc48d98af757521
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     elvanto
%global gh_project   litemoji
%global php_home     %{_datadir}/php
%global with_tests   0%{!?_without_tests:1}
%global ns_project   LitEmoji
Name:           php-%{gh_owner}-%{gh_project}
Version:        2.0.1
Release:        2%{?gh_date:.%{gh_date}git%{gh_short}}%{?dist}
Summary:        Conversion of unicode, HTML and shortcode emoji

License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{name}-%{version}-%{?gh_short}.tar.gz

BuildArch:      noarch
%if %{with_tests}
# For tests
BuildRequires:  php(language) >= 5.6
BuildRequires:  php-mbstring
BuildRequires:  php-pcre
# From composer.json, "require-dev": {
#        "phpunit/phpunit": "^5.0",
#        "milesj/emojibase": "4.0.0"
%global phpunit %{_bindir}/phpunit
BuildRequires: php-phpunit-PHPUnit >= 5.0
# Autoloader
BuildRequires:  php-composer(fedora/autoloader)
%endif

# From composer.json, "require": {
#        "php": ">=5.6",
Requires:       php(language) >= 5.6
# From phpcompatinfo report for version 2.0.0
Requires:       php-mbstring
Requires:       php-pcre
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{gh_owner}/%{gh_project}) = %{version}


%description
A PHP library simplifying the conversion of unicode, HTML and shortcode emoji.

Autoloader: %{_datadir}/php/%{ns_project}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}


%build
: Create autoloader
cat <<'AUTOLOAD' | tee src/autoload.php
<?php
/* Autoloader for %{name} and its dependencies */
require_once '%{_datadir}/php/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('%{ns_project}\\', __DIR__);
AUTOLOAD


%install
mkdir -p   %{buildroot}%{_datadir}/php/
cp -pr src %{buildroot}%{_datadir}/php/%{ns_project}


%check
%if %{with_tests}
ret=0
for cmd in php php56 php70 php71 php72 php73 php74; do
  if which $cmd; then
    $cmd %{phpunit} \
      --bootstrap %{buildroot}%{_datadir}/php/%{ns_project}/autoload.php \
      --no-coverage \
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
%{php_home}/%{ns_project}


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Remi Collet <remi@remirepo.net> - 2.0.1-1
- update to 2.0.1

* Fri Jul 19 2019 Remi Collet <remi@remirepo.net> - 2.0.0-1
- update to 2.0.0
- raise dependency on PHP 5.6

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Nov  6 2018 Remi Collet <remi@remirepo.net> - 1.4.4-1
- initial package, version 1.4.4

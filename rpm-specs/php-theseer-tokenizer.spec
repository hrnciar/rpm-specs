# remirepo/fedora spec file for php-theseer-tokenizer
#
# Copyright (c) 2017-2019 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global gh_commit    11336f6f84e16a720dae9d8e6ed5019efa85a0f9
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_vendor    theseer
%global gh_project   tokenizer
%global ns_vendor    TheSeer
%global ns_project   Tokenizer

Name:           php-%{gh_vendor}-%{gh_project}
Version:        1.1.3
Release:        3%{?dist}
Summary:        Library for converting tokenized PHP source code into XML

License:        BSD
URL:            https://github.com/%{gh_vendor}/%{gh_project}
Source0:        https://github.com/%{gh_vendor}/%{gh_project}/archive/%{gh_commit}/%{gh_project}-%{version}-%{?gh_short}.tar.gz

BuildArch:      noarch
BuildRequires:  php(language) >= 7.0
BuildRequires:  php-xmlwriter
BuildRequires:  php-dom
BuildRequires:  php-tokenizer
BuildRequires:  php-pcre
BuildRequires:  php-spl
# Autoloader
BuildRequires:  php-fedora-autoloader-devel >= 1.0.0
# Tests
%global phpunit %{_bindir}/phpunit7
BuildRequires:  %{phpunit}

# From composer.json, "require": {
#    "php": "^7.0",
#    "ext-xmlwriter": "*",
#    "ext-dom": "*",
#    "ext-tokenizer": "*"
Requires:       php(language) >= 7.0
Requires:       php-xmlwriter
Requires:       php-dom
Requires:       php-tokenizer
# From phpcompatinfo report for version 1.1.0
Requires:       php-pcre
Requires:       php-spl
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{gh_vendor}/%{gh_project}) = %{version}


%description
A small library for converting tokenized PHP source code into XML
and potentially other formats.

Autoloader: %{_datadir}/php/%{ns_vendor}/%{ns_project}/autoload.php

%prep
%setup -q -n %{gh_project}-%{gh_commit}


%build
: Generate a simple classmap autoloader
%{_bindir}/phpab --template fedora --output src/autoload.php src


%install
mkdir -p   %{buildroot}%{_datadir}/php/%{ns_vendor}
cp -pr src %{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}


%check
ret=0
for cmdarg in "php %{phpunit}" php71 php72 php73 php74; do
  if which $cmdarg; then
      set $cmdarg
      $1 -d auto_prepend_file=%{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}/autoload.php \
        ${2:-%{_bindir}/phpunit7} \
          --no-coverage --verbose || ret=1
  fi
done
exit $ret


%files
%license LICENSE
%doc README.md composer.json
%dir %{_datadir}/php/%{ns_vendor}
     %{_datadir}/php/%{ns_vendor}/%{ns_project}


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 14 2019 Remi Collet <remi@remirepo.net> - 1.1.3-1
- update to 1.1.3

* Thu Apr  4 2019 Remi Collet <remi@remirepo.net> - 1.1.2-1
- update to 1.1.2 (no change)
- switch back to phpunit 7

* Thu Apr  4 2019 Remi Collet <remi@remirepo.net> - 1.1.1-1
- update to 1.1.1
- use phpunit8

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Apr 21 2017 Remi Collet <remi@remirepo.net> - 1.1.0-1
- initial package, version 1.1.0

# remirepo/fedora spec file for php-phar-io-version
#
# Copyright (c) 2017-2018 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global bootstrap    0
%global gh_commit    45a2ec53a73c70ce41d55cedef9063630abaf1b6
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     phar-io
%global gh_project   version
%global pk_vendor    %{gh_owner}
%global pk_project   %{gh_project}
%global ns_vendor    PharIo
%global ns_project   Version
%global major        %nil
%global php_home     %{_datadir}/php
%if %{bootstrap}
%global with_tests   0%{?_with_tests:1}
%else
%global with_tests   0%{!?_without_tests:1}
%endif

Name:           php-%{pk_vendor}-%{pk_project}%{major}
Version:        2.0.1
Release:        4%{?dist}
Summary:        Library for handling version information and constraints

License:        BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{name}-%{version}-%{gh_short}.tar.gz

BuildArch:      noarch
# PHP 7 for phpunit6
BuildRequires:  php(language) >= 7
BuildRequires:  php-pcre
BuildRequires:  php-spl
BuildRequires:  php-fedora-autoloader-devel >= 1.0.0
%if %{with_tests}
BuildRequires:  phpunit6
%endif

# from composer.json
#    "php": "^5.6 || ^7.0"
Requires:       php(language) >= 5.6
# from phpcompatinfo report for version 1.0.1
Requires:       php-pcre
Requires:       php-spl
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}


%description
Library for handling version information and constraints.

Autoloader: %{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}


%build
# Generate the Autoloader
%{_bindir}/phpab --template fedora2 --output src/autoload.php src


%install
mkdir -p   %{buildroot}%{php_home}/%{ns_vendor}
cp -pr src %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}


%check
%if %{with_tests}
: Run upstream test suite
ret=0
for cmd in php php70 php71 php72 php73; do
  if which $cmd; then
    $cmd -d auto_prepend_file=%{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php \
    %{_bindir}/phpunit6  --bootstrap %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}/autoload.php --verbose || ret=1
  fi
done
exit $ret
%else
: bootstrap build with test suite disabled
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc README.md composer.json
%dir %{php_home}/%{ns_vendor}
     %{php_home}/%{ns_vendor}/%{ns_project}%{major}


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 16 2018 Remi Collet <remi@remirepo.net> - 2.0.1-1
- update to 2.0.1

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Apr  7 2017 Remi Collet <remi@remirepo.net> - 1.0.1-1
- initial package


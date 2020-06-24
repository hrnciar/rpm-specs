# spec file for php-phpspec-php-diff
#
# Copyright (c) 2015-2016 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global gh_commit    0464787bfa7cd13576c5a1e318709768798bec6a
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     phpspec
%global gh_project   php-diff

Name:           php-phpspec-php-diff
Version:        1.1.0
Release:        8%{?dist}
Summary:        A library for generating differences between two hashable objects

# LICENSE text is inclued in the README file
License:        BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{gh_project}-%{version}.tar.gz

# Fix example to use our generated autoloader
Patch0:         %{gh_project}-example.patch

BuildArch:      noarch
# For minimal test
BuildRequires:  php-cli
BuildRequires:  php-mbstring
# To generate an autoloader
BuildRequires:  %{_bindir}/phpab

# From phpcompatinfo report for version 1.1.0
Requires:       php(language)
Requires:       php-mbstring
Requires:       php-pcre

Provides:       php-composer(phpspec/php-diff) = %{version}


%description
A comprehensive library for generating differences between two hashable
objects (strings or arrays). Generated differences can be rendered in
all of the standard formats including:
 * Unified
 * Context
 * Inline HTML
 * Side by Side HTML

The logic behind the core of the diff engine (ie, the sequence matcher)
is primarily based on the Python difflib package. The reason for doing
so is primarily because of its high degree of accuracy.


%prep
%setup -q -n %{gh_project}-%{gh_commit}

%patch0 -p0


%build
: Generate a simple autoloader
%{_bindir}/phpab --output lib/autoload.php lib


%install
# No namespace, so use a package specific dir
mkdir -p     %{buildroot}%{_datadir}/php/phpspec/php-diff
cp -pr lib/* %{buildroot}%{_datadir}/php/phpspec/php-diff


%check
# Not really a test... but should work without error
cd example
%{_bindir}/php -d include_path=%{buildroot}%{_datadir}/php example.php >/dev/null


%files
%doc README example
%doc composer.json
%{_datadir}/php/phpspec


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Apr  7 2016 Remi Collet <remi@fedoraproject.org> - 1.1.0-1
- update to 1.1.0
- add dependency on mbstring

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Feb 17 2015 Remi Collet <remi@fedoraproject.org> - 1.0.2-1
- initial package
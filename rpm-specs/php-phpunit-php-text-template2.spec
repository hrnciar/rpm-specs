# remirepo/fedora spec file for php-phpunit-php-text-template2
#
# Copyright (c) 2010-2020 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global bootstrap    0
%global gh_commit    0c69cbf965d5317ba33f24a352539f354a25db09
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sebastianbergmann
%global gh_project   php-text-template
# Packagist
%global pk_vendor    phpunit
%global pk_project   %{gh_project}
# Namespace
%global ns_vendor    SebastianBergmann
%global ns_project   Template
%global php_home     %{_datadir}/php
%global ver_major    2

%if %{bootstrap}
%global with_tests   0%{?_with_tests:1}
%else
%global with_tests   0%{!?_without_tests:1}
%endif

Name:           php-%{pk_vendor}-%{pk_project}%{ver_major}
Version:        2.0.1
Release:        1%{?dist}
Summary:        Simple template engine

License:        BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
BuildRequires:  php(language) >= 7.3
BuildRequires:  php-cli
BuildRequires:  php-fedora-autoloader-devel
%if %{with_tests}
# From composer.json, require-dev
#        "phpunit/phpunit": "^9.0"
BuildRequires:  phpunit9
%endif

# From composer.json
#        "php": "^7.3"
Requires:       php(language) >= 7.3
# From phpcompatinfo report for version 2.0.0
Requires:       php-spl

Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}


%description
Simple template engine.


%prep
%setup -q -n %{gh_project}-%{gh_commit}


%build
# Generate the Autoloader
%{_bindir}/phpab --template fedora --output src/autoload.php src


%install
mkdir -p   %{buildroot}%{php_home}/%{ns_vendor}
cp -pr src %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{ver_major}


%if %{with_tests}
%check
: Generate tests autoloader
mkdir vendor
%{_bindir}/phpab --output vendor/autoload.php tests

: Run upstream test suite
ret=0
for cmd in php php73 php74 php80; do
  if which $cmd; then
    $cmd -d auto_prepend_file=%{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{ver_major}/autoload.php \
      %{_bindir}/phpunit9 --verbose || ret=1
  fi
done
exit $ret
%endif


%files
%license LICENSE
%doc *.md
%doc composer.json
%dir %{php_home}/%{ns_vendor}
     %{php_home}/%{ns_vendor}/%{ns_project}%{ver_major}


%changelog
* Tue Jun 16 2020 Remi Collet <remi@remirepo.net> - 2.0.1-1
- update to 2.0.1
- sources from git snapshot
- run upstream test suite

* Fri Feb  7 2020 Remi Collet <remi@remirepo.net> - 2.0.0-1
- update to 2.0.0
- raise dependency on PHP 7.3
- rename to php-phpunit-php-text-template2
- move to /usr/share/php/SebastianBergmann/Template2

* Sun Jun 21 2015 Remi Collet <remi@fedoraproject.org> - 1.2.1-1
- update to 1.2.1
- generate autoloader

* Sat Jun  7 2014 Remi Collet <remi@fedoraproject.org> - 1.2.0-4
- composer dependencies

* Wed Apr 30 2014 Remi Collet <remi@fedoraproject.org> - 1.2.0-3
- cleanup pear registry

* Tue Apr 29 2014 Remi Collet <remi@fedoraproject.org> - 1.2.0-2
- sources from github

* Thu Jan 30 2014 Remi Collet <remi@fedoraproject.org> - 1.2.0-1
- Update to 1.2.0

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Nov  1 2012 Remi Collet <remi@fedoraproject.org> - 1.1.4-1
- Version 1.1.4 (stable) - API 1.1.0 (stable)

* Sat Oct  6 2012 Remi Collet <remi@fedoraproject.org> - 1.1.3-1
- Version 1.1.3 (stable) - API 1.1.0 (stable)

* Mon Sep 24 2012 Remi Collet <remi@fedoraproject.org> - 1.1.2-1
- Version 1.1.2 (stable) - API 1.1.0 (stable)
- LICENSE is now provided in upstream tarball

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Nov 01 2011 Remi Collet <remi@fedoraproject.org> - 1.1.1-1
- Version 1.1.1 (stable) - API 1.1.0 (stable)
- raise dependencies, PEAR 1.9.4 and PHP 5.2.7

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Dec 05 2010 Remi Collet <Fedora@famillecollet.com> - 1.1.0-1
- Version 1.1.0 (stable) - API 1.1.0 (stable)
- remove README.mardown (which is only install doc)

* Fri Nov 05 2010 Remi Collet <Fedora@famillecollet.com> - 1.0.0-2
- fix URL

* Sun Sep 26 2010 Remi Collet <Fedora@famillecollet.com> - 1.0.0-1
- initial generated spec + clean

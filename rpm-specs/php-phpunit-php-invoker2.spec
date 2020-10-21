# remirepo/fedora spec file for php-phpunit-php-invoker2
#
# Copyright (c) 2011-2018 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global bootstrap    0
%global gh_commit    4a01883f660b10d4a19a14de5efd19b22eac2d93
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sebastianbergmann
%global gh_project   php-invoker
%global php_home     %{_datadir}/php
%global ns_vendor    SebastianBergmann
%global ns_project   Invoker
%if %{bootstrap}
%global with_tests   %{?_with_tests:1}%{!?_with_tests:0}
%else
%global with_tests   %{?_without_tests:0}%{!?_without_tests:1}
%endif

Name:           php-phpunit-php-invoker2
Version:        2.0.0
Release:        6%{?dist}
Summary:        Invoke callables with a timeout

License:        BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{name}-%{version}-%{gh_short}.tar.gz

BuildArch:      noarch
BuildRequires:  php(language) >= 7.1
BuildRequires:  php-fedora-autoloader-devel
%if %{with_tests}
# From composer.json, require-dev
#        "phpunit/phpunit": "^6.5"
BuildRequires:  phpunit6 >= 6.5
%endif

# From composer.json, require
#        "php": "^7.1",
#        "ext-pcntl": "*"
Requires:       php(language) >= 7.1
Requires:       php-pcntl
# From phpcompatinfo report for version 2.0.0
Requires:       php-spl
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(phpunit/php-invoker) = %{version}


%description
phpunit/php-invoker provides the means to invoke a callable with a timeout.

Autoloader: %{php_home}/%{ns_vendor}/%{ns_project}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}

%build
: Generate autoloader
%{_bindir}/phpab \
   --template fedora \
   --output  src/autoload.php \
   src


%install
mkdir -p   %{buildroot}%{php_home}/%{ns_vendor}
cp -pr src %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}


%if %{with_tests}
%check
: Generate tests autoloader
mkdir vendor
%{_bindir}/phpab --output vendor/autoload.php tests

: Run upstream test suite
ret=0
for cmd in php php71 php72; do
  if which $cmd; then
    $cmd -d auto_prepend_file=%{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}/autoload.php \
      %{_bindir}/phpunit6 --verbose || ret=1
  fi
done
exit $ret
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc README.md
%doc composer.json
%dir %{php_home}/%{ns_vendor}
     %{php_home}/%{ns_vendor}/%{ns_project}


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jan 29 2018 Remi Collet <remi@remirepo.net> - 2.0.0-1
- Update to 2.0.0
- rename to php-phpunit-php-invoker2
- raise dependency on PHP 7.1
- move to PSR-0 tree (/usr/share/php/SebastianBergmann/Invoker)
- switch to phpunit6
- switch to fedora/autoloader

* Sun Jun 21 2015 Remi Collet <remi@fedoraproject.org> - 1.1.4-1
- update to 1.1.4
- raise dependencies on PHP >= 5.3.3 and php-timer >= 1.0.6
- generate autoloader

* Fri Jul 18 2014 Remi Collet <remi@fedoraproject.org> - 1.1.3-6
- add composer dependencies

* Wed Apr 30 2014 Remi Collet <remi@fedoraproject.org> - 1.1.3-4
- cleanup pear registry

* Wed Apr 23 2014 Remi Collet <remi@fedoraproject.org> - 1.1.3-3
- get sources from github
- run test suite when build --with tests

* Tue Jul 16 2013 Remi Collet <remi@fedoraproject.org> - 1.1.3-1
- Update to 1.1.3 (stable) - API 1.1.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Oct  6 2012 Remi Collet <remi@fedoraproject.org> - 1.1.2-1
- Update to 1.1.2 (stable) - API 1.1.0

* Mon Sep 24 2012 Remi Collet <remi@fedoraproject.org> - 1.1.1-1
- Update to 1.1.1 (stable) - API 1.1.0

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jan 24 2012 Remi Collet <remi@fedoraproject.org> - 1.1.0-1
- Update to 1.1.0 (stable) - API 1.1.0
- now requires PHP_Timer

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Nov 26 2011 Remi Collet <remi@fedoraproject.org> - 1.0.1-1
- Update to 1.0.1 (stable) - API 1.0.0

* Tue Nov 01 2011 Remi Collet <remi@fedoraproject.org> - 1.0.0-3
- fix provides

* Tue Nov 01 2011 Remi Collet <remi@fedoraproject.org> - 1.0.0-2
- new tarball, with documentation

* Tue Nov 01 2011 Remi Collet <remi@fedoraproject.org> - 1.0.0-1
- initial generated RPM by pear make-rpm-spec + cleanups

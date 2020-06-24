# remirepo/fedora spec file for php-sebastian-environment3
#
# Copyright (c) 2014-2017 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global bootstrap    0
%global gh_commit    cd0871b3975fb7fc44d11314fd1ee20925fce4f5
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sebastianbergmann
%global gh_project   environment
%global pk_vendor    sebastian
%global pk_project   %{gh_project}
%global major        3
%global php_home     %{_datadir}/php
%global ns_vendor    SebastianBergmann
%global ns_project   Environment
%if %{bootstrap}
%global with_tests   0%{?_with_tests:1}
%else
%global with_tests   0%{!?_without_tests:1}
%endif

Name:           php-%{pk_vendor}-%{pk_project}%{major}
Version:        3.1.0
Release:        7%{?dist}
Summary:        Handle HHVM/PHP environments

License:        BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{name}-%{version}-%{gh_short}.tar.gz

BuildArch:      noarch
BuildRequires:  php(language) >= 7.0
BuildRequires:  php-pcre
BuildRequires:  php-posix
# Autoloader
BuildRequires:  php-fedora-autoloader-devel >= 1.0.0
%if %{with_tests}
# from composer.json, "require-dev": {
#        "phpunit/phpunit": "^6.1"
BuildRequires:  phpunit6 >= 6.1
%endif

# from composer.json, "require": {
#        "php": "^7.0"
Requires:       php(language) >= 7.0
# From phpcompatinfo report for 3.0.2
Requires:       php-pcre
Requires:       php-posix
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}


%description
This component provides functionality that helps writing PHP code that
has runtime-specific (PHP / HHVM) execution paths.


%prep
%setup -q -n %{gh_project}-%{gh_commit}


%build
# Generate the Autoloader
%{_bindir}/phpab \
   --template fedora2 \
   --output src/autoload.php \
   src


%install
mkdir -p   %{buildroot}%{php_home}/%{ns_vendor}
cp -pr src %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}


%if %{with_tests}
%check
: Run tests - set include_path to ensure PHPUnit autoloader use it
ret=0
for cmd in php php70 php71 php72; do
  if which $cmd; then
   $cmd -d include_path=.:%{buildroot}%{php_home}:%{php_home} \
     %{_bindir}/phpunit6 --bootstrap %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php \
       --verbose || ret=1
  fi
done
exit $ret
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc README.md composer.json
%dir %{php_home}/%{ns_vendor}
     %{php_home}/%{ns_vendor}/%{ns_project}%{major}


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jul  2 2017 Remi Collet <remi@remirepo.net> - 3.1.0-1
- Update to 3.1.0

* Wed Jun 21 2017 Remi Collet <remi@remirepo.net> - 3.0.4-1
- Update to 3.0.4

* Mon May 22 2017 Remi Collet <remi@remirepo.net> - 3.0.3-1
- Update to 3.0.3

* Mon May  1 2017 Remi Collet <remi@remirepo.net> - 3.0.2-1
- enable test suite

* Sun Apr 30 2017 Remi Collet <remi@remirepo.net> - 3.0.2-0
- boostrap build for review #1444648

* Sun Apr 23 2017 Remi Collet <remi@remirepo.net> - 3.0.2-1
- rename to php-sebastian-environment3
- update to 3.0.2

* Sat Nov 26 2016 Remi Collet <remi@fedoraproject.org> - 2.0.0-1
- update to 2.0.0
- raise dependency on PHP 5.6
- switch to fedora/autoloader

* Wed Aug 31 2016 Remi Collet <remi@fedoraproject.org> - 1.3.8-1
- update to 1.3.8

* Tue May 17 2016 Remi Collet <remi@fedoraproject.org> - 1.3.7-1
- update to 1.3.7
- add explicit dependencies on pcre and posix

* Wed May  4 2016 Remi Collet <remi@fedoraproject.org> - 1.3.6-1
- update to 1.3.6

* Sun Feb 28 2016 Remi Collet <remi@fedoraproject.org> - 1.3.5-1
- update to 1.3.5

* Wed Dec  2 2015 Remi Collet <remi@fedoraproject.org> - 1.3.3-1
- update to 1.3.3 (no change on linux)
- run test suite with both php 5 and 7 when available

* Mon Aug  3 2015 Remi Collet <remi@fedoraproject.org> - 1.3.2-1
- update to 1.3.2

* Sun Aug  2 2015 Remi Collet <remi@fedoraproject.org> - 1.3.1-1
- update to 1.3.1

* Sun Jul 26 2015 Remi Collet <remi@fedoraproject.org> - 1.3.0-1
- update to 1.3.0

* Fri Apr  3 2015 Remi Collet <remi@fedoraproject.org> - 1.2.2-1
- update to 1.2.2
- fix license handling

* Tue Dec  2 2014 Remi Collet <remi@fedoraproject.org> - 1.2.1-1
- update to 1.2.1

* Sat Oct 25 2014 Remi Collet <remi@fedoraproject.org> - 1.2.0-1
- update to 1.2.0

* Wed Oct  8 2014 Remi Collet <remi@fedoraproject.org> - 1.1.0-1
- update to 1.1.0

* Sun Oct  5 2014 Remi Collet <remi@fedoraproject.org> - 1.0.1-1
- update to 1.0.1
- enable test suite

* Wed Jun 25 2014 Remi Collet <remi@fedoraproject.org> - 1.0.0-4
- composer dependencies

* Wed Apr 23 2014 Remi Collet <remi@fedoraproject.org> - 1.0.0-2
- add generated autoload.php

* Tue Apr  1 2014 Remi Collet <remi@fedoraproject.org> - 1.0.0-1
- initial package

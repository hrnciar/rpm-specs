# remirepo/fedora spec file for php-phpunit-PHP-Invoker
#
# Copyright (c) 2011-2018 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global bootstrap    0
%global gh_commit    86074bf0fc2caf02ec8819a93f65a37cd0b44c8e
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sebastianbergmann
%global gh_project   php-invoker
%global php_home     %{_datadir}/php
%global pear_name    PHP_Invoker
%global pear_channel pear.phpunit.de
%if %{bootstrap}
%global with_tests   %{?_with_tests:1}%{!?_with_tests:0}
%else
%global with_tests   %{?_without_tests:0}%{!?_without_tests:1}
%endif

Name:           php-phpunit-PHP-Invoker
Version:        1.1.4
Release:        11%{?dist}
Summary:        Utility class for invoking callables with a timeout

License:        BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{gh_project}-%{version}-%{gh_short}.tar.gz

BuildArch:      noarch
BuildRequires:  php(language) >= 5.2.7
BuildRequires:  %{_bindir}/phpab
%if %{with_tests}
BuildRequires:  %{_bindir}/phpunit
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
BuildRequires:  (php-composer(phpunit/php-timer) >= 1.0.6 with php-composer(phpunit/php-timer) < 2)
%else
BuildRequires:  php-phpunit-PHP-Timer >= 1.0.6
%endif
%endif

# From composer.json
#        "php": ">=5.3.3",
#        "phpunit/php-timer": ">=1.0.6",
#        "ext-pcntl": "*"
Requires:       php(language) >= 5.3.3
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
Requires:       (php-composer(phpunit/php-timer) >= 1.0.6 with php-composer(phpunit/php-timer) < 2)
%else
Requires:       php-phpunit-PHP-Timer >= 1.0.6
%endif

Requires:       php-pcntl
# From phpcompatinfo report for version 1.0.5
Requires:       php-spl

Provides:       php-composer(phpunit/php-invoker) = %{version}

# For compatibility with PEAR mode
Provides:       php-pear(%{pear_channel}/%{pear_name}) = %{version}


%description
Utility class for invoking callables with a timeout.


%prep
%setup -q -n %{gh_project}-%{gh_commit}

: Restore previous PSR-0 layout
mkdir -p PHP/Invoker
mv src/Invoker.php PHP/
mv src/*.php       PHP/Invoker/
rmdir src


%build
: Generate autoloader
%{_bindir}/phpab \
   --output  PHP/Invoker/Autoload.php \
   --basedir PHP/Invoker \
   PHP

cat << EOF | tee -a PHP/Invoker/Autoload.php
// Dependencies
require_once 'PHP/Timer/Autoload.php';
EOF


%install
mkdir -p   %{buildroot}%{php_home}
cp -pr PHP %{buildroot}%{php_home}


%if %{with_tests}
%check
: Generate tests autoloader
%{_bindir}/phpab \
   --output tests/bs.php \
   tests

: Run upstream test suite
%{_bindir}/phpunit \
  --include-path %{buildroot}%{php_home} \
  --bootstrap tests/bs.php \
  --verbose
%endif


%post
if [ -x %{_bindir}/pear ]; then
   %{_bindir}/pear uninstall --nodeps --ignore-errors --register-only \
      %{pear_channel}/%{pear_name} >/dev/null || :
fi

%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc README.md
%doc composer.json
%{php_home}/PHP/Invoker*


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Dec  4 2018 Remi Collet <remi@fedoraproject.org> - 1.1.4-7
- cleanup for EL-8

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb  2 2018 Remi Collet <remi@remirepo.net> - 1.1.4-5
- use range dependencies on F27+

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jun 21 2015 Remi Collet <remi@fedoraproject.org> - 1.1.4-1
- update to 1.1.4
- raise dependencies on PHP >= 5.3.3 and php-timer >= 1.0.6
- generate autoloader

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jul 18 2014 Remi Collet <remi@fedoraproject.org> - 1.1.3-6
- add composer dependencies

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Apr 30 2014 Remi Collet <remi@fedoraproject.org> - 1.1.3-4
- cleanup pear registry

* Wed Apr 23 2014 Remi Collet <remi@fedoraproject.org> - 1.1.3-3
- get sources from github
- run test suite when build --with tests

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

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


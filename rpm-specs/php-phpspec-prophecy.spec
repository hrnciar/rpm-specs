# remirepo/fedora spec file for php-phpspec-prophecy
#
# Copyright (c) 2015-2019 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global bootstrap    0
%global gh_commit    451c3cd1418cf640de218914901e51b064abb093
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     phpspec
%global gh_project   prophecy
%if %{bootstrap}
# no test because of circular dependency with phpspec
%global with_tests   0%{?_with_tests:1}
%else
%global with_tests   0%{!?_without_tests:1}
%endif

Name:           php-phpspec-prophecy
Version:        1.10.3
Release:        1%{?dist}
Summary:        Highly opinionated mocking framework for PHP

License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source2:        makesrc.sh

# Autoloader
Source1:        %{name}-autoload.php

BuildArch:      noarch
%if %{with_tests}
# from composer.json, "require-dev": {
#        "phpspec/phpspec": "^2.5|^3.2"
#        "phpunit/phpunit": "^4.8.35 || ^5.7 || ^6.5 || ^7.1"
BuildRequires:  php-composer(phpspec/phpspec) >= 2.5
# Autoloader
BuildRequires:  php-composer(fedora/autoloader)
%endif

# from composer.json, "requires": {
#        "php":                               "^5.3|^7.0",
#        "phpdocumentor/reflection-docblock": "^2.0|^3.0.2|^4.0|^5.0",
#        "sebastian/comparator":              "^1.2.3|^2.0|^3.0|^4.0",
#        "doctrine/instantiator":             "^1.0.2",
#        "sebastian/recursion-context":       "^1.0|^2.0|^3.0|^4.0"
Requires:       php(language) >= 5.3
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
Requires:       (php-composer(phpdocumentor/reflection-docblock) >= 2.0   with php-composer(phpdocumentor/reflection-docblock) < 6)
Requires:       (php-composer(sebastian/comparator)              >= 1.2.3 with php-composer(sebastian/comparator)              < 5)
# recursion-context will be pulled by phpspec or phpunit or phpunit6
#Requires:      (php-composer(sebastian/recursion-context)       >= 1.0   with php-composer(sebastian/recursion-context)       < 4)
# use 1.0.4 to ensure we have the autoloader
Requires:       (php-composer(doctrine/instantiator)             >= 1.0.4 with php-composer(doctrine/instantiator)             < 2)
%else
Requires:       php-composer(phpdocumentor/reflection-docblock) >= 2.0
# ignore v4 for now
Requires:       php-composer(phpdocumentor/reflection-docblock) <  4
Requires:       php-composer(sebastian/comparator)              >= 1.2.3
Requires:       php-composer(sebastian/comparator)              <  3
# recursion-context will be pulled by phpspec or phpunit or phpunit6
#Requires:       php-composer(sebastian/recursion-context)       >= 1.0
#Requires:       php-composer(sebastian/recursion-context)       <  4
# use 1.0.4 to ensure we have the autoloader
Requires:       php-composer(doctrine/instantiator)             >= 1.0.4
Requires:       php-composer(doctrine/instantiator)             <  2
%endif
# From phpcompatinfo report for version 1.1.0
Requires:       php-pcre
Requires:       php-reflection
Requires:       php-spl
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(phpspec/prophecy) = %{version}


%description
Prophecy is a highly opinionated yet very powerful and flexible PHP object
mocking framework.

Though initially it was created to fulfil phpspec2 needs, it is flexible enough
to be used inside any testing framework out there with minimal effort.


%prep
%setup -q -n %{gh_project}-%{gh_commit}

cp %{SOURCE1} src/Prophecy/autoload.php


%build
# Nothing


%install
mkdir -p     %{buildroot}%{_datadir}/php
cp -pr src/* %{buildroot}%{_datadir}/php


%check
%if %{with_tests}
: check autoloader
php %{buildroot}%{_datadir}/php/Prophecy/autoload.php

: check phpspec
phpspec --version
VER=$(phpspec --version | sed -n -e 's/.* //;s/\..*$//;p')
if [ $VER -ge 4 ]; then
  : phpspec $VER is too recent
  exit 0
fi

ret=0
for cmd in php php70 php71 php72 php73 php74; do
  if which $cmd; then
    $cmd -d include_path=.:%{buildroot}%{_datadir}/php:%{_datadir}/php \
      %{_bindir}/phpspec run --format pretty --verbose --no-ansi || ret=1
  fi
done
exit $ret
%else
: Test suite disabled
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc *.md
%doc composer.json
%{_datadir}/php/Prophecy


# TODO ignore phpdocumentor/reflection-docblock 5.0
# not yet packaged

%changelog
* Fri Mar  6 2020 Remi Collet <remi@remirepo.net> - 1.10.3-1
- update to 1.10.3
- allow phpdocumentor/reflection-docblock 5.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 21 2020 Remi Collet <remi@remirepo.net> - 1.10.2-1
- update to 1.10.2
- allow sebastian/comparator 4 and sebastian/recursion-context 4

* Fri Jan  3 2020 Remi Collet <remi@remirepo.net> - 1.10.1-1
- update to 1.10.1

* Fri Oct  4 2019 Remi Collet <remi@remirepo.net> - 1.9.0-1
- update to 1.9.0

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 13 2019 Remi Collet <remi@remirepo.net> - 1.8.1-1
- update to 1.8.1

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Aug 20 2018 Remi Collet <remi@remirepo.net> - 1.8.0-1
- update to 1.8.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Apr 19 2018 Remi Collet <remi@remirepo.net> - 1.7.6-1
- update to 1.7.6

* Tue Feb 20 2018 Remi Collet <remi@remirepo.net> - 1.7.5-1
- Update to 1.7.5

* Mon Feb 12 2018 Remi Collet <remi@remirepo.net> - 1.7.4-1
- Update to 1.7.4
- use range dependency on F27+

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Nov 27 2017 Remi Collet <remi@remirepo.net> - 1.7.3-1
- Update to 1.7.3

* Tue Sep  5 2017 Remi Collet <remi@remirepo.net> - 1.7.2-1
- Update to 1.7.2

* Mon Sep  4 2017 Remi Collet <remi@remirepo.net> - 1.7.1-1
- Update to 1.7.1
- use git snapshot for sources
- skip test with phpspec v4

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Apr 13 2017 Shawn Iwinski <shawn@iwin.ski> - 1.7.0-4
- Prepare for php-phpdocumentor-reflection-docblock =>
  php-phpdocumentor-reflection-docblock2 dependency rename
- Update autoloader to try loading newest
  php-composer(phpdocumentor/reflection-docblock), then try loading older v2,
  then trigger an error if neither are found in include path

* Sat Mar  4 2017 Remi Collet <remi@remirepo.net> - 1.7.0-3
- drop implicit dependency on sebastian/recursion-context

* Fri Mar  3 2017 Remi Collet <remi@remirepo.net> - 1.7.0-2
- fix autoloader for dep. with multiple versions

* Fri Mar  3 2017 Remi Collet <remi@remirepo.net> - 1.7.0-1
- Update to 1.7.0

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Nov 22 2016 Remi Collet <remi@fedoraproject.org> - 1.6.2-1
- update to 1.6.2
- allow sebastian/recursion-context 2.0
- switch to fedora/autoloader

* Tue Jun  7 2016 Remi Collet <remi@fedoraproject.org> - 1.6.1-1
- update to 1.6.1

* Mon Feb 15 2016 Remi Collet <remi@fedoraproject.org> - 1.6.0-1
- update to 1.6.0
- add dependency on sebastian/recursion-context
- run test suite with both PHP 5 and 7 when available
- ignore 1 failed spec with PHP 7
  open https://github.com/phpspec/prophecy/issues/258

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Oct 28 2015 Remi Collet <remi@fedoraproject.org> - 1.5.0-2
- fix autolaoder, rely on include_path for symfony/class-loader

* Thu Aug 13 2015 Remi Collet <remi@fedoraproject.org> - 1.5.0-1
- update to 1.5.0

* Mon Jun 29 2015 Remi Collet <remi@fedoraproject.org> - 1.4.1-4
- use symfony/class-loader
- enable test suite

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue May  5 2015 Remi Collet <remi@fedoraproject.org> - 1.4.1-2
- enable test suite

* Tue Apr 28 2015 Remi Collet <remi@fedoraproject.org> - 1.4.1-1
- update to 1.4.1

* Sun Mar 29 2015 Remi Collet <remi@fedoraproject.org> - 1.4.0-1
- update to 1.4.0
- add dependency on sebastian/comparator

* Fri Feb 13 2015 Remi Collet <remi@fedoraproject.org> - 1.3.1-1
- initial package

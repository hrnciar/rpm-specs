#
# Fedora spec file for php-deepend-Mockery
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#
%global gh_commit    60fa2f67f6e4d3634bb4a45ff3171fa52215800d
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     mockery
%global gh_project   mockery
%global ns_project   Mockery
%global major        1
%global with_tests   0%{!?_without_tests:1}

Name:           php-mockery
Version:        1.3.3
Release:        1%{?dist}
Summary:        Mockery is a simple but flexible PHP mock object framework

License:        BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

# Use our autoloader
Patch0:         %{gh_project}-tests.patch

BuildArch:      noarch
%if %{with_tests}
BuildRequires:  php(language) >= 5.6.0
# From composer.json, "require-dev": {
#        "phpunit/phpunit": "^5.7.10|^6.5|^7.5|^8.5|^9.3"
%global phpunit %{_bindir}/phpunit9
BuildRequires: phpunit9
BuildRequires:  (php-composer(hamcrest/hamcrest-php) >= 2.0.1 with php-composer(hamcrest/hamcrest-php) < 3)
# Autoloader
%endif
BuildRequires:  php-fedora-autoloader-devel

# From composer.json, "require": {
#        "php": ">=5.6.0",
#        "lib-pcre": ">=7.0",
#        "hamcrest/hamcrest-php": "~2.0"
Requires:       php(language) >= 5.6.0
Requires:       (php-composer(hamcrest/hamcrest-php) >= 2.0.1 with php-composer(hamcrest/hamcrest-php) < 3)
# From phpcompatinfo report for version 1.0
Requires:       php-pcre
Requires:       php-spl
Requires:       php-reflection
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(mockery/mockery) = %{version}


%description
Mockery is a simple but flexible PHP mock object framework for use in unit 
testing. It is inspired by Ruby's flexmock and Java's Mockito, borrowing 
elements from both of their APIs.

Autoloader: %{_datadir}/php/%{ns_project}%{major}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}

mv library/*.php library/%{ns_project}/
phpab --template fedora --output library/%{ns_project}/autoload.php library

cat << 'EOF' | tee -a library/%{ns_project}/autoload.php

\Fedora\Autoloader\Dependencies::required([
    '/usr/share/php/Hamcrest2/autoload.php',
]);
EOF

%patch0 -p0 -b .rpm

rm -f docs/.gitignore


%build
# Empty build section, most likely nothing required.


%install
mkdir -p %{buildroot}/%{_datadir}/php
cp -rp library/%{ns_project} %{buildroot}/%{_datadir}/php/%{ns_project}%{major}


%check
%if %{with_tests}
: Use installed tree and our autoloader
export COMPOSER_VENDOR_DIR=%{buildroot}%{_datadir}/php/%{ns_project}%{major}

phpab --output tests/classmap.php --exclude */SemiReservedWordsAsMethods.php tests/Mockery

: Run upstream test suite
ret=0
for cmd in "php %{phpunit}" "php72 %{_bindir}/phpunit8" php73 php74 php80; do
  if which $cmd; then
    set $cmd
    # see .travis.yml
    if [ $($1 -r 'echo PHP_MAJOR_VERSION;') -lt 7 ]
    then SUITE="Mockery Test Suite PHP56"
    else SUITE="Mockery Test Suite"
    fi
    $1 ${2:-%{_bindir}/phpunit9} \
      --no-coverage \
      --verbose --testsuite="$SUITE" || ret=1
  fi
done
exit $ret
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc *.md docs
%doc composer.json
%{_datadir}/php/%{ns_project}%{major}


%changelog
* Mon Aug 17 2020 Remi Collet <remi@remirepo.net> - 1.3.3-1
- update to 1.3.3

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 21 2020 Remi Collet <remi@remirepo.net> - 1.3.2-1
- update to 1.3.2
- switch to phpunit9
- raise dependency on hamcrest/hamcrest-php 2.0.1
- sources from git snapshot

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan  3 2020 Remi Collet <remi@remirepo.net> - 1.3.1-1
- update to 1.3.1

* Mon Nov 25 2019 Remi Collet <remi@remirepo.net> - 1.3.0-1
- update to 1.3.0
- use phpunit8

* Mon Sep 30 2019 Remi Collet <remi@remirepo.net> - 1.2.4-1
- update to 1.2.4
- drop patch merged upstream

* Mon Aug 19 2019 Remi Collet <remi@remirepo.net> - 1.2.3-1
- update to 1.2.3
- add patch for PHP 7.4 from
  https://github.com/mockery/mockery/pull/993

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb 13 2019 Remi Collet <remi@remirepo.net> - 1.2.2-1
- update to 1.2.2

* Mon Feb 11 2019 Remi Collet <remi@remirepo.net> - 1.2.1-1
- update to 1.2.1

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct  3 2018 Remi Collet <remi@remirepo.net> - 1.2.0-1
- update to 1.2.0
- switch to phpunit7

* Sun May 13 2018 Remi Collet <remi@remirepo.net> - 1.1.0-1
- update to 1.1.0

* Mon Jan 22 2018 Remi Collet <remi@remirepo.net> - 1.0-1
- Update to 1.0
- rename to php-mockery and move to /usr/share/php/Mockery1
- raise dependency on PHP 5.6
- raise dependency on hamcrest/hamcrest-php 2.0
- use phpunit6 on F26+

* Fri Oct  6 2017 Remi Collet <remi@remirepo.net> - 0.9.9-4
- add patches for PHP 7.2

* Tue Feb 28 2017 Remi Collet <remi@remirepo.net> - 0.9.9-1
- Update to 0.9.9

* Fri Feb 10 2017 Remi Collet <remi@remirepo.net> - 0.9.8-1
- Update to 0.9.8

* Fri Dec 23 2016 Remi Collet <remi@fedoraproject.org> - 0.9.7-1
- Update to 0.9.7

* Sat Nov 26 2016 Remi Collet <remi@fedoraproject.org> - 0.9.6-1
- Update to 0.9.6
- switch to fedora/autoloader

* Tue Jun 14 2016 Remi Collet <remi@fedoraproject.org> - 0.9.5-1
- Update to 0.9.5

* Fri Oct 16 2015 Remi Collet <remi@fedoraproject.org> - 0.9.3-1
- downgrade to 0.9.3

* Fri Oct 16 2015 Remi Collet <remi@fedoraproject.org> - 0.9.4-1
- Update to 0.9.4
- add autoloader using symfony/class-loader
- add dependency on hamcrest/hamcrest-php
- run test suite
- use github archive from commit reference

* Wed Jul 16 2014 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.9.1-2
- fixed requires (Remi)
- add script which will delete older pear package if installed (Remi)
- fix provides/obsoletes (Remi)

* Tue Jul 15 2014 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.9.1-1
- update to 0.9.1 (RHBZ #1119451)

* Tue Feb 11 2014 Remi Collet <remi@fedoraproject.org> - 0.9.0-1
- Update to 0.9.0

* Fri Apr 19 2013 Remi Collet <remi@fedoraproject.org> - 0.8.0-1
- Update to 0.8.0 (backport)

* Thu Apr 18 2013 Christof Damian <christof@damian.net> - 0.8.0-1
- upstream 0.8.0

* Sun Mar 04 2012 Remi Collet <RPMS@FamilleCollet.com> - 0.7.2-1
- upstream 0.7.2, rebuild for remi repository

* Sun Mar  4 2012 Christof Damian <christof@damian.net> - 0.7.2-1
- upstream 0.7.2

* Tue Jul 27 2010 Remi Collet <RPMS@FamilleCollet.com> - 0.6.3-2
- rebuild for remi repository

* Tue Jul 27 2010 Christof Damian <christof@damian.net> - 0.6.3-2
- add license and readme file from github

* Fri May 28 2010 Christof Damian <christof@damian.net> - 0.6.0-1
- initial packaging



# remirepo/fedora spec file for php-bartlett-PHP-CompatInfo
#
# Copyright (c) 2011-2020 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

# For compatibility with SCL
%undefine __brp_mangle_shebangs

%{!?php_version:  %global php_version  %(php -r 'echo PHP_VERSION;' 2>/dev/null)}
%global gh_commit    5b58fb55f2a759f6c134d1649d1e1df1b8cd5cf2
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
#global gh_date      20151005
%global gh_owner     llaville
%global gh_project   php-compat-info
#global prever       RC2
%bcond_without       tests

%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
%global sym_prefix php-symfony3
%else
%global sym_prefix php-symfony
%endif

Name:           php-bartlett-PHP-CompatInfo
Version:        5.3.0
%global specrel 1
Release:        %{?gh_date:1%{specrel}.%{?prever}%{!?prever:%{gh_date}git%{gh_short}}}%{!?gh_date:%{specrel}}%{?dist}.1
Summary:        Find out version and the extensions required for a piece of code to run

License:        BSD
URL:            http://php5.laurent-laville.org/compatinfo/
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{name}-%{version}%{?prever}-%{gh_short}.tar.gz

# Script for fedora-review
Source1:        fedora-review-check

# RPM autoloader
Source2:        %{name}-5.1.0-autoload.php

# Autoload and sqlite database path
# avoid jean85/pretty-package-versions
Patch0:         %{name}-5.3.0-rpm.patch

BuildArch:      noarch
BuildRequires:  php(language) >= 7.1.3
%if %{with tests}
# to run test suite
BuildRequires:  php-pdo_sqlite
BuildRequires:  (php-composer(bartlett/php-reflect)       >= 4.4  with php-composer(bartlett/php-reflect)       < 5)
BuildRequires:  (php-composer(bartlett/php-compatinfo-db) >= 2.0  with php-composer(bartlett/php-compatinfo-db) < 3)
BuildRequires:  (php-composer(psr/log)                    >= 1.0  with php-composer(psr/log)                    < 2)
BuildRequires:  (php-composer(doctrine/cache)             >= 1.3  with php-composer(doctrine/cache)             < 2)
%global phpunit %{_bindir}/phpunit8
BuildRequires:  %{phpunit}
# For our patch / autoloader
BuildRequires:  php-composer(fedora/autoloader)
%endif

# From composer.json, "require"
#        "php": "^7.1.3",
#        "ext-libxml": "*",
#        "ext-pcre": "*",
#        "ext-spl": "*",
#        "ext-json": "*",
#        "ext-pdo": "*",
#        "ext-pdo_sqlite": "*",
#        "bartlett/php-reflect": "^4.4",
#        "bartlett/php-compatinfo-db": "^2.0",
#        "jean85/pretty-package-versions": "^1.5",
#        "psr/log": "^1.0"
Requires:       php(language) >= 7.1.3
Requires:       php-cli
Requires:       php-json
Requires:       php-libxml
Requires:       php-pcre
Requires:       php-pdo
Requires:       php-pdo_sqlite
Requires:       php-spl
Requires:       (php-composer(bartlett/php-reflect)       >= 4.4  with php-composer(bartlett/php-reflect)       < 5)
Requires:       (php-composer(bartlett/php-compatinfo-db) >= 2.0  with php-composer(bartlett/php-compatinfo-db) < 3)
Requires:       (php-composer(psr/log)                    >= 1.0  with php-composer(psr/log)                    < 2)
# Mandatory for our patch
Requires:       (php-composer(doctrine/cache)             >= 1.3  with php-composer(doctrine/cache)             < 2)
Requires:       php-composer(fedora/autoloader)

Provides:       phpcompatinfo = %{version}
Provides:       php-composer(bartlett/php-compatinfo) = %{version}


%description
PHP_CompatInfo will parse a file/folder/array to find out the minimum
version and extensions required for it to run. CLI version has many reports
(extension, interface, class, function, constant) to display and ability to
show content of dictionary references.

Documentation: http://php5.laurent-laville.org/compatinfo/manual/current/en/


%prep
%setup -q -n %{gh_project}-%{gh_commit}

%patch0 -p1 -b .rpm
cp %{SOURCE2} src/Bartlett/CompatInfo/autoload.php

# Cleanup patched files
find src -name \*rpm -delete -print

# Check package version
FILE=src/Bartlett/CompatInfo/Console/Application.php
grep " VERSION" $FILE
sed -e '/VERSION/s/5.3.x-dev/%{version}/' -i $FILE
grep %{version} $FILE


%build
# Nothing


%install
mkdir -p %{buildroot}%{_datadir}/php
cp -pr src/Bartlett %{buildroot}%{_datadir}/php/Bartlett

install -D -p -m 755 bin/phpcompatinfo           %{buildroot}%{_bindir}/phpcompatinfo
install -D -p -m 644 bin/phpcompatinfo.json.dist %{buildroot}%{_sysconfdir}/phpcompatinfo.json
install -D -p -m 644 bin/phpcompatinfo.1         %{buildroot}%{_mandir}/man1/phpcompatinfo.1

install -D -p -m 755 %{SOURCE1}                  %{buildroot}%{_datadir}/%{name}/fedora-review-check


%if %{with tests}
%check
mkdir vendor
ln -s %{buildroot}%{_datadir}/php/Bartlett/CompatInfo/autoload.php vendor/


ret=0
for cmdarg in "php %{phpunit}" php72 php73 php74 php80; do
  if which $cmdarg; then
    set $cmdarg
    $1 ${2:-%{_bindir}/phpunit8} \
       --include-path %{buildroot}%{_datadir}/php --verbose || ret=1
  fi
done
exit $ret
%endif


%post
if [ -x %{_bindir}/pear ]; then
   %{_bindir}/pear uninstall --nodeps --ignore-errors --register-only \
      bartlett.laurent-laville.org/PHP_CompatInfo >/dev/null || :
fi


%files
%license LICENSE
%doc composer.json README.*
%config(noreplace) %{_sysconfdir}/phpcompatinfo.json
%{_bindir}/phpcompatinfo
%{_datadir}/php/Bartlett/CompatInfo
%{_mandir}/man1/phpcompatinfo.1*
%{_datadir}/%{name}


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.0-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul  8 2020 Remi Collet <remi@remirepo.net> - 5.3.0-1
- update to 5.3.0
- raise dependency on PHP 7.1.3
- raise dependency on bartlett/php-reflect 4.4
- raise dependency on bartlett/php-compatinfo-db 2.0
- switch to phpunit8

* Wed Apr 29 2020 Remi Collet <remi@remirepo.net> - 5.2.3-1
- update to 5.2.3

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.1-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 22 2019 Remi Collet <remi@remirepo.net> - 5.2.1-1
- update to 5.2.1 (no change)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun  3 2019 Remi Collet <remi@remirepo.net> - 5.2.0-1
- update to 5.2.0
- allow bartlett/php-compatinfo-db v2

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 28 2018 Remi Collet <remi@remirepo.net> - 5.1.0-1
- update to 5.1.0
- raise dependency on bartlett/php-reflect 4.3
- add explicit dependency on nikic/php-parser
- add explicit dependency on doctrine/cache
- add dependency on psr/log
- switch to phpunit7

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.12-1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.12-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Feb  2 2018 Remi Collet <remi@remirepo.net> - 5.0.12-1
- Update to 5.0.12 (no change)
- use range dependency on F27+

* Tue Dec 12 2017 Remi Collet <remi@remirepo.net> - 5.0.11-1
- Update to 5.0.11 (no change)
- raise dependency on PHP 5.5

* Tue Dec 12 2017 Remi Collet <remi@remirepo.net> - 5.0.10-1
- Update to 5.0.10 (no change)
- raise dependency on bartlett/php-reflect 4.2
- only require a single Symfony version

* Wed Dec  6 2017 Remi Collet <remi@remirepo.net> - 5.0.9-1
- Update to 5.0.9

* Mon Aug  7 2017 Remi Collet <remi@remirepo.net> - 5.0.8-1
- Update to 5.0.8

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.7-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jun 10 2017 Remi Collet <remi@remirepo.net> - 5.0.7-1
- Update to 5.0.7

* Mon Mar 27 2017 Remi Collet <remi@remirepo.net> - 5.0.6-1
- Update to 5.0.6

* Fri Mar 17 2017 Remi Collet <remi@remirepo.net> - 5.0.5-1
- Update to 5.0.5

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.4-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 17 2017 Remi Collet <remi@fedoraproject.org> - 5.0.4-1
- update to 5.0.4

* Wed Jan 11 2017 Remi Collet <remi@fedoraproject.org> - 5.0.3-1
- update to 5.0.3

* Fri Dec 16 2016 Remi Collet <remi@fedoraproject.org> - 5.0.2-1
- update to 5.0.2

* Mon Oct 31 2016 Remi Collet <remi@fedoraproject.org> - 5.0.1-2
- switch to fedora/autoloader

* Wed Jul  6 2016 Remi Collet <remi@fedoraproject.org> - 5.0.1-1
- update to 5.0.1
- display DB version instead of build date

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Dec 10 2015 Remi Collet <remi@fedoraproject.org> - 5.0.0-1
- update to 5.0.0
- raise dependency on bartlett/php-reflect ~4.0
- raise minimal php version to 5.4
- add dependency on bartlett/php-compatinfo-db

* Wed Nov 25 2015 Remi Collet <remi@fedoraproject.org> - 4.5.2-1
- update to 4.5.2

* Sun Oct 11 2015 Remi Collet <remi@fedoraproject.org> - 4.5.1-1
- update to 4.5.1

* Tue Oct  6 2015 Remi Collet <remi@fedoraproject.org> - 4.5.0-1
- update to 4.5.0

* Mon Jul 20 2015 Remi Collet <remi@fedoraproject.org> - 4.4.0-2
- add upstream patch for Intl reference

* Mon Jul 13 2015 Remi Collet <remi@fedoraproject.org> - 4.4.0-1
- update to 4.4.0

* Mon Jun 29 2015 Remi Collet <remi@fedoraproject.org> - 4.3.0-4
- upstream patch for ldap extension in 5.6.11RC1 (thanks Koschei)

* Fri Jun 26 2015 Remi Collet <remi@fedoraproject.org> - 4.3.0-3
- rewrite autoloader

* Sun Jun 21 2015 Remi Collet <remi@fedoraproject.org> - 4.3.0-2
- fix autoloader

* Tue Jun 16 2015 Remi Collet <remi@fedoraproject.org> - 4.3.0-1
- update to 4.3.0

* Tue May 19 2015 Remi Collet <remi@fedoraproject.org> - 4.2.0-1
- update to 4.2.0
- raise dependency on bartlett/php-reflect 3.1
- add dependency on bartlett/umlwriter
- add fedora-review-check script
- handle --without tests option to skip test suite during build

* Mon Feb  2 2015 Remi Collet <remi@fedoraproject.org> - 3.7.3-1
- Update to 3.7.3

* Mon Jan  5 2015 Remi Collet <remi@fedoraproject.org> - 3.7.2-1
- Update to 3.7.2
- open https://github.com/llaville/php-compat-info/pull/157

* Fri Dec 19 2014 Remi Collet <remi@fedoraproject.org> - 3.7.1-1
- Update to 3.7.1

* Thu Nov 20 2014 Remi Collet <remi@fedoraproject.org> - 3.6.1-1
- Update to 3.6.1

* Thu Nov 13 2014 Remi Collet <remi@fedoraproject.org> - 3.6.0-1
- Update to 3.6.0
- add dependency on justinrainbow/json-schema
- raise dependency on bartlett/php-reflect 2.6

* Thu Oct 16 2014 Remi Collet <remi@fedoraproject.org> - 3.5.0-1
- Update to 3.5.0
- add dependency on sebastian/version
- raise dependency on bartlett/php-reflect 2.5

* Mon Oct  6 2014 Remi Collet <remi@fedoraproject.org> - 3.4.0-2
- fix FTBFS with PHP 5.6.1 (Thanks to Koschei)

* Thu Sep 25 2014 Remi Collet <remi@fedoraproject.org> - 3.4.0-1
- Update to 3.4.0

* Fri Aug 22 2014 Remi Collet <remi@fedoraproject.org> - 3.3.0-1
- Update to 3.2.0
- add dependency on seld/jsonlint
- raise dependency on bartlett/php-reflect 2.3
- enable the cache plugin in default configuration

* Fri Jul 25 2014 Remi Collet <remi@fedoraproject.org> - 3.2.0-1
- Update to 3.2.0
- add manpage
- sources from github
- patch autoloader to not rely on composer
- drop documentation (link to online doc in description)
- add upstream patch for SNMP extension

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.26.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Dec 13 2013 Remi Collet <remi@fedoraproject.org> - 2.26.0-1
- Update to 2.26.0 (stable)

* Thu Nov 14 2013 Remi Collet <remi@fedoraproject.org> - 2.25.0-1
- Update to 2.25.0
- remove phpci temporary compat command

* Fri Oct 18 2013 Remi Collet <remi@fedoraproject.org> - 2.24.0-1
- update to 2.24.0
- raise dependency, PHP_Reflect 1.9.0

* Mon Sep 23 2013 Remi Collet <remi@fedoraproject.org> - 2.23.1-1
- Update to 2.23.1
- raise dependencies: PHP 5.3.0, PHP_Reflect 1.8.0 (and < 2)

* Fri Aug 23 2013 Remi Collet <remi@fedoraproject.org> - 2.22.0-1
- Update to 2.22.0

* Tue Aug 20 2013 Remi Collet <remi@fedoraproject.org> - 2.21.0-1
- Update to 2.21.0
- patch for https://github.com/llaville/php-compat-info/issues/99

* Thu Jul 25 2013 Remi Collet <remi@fedoraproject.org> - 2.20.0-1
- Update to 2.20.0
- patch from https://github.com/llaville/php-compat-info/pull/98

* Fri Jul 12 2013 Remi Collet <remi@fedoraproject.org> - 2.19.0-1
- Update to 2.19.0
- add module and install to fileExtensions in default configuration
  for drupal packages, #979830
- patch from https://github.com/llaville/php-compat-info/pull/95

* Wed Jun 26 2013 Remi Collet <remi@fedoraproject.org> - 2.18.0-1
- Update to 2.18.0
- raise dependencies, PHP_Reflect 1.7.0
- drop PHP 5.5 patches, applied upstream
- add patch for windows only constants

* Fri Jun 07 2013 Remi Collet <remi@fedoraproject.org> - 2.17.0-2
- keep phpci command for now

* Fri Jun 07 2013 Remi Collet <remi@fedoraproject.org> - 2.17.0-1
- Update to 2.17.0
- phpci command renamed to phpcompatinfo

* Fri May 10 2013 Remi Collet <remi@fedoraproject.org> - 2.16.0-1
- Update to 2.16.0

* Fri Apr 12 2013 Remi Collet <remi@fedoraproject.org> - 2.15.0-2
- add upstream man page (from github)
- Update to 2.15.0
- raise dependencies, PHP_Reflect 1.6.2
- add more patches for PHP 5.5 reference

* Tue Apr 02 2013 Remi Collet <remi@fedoraproject.org> - 2.14.1-1
- Update to 2.14.1
- make cache path user dependent

* Mon Mar 18 2013 Remi Collet <remi@fedoraproject.org> - 2.14.0-2
- update References for PHP 5.5 from
  https://github.com/llaville/php-compat-info/commits/php-5.5

* Mon Mar 18 2013 Remi Collet <remi@fedoraproject.org> - 2.14.0-1
- Update to 2.14.0

* Tue Feb 26 2013 Remi Collet <remi@fedoraproject.org> - 2.13.2-1
- Update to 2.13.2
- raise dependencies, PHP_Reflect 1.6.1
- provides phpci
- patch for https://github.com/llaville/php-compat-info/issues/69

* Fri Feb 22 2013 Remi Collet <remi@fedoraproject.org> - 2.13.0-1
- Update to 2.13.0
- raise dependencies, PHP_Reflect 1.6.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 18 2013 Remi Collet <remi@fedoraproject.org> - 2.12.1-1
- update to Version 2.12.1
- fix path to documentation in description
- drop dependency on eZ components
- raise PHPUnit dependency to 3.6.0
- skip HashTest (mhash not available) on EL-6

* Fri Dec 21 2012 Remi Collet <remi@fedoraproject.org> - 2.11.0-1
- update to Version 2.11.0
- html documentation is now provided by upstream
- raise dependencies, PHP_Reflect 1.5.0, Console_CommandLine 1.2.0

* Sat Sep 29 2012 Remi Collet <remi@fedoraproject.org> - 2.8.1-1
- Version 2.8.1 (stable) - API 2.8.0 (stable)

* Mon Sep 17 2012 Remi Collet <remi@fedoraproject.org> - 2.8.0-1
- Version 2.8.0 (stable) - API 2.8.0 (stable)
- new extensions : amqp, geoip, inclued, xcache

* Mon Sep  3 2012 Remi Collet <remi@fedoraproject.org> - 2.7.0-1
- Version 2.7.0 (stable) - API 2.7.0 (stable)

* Sun Aug 19 2012 Remi Collet <remi@fedoraproject.org> - 2.6.0-3
- rebuilt for new pear_datadir

* Tue Aug 14 2012 Remi Collet <remi@fedoraproject.org> - 2.6.0-2
- rebuildt for new pear_testdir

* Wed Aug 01 2012 Remi Collet <remi@fedoraproject.org> - 2.6.0-1
- Version 2.6.0 (stable) - API 2.6.0 (stable)
- raise dependencies: PHPUnit 3.6.0, PHP_Reflect 1.4.2

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.0-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jul  8 2012 Remi Collet <remi@fedoraproject.org> - 2.5.0-1.1
- drop XslTest in EL-6

* Fri Jun 22 2012 Remi Collet <remi@fedoraproject.org> - 2.5.0-1
- Version 2.5.0 (stable) - API 2.5.0 (stable)
- use reference="ALL" in provided config

* Fri May 11 2012 Remi Collet <remi@fedoraproject.org> - 2.4.0-1.1
- add patch for old libxml

* Fri May 11 2012 Remi Collet <remi@fedoraproject.org> - 2.4.0-1
- Version 2.4.0 (stable) - API 2.3.0 (stable)

* Mon Mar 05 2012 Remi Collet <remi@fedoraproject.org> - 2.3.0-1
- Version 2.3.0 (stable) - API 2.3.0 (stable)

* Sat Feb 25 2012 Remi Collet <remi@fedoraproject.org> - 2.2.5-1
- Version 2.2.5 (stable) - API 2.2.0 (stable)

* Fri Feb 17 2012 Remi Collet <remi@fedoraproject.org> - 2.2.4-1
- Version 2.2.4 (stable) - API 2.2.0 (stable)

* Tue Feb 14 2012 Remi Collet <remi@fedoraproject.org> - 2.2.3-1
- Version 2.2.3 (stable) - API 2.2.0 (stable)

* Thu Feb 09 2012 Remi Collet <remi@fedoraproject.org> - 2.2.2-1
- Version 2.2.2 (stable) - API 2.2.0 (stable)

* Sun Feb 05 2012 Remi Collet <remi@fedoraproject.org> - 2.2.1-1
- Version 2.2.1 (stable) - API 2.2.0 (stable)

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Sep 24 2011 Remi Collet <remi@fedoraproject.org> - 2.1.0-3.1
- no html doc on EL6

* Wed Sep 21 2011 Remi Collet <remi@fedoraproject.org> - 2.1.0-3
- remove all files with licensing issue
  don't use it during test, don't install it
  can keep it in sources are this files are still under free license

* Tue Sep 20 2011 Remi Collet <remi@fedoraproject.org> - 2.1.0-2
- comments from review #693204
- remove ascii*js (not used)
- add MIT to license for bundled jquery

* Thu Aug 25 2011 Remi Collet <Fedora@FamilleCollet.com> - 2.1.0-1
- Version 2.1.0 (stable) - API 2.1.0 (stable)
- fix documentation for asciidoc 8.4

* Thu Jun 02 2011 Remi Collet <Fedora@FamilleCollet.com> - 2.0.0-1
- Version 2.0.0 (stable) - API 2.0.0 (stable)
- add HTML documentation

* Tue Apr 26 2011 Remi Collet <Fedora@FamilleCollet.com> - 2.0.0-0.3.RC4
- Version 2.0.0RC4 (beta) - API 2.0.0 (beta)

* Fri Mar 25 2011 Remi Collet <Fedora@FamilleCollet.com> - 2.0.0-0.2.RC3
- Version 2.0.0RC3

* Fri Feb 25 2011 Remi Collet <Fedora@FamilleCollet.com> - 2.0.0-0.1.RC2
- Version 2.0.0RC2
- Initial Release


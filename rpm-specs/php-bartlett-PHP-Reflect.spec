# remirepo/fedora spec file for php-bartlett-PHP-Reflect
#
# Copyright (c) 2011-2020 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global bootstrap    0
%global gh_commit    5010b4de0540a711f329a26c72bd48280a3d755a
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
#global gh_date      20150331
%global gh_owner     llaville
%global gh_project   php-reflect
#global prever       RC2
%if %{bootstrap}
%global with_tests   %{?_with_tests:1}%{!?_with_tests:0}
%else
%global with_tests   %{?_without_tests:0}%{!?_without_tests:1}
%endif

%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
%global sym_prefix php-symfony4
%global phpunit %{_bindir}/phpunit7
%else
%global sym_prefix php-symfony3
%global phpunit %{_bindir}/phpunit
%endif

Name:           php-bartlett-PHP-Reflect
Version:        4.3.1
%global specrel 1
Release:        %{?gh_date:1%{specrel}.%{?prever}%{!?prever:%{gh_date}git%{gh_short}}}%{!?gh_date:%{specrel}}%{?dist}
Summary:        Adds the ability to reverse-engineer PHP

License:        BSD
URL:            http://php5.laurent-laville.org/reflect/
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{name}-%{version}%{?prever}-%{gh_short}.tar.gz

# Autoloader for RPM - die composer !
Source1:        %{name}-autoload.php

# Enable cache plugin
Patch0:         %{name}-4.3.0-rpm.patch

BuildArch:      noarch
BuildRequires:  php(language) >= 5.5
%if %{with_tests}
# to run test suite
BuildRequires:  %{phpunit}
BuildRequires: (php-composer(sebastian/version)                 >= 1.0   with php-composer(sebastian/version)                 < 3)
BuildRequires: (php-composer(nikic/php-parser)                  >= 3.1   with php-composer(nikic/php-parser)                  < 4)
BuildRequires: (php-composer(doctrine/collections)              >= 1.4   with php-composer(doctrine/collections)              < 2)
BuildRequires: (php-composer(phpdocumentor/reflection-docblock) >= 3.0   with php-composer(phpdocumentor/reflection-docblock) < 4)
BuildRequires: (php-composer(seld/jsonlint)                     >= 1.1   with php-composer(seld/jsonlint)                     < 2)
BuildRequires: (php-composer(justinrainbow/json-schema)         >= 1.3   with php-composer(justinrainbow/json-schema)         < 2)
BuildRequires: (php-composer(monolog/monolog)                   >= 1.10  with php-composer(monolog/monolog)                   < 2)
BuildRequires: (php-composer(psr/log)                           >= 1.0   with php-composer(psr/log)                           < 2)
BuildRequires: (php-composer(doctrine/cache)                    >= 1.3   with php-composer(doctrine/cache)                    <  2)
BuildRequires:  %{sym_prefix}-event-dispatcher
BuildRequires:  %{sym_prefix}-finder
BuildRequires:  %{sym_prefix}-console
BuildRequires:  %{sym_prefix}-stopwatch
BuildRequires:  %{sym_prefix}-dependency-injection
# For our autoloader
BuildRequires:  php-composer(fedora/autoloader)
%endif

# From composer.json, "require": {
#        "php": "^5.5|^7.0",
#        "ext-tokenizer": "*",
#        "ext-pcre": "*",
#        "ext-spl": "*",
#        "ext-json": "*",
#        "ext-date": "*",
#        "ext-reflection": "*",
#        "sebastian/version": "^1.0|^2.0",
#        "nikic/php-parser": "^3.1",
#        "doctrine/collections": "^1.4",
#        "symfony/event-dispatcher": "^2.5|^3.0|^4.0",
#        "symfony/finder": "^2.5|^3.0|^4.0",
#        "symfony/console": "^2.5|^3.0|^4.0",
#        "symfony/stopwatch": "^2.5|^3.0|^4.0",
#        "symfony/dependency-injection": "^2.5|^3.0|^4.0",
#        "phpdocumentor/reflection-docblock": "^3.0",
#        "justinrainbow/json-schema": "^1.3",
#        "seld/jsonlint": "^1.1"
#        "psr/log": "^1.0"
Requires:       php(language) >= 5.5
Requires:       php-cli
Requires:       php-reflection
Requires:       php-date
Requires:       php-json
Requires:       php-pcre
Requires:       php-phar
Requires:       php-spl
Requires:       php-tokenizer
Requires:      (php-composer(sebastian/version)                 >= 1.0   with php-composer(sebastian/version)                 < 3)
Requires:      (php-composer(nikic/php-parser)                  >= 3.1   with php-composer(nikic/php-parser)                  < 4)
Requires:      (php-composer(doctrine/collections)              >= 1.4   with php-composer(doctrine/collections)              < 2)
Requires:      (php-composer(phpdocumentor/reflection-docblock) >= 3.0   with php-composer(phpdocumentor/reflection-docblock) < 4)
Requires:      (php-composer(seld/jsonlint)                     >= 1.1   with php-composer(seld/jsonlint)                     < 2)
Requires:      (php-composer(justinrainbow/json-schema)         >= 1.3   with php-composer(justinrainbow/json-schema)         < 2)
Requires:      (php-composer(psr/log)                           >= 1.0   with php-composer(psr/log)                           < 2)
# Mandatory for our patch
Requires:      (php-composer(doctrine/cache)                    >= 1.3   with php-composer(doctrine/cache)                    <  2)
Requires:       %{sym_prefix}-event-dispatcher
Requires:       %{sym_prefix}-finder
Requires:       %{sym_prefix}-console
Requires:       %{sym_prefix}-stopwatch
Requires:       %{sym_prefix}-dependency-injection
#    "require-dev": {
#        "monolog/monolog": "~1.10",
#    "suggest": {
#        "doctrine/cache": "Allow caching results"
#        "bartlett/phpunit-loggertestlistener": "Allow logging unit tests to your favorite PSR-3 logger interface",
#        "bartlett/umlwriter": "Allow writing UML class diagrams (Graphviz or PlantUML)"
%if ! %{bootstrap}
Requires:       php-composer(bartlett/umlwriter)       >= 1.0
Requires:       php-composer(bartlett/umlwriter)       <  2
%if 0%{?fedora} >= 21 || 0%{?rhel} >= 8
Suggests:       php-composer(monolog/monolog)
%endif
%endif
# For our autoloader
Requires:       php-composer(fedora/autoloader)

Obsoletes:      php-channel-bartlett <= 1.3

Provides:       php-composer(bartlett/php-reflect) = %{version}


%description
PHP_Reflect adds the ability to reverse-engineer classes, interfaces,
functions, constants and more, by connecting php callbacks to other tokens.

Documentation: http://php5.laurent-laville.org/reflect/manual/current/en/


%prep
%setup -q -n %{gh_project}-%{gh_commit}

%patch0 -p1 -b .rpm
find . -name \*.rpm -delete -print

cp %{SOURCE1} src/Bartlett/Reflect/autoload.php

sed -e 's/@package_version@/%{version}%{?prever}/' \
    -i $(find src -name \*.php) bin/phpreflect


%build
# Nothing


%install
mkdir -p %{buildroot}%{_datadir}/php
cp -pr src/Bartlett %{buildroot}%{_datadir}/php/Bartlett

install -D -p -m 755 bin/phpreflect           %{buildroot}%{_bindir}/phpreflect
install -D -p -m 644 bin/phpreflect.json.dist %{buildroot}%{_sysconfdir}/phpreflect.json
install -D -p -m 644 bin/phpreflect.1         %{buildroot}%{_mandir}/man1/phpreflect.1


%check
%if %{with_tests}
ret=0
for cmdarg in "php %{phpunit}" php72 php73 php74; do
  if which $cmdarg; then
    set $cmdarg
    $1 ${2:-%{_bindir}/phpunit7} \
      --include-path=%{buildroot}%{_datadir}/php \
      --verbose || ret=1
  fi
done
exit $ret
%else
: Test suite disabled
%endif


%post
if [ -x %{_bindir}/pear ]; then
   %{_bindir}/pear uninstall --nodeps --ignore-errors --register-only \
      bartlett.laurent-laville.org/PHP_Reflect >/dev/null || :
fi


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc composer.json README.*
%config(noreplace) %{_sysconfdir}/phpreflect.json
%{_bindir}/phpreflect
%{_datadir}/php/Bartlett/Reflect*
%{_mandir}/man1/phpreflect.1*


%changelog
* Wed Feb 26 2020 Remi Collet <remi@remirepo.net> - 4.3.1-1
- update to 4.3.1
- drop patch merged upstream

* Tue Feb 25 2020 Remi Collet <remi@remirepo.net> - 4.3.0-3
- fix compatibility with Symfony 4 using patch from
  https://github.com/llaville/php-reflect/pull/37

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-2.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-2.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Dec  9 2018 Remi Collet <remi@remirepo.net> - 4.3.0-2
- Fedora: switch to symfony4 only, see #1657328

* Mon Nov 26 2018 Remi Collet <remi@remirepo.net> - 4.3.0-1
- update to 4.3.0
- use range dependencies
- raise dependency on nikic/php-parser 3.1
- raise dependency on doctrine/collections 1.4
- add dependency on psr/log
- allow Symfony 4
- switch to phpunit7

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.2-2.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.2-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Dec 19 2017 Remi Collet <remi@remirepo.net> - 4.2.2-2
- fix autoloader to ensure nikic/php-parser v2 is used

* Thu Dec 14 2017 Remi Collet <remi@remirepo.net> - 4.2.2-1
- Update to 4.2.2

* Tue Dec 12 2017 Remi Collet <remi@remirepo.net> - 4.2.1-2
- fix regression with cache configuration
  from https://github.com/llaville/php-reflect/pull/27

* Tue Dec 12 2017 Remi Collet <remi@remirepo.net> - 4.2.1-1
- Update to 4.2.1 (no change)
- raise dependency on PHP 5.5

* Tue Dec 12 2017 Remi Collet <remi@remirepo.net> - 4.2.0-1
- Update to 4.2.0
- only require a single Symfony version

* Thu Oct  5 2017 Remi Collet <remi@remirepo.net> - 4.1.0-2
- fix autoloader for Symfony 3, FTBFS from Koschei

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu May  4 2017 Remi Collet <remi@remirepo.net> - 4.1.0-1
- Update to 4.1.0
- raise dependency on nikic/php-parser >= 2.1
- raise dependency on phpdocumentor/reflection-docblock >= 3
- allow symfony 3

* Thu Apr 13 2017 Shawn Iwinski <shawn@iwin.ski> - 4.0.2-3
- Add max versions to BuildRequires
- Prepare for Symfony 3
- Prepare for php-phpdocumentor-reflection-docblock =>
  php-phpdocumentor-reflection-docblock2 dependency rename

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Oct 31 2016 Remi Collet <remi@fedoraproject.org> - 4.0.2-2
- switch to fedora/autoloader

* Fri Sep 23 2016 Remi Collet <remi@fedoraproject.org> - 4.0.2-1
- update to 4.0.2

* Wed Aug 10 2016 Remi Collet <remi@fedoraproject.org> - 4.0.1-2
- fix test suite to work with all Monolog versions

* Wed Jul  6 2016 Remi Collet <remi@fedoraproject.org> - 4.0.1-1
- update to 4.0.1
- rewrite autoloader
- add patch for monolog https://github.com/llaville/php-reflect/pull/22

* Mon Apr 18 2016 Remi Collet <remi@fedoraproject.org> - 1.1.0-3
- allow sebastian/version 2.0
- run test suite with both PHP 5 and 7 when available

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Dec  5 2015 Remi Collet <remi@fedoraproject.org> - 4.0.0-1
- update to 4.0.0
- raise dependency on nikic/php-parser >= 1.4
- raise dependency on PHP >= 5.4

* Tue Sep 29 2015 Remi Collet <remi@fedoraproject.org> - 3.1.2-1
- update to 3.1.2

* Fri Jun 26 2015 Remi Collet <remi@fedoraproject.org> - 3.1.1-3
- rewrite autoloader

* Sun Jun 21 2015 Remi Collet <remi@fedoraproject.org> - 3.1.1-2
- fix autoloader

* Thu Jun 18 2015 Remi Collet <remi@fedoraproject.org> - 3.1.1-1
- update to 3.1.1

* Mon May 11 2015 Remi Collet <remi@fedoraproject.org> - 3.1.0-1
- update to 3.1.0
- raise dependency on nikic/php-parser >= 1.2.2
- drop dependency on phpunit/php-timer
- add dependencies on php-pdo_sqlite, doctrine/collections,
  symfony/stopwatch, symfony/dependency-injection
  and phpdocumentor/reflection-docblock, bartlett/umlwriter

* Mon Jan  5 2015 Remi Collet <remi@fedoraproject.org> - 2.6.2-1
- Update to 2.6.2
- open https://github.com/llaville/php-reflect/pull/16

* Thu Dec  4 2014 Remi Collet <remi@fedoraproject.org> - 2.6.1-1
- Update to 2.6.1

* Thu Nov 13 2014 Remi Collet <remi@fedoraproject.org> - 2.6.0-1
- Update to 2.6.0
- add dependency on justinrainbow/json-schema

* Thu Oct 16 2014 Remi Collet <remi@fedoraproject.org> - 2.5.0-1
- Update to 2.5.0
- add dependency on sebastian/version

* Fri Sep 19 2014 Remi Collet <remi@fedoraproject.org> - 2.4.0-1
- Update to 2.4.0

* Fri Aug 22 2014 Remi Collet <remi@fedoraproject.org> - 2.3.0-1
- Update to 2.3.0
- add dependency on seld/jsonlint

* Fri Jul 25 2014 Remi Collet <remi@fedoraproject.org> - 2.2.0-2
- Update to 2.2.0
- sources from github
- add manpage
- patch autoloader to not rely on composer
- drop documentation (link to online doc in description)
- obsoletes php-channel-bartlett

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Oct 12 2013 Remi Collet <remi@fedoraproject.org> - 1.9.0-1
- Update to 1.9.0
- raise dependency on PHP >= 5.3

* Mon Sep 23 2013 Remi Collet <remi@fedoraproject.org> - 1.8.1-1
- Update to 1.8.1

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jun 26 2013 Remi Collet <remi@fedoraproject.org> - 1.7.0-1
- Update to 1.7.0

* Sat Apr 06 2013 Remi Collet <remi@fedoraproject.org> - 1.6.2-1
- Update to 1.6.2

* Tue Feb 26 2013 Remi Collet <remi@fedoraproject.org> - 1.6.1-1
- Update to 1.6.1

* Fri Feb 22 2013 Remi Collet <remi@fedoraproject.org> - 1.6.0-1
- Version 1.6.0 (stable) - API 1.6.0 (stable)
- html documentation is now provided by upstream

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Dec 30 2012 Remi Collet <remi@fedoraproject.org> - 1.5.0-1
- Version 1.5.0 (stable) - API 1.5.0 (stable)
- generate documentation using asciidoc, without phing

* Tue Oct 30 2012 Remi Collet <remi@fedoraproject.org> - 1.4.3-1
- Version 1.4.3 (stable) - API 1.4.0 (stable)

* Tue Aug 14 2012 Remi Collet <remi@fedoraproject.org> - 1.4.2-2
- rebuildt for new pear_testdir

* Wed Aug 01 2012 Remi Collet <remi@fedoraproject.org> - 1.4.2-1
- Version 1.4.2 (stable) - API 1.4.0 (stable)

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Feb 17 2012 Remi Collet <remi@fedoraproject.org> - 1.3.0-2
- bump release

* Fri Feb 17 2012 Remi Collet <remi@fedoraproject.org> - 1.3.0-1
- Version 1.3.0 (stable) - API 1.3.0 (stable)

* Sun Feb 05 2012 Remi Collet <remi@fedoraproject.org> - 1.2.0-1
- Version 1.2.0 (stable) - API 1.2.0 (stable)

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Nov 11 2011 Remi Collet <Fedora@FamilleCollet.com> - 1.1.0-1
- Version 1.1.0 (stable) - API 1.1.0 (stable)

* Mon Sep 19 2011 Remi Collet <Fedora@FamilleCollet.com> - 1.0.2-2
- remove unused .js and improve installation of generated doc
- use buildroot macro

* Mon Jul 18 2011 Remi Collet <Fedora@FamilleCollet.com> - 1.0.2-1
- Version 1.0.2 (stable) - API 1.0.0 (stable)

* Thu Jun 16 2011 Remi Collet <Fedora@FamilleCollet.com> - 1.0.1-1
- Version 1.0.1 (stable) - API 1.0.0 (stable)

* Thu Jun 02 2011 Remi Collet <Fedora@FamilleCollet.com> - 1.0.0-1
- Version 1.0.0 (stable) - API 1.0.0 (stable)
- add HTML documentation

* Tue Apr 26 2011 Remi Collet <Fedora@FamilleCollet.com> - 1.0.0-0.1.RC1
- Version 1.0.0RC1 (beta) - API 1.0.0 (beta)

* Sun Apr 17 2011 Remi Collet <Fedora@FamilleCollet.com> - 0.7.0-1
- Version 0.7.0 (beta) - API 0.7.0 (beta)

* Mon Apr 11 2011 Remi Collet <Fedora@FamilleCollet.com> - 0.6.0-1
- Version 0.6.0 (beta) - API 0.6.0 (beta)

* Wed Apr 06 2011 Remi Collet <Fedora@FamilleCollet.com> - 0.5.1-1
- Version 0.5.1 (beta) - API 0.5.0 (beta)

* Fri Mar 25 2011 Remi Collet <Fedora@FamilleCollet.com> - 0.5.0-1
- Version 0.5.0 (beta) - API 0.5.0 (beta)

* Fri Feb 25 2011 Remi Collet <Fedora@FamilleCollet.com> - 0.4.0-1
- Version 0.4.0 (beta)
- Initial RPM package

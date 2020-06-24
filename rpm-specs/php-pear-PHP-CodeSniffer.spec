# spec file for php-pear-PHP-CodeSniffer
#
# Copyright (c) 2013-2020 Remi Collet
# Copyright (c) 2009-2013 Christof Damian
# Copyright (c) 2006-2009 Konstantin Ryabitsev
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please, preserve the changelog entries
#
%{!?__pear:       %global __pear       %{_bindir}/pear}
%global pear_name     PHP_CodeSniffer

Name:           php-pear-PHP-CodeSniffer
Version:        3.5.5
Release:        1%{?dist}
Summary:        PHP coding standards enforcement tool

License:        BSD
URL:            http://pear.php.net/package/PHP_CodeSniffer
Source0:        http://pear.php.net/get/%{pear_name}-%{version}.tgz

BuildArch:      noarch
BuildRequires:  php(language) >= 5.4
BuildRequires:  php-pear
# to run test suite
%global phpunit %{_bindir}/phpunit7
BuildRequires:  %{phpunit}

Requires(post): %{__pear}
Requires(postun): %{__pear}
# From package.xml
Requires:       php-pear(PEAR)
Requires:       php(language) >= 5.4
Requires:       php-tokenizer
Requires:       php-xmlwriter
Requires:       php-simplexml
# From phpcompatinfo report for version 3.0.0
Requires:       php-reflection
Requires:       php-ctype
Requires:       php-date
Requires:       php-dom
Requires:       php-json
Requires:       php-iconv
Requires:       php-pcntl
Requires:       php-pcre
Requires:       php-soap
Requires:       php-spl

Provides:       php-pear(%{pear_name}) = %{version}
Provides:       php-composer(squizlabs/php_codesniffer) = %{version}
Provides:       phpcs = %{version}
Obsoletes:      phpcs < %{version}


%description
PHP_CodeSniffer provides functionality to verify that code conforms to
certain standards, such as PEAR, or user-defined.


%prep
%setup -q -c

cd %{pear_name}-%{version}
mv ../package.xml %{pear_name}.xml


%build
# Empty build section, 


%install
cd %{pear_name}-%{version}

%{__pear} install --nodeps --packagingroot %{buildroot} %{pear_name}.xml

# Clean up unnecessary files
rm -rf %{buildroot}%{pear_metadir}/.??*

# Install XML package description
mkdir -p %{buildroot}%{pear_xmldir}
install -pm 644 %{pear_name}.xml %{buildroot}%{pear_xmldir}


%check
cd %{pear_name}-%{version}

# fix broken pear detection (may use export PHP_CODESNIFFER_PEAR=1 if PR accepted)
# https://github.com/squizlabs/PHP_CodeSniffer/pull/2847
sed -e '/PHP_CODESNIFFER_PEAR/s/false/true/' -i tests/AllTests.php

# fails with js: Couldn't read source file
rm src/Standards/Generic/Tests/Debug/JSHintUnitTest.*

# Version 3.4.0: Tests: 364, Assertions: 419, Skipped: 3.
ret=0
for cmdarg in "php %{phpunit}" php71 php72 php73 php74; do
  if which $cmdarg; then
    set $cmdarg
    $1 -d memory_limit=1G ${2:-%{_bindir}/phpunit7} \
       --verbose || ret=1
  fi
done
exit $ret


%post
%{__pear} install --nodeps --soft --force --register-only \
    %{pear_xmldir}/%{pear_name}.xml >/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    %{__pear} uninstall --nodeps --ignore-errors --register-only \
        %{pear_name} >/dev/null || :
fi


%files
%doc %{pear_docdir}/%{pear_name}
%{pear_xmldir}/%{pear_name}.xml
%{pear_testdir}/%{pear_name}
%{pear_datadir}/%{pear_name}
%{pear_phpdir}/PHP
%{_bindir}/phpcbf
%{_bindir}/phpcs


%changelog
* Mon Apr 20 2020 Remi Collet <remi@remirepo.net> - 3.5.5-1
- update to 3.5.5

* Fri Jan 31 2020 Remi Collet <remi@remirepo.net> - 3.5.4-1
- update to 3.5.4
- fix test suite from
  https://github.com/squizlabs/PHP_CodeSniffer/pull/2847

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec  4 2019 Remi Collet <remi@remirepo.net> - 3.5.3-1
- update to 3.5.3

* Mon Oct 28 2019 Remi Collet <remi@remirepo.net> - 3.5.2-1
- update to 3.5.2

* Thu Oct 17 2019 Remi Collet <remi@remirepo.net> - 3.5.1-1
- update to 3.5.1

* Fri Sep 27 2019 Remi Collet <remi@remirepo.net> - 3.5.0-1
- update to 3.5.0

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Apr 11 2019 Remi Collet <remi@remirepo.net> - 3.4.2-1
- update to 3.4.2

* Tue Mar 19 2019 Remi Collet <remi@remirepo.net> - 3.4.1-1
- update to 3.4.1

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec 20 2018 Remi Collet <remi@remirepo.net> - 3.4.0-1
- update to 3.4.0

* Mon Sep 24 2018 Remi Collet <remi@remirepo.net> - 3.3.2-1
- update to 3.3.2

* Fri Jul 27 2018 Remi Collet <remi@remirepo.net> - 3.3.1-1
- update to 3.3.1

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun  7 2018 Remi Collet <remi@remirepo.net> - 3.3.0-1
- update to 3.3.0

* Wed Feb 21 2018 Remi Collet <remi@remirepo.net> - 3.2.3-1
- Update to 3.2.3
- use phpunit7 on F28+

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Dec 20 2017 Remi Collet <remi@remirepo.net> - 3.2.2-1
- Update to 3.2.2

* Mon Dec 18 2017 Remi Collet <remi@remirepo.net> - 3.2.1-1
- Update to 3.2.1

* Wed Dec 13 2017 Remi Collet <remi@remirepo.net> - 3.2.0-1
- Update to 3.2.0

* Tue Oct 17 2017 Remi Collet <remi@remirepo.net> - 3.1.1-1
- Update to 3.1.1

* Wed Sep 20 2017 Remi Collet <remi@remirepo.net> - 3.1.0-1
- Update to 3.1.0
- use phpunit6 on F26+

* Tue Jul 18 2017 Remi Collet <remi@remirepo.net> - 3.0.2-1
- Update to 3.0.2

* Wed Jun 14 2017 Remi Collet <remi@remirepo.net> - 3.0.1-1
- Update to 3.0.1

* Thu May  4 2017 Remi Collet <remi@remirepo.net> - 3.0.0-1
- Update to 3.0.0
- raise dependency on PHP >= 5.4
- drop phpcs-svn-pre-commit command

* Thu Mar 02 2017 Remi Collet <remi@remirepo.net> - 2.8.1-1
- Update to 2.8.1

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 02 2017 Remi Collet <remi@fedoraproject.org> - 2.8.0-1
- Update to 2.8.0

* Wed Nov 30 2016 Remi Collet <remi@fedoraproject.org> - 2.7.1-1
- Update to 2.7.1

* Fri Sep 02 2016 Remi Collet <remi@fedoraproject.org> - 2.7.0-1
- Update to 2.7.0

* Mon Jul 18 2016 Remi Collet <remi@fedoraproject.org> - 2.6.2-1
- Update to 2.6.2

* Tue May 31 2016 Remi Collet <remi@fedoraproject.org> - 2.6.1-1
- Update to 2.6.1

* Mon Apr 04 2016 Remi Collet <remi@fedoraproject.org> - 2.6.0-1
- Update to 2.6.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 20 2016 Remi Collet <remi@fedoraproject.org> - 2.5.1-1
- Update to 2.5.1 (stable)

* Fri Dec 11 2015 Remi Collet <remi@fedoraproject.org> - 2.5.0-1
- Update to 2.5.0 (stable)

* Wed Nov 25 2015 Remi Collet <remi@fedoraproject.org> - 2.4.0-1
- Update to 2.4.0 (stable)

* Wed Sep  9 2015 Remi Collet <remi@fedoraproject.org> - 2.3.4-1
- Update to 2.3.4

* Wed Jun 24 2015 Remi Collet <remi@fedoraproject.org> - 2.3.3-1
- Update to 2.3.3 (stable)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr 29 2015 Remi Collet <remi@fedoraproject.org> - 2.3.2-1
- Update to 2.3.2

* Thu Apr 23 2015 Remi Collet <remi@fedoraproject.org> - 2.3.1-1
- Update to 2.3.1 (stable)

* Wed Mar 04 2015 Remi Collet <remi@fedoraproject.org> - 2.3.0-1
- Update to 2.3.0 (stable)

* Thu Jan 22 2015 Remi Collet <remi@fedoraproject.org> - 2.2.0-1
- Update to 2.2.0 (stable)

* Thu Dec 18 2014 Remi Collet <remi@fedoraproject.org> - 2.1.0-1
- Update to 2.1.0 (stable)

* Fri Dec 05 2014 Remi Collet <remi@fedoraproject.org> - 2.0.0-1
- Update to 2.0.0
- add phpcbf and phpcs-svn-pre-commit commands

* Thu Oct  9 2014 Remi Collet <remi@fedoraproject.org> - 1.5.5
- Update to 1.5.5
- cleanup + changes from remi repo
- add explicit dependencies on need extensions
- run test suite during build
- provide php-composer(squizlabs/php_codesniffer)
- request LICENSE to be part of upstream tarball
  https://github.com/squizlabs/PHP_CodeSniffer/issues/273
- add spec License header

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Apr 19 2013 Christof Damian <christof@damian.net> - 1.4.5-1
- upstream 1.4.5

* Mon Feb 25 2013 Christof Damian <christof@damian.net> - 1.4.4-1
- upstream 1.4.4

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jan 12 2013 Christof Damian <christof@damian.net> - 1.4.3-1
- upstream 1.4.3
- use php_metadir

* Fri Oct 12 2012 Christof Damian <christof@damian.net> - 1.4.0-1
- upstream 1.4.0

* Sat Sep  8 2012 Christof Damian <christof@damian.net> - 1.3.6-1
- upstream 1.3.6

* Sun Aug 19 2012 Remi Collet <remi@fedoraproject.org> - 1.3.5-4
- rebuilt for new pear_datadir

* Tue Aug 14 2012 Remi Collet <remi@fedoraproject.org> - 1.3.5-3
- rebuilt for new pear_testdir

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jul 13 2012 Christof Damian <christof@damian.net> - 1.3.5-1
- upstream 1.3.5

* Sat May 19 2012 Christof Damian <christof@damian.net> - 1.3.4-1
- upstream 1.3.4

* Fri Mar  2 2012 Christof Damian <christof@damian.net> - 1.3.3-1
- upstream 1.3.3

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Nov  3 2011 Christof Damian <christof@damian.net> - 1.3.1-1
- upstream 1.3.1

* Fri Mar 18 2011 Christof Damian <christof@damian.net> - 1.3.0final-1
- fix my version foo until 1.3.1

* Fri Mar 18 2011 Christof Damian <christof@damian.net> - 1.3.0-1
- upstream 1.3.0 final

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-3.RC1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Dec  4 2010 Christof Damian <christof@damian.net> - 1.3.0-2.RC1
- fix version number 
- fix timezone warnings

* Fri Sep  3 2010 Christof Damian <christof@damian.net> - 1.3.0RC1-1
- upstream 1.3.0RC1

* Thu Jul 15 2010 Christof Damian <christof@damian.net> - 1.3.0a1-1
- upstream 1.3.0a1

* Wed Jan 27 2010 Christof Damian <christof@damian.net> 1.2.2-1
- upstream 1.2.2 ( bug:559170 )
- move phpcs into main package ( bug: 517775 )
- add php-common version requirement

* Tue Nov 17 2009 Christof Damian <christof@damian.net> - 1.2.1-1
- Upstream 1.2.1

* Sat Sep 19 2009 Christof Damian <christof@damian.net> - 1.2.0-1
- Upstream 1.2.0

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Mar 05 2009 Konstantin Ryabitsev <icon@fedoraproject.org> - 1.1.0-1
- Belatedly update to 1.1.0 final.

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-0.2.RC2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Jun 30 2008 Konstantin Ryabitsev <icon@fedoraproject.org> - 1.1.0-0.1.RC2
- Upstream 1.1.0RC2

* Sun Feb 17 2008 Konstantin Ryabitsev <icon@fedoraproject.org> - 1.0.1-1
- Upstream 1.0.1
- Move sample config into docs

* Fri Aug 17 2007 Konstantin Ryabitsev <icon@fedoraproject.org> - 0.8.0-1
- Upstream 0.8.0

* Mon Jun 11 2007 Konstantin Ryabitsev <icon@fedoraproject.org> - 0.7.0-1
- Upstream 0.7.0
- Drop Requirement on php-common (php-pear pulls that in)

* Mon Jun 11 2007 Konstantin Ryabitsev <icon@fedoraproject.org> - 0.6.0-1
- Upstream 0.6.0
- Fix owner on phpcs

* Tue Apr 17 2007 Konstantin Ryabitsev <icon@fedoraproject.org> - 0.5.0-1
- Upstream 0.5.0

* Tue Feb 20 2007 Konstantin Ryabitsev <icon@fedoraproject.org> - 0.4.0-1
- Upstream 0.4.0

* Mon Jan 29 2007 Konstantin Ryabitsev <icon@fedoraproject.org> - 0.3.0-1
- Rename to php-pear-PHP-CodeSniffer
- Own all dirs we create
- Require php-common > 5.1.0

* Mon Jan 29 2007 Konstantin Ryabitsev <icon@fedoraproject.org> - 0.3.0-1
- Split phpcs into a separate package (so we don't require php-cli)

* Fri Jan 12 2007 Konstantin Ryabitsev <icon@fedoraproject.org> - 0.3.0-0.1
- Upstream 0.3.0

* Mon Oct 23 2006 Konstantin Ryabitsev <icon@fedoraproject.org> - 0.2.0-0.1
- Upstream 0.2.0

* Mon Sep 25 2006 Konstantin Ryabitsev <icon@fedoraproject.org> - 0.1.1-0.1
- Upstream update.

* Fri Sep 22 2006 Konstantin Ryabitsev <icon@fedoraproject.org> - 0.1.0-0.1
- Initial packaging.

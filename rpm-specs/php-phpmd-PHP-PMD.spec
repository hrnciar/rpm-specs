#
# Fedora spec file for php-phpmd-PHP-PMD
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please, preserve the changelog entries
#
%global gh_commit    ce10831d4ddc2686c1348a98069771dd314534a8
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     phpmd
%global gh_project   phpmd
%{!?__pear: %{expand: %%global __pear %{_bindir}/pear}}
%global pear_name    PHP_PMD
%global pear_channel pear.phpmd.org
%global php_home     %{_datadir}/php/PHPMD
%global with_tests   0%{!?_without_tests:1}

Name:           php-phpmd-PHP-PMD
Version:        2.9.1
Release:        1%{?dist}
Summary:        PHPMD - PHP Mess Detector

License:        BSD
URL:            http://phpmd.org/
# git snashop to get upstream test suite
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh
# Autoloader
Source2:        %{name}-autoload.php
Patch0:         %{name}-rpm.patch

BuildArch:      noarch
%if %{with_tests}
# For tests
# From composer.json, "require-dev": {
#    "phpunit/phpunit": "^4.8.36 || ^5.7.27",
#    "squizlabs/php_codesniffer": "^2.0",
#    "mikey179/vfsstream": "^1.6.4",
#    "gregwar/rst": "^1.0",
#    "ext-simplexml": "*",
#    "ext-json": "*",
#    "easy-doc/easy-doc": "0.0.0 || ^1.3.2"
BuildRequires:  php-composer(phpunit/phpunit) >= 4.8.36
BuildRequires:  php(language) >= 5.3.9
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
BuildRequires: (php-composer(pdepend/pdepend)         >= 2.7.1  with php-composer(pdepend/pdepend)         < 3)
BuildRequires: (php-composer(composer/xdebug-handler) >= 1.0    with php-composer(composer/xdebug-handler) < 2)
BuildRequires: (php-composer(mikey179/vfsstream)      >= 1.6.4  with php-composer(mikey179/vfsstream)      < 2)
%else
BuildRequires:  php-composer(pdepend/pdepend)         <  3
BuildRequires:  php-composer(pdepend/pdepend)         >= 2.5
BuildRequires:  php-composer(composer/xdebug-handler) <  2
BuildRequires:  php-composer(composer/xdebug-handler) >= 1.0
BuildRequires:  php-composer(mikey179/vfsstream)      <  2
BuildRequires:  php-composer(mikey179/vfsstream)      >= 1.6.4
%endif
BuildRequires:  php-reflection
BuildRequires:  php-date
BuildRequires:  php-json
BuildRequires:  php-libxml
BuildRequires:  php-pcre
BuildRequires:  php-simplexml
BuildRequires:  php-spl
# Autoloader
BuildRequires:  php-composer(fedora/autoloader)
%endif

# From composer.json,     "require": {
#    "php": ">=5.3.9",
#    "pdepend/pdepend": "^2.7.1",
#    "ext-xml": "*",
#    "composer/xdebug-handler": "^1.0"
Requires:       php(language) >= 5.3.9
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
Requires:      (php-composer(pdepend/pdepend)         >= 2.7.1 with php-composer(pdepend/pdepend)         < 3)
Requires:      (php-composer(composer/xdebug-handler) >= 1.0   with php-composer(composer/xdebug-handler) < 2)
%else
Requires:       php-composer(pdepend/pdepend)         <  3
Requires:       php-composer(pdepend/pdepend)         >= 2.6
Requires:       php-composer(composer/xdebug-handler) <  2
Requires:       php-composer(composer/xdebug-handler) >= 1.0
%endif
Requires:       php-xml
# From phpcompatinfo report for version 2.9.0
Requires:       php-reflection
Requires:       php-date
Requires:       php-json
Requires:       php-libxml
Requires:       php-pcre
Requires:       php-simplexml
Requires:       php-spl
# Autoloader
Requires:       php-composer(fedora/autoloader)

# Single package in this channel
Obsoletes:      php-channel-phpmd <= 1.3

Provides:       php-pear(%{pear_channel}/%{pear_name}) = %{version}
Provides:       php-composer(%{gh_owner}/%{gh_project}) = %{version}


%description
This is the project site of PHPMD. It is a spin-off project of PHP Depend 
and aims to be a PHP equivalent of the well known Java tool PMD. PHPMD can 
be seen as an user friendly front-end application for the raw metrics 
stream measured by PHP Depend.


%prep
%setup -q -n %{gh_project}-%{gh_commit}

%patch0 -p0 -b .rpm
find . -name \*.rpm -delete

cp %{SOURCE2} src/main/php/PHPMD/autoload.php

find src/main/php -name \*php -exec sed -e 's:@package_version@:%{version}:' -i {} \;
find src/test     -type f     -exec sed -e 's:@package_version@:%{version}:' -i {} \;
sed -e '/project.version/s/2.8.1/%{version}/' -i build.properties


%build
# Empty build section, most likely nothing required.


%install
: Library
mkdir -p $(dirname %{buildroot}%{php_home})
cp -pr src/main/php/PHPMD %{buildroot}%{php_home}

: Resources
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -pr src/main/resources %{buildroot}%{_datadir}/%{name}/resources

: Command
install -Dpm 0755 src/bin/phpmd %{buildroot}%{_bindir}/phpmd


%check
%if %{with_tests}
cat << 'EOF' | tee src/test/php/bootstrap.php
<?php
require '%{buildroot}%{php_home}/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('PHPMD\\',  __DIR__ . '/PHPMD');
\Fedora\Autoloader\Dependencies::required([
    '%{_datadir}/php/org/bovigo/vfs/autoload.php',
]);

EOF

ret=0
for cmd in php php71 php72 php73 php74; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit --columns max --verbose || ret=1
  fi
done
exit $ret
%else
: Test suite disabled
%endif


%pre
if [ -x %{_bindir}/pear ]; then
   %{_bindir}/pear uninstall --nodeps --ignore-errors --register-only \
      %{pear_channel}/%{pear_name} >/dev/null || :
fi


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc composer.json
%doc CONTRIBUTING.md README.rst AUTHORS.rst
%doc CHANGELOG
%{php_home}
%{_datadir}/%{name}
%{_bindir}/phpmd


%changelog
* Thu Sep 24 2020 Remi Collet <remi@remirepo.net> - 2.9.1-1
- update to 2.9.1

* Wed Sep  2 2020 Remi Collet <remi@remirepo.net> - 2.9.0-1
- update to 2.9.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Feb 25 2020 Remi Collet <remi@remirepo.net> - 2.8.2-1
- update to 2.8.2
- raise dependency on pdepend/pdepend version 2.7.1

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan  7 2020 Remi Collet <remi@remirepo.net> - 2.8.1-1
- update to 2.8.1
- raise dependency on pdepend/pdepend version 2.6
- add dependency on composer/xdebug-handler

* Fri Aug  2 2019 Remi Collet <remi@remirepo.net> - 2.7.0-1
- update to 2.7.0

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 15 2019 Remi Collet <remi@remirepo.net> - 2.6.1-1
- update to 2.6.1
- use range dependencies

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 20 2017 Remi Collet <remi@fedoraproject.org> - 2.6.0-1
- update to 2.6.0
- raise dependency on pdepend/pdepend version 2.5

* Thu Nov 24 2016 Remi Collet <remi@fedoraproject.org> - 2.5.0-1
- update to 2.5.0

* Tue Nov 22 2016 Remi Collet <remi@fedoraproject.org> - 2.4.4-1
- update to 2.4.4
- raise dependency on PHP 5.3.9
- switch to fedora/autoloader

* Thu Apr 21 2016 Remi Collet <remi@fedoraproject.org> - 2.4.3-1
- update to 2.4.3

* Fri Mar 11 2016 Remi Collet <remi@fedoraproject.org> - 2.4.2-1
- update to 2.4.2

* Wed Mar  9 2016 Remi Collet <remi@fedoraproject.org> - 2.4.1-1
- update to 2.4.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Sep 25 2015 Remi Collet <remi@fedoraproject.org> - 2.3.2-1
- update to 2.3.2

* Tue Sep 22 2015 Remi Collet <remi@fedoraproject.org> - 2.3.1-1
- update to 2.3.1

* Tue Sep 22 2015 Remi Collet <remi@fedoraproject.org> - 2.3.0-1
- update to 2.3.0

* Mon Jul 13 2015 Remi Collet <remi@fedoraproject.org> - 2.2.3-1
- update to 2.2.3
- switch from pear channel to git snapshot sources
- run upstream test suite during build

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Aug 23 2013 Guillaume Kulakowski <guillaume.kulakowski@fedoraproject.org> - 1.5.0-2
- Fix "Broken dependencies: php-phpmd-PHP-PMD": requires php-language

* Mon Aug 05 2013 Christof Damian <christof@damian.net> - 1.5.0-1
- upstream 1.5.0
- explicit requires

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jan 12 2013 Christof Damian <christof@damian.net> - 1.4.1-1
- upstream 1.4.1
- add metadir support

* Sat Sep  8 2012 Christof Damian <christof@damian.net> - 1.4.0-1
- upstream 1.4.0

* Sun Aug 19 2012 Remi Collet <remi@fedoraproject.org> - 1.3.3-3
- rebuilt for new pear_datadir

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Mar  2 2012 Christof Damian <christof@damian.net> - 1.3.3-1
- upstream 1.3.3

* Thu Feb  9 2012 Christof Damian <christof@damian.net> - 1.3.0-1
- upstream 1.3.0

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Oct 28 2011 Christof Damian <christof@damian.net> - 1.2.0-1
- upstream 1.2.0

* Fri Jul 15 2011 Christof Damian <christof@damian.net> - 1.1.1-1
- upstream 1.1.1

* Thu Mar 24 2011 Christof Damian <christof@damian.net> - 1.1.0-1
- upstream 1.1.0

* Tue Feb 15 2011 Christof Damian <christof@damian.net> - 1.0.1-1
- upstream 1.0.1 - bugfixes

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Feb  6 2011 Christof Damian <christof@damian.net> - 1.0.0-1
- upstream stable release 1.0.0

* Sat Oct  2 2010 Christof Damian <christof@damian.net> - 0.2.7-1
- new upstream

* Sun Jul  4 2010 Christof Damian <christof@damian.net> - 0.2.6-1
- upstream 0.2.6

* Sun Apr  4 2010 Christof Damian <christof@damian.net> - 0.2.5-1
- upsteam 0.2.5: bugfixes

* Tue Mar  9 2010 Christof Damian <christof@damian.net> - 0.2.4-1
- upstream 0.2.4 : Small bugfix release which closes an E_NOTICE issue introduced with release 0.2.3

* Thu Mar  4 2010 Christof Damian <christof@damian.net> - 0.2.3-1
- upstream 0.2.3
- increased php and pdepend requirements 

* Sun Jan 31 2010 Christof Damian <christof@damian.net> - 0.2.2-2
- use pear_datadir in filesection

* Sat Jan 30 2010 Christof Damian <christof@damian.net> 0.2.2-1
- upstream 0.2.2
- changed define to global
- moved docs to /usr/share/doc
- use channel macro in postun

* Tue Jan 12 2010 Christof Damian <christof@damian.net> - 0.2.1-1
- upstream 0.2.1

* Fri Jan 1 2010 Christof Damian <christof@damian.net> 0.2.0-1
- initial release


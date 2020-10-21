# remirepo/fedora spec file for php-bartlett-umlwriter
#
# Copyright (c) 2015-2018 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

# For compatibility with SCL
%undefine __brp_mangle_shebangs

%global bootstrap    0
%global gh_commit    9f2b0800a4f541ad74e723e1f2f134dcddb8ddf5
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
#global gh_date      20150331
%global gh_owner     llaville
%global gh_project   umlwriter
#global prever       RC2
%if %{bootstrap}
%global with_tests   %{?_with_tests:1}%{!?_with_tests:0}
%else
%global with_tests   %{?_without_tests:0}%{!?_without_tests:1}
%endif

Name:           php-bartlett-umlwriter
Version:        1.3.1
%global specrel 1
Release:        %{?gh_date:1%{specrel}.%{?prever}%{!?prever:%{gh_date}git%{gh_short}}}%{!?gh_date:%{specrel}}%{?dist}.2
Summary:        Create UML class diagrams from your PHP source

License:        BSD
URL:            http://php5.laurent-laville.org/umlwriter/
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{gh_project}-%{version}%{?prever}-%{gh_short}.tar.gz

# Autoloader for RPM - die composer !
Source1:        %{name}-autoload.php

# Use out autoloader
Patch0:         %{name}-rpm.patch

BuildArch:      noarch
BuildRequires:  php(language) >= 5.4.0
%if %{with_tests}
BuildRequires:  %{_bindir}/phpunit
BuildRequires:  (php-composer(symfony/console)                   >= 2.5  with php-composer(symfony/console)                   < 5)
BuildRequires:  (php-composer(sebastian/version)                 >= 1.0  with php-composer(sebastian/version)                 < 3)
BuildRequires:  (php-composer(bartlett/php-reflect)              >= 4.3  with php-composer(bartlett/php-reflect)              < 5)
BuildRequires:  (php-composer(andrewsville/php-token-reflection) >= 1.4  with php-composer(andrewsville/php-token-reflection) < 2)
# For our patch / autoloader
BuildRequires:   php-composer(fedora/autoloader)
%endif

# From composer.json
#    "require": {
#        "php": "^5.4|^7.0"
#        "symfony/console": "^2.5|^3.0|^4.0",
#        "sebastian/version": "^1.0|^2.0"
Requires:       php(language) >= 5.4.0
Requires:       php-cli
Requires:       php-spl
Requires:       (php-composer(symfony/console)                   >= 2.5  with php-composer(symfony/console)                   < 5)
Requires:       (php-composer(sebastian/version)                 >= 1.0  with php-composer(sebastian/version)                 < 3)
#    "require-dev": {
#        "bartlett/php-reflect": "^4.3",
#        "andrewsville/php-token-reflection": "^1.4"
#    "suggest": {
#        "bartlett/php-reflect": "Reverse-engine, default solution",
#        "andrewsville/php-token-reflection": "Reverse-engine, alternative solution"
%if ! %{bootstrap}
Requires:      (php-composer(bartlett/php-reflect)              >= 4.3  with php-composer(bartlett/php-reflect)              < 5)
Requires:      (php-composer(andrewsville/php-token-reflection) >= 1.4  with php-composer(andrewsville/php-token-reflection) < 2)
%endif
# For our patch / autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(bartlett/umlwriter) = %{version}


%description
This tool wil generate UML class diagrams with all class,
interface and trait definitions in your PHP project.

* reverse-engine interchangeable (currently support Bartlett\Reflect
  and Andrewsville\TokenReflection)
* UML syntax processor interchangeable (currently support Graphviz
  and PlantUML)
* generates a class and its direct dependencies
* generates a namespace with all objects
* generates a full package with all namespaces and objects


%prep
%setup -q -n %{gh_project}-%{gh_commit}

%patch0 -p1 -b .rpm
cp %{SOURCE1} src/Bartlett/UmlWriter/autoload.php

sed -e 's/@package_version@/%{version}%{?prever}/' \
    -i $(find src -name \*.php) bin/umlwriter


%build
# Nothing


%install
mkdir -p %{buildroot}%{_datadir}/php
cp -pr src/Bartlett %{buildroot}%{_datadir}/php/Bartlett

install -Dpm 755 bin/umlwriter   %{buildroot}%{_bindir}/umlwriter
install -Dpm 644 bin/umlwriter.1 %{buildroot}%{_mandir}/man1/umlwriter.1


%check
%if %{with_tests}
ret=0
for cmd in php php72 php73 php74; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit --bootstrap %{buildroot}%{_datadir}/php/Bartlett/UmlWriter/autoload.php || ret=1
  fi
done
exit $ret
%else
: Test suite disabled
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc composer.json README.* examples
%{_bindir}/umlwriter
%{_mandir}/man1/umlwriter.1*
%dir %{_datadir}/php/Bartlett
     %{_datadir}/php/Bartlett/UmlWriter


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 25 2019 Remi Collet <remi@remirepo.net> - 1.3.1-1
- update to 1.3.1 (no change)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Nov 27 2018 Remi Collet <remi@remirepo.net> - 1.3.0-1
- update to 1.3.0
- raise dependency on bartlett/php-reflect 4.3
- allow Symfony 4

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Mar 20 2018 Remi Collet <remi@remirepo.net> - 1.2.1-1
- update to 1.2.1 (no change)
- use range dependencies
- allow Symfony 3
- raise dependency on bartlett/php-reflect 4.0

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Mar 09 2017 Remi Collet <remi@fedoraproject.org> - 1.2.0-2
- rebuild

* Wed Mar  1 2017 Remi Collet <remi@remirepo.net> - 1.2.0-1
- update to 1.2.0 (no change)
- add the command man page

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Oct 31 2016 Remi Collet <remi@fedoraproject.org> - 1.1.0-4
- switch to fedora/autoloader

* Mon Apr 18 2016 Remi Collet <remi@fedoraproject.org> - 1.1.0-3
- allow sebastian/version 2.0
- run test suite with both PHP 5 and 7 when available

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Dec 10 2015 Remi Collet <remi@fedoraproject.org> - 1.1.0-1
- update to 1.1.0
- raise dependency on php >= 5.4.0
- allow php-reflect 4

* Tue Sep 29 2015 Remi Collet <remi@fedoraproject.org> - 1.0.1-1
- update to 1.0.1

* Sun Jun 28 2015 Remi Collet <remi@fedoraproject.org> - 1.0.0-6
- fix autoloader

* Fri Jun 26 2015 Remi Collet <remi@fedoraproject.org> - 1.0.0-5
- rewrite autoloader

* Mon Jun 22 2015 Remi Collet <remi@fedoraproject.org> - 1.0.0-4
- fix Autoload

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 22 2015 Remi Collet <remi@fedoraproject.org> - 1.0.0-2
- standard build (no bootstrap)

* Fri Apr  3 2015 Remi Collet <remi@fedoraproject.org> - 1.0.0-1
- update to 1.0.0

* Tue Mar 31 2015 Remi Collet <remi@fedoraproject.org> - 1.0.0-0.3.20150331gitdd58a0b
- git snapshot, post 1.0.0RC2
- cleanup EL-5 stuff

* Tue Mar 31 2015 Remi Collet <remi@fedoraproject.org> - 1.0.0-0.2.RC2
- update to 1.0.0RC2
- add umlwrite command
- add dependencies on symfony/console, symfony/class-loader,
  bartlett/php-reflect, sebastian/version
  and andrewsville/php-token-reflection
- run test suite during build, but ignore results for now
- open https://github.com/llaville/umlwriter/issues/1 test suite issue
- open https://github.com/llaville/umlwriter/issues/2 runtime issue

* Tue Mar 24 2015 Remi Collet <remi@fedoraproject.org> - 1.0.0-0.1.RC1
- Initial RPM package, version 1.0.0RC1

# spec file for php-pear-Console-Getargs
#
# Copyright (c) 2006-2018 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/3.0/
#
# Please, preserve the changelog entries
#
%{!?pear_metadir: %global pear_metadir %{pear_phpdir}}
%{!?__pear:       %global __pear       %{_bindir}/pear}
%global pear_name Console_Getargs

Name:           php-pear-Console-Getargs
Version:        1.4.0
Release:        6%{?dist}
Summary:        Command-line arguments and parameters parser
Summary(fr):    Analyseur des arguments et paramètres en ligne de commande

License:        PHP
URL:            http://pear.php.net/package/Console_Getargs
Source0:        http://pear.php.net/get/%{pear_name}-%{version}.tgz

BuildArch:      noarch
BuildRequires:  php-pear
# For test suite
BuildRequires:  php-phpunit-PHPUnit

Requires:       php-pear(PEAR)
Requires(post): %{__pear}
Requires(postun): %{__pear}

Provides:       php-pear(%{pear_name}) = %{version}
Provides:       php-composer(pear/console_getargs) = %{version}


%description
The Console_Getargs package implements a Command Line arguments and
parameters parser for your CLI applications. It performs some basic
arguments validation and automatically creates a formatted help text,
based on the given configuration.
 
%description -l fr
L'extension Console_Getargs fournit un analyseur des arguments et des
paramètres passés à vos applications sur la ligne de commande. 
Il réalise quelques validations simples des arguments et crée 
automatiquement un texte d'aide à partir de la configuration fournie.


%prep
%setup -c -q
cd %{pear_name}-%{version}
# package.xml is V2
sed -e '/README/s/role="data"/role="doc"/' ../package.xml >%{name}.xml


%build
cd %{pear_name}-%{version}
# Empty build section, most likely nothing required.


%install
cd %{pear_name}-%{version}
%{__pear} install --nodeps --packagingroot $RPM_BUILD_ROOT %{name}.xml

# Clean up unnecessary files
rm -rf $RPM_BUILD_ROOT%{pear_metadir}/.??*

# Install XML package description
mkdir -p $RPM_BUILD_ROOT%{pear_xmldir}
install -pm 644 %{name}.xml $RPM_BUILD_ROOT%{pear_xmldir}


%check
cd %{pear_name}-%{version}
%{_bindir}/phpunit \
   --include-path=$RPM_BUILD_ROOT%{pear_phpdir} \
   --verbose tests


%post
%{__pear} install --nodeps --soft --force --register-only \
    %{pear_xmldir}/%{name}.xml >/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    %{__pear} uninstall --nodeps --ignore-errors --register-only \
        %{pear_name} >/dev/null || :
fi


%files
%doc %{pear_docdir}/%{pear_name}
%doc %{pear_testdir}/%{pear_name}
%{pear_xmldir}/%{name}.xml
%{pear_phpdir}/Console/Getargs.php


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Feb 13 2018 Remi Collet <remi@remirepo.net> - 1.4.0-1
- update to 1.4.0
- add provides php-composer(pear/console_getargs)
- drop generated changelog
- install tests as documentation

* Tue Feb 13 2018 Remi Collet <remi@remirepo.net> - 1.3.5-16
- add patch for PHP 7.2 from
  https://github.com/pear/Console_Getargs/pull/3

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Remi Collet <remi@fedoraproject.org> - 1.3.5-11
- fix FTBFS, include path for tests
- error_reporting = E_ALL - E_STRICT - E_DEPRECATED for tests

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Feb 19 2013 Remi Collet <remi@fedoraproject.org> - 1.3.5-9
- fix metadata location

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Aug 14 2012 Remi Collet <remi@fedoraproject.org> - 1.3.5-7
- rebuilt for new pear_testdir

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jan 16 2012 Remi Collet <remi@fedoraproject.org> - 1.3.5-5
- fix from GIT for test suite

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Apr 06 2011 Remi Collet <Fedora@FamilleCollet.com> 1.3.5-3
- doc in /usr/share/doc/pear

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Oct 11 2010 Remi Collet <Fedora@FamilleCollet.com> 1.3.5-1
- upstream Version 1.3.5 (stable) - API 1.3.5 (stable)
- set timezone during build
- run phpunit test suite in %%check

* Sat Apr 17 2010 Remi Collet <Fedora@FamilleCollet.com> 1.3.4-4
- remove php (and httpd) dependency
- rename Console_Getargs.xml to php-pear-Console-Getargs.xml

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-3.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Aug 21 2007 Remi Collet <Fedora@FamilleCollet.com> 1.3.4-1.fc8.1
- bump release (missing sources)

* Tue Aug 21 2007 Remi Collet <Fedora@FamilleCollet.com> 1.3.4-1
- update to 1.3.4
- fix license and Remove file

* Sat Oct  7 2006 Remi Collet <Fedora@FamilleCollet.com> 1.3.3-1
- update to 1.3.3

* Wed Oct  4 2006 Remi Collet <Fedora@FamilleCollet.com> 1.3.2-1
- update to 1.3.2

* Thu Sep 28 2006 Remi Collet <Fedora@FamilleCollet.com> 1.3.1-1
- generated specfile (pear make-rpm-spec) + cleaning
- generated CHANGELOG
- add LICENSE, french summary and description

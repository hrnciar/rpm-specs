# spec file for php-pear-Numbers-Words
#
# Copyright (c) 2010-2019 Remi Collet
# Copyright (c) 2006-2009 Christopher Stone
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please, preserve the changelog entries
#
%{!?__pear:       %global __pear       %{_bindir}/pear}
%global pear_name Numbers_Words

Name:           php-pear-Numbers-Words
Version:        0.18.2
Release:        6%{?dist}
Summary:        Methods for spelling numerals in words

License:        PHP
URL:            http://pear.php.net/package/Numbers_Words
Source0:        http://pear.php.net/get/%{pear_name}-%{version}.tgz

BuildArch:      noarch
BuildRequires:  php-pear
# For test suite
BuildRequires:  php-phpunit-PHPUnit
%if 0%{?fedora} >= 26 || 0%{?rhel} >= 8
BuildRequires:  php-pear(Math_BigInteger)
%else
BuildRequires:  php-pear(phpseclib.sourceforge.net/Math_BigInteger)
%endif

Requires(post): %{__pear}
Requires(postun): %{__pear}
# From package.xml
Requires:       php(language) >= 5.3.2
Requires:       php-pear(PEAR)
%if 0%{?fedora} >= 26 || 0%{?rhel} >= 8
Requires:       php-pear(Math_BigInteger)
%else
# Instead of php-pear(Math_BigInteger), same API
Requires:       php-pear(phpseclib.sourceforge.net/Math_BigInteger)
%endif
# From phpcompatinfo report for version 0.18.0
Requires:       php-pcre

Provides:       php-pear(%{pear_name}) = %{version}
Provides:       php-composer(pear/numbers_words) = %{version}


%description
With Numbers_Words class you can convert numbers written in Arabic digits to
words in several languages.  You can convert an integer between -infinity and
infinity.  If your system does not support such long numbers you can call
Numbers_Words::toWords() with just a string.


%prep
%setup -qc

cd %{pear_name}-%{version}
mv ../package.xml %{name}.xml


%build
cd %{pear_name}-%{version}
# Empty build section, most likely nothing required.


%install
cd %{pear_name}-%{version}
%{__pear} install --nodeps --packagingroot %{buildroot} %{name}.xml

# Clean up unnecessary files
rm -rf %{buildroot}%{pear_metadir}/.??*

# Install XML package description
install -d %{buildroot}%{pear_xmldir}
install -pm 644 %{name}.xml %{buildroot}%{pear_xmldir}


%check
cd %{pear_name}-%{version}/tests
phpunit .


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
%{pear_xmldir}/%{name}.xml
%{pear_testdir}/%{pear_name}
%{pear_phpdir}/Numbers


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan  4 2019 Remi Collet <remi@remirepo.net> - 0.18.2-3
- cleanup for EL-8

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Feb 13 2018 Remi Collet <remi@remirepo.net> - 0.18.2-1
- update to 0.18.2

* Tue Feb 13 2018 Remi Collet <remi@remirepo.net> - 0.18.1-7
- add patch for PHP 7.2 from
  https://github.com/pear/Numbers_Words/pull/32

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec  5 2016 Remi Collet <remi@fedoraproject.org> - 0.18.1-4
- switch to php-pear(Math_BigInteger) in F26+

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Nov  3 2014 Remi Collet <remi@fedoraproject.org> - 0.18.1-1
- update to 0.18.1

* Sat Nov  1 2014 Remi Collet <remi@fedoraproject.org> - 0.18.0-1
- update to 0.18.0
- add provide php-composer(pear/numbers_words)
- add dependency on php-pear(phpseclib.sourceforge.net/Math_BigInteger)
- open https://pear.php.net/bugs/20435 missing files

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Feb 19 2013 Remi Collet <remi@fedoraproject.org> - 0.16.4-5
- fix metadata location

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Aug 14 2012 Remi Collet <remi@fedoraproject.org> - 0.16.4-3
- rebuilt for new pear_testdir

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Mar 22 2012 Remi Collet <remi@fedoraproject.org> 0.16.4-1
- update to 0.16.4 (api 0.16.0)

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Dec 11 2011 Remi Collet <remi@fedoraproject.org> 0.16.3-1
- update to 0.16.3

* Thu Apr 21 2011 Remi Collet <Fedora@FamilleCollet.com> 0.16.2-3
- doc in /usr/share/doc/pear

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Aug 15 2010 Remi Collet <Fedora@FamilleCollet.com> - 0.16.2-1
- update to 0.16.2
- rename Numbers_Words.xml to php-pear-Numbers-Words.xml
- add %%check
- set date.timezone during build

* Wed Sep 09 2009 Christopher Stone <chris.stone@gmail.com> 0.16.1-1
- Upstream sync

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Oct 23 2008 Christopher Stone <chris.stone@gmail.com> 0.15.0-4
- Update LICENSE file to version 3.01

* Thu Aug 28 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.15.0-3
- fix license tag

* Sun Jan 14 2007 Christopher Stone <chris.stone@gmail.com> 0.15.0-2
- Use correct version of PHP License

* Fri Jan 05 2007 Christopher Stone <chris.stone@gmail.com> 0.15.0-1
- Initial Release

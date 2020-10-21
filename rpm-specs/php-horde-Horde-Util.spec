# remirepo/fedora spec file for php-horde-Horde-Util
#
# Copyright (c) 2012-2019 Nick Bebout, Remi Collet
#
# License: MIT
# https://fedoraproject.org/wiki/Licensing:MIT#Modern_Style_with_sublicense
#
# Please, preserve the changelog entries
#
%{!?__pear:       %global __pear       %{_bindir}/pear}
%global bootstrap    0
%global pear_name    Horde_Util
%global pear_channel pear.horde.org
%if %{bootstrap}
%global with_tests   %{?_with_tests:1}%{!?_with_tests:0}
%else
%global with_tests   %{?_without_tests:0}%{!?_without_tests:1}
%endif

Name:           php-horde-Horde-Util
Version:        2.5.9
Release:        3%{?dist}
Summary:        Horde Utility Libraries

License:        LGPLv2
URL:            http://%{pear_channel}
Source0:        http://%{pear_channel}/get/%{pear_name}-%{version}.tgz

BuildArch:      noarch
BuildRequires:  php(language) >= 5.3.0
BuildRequires:  php-pear(PEAR) >= 1.7.0
BuildRequires:  php-channel(%{pear_channel})
%if 0%{?fedora} >= 24 || 0%{?rhel} >= 8
# Used as default LANG for the test suite
BuildRequires:  glibc-langpack-fr
# Used by some tests
BuildRequires:  glibc-langpack-tr
%endif
%if %{with_tests}
# To run unit tests
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
BuildRequires: (php-pear(%{pear_channel}/Horde_Test)      >= 2.1.0  with php-pear(%{pear_channel}/Horde_Test)      < 3)
%else
BuildRequires:  php-pear(%{pear_channel}/Horde_Test)      >= 2.1.0
%endif
%endif

Requires(post): %{__pear}
Requires(postun): %{__pear}
# From package.xml
Requires:       php(language) >= 5.3.0
Requires:       php-pear(PEAR) >= 1.7.0
Requires:       php-channel(%{pear_channel})
# Optional
Requires:       php-ctype
Requires:       php-filter
Requires:       php-iconv
Requires:       php-intl
Requires:       php-json
Requires:       php-mbstring
Requires:       php-xml
# From phpcompatinfo report for version 2.4.0
Requires:       php-dom
Requires:       php-libxml
Requires:       php-pcre
Requires:       php-session
Requires:       php-spl
# Optional: Horde_Imap_Client not required to reduce build tree

Provides:       php-pear(%{pear_channel}/%{pear_name}) = %{version}
Provides:       php-composer(horde/horde-util) = %{version}


%description
These classes provide functionality useful for all kind of applications.

%prep
%setup -q -c

cd %{pear_name}-%{version}
sed -e 's/md5sum="[^"]*"//' ../package.xml >%{name}.xml


%build
cd %{pear_name}-%{version}
# Empty build section, most likely nothing required.


%install
cd %{pear_name}-%{version}
%{__pear} install --nodeps --packagingroot %{buildroot} %{name}.xml

# Clean up unnecessary files
rm -rf %{buildroot}%{pear_metadir}/.??*

# Install XML package description
mkdir -p %{buildroot}%{pear_xmldir}
install -pm 644 %{name}.xml %{buildroot}%{pear_xmldir}


%check
%if %{with_tests}
export LANG=fr_FR.utf8
cd %{pear_name}-%{version}/test/$(echo %{pear_name} | sed -e s:_:/:g)

ret=0
for cmd in php php56 php70 php71 php72 php73 php74; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit --bootstrap bootstrap.php --verbose . || ret=1
  fi
done
exit $ret
%else
: Test disabled, bootstrap build
%endif


%post
%{__pear} install --nodeps --soft --force --register-only \
    %{pear_xmldir}/%{name}.xml >/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    %{__pear} uninstall --nodeps --ignore-errors --register-only \
        %{pear_channel}/%{pear_name} >/dev/null || :
fi


%files
%doc %{pear_docdir}/%{pear_name}
%{pear_xmldir}/%{name}.xml
%{pear_phpdir}/Horde/Array
%{pear_phpdir}/Horde/Array.php
%{pear_phpdir}/Horde/Domhtml.php
%{pear_phpdir}/Horde/String.php
%{pear_phpdir}/Horde/String
%{pear_phpdir}/Horde/Util.php
%{pear_phpdir}/Horde/Variables.php
%doc %{pear_testdir}/%{pear_name}


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov  4 2019 Remi Collet <remi@remirepo.net> - 2.5.9-1
- update to 2.5.9
- drop patch merged upstream

* Thu Oct 17 2019 Remi Collet <remi@remirepo.net> - 2.5.8-12
- another patch for PHP 7.4 from
  https://github.com/horde/Util/pull/2

* Tue Oct  1 2019 Remi Collet <remi@remirepo.net> - 2.5.8-11
- add patch for PHP 7.2 from
  https://github.com/horde/Util/pull/2

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan  4 2019 Remi Collet <remi@remirepo.net> - 2.5.8-8
- cleanup for EL-8

* Sun Nov 18 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.5.8-7
- Use C.UTF-8 locale
  See https://fedoraproject.org/wiki/Changes/Remove_glibc-langpacks-all_from_buildroot

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Dec 19 2017 Remi Collet <remi@remirepo.net> - 2.5.8-4
- Fix Horde_Mime FTBFS from Koschei, add upstream patch for PHP 7.2

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jul 02 2016 Remi Collet <remi@fedoraproject.org> - 2.5.8-1
- Update to 2.5.8

* Mon Feb 29 2016 Remi Collet <remi@fedoraproject.org> - 2.5.7-2
- add BR on glibc-langpack-fr, glibc-langpack-tr (F25+)
  FTBFS detected by Koschei

* Tue Feb 02 2016 Remi Collet <remi@fedoraproject.org> - 2.5.7-1
- Update to 2.5.7 (no change)
- PHP 7 compatible version

* Fri Jul 31 2015 Remi Collet <remi@fedoraproject.org> - 2.5.6-1
- Update to 2.5.6

* Tue Jul 28 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.5-3
- fix failed test with newer glibc, thanks Koschei

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr 14 2015 Remi Collet <remi@fedoraproject.org> - 2.5.5-1
- Update to 2.5.5

* Tue Mar 03 2015 Remi Collet <remi@fedoraproject.org> - 2.5.4-1
- Update to 2.5.4
- enable the test suite during build

* Wed Feb 11 2015 Remi Collet <remi@fedoraproject.org> - 2.5.3-1
- Update to 2.5.3
- add provides php-composer(horde/horde-util)

* Mon Dec 29 2014 Remi Collet <remi@fedoraproject.org> - 2.5.2-1
- Update to 2.5.2

* Sat Aug 16 2014 Remi Collet <remi@fedoraproject.org> - 2.5.1-1
- Update to 2.5.1

* Mon Aug 11 2014 Remi Collet <remi@fedoraproject.org> - 2.5.0-1
- Update to 2.5.0

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May 03 2014 Remi Collet <remi@fedoraproject.org> - 2.4.0-1
- Update to 2.4.0

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 28 2013 Remi Collet <remi@fedoraproject.org> - 2.3.0-1
- Update to 2.3.0
- requires php-json

* Tue May 07 2013 Remi Collet <remi@fedoraproject.org> - 2.2.2-1
- Update to 2.2.2

* Wed Mar 06 2013 Remi Collet <remi@fedoraproject.org> - 2.2.1-1
- Update to 2.2.1

* Tue Feb 26 2013 Remi Collet <remi@fedoraproject.org> - 2.2.0-1
- Update to 2.2.0

* Sun Feb 17 2013 Remi Collet <remi@fedoraproject.org> - 2.1.0-2
- fix dependency, no php-filter on EL-6

* Tue Feb 12 2013 Remi Collet <remi@fedoraproject.org> - 2.1.0-1
- Update to 2.1.0
- fix License
- cleanups
- run test when build --with tests

* Fri Jan 11 2013 Nick Bebout <nb@fedoraproject.org> - 2.0.3-1
- update to 2.0.3

* Fri Dec 28 2012 Nick Bebout <nb@fedoraproject.org> - 2.0.2-1
- update to 2.0.2

* Wed Dec 12 2012 Nick Bebout <nb@fedoraproject.org> - 2.0.1-1
- update to 2.0.1

* Tue Aug 14 2012 Remi Collet <remi@fedoraproject.org> - 1.4.0-3
- rebuilt for new pear_testdir

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jul 12 2012 Nick Bebout <nb@fedoraproject.org> - 1.4.0-1
- Update to 1.4.0

* Thu Jun 14 2012 Nick Bebout <nb@fedoraproject.org> - 1.3.1-1
- Update to 1.3.1

* Wed Mar 21 2012 Nick Bebout <nb@fedoraproject.org> - 1.3.0-1
- Update to 1.3.0

* Sat Jan 28 2012 Nick Bebout <nb@fedoraproject.org> - 1.2.0-1
- Initial package

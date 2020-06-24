# remirepo/fedora spec file for php-horde-Horde-Compress
#
# Copyright (c) 2012-2019 Nick Bebout, Remi Collet
#
# License: MIT
# https://fedoraproject.org/wiki/Licensing:MIT#Modern_Style_with_sublicense
#
# Please, preserve the changelog entries
#
%{!?__pear:       %global __pear       %{_bindir}/pear}
%global pear_name    Horde_Compress
%global pear_channel pear.horde.org

Name:           php-horde-Horde-Compress
Version:        2.2.3
Release:        2%{?dist}
Summary:        Horde Compression API

License:        LGPLv2
URL:            http://pear.horde.org
Source0:        http://%{pear_channel}/get/%{pear_name}-%{version}.tgz

BuildArch:      noarch
BuildRequires:  php-pear(PEAR) >= 1.7.0
BuildRequires:  php-channel(%{pear_channel})
BuildRequires:  gettext
# To run unit tests
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
BuildRequires: (php-pear(%{pear_channel}/Horde_Test)          >= 2.1.0  with php-pear(%{pear_channel}/Horde_Test)          < 3)
BuildRequires: (php-pear(%{pear_channel}/Horde_Stream_Filter) >= 2.0.0  with php-pear(%{pear_channel}/Horde_Stream_Filter) < 3)
BuildRequires: (php-pear(%{pear_channel}/Horde_Mime)          >= 2.5.0  with php-pear(%{pear_channel}/Horde_Mime)          < 3)
BuildRequires: (php-pear(%{pear_channel}/Horde_Icalendar)     >= 2.0.0  with php-pear(%{pear_channel}/Horde_Icalendar)     < 3)
BuildRequires: (php-pear(%{pear_channel}/Horde_Mapi)          >= 1.0.0  with php-pear(%{pear_channel}/Horde_Mapi)          < 2)
%else
BuildRequires:  php-pear(%{pear_channel}/Horde_Test) >= 2.1.0
BuildRequires:  php-pear(%{pear_channel}/Horde_Stream_Filter) >= 2.0.0
BuildRequires:  php-pear(%{pear_channel}/Horde_Mime) >= 2.5.0
BuildRequires:  php-pear(%{pear_channel}/Horde_Icalendar) >= 2.0.0
BuildRequires:  php-pear(%{pear_channel}/Horde_Mapi) >= 1.0.0
%endif
# avoid Math_Biginteger native implementation
BuildRequires:  php-gmp

Requires(post): %{__pear}
Requires(postun): %{__pear}
# From package.xml, Required
Requires:       php(language) >= 5.3.0
Requires:       php-pear(PEAR) >= 1.7.0
Requires:       php-channel(%{pear_channel})
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
Requires:      (php-pear(%{pear_channel}/Horde_Exception)   >= 2.0.0  with php-pear(%{pear_channel}/Horde_Exception)   < 3)
Requires:      (php-pear(%{pear_channel}/Horde_Mime)        >= 2.5.0  with php-pear(%{pear_channel}/Horde_Mime)        < 3)
Requires:      (php-pear(%{pear_channel}/Horde_Translation) >= 2.2.0  with php-pear(%{pear_channel}/Horde_Translation) < 3)
Requires:      (php-pear(%{pear_channel}/Horde_Util)        >= 2.0.0  with php-pear(%{pear_channel}/Horde_Util)        < 3)
# From package.xml, Optional
Recommends:    (php-pear(%{pear_channel}/Horde_Icalendar)   >= 2.0.0  with php-pear(%{pear_channel}/Horde_Icalendar)   < 3)
Recommends:    (php-pear(%{pear_channel}/Horde_Mapi)        >= 1.0.0  with php-pear(%{pear_channel}/Horde_Mapi)        < 2)
%else
Requires:       php-pear(%{pear_channel}/Horde_Exception) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Exception) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Mime) >= 2.5.0
Requires:       php-pear(%{pear_channel}/Horde_Mime) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Translation) >= 2.2.0
Requires:       php-pear(%{pear_channel}/Horde_Translation) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Util) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Util) <  3.0.0
# From package.xml, Optional
Requires:       php-pear(%{pear_channel}/Horde_Icalendar) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Icalendar) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Mapi) >= 1.0.0
Requires:       php-pear(%{pear_channel}/Horde_Mapi) <  2.0.0
%endif
Requires:       php-zlib
# From phpcompatinfo reporet form version 2.0.5
Requires:       php-date
Requires:       php-pcre
# Optional and not available: Horde_Mapi
# Optional and implicitly required Horde_Stream_Filter

Provides:       php-pear(%{pear_channel}/%{pear_name}) = %{version}
Provides:       php-composer(horde/horde-compress) = %{version}


%description
An API for various compression techniques.

%prep
%setup -q -c
cd %{pear_name}-%{version}
# Don't install .po and .pot files
# Remove checksum for .mo, as we regenerate them
sed -e '/%{pear_name}.po/d' \
    -e '/%{pear_name}.mo/s/md5sum=.*name=/name=/' \
    ../package.xml >%{name}.xml
touch -r ../package.xml %{name}.xml


%build
cd %{pear_name}-%{version}

# Regenerate the locales
for po in $(find locale -name \*.po)
do
   msgfmt $po -o $(dirname $po)/$(basename $po .po).mo
done


%install
cd %{pear_name}-%{version}
%{__pear} install --nodeps --packagingroot %{buildroot} %{name}.xml

# Clean up unnecessary files
rm -rf %{buildroot}%{pear_metadir}/.??*

# Install XML package description
mkdir -p %{buildroot}%{pear_xmldir}
install -pm 644 %{name}.xml %{buildroot}%{pear_xmldir}

for loc in locale/{??,??_??}
do
    lang=$(basename $loc)
    test -d $loc && echo "%%lang(${lang%_*}) %{pear_datadir}/%{pear_name}/$loc"
done | tee ../%{pear_name}.lang


%check
cd %{pear_name}-%{version}/test/$(echo %{pear_name} | sed -e s:_:/:g)

ret=0
for cmd in php php71 php72 php73 php74; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit --bootstrap bootstrap.php --verbose . || ret=1
  fi
done
exit $ret


%post
%{__pear} install --nodeps --soft --force --register-only \
    %{pear_xmldir}/%{name}.xml >/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    %{__pear} uninstall --nodeps --ignore-errors --register-only \
        %{pear_channel}/%{pear_name} >/dev/null || :
fi

%files -f %{pear_name}.lang
%doc %{pear_docdir}/%{pear_name}
%{pear_xmldir}/%{name}.xml
%{pear_phpdir}/Horde/Compress
%{pear_phpdir}/Horde/Compress.php
%doc %{pear_testdir}/%{pear_name}
%dir %{pear_datadir}/%{pear_name}
%dir %{pear_datadir}/%{pear_name}/locale


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov  4 2019 Remi Collet <remi@remirepo.net> - 2.2.3-1
- update to 2.2.3
- drop patch merged upstream

* Tue Oct  1 2019 Remi Collet <remi@remirepo.net> - 2.2.2-3
- add patch for PHP 7.4 from
  https://github.com/horde/Compress/pull/2

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb 11 2019 Remi Collet <remi@remirepo.net> - 2.2.2-1
- update to 2.2.2
- drop patch merged upstream
- use range dependencies

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Aug 28 2017 Remi Collet <remi@remirepo.net> - 2.2.1-1
- Update to 2.2.1

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed May  3 2017 Remi Collet <remi@remirepo.net> - 2.2.0-1
- Update to 2.2.0
- open https://github.com/horde/horde/pull/219 - fix tests

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 20 2016 Remi Collet <remi@fedoraproject.org> - 2.1.6-1
- Update to 2.1.6

* Mon Mar 21 2016 Remi Collet <remi@fedoraproject.org> - 2.1.5-1
- Update to 2.1.5

* Mon Feb  8 2016 Remi Collet <remi@fedoraproject.org> - 2.1.4-1
- Update to 2.1.4 (no change)
- PHP 7 compatible version

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jul 31 2015 Remi Collet <remi@fedoraproject.org> - 2.1.3-1
- Update to 2.1.3

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr 28 2015 Remi Collet <remi@fedoraproject.org> - 2.1.2-1
- Update to 2.1.2

* Sat Mar 14 2015 Remi Collet <remi@fedoraproject.org> - 2.1.1-1
- Update to 2.1.1

* Mon Feb 16 2015 Remi Collet <remi@fedoraproject.org> - 2.1.0-1
- Update to 2.1.0
- add dependency on Horde_Mime
- raise dependency on Horde_Translation >= 2.2.0
- add provides php-composer(horde/horde-mime)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 22 2014 Remi Collet <remi@fedoraproject.org> - 2.0.8-1
- Update to 2.0.8

* Wed Jan 22 2014 Remi Collet <remi@fedoraproject.org> - 2.0.7-1
- Update to 2.0.7
- add optional requires: Horde_Mapi, Horde_Icalendar

* Thu Jul 25 2013 Remi Collet <remi@fedoraproject.org> - 2.0.4-1
- Update to 2.0.4

* Wed Mar 20 2013 Nick Bebout <nb@fedoraproject.org> - 2.0.3-3
- Update for review

* Wed Feb 6 2013 Nick Bebout <nb@fedoraproject.org> - 2.0.3-2
- Update for review

* Tue Jan 29 2013 Remi Collet <remi@fedoraproject.org> - 2.0.3-1
- Update to 2.0.3

* Wed Jan  9 2013 Remi Collet <remi@fedoraproject.org> - 2.0.2-1
- Update to 2.0.2
- use local script instead of find_lang
- new test layout (requires Horde_Test 2.1.0)
- add option for test (can't be run in mock)

* Wed Nov  7 2012 Remi Collet <remi@fedoraproject.org> - 2.0.1-1
- Update to 2.0.1

* Sat Nov  3 2012 Remi Collet <remi@fedoraproject.org> - 2.0.0-1
- Update to 2.0.0

* Mon Jun 25 2012 Nick Bebout <nb@fedoraproject.org> - 1.0.7-2
- Fix requires

* Wed Jun 20 2012 Nick Bebout <nb@fedoraproject.org> - 1.0.7-1
- Upgrade to 1.0.7, fix review issues

* Sat Jan 28 2012 Nick Bebout <nb@fedoraproject.org> - 1.0.6-1
- Initial package

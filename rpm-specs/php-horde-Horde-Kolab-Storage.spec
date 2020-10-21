# remirepo/fedora spec file for php-horde-Horde-Kolab-Storage
#
# Copyright (c) 2013-2019 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%{!?__pear:       %global __pear       %{_bindir}/pear}
%global bootstrap    0
%global pear_name    Horde_Kolab_Storage
%global pear_channel pear.horde.org
%if %{bootstrap}
%global with_tests   %{?_with_tests:1}%{!?_with_tests:0}
%else
%global with_tests   %{?_without_tests:0}%{!?_without_tests:1}
%endif

Name:           php-horde-Horde-Kolab-Storage
Version:        2.2.4
Release:        3%{?dist}
Summary:        A package for handling Kolab data stored on an IMAP server

License:        LGPLv2
URL:            http://%{pear_channel}
Source0:        http://%{pear_channel}/get/%{pear_name}-%{version}.tgz

BuildArch:      noarch
BuildRequires:  gettext
BuildRequires:  php(language) >= 5.3.0
BuildRequires:  php-pear(PEAR) >= 1.7.0
BuildRequires:  php-channel(%{pear_channel})
%if %{with_tests}
# To run unit tests
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
BuildRequires: (php-pear(%{pear_channel}/Horde_Test)         >= 2.1.0  with php-pear(%{pear_channel}/Horde_Test)         < 3)
BuildRequires: (php-pear(%{pear_channel}/Horde_Cache)        >= 2.0.0  with php-pear(%{pear_channel}/Horde_Cache)        < 3)
BuildRequires: (php-pear(%{pear_channel}/Horde_Exception)    >= 2.0.0  with php-pear(%{pear_channel}/Horde_Exception)    < 3)
BuildRequires: (php-pear(%{pear_channel}/Horde_Kolab_Format) >= 2.0.0  with php-pear(%{pear_channel}/Horde_Kolab_Format) < 3)
BuildRequires: (php-pear(%{pear_channel}/Horde_Mime)         >= 2.0.0  with php-pear(%{pear_channel}/Horde_Mime)         < 3)
BuildRequires: (php-pear(%{pear_channel}/Horde_Translation)  >= 2.2.0  with php-pear(%{pear_channel}/Horde_Translation)  < 3)
BuildRequires: (php-pear(%{pear_channel}/Horde_Support)      >= 2.0.0  with php-pear(%{pear_channel}/Horde_Support)      < 3)
BuildRequires: (php-pear(%{pear_channel}/Horde_Util)         >= 2.0.0  with php-pear(%{pear_channel}/Horde_Util)         < 3)
BuildRequires: (php-pear(%{pear_channel}/Horde_Imap_Client)  >= 2.14.0 with php-pear(%{pear_channel}/Horde_Imap_Client)  < 3)
BuildRequires: (php-pear(%{pear_channel}/Horde_History)      >= 2.0.0  with php-pear(%{pear_channel}/Horde_History)      < 3)
%else
BuildRequires:  php-pear(%{pear_channel}/Horde_Test) >= 2.1.0
BuildRequires:  php-pear(%{pear_channel}/Horde_Cache) >= 2.0.0
BuildRequires:  php-pear(%{pear_channel}/Horde_History) >= 2.0.0
BuildRequires:  php-pear(%{pear_channel}/Horde_Imap_Client) >= 2.0.0
BuildRequires:  php-pear(%{pear_channel}/Horde_Kolab_Format) >= 2.0.0
%endif
%endif

Requires(post): %{__pear}
Requires(postun): %{__pear}
Requires:       php(language) >= 5.3.0
Requires:       php-date
Requires:       php-imap
Requires:       php-json
Requires:       php-pcre
Requires:       php-spl
Requires:       php-pear(PEAR) >= 1.7.0
Requires:       php-channel(%{pear_channel})
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
Requires:      (php-pear(%{pear_channel}/Horde_Cache)        >= 2.0.0  with php-pear(%{pear_channel}/Horde_Cache)        < 3)
Requires:      (php-pear(%{pear_channel}/Horde_Exception)    >= 2.0.0  with php-pear(%{pear_channel}/Horde_Exception)    < 3)
Requires:      (php-pear(%{pear_channel}/Horde_Kolab_Format) >= 2.0.0  with php-pear(%{pear_channel}/Horde_Kolab_Format) < 3)
Requires:      (php-pear(%{pear_channel}/Horde_Mime)         >= 2.0.0  with php-pear(%{pear_channel}/Horde_Mime)         < 3)
Requires:      (php-pear(%{pear_channel}/Horde_Translation)  >= 2.2.0  with php-pear(%{pear_channel}/Horde_Translation)  < 3)
Requires:      (php-pear(%{pear_channel}/Horde_Support)      >= 2.0.0  with php-pear(%{pear_channel}/Horde_Support)      < 3)
Requires:      (php-pear(%{pear_channel}/Horde_Util)         >= 2.0.0  with php-pear(%{pear_channel}/Horde_Util)         < 3)
# Optional
Recommends:    (php-pear(%{pear_channel}/Horde_Imap_Client)  >= 2.14.0 with php-pear(%{pear_channel}/Horde_Imap_Client)  < 3)
Recommends:    (php-pear(%{pear_channel}/Horde_History)      >= 2.0.0  with php-pear(%{pear_channel}/Horde_History)      < 3)
Recommends:     php-pear(HTTP_Request)
Recommends:     php-pear(Net_IMAP) >= 1.1.0
%else
Requires:       php-pear(%{pear_channel}/Horde_Cache) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Cache) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Exception) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Exception) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Kolab_Format) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Kolab_Format) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Mime) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Mime) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Translation) >= 2.2.0
Requires:       php-pear(%{pear_channel}/Horde_Translation) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Support) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Support) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Util) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Util) <  3.0.0
# Optional
Requires:       php-pear(%{pear_channel}/Horde_Imap_Client) >= 2.14.0
Requires:       php-pear(%{pear_channel}/Horde_Imap_Client) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_History) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_History) <  3.0.0
Requires:       php-pear(HTTP_Request)
Requires:       php-pear(Net_IMAP) >= 1.1.0
%endif

Provides:       php-pear(%{pear_channel}/%{pear_name}) = %{version}
Provides:       php-composer(horde/horde-kolab-storage) = %{version}


%description
Storing user data in an IMAP account belonging to the user is one of the
Kolab server core concepts. This package provides all the necessary means
to deal with this type of data storage effectively.


%prep
%setup -q -c
cd %{pear_name}-%{version}

# Don't install .po and .pot files
# Remove checksum for .mo, as we regenerate them
sed -e '/%{pear_name}.po/d' \
    -e '/Horde_Other.po/d' \
    -e '/%{pear_name}.mo/s/md5sum=.*name=/name=/' \
    -e '/role="test"/s/md5sum=.*name=/name=/' \
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

# Locales
for loc in locale/{??,??_??}
do
    lang=$(basename $loc)
    test -d %{buildroot}%{pear_datadir}/%{pear_name}/$loc && \
         echo "%%lang(${lang%_*}) %{pear_datadir}/%{pear_name}/$loc"
done | tee ../%{pear_name}.lang


%check
%if %{with_tests}
cd %{pear_name}-%{version}/test/$(echo %{pear_name} | sed -e s:_:/:g)

# Retrieve version of Horde_Kolab_Format
VER=$(sed -n "/const VERSION/{s/.* '//;s/'.*\$//;p}" %{pear_phpdir}/Horde/Kolab/Format.php)

# Fix test executed from sources
sed -e "s/Horde_Kolab_Format_Xml-@version@/Horde_Kolab_Format_Xml-${VER}/" \
    -e "s/Horde_Kolab_Storage @version@/Horde_Kolab_Storage %{version}/" \
    -i ComponentTest/Data/Object/Message/ModifiedTest.php \
       ComponentTest/Data/Object/Message/NewTest.php

ret=0
if phpunit --atleast-version 4; then
  for cmd in php php56 php70 php71 php72 php73 php74; do
    if which $cmd; then
      $cmd %{_bindir}/phpunit --bootstrap bootstrap.php --verbose . || ret=1
    fi
  done
else : PHPUnit is too old
fi

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


%files -f %{pear_name}.lang
%doc %{pear_docdir}/%{pear_name}
%{pear_xmldir}/%{name}.xml
%{pear_phpdir}/Horde/Kolab/Storage
%{pear_phpdir}/Horde/Kolab/Storage.php
%dir %{pear_datadir}/%{pear_name}
%dir %{pear_datadir}/%{pear_name}/locale
%doc %{pear_testdir}/%{pear_name}


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov  4 2019 Remi Collet <remi@remirepo.net> - 2.2.4-1
- update to 2.2.4
- drop patch merged upstream

* Thu Oct 17 2019 Remi Collet <remi@remirepo.net> - 2.2.3-8
- add patch for PHP 7.4 from
  https://github.com/horde/Kolab_Storage/pull/1
- use range dependencies

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 20 2016 Remi Collet <remi@fedoraproject.org> - 2.2.3-1
- Update to 2.2.3

* Tue Apr 05 2016 Remi Collet <remi@fedoraproject.org> - 2.2.2-1
- Update to 2.2.2

* Mon Feb  8 2016 Remi Collet <remi@fedoraproject.org> - 2.2.1-1
- Update to 2.2.1
- PHP 7 compatible version

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 03 2016 Remi Collet <remi@fedoraproject.org> - 2.2.0-1
- Update to 2.2.0

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr 28 2015 Remi Collet <remi@fedoraproject.org> - 2.1.4-1
- Update to 2.1.4

* Tue Apr 14 2015 Remi Collet <remi@fedoraproject.org> - 2.1.3-1
- Update to 2.1.3

* Mon Mar 16 2015 Remi Collet <remi@fedoraproject.org> - 2.1.2-2
- add upstream patch for test suite, thanks Koschei

* Fri Jan 09 2015 Remi Collet <remi@fedoraproject.org> - 2.1.2-1
- Update to 2.1.2
- add provides php-composer(horde/horde-kolab-storage)
- raise dependency on Horde_Translation 2.2.0

* Tue Nov 25 2014 Remi Collet <remi@fedoraproject.org> - 2.1.1-2
- add suptream patch for test (thanks Koschei)

* Sat Aug 30 2014 Remi Collet <remi@fedoraproject.org> - 2.1.1-1
- Update to 2.1.1

* Sat Aug 16 2014 Remi Collet <remi@fedoraproject.org> - 2.1.0-3
- fix test suite for PHP 5.6

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Apr 04 2014 Remi Collet <remi@fedoraproject.org> - 2.1.0-1
- Update to 2.1.0

* Tue Aug 27 2013 Remi Collet <remi@fedoraproject.org> - 2.0.5-1
- Update to 2.0.5
- raise dependency on Horde_Imap_Client >= 2.14.0

* Fri Mar 29 2013 Remi Collet <remi@fedoraproject.org> - 2.0.4-2
- add requires on Net_IMAP

* Thu Mar 28 2013 Remi Collet <remi@fedoraproject.org> - 2.0.4-1
- initial package

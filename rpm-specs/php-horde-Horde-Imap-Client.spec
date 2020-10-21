# remirepo/fedora spec file for php-horde-Horde-Imap-Client
#
# Copyright (c) 2012-2019 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%{!?__pear:       %global __pear       %{_bindir}/pear}
%global pear_name    Horde_Imap_Client
%global pear_channel pear.horde.org
%global with_tests   0%{!?_without_tests:1}

Name:           php-horde-Horde-Imap-Client
Version:        2.30.1
Release:        3%{?dist}
Summary:        Horde IMAP abstraction interface

License:        LGPLv2
URL:            http://pear.horde.org
Source0:        http://%{pear_channel}/get/%{pear_name}-%{version}.tgz

BuildArch:      noarch
BuildRequires:  php(language) >= 5.3.0
BuildRequires:  php-pear(PEAR) >= 1.7.0
BuildRequires:  php-channel(%{pear_channel})
BuildRequires:  gettext
%if %{with_tests}
# To run unit tests
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
BuildRequires: (php-pear(%{pear_channel}/Horde_Test)           >= 2.2.7   with php-pear(%{pear_channel}/Horde_Test)           < 3)
BuildRequires: (php-pear(%{pear_channel}/Horde_Stream)         >= 1.4.0   with php-pear(%{pear_channel}/Horde_Stream)         < 2)
BuildRequires: (php-pear(%{pear_channel}/Horde_Mime)           >= 2.5.2   with php-pear(%{pear_channel}/Horde_Mime)           < 3)
BuildRequires: (php-pear(%{pear_channel}/Horde_Cache)          >= 2.0.0   with php-pear(%{pear_channel}/Horde_Cache)          < 3)
BuildRequires: (php-pear(%{pear_channel}/Horde_Pack)           >= 1.0.0   with php-pear(%{pear_channel}/Horde_Pack)           < 2)
BuildRequires: (php-pear(%{pear_channel}/Horde_Crypt_Blowfish) >= 1.1.0   with php-pear(%{pear_channel}/Horde_Crypt_Blowfish) < 2)
BuildRequires: (php-pear(%{pear_channel}/Horde_Stringprep)     >= 1.0.0   with php-pear(%{pear_channel}/Horde_Stringprep)     < 2)
%else
BuildRequires:  php-pear(%{pear_channel}/Horde_Test) >= 2.2.7
BuildRequires:  php-pear(%{pear_channel}/Horde_Stream) >= 1.4.0
BuildRequires:  php-pear(%{pear_channel}/Horde_Mime) >= 2.5.2
BuildRequires:  php-pear(%{pear_channel}/Horde_Cache) >= 2.0.0
BuildRequires:  php-pear(%{pear_channel}/Horde_Pack) >= 1.0.0
BuildRequires:  php-pear(%{pear_channel}/Horde_Crypt_Blowfish) >= 1.1.0
BuildRequires:  php-pear(%{pear_channel}/Horde_Stringprep) >= 1.0.0
%endif
%endif

Requires(post): %{__pear}
Requires(postun): %{__pear}
# From package.xml, required
Requires:       php(language) >= 5.3.0
Requires:       php-hash
Requires:       php-intl
Requires:       php-json
Requires:       php-pear(PEAR) >= 1.7.0
Requires:       php-channel(%{pear_channel})
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
Requires:      (php-pear(%{pear_channel}/Horde_Exception)     >= 2.0.0    with php-pear(%{pear_channel}/Horde_Exception)     < 3)
Requires:      (php-pear(%{pear_channel}/Horde_Mail)          >= 2.0.0    with php-pear(%{pear_channel}/Horde_Mail)          < 3)
Requires:      (php-pear(%{pear_channel}/Horde_Mime)          >= 2.5.2    with php-pear(%{pear_channel}/Horde_Mime)          < 3)
Requires:      (php-pear(%{pear_channel}/Horde_Secret)        >= 2.0.0    with php-pear(%{pear_channel}/Horde_Secret)        < 3)
Requires:      (php-pear(%{pear_channel}/Horde_Socket_Client) >= 2.0.0    with php-pear(%{pear_channel}/Horde_Socket_Client) < 3)
Requires:      (php-pear(%{pear_channel}/Horde_Stream)        >= 1.4.0    with php-pear(%{pear_channel}/Horde_Stream)        < 2)
Requires:      (php-pear(%{pear_channel}/Horde_Stream_Filter) >= 2.0.0    with php-pear(%{pear_channel}/Horde_Stream_Filter) < 3)
Requires:      (php-pear(%{pear_channel}/Horde_Translation)   >= 2.2.0    with php-pear(%{pear_channel}/Horde_Translation)   < 3)
Requires:      (php-pear(%{pear_channel}/Horde_Util)          >= 2.0.0    with php-pear(%{pear_channel}/Horde_Util)          < 3)
# From package.xml, optional
Recommends:    (php-pear(%{pear_channel}/Horde_Cache)          >= 2.0.0   with php-pear(%{pear_channel}/Horde_Cache)         < 3)
Recommends:    (php-pear(%{pear_channel}/Horde_Db)             >= 2.2.0   with php-pear(%{pear_channel}/Horde_Db)            < 3)
Recommends:    (php-pear(%{pear_channel}/Horde_Pack)           >= 1.0.0   with php-pear(%{pear_channel}/Horde_Pack)          < 2)
Recommends:    (php-pear(%{pear_channel}/Horde_Stringprep)     >= 1.0.0   with php-pear(%{pear_channel}/Horde_Stringprep)    < 2)
%else
Requires:       php-pear(%{pear_channel}/Horde_Exception) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Exception) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Mail) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Mail) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Mime) >= 2.5.2
Requires:       php-pear(%{pear_channel}/Horde_Mime) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Secret) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Secret) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Socket_Client) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Socket_Client) <  3
Requires:       php-pear(%{pear_channel}/Horde_Stream) >= 1.4.0
Requires:       php-pear(%{pear_channel}/Horde_Stream) <  2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Stream_Filter) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Stream_Filter) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Translation) >= 2.2.0
Requires:       php-pear(%{pear_channel}/Horde_Translation) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Util) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Util) <  3.0.0
# From package.xml, optional
Requires:       php-mbstring
Requires:       php-pear(%{pear_channel}/Horde_Cache) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Cache) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Db) >= 2.2.0
Requires:       php-pear(%{pear_channel}/Horde_Db) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Pack) >= 1.0.0
Requires:       php-pear(%{pear_channel}/Horde_Pack) <  2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Stringprep) >= 1.0.0
Requires:       php-pear(%{pear_channel}/Horde_Stringprep) <  2.0.0
%endif
Requires:       php-mbstring
# From phpcompatinfo report for version 2.19.4
Requires:       php-date
Requires:       php-openssl
Requires:       php-pcre
Requires:       php-spl
# Optional and implicilyt required :
#   Horde_Compress_Fast, Horde_HashTable, Horde_Mongo, mongo, Horde_Support
#   Horde_Crypt_Blowfish

Provides:       php-pear(%{pear_channel}/%{pear_name}) = %{version}
Provides:       php-composer(horde/horde-imap-client) = %{version}


%description
An abstracted API interface to various IMAP4rev1 (RFC 3501) backend
drivers.


%prep
%setup -q -c
cd %{pear_name}-%{version}

# Don't install .po and .pot files
# Remove checksum for .mo, as we regenerate them
sed -e '/%{pear_name}\.po/d' \
    -e '/%{pear_name}\.mo/s/md5sum=.*name=/name=/' \
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
    test -d $loc && echo "%%lang(${lang%_*}) %{pear_datadir}/%{pear_name}/$loc"
done | tee ../%{pear_name}.lang


%check
%if %{with_tests}
export LANG=C.UTF-8
cd %{pear_name}-%{version}/test/$(echo %{pear_name} | sed -e s:_:/:g)

ret=0
for cmd in php php71 php72 php73 php74; do
  if which $cmd; then
    if %{_bindir}/phpunit --atleast-version 4.8; then
      $cmd %{_bindir}/phpunit --bootstrap bootstrap.php --verbose . || ret=1
    else
     : PHPUnit is too old for this package
    fi
  fi
done
exit $ret
%else
: bootstrap build with test suite disabled
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
%dir %{pear_phpdir}/Horde/Imap
%{pear_phpdir}/Horde/Imap/Client
%{pear_phpdir}/Horde/Imap/Client.php
%doc %{pear_testdir}/%{pear_name}
%dir %{pear_datadir}/%{pear_name}
%dir %{pear_datadir}/%{pear_name}/locale
%{pear_datadir}/%{pear_name}/migration


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.30.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.30.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov  4 2019 Remi Collet <remi@remirepo.net> - 2.30.1-1
- update to 2.30.1
- drop patch merged upstream

* Tue Oct  1 2019 Remi Collet <remi@remirepo.net> - 2.30.0-2
- add patch for PHP 7.4 from
  https://github.com/horde/Imap_Client/pull/9

* Mon Sep 30 2019 Remi Collet <remi@remirepo.net> - 2.30.0-1
- update to 2.30.0

* Mon Sep 16 2019 Remi Collet <remi@remirepo.net> - 2.29.18-1
- update to 2.29.18

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.29.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Mar  3 2019 Remi Collet <remi@remirepo.net> - 2.29.17-1
- update to 2.29.17
- use range dependencies

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.29.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Nov 18 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.29.16-3
- Use C.UTF-8 locale
  See https://fedoraproject.org/wiki/Changes/Remove_glibc-langpacks-all_from_buildroot

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.29.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 25 2018 Remi Collet <remi@remirepo.net> - 2.29.16-1
- update to 2.29.16

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.29.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Aug 28 2017 Remi Collet <remi@remirepo.net> - 2.29.15-1
- Update to 2.29.15

* Tue Aug  1 2017 Remi Collet <remi@remirepo.net> - 2.29.14-1
- Update to 2.29.14

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.29.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 23 2017 Remi Collet <remi@remirepo.net> - 2.29.13-1
- Update to 2.29.13

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.29.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 20 2016 Remi Collet <remi@fedoraproject.org> - 2.29.12-1
- Update to 2.29.12

* Sun Dec 04 2016 Remi Collet <remi@fedoraproject.org> - 2.29.11-1
- Update to 2.29.11

* Thu Nov 03 2016 Remi Collet <remi@fedoraproject.org> - 2.29.10-1
- Update to 2.29.10

* Fri Sep 02 2016 Remi Collet <remi@fedoraproject.org> - 2.29.9-1
- Update to 2.29.9

* Sat Jul 02 2016 Remi Collet <remi@fedoraproject.org> - 2.29.8-1
- Update to 2.29.8

* Thu Jun 02 2016 Remi Collet <remi@fedoraproject.org> - 2.29.7-1
- Update to 2.29.7

* Mon Mar 21 2016 Remi Collet <remi@fedoraproject.org> - 2.29.6-1
- Update to 2.29.6

* Mon Feb  8 2016 Remi Collet <remi@fedoraproject.org> - 2.29.5-1
- Update to 2.29.5
- PHP 7 compatible version

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.29.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Nov 25 2015 Remi Collet <remi@fedoraproject.org> - 2.29.4-1
- Update to 2.29.4

* Tue Sep 08 2015 Remi Collet <remi@fedoraproject.org> - 2.29.3-1
- Update to 2.29.3

* Wed Sep 02 2015 Remi Collet <remi@fedoraproject.org> - 2.29.2-1
- Update to 2.29.2

* Wed Jul 15 2015 Remi Collet <remi@fedoraproject.org> - 2.29.1-1
- Update to 2.29.1

* Mon Jun 22 2015 Remi Collet <remi@fedoraproject.org> - 2.29.0-1
- Update to 2.29.0
- add BR on Horde_Crypt_Blowfish and Horde_Stringprep
- add optional dependency on Horde_Stringprep

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.28.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed May 13 2015 Remi Collet <remi@fedoraproject.org> - 2.28.1-1
- Update to 2.28.1

* Tue Apr 28 2015 Remi Collet <remi@fedoraproject.org> - 2.28.0-1
- Update to 2.28.0

* Tue Mar 10 2015 Remi Collet <remi@fedoraproject.org> - 2.27.0-1
- Update to 2.27.0
- add provides php-composer(horde/horde-imap-client)
- raise dependency on Horde_Socket_Client > 2

* Tue Jan 27 2015 Remi Collet <remi@fedoraproject.org> - 2.26.1-1
- Update to 2.26.1

* Tue Jan 13 2015 Remi Collet <remi@fedoraproject.org> - 2.26.0-2
- add upstream for stream change in php

* Wed Jan 07 2015 Remi Collet <remi@fedoraproject.org> - 2.26.0-1
- Update to 2.26.0

* Wed Dec 03 2014 Remi Collet <remi@fedoraproject.org> - 2.25.6-1
- Update to 2.25.6
- raise dependency on Horde_Mime >= 2.5.2

* Tue Nov 25 2014 Remi Collet <remi@fedoraproject.org> - 2.25.5-1
- Update to 2.25.5

* Sun Nov 23 2014 Remi Collet <remi@fedoraproject.org> - 2.25.4-1
- Update to 2.25.4
- raise dependency on Horde_Mime >= 2.5.0

* Tue Nov 11 2014 Remi Collet <remi@fedoraproject.org> - 2.25.3-1
- Update to 2.25.3
- raise dependency on Horde_Translation >= 2.2.0

* Tue Oct 14 2014 Remi Collet <remi@fedoraproject.org> - 2.25.2-1
- Update to 2.25.2

* Wed Sep 17 2014 Remi Collet <remi@fedoraproject.org> - 2.25.1-1
- Update to 2.25.1

* Thu Sep 04 2014 Remi Collet <remi@fedoraproject.org> - 2.25.0-1
- Update to 2.25.0
- add dependency on php-intl

* Tue Aug 12 2014 Remi Collet <remi@fedoraproject.org> - 2.24.2-1
- Update to 2.24.2

* Mon Aug 11 2014 Remi Collet <remi@fedoraproject.org> - 2.24.1-1
- Update to 2.24.1

* Tue Aug 05 2014 Remi Collet <remi@fedoraproject.org> - 2.24.0-1
- Update to 2.24.0

* Wed Jul 09 2014 Remi Collet <remi@fedoraproject.org> - 2.23.2-1
- Update to 2.23.2

* Wed Jun 18 2014 Remi Collet <remi@fedoraproject.org> - 2.23.1-1
- Update to 2.23.1

* Tue Jun 17 2014 Remi Collet <remi@fedoraproject.org> - 2.23.0-1
- Update to 2.23.0

* Sat Jun 07 2014 Remi Collet <remi@fedoraproject.org> - 2.22.0-1
- Update to 2.22.0

* Wed Jun 04 2014 Remi Collet <remi@fedoraproject.org> - 2.21.0-1
- Update to 2.21.0

* Thu May 22 2014 Remi Collet <remi@fedoraproject.org> - 2.20.0-1
- Update to 2.20.0

* Wed May 14 2014 Remi Collet <remi@fedoraproject.org> - 2.19.6-1
- Update to 2.19.6

* Sat May 03 2014 Remi Collet <remi@fedoraproject.org> - 2.19.5-1
- Update to 2.19.5

* Thu Apr 24 2014 Remi Collet <remi@fedoraproject.org> - 2.19.4-1
- Update to 2.19.4

* Wed Apr 23 2014 Remi Collet <remi@fedoraproject.org> - 2.19.3-1
- Update to 2.19.3

* Thu Apr 03 2014 Remi Collet <remi@fedoraproject.org> - 2.19.2-1
- Update to 2.19.2

* Mon Mar 17 2014 Remi Collet <remi@fedoraproject.org> - 2.19.1-1
- Update to 2.19.1

* Tue Mar 11 2014 Remi Collet <remi@fedoraproject.org> - 2.19.0-1
- Update to 2.19.0
- raise dependencies: Horde_Test 2.2.7, Horde_Mime 2.3.0
- add BR on Horde_Pack

* Tue Mar 04 2014 Remi Collet <remi@fedoraproject.org> - 2.18.6-1
- Update to 2.18.6

* Tue Feb 25 2014 Remi Collet <remi@fedoraproject.org> - 2.18.3-1
- Update to 2.18.3

* Fri Feb 14 2014 Remi Collet <remi@fedoraproject.org> - 2.18.1-1
- Update to 2.18.1

* Tue Feb 11 2014 Remi Collet <remi@fedoraproject.org> - 2.18.0-1
- Update to 2.18.0
- Raise dependencies: Horde_Stream >= 1.4.0, Horde_Translation >= 2.1.0

* Wed Jan 22 2014 Remi Collet <remi@fedoraproject.org> - 2.17.1-1
- Update to 2.17.1

* Sat Jan 18 2014 Remi Collet <remi@fedoraproject.org> - 2.17.0-1
- Update to 2.17.0
- add dependency: Horde_Pack >= 1.0.0
- add dependency: Horde_Socket_Client >= 1.1.0

* Sat Oct 12 2013 Remi Collet <remi@fedoraproject.org> - 2.15.5-1
- Update to 2.15.5

* Thu Oct 10 2013 Remi Collet <remi@fedoraproject.org> - 2.15.4-1
- Update to 2.15.4

* Tue Sep 17 2013 Remi Collet <remi@fedoraproject.org> - 2.15.3-1
- Update to 2.15.3

* Mon Sep 16 2013 Remi Collet <remi@fedoraproject.org> - 2.15.2-1
- Update to 2.15.2

* Sun Sep 08 2013 Remi Collet <remi@fedoraproject.org> - 2.15.0-1
- Update to 2.15.0

* Mon Aug 26 2013 Remi Collet <remi@fedoraproject.org> - 2.14.0-1
- Update to 2.14.0

* Wed Aug 21 2013 Remi Collet <remi@fedoraproject.org> - 2.13.1-1
- Update to 2.13.1

* Tue Aug 20 2013 Remi Collet <remi@fedoraproject.org> - 2.13.0-1
- Update to 2.13.0

* Thu Jul 25 2013 Remi Collet <remi@fedoraproject.org> - 2.12.0-1
- Update to 2.12.0
- Horde_Secret, Horde_Stream_Filter and json are now mandatory

* Wed Jun 19 2013 Remi Collet <remi@fedoraproject.org> - 2.11.6-1
- Update to 2.11.6

* Fri May 31 2013 Remi Collet <remi@fedoraproject.org> - 2.11.2-1
- Update to 2.11.2
- add mising requires on Horde_Translation

* Tue May 21 2013 Remi Collet <remi@fedoraproject.org> - 2.10.1-1
- Update to 2.10.1
- switch from Conflicts >= max to Requires < max

* Sat May 04 2013 Remi Collet <remi@fedoraproject.org> - 2.9.0-1
- Update to 2.9.0
- drop optional requires imap
- add optional dependency on Horde_Db

* Fri Apr 19 2013 Remi Collet <remi@fedoraproject.org> - 2.8.2-1
- Update to 2.8.2

* Fri Mar 29 2013 Remi Collet <remi@fedoraproject.org> - 2.8.1-1
- Update to 2.8.1

* Wed Mar 27 2013 Remi Collet <remi@fedoraproject.org> - 2.8.0-1
- Update to 2.8.0

* Sat Mar 09 2013 Remi Collet <remi@fedoraproject.org> - 2.7.2-1
- Update to 2.7.2

* Wed Mar 06 2013 Remi Collet <remi@fedoraproject.org> - 2.7.1-1
- Update to 2.7.1

* Tue Feb 26 2013 Remi Collet <remi@fedoraproject.org> - 2.7.0-1
- Update to 2.7.0

* Sat Feb 09 2013 Remi Collet <remi@fedoraproject.org> - 2.6.0-1
- Update to 2.6.0

* Wed Jan 23 2013 Remi Collet <remi@fedoraproject.org> - 2.5.0-1
- Update to 2.5.0

* Sat Jan  5 2013 Remi Collet <remi@fedoraproject.org> - 2.4.2-1
- Update to 2.4.2

* Fri Dec 21 2012 Remi Collet <remi@fedoraproject.org> - 2.4.1-1
- Update to 2.4.1

* Tue Dec 18 2012 Remi Collet <remi@fedoraproject.org> - 2.4.0-1
- Update to 2.4.0

* Sat Dec  8 2012 Remi Collet <remi@fedoraproject.org> - 2.3.2-1
- Update to 2.3.2

* Tue Dec  4 2012 Remi Collet <remi@fedoraproject.org> - 2.3.0-1
- Update to 2.3.0

* Wed Nov 28 2012 Remi Collet <remi@fedoraproject.org> - 2.2.3-1
- Update to 2.2.3

* Tue Nov 27 2012 Remi Collet <remi@fedoraproject.org> - 2.2.2-1
- Update to 2.2.2
- review locale management

* Thu Nov 22 2012 Remi Collet <remi@fedoraproject.org> - 2.2.1-1
- Update to 2.2.1

* Mon Nov 19 2012 Remi Collet <remi@fedoraproject.org> - 2.2.0-1
- Update to 2.2.0

* Mon Nov 12 2012 Remi Collet <remi@fedoraproject.org> - 2.1.6-1
- Update to 2.1.6

* Wed Nov  7 2012 Remi Collet <remi@fedoraproject.org> - 2.1.5-1
- Update to 2.1.5

* Tue Nov  6 2012 Remi Collet <remi@fedoraproject.org> - 2.1.3-1
- Update to 2.1.3

* Sun Nov  4 2012 Remi Collet <remi@fedoraproject.org> - 2.1.1-1
- Update to 2.1.1

* Sat Nov  3 2012 Remi Collet <remi@fedoraproject.org> - 2.0.0-1
- Update to 2.0.0


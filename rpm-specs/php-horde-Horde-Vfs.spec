# remirepo/fedora spec file for php-horde-Horde-Vfs
#
# Copyright (c) 2012-2020 Nick Bebout, Remi Collet
#
# License: MIT
# https://fedoraproject.org/wiki/Licensing:MIT#Modern_Style_with_sublicense
#
# Please, preserve the changelog entries
#
%{!?__pear:       %global __pear       %{_bindir}/pear}
%global pear_name    Horde_Vfs
%global pear_channel pear.horde.org

%global with_tests   %{?_without_tests:0}%{!?_without_tests:1}

Name:           php-horde-Horde-Vfs
Version:        2.4.1
Release:        1%{?dist}
Summary:        Virtual File System API

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
BuildRequires: (php-pear(%{pear_channel}/Horde_Test)    >= 2.1.0  with php-pear(%{pear_channel}/Horde_Test)    < 3)
BuildRequires: (php-pear(%{pear_channel}/Horde_Db)      >= 2.4.0  with php-pear(%{pear_channel}/Horde_Db)      < 3)
%else
BuildRequires:  php-pear(%{pear_channel}/Horde_Test)    >= 2.1.0
BuildRequires:  php-pear(%{pear_channel}/Horde_Db)      >= 2.4.0
%endif
%endif

Requires(post): %{__pear}
Requires(postun): %{__pear}
Requires:       php(language) >= 5.3.0
Requires:       php-date
Requires:       php-pcre
Requires:       php-posix
Requires:       php-pear(PEAR) >= 1.7.0
Requires:       php-channel(%{pear_channel})
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
Requires:      (php-pear(%{pear_channel}/Horde_Exception)     >= 2.0.0  with php-pear(%{pear_channel}/Horde_Exception)     < 3)
Requires:      (php-pear(%{pear_channel}/Horde_Translation)   >= 2.2.0  with php-pear(%{pear_channel}/Horde_Translation)   < 3)
Requires:      (php-pear(%{pear_channel}/Horde_Util)          >= 2.0.0  with php-pear(%{pear_channel}/Horde_Util)          < 3)
# Optional
Recommends:     php-ftp
Recommends:     php-pecl(ssh2) >= 0.12
Recommends:    (php-pear(%{pear_channel}/Horde_Auth)          >= 2.0.0  with php-pear(%{pear_channel}/Horde_Auth)          < 3)
Recommends:    (php-pear(%{pear_channel}/Horde_Db)            >= 2.4.0  with php-pear(%{pear_channel}/Horde_Db)            < 3)
Recommends:    (php-pear(%{pear_channel}/Horde_Kolab_Session) >= 2.0.0  with php-pear(%{pear_channel}/Horde_Kolab_Session) < 3)
Recommends:    (php-pear(%{pear_channel}/Horde_Perms)         >= 2.0.0  with php-pear(%{pear_channel}/Horde_Perms)         < 3)
%else
Requires:       php-pear(%{pear_channel}/Horde_Exception)     <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Exception)     >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Translation)   <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Translation)   >= 2.2.0
Requires:       php-pear(%{pear_channel}/Horde_Util)          <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Util)          >= 2.0.0
# Optional
Requires:       php-pear(%{pear_channel}/Horde_Auth)          <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Auth)          >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Db)            <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Db)            >= 2.4.0
Requires:       php-pear(%{pear_channel}/Horde_Kolab_Session) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Kolab_Session) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Perms)         <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Perms)         >= 2.0.0
%endif
# Optional and skiped to avoid circular dependency: Horde_Core
# Optional and implicitly required: Horde_Db, Horde_Mime, Horde_Mime

Provides:       php-pear(%{pear_channel}/%{pear_name}) = %{version}
Provides:       php-composer(horde/horde-vfs) = %{version}


%description
This package provides a Virtual File System API, with backends for:

* SQL
* FTP
* Local filesystems
* Hybrid SQL and filesystem
* Samba
* SSH2/SFTP
* IMAP (Kolab)

Reading, writing and listing of files are all supported, and there are both
object-based and array-based interfaces to directory listings.


%prep
%setup -q -c

cd %{pear_name}-%{version}

# Don't install .po and .pot files
# Remove checksum for .mo, as we regenerate them
sed -e '/%{pear_name}.po/d' \
    -e '/Horde_Other.po/d' \
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

# Locales
for loc in locale/{??,??_??}
do
    lang=$(basename $loc)
    test -d %{buildroot}%{pear_datadir}/%{pear_name}/$loc \
         && echo "%%lang(${lang%_*}) %{pear_datadir}/%{pear_name}/$loc"
done | tee ../%{pear_name}.lang


%check
%if %{with_tests}
cd %{pear_name}-%{version}/test/$(echo %{pear_name} | sed -e s:_:/:g)
# Failed asserting that file "/tmp/vfsfiletest/.horde/foo/高&执&行&力&的&打&造.txt" exists.
sed -e 's/testDeleteUnusalFileNames/SKIP_testDeleteUnusalFileNames/' \
    -i FileTest.php

ret=0
# TODO: php80
for cmd in php php72 php73 php74; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit --bootstrap bootstrap.php --verbose . || ret=1
  fi
done
exit $ret
%else
: Test disabled
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
%{_bindir}/horde-vfs
%{pear_xmldir}/%{name}.xml
%{pear_phpdir}/Horde/Vfs
%{pear_phpdir}/Horde/Vfs.php
%doc %{pear_testdir}/%{pear_name}
%dir %{pear_datadir}/%{pear_name}
%dir %{pear_datadir}/%{pear_name}/locale
%{pear_datadir}/%{pear_name}/migration


%changelog
* Wed Oct 14 2020 Remi Collet <remi@remirepo.net> - 2.4.1-1
- update to 2.4.1
- use weak and range dependencies

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb 27 2017 Remi Collet <remi@fedoraproject.org> - 2.4.0-1
- Update to 2.4.0
- raise dependency on Horde_Db 2.4.0

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Dec 04 2016 Remi Collet <remi@fedoraproject.org> - 2.3.4-1
- Update to 2.3.4

* Sun Jul 03 2016 Remi Collet <remi@fedoraproject.org> - 2.3.3-1
- Update to 2.3.3

* Mon Mar 21 2016 Remi Collet <remi@fedoraproject.org> - 2.3.2-1
- Update to 2.3.2

* Tue Feb  9 2016 Remi Collet <remi@fedoraproject.org> - 2.3.1-1
- Update to 2.3.1
- PHP 7 compatible version

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jul 31 2015 Remi Collet <remi@fedoraproject.org> - 2.3.0-1
- Update to 2.3.0

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Feb 11 2015 Remi Collet <remi@fedoraproject.org> - 2.2.2-1
- Update to 2.2.2

* Fri Jan 09 2015 Remi Collet <remi@fedoraproject.org> - 2.2.1-1
- Update to 2.2.1
- add provides php-composer(horde/horde-vfs)
- raise dependency on Horde_Translation 2.2.0

* Sun Jun 08 2014 Remi Collet <remi@fedoraproject.org> - 2.2.0-2
- fix FTBFS (include path for test)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 04 2014 Remi Collet <remi@fedoraproject.org> - 2.2.0-1
- Update to 2.2.0
- raise dependency on Horde_Db >= 2.1.0

* Mon Feb 03 2014 Remi Collet <remi@fedoraproject.org> - 2.1.2-2.1
- drop optional dependency on pecl/ssh2 not yet available in EL-6

* Sun Jan 12 2014 Remi Collet <remi@fedoraproject.org> - 2.1.2-2
- add BR Horde_Log >= 2.1.0

* Mon Oct 28 2013 Remi Collet <remi@fedoraproject.org> - 2.1.2-1
- Update to 2.1.2
- skip 1 failed test instead of ignoring test result

* Thu Jul 25 2013 Remi Collet <remi@fedoraproject.org> - 2.1.1-1
- Update to 2.1.1

* Tue May 07 2013 Remi Collet <remi@fedoraproject.org> - 2.1.0-1
- Update to 2.1.0

* Sun Feb 10 2013 Remi Collet <remi@fedoraproject.org> - 2.0.4-3
- fix shebang, https://github.com/horde/horde/pull/29

* Sun Feb 10 2013 Remi Collet <remi@fedoraproject.org> - 2.0.4-2
- cleanups for review

* Thu Jan 10 2013 Remi Collet <RPMS@FamilleCollet.com> - 2.0.4-1
- Update to 2.0.4 for remi repo
- add option for test (need investigation)

* Tue Nov 27 2012 Remi Collet <RPMS@FamilleCollet.com> - 2.0.3-1
- Update to 2.0.3 for remi repo

* Sat Nov 17 2012 Remi Collet <RPMS@FamilleCollet.com> - 2.0.2-2
- enable test

* Thu Nov 15 2012 Remi Collet <RPMS@FamilleCollet.com> - 2.0.2-1
- Update to 2.0.2 for remi repo
- disable test are a newer Horde_Test is required
  http://bugs.horde.org/ticket/11710

* Wed Nov  7 2012 Remi Collet <RPMS@FamilleCollet.com> - 2.0.1-1
- Update to 2.0.1 for remi repo

* Sat Nov  3 2012 Remi Collet <RPMS@FamilleCollet.com> - 2.0.0-1
- Update to 2.0.0 for remi repo

* Thu Jun 21 2012 Nick Bebout <nb@fedoraproject.org> - 1.0.9-1
- Upgrade to 1.0.9

* Sat Jan 28 2012 Nick Bebout <nb@fedoraproject.org> - 1.0.8-1
- Initial package

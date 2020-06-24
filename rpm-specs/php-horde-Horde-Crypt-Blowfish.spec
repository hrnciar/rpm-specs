# remirepo/fedora spec file for php-horde-Horde-Crypt-Blowfish
#
# Copyright (c) 2013-2019 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%{!?__pear:       %global __pear       %{_bindir}/pear}
%global pear_name    Horde_Crypt_Blowfish
%global pear_channel pear.horde.org

Name:           php-horde-Horde-Crypt-Blowfish
Version:        1.1.3
Release:        2%{?dist}
Summary:        Blowfish Encryption Library

License:        LGPLv2
URL:            http://pear.horde.org
Source0:        http://%{pear_channel}/get/%{pear_name}-%{version}.tgz

BuildArch:      noarch
BuildRequires:  php(language) >= 5.3.0
BuildRequires:  php-pear(PEAR) >= 1.7.0
BuildRequires:  php-hash
BuildRequires:  php-channel(%{pear_channel})
# To run unit tests
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
BuildRequires: (php-pear(%{pear_channel}/Horde_Test)      >= 2.1.0  with php-pear(%{pear_channel}/Horde_Test)      < 3)
%else
BuildRequires:  php-pear(%{pear_channel}/Horde_Test)      >= 2.1.0
%endif

Requires(post): %{__pear}
Requires(postun): %{__pear}
Requires:       php(language) >= 5.3.0
Requires:       php-hash
Requires:       php-openssl
Requires:       php-channel(%{pear_channel})
Requires:       php-pear(PEAR) >= 1.7.0
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
Requires:      (php-pear(%{pear_channel}/Horde_Exception) >= 2.0.0  with php-pear(%{pear_channel}/Horde_Exception) < 3)
Requires:      (php-pear(%{pear_channel}/Horde_Support)   >= 2.0.0  with php-pear(%{pear_channel}/Horde_Support)        < 3)
Suggests:       php-mcrypt
%else
Requires:       php-pear(%{pear_channel}/Horde_Exception) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Exception) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Support)   <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Support)   >= 2.0.0
%endif

Provides:       php-pear(%{pear_channel}/%{pear_name}) = %{version}
Provides:       php-composer(horde/horde-crypt-blowfish) = %{version}


%description
Provides blowfish encryption/decryption for PHP string data.

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
cd %{pear_name}-%{version}/test/$(echo %{pear_name} | sed -e s:_:/:g)

ret=0
for cmd in php php56 php70 php71 php72 php73 php74; do
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


%files
%doc %{pear_docdir}/%{pear_name}
%{pear_xmldir}/%{name}.xml
# dir also owned by Horde_Crypt which is not required
%dir %{pear_phpdir}/Horde/Crypt
%{pear_phpdir}/Horde/Crypt/Blowfish
%{pear_phpdir}/Horde/Crypt/Blowfish.php
%doc %{pear_testdir}/%{pear_name}


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov  4 2019 Remi Collet <remi@remirepo.net> - 1.1.3-1
- update to 1.1.3
- drop patch merged upstream

* Tue Oct  1 2019 Remi Collet <remi@fedoraproject.org> - 1.1.2-9
- add patch for PHP 7.4 from
  https://github.com/horde/Crypt_Blowfish/pull/1
- use range dependencies

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Oct  3 2017 Remi Collet <remi@fedoraproject.org> - 1.1.2-4
- php-mcrypt is optional

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Sep 02 2016 Remi Collet <remi@fedoraproject.org> - 1.1.2-1
- Update to 1.1.2

* Tue Feb 02 2016 Remi Collet <remi@fedoraproject.org> - 1.1.1-1
- Update to 1.1.1 (no change)
- PHP 7 compatible version

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 22 2015 Remi Collet <remi@fedoraproject.org> - 1.1.0-1
- Update to 1.1.0

* Thu Jan 08 2015 Remi Collet <remi@fedoraproject.org> - 1.0.3-1
- Update to 1.0.3
- add provides php-composer(horde/horde-crypt-blowfish)

* Sun Jun 08 2014 Remi Collet <remi@fedoraproject.org> - 1.0.2-4
- fix FTBFS (include path for test)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jan  9 2013 Remi Collet <RPMS@FamilleCollet.com> - 1.0.2-1
- Update to 1.0.2 for remi repo

* Thu Nov 22 2012 Remi Collet <remi@fedoraproject.org> - 1.0.1-1
- Update to 1.0.1 for remi repo (no change)

* Mon Nov 19 2012 Remi Collet <remi@fedoraproject.org> - 1.0.0-1
- Initial package

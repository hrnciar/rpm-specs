# remirepo/fedora spec file for php-horde-Horde-Mapi
#
# Copyright (c) 2014-2019 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%{!?__pear:       %global __pear       %{_bindir}/pear}
%global pear_name    Horde_Mapi
%global pear_channel pear.horde.org

Name:           php-horde-Horde-Mapi
Version:        1.0.10
Release:        3%{?dist}
Summary:        MAPI utility library

License:        LGPLv2
URL:            http://%{pear_channel}
Source0:        http://%{pear_channel}/get/%{pear_name}-%{version}.tgz

Patch0:         0001-fix-for-BigEndian.patch

BuildArch:      noarch
BuildRequires:  php(language) >= 5.3.0
BuildRequires:  php-pear(PEAR) >= 1.7.0
BuildRequires:  php-channel(%{pear_channel})
# To run unit tests
BuildRequires:  php-bcmath
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
BuildRequires: (php-pear(%{pear_channel}/Horde_Test) >= 2.1.0  with php-pear(%{pear_channel}/Horde_Test) < 3)
BuildRequires: (php-pear(%{pear_channel}/Horde_Date) >= 2.3.0  with php-pear(%{pear_channel}/Horde_Date) < 3)
%else
BuildRequires:  php-pear(%{pear_channel}/Horde_Test) >= 2.1.0
BuildRequires:  php-pear(%{pear_channel}/Horde_Date) >= 2.3.0
%endif

Requires(post): %{__pear}
Requires(postun): %{__pear}
# From package.xml, required
Requires:       php(language) >= 5.3.0
Requires:       php-pear(PEAR) >= 1.7.0
Requires:       php-channel(%{pear_channel})
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
Requires:      (php-pear(%{pear_channel}/Horde_Date)      >= 2.3.0  with php-pear(%{pear_channel}/Horde_Date)      < 3)
Requires:      (php-pear(%{pear_channel}/Horde_Exception) >= 2.0.0  with php-pear(%{pear_channel}/Horde_Exception) < 3)
%else
Requires:       php-pear(%{pear_channel}/Horde_Date) >= 2.3.0
Requires:       php-pear(%{pear_channel}/Horde_Date) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Exception) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Exception) <  3.0.0
%endif
# From phpcompatinfo report for version 1.0.0
Requires:       php-date

Provides:       php-pear(%{pear_channel}/%{pear_name}) = %{version}
Provides:       php-composer(horde/horde-mapi) = %{version}


%description
Provides various utility classes for dealing with Microsoft MAPI structured
data.


%prep
%setup -q -c

cd %{pear_name}-%{version}
%patch0 -p1 -b .temp

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
for cmd in php php56 php70 php71 php72 php73; do
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
%{pear_phpdir}/Horde/Mapi
%{pear_phpdir}/Horde/Mapi.php
%doc %{pear_testdir}/%{pear_name}


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb 18 2019 Remi Collet <remi@remirepo.net> - 1.0.10-1
- update to 1.0.10 (no change)

* Mon Feb 11 2019 Remi Collet <remi@remirepo.net> - 1.0.9-1
- update to 1.0.9
- use range dependencies
- drop dependency on Math_BigInteger
- open https://github.com/horde/Mapi/pull/2 fix for tests

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan  4 2019 Remi Collet <remi@remirepo.net> - 1.0.8-8
- cleanup for EL-8

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Nov 13 2017 Remi Collet <remi@fedoraproject.org> - 1.0.8-5
- fix erratic FTBFS from Koschei, add fix for big endian from
  https://github.com/horde/Mapi/pull/1

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec  5 2016 Remi Collet <remi@fedoraproject.org> - 1.0.8-2
- switch to php-pear(Math_BigInteger) in F26+

* Mon Mar 21 2016 Remi Collet <remi@fedoraproject.org> - 1.0.8-1
- Update to 1.0.8
- raise dependency on Horde_Date >= 2.3.0

* Mon Feb  8 2016 Remi Collet <remi@fedoraproject.org> - 1.0.6-1
- Update to 1.0.6 (no change)
- PHP 7 compatible version

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr 28 2015 Remi Collet <remi@fedoraproject.org> - 1.0.5-1
- Update to 1.0.5
- drop dependency on bcmath
- add dependency on Math_BigInteger

* Fri Jan 09 2015 Remi Collet <remi@fedoraproject.org> - 1.0.4-1
- Update to 1.0.4
- add provides php-composer(horde/horde-mapi)

* Fri Jun 27 2014 Remi Collet <remi@fedoraproject.org> - 1.0.3-1
- Update to 1.0.3

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Jan 19 2014 Remi Collet <remi@fedoraproject.org> - 1.0.2-1
- Update to 1.0.2
- License is LGPLv2, upstream clarification

* Sat Jan 18 2014 Remi Collet <remi@fedoraproject.org> - 1.0.0-1
- initial package
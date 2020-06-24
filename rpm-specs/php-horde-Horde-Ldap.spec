# remirepo/fedora spec file for php-horde-Horde-Ldap
#
# Copyright (c) 2012-2019 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%{!?__pear:       %global __pear       %{_bindir}/pear}
%global pear_name    Horde_Ldap
%global pear_channel pear.horde.org

Name:           php-horde-Horde-Ldap
Version:        2.4.2
Release:        2%{?dist}
Summary:        Horde LDAP libraries

License:        LGPLv3
URL:            http://pear.horde.org
Source0:        http://%{pear_channel}/get/%{pear_name}-%{version}.tgz

BuildArch:      noarch
BuildRequires:  php(language) >= 5.3.0
BuildRequires:  php-pear(PEAR) >= 1.7.0
BuildRequires:  php-channel(%{pear_channel})
# To run unit tests
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
BuildRequires:  php-ldap
BuildRequires: (php-pear(%{pear_channel}/Horde_Test)      >= 2.1.0  with php-pear(%{pear_channel}/Horde_Test)      < 3)
BuildRequires: (php-pear(%{pear_channel}/Horde_Exception) >= 2.0.0  with php-pear(%{pear_channel}/Horde_Exception) < 3)
BuildRequires: (php-pear(%{pear_channel}/Horde_Util)      >= 2.0.0  with php-pear(%{pear_channel}/Horde_Util)      < 3)
%else
BuildRequires:  php-pear(%{pear_channel}/Horde_Test) >= 2.1.0
%endif

Requires(post): %{__pear}
Requires(postun): %{__pear}
Requires:       php(language) >= 5.3.0
Requires:       php-ldap
Requires:       php-pcre
Requires:       php-spl
Requires:       php-pear(PEAR) >= 1.7.0
Requires:       php-channel(%{pear_channel})
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
Requires:      (php-pear(%{pear_channel}/Horde_Exception) >= 2.0.0  with php-pear(%{pear_channel}/Horde_Exception) < 3)
Requires:      (php-pear(%{pear_channel}/Horde_Util)      >= 2.0.0  with php-pear(%{pear_channel}/Horde_Util)      < 3)
%else
Requires:       php-pear(%{pear_channel}/Horde_Exception) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Exception) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Util) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Util) <  3.0.0
%endif

Provides:       php-pear(%{pear_channel}/%{pear_name}) = %{version}
Provides:       php-composer(horde/horde-ldap) = %{version}


%description
A set of classes for connecting to LDAP servers and working with directory
objects.

%prep
%setup -q -c
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
mkdir -p %{buildroot}%{pear_xmldir}
install -pm 644 %{name}.xml %{buildroot}%{pear_xmldir}


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


%files
%doc %{pear_docdir}/%{pear_name}
%{pear_xmldir}/%{name}.xml
%{pear_phpdir}/Horde/Ldap
%{pear_phpdir}/Horde/Ldap.php
%doc %{pear_testdir}/%{pear_name}


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov  4 2019 Remi Collet <remi@remirepo.net> - 2.4.2-1
- update to 2.4.2
- drop patch merged upstream

* Thu Oct 17 2019 Remi Collet <remi@remirepo.net> - 2.4.1-6
- use range dependencies
- add patch for PHP 7.4 from
  https://github.com/horde/Ldap/pull/1

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 26 2018 Remi Collet <remi@remirepo.net> - 2.4.1-1
- Update to 2.4.1

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb 27 2017 Remi Collet <remi@fedoraproject.org> - 2.4.0-1
- Update to 2.4.0

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Feb  8 2016 Remi Collet <remi@fedoraproject.org> - 2.3.2-1
- Update to 2.3.2 (no change)
- PHP 7 compatible version

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Feb 13 2015 Remi Collet <remi@fedoraproject.org> - 2.3.1-1
- Update to 2.3.1

* Wed Feb 11 2015 Remi Collet <remi@fedoraproject.org> - 2.3.0-1
- Update to 2.3.0
- add provides php-composer(horde/horde-ldap)

* Tue Jun 17 2014 Remi Collet <remi@fedoraproject.org> - 2.2.0-1
- Update to 2.2.0

* Tue Jun 10 2014 Remi Collet <remi@fedoraproject.org> - 2.1.0-1
- Update to 2.1.0

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Jun 03 2014 Remi Collet <remi@fedoraproject.org> - 2.0.6-1
- Update to 2.0.6 (security)

* Thu May 22 2014 Remi Collet <remi@fedoraproject.org> - 2.0.5-1
- Update to 2.0.5

* Fri Apr 04 2014 Remi Collet <remi@fedoraproject.org> - 2.0.4-1
- Update to 2.0.4

* Mon Oct 28 2013 Remi Collet <remi@fedoraproject.org> - 2.0.3-1
- Update to 2.0.3

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jan 29 2013 Remi Collet <remi@fedoraproject.org> - 2.0.2-1
- Update to 2.0.2

* Mon Nov 19 2012 Remi Collet <remi@fedoraproject.org> - 2.0.1-1
- Update to 2.0.1

* Thu Nov  8 2012 Remi Collet <remi@fedoraproject.org> - 2.0.0-1
- initial package

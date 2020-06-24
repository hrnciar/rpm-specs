# remirepo/fedora spec file for php-horde-Horde-Kolab-Server
#
# Copyright (c) 2012-2017 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%{!?__pear:       %global __pear       %{_bindir}/pear}
%global pear_name    Horde_Kolab_Server
%global pear_channel pear.horde.org

Name:           php-horde-Horde-Kolab-Server
Version:        2.0.5
Release:        9%{?dist}
Summary:        A package for manipulating the Kolab user database

License:        LGPLv2
URL:            http://%{pear_channel}/
Source0:        http://%{pear_channel}/get/%{pear_name}-%{version}.tgz

Patch0:         https://github.com/horde/Kolab_Server/commit/5efb632b7a3a2fa76cf3ee76df650f1f2317a206.patch

BuildArch:      noarch
BuildRequires:  php-pear(PEAR) >= 1.7.0
BuildRequires:  php-channel(%{pear_channel})
# To run unit tests
BuildRequires:  php-pear(%{pear_channel}/Horde_Test) >= 2.4.0
BuildRequires:  php-pear(pear.phpunit.de/PHPUnit_Story)

Requires(post): %{__pear}
Requires(postun): %{__pear}
Requires:       php-pear(PEAR) >= 1.7.0
Requires:       php-pcre
Requires:       php-hash
Requires:       php-channel(%{pear_channel})
Requires:       php-pear(%{pear_channel}/Horde_Auth) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Auth) < 3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Exception) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Exception) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Util) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Util) <  3.0.0
# optional and implicitly required: Horde_Date, Horde_Ldap

Provides:       php-pear(%{pear_channel}/%{pear_name}) = %{version}
Provides:       php-composer(horde/horde-kolab-server) = %{version}


%description
This package reads/writes entries in the Kolab user database stored in LDAP.


%prep
%setup -q -c
cd %{pear_name}-%{version}
%patch0 -p1 -b .upstream

sed -e '/Changes.php/s/md5sum=.*name=/name=/' \
    ../package.xml >%{name}.xml
touch -r ../package.xml %{name}.xml


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
for cmd in php php56 php70 php71 php72; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit . || ret=1
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
%dir %{pear_phpdir}/Horde/Kolab
%{pear_phpdir}/Horde/Kolab/Server
%doc %{pear_testdir}/%{pear_name}


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Oct 12 2017 Remi Collet <remi@remirepo.net> - 2.1.4-1
- add upstream patch for PHP 7.2, FTBFS from Koschei

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Feb  8 2016 Remi Collet <remi@fedoraproject.org> - 2.0.5-1
- Update to 2.0.5 (no change)
- PHP 7 compatible version

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr 28 2015 Remi Collet <remi@fedoraproject.org> - 2.0.4-1
- Update to 2.0.4
- add dependency on Horde_Util
- add provides php-composer(horde/horde-kolab-server)

* Wed Jan 07 2015 Remi Collet <remi@fedoraproject.org> - 2.0.3-1
- Update to 2.0.3
- raise dependency on Horde_Test 2.4.0

* Sun Jun 08 2014 Remi Collet <remi@fedoraproject.org> - 2.0.2-2
- fix FTBFS (include path for test)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Mar 28 2013 Remi Collet <remi@fedoraproject.org> - 2.0.2-1
- initial package
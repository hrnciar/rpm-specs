# remirepo/fedora spec file for php-horde-Horde-Serialize
#
# Copyright (c) 2012-2019 Nick Bebout, Remi Collet
#
# License: MIT
# https://fedoraproject.org/wiki/Licensing:MIT#Modern_Style_with_sublicense
#
# Please, preserve the changelog entries
#
%{!?__pear:       %global __pear       %{_bindir}/pear}
%global pear_name    Horde_Serialize
%global pear_channel pear.horde.org

Name:           php-horde-Horde-Serialize
Version:        2.0.5
Release:        10%{?dist}
Summary:        Data Encapulation API

License:        LGPLv2
URL:            http://pear.horde.org
Source0:        http://%{pear_channel}/get/%{pear_name}-%{version}.tgz

BuildArch:      noarch
BuildRequires:  php(language) >= 5.3.0
BuildRequires:  php-pear
BuildRequires:  php-channel(%{pear_channel})
# To run unit tests
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
BuildRequires: (php-pear(%{pear_channel}/Horde_Test)        >= 2.1.0  with php-pear(%{pear_channel}/Horde_Test)        < 3)
%else
BuildRequires:  php-pear(%{pear_channel}/Horde_Test) >= 2.1.0
%endif

Requires(post): %{__pear}
Requires(postun): %{__pear}
Requires:       php(language) >= 5.3.0
Requires:       php-channel(%{pear_channel})
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
Requires:      (php-pear(%{pear_channel}/Horde_Exception)   >= 2.0.0  with php-pear(%{pear_channel}/Horde_Exception)   <  3)
Requires:      (php-pear(%{pear_channel}/Horde_Util)        >= 2.0.0  with php-pear(%{pear_channel}/Horde_Util)        <  3)
Recommends:    (php-pear(%{pear_channel}/Horde_Imap_Client) >= 2.0.0  with php-pear(%{pear_channel}/Horde_Imap_Client) <  3)
Recommends:    (php-pear(%{pear_channel}/Horde_Mime)        >= 2.0.0  with php-pear(%{pear_channel}/Horde_Mime)        <  3)
# Always there
Recommends:     php-bz2
Recommends:     php-json
Recommends:     php-zlib
# only suggested as removed in 7.4
Suggests:       php-wddx
Suggests:       php-lzf
%else
Requires:       php-pear(%{pear_channel}/Horde_Exception) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Exception) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Util) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Util) <  3.0.0
Requires:       php-bz2
Requires:       php-json
Requires:       php-wddx
Requires:       php-zlib
Requires:       php-pecl(LZF)
# Optional and skipped for build order: Horde_Imap_Client, Horde_Mime
%endif

Provides:       php-pear(%{pear_channel}/%{pear_name}) = %{version}
Provides:       php-composer(horde/horde-serialize) = %{version}


%description
The Horde_Serialize library provides various methods of encapsulating data.


%prep
%setup -q -c

cd %{pear_name}-%{version}
cp ../package.xml %{name}.xml


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
for cmd in php php70 php71 php72 php73; do
  if which $cmd; then
    if %{_bindir}/phpunit --atleast-version 4.8; then
      $cmd %{_bindir}/phpunit --verbose . || ret=1
    else
     : PHPUnit is too old for this package
    fi
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
%{pear_phpdir}/Horde/Serialize
%{pear_phpdir}/Horde/Serialize.php
%doc %{pear_testdir}/%{pear_name}


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Mar 20 2019 Remi Collet <remi@fedoraproject.org> - 2.0.5-7
- use range dependencies
- use weak dependencies, drop dependency on wddx

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Feb  8 2016 Remi Collet <remi@fedoraproject.org> - 2.0.5-1
- Update to 2.0.5 (no change)
- PHP 7 compatible version

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jul 31 2015 Remi Collet <remi@fedoraproject.org> - 2.0.4-1
- Update to 2.0.4 (no change)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jan 09 2015 Remi Collet <remi@fedoraproject.org> - 2.0.3-1
- Update to 2.0.3
- add provides php-composer(horde/horde-serialize)

* Sun Jun 08 2014 Remi Collet <remi@fedoraproject.org> - 2.0.2-4
- fix FTBFS (include path for test)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Aug  5 2013 Remi Collet <remi@fedoraproject.org> - 2.0.2-3
- ignore testJsonEncodeAndDecode for now

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Mar 06 2013 Remi Collet <remi@fedoraproject.org> - 2.0.2-1
- Update to 2.0.2

* Wed Feb 6 2013 Nick Bebout <nb@fedoraproject.org> - 2.0.1-3
- Update for review

* Tue Feb 5 2013 Nick Bebout <nb@fedoraproject.org> - 2.0.1-2
- Use php-common instead of php(language), Remove BuildRoot

* Mon Nov 19 2012 Remi Collet <remi@fedoraproject.org> - 2.0.1-1
- Update to 2.0.1

* Thu Nov  1 2012 Remi Collet <remi@fedoraproject.org> - 2.0.0-1
- Update to 2.0.0

* Sat Jan 28 2012 Nick Bebout <nb@fedoraproject.org> - 1.0.2-1
- Initial package

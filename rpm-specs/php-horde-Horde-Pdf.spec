# remirepo/fedora spec file for php-horde-Horde-Pdf
#
# Copyright (c) 2014-2018 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%{!?__pear:       %global __pear       %{_bindir}/pear}
%global pear_name    Horde_Pdf
%global pear_channel pear.horde.org
%global with_tests   %{?_without_tests:0}%{!?_without_tests:1}

Name:           php-horde-Horde-Pdf
Version:        2.0.8
Release:        2%{?dist}
Summary:        Horde PDF library

License:        LGPLv2
URL:            http://%{pear_channel}
Source0:        http://%{pear_channel}/get/%{pear_name}-%{version}.tgz

BuildArch:      noarch
BuildRequires:  php(language) >= 5.3.0
BuildRequires:  php-pear(PEAR) >= 1.7.0
BuildRequires:  php-channel(%{pear_channel})
%if %{with_tests}
# To run unit tests
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
BuildRequires: (php-pear(%{pear_channel}/Horde_Test)      >= 2.1.0  with php-pear(%{pear_channel}/Horde_Test)      < 3)
BuildRequires: (php-pear(%{pear_channel}/Horde_Exception) >= 2.0.0  with php-pear(%{pear_channel}/Horde_Exception) < 3)
BuildRequires: (php-pear(%{pear_channel}/Horde_Util)      >= 2.0.0  with php-pear(%{pear_channel}/Horde_Util)      < 3)
%else
BuildRequires:  php-pear(%{pear_channel}/Horde_Test) >= 2.1.0
%endif
%endif

Requires(post): %{__pear}
Requires(postun): %{__pear}
# From package.xml, required
Requires:       php(language) >= 5.3.0
Requires:       php-pear(PEAR) >= 1.7.0
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
Requires:      (php-pear(%{pear_channel}/Horde_Exception) >= 2.0.0  with php-pear(%{pear_channel}/Horde_Exception) < 3)
Requires:      (php-pear(%{pear_channel}/Horde_Util)      >= 2.0.0  with php-pear(%{pear_channel}/Horde_Util)      < 3)
%else
Requires:       php-pear(%{pear_channel}/Horde_Exception) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Exception) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Util) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Util) <  3.0.0
%endif
Requires:       php-channel(%{pear_channel})
# From phpcompatinfo report for version 2.0.3
Requires:       php-date
Requires:       php-zlib

Provides:       php-pear(%{pear_channel}/%{pear_name}) = %{version}
Provides:       php-composer(horde/horde-pdf) = %{version}


%description
PDF generation using only PHP, without requiring any external libraries.


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
%if %{with_tests}
cd %{pear_name}-%{version}/test/$(echo %{pear_name} | sed -e s:_:/:g)

ret=0
for cmd in php php71 php72 php73 php74; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit --bootstrap bootstrap.php --verbose . || ret=1
  fi
done
exit $ret
%else
: Test disabled, missing '--with tests' option.
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
%{pear_phpdir}/Horde/Pdf
%doc %{pear_testdir}/%{pear_name}


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov  4 2019 Remi Collet <remi@remirepo.net> - 2.0.8-1
- update to 2.0.8
- drop patch merged upstream

* Thu Oct 17 2019 Remi Collet <remi@remirepo.net> - 2.0.7-8
- add patch for PHP 7.4 from
  https://github.com/horde/Pdf/pull/1
- use range dependencies

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Feb  8 2016 Remi Collet <remi@fedoraproject.org> - 2.0.7-1
- Update to 2.0.7 (no change)
- PHP 7 compatible version

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Oct 21 2015 Remi Collet <remi@fedoraproject.org> - 2.0.6-1
- Update to 2.0.6

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr 28 2015 Remi Collet <remi@fedoraproject.org> - 2.0.5-1
- Update to 2.0.5
- add dependency on Horde_Util

* Fri Jan 09 2015 Remi Collet <remi@fedoraproject.org> - 2.0.4-1
- Update to 2.0.4
- add provides php-composer(horde/horde-pdf)

* Sun Sep 14 2014 Remi Collet <remi@fedoraproject.org> - 2.0.3-1
- initial package
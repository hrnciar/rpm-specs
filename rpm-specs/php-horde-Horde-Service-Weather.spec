# remirepo/fedora spec file for php-horde-Horde-Service-Weather
#
# Copyright (c) 2012-2019 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%{!?__pear:       %global __pear       %{_bindir}/pear}
%global pear_name    Horde_Service_Weather
%global pear_channel pear.horde.org

Name:           php-horde-Horde-Service-Weather
Version:        2.5.4
Release:        8%{?dist}
Summary:        Horde Weather Provider

License:        BSD
URL:            http://%{pear_channel}
Source0:        http://%{pear_channel}/get/%{pear_name}-%{version}.tgz

Patch0:         https://patch-diff.githubusercontent.com/raw/horde/Service_Weather/pull/1.patch

BuildArch:      noarch
BuildRequires:  gettext
BuildRequires:  php(language) >= 5.3.0
BuildRequires:  php-pear(PEAR)
BuildRequires:  php-channel(%{pear_channel})
BuildRequires:  php-pear(%{pear_channel}/Horde_Role) >= 1.0.0
# To run unit tests
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
BuildRequires: (php-pear(%{pear_channel}/Horde_Date)        >= 2.0.0 with php-pear(%{pear_channel}/Horde_Date)        < 3)
BuildRequires: (php-pear(%{pear_channel}/Horde_Exception)   >= 2.0.0 with php-pear(%{pear_channel}/Horde_Exception)   < 3)
BuildRequires: (php-pear(%{pear_channel}/Horde_Http)        >= 2.0.0 with php-pear(%{pear_channel}/Horde_Http)        < 3)
BuildRequires: (php-pear(%{pear_channel}/Horde_Translation) >= 2.2.0 with php-pear(%{pear_channel}/Horde_Translation) < 3)
BuildRequires: (php-pear(%{pear_channel}/Horde_Url)         >= 2.0.0 with php-pear(%{pear_channel}/Horde_Url)         < 3)
BuildRequires: (php-pear(%{pear_channel}/Horde_Serialize)   >= 2.0.0 with php-pear(%{pear_channel}/Horde_Serialize)   < 3)
BuildRequires: (php-pear(%{pear_channel}/Horde_Test)        >= 2.1.0 with php-pear(%{pear_channel}/Horde_Test)        < 3)
%else
BuildRequires:  php-pear(%{pear_channel}/Horde_Date) >= 2.0.0
BuildRequires:  php-pear(%{pear_channel}/Horde_Http) >= 2.0.0
BuildRequires:  php-pear(%{pear_channel}/Horde_Serialize) >= 2.0.0
BuildRequires:  php-pear(%{pear_channel}/Horde_Test) >= 2.1.0
BuildRequires:  php-pear(%{pear_channel}/Horde_Url) >= 2.0.0
%endif

Requires(post): %{__pear}
Requires(postun): %{__pear}
Requires:       php(language) >= 5.3.0
Requires:       php-cli
Requires:       php-date
Requires:       php-gettext
Requires:       php-spl
Requires:       php-pear(PEAR) >= 1.7.0
Requires:       php-channel(%{pear_channel})
Requires:       php-pear(%{pear_channel}/Horde_Role) >= 1.0.0
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
Requires:      (php-pear(%{pear_channel}/Horde_Date)        >= 2.0.0 with php-pear(%{pear_channel}/Horde_Date)        < 3)
Requires:      (php-pear(%{pear_channel}/Horde_Exception)   >= 2.0.0 with php-pear(%{pear_channel}/Horde_Exception)   < 3)
Requires:      (php-pear(%{pear_channel}/Horde_Http)        >= 2.0.0 with php-pear(%{pear_channel}/Horde_Http)        < 3)
Requires:      (php-pear(%{pear_channel}/Horde_Translation) >= 2.2.0 with php-pear(%{pear_channel}/Horde_Translation) < 3)
Requires:      (php-pear(%{pear_channel}/Horde_Url)         >= 2.0.0 with php-pear(%{pear_channel}/Horde_Url)         < 3)
# Not documented, detected by phpci
Requires:      (php-pear(%{pear_channel}/Horde_Serialize)   >= 2.0.0 with php-pear(%{pear_channel}/Horde_Serialize)   < 3)
%else
Requires:       php-pear(%{pear_channel}/Horde_Date) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Date) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Exception) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Exception) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Http) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Http) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Translation) >= 2.2.0
Requires:       php-pear(%{pear_channel}/Horde_Translation) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Url) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Url) <  3.0.0
# Not documented, detected by phpci
Requires:       php-pear(%{pear_channel}/Horde_Serialize) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Serialize) <  3.0.0
%endif

Provides:       php-pear(%{pear_channel}/%{pear_name}) = %{version}
Provides:       php-composer(horde/horde-service-weather) = %{version}


%description
Set of classes that provide an abstraction to various online weather
service providers. Includes drivers for WeatherUnderground,
WorldWeatherOnline, and Google Weather.


%prep
%setup -q -c

cd %{pear_name}-%{version}
%patch0 -p1 -b .pr1

# Don't install .po and .pot files
# Remove checksum for .mo, as we regenerate them
sed -e '/%{pear_name}.po/d' \
    -e '/Horde_Other.po/d' \
    -e '/%{pear_name}.mo/s/md5sum="[^"]*"//' \
    -e '/.php/s/md5sum="[^"]*"//' \
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
%dir %{pear_phpdir}/Horde/Service
%{pear_phpdir}/Horde/Service/Weather
%{pear_phpdir}/Horde/Service/Weather.php
%dir %{pear_datadir}/%{pear_name}
%dir %{pear_datadir}/%{pear_name}/locale
     %{pear_datadir}/%{pear_name}/migration
%doc %{pear_testdir}/%{pear_name}
%{pear_hordedir}/themes
%{_bindir}/horde-service-weather-metar-database


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 18 2019 Remi Collet <remi@fedoraproject.org> - 2.5.4-7
- Fix FTBFS from Koschei, add patch for PHP 7.4 from
  https://github.com/horde/Service_Weather/pull/1
- use range dependencies

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb 27 2017 Remi Collet <remi@fedoraproject.org> - 2.5.4-1
- Update to 2.5.4

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Dec 11 2016 Remi Collet <remi@fedoraproject.org> - 2.5.3-1
- Update to 2.5.3
- add horde-service-weather-metar-database command

* Thu Nov 10 2016 Remi Collet <remi@fedoraproject.org> - 2.5.2-1
- Update to 2.5.2

* Thu Nov 10 2016 Remi Collet <remi@fedoraproject.org> - 2.5.1-1
- Update to 2.5.1

* Sun Nov 06 2016 Remi Collet <remi@fedoraproject.org> - 2.5.0-1
- Update to 2.5.0

* Thu Nov 03 2016 Remi Collet <remi@fedoraproject.org> - 2.4.1-1
- Update to 2.4.1

* Fri Sep 02 2016 Remi Collet <remi@fedoraproject.org> - 2.4.0-1
- Update to 2.4.0

* Sat Jul 02 2016 Remi Collet <remi@fedoraproject.org> - 2.3.4-1
- Update to 2.3.4

* Wed Mar 16 2016 Remi Collet <remi@fedoraproject.org> - 2.3.3-1
- Update to 2.3.3

* Mon Feb  8 2016 Remi Collet <remi@fedoraproject.org> - 2.3.2-1
- Update to 2.3.2
- PHP 7 compatible version

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Dec 04 2015 Remi Collet <remi@fedoraproject.org> - 2.3.1-1
- Update to 2.3.1

* Wed Oct 21 2015 Remi Collet <remi@fedoraproject.org> - 2.3.0-1
- Update to 2.3.0

* Sun Aug 30 2015 Remi Collet <remi@fedoraproject.org> - 2.2.0-1
- Update to 2.2.0

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Mar 04 2015 Remi Collet <remi@fedoraproject.org> - 2.1.6-1
- Update to 2.1.6

* Fri Jan 09 2015 Remi Collet <remi@fedoraproject.org> - 2.1.5-1
- Update to 2.1.5
- add dependency on Horde_Translation 2.2.0
- add provides php-composer(horde/horde-service-weather)

* Sun Oct 12 2014 Remi Collet <remi@fedoraproject.org> - 2.1.4-1
- Update to 2.1.4

* Mon Jul 07 2014 Remi Collet <remi@fedoraproject.org> - 2.1.3-1
- Update to 2.1.3

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 22 2014 Remi Collet <remi@fedoraproject.org> - 2.1.1-1
- Update to 2.1.1

* Mon May 19 2014 Remi Collet <remi@fedoraproject.org> - 2.1.0-1
- Update to 2.1.0

* Mon May 27 2013 Remi Collet <remi@fedoraproject.org> - 2.0.5-1
- Update to 2.0.5
- switch from Conflicts >= max to Requires < max

* Sat Apr  6 2013 Remi Collet <remi@fedoraproject.org> - 2.0.4-1
- initial package

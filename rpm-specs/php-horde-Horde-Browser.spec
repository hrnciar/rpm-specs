# remirepo/fedora spec file for php-horde-Horde-Browser
#
# Copyright (c) 2012-2018 Nick Bebout, Remi Collet
#
# License: MIT
# https://fedoraproject.org/wiki/Licensing:MIT#Modern_Style_with_sublicense
#
# Please, preserve the changelog entries
#
%{!?__pear:       %global __pear       %{_bindir}/pear}
%global pear_name    Horde_Browser
%global pear_channel pear.horde.org

Name:           php-horde-Horde-Browser
Version:        2.0.16
Release:        5%{?dist}
Summary:        Horde Browser API

License:        LGPLv2+
URL:            http://pear.horde.org
Source0:        http://%{pear_channel}/get/%{pear_name}-%{version}.tgz

BuildArch:      noarch
BuildRequires:  php-pear(PEAR) >= 1.7.0
BuildRequires:  php-channel(%{pear_channel})
BuildRequires:  gettext

Requires(post): %{__pear}
Requires(postun): %{__pear}
Requires:       php(language) >= 5.3.0
Requires:       php-pcre
Requires:       php-pear(PEAR) >= 1.7.0
Requires:       php-channel(%{pear_channel})
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
Requires:      (php-pear(%{pear_channel}/Horde_Exception)   >= 2.0.0  with php-pear(%{pear_channel}/Horde_Exception)   < 3.0.0)
Requires:      (php-pear(%{pear_channel}/Horde_Translation) >= 2.2.0  with php-pear(%{pear_channel}/Horde_Translation) < 3.0.0)
Requires:      (php-pear(%{pear_channel}/Horde_Util)        >= 2.0.0  with php-pear(%{pear_channel}/Horde_Util)        < 3.0.0)
%else
Requires:       php-pear(%{pear_channel}/Horde_Exception) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Exception) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Translation) >= 2.2.0
Requires:       php-pear(%{pear_channel}/Horde_Translation) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Util) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Util) <  3.0.0
%endif

Provides:       php-pear(%{pear_channel}/%{pear_name}) = %{version}
Provides:       php-composer(horde/horde-browser) = %{version}


%description
The Horde_Browser class provides an API for getting information about the
current user's browser and its capabilities.


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
%{pear_phpdir}/Horde/Browser
%{pear_phpdir}/Horde/Browser.php
%dir %{pear_datadir}/%{pear_name}
%dir %{pear_datadir}/%{pear_name}/locale


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Dec 28 2018 Remi Collet <remi@remirepo.net> - 2.0.16-1
- update to 2.0.16
- use range dependencies

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Sep 19 2017 Remi Collet <remi@remirepo.net> - 2.0.15-1
- Update to 2.0.15 (no change)

* Tue Aug  1 2017 Remi Collet <remi@remirepo.net> - 2.0.14-1
- Update to 2.0.14

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 20 2016 Remi Collet <remi@fedoraproject.org> - 2.0.13-1
- Update to 2.0.13

* Mon Mar 21 2016 Remi Collet <remi@fedoraproject.org> - 2.0.12-1
- Update to 2.0.12

* Mon Feb 01 2016 Remi Collet <remi@fedoraproject.org> - 2.0.11-1
- Update to 2.0.11

* Fri Jul 31 2015 Remi Collet <remi@fedoraproject.org> - 2.0.10-1
- Update to 2.0.10

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr 28 2015 Remi Collet <remi@fedoraproject.org> - 2.0.9-1
- Update to 2.0.9
- add provides php-composer(horde/horde-browser)

* Tue Nov 18 2014 Remi Collet <remi@fedoraproject.org> - 2.0.8-1
- Update to 2.0.8
- add dependency on Horde_Translation

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May 03 2014 Remi Collet <remi@fedoraproject.org> - 2.0.7-1
- Update to 2.0.7

* Tue Mar 18 2014 Remi Collet <remi@fedoraproject.org> - 2.0.6-1
- Update to 2.0.6

* Tue Mar 04 2014 Remi Collet <remi@fedoraproject.org> - 2.0.5-1
- Update to 2.0.5

* Tue Aug 27 2013 Remi Collet <remi@fedoraproject.org> - 2.0.4-1
- Update to 2.0.4

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 11 2013 Remi Collet <remi@fedoraproject.org> - 2.0.3-1
- Update to 2.0.3
- fix files listed twice

* Wed Dec 12 2012 Nick Bebout <nb@fedoraproject.org> - 2.0.2-1
- Upgrade to 2.0.2

* Thu Jun 21 2012 Nick Bebout <nb@fedoraproject.org> - 1.0.7-1
- Upgrade to 1.0.7

* Sat Jan 28 2012 Nick Bebout <nb@fedoraproject.org> - 1.0.5-1
- Initial package

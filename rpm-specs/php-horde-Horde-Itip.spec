# remirepo/fedora spec file for php-horde-Horde-Itip
#
# Copyright (c) 2012-2016 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%{!?pear_metadir: %global pear_metadir %{pear_phpdir}}
%{!?__pear:       %global __pear       %{_bindir}/pear}
%global pear_name    Horde_Itip
%global pear_channel pear.horde.org

Name:           php-horde-Horde-Itip
Version:        2.1.2
Release:        8%{?dist}
Summary:        iTip invitation response handling

License:        LGPLv2
URL:            http://pear.horde.org
Source0:        http://%{pear_channel}/get/%{pear_name}-%{version}.tgz

BuildArch:      noarch
BuildRequires:  php(language) >= 5.3.0
BuildRequires:  php-pear(PEAR) >= 1.7.0
BuildRequires:  php-channel(%{pear_channel})
BuildRequires:  gettext
# To run unit tests
BuildRequires:  php-pear(%{pear_channel}/Horde_Test) >= 2.1.0
BuildRequires:  php-pear(%{pear_channel}/Horde_Icalendar) >= 2.0.0

Requires(post): %{__pear}
Requires(postun): %{__pear}
Requires:       php(language) >= 5.3.0
Requires:       php-date
Requires:       php-pcre
Requires:       php-pear(PEAR) >= 1.7.0
Requires:       php-channel(%{pear_channel})
Requires:       php-pear(%{pear_channel}/Horde_Icalendar) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Icalendar) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Mime) >= 2.5.0
Requires:       php-pear(%{pear_channel}/Horde_Mime) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Translation) >= 2.2.0
Requires:       php-pear(%{pear_channel}/Horde_Translation) <  3.0.0
# Optional
Requires:       php-pear(%{pear_channel}/Horde_Prefs) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Prefs) <  3.0.0

Provides:       php-pear(%{pear_channel}/%{pear_name}) = %{version}
Provides:       php-composer(horde/horde-itip) = %{version}


%description
This package to generates MIME encapsuled responses to iCalendar
invitations.


%prep
%setup -q -c
cd %{pear_name}-%{version}

# Don't install .po and .pot files
# Remove checksum for .mo, as we regenerate them
sed -e '/%{pear_name}.po/d' \
    -e '/Horde_Other.po/d' \
    -e '/%{pear_name}.mo/s/md5sum=.*name=/name=/' \
    ../package.xml >%{name}.xml


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

for loc in locale/{??,??_??}
do
    lang=$(basename $loc)
    test -d $loc && echo "%%lang(${lang%_*}) %{pear_datadir}/%{pear_name}/$loc"
done | tee ../%{pear_name}.lang


%check
cd %{pear_name}-%{version}/test/$(echo %{pear_name} | sed -e s:_:/:g)
%{_bindir}/phpunit .

if which php70; then
   php70 %{_bindir}/phpunit .
fi


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
%{pear_phpdir}/Horde/Itip
%{pear_phpdir}/Horde/Itip.php
%{pear_testdir}/%{pear_name}
%dir %{pear_datadir}/%{pear_name}
%dir %{pear_datadir}/%{pear_name}/locale


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Mar 21 2016 Remi Collet <remi@fedoraproject.org> - 2.1.2-1
- Update to 2.1.2

* Mon Feb  8 2016 Remi Collet <remi@fedoraproject.org> - 2.1.1-1
- Update to 2.1.1
- PHP 7 compatible version

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr 14 2015 Remi Collet <remi@fedoraproject.org> - 2.1.0-1
- Update to 2.1.0

* Fri Jan 09 2015 Remi Collet <remi@fedoraproject.org> - 2.0.7-1
- Update to 2.0.7
- add provides php-composer(horde/horde-itip)
- add dependency on Horde_Translation 2.2.0
- raise dependency on Horde_Mime 2.5.0

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 22 2014 Remi Collet <remi@fedoraproject.org> - 2.0.6-1
- Update to 2.0.6

* Fri May 31 2013 Remi Collet <remi@fedoraproject.org> - 2.0.5-1
- Update to 2.0.5
- switch from Conflicts to Requires

* Tue Feb 12 2013 Remi Collet <remi@fedoraproject.org> - 2.0.4-1
- Update to 2.0.4
- run test during build

* Tue Jan 29 2013 Remi Collet <remi@fedoraproject.org> - 2.0.3-1
- Update to 2.0.3

* Wed Jan  9 2013 Remi Collet <remi@fedoraproject.org> - 2.0.2-1
- Update to 2.0.2
- use local script instead of find_lang
- new test layout (requires Horde_Test 2.1.0)
- add option for test (need investigation)

* Fri Nov  9 2012 Remi Collet <remi@fedoraproject.org> - 2.0.1-1
- Update to 2.0.1

* Sat Nov  3 2012 Remi Collet <remi@fedoraproject.org> - 2.0.0-1
- Update to 2.0.0

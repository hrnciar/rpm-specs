# remirepo/fedora spec file for php-horde-Horde-Text-Filter
#
# Copyright (c) 2012-2018 Nick Bebout, Remi Collet
#
# License: MIT
# https://fedoraproject.org/wiki/Licensing:MIT#Modern_Style_with_sublicense
#
# Please, preserve the changelog entries
#
%{!?__pear:       %global __pear       %{_bindir}/pear}
%global pear_name    Horde_Text_Filter
%global pear_channel pear.horde.org

Name:           php-horde-Horde-Text-Filter
Version:        2.3.6
Release:        5%{?dist}
Summary:        Horde Text Filter API

License:        LGPLv2
URL:            http://%{pear_channel}/
Source0:        http://%{pear_channel}/get/%{pear_name}-%{version}.tgz

BuildArch:      noarch
BuildRequires:  php(language) >= 5.3.0
BuildRequires:  php-pear(PEAR) >= 1.7.0
BuildRequires:  php-channel(%{pear_channel})
BuildRequires:  gettext
# To run unit tests
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
BuildRequires: (php-pear(%{pear_channel}/Horde_Test)        >= 2.1.0  with php-pear(%{pear_channel}/Horde_Test)        < 3)
BuildRequires: (php-pear(%{pear_channel}/Horde_Text_Flowed) >= 2.0.0  with php-pear(%{pear_channel}/Horde_Text_Flowed) < 3)
BuildRequires: (php-pear(%{pear_channel}/Horde_Idna)        >= 1.0.0  with php-pear(%{pear_channel}/Horde_Idna)        < 2)
%else
BuildRequires:  php-pear(%{pear_channel}/Horde_Test) >= 2.1.0
BuildRequires:  php-pear(%{pear_channel}/Horde_Text_Flowed) >= 2.0.0
BuildRequires:  php-pear(%{pear_channel}/Horde_Idna) >= 1.0.0
%endif

Requires(post): %{__pear}
Requires(postun): %{__pear}
# From package.xml
Requires:       php(language) >= 5.3.0
Requires:       php-pear(PEAR) >= 1.7.0
Requires:       php-channel(%{pear_channel})
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
Requires:      (php-pear(%{pear_channel}/Horde_Exception)   >= 2.0.0  with php-pear(%{pear_channel}/Horde_Exception)  < 3)
Requires:      (php-pear(%{pear_channel}/Horde_Idna)        >= 1.0.0  with php-pear(%{pear_channel}/Horde_Idna)       < 2)
Requires:      (php-pear(%{pear_channel}/Horde_Util)        >= 2.0.0  with php-pear(%{pear_channel}/Horde_Util)       < 3)
# Optional
Recommends:     php-tidy
Recommends:    (php-pear(%{pear_channel}/Horde_Text_Flowed) >= 2.0.0 with php-pear(%{pear_channel}/Horde_Text_Flowed) < 3)
%else
Requires:       php-pear(%{pear_channel}/Horde_Exception) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Exception) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Idna) >= 1.0.0
Requires:       php-pear(%{pear_channel}/Horde_Idna) <  2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Util) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Util) <  3.0.0
# Optional
Requires:       php-tidy
Requires:       php-pear(%{pear_channel}/Horde_Text_Flowed) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Text_Flowed) <  3.0.0
%endif
# From phpcompatinfo report for version 2.2.0
Requires:       php-dom
Requires:       php-pcre
# Optional and implicitly required: Horde_Translation
# Optional but non-free: Horde_Text_Filter_Jsmin

Provides:       php-pear(%{pear_channel}/%{pear_name}) = %{version}
Provides:       php-composer(horde/horde-text-filter) = %{version}


%description
Common methods for fitering and converting text.

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
cd %{pear_name}-%{version}/test/$(echo %{pear_name} | sed -e s:_:/:g)


%if 0%{?rhel} == 6
# Only fails with PHP < 5.3.6, see http://3v4l.org/Vkcdu
sed -e 's/testLinkurls/SKIP_testLinkurls/' \
    -i LinkurlsTest.php
sed -e 's/testMsoNormalCss/SKIP_testMsoNormalCss/' \
    -i MsofficeTest.php
%endif

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


%files -f %{pear_name}.lang
%doc %{pear_docdir}/%{pear_name}
%{pear_xmldir}/%{name}.xml
%{pear_phpdir}/Horde/Text/Filter
%{pear_phpdir}/Horde/Text/Filter.php
%doc %{pear_testdir}/%{pear_name}
%dir %{pear_datadir}/%{pear_name}
%dir %{pear_datadir}/%{pear_name}/locale


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 31 2018 Remi Collet <remi@remirepo.net> - 2.3.6-1
- update to 2.3.6
- drop patch merged upstream
- use range dependencies

* Mon Oct 15 2018 Remi Collet <remi@fedoraproject.org> - 2.3.5-6
- add patch for PHP 7.3 from https://github.com/horde/Text_Filter/pull/1

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Sep 07 2016 Remi Collet <remi@fedoraproject.org> - 2.3.5-1
- Update to 2.3.5

* Mon Mar 21 2016 Remi Collet <remi@fedoraproject.org> - 2.3.4-1
- Update to 2.3.4

* Mon Feb  8 2016 Remi Collet <remi@fedoraproject.org> - 2.3.3-1
- Update to 2.3.3 (no change)
- PHP 7 compatible version

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jul 31 2015 Remi Collet <remi@fedoraproject.org> - 2.3.2-1
- Update to 2.3.2 (no change)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr 28 2015 Remi Collet <remi@fedoraproject.org> - 2.3.1-1
- Update to 2.3.1

* Fri Apr 03 2015 Remi Collet <remi@fedoraproject.org> - 2.3.0-1
- Update to 2.3.0

* Fri Jan 09 2015 Remi Collet <remi@fedoraproject.org> - 2.2.2-1
- Update to 2.2.2
- add provides php-composer(horde/horde-text-filter)
- add dependency on Horde_Idna

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May 03 2014 Remi Collet <remi@fedoraproject.org> - 2.2.1-1
- Update to 2.2.1

* Wed Nov 20 2013 Remi Collet <remi@fedoraproject.org> - 2.2.0-1
- Update to 2.2.0
- upstream have move JSMin non-free code to a separate package
- add dependency on php-dom

* Thu Oct 24 2013 Remi Collet <remi@fedoraproject.org> - 2.1.5-1
- Update to 2.1.5

* Thu Oct 10 2013 Remi Collet <remi@fedoraproject.org> - 2.1.4-1
- Update to 2.1.4

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri May 31 2013 Remi Collet <remi@fedoraproject.org> - 2.1.3-1
- Update to 2.1.3

* Fri May 17 2013 Remi Collet <remi@fedoraproject.org> - 2.1.2-1
- Update to 2.1.2
- switch from Conflicts >= max to Requires < max

* Tue May 07 2013 Remi Collet <remi@fedoraproject.org> - 2.1.1-1
- Update to 2.1.1

* Wed Mar 06 2013 Remi Collet <remi@fedoraproject.org> - 2.1.0-1
- Update to 2.1.0

* Tue Feb 26 2013 Remi Collet <remi@fedoraproject.org> - 2.0.5-2
- fix License (review #908389)

* Tue Feb 12 2013 Remi Collet <remi@fedoraproject.org> - 2.0.5-1
- Update to 2.0.5

* Wed Feb  6 2013 Remi Collet <remi@fedoraproject.org> - 2.0.4-3
- cleanups for review
- always run tests but skip 2 for now

* Sun Jan 13 2013 Remi Collet <remi@fedoraproject.org> - 2.0.4-2
- remove non-free stuff

* Thu Jan 10 2013 Remi Collet <remi@fedoraproject.org> - 2.0.4-1
- Update to 2.0.4
- add option for test (need investigation)
- add patch php 5.5 compatibility (preg_replace with eval)
  http://bugs.horde.org/ticket/11943

* Tue Nov 27 2012 Remi Collet <remi@fedoraproject.org> - 2.0.3-1
- Update to 2.0.3

* Mon Nov 19 2012 Remi Collet <remi@fedoraproject.org> - 2.0.2-1
- Update to 2.0.2

* Wed Nov  7 2012 Remi Collet <remi@fedoraproject.org> - 2.0.1-1
- Update to 2.0.1

* Fri Nov  2 2012 Remi Collet <remi@fedoraproject.org> - 2.0.0-1
- Update to 2.0.0

* Thu Jun 21 2012 Nick Bebout <nb@fedoraproject.org> - 1.1.5-1
- Upgrade to 1.1.5

* Sat Jan 28 2012 Nick Bebout <nb@fedoraproject.org> - 1.1.2-1
- Initial package

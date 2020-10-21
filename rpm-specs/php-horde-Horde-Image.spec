# remirepo/fedora spec file for php-horde-Horde-Image
#
# Copyright (c) 2012-2020 Nick Bebout, Remi Collet
#
# License: MIT
# https://fedoraproject.org/wiki/Licensing:MIT#Modern_Style_with_sublicense
#
# Please, preserve the changelog entries
#
%{!?__pear:       %global __pear       %{_bindir}/pear}
%global pear_name    Horde_Image
%global pear_channel pear.horde.org
%global with_tests   %{?_without_tests:0}%{!?_without_tests:1}

Name:           php-horde-Horde-Image
Version:        2.6.1
Release:        2%{?dist}
Summary:        Horde Image API

License:        GPLv2+ and LGPLv2
URL:            http://pear.horde.org
Source0:        http://%{pear_channel}/get/%{pear_name}-%{version}.tgz

BuildArch:      noarch
BuildRequires:  gettext
BuildRequires:  php(language) >= 5.3.0
BuildRequires:  php-pear(PEAR) >= 1.7.0
BuildRequires:  php-channel(%{pear_channel})
%if %{with_tests}
# To run unit tests
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
BuildRequires: (php-pear(%{pear_channel}/Horde_Stream) >= 1.6.2  with php-pear(%{pear_channel}/Horde_Stream) < 2)
BuildRequires: (php-pear(%{pear_channel}/Horde_Test)   >= 2.1.0  with php-pear(%{pear_channel}/Horde_Test)   < 3)
%else
BuildRequires:  php-pear(%{pear_channel}/Horde_Stream) >= 1.6.2
BuildRequires:  php-pear(%{pear_channel}/Horde_Test) >= 2.1.0
%endif
%endif

Requires(post): %{__pear}
Requires(postun): %{__pear}
Requires:       php(language) >= 5.3.0
Requires:       php-date
Requires:       php-exif
Requires:       php-pcre
Requires:       php-spl
Requires:       php-pear(PEAR) >= 1.7.0
Requires:       php-channel(%{pear_channel})
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
Requires:      (php-pear(%{pear_channel}/Horde_Exception)   >= 2.0.0  with php-pear(%{pear_channel}/Horde_Exception)   < 3.0.0)
Requires:      (php-pear(%{pear_channel}/Horde_Stream)      >= 1.6.2  with php-pear(%{pear_channel}/Horde_Stream)      < 2.0.0)
Requires:      (php-pear(%{pear_channel}/Horde_Support)     >= 2.0.0  with php-pear(%{pear_channel}/Horde_Support)     < 3.0.0)
Requires:      (php-pear(%{pear_channel}/Horde_Translation) >= 2.2.0  with php-pear(%{pear_channel}/Horde_Translation) < 3.0.0)
Requires:      (php-pear(%{pear_channel}/Horde_Util)        >= 2.0.0  with php-pear(%{pear_channel}/Horde_Util)        < 3.0.0)
%else
Requires:       php-pear(%{pear_channel}/Horde_Exception) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Exception) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Stream) >= 1.6.2
Requires:       php-pear(%{pear_channel}/Horde_Stream) <  2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Support) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Support) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Translation) >= 2.2.0
Requires:       php-pear(%{pear_channel}/Horde_Translation) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Util) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Util) <  3.0.0
%endif
# Optional
Requires:       php-gd
Requires:       php-json
Requires:       php-zlib
Requires:       php-pear(XML_SVG)

Provides:       php-pear(%{pear_channel}/%{pear_name}) = %{version}
Provides:       php-composer(horde/horde-image) = %{version}


%description
An Image utility API, with backends for:
* GD
* GIF
* PNG
* SVG
* SWF
* ImageMagick convert command line tool
* Imagick Extension

Optional dependency: php-pecl-imagick


%prep
%setup -q -c

cd %{pear_name}-%{version}

# Don't install .po and .pot files
# Remove checksum for .mo, as we regenerate them
sed -e '/%{pear_name}.po/d' \
    -e '/.htaccess/d' \
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

for loc in locale/{??,??_??}
do
    lang=$(basename $loc)
    test -d %{buildroot}%{pear_datadir}/%{pear_name}/$loc \
         && echo "%%lang(${lang%_*}) %{pear_datadir}/%{pear_name}/$loc"
done | tee ../%{pear_name}.lang


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
: Test disabled, bootstrap build
%endif


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
%{pear_phpdir}/Horde/Image
%{pear_phpdir}/Horde/Image.php
%dir %{pear_datadir}/%{pear_name}
%dir %{pear_datadir}/%{pear_name}/locale
%doc %{pear_testdir}/Horde_Image


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Mar 13 2020 Remi Collet <remi@remirepo.net> - 2.6.1-1
- update to 2.6.1
- drop patch merged upstream

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 17 2019 Remi Collet <remi@remirepo.net> - 2.6.0-4
- add patch for PHP 7.4 from
  https://github.com/horde/Image/pull/3

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Remi Collet <remi@remirepo.net> - 2.6.0-1
- update to 2.6.0

* Wed Jan  2 2019 Remi Collet <remi@remirepo.net> - 2.5.4-1
- update to 2.5.4
- use range dependencies

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 25 2018 Remi Collet <remi@remirepo.net> - 2.5.3-1
- update to 2.5.3

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov 16 2017 Remi Collet <remi@remirepo.net> - 2.5.2-2
- drop uneeded .htacess from test directory

* Wed Sep 20 2017 Remi Collet <remi@remirepo.net> - 2.5.2-1
- Update to 2.5.2

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 26 2017 Remi Collet <remi@remirepo.net> - 2.5.1-1
- Update to 2.5.1

* Wed Jun 21 2017 Remi Collet <remi@remirepo.net> - 2.5.0-1
- Update to 2.5.0

* Tue Apr 11 2017 Remi Collet <remi@remirepo.net> - 2.4.1-1
- Update to 2.4.1

* Mon Mar 20 2017 Remi Collet <remi@remirepo.net> - 2.4.0-1
- Update to 2.4.0

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jul 13 2016 Remi Collet <remi@fedoraproject.org> - 2.3.6-1
- Update to 2.3.6

* Mon Mar 21 2016 Remi Collet <remi@fedoraproject.org> - 2.3.5-1
- Update to 2.3.5

* Mon Feb  8 2016 Remi Collet <remi@fedoraproject.org> - 2.3.4-1
- Update to 2.3.4 (no change)
- PHP 7 compatible version

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Sep 08 2015 Remi Collet <remi@fedoraproject.org> - 2.3.3-1
- Update to 2.3.3

* Fri Jul 31 2015 Remi Collet <remi@fedoraproject.org> - 2.3.2-1
- Update to 2.3.2

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr 28 2015 Remi Collet <remi@fedoraproject.org> - 2.3.1-1
- Update to 2.3.1

* Tue Apr 14 2015 Remi Collet <remi@fedoraproject.org> - 2.3.0-1
- Update to 2.3.0

* Wed Feb 11 2015 Remi Collet <remi@fedoraproject.org> - 2.2.0-1
- Update to 2.2.0
- add povides php-composer(horde/horde-image)
- add dependency on Horde_Stream
- raise dependency on Horde_Translation 2.2.0

* Tue Jun 17 2014 Remi Collet <remi@fedoraproject.org> - 2.1.0-1
- Update to 2.1.0

* Tue Jun 10 2014 Remi Collet <remi@fedoraproject.org> - 2.0.9-1
- Update to 2.0.9

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 22 2014 Remi Collet <remi@fedoraproject.org> - 2.0.8-1
- Update to 2.0.8

* Wed Apr 23 2014 Remi Collet <remi@fedoraproject.org> - 2.0.7-1
- Update to 2.0.7

* Fri Apr 04 2014 Remi Collet <remi@fedoraproject.org> - 2.0.6-1
- Update to 2.0.6
- enable test suite

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 15 2013 Remi Collet <remi@fedoraproject.org> - 2.0.5-1
- Update to 2.0.5

* Wed Mar 06 2013 Remi Collet <remi@fedoraproject.org> - 2.0.4-1
- Update to 2.0.4

* Wed Feb 6 2013 Nick Bebout <nb@fedoraproject.org> - 2.0.3-3
- Update for review

* Tue Feb 5 2013 Nick Bebout <nb@fedoraproject.org> - 2.0.3-2
- Remove BuildRoot, change php(language) to php-common

* Tue Jan 29 2013 Remi Collet <remi@fedoraproject.org> - 2.0.3-1
- Update to 2.0.3

* Wed Jan  9 2013 Remi Collet <remi@fedoraproject.org> - 2.0.2-1
- Update to 2.0.2
- manage locales
- new test layout (requires Horde_Test 2.1.0)

* Mon Nov 19 2012 Remi Collet <remi@fedoraproject.org> - 2.0.1-1
- Update to 2.0.1

* Mon Nov  5 2012 Remi Collet <remi@fedoraproject.org> - 2.0.0-2
- cleanups
- requires php-pear(XML_SVG)

* Thu Nov  1 2012 Remi Collet <remi@fedoraproject.org> - 2.0.0-1
- Update to 2.0.0

* Thu Jun 21 2012 Nick Bebout <nb@fedoraproject.org> - 1.0.10-1
- Upgrade to 1.0.10

* Sat Jan 28 2012 Nick Bebout <nb@fedoraproject.org> - 1.0.9-1
- Initial package

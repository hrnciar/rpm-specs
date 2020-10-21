# remirepo/fedora spec file for php-horde-Horde-Crypt
#
# Copyright (c) 2012-2018 Nick Bebout, Remi Collet
#
# License: MIT
# https://fedoraproject.org/wiki/Licensing:MIT#Modern_Style_with_sublicense
#
# Please, preserve the changelog entries
#
%{!?__pear:       %global __pear       %{_bindir}/pear}
%global pear_name    Horde_Crypt
%global pear_channel pear.horde.org

Name:           php-horde-Horde-Crypt
Version:        2.7.12
Release:        7%{?dist}
Summary:        Horde Cryptography API

License:        LGPLv2
URL:            http://%{pear_channel}
Source0:        http://%{pear_channel}/get/%{pear_name}-%{version}.tgz

BuildArch:      noarch
BuildRequires:  php(language) >= 5.3.0
BuildRequires:  php-pear(PEAR) >= 1.7.0
BuildRequires:  php-channel(%{pear_channel})
BuildRequires:  gettext
# To run unit tests
BuildRequires:  php-pear(%{pear_channel}/Horde_Http) >= 2.0.0
BuildRequires:  php-pear(%{pear_channel}/Horde_Test) >= 2.1.0
BuildRequires:  php-pear(%{pear_channel}/Horde_Stream) >= 1.5.0
BuildRequires:  php-pear(%{pear_channel}/Horde_Url) >= 2.0.0
%if 0%{?fedora} >= 30 || 0%{?rhel} >= 8
BuildRequires:  %{_bindir}/gpg1
%else
BuildRequires:  %{_bindir}/gpg2
%endif
# rhel have gnupg2 which provides this
BuildRequires:  %{_bindir}/gpg
%if 0%{?fedora}
%endif

Requires(post): %{__pear}
Requires(postun): %{__pear}
Requires:       php(language) >= 5.3.0
Requires:       php-date
Requires:       php-hash
Requires:       php-openssl
Requires:       php-pcre
Requires:       php-spl
Requires:       php-pear(PEAR) >= 1.7.0
Requires:       php-channel(%{pear_channel})
Requires:       php-pear(%{pear_channel}/Horde_Exception) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Exception) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Http) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Http) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Mime) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Mime) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Stream) >= 1.5.0
Requires:       php-pear(%{pear_channel}/Horde_Stream) <  2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Stream_Filter) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Stream_Filter) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Translation) >= 2.2.0
Requires:       php-pear(%{pear_channel}/Horde_Translation) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Url) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Url) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Util) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Util) <  3.0.0

Provides:       php-pear(%{pear_channel}/%{pear_name}) = %{version}
Provides:       php-composer(horde/horde-crypt) = %{version}


%description
The Horde_Crypt package class provides an API for various cryptographic
systems.

%prep
%setup -q -c
cd %{pear_name}-%{version}

# Don't install .po and .pot files
# Remove checksum for .mo, as we regenerate them
sed -e '/%{pear_name}.po/d' \
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
    test -d $loc && echo "%%lang(${lang%_*}) %{pear_datadir}/%{pear_name}/$loc"
done | tee ../%{pear_name}.lang


%check
cd %{pear_name}-%{version}/test/$(echo %{pear_name} | sed -e s:_:/:g)
: Skip online test
rm PgpKeyserverTest.php

%if 0%{?fedora} >= 30 || 0%{?rhel} >= 8
export CRYPT_TEST_CONFIG='{"gnupg":"%{_bindir}/gpg1,"gnupg2":false}'
%{_bindir}/gpg1 --version
%else
%if 0%{?fedora}
# use both versions (still broken with 2.1, ok with 2.0 and 2.2)
export CRYPT_TEST_CONFIG='{"gnupg":"%{_bindir}/gpg","gnupg2":"%{_bindir}/gpg2"}'
%{_bindir}/gpg2 --version
%endif
%endif
%{_bindir}/gpg  --version

ret=0
for cmd in php php70 php71 php72; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit \
      --filter '^((?!(testGenerateKey)).)*$' \
      --bootstrap bootstrap.php \
      --verbose . || ret=1
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
%{pear_phpdir}/Horde/Crypt
%{pear_phpdir}/Horde/Crypt.php
%doc %{pear_testdir}/%{pear_name}
%dir %{pear_datadir}/%{pear_name}
%dir %{pear_datadir}/%{pear_name}/locale


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.12-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan  4 2019 Remi Collet <remi@remirepo.net> - 2.7.12-3
- cleanup for EL-8

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon May 14 2018 Remi Collet <remi@remirepo.net> - 2.7.12-1
- update to 2.7.12

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Oct  9 2017 Remi Collet <remi@remirepo.net> - 2.7.11-1
- Update to 2.7.11

* Tue Sep 19 2017 Remi Collet <remi@remirepo.net> - 2.7.10-1
- Update to 2.7.10

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 23 2017 Remi Collet <remi@remirepo.net> - 2.7.9-1
- Update to 2.7.9

* Wed May  3 2017 Remi Collet <remi@remirepo.net> - 2.7.8-1
- Update to 2.7.8

* Tue Apr  4 2017 Remi Collet <remi@remirepo.net> - 2.7.6-1
- Update to 2.7.6

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 20 2016 Remi Collet <remi@fedoraproject.org> - 2.7.5-1
- Update to 2.7.5

* Sun Dec 04 2016 Remi Collet <remi@fedoraproject.org> - 2.7.4-1
- Update to 2.7.4

* Tue Apr 05 2016 Remi Collet <remi@fedoraproject.org> - 2.7.3-1
- Update to 2.7.3

* Fri Mar 11 2016 Remi Collet <remi@fedoraproject.org> - 2.7.2-1
- Update to 2.7.2

* Wed Mar 09 2016 Remi Collet <remi@fedoraproject.org> - 2.7.1-1
- Update to 2.7.1

* Mon Feb  8 2016 Remi Collet <remi@fedoraproject.org> - 2.7.0-1
- Update to 2.7.0
- PHP 7 compatible version

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Aug 26 2015 Remi Collet <remi@fedoraproject.org> - 2.6.1-1
- Update to 2.6.1

* Fri Jul 31 2015 Remi Collet <remi@fedoraproject.org> - 2.6.0-1
- Update to 2.6.0

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Feb 11 2015 Remi Collet <remi@fedoraproject.org> - 2.5.3-1
- Update to 2.5.3
- add provides php-composer(horde/horde-crypt)

* Mon Dec 29 2014 Remi Collet <remi@fedoraproject.org> - 2.5.2-1
- Update to 2.5.2

* Tue Nov 18 2014 Remi Collet <remi@fedoraproject.org> - 2.5.1-1
- Update to 2.5.1
- raise dependency on Horde_Translation 2.2.0

* Mon Jul 07 2014 Remi Collet <remi@fedoraproject.org> - 2.5.0-1
- Update to 2.5.0

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 22 2014 Remi Collet <remi@fedoraproject.org> - 2.4.3-1
- Update to 2.4.3

* Fri Apr 04 2014 Remi Collet <remi@fedoraproject.org> - 2.4.2-1
- Update to 2.4.2

* Wed Mar 05 2014 Remi Collet <remi@fedoraproject.org> - 2.4.1-2
- Update to 2.4.1
- BR /usr/bin/gpg on all branches (gnupg or gnupg2 on RHEL >= 6)

* Sun Jan 12 2014 Remi Collet <remi@fedoraproject.org> - 2.4.0-2
- fix failed tests because of gpg version output

* Wed Nov 20 2013 Remi Collet <remi@fedoraproject.org> - 2.4.0-1
- Update to 2.4.0
- add dependencies: Horde_Http, Horde_Url

* Tue Nov 12 2013 Remi Collet <remi@fedoraproject.org> - 2.3.0-1
- Update to 2.3.0
- add dependency: Horde_Stream >= 1.5.0

* Tue Aug 27 2013 Remi Collet <remi@fedoraproject.org> - 2.2.2-1
- Update to 2.2.2

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jun 27 2013 Remi Collet <remi@fedoraproject.org> - 2.2.1-1
- Update to 2.2.1

* Tue May 07 2013 Remi Collet <remi@fedoraproject.org> - 2.2.0-1
- Update to 2.2.0

* Wed Mar 06 2013 Remi Collet <remi@fedoraproject.org> - 2.1.3-1
- Update to 2.1.3

* Mon Feb 11 2013 Remi Collet <remi@fedoraproject.org> - 2.1.2-2
- cleanups for review

* Tue Jan 29 2013 Remi Collet <remi@fedoraproject.org> - 2.1.2-1
- Update to 2.1.2

* Wed Jan  9 2013 Remi Collet <remi@fedoraproject.org> - 2.1.1-1
- Update to 2.1.1
- use local script instead of find_lang
- new test layout (requires Horde_Test 2.1.0)
- add option for test (can't be run in mock)

* Wed Nov  7 2012 Remi Collet <remi@fedoraproject.org> - 2.1.0-1
- Update to 2.1.0

* Sat Nov  3 2012 Remi Collet <remi@fedoraproject.org> - 2.0.0-1
- Update to 2.0.0

* Thu Jun 21 2012 Nick Bebout <nb@fedoraproject.org> - 1.1.2-1
- Initial package

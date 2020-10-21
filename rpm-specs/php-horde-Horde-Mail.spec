# remirepo/fedora spec file for php-horde-Horde-Mail
#
# Copyright (c) 2012-2019 Nick Bebout, Remi Collet
#
# License: MIT
# https://fedoraproject.org/wiki/Licensing:MIT#Modern_Style_with_sublicense
#
# Please, preserve the changelog entries
#
%{!?__pear:       %global __pear       %{_bindir}/pear}
%global pear_name    Horde_Mail
%global pear_channel pear.horde.org
%global with_tests   0%{!?_without_tests:1}

Name:           php-horde-Horde-Mail
Version:        2.6.5
Release:        4%{?dist}
Summary:        Horde Mail Library

License:        BSD
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
BuildRequires: (php-pear(%{pear_channel}/Horde_Test)          >= 2.1.0   with php-pear(%{pear_channel}/Horde_Test)          < 3)
BuildRequires: (php-pear(%{pear_channel}/Horde_Exception)     >= 2.0.0   with php-pear(%{pear_channel}/Horde_Exception)     < 3)
BuildRequires: (php-pear(%{pear_channel}/Horde_Mime)          >= 2.0.0   with php-pear(%{pear_channel}/Horde_Mime)          < 3)
BuildRequires: (php-pear(%{pear_channel}/Horde_Idna)          >= 1.0.0   with php-pear(%{pear_channel}/Horde_Idna)          < 2)
BuildRequires: (php-pear(%{pear_channel}/Horde_Stream_Filter) >= 2.0.0   with php-pear(%{pear_channel}/Horde_Stream_Filter) < 3)
BuildRequires: (php-pear(%{pear_channel}/Horde_Translation)   >= 2.2.0   with php-pear(%{pear_channel}/Horde_Translation)   < 3)
BuildRequires: (php-pear(%{pear_channel}/Horde_Util)          >= 2.0.0   with php-pear(%{pear_channel}/Horde_Util)          < 3)
%else
BuildRequires:  php-pear(%{pear_channel}/Horde_Test) <  3.0.0
BuildRequires:  php-pear(%{pear_channel}/Horde_Test) >= 2.1.0
BuildRequires:  php-pear(%{pear_channel}/Horde_Exception) >= 2.0.0
BuildRequires:  php-pear(%{pear_channel}/Horde_Exception) <  3.0.0
BuildRequires:  php-pear(%{pear_channel}/Horde_Mime) >= 2.0.0
BuildRequires:  php-pear(%{pear_channel}/Horde_Mime) <  3.0.0
BuildRequires:  php-pear(%{pear_channel}/Horde_Idna) >= 1.0.0
BuildRequires:  php-pear(%{pear_channel}/Horde_Idna) <  2.0.0
BuildRequires:  php-pear(%{pear_channel}/Horde_Stream_Filter) >= 2.0.0
BuildRequires:  php-pear(%{pear_channel}/Horde_Stream_Filter) <  3.0.0
BuildRequires:  php-pear(%{pear_channel}/Horde_Translation) >= 2.2.0
BuildRequires:  php-pear(%{pear_channel}/Horde_Translation) <  3.0.0
BuildRequires:  php-pear(%{pear_channel}/Horde_Util) >= 2.0.0
BuildRequires:  php-pear(%{pear_channel}/Horde_Util) <  3.0.0
%endif
%endif

Requires(post): %{__pear}
Requires(postun): %{__pear}
# From package.xml, required
Requires:       php(language) >= 5.3.0
Requires:       php-pear(PEAR) >= 1.7.0
Requires:       php-channel(%{pear_channel})
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
Requires:      (php-pear(%{pear_channel}/Horde_Exception)     >= 2.0.0   with php-pear(%{pear_channel}/Horde_Exception)     < 3)
Requires:      (php-pear(%{pear_channel}/Horde_Mime)          >= 2.0.0   with php-pear(%{pear_channel}/Horde_Mime)          < 3)
Requires:      (php-pear(%{pear_channel}/Horde_Idna)          >= 1.0.0   with php-pear(%{pear_channel}/Horde_Idna)          < 2)
Requires:      (php-pear(%{pear_channel}/Horde_Stream_Filter) >= 2.0.0   with php-pear(%{pear_channel}/Horde_Stream_Filter) < 3)
Requires:      (php-pear(%{pear_channel}/Horde_Translation)   >= 2.2.0   with php-pear(%{pear_channel}/Horde_Translation)   < 3)
Requires:      (php-pear(%{pear_channel}/Horde_Util)          >= 2.0.0   with php-pear(%{pear_channel}/Horde_Util)          < 3)
# From package.xml, optional
Recommends:     php-pear(Net_SMTP) >= 1.6.0
Recommends:     php-pear(Net_DNS2)
%else
Requires:       php-pear(%{pear_channel}/Horde_Exception) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Exception) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Mime) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Mime) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Idna) >= 1.0.0
Requires:       php-pear(%{pear_channel}/Horde_Idna) <  2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Stream_Filter) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Stream_Filter) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Translation) >= 2.2.0
Requires:       php-pear(%{pear_channel}/Horde_Translation) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Util) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Util) <  3.0.0
# From package.xml, optional
Requires:       php-pear(Net_SMTP) >= 1.6.0
Requires:       php-pear(Net_DNS2)
%endif
# From phpcompatinfo report for version 2.1.3
Requires:       php-intl
Requires:       php-pcre
Requires:       php-posix
Requires:       php-spl
# optional and implicitly required: Horde_Support, Horde_Stream_Wrapper
# Horde_Smtp optional and ignored to avoid circular dep.

Provides:       php-pear(%{pear_channel}/%{pear_name}) = %{version}
Provides:       php-composer(horde/horde-mail) = %{version}


%description
The Horde_Mail library is a fork of the PEAR Mail library that provides
additional functionality, including (but not limited to):
* Allows a stream to be passed in.
* Allows raw headertext to be used in the outgoing messages (required for
things like message redirection pursuant to RFC 5322 [3.6.6]).
* Native PHP 5 code.
* PHPUnit test suite.
* Provides more comprehensive sendmail error messages.
* Uses Exceptions instead of PEAR_Errors.


%prep
%setup -q -c

cd %{pear_name}-%{version}
# Don't install .po and .pot files
# Remove checksum for .mo, as we regenerate them
sed -e '/%{pear_name}\.po/d' \
    -e '/%{pear_name}.mo/s/md5sum=.*name=/name=/' \
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
for cmd in php php56 php70 php71 php72 php73; do
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


%files -f %{pear_name}.lang
%doc %{pear_docdir}/%{pear_name}
%{pear_xmldir}/%{name}.xml
%{pear_phpdir}/Horde/Mail
%doc %{pear_testdir}/%{pear_name}
%dir %{pear_datadir}/%{pear_name}
%dir %{pear_datadir}/%{pear_name}/locale


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Mar  3 2019 Remi Collet <remi@remirepo.net> - 2.6.5-1
- update to 2.6.5
- use range dependencies
- enable test suite

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 23 2017 Remi Collet <remi@remirepo.net> - 2.6.4-1
- Update to 2.6.4
- add locales

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Feb  8 2016 Remi Collet <remi@fedoraproject.org> - 2.6.3-1
- Update to 2.6.3 (no change)
- PHP 7 compatible version

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jul 31 2015 Remi Collet <remi@fedoraproject.org> - 2.6.2-1
- Update to 2.6.2

* Wed Jun 24 2015 Remi Collet <remi@fedoraproject.org> - 2.6.1-1
- Update to 2.6.1

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr 28 2015 Remi Collet <remi@fedoraproject.org> - 2.6.0-1
- Update to 2.6.0
- add dependency on Horde_Util
- add povides php-composer(horde/horde-mail)

* Wed Jan 07 2015 Remi Collet <remi@fedoraproject.org> - 2.5.1-1
- Update to 2.5.1
- add required dependency on Horde_Idna

* Sun Nov 23 2014 Remi Collet <remi@fedoraproject.org> - 2.5.0-1
- Update to 2.5.0
- add dependency on Horde_Translation

* Mon Aug 04 2014 Remi Collet <remi@fedoraproject.org> - 2.4.0-1
- Update to 2.4.0

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 22 2014 Remi Collet <remi@fedoraproject.org> - 2.3.0-1
- Update to 2.3.0

* Sat May 03 2014 Remi Collet <remi@fedoraproject.org> - 2.2.0-1
- Update to 2.2.0

* Fri Apr 04 2014 Remi Collet <remi@fedoraproject.org> - 2.1.6-1
- Update to 2.1.6

* Tue Feb 11 2014 Remi Collet <remi@fedoraproject.org> - 2.1.5-1
- Update to 2.1.5
- Raise dependency on Horde_Stream_Wrapper >= 2.1.0

* Wed Jan 22 2014 Remi Collet <remi@fedoraproject.org> - 2.1.4-1
- Update to 2.1.4

* Tue Oct 15 2013 Remi Collet <remi@fedoraproject.org> - 2.1.2-1
- Update to 2.1.2

* Tue Aug 27 2013 Remi Collet <remi@fedoraproject.org> - 2.1.1-1
- Update to 2.1.1

* Fri Aug 23 2013 Remi Collet <remi@fedoraproject.org> - 2.1.0-1
- Update to 2.1.0

* Thu Jul 25 2013 Remi Collet <remi@fedoraproject.org> - 2.0.6-1
- Update to 2.0.6

* Tue Apr 09 2013 Remi Collet <remi@fedoraproject.org> - 2.0.5-1
- Update to 2.0.5

* Wed Mar 20 2013 Nick Bebout <nb@fedoraproject.org> - 2.0.4-1
- Update for review

* Tue Feb  5 2013 Nick Bebout <nb@fedoraproject.org> - 2.0.3-2
- Remove BuildRoot, Change php(language) to php-common

* Thu Dec 27 2012 Remi Collet <remi@fedoraproject.org> - 2.0.3-1
- Update to 2.0.3 for remi repo

* Tue Dec  4 2012 Remi Collet <remi@fedoraproject.org> - 2.0.2-1
- Update to 2.0.2 for remi repo

* Sat Nov 17 2012 Remi Collet <remi@fedoraproject.org> - 2.0.1-1
- Update to 2.0.1 for remi repo

* Fri Nov  2 2012 Remi Collet <remi@fedoraproject.org> - 2.0.0-1
- Update to 2.0.0 for remi repo

* Thu Jun 21 2012 Nick Bebout <nb@fedoraproject.org> - 1.2.0-1
- Upgrade to 1.2.0

* Sat Jan 28 2012 Nick Bebout <nb@fedoraproject.org> - 1.0.3-1
- Initial package

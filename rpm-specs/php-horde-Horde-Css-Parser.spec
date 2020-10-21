# remirepo/fedora spec file for php-horde-Horde-Css-Parser
#
# Copyright (c) 2013-2016 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%{!?__pear:       %global __pear       %{_bindir}/pear}
%global pear_name    Horde_Css_Parser
%global pear_channel pear.horde.org

Name:           php-horde-Horde-Css-Parser
Version:        1.0.11
Release:        9%{?dist}
Summary:        Horde CSS Parser

License:        LGPLv2
URL:            http://%{pear_channel}
Source0:        http://%{pear_channel}/get/%{pear_name}-%{version}.tgz

# Use fedora autoloader instead of composer one
Patch0:         %{pear_name}-rpm.patch

BuildArch:      noarch
BuildRequires:  php(language) >= 5.3.2
BuildRequires:  php-pear(PEAR) >= 1.7.0
BuildRequires:  php-channel(%{pear_channel})
# To run unit tests
BuildRequires:  php-pear(%{pear_channel}/Horde_Test) >= 2.1.0
BuildRequires:  php-composer(sabberworm/php-css-parser) >= 7.0.2

Requires(post): %{__pear}
Requires(postun): %{__pear}
# From package.xml
Requires:       php(language) >= 5.3.2
Requires:       php-mbstring
Requires:       php-pear(PEAR) >= 1.7.0
Requires:       php-channel(%{pear_channel})
# Unbundled library
Requires:       php-composer(sabberworm/php-css-parser) >= 7.0.3
# From phpcompatinfo report for 1.0.2
Requires:       php-iconv
Requires:       php-pcre

Provides:       php-pear(%{pear_channel}/%{pear_name}) = %{version}
Provides:       php-composer(horde/horde-css-parser) = %{version}


%description
This package provides access to the Sabberworm CSS Parser from within the
Horde framework.


%prep
%setup -q -c

cd %{pear_name}-%{version}
%patch0 -p1 -b .rpm

sed -e '/bundle/d' \
    -e '/EXPAT_LICENSE/d' \
    -e '/Parser.php/s/md5sum="[^"]*"//' \
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

%{_bindir}/phpunit --verbose .


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
%doc %{pear_testdir}/%{pear_name}
%{pear_xmldir}/%{name}.xml
%dir %{pear_phpdir}/Horde
%{pear_phpdir}/Horde/Css


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.11-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jul 03 2016 Remi Collet <remi@fedoraproject.org> - 1.0.11-1
- Update to 1.0.11 (no change)
- raise dependency on php-PHP-CSS-Parser >= 7.0.3

* Fri Apr 15 2016 Remi Collet <remi@fedoraproject.org> - 1.0.10-1
- Update to 1.0.10

* Tue Apr 05 2016 Remi Collet <remi@fedoraproject.org> - 1.0.9-1
- Update to 1.0.9
- raise dependency on php-PHP-CSS-Parser >= 7.0.2
- use php-PHP-CSS-Parser autoloader (instead of PSR-0)

* Mon Feb  8 2016 Remi Collet <remi@fedoraproject.org> - 1.0.8-1
- Update to 1.0.8 (no change)
- PHP 7 compatible version

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jul 31 2015 Remi Collet <remi@fedoraproject.org> - 1.0.7-1
- Update to 1.0.7 (no change)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jan 13 2015 Remi Collet <remi@fedoraproject.org> - 1.0.6-2
- Update to 1.0.6
- raise dependency on sabberworm/php-css-parser >= 6

* Thu Jan 08 2015 Remi Collet <remi@fedoraproject.org> - 1.0.5-1
- Update to 1.0.5
- add provides php-composer(horde/horde-css-parser)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Feb 20 2014 Remi Collet <remi@fedoraproject.org> - 1.0.4-1
- Update to 1.0.4

* Thu Oct 24 2013 Remi Collet <remi@fedoraproject.org> - 1.0.3-1
- Update to 1.0.3 (no change)

* Tue Oct 15 2013 Remi Collet <remi@fedoraproject.org> - 1.0.2-1
- Update to 1.0.2

* Fri Aug 23 2013 Remi Collet <remi@fedoraproject.org> - 1.0.1-1
- Update to 1.0.1 for PHP-CSS-Parser 5.0.8

* Thu May 30 2013 Remi Collet <remi@fedoraproject.org> - 1.0.0-2
- use system php-PHP-CSS-Parser

* Thu May 30 2013 Remi Collet <remi@fedoraproject.org> - 1.0.0-1
- initial package, with bundled lib (need to be cleaned)

# remirepo/fedora spec file for php-tecnickcom-tc-lib-barcode
#
# Copyright (c) 2015-2020 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global gh_commit    dd8de5620ec436d61cc8535e11f2879146ebc16b
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global c_vendor     tecnickcom
%global gh_owner     tecnickcom
%global gh_project   tc-lib-barcode
%global php_project  %{_datadir}/php/Com/Tecnick/Barcode
%global with_tests   0%{!?_without_tests:1}

Name:           php-%{gh_owner}-%{gh_project}
Version:        1.15.20
Release:        2%{?dist}.1
Summary:        PHP library to generate linear and bidimensional barcodes

License:        LGPLv3+
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{gh_project}-%{version}-%{?gh_short}.tar.gz

BuildArch:      noarch
%if %{with_tests}
# For tests
%if 0%{?fedora} >= 28 || 0%{?rhel} >= 8
%global phpunit %{_bindir}/phpunit7
%else
%global phpunit %{_bindir}/phpunit
%endif
BuildRequires:  %{phpunit}
BuildRequires:  php(language) >= 5.3
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
BuildRequires: (php-composer(%{c_vendor}/tc-lib-color) >= 1.12.13 with php-composer(%{c_vendor}/tc-lib-color) <  2)
%else
BuildRequires:  php-composer(%{c_vendor}/tc-lib-color) <  2
BuildRequires:  php-composer(%{c_vendor}/tc-lib-color) >= 1.12.13
%endif
BuildRequires:  php-bcmath
BuildRequires:  php-ctype
BuildRequires:  php-date
BuildRequires:  php-gd
BuildRequires:  php-pcre
# Optional but required for test
BuildRequires:  php-pecl-imagick
%endif

# From composer.json, "require": {
#        "php": ">=5.3"
#        "ext-bcmath": "*",
#        "ext-date": "*",
#        "ext-gd": "*",
#        "ext-pcre": "*",
#        "tecnickcom/tc-lib-color": "^1.12.15"
Requires:       php(language) >= 5.3
Requires:       php-bcmath
Requires:       php-ctype
Requires:       php-date
Requires:       php-gd
Requires:       php-pcre
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
Requires:      (php-composer(%{c_vendor}/tc-lib-color) >= 1.12.13 with php-composer(%{c_vendor}/tc-lib-color) <  2)
%else
Requires:       php-composer(%{c_vendor}/tc-lib-color) <  2
Requires:       php-composer(%{c_vendor}/tc-lib-color) >= 1.12.13
%endif
# From phpcompatinfo report for version 1.15.5
# none

# Composer
Provides:       php-composer(%{c_vendor}/%{gh_project}) = %{version}
# Upstream package name
Provides:       php-%{gh_project} = %{version}


%description
Provides tc-lib-barcode: PHP classes to generate linear and bidimensional
barcodes: CODE 39, ANSI MH10.8M-1983, USD-3, 3 of 9, CODE 93, USS-93,
Standard 2 of 5, Interleaved 2 of 5, CODE 128 A/B/C, 2 and 5 Digits
UPC-Based Extension, EAN 8, EAN 13, UPC-A, UPC-E, MSI, POSTNET, PLANET,
RMS4CC (Royal Mail 4-state Customer Code), CBC (Customer Bar Code),
KIX (Klant index - Customer index), Intelligent Mail Barcode, Onecode,
USPS-B-3200, CODABAR, CODE 11, PHARMACODE, PHARMACODE TWO-TRACKS, Datamatrix
ECC200, QR-Code, PDF417.

Optional dependency: php-pecl-imagick


%prep
%setup -q -n %{gh_project}-%{gh_commit}

: Sanity check
grep -q '^%{version}$' VERSION

: Fix the examples
sed -e 's:^require:////require:' \
    -e 's:^//require:require:'   \
    -i example/*php


%build
# Empty build section, most likely nothing required.


%install
mkdir -p   $(dirname %{buildroot}%{php_project})
cp -pr src %{buildroot}%{php_project}
cp -p  resources/autoload.php \
           %{buildroot}%{php_project}/autoload.php


%check
%if %{with_tests}
mkdir vendor
cat <<EOF | tee vendor/autoload.php
<?php
require '%{buildroot}%{php_project}/autoload.php';
require '%{php_project}/../Color/autoload.php';
require __DIR__ . '/../test/TestStrings.php';
EOF

ret=0
for cmdarg in "php %{phpunit}" php71 php72 php73 php74; do
   if which $cmdarg; then
      set $cmdarg
      $1 ${2:-%{_bindir}/phpunit7} --no-coverage --verbose || ret=1
   fi
done
exit $ret
%else
: Test suite disabled
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc composer.json
%doc README.md example
%{php_project}


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.20-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan  3 2020 Remi Collet <remi@remirepo.net> - 1.15.20-1
- update to 1.15.20

* Wed Oct  2 2019 Remi Collet <remi@remirepo.net> - 1.15.16-1
- update to 1.15.16

* Thu Sep 19 2019 Remi Collet <remi@remirepo.net> - 1.15.15-1
- update to 1.15.15

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun  3 2019 Remi Collet <remi@remirepo.net> - 1.15.14-1
- update to 1.15.14

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 25 2018 Remi Collet <remi@remirepo.net> - 1.15.12-1
- update to 1.15.12 (no change)

* Tue May 15 2018 Remi Collet <remi@remirepo.net> - 1.15.11-1
- update to 1.15.11 (no change)

* Mon May 14 2018 Remi Collet <remi@remirepo.net> - 1.15.10-1
- update to 1.15.10 (no change)
- switch to phpunit7
- use range dependencies

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan  2 2018 Remi Collet <remi@remirepo.net> - 1.15.7-1
- Update to 1.15.7

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Feb 12 2017 Remi Collet <remi@remirepo.net.org> - 1.15.6-1
- update to 1.15.6 (no change)
- use phpunit6 on F26+

* Mon Feb  6 2017 Remi Collet <remi@fedoraproject.org> - 1.15.5-1
- update to 1.15.5 (no change)

* Fri Nov 18 2016 Remi Collet <remi@fedoraproject.org> - 1.15.4-1
- update to 1.15.4

* Fri Oct 14 2016 Remi Collet <remi@fedoraproject.org> - 1.15.2-1
- update to 1.15.2

* Mon Sep  5 2016 Remi Collet <remi@fedoraproject.org> - 1.15.0-1
- update to 1.15.0

* Fri Sep  2 2016 Remi Collet <remi@fedoraproject.org> - 1.14.0-1
- update to 1.14.0
- raise dependency on tecnickcom/tc-lib-color >= 1.12.1

* Mon Jul 11 2016 Remi Collet <remi@fedoraproject.org> - 1.9.2-1
- update to 1.9.2

* Tue Jun 14 2016 Remi Collet <remi@fedoraproject.org> - 1.9.0-1
- update to 1.9.0
- raise dependency on tecnickcom/tc-lib-color >= 1.10.0
- raise dependency on php >= 5.4
- run test suite with both PHP 5 and 7 when available

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Nov  4 2015 Remi Collet <remi@fedoraproject.org> - 1.5.0-1
- update to 1.5.0

* Sun Sep 13 2015 Remi Collet <remi@fedoraproject.org> - 1.4.3-1
- update to 1.4.3
- provide php-composer(tecnickcom/tc-lib-barcode)

* Thu Aug 27 2015 Remi Collet <remi@fedoraproject.org> - 1.4.2-1
- update to 1.4.2

* Tue Aug 25 2015 Remi Collet <remi@fedoraproject.org> - 1.4.1-3
- add patch for PHP 5.3
  https://github.com/tecnickcom/tc-lib-barcode/pull/7

* Wed Aug 12 2015 Remi Collet <remi@fedoraproject.org> - 1.4.1-2
- fix package summary

* Tue Aug 11 2015 Remi Collet <remi@fedoraproject.org> - 1.4.1-1
- update to 1.4.1

* Tue Aug 11 2015 Remi Collet <remi@fedoraproject.org> - 1.4.0-1
- update to 1.4.0

* Sat Aug  8 2015 Remi Collet <remi@fedoraproject.org> - 1.3.1-1
- update to 1.3.1

* Thu Aug  6 2015 Remi Collet <remi@fedoraproject.org> - 1.3.0-1
- update to 1.3.0

* Fri Jul 24 2015 Remi Collet <remi@fedoraproject.org> - 1.2.1-1
- update to 1.2.1 (no change)

* Thu Jul  2 2015 Remi Collet <remi@fedoraproject.org> - 1.2.0-1
- update to 1.2.0

* Wed Jul  1 2015 Remi Collet <remi@fedoraproject.org> - 1.1.3-1
- update to 1.1.3
- drop patch merged upstream

* Wed Jul  1 2015 Remi Collet <remi@fedoraproject.org> - 1.1.2-1
- initial package, version 1.1.2
- open https://github.com/tecnickcom/tc-lib-barcode/pull/2
  PHP < 5.5 compatibility

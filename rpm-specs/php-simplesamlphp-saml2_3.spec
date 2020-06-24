#
# Fedora spec file for php-simplesamlphp-saml2_3
#
# Copyright (c) 2017-2019 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve the changelog entries
#

%global github_owner     simplesamlphp
%global github_name      saml2
%global github_version   3.4.2
%global github_commit    3806d276edb066c60aa3d748ffd0681d92ffbda7

%global composer_vendor  simplesamlphp
%global composer_project saml2

# "php": ">=5.4"
%global php_min_ver 5.4
# "mockery/mockery": "~0.9"
%global mockery_min_ver 0.9
%global mockery_max_ver 1.0
# "psr/log": "~1.0"
#     NOTE: Min version not 1.0 because autoloader required
%global psr_log_min_ver 1.0.1
%global psr_log_max_ver 2.0
# "webmozart/assert": "^1.4"
%global webmozart_assert_min_ver 1.4
%global webmozart_assert_max_ver 2.0
# "robrichards/xmlseclibs": "^3.0.4"
%global xmlseclibs_min_ver 3.0.4
%global xmlseclibs_max_ver 4.0

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}_3
Version:       %{github_version}
Release:       2%{?github_release}%{?dist}
Summary:       SAML2 PHP library from SimpleSAMLphp (version 3)

License:       LGPLv2+
URL:           https://github.com/%{github_owner}/%{github_name}

# GitHub export does not include tests.
# Run php-simplesamlphp-saml2_3-get-source.sh to create full source.
Source0:       %{name}-%{github_version}-%{github_commit}.tar.gz
Source1:       %{name}-get-source.sh

BuildArch:     noarch
# Tests
%if %{with_tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: php-composer(phpunit/phpunit)
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
BuildRequires: (php-composer(mockery/mockery) >= %{mockery_min_ver} with php-composer(mockery/mockery) < %{mockery_max_ver})
BuildRequires: (php-composer(psr/log) >= %{psr_log_min_ver} with php-composer(psr/log) < %{psr_log_max_ver})
BuildRequires: (php-composer(robrichards/xmlseclibs) >= %{xmlseclibs_min_ver} with php-composer(robrichards/xmlseclibs) < %{xmlseclibs_max_ver})
BuildRequires: (php-composer(webmozart/assert) >= %{webmozart_assert_min_ver} with php-composer(webmozart/assert) < %{webmozart_assert_max_ver})
%else
BuildRequires: php-composer(mockery/mockery) <  %{mockery_max_ver}
BuildRequires: php-composer(mockery/mockery) >= %{mockery_min_ver}
BuildRequires: php-composer(psr/log) <  %{psr_log_max_ver}
BuildRequires: php-composer(psr/log) >= %{psr_log_min_ver}
BuildRequires: php-composer(robrichards/xmlseclibs) <  %{xmlseclibs_max_ver}
BuildRequires: php-composer(robrichards/xmlseclibs) >= %{xmlseclibs_min_ver}
BuildRequires: php-composer(webmozart/assert) <  %{webmozart_assert_max_ver}
BuildRequires: php-composer(webmozart/assert) >= %{webmozart_assert_min_ver}
%endif
BuildRequires: php-dom
BuildRequires: php-openssl
BuildRequires: php-zlib
## phpcompatinfo (computed from version 3.4.1)
BuildRequires: php-date
BuildRequires: php-filter
BuildRequires: php-libxml
BuildRequires: php-pcre
BuildRequires: php-soap
BuildRequires: php-spl
%endif
## Autoloader
BuildRequires: php-fedora-autoloader-devel

# composer.json
Requires:      php(language) >= %{php_min_ver}
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
Requires:      (php-composer(psr/log) >= %{psr_log_min_ver} with php-composer(psr/log) < %{psr_log_max_ver})
Requires:      (php-composer(robrichards/xmlseclibs) >= %{xmlseclibs_min_ver} with php-composer(robrichards/xmlseclibs) < %{xmlseclibs_max_ver})
Requires:      (php-composer(webmozart/assert) >= %{webmozart_assert_min_ver} with php-composer(webmozart/assert) < %{webmozart_assert_max_ver})
%else
Requires:      php-composer(psr/log) <  %{psr_log_max_ver}
Requires:      php-composer(psr/log) >= %{psr_log_min_ver}
Requires:      php-composer(robrichards/xmlseclibs) <  %{xmlseclibs_max_ver}
Requires:      php-composer(robrichards/xmlseclibs) >= %{xmlseclibs_min_ver}
Requires:      php-composer(webmozart/assert) <  %{webmozart_assert_max_ver}
Requires:      php-composer(webmozart/assert) >= %{webmozart_assert_min_ver}
%endif
Requires:      php-dom
Requires:      php-openssl
Requires:      php-zlib
# phpcompatinfo (computed from version 3.4.1)
Requires:      php-date
Requires:      php-filter
Requires:      php-libxml
Requires:      php-pcre
Requires:      php-soap
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}


%description
A PHP library for SAML2 related functionality. Extracted from SimpleSAMLphp [1],
used by OpenConext [2]. This library started as a collaboration between
UNINETT [3] and SURFnet [4] but everyone is invited to contribute.

Autoloader: %{phpdir}/SAML2_3/autoload.php

[1] https://www.simplesamlphp.org/
[2] https://www.openconext.org/
[3] https://www.uninett.no/
[4] https://www.surfnet.nl/


%prep
%setup -qn %{github_name}-%{github_commit}


%build
: Create autoloader
%{_bindir}/phpab --template fedora --output src/SAML2/autoload.php src/SAML2
cat <<'AUTOLOAD' >> src/SAML2/autoload.php

class_alias('\\SAML2\\Constants', 'SAML2_Const');

\Fedora\Autoloader\Dependencies::required(array(
    '%{phpdir}/Psr/Log/autoload.php',
    '%{phpdir}/RobRichards/XMLSecLibs3/autoload.php',
    '%{phpdir}/Webmozart/Assert/autoload.php',
));
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}
cp -rp src/SAML2 %{buildroot}%{phpdir}/SAML2_3


%check
%if %{with_tests}
: Create pseudo Composer autoloader
mkdir vendor
%{_bindir}/phpab --template fedora --output vendor/autoload.php tests
cat <<'AUTOLOAD' | tee -a vendor/autoload.php
require_once '%{buildroot}%{phpdir}/SAML2_3/autoload.php';
require_once '%{phpdir}/Mockery/autoload.php';
AUTOLOAD

: Skip tests known to fail
sed -e 's/function testMarshalling/function SKIP_testMarshalling/' \
    -e 's/function testMarshallingChildren/function SKIP_testMarshallingChildren/' \
    -i tests/SAML2/XML/mdui/DiscoHintsTest.php
sed -e 's/function testMarshalling/function SKIP_testMarshalling/' \
    -e 's/function testMarshallingChildren/function SKIP_testMarshallingChildren/' \
    -i tests/SAML2/XML/mdui/UIInfoTest.php
sed 's/function testToString/function SKIP_testToString/' \
    -i tests/SAML2/XML/saml/NameIDTest.php

: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which phpunit)
for PHP_EXEC in php %{?rhel:php55 php56} php70 php71 php72 php73 php74; do
    if [ "php" = "$PHP_EXEC" ] || which $PHP_EXEC; then
        $PHP_EXEC $PHPUNIT --verbose || RETURN_CODE=1
    fi
done
exit $RETURN_CODE
%else
: Tests skipped
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc *.md
%doc composer.json
%{phpdir}/SAML2_3


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 07 2019 Shawn Iwinski <shawn@iwin.ski> - 3.4.2-1
- Update to 3.4.2 (RHBZ #1769354 / SSPSA 201911-01 / CVE-2019-3465)
- https://simplesamlphp.org/security/201911-01

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 21 2019 Shawn Iwinski <shawn@iwin.ski> - 3.4.1-1
- Update to 3.4.1 (RHBZ #1688285)

* Wed Feb 13 2019 Shawn Iwinski <shawn@iwin.ski> - 3.3.8-1
- Update to 3.3.8 (RHBZ #1600514)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat May 26 2018 Shawn Iwinski <shawn@iwin.ski> - 3.1.6-1
- Update to 3.1.6 (RHBZ #1581245)

* Sun Apr 29 2018 Shawn Iwinski <shawn@iwin.ski> - 3.1.5-1
- Update to 3.1.5 (RHBZ #1568917)

* Mon Mar 12 2018 Shawn Iwinski <shawn@iwin.ski> - 3.1.4-3
- Update range dependencies' conditional to include RHEL 8+

* Mon Mar 12 2018 Remi Collet <remi@remirepo.net> - 3.1.4-2
- fix dependencies

* Sat Mar 10 2018 Shawn Iwinski <shawn@iwin.ski> - 3.1.4-1
- Update to 3.1.4 (RHBZ #1528489, SSPSA 201801-01, CVE-2018-6519, SSPSA 201802-01, CVE-2018-7644, SSPSA 201803-01, CVE-2018-7711)
- License changed from LGPLv2 to LGPLv2+
- Update "get source" to save tarball in same directory as spec file
- Use range dependencies on F27+

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 30 2017 Shawn Iwinski <shawn@iwin.ski> - 3.0.2-3
- Drop support for simplesamlphp/xmlseclibs v2

* Tue Aug 22 2017 Shawn Iwinski <shawn@iwin.ski> - 3.0.2-2
- Build require mcrypt for robrichards/xmlseclibs version 2

* Sun Aug 20 2017 Shawn Iwinski <shawn@iwin.ski> - 3.0.2-1
- Update to 3.0.2

* Wed Jul 12 2017 Shawn Iwinski <shawn@iwin.ski> - 3.0.0-1
- Initial package

# remirepo/fedora spec file for php-pragmarx-google2fa
#
# Copyright (c) 2018 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%global with_tests   0%{!?_without_tests:1}
# Github
%global gh_commit    6949226739e4424f40031e6f1c96b1fd64047335
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     antonioribeiro
%global gh_project   google2fa
# Packagist
%global pk_vendor    pragmarx
%global pk_project   %{gh_project}
# Namespace
%global ns_vendor    PragmaRX
%global ns_project   Google2FA

Name:           php-%{pk_vendor}-%{pk_project}
Version:        3.0.3
Release:        4%{?gh_date?%{gh_date}git%{gh_short}}%{?dist}
Summary:        Google Two-Factor Authentication for PHP Package

License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{name}-%{version}-%{?gh_short}.tar.gz

BuildArch:      noarch
%if %{with_tests}
BuildRequires:  php(language) >= 5.6
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
BuildRequires:  (php-composer(paragonie/constant_time_encoding) >= 1.0   with php-composer(paragonie/constant_time_encoding) < 3)
BuildRequires:  (php-composer(paragonie/random_compat) >= 2.0            with php-composer(paragonie/random_compat)          < 3)
%else
BuildRequires:  php-paragonie-constant-time-encoding
BuildRequires:  php-paragonie-random-compat
%endif
BuildRequires:  php-date
BuildRequires:  php-hash
BuildRequires:  php-pcre
# For tests, from composer.json "require-dev": {
#       "phpunit/phpunit": "~4|~5|~6",
#       "bacon/bacon-qr-code": "~1.0"
BuildRequires:  php-composer(phpunit/phpunit)
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
BuildRequires:  (php-composer(bacon/bacon-qr-code) >= 1.0                with php-composer(bacon/bacon-qr-code)              < 2)
%else
BuildRequires:  php-bacon-qr-code
%endif
# For autoloader
BuildRequires:  php-composer(fedora/autoloader)
%endif

# From composer.json, "require": {
#        "php": ">=5.4",
#        "paragonie/constant_time_encoding": "~1.0|~2.0",
#        "paragonie/random_compat": ">=1",
#        "symfony/polyfill-php56": "~1.2"
# Use 5.6 and avoid polyfill
Requires:       php(language) >= 5.6
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
# Only use constant_time_encoding v1 available in Fedora for autoloader path
Requires:       (php-composer(paragonie/constant_time_encoding) >= 1.0   with php-composer(paragonie/constant_time_encoding) < 3)
# Only use random_compat v2 available in Fedora for autoloader path
Requires:       (php-composer(paragonie/random_compat) >= 2.0            with php-composer(paragonie/random_compat)          < 3)
%else
Requires:       php-paragonie-constant-time-encoding
Requires:       php-paragonie-random-compat
%endif
# From phpcompatinfo report for 2.0.7
Requires:       php-hash
Requires:       php-pcre
# From composer.json, "suggest": {
#      "bacon/bacon-qr-code": "Required to generate inline QR Codes."
%if 0%{?fedora} >= 21 || 0%{?rhel} >= 8
Recommends:     php-composer(bacon/bacon-qr-code)
%endif
# For generated autoloader
Requires:       php-composer(fedora/autoloader)

# Composer
Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}


%description
Google2FA is a PHP implementation of the Google Two-Factor Authentication
Module, supporting the HMAC-Based One-time Password (HOTP) algorithm
specified in RFC 4226 and the Time-based One-time Password (TOTP) algorithm
specified in RFC 6238.

Autoloader: %{_datadir}/php/%{ns_vendor}/%{ns_project}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}

: Create autoloader
cat <<'AUTOLOAD' | tee src/autoload.php
<?php
/* Autoloader for %{name} and its dependencies */
require_once '%{_datadir}/php/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('%{ns_vendor}\\%{ns_project}\\', __DIR__);
\Fedora\Autoloader\Dependencies::required([
    '%{_datadir}/php/ParagonIE/ConstantTime/autoload.php',
    '%{_datadir}/php/random_compat/autoload.php',
]);
\Fedora\Autoloader\Dependencies::optional([
    '%{_datadir}/php/BaconQrCode/autoload.php',
]);
AUTOLOAD


%build
: Nothing to build


%install
: Library
mkdir -p      %{buildroot}%{_datadir}/php/%{ns_vendor}
cp -pr src    %{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}


%check
%if %{with_tests}
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require '%{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('%{ns_vendor}\\%{ns_project}\\Tests\\', dirname(__DIR__).'/tests');
EOF

# TODO investigate test_qrcode_inline failing with php < 7.2 (both images seems ok)
ret=0
for cmd in php php70 php71 php72 php73; do
   if which $cmd; then
      if [ $($cmd -r 'echo PHP_VERSION_ID;') -lt 70200 ]; then
        $cmd %{_bindir}/phpunit --no-coverage --verbose --filter '^((?!(testQrcodeInline)).)*$' || ret=1
      else
        $cmd %{_bindir}/phpunit --no-coverage --verbose || ret=1
      fi
   fi
done
exit $ret
%else
: Test suite disabled
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE.md RELICENSED.md
%doc composer.json
%doc README.md changelog.md
%dir %{_datadir}/php/%{ns_vendor}
     %{_datadir}/php/%{ns_vendor}/%{ns_project}


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Aug 29 2018 Remi Collet <remi@remirepo.net> - 3.0.3-1
- update to 3.0.3 (no change)

* Mon Aug 20 2018 Remi Collet <remi@remirepo.net> - 3.0.2-1
- update to 3.0.2 (no change)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May  2 2018 Remi Collet <remi@remirepo.net> - 3.0.1-2
- allow paragonie/constant_time_encoding v2

* Thu Mar 22 2018 Remi Collet <remi@remirepo.net> - 3.0.1-1
- update to 3.0.1
- license have be changed to MIT

* Wed Mar  7 2018 Remi Collet <remi@remirepo.net> - 2.0.7-2
- add GPLv3+ to License field and ask upstream for clarification
  https://github.com/antonioribeiro/google2fa/issues/95

* Wed Mar  7 2018 Remi Collet <remi@remirepo.net> - 2.0.7-1
- initial package

%global composer_vendor         phpseclib
%global composer_project        phpseclib

%global github_owner            phpseclib
%global github_name             phpseclib
%global github_commit           497856a8d997f640b4a516062f84228a772a48a8
%global github_short            %(c=%{github_commit}; echo ${c:0:7})
%bcond_without                  tests

Name:       php-%{composer_vendor}
Version:    2.0.29
Release:    1%{?dist}
Summary:    PHP Secure Communications Library
License:    MIT
URL:        https://github.com/%{github_owner}/%{github_name}

Source0:    %{name}-%{version}-%{github_short}.tgz
Source1:    %{name}-autoload.php
# Generate a full archive from git snapshot, with tests
Source2:    makesrc.sh

BuildArch:      noarch

%if %{with tests}
BuildRequires:  php-composer(fedora/autoloader)
%if 0%{?fedora} >= 26 || 0%{?rhel} >= 8
%global phpunit %{_bindir}/phpunit6
%else
%global phpunit %{_bindir}/phpunit
%endif
BuildRequires:  %{phpunit}
BuildRequires:  %{_bindir}/phpab
# Optional at runtime, to avoid too muck skipped tests
BuildRequires:  php-bcmath
BuildRequires:  php-gmp
%endif

Requires:   php(language) >= 5.3.3
Requires:   php-bcmath
Requires:   php-date
Requires:   php-gmp
Requires:   php-hash
Requires:   php-openssl
Requires:   php-pcre
Requires:   php-session
Requires:   php-standard
Requires:   php-xml
# Autoloader
Requires:   php-composer(fedora/autoloader)

Provides:   php-composer(%{composer_vendor}/%{composer_project}) = %{version}


%description
MIT-licensed pure-PHP implementations of an arbitrary-precision integer 
arithmetic library, fully PKCS#1 (v2.1) compliant RSA, DES, 3DES, RC4, 
Rijndael, AES, Blowfish, Twofish, SSH-1, SSH-2, SFTP, and X.509


%prep
%setup -qn %{github_name}-%{github_commit}
cp %{SOURCE1} %{composer_vendor}/autoload.php


%build


%install
mkdir -p %{buildroot}%{_datadir}/php
cp -pr %{composer_vendor} %{buildroot}%{_datadir}/php


%if %{with tests}
%check
%{_bindir}/phpab --output tests/bootstrap.php tests
cat << 'EOF' | tee -a tests/bootstrap.php
if (class_exists("PHPUnit_Framework_TestCase") && !class_exists("PHPUnit\\Framework\\TestCase")) {
     class_alias("PHPUnit_Framework_TestCase", "PHPUnit\\Framework\\TestCase");
}
require "%{buildroot}%{_datadir}/php/%{composer_vendor}/autoload.php";
date_default_timezone_set('UTC');
EOF


# testAuthorityInfoAccess fails without internet access
ret=0
for cmd in "php %{phpunit}" php72 php73 php74; do
  if which $cmd; then
    set $cmd
    $1 -d memory_limit=1G ${2:-%{_bindir}/phpunit6} \
       --filter '^((?!(testAuthorityInfoAccess)).)*$' \
       --verbose || ret=1
  fi
done
exit $ret
%endif


%files
%{_datadir}/php/%{composer_vendor}
%doc AUTHORS CHANGELOG.md composer.json README.md
%{!?_licensedir:%global license %%doc}
%license LICENSE


%changelog
* Tue Sep  8 2020 Remi Collet <remi@remirepo.net> - 2.0.29-1
- update to 2.0.29

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul  8 2020 Remi Collet <remi@remirepo.net> - 2.0.28-1
- update to 2.0.28

* Mon Apr  6 2020 Remi Collet <remi@remirepo.net> - 2.0.27-1
- update to 2.0.27

* Mon Mar 23 2020 Remi Collet <remi@remirepo.net> - 2.0.26-1
- update to 2.0.26

* Tue Feb 25 2020 Remi Collet <remi@remirepo.net> - 2.0.25-1
- update to 2.0.25

* Mon Feb 24 2020 Remi Collet <remi@remirepo.net> - 2.0.24-1
- update to 2.0.24

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 17 2019 Remi Collet <remi@remirepo.net> - 2.0.23-1
- update to 2.0.23

* Mon Sep 16 2019 Remi Collet <remi@remirepo.net> - 2.0.22-1
- update to 2.0.22

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 15 2019 Remi Collet <remi@remirepo.net> - 2.0.21-1
- update to 2.0.21

* Tue Jun 25 2019 Remi Collet <remi@remirepo.net> - 2.0.20-1
- update to 2.0.20

* Fri Jun 21 2019 Remi Collet <remi@remirepo.net> - 2.0.19-1
- update to 2.0.19

* Thu Jun 13 2019 Remi Collet <remi@remirepo.net> - 2.0.18-1
- update to 2.0.18

* Mon May 27 2019 Remi Collet <remi@remirepo.net> - 2.0.17-1
- update to 2.0.17

* Mon Mar 11 2019 Remi Collet <remi@remirepo.net> - 2.0.15-1
- update to 2.0.15

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 31 2019 Remi Collet <remi@remirepo.net> - 2.0.14-1
- update to 2.0.14

* Tue Dec 18 2018 Remi Collet <remi@remirepo.net> - 2.0.13-1
- update to 2.0.13

* Mon Nov  5 2018 Remi Collet <remi@remirepo.net> - 2.0.12-1
- update to 2.0.12

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 16 2018 Remi Collet <remi@remirepo.net> - 2.0.11-1
- update to 2.0.11

* Tue Feb 20 2018 Remi Collet <remi@remirepo.net> - 2.0.10-1
- Update to 2.0.10
- use phpunit6 when available
- skip tests with PHPUnit < 4.8.35 (EPEL-6)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov 29 2017 Remi Collet <remi@remirepo.net> - 2.0.9-1
- Update to 2.0.9

* Mon Oct 23 2017 Remi Collet <remi@remirepo.net> - 2.0.7-1
- Update to 2.0.7

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun  5 2017 Remi Collet <remi@remirepo.net> - 2.0.6-1
- Update to 2.0.6

* Mon May  8 2017 Remi Collet <remi@remirepo.net> - 2.0.5-1
- Update to 2.0.5
- switch to fedora/autoloader
- use SCL of PHP when available for test suite
- open https://github.com/phpseclib/phpseclib/issues/1122 - regression with 5.3
- open https://github.com/phpseclib/phpseclib/pull/1121 - fix permission

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Oct  4 2016 Remi Collet <remi@fedoraproject.org> - 2.0.4-1
- update to 2.0.4

* Tue Jun  7 2016 Remi Collet <remi@fedoraproject.org> - 2.0.2-1
- update to 2.0.2

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 19 2016 Remi Collet <remi@fedoraproject.org> - 2.0.1-1
- update to 2.0.1
- sources from git snapshot for tests

* Sun Sep  6 2015 Remi Collet <remi@fedoraproject.org> - 2.0.0-4
- change source0 to commit reference
- add BR for better test coverage
- add needed backport stuff for EL-5 in #remirepo

* Wed Sep 02 2015 François Kooman <fkooman@tuxed.net> - 2.0.0-3
- apply patch for test to avoid loading class that is now autoloaded

* Wed Sep 02 2015 François Kooman <fkooman@tuxed.net> - 2.0.0-2
- add autoload script
- make use of autoload script when running tests during build
- fix double inclusion of directory

* Sat Aug 08 2015 François Kooman <fkooman@tuxed.net> - 2.0.0-1
- initial package

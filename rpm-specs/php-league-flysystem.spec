# remirepo/fedora spec file for php-league-flysystem
#
# Copyright (c) 2016-2019 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
# Github
%global gh_commit    021569195e15f8209b1c4bebb78bd66aa4f08c21
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     thephpleague
%global gh_project   flysystem
# Packagist
%global pk_vendor    league
%global pk_name      flysystem
# PSR-0 namespace
%global ns_vendor    League
%global ns_project   Flysystem

Name:           php-%{pk_vendor}-%{pk_name}
Version:        1.0.66
Release:        1%{?dist}
Summary:        Filesystem abstraction: Many filesystems, one API

License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
# Create git snapshot as tests are excluded from official tarball
Source1:        makesrc.sh

BuildArch:      noarch
# As we use phpunit 6 and phpspec 5
BuildRequires:  php(language) >= 7.2
BuildRequires:  php-date
BuildRequires:  php-fileinfo
BuildRequires:  php-ftp
BuildRequires:  php-hash
BuildRequires:  php-mbstring
BuildRequires:  php-pcre
BuildRequires:  php-spl
# From composer.json, "require-dev": {
#        "phpspec/phpspec": "^3.4",
#        "phpunit/phpunit": "^5.7.26"
BuildRequires:  php-composer(phpspec/phpspec) >= 3.4
BuildRequires:  phpunit6
# Autoloader
BuildRequires:  php-composer(fedora/autoloader)

# From composer.json, "require": {
#        "php": ">=5.5.9",
#        "ext-fileinfo": "*"
Requires:       php(language) >= 5.5.9
Requires:       php-fileinfo
# From phpcompatifo report for 1.0.49
Requires:       php-date
Requires:       php-ftp
Requires:       php-hash
Requires:       php-mbstring
Requires:       php-pcre
Requires:       php-spl
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_vendor}/%{pk_name}) = %{version}


%description
Flysystem is a filesystem abstraction which allows you to easily swap out
a local filesystem for a remote one.

Autoloader: %{_datadir}/php/%{ns_vendor}/%{ns_project}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}


%build
: Create autoloader
cat <<'AUTOLOAD' | tee src/autoload.php
<?php
/* Autoloader for %{name} and its dependencies */
require_once '%{_datadir}/php/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('%{ns_vendor}\\%{ns_project}\\', __DIR__);
AUTOLOAD


%install
# Restore PSR-0 tree
mkdir -p   %{buildroot}%{_datadir}/php/%{ns_vendor}
cp -pr src %{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}


%check
: Generate a simple autoloader
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
// Installed library
require '%{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}/autoload.php';

// Test suite
\Fedora\Autoloader\Autoload::addPsr4('%{ns_vendor}\\%{ns_project}\\Stub\\', dirname(__DIR__).'/stub');
require_once dirname(__DIR__) . '/tests/PHPUnitHacks.php';
EOF

: Fix bootstraping
sed -e 's/file="[^"]*"//' -i phpunit.xml
echo 'bootstrap: vendor/autoload.php' >>phpspec.yml

PHPSPECVER=$(%{_bindir}/phpspec --version | sed 's/.* //;s/\..*//')
if [ "$PHPSPECVER" -lt 3 ]
then PHPSPEC=/dev/null
else PHPSPEC=%{_bindir}/phpspec
fi

ret=0
for cmd in php php72 php73 php74; do
  if which $cmd; then
   : Run upstream test suite
   $cmd $PHPSPEC run || ret=1
   $cmd %{_bindir}/phpunit6 \
     --exclude-group integration \
     --filter '^((?!(testPathinfoHandlesUtf8|testStreamSizeForUrl|testListingFromUnixFormat)).)*$' \
     --no-coverage --verbose || ret=1
  fi
done
exit $ret


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc *.md
%doc composer.json
%{_datadir}/php/%{ns_vendor}


%changelog
* Wed Mar 18 2020 Remi Collet <remi@remirepo.net> - 1.0.66-1
- update to 1.0.66

* Mon Mar  9 2020 Remi Collet <remi@remirepo.net> - 1.0.65-1
- update to 1.0.65

* Thu Feb  6 2020 Remi Collet <remi@remirepo.net> - 1.0.64-1
- update to 1.0.64

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.63-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan  6 2020 Remi Collet <remi@remirepo.net> - 1.0.63-1
- update to 1.0.63

* Mon Dec  9 2019 Remi Collet <remi@remirepo.net> - 1.0.61-1
- update to 1.0.61

* Thu Oct 17 2019 Remi Collet <remi@remirepo.net> - 1.0.57-1
- update to 1.0.57

* Sun Oct 13 2019 Remi Collet <remi@remirepo.net> - 1.0.56-1
- update to 1.0.56
- drop patch merged upstream

* Fri Oct 11 2019 Remi Collet <remi@remirepo.net> - 1.0.55-2
- add patch for PHP 7.4 from
  https://github.com/thephpleague/flysystem/pull/1081

* Mon Aug 26 2019 Remi Collet <remi@remirepo.net> - 1.0.55-1
- update to 1.0.55

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.53-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 19 2019 Remi Collet <remi@remirepo.net> - 1.0.53-1
- update to 1.0.53

* Tue May 21 2019 Remi Collet <remi@remirepo.net> - 1.0.52-1
- update to 1.0.52

* Mon Apr  1 2019 Remi Collet <remi@remirepo.net> - 1.0.51-1
- update to 1.0.51

* Fri Feb  1 2019 Remi Collet <remi@remirepo.net> - 1.0.50-1
- update to 1.0.50

* Mon Nov 26 2018 Remi Collet <remi@remirepo.net> - 1.0.49-1
- update to 1.0.49

* Tue Oct 16 2018 Remi Collet <remi@remirepo.net> - 1.0.48-1
- update to 1.0.48

* Sat Sep 15 2018 Remi Collet <remi@remirepo.net> - 1.0.47-1
- update to 1.0.47

* Wed Aug 22 2018 Remi Collet <remi@remirepo.net> - 1.0.46-1
- update to 1.0.46

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.45-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon May 14 2018 Remi Collet <remi@remirepo.net> - 1.0.45-1
- update to 1.0.45

* Mon Apr  9 2018 Remi Collet <remi@remirepo.net> - 1.0.44-1
- update to 1.0.44

* Thu Mar  1 2018 Remi Collet <remi@remirepo.net> - 1.0.43-1
- Update to 1.0.43

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.42-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 29 2018 Remi Collet <remi@remirepo.net> - 1.0.42-1
- Update to 1.0.42
- switch to phpunit 6 and phpspec 4

* Mon Aug  7 2017 Remi Collet <remi@remirepo.net> - 1.0.41-1
- Update to 1.0.41

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.40-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Apr 28 2017 Remi Collet <remi@remirepo.net> - 1.0.40-1
- Update to 1.0.40

* Wed Apr 26 2017 Remi Collet <remi@remirepo.net> - 1.0.39-1
- Update to 1.0.39

* Mon Apr 24 2017 Remi Collet <remi@remirepo.net> - 1.0.38-1
- Update to 1.0.38

* Thu Mar 23 2017 Remi Collet <remi@remirepo.net> - 1.0.37-1
- Update to 1.0.37

* Mon Mar 20 2017 Remi Collet <remi@remirepo.net> - 1.0.36-1
- Update to 1.0.36

* Thu Feb  9 2017 Remi Collet <remi@fedoraproject.org> - 1.0.35-1
- update to 1.0.35

* Wed Feb  1 2017 Remi Collet <remi@fedoraproject.org> - 1.0.34-1
- update to 1.0.34

* Mon Jan 23 2017 Remi Collet <remi@fedoraproject.org> - 1.0.33-1
- update to 1.0.33 (windows only)
- switch to fedora/autoloader

* Wed Oct 19 2016 Remi Collet <remi@fedoraproject.org> - 1.0.30-1
- update to 1.0.30
- lower dependency on PHP 5.5.9

* Tue Oct 18 2016 Remi Collet <remi@fedoraproject.org> - 1.0.29-1
- update to 1.0.29
- raise dependency on PHP 5.6

* Fri Oct  7 2016 Remi Collet <remi@fedoraproject.org> - 1.0.28-1
- update to 1.0.28

* Wed Aug 10 2016 Remi Collet <remi@fedoraproject.org> - 1.0.27-1
- update to 1.0.27

* Wed Aug  3 2016 Remi Collet <remi@fedoraproject.org> - 1.0.26-1
- update to 1.0.26

* Mon Jul 18 2016 Remi Collet <remi@fedoraproject.org> - 1.0.25-1
- update to 1.0.25
- disable spec test suite with phpspec 3

* Sat Jun  4 2016 Remi Collet <remi@fedoraproject.org> - 1.0.24-1
- update to 1.0.24

* Thu Apr 28 2016 Remi Collet <remi@fedoraproject.org> - 1.0.22-1
- update to 1.0.22

* Fri Apr 22 2016 Remi Collet <remi@fedoraproject.org> - 1.0.21-1
- update to 1.0.21

* Tue Mar 15 2016 Remi Collet <remi@fedoraproject.org> - 1.0.20-1
- update to 1.0.20

* Tue Mar  8 2016 Remi Collet <remi@fedoraproject.org> - 1.0.18-1
- update to 1.0.18

* Sat Feb 20 2016 Remi Collet <remi@fedoraproject.org> - 1.0.17-1
- update to 1.0.17

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 14 2016 Remi Collet <remi@fedoraproject.org> - 1.0.16-1
- initial package
- open https://github.com/thephpleague/flysystem/pull/592 - PHPUnit

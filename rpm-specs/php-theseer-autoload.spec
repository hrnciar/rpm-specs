# remirepo/fedora spec file for php-theseer-autoload
#
# Copyright (c) 2014-2019 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

# For compatibility with SCL
%undefine __brp_mangle_shebangs

%global gh_commit    7b667d946d897770e3285e52bb85d3b1f0be21a3
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     theseer
%global gh_project   Autoload
%global php_home     %{_datadir}/php/TheSeer
%global pear_name    Autoload
%global pear_channel pear.netpirates.net

Name:           php-theseer-autoload
Version:        1.25.9
Release:        1%{?dist}
Summary:        A tool and library to generate autoload code

License:        BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{name}-%{version}-%{?gh_short}.tar.gz

# Autoloader path
Patch0:         %{gh_project}-rpm.patch

BuildArch:      noarch
BuildRequires:  php(language) >= 5.3.1
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
BuildRequires: (php-composer(theseer/directoryscanner)     >= 1.3  with php-composer(theseer/directoryscanner)     < 2)
BuildRequires: (php-composer(zetacomponents/console-tools) >= 1.7  with php-composer(zetacomponents/console-tools) < 2)
%global phpunit %{_bindir}/phpunit7
%else
BuildRequires:  php-composer(theseer/directoryscanner) <  2
BuildRequires:  php-composer(theseer/directoryscanner) >= 1.3
BuildRequires:  php-composer(zetacomponents/console-tools) <  2
BuildRequires:  php-composer(zetacomponents/console-tools) >= 1.7
%global phpunit %{_bindir}/phpunit
%endif
BuildRequires:  %{phpunit}

# From composer.json, "require": {
#        "theseer/directoryscanner": "^1.3",
#        "zetacomponents/console-tools": "^1.7.1"
Requires:       php(language) >= 5.3.1
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
Requires:      (php-composer(theseer/directoryscanner)     >= 1.3  with php-composer(theseer/directoryscanner)     < 2)
Requires:      (php-composer(zetacomponents/console-tools) >= 1.7  with php-composer(zetacomponents/console-tools) < 2)
%else
Requires:       php-composer(theseer/directoryscanner) <  2
Requires:       php-composer(theseer/directoryscanner) >= 1.3
Requires:       php-composer(zetacomponents/console-tools) <  2
Requires:       php-composer(zetacomponents/console-tools) >= 1.7
%endif
# From phpcompatinfo report for version 1.25.0
Requires:       php-cli
Requires:       php-date
Requires:       php-json
Requires:       php-openssl
Requires:       php-phar
Requires:       php-spl
Requires:       php-tokenizer
# Optional xdebug

Provides:       php-pear(%{pear_channel}/%{pear_name}) = %{version}
Provides:       php-composer(theseer/autoload) = %{version}


%description
The PHP AutoloadBuilder CLI tool phpab is a command line application
to automate the process of generating an autoload require file with
the option of creating static require lists as well as phar archives.


%prep
%setup -q -n %{gh_project}-%{gh_commit}

%patch0 -p0 -b .rpm

: drop composer dependencies
sed -e '\:../vendor/:d'    -i src/autoload.php

: add package dependencies
cat <<EOF | tee            -a src/autoload.php
// Dependencies
require '/usr/share/php/TheSeer/DirectoryScanner/autoload.php';
require '/usr/share/php/ezc/Base/base.php';
spl_autoload_register(array('\\ezcBase','autoload'));
EOF

# set version
sed -e 's/@VERSION@/%{version}/' -i phpab.php


%build
# Empty build section, most likely nothing required.


%install
mkdir -p   %{buildroot}%{php_home}
cp -pr src %{buildroot}%{php_home}/%{gh_project}

install -Dpm 0755 phpab.php %{buildroot}%{_bindir}/phpab


%check
: Check version
sed -e 's:%{php_home}:%{buildroot}%{php_home}:' phpab.php >t.php
php t.php --version | grep %{version}
php t.php --output foo.php src

: Fix test suite to use installed library
cat <<EOF | tee tests/init.php
<?php
require '%{buildroot}%{_datadir}/php/TheSeer/Autoload/autoload.php';
class_exists('PHPUnit\Framework\TestCase') or class_alias('PHPUnit_Framework_TestCase', 'PHPUnit\Framework\TestCase');
EOF

ret=0
for cmd in "php %{phpunit}" "php56 %{_bindir}/phpunit" "php70 %{_bindir}/phpunit6" php71 php72 php73 php74; do
  if which $cmd; then
    set $cmd
    $1 ${2:-%{_bindir}/phpunit7} --verbose || ret=1
  fi
done
exit $ret


%pre
if [ -x %{_bindir}/pear ]; then
  %{_bindir}/pear uninstall --nodeps --ignore-errors --register-only \
      %{pear_channel}/%{pear_name} >/dev/null || :
fi


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc README.md composer.json
%{php_home}/%{gh_project}
%{_bindir}/phpab


%changelog
* Fri Mar 20 2020 Remi Collet <remi@remirepo.net> - 1.25.9-1
- update to 1.25.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.25.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 25 2019 Remi Collet <remi@remirepo.net> - 1.25.8-1
- update to 1.25.8

* Fri Nov 15 2019 Remi Collet <remi@remirepo.net> - 1.25.7-1
- update to 1.25.7

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.25.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 16 2019 Remi Collet <remi@remirepo.net> - 1.25.6-1
- update to 1.25.6

* Thu Apr 25 2019 Remi Collet <remi@remirepo.net> - 1.25.5-1
- update to 1.25.5

* Fri Apr 19 2019 Remi Collet <remi@remirepo.net> - 1.25.4-1
- update to 1.25.4

* Mon Feb 11 2019 Remi Collet <remi@remirepo.net> - 1.25.3-1
- update to 1.25.3

* Mon Feb  4 2019 Remi Collet <remi@remirepo.net> - 1.25.2-1
- update to 1.25.2

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.25.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Oct 20 2018 Remi Collet <remi@remirepo.net> - 1.25.1-1
- update to 1.25.1
- drop patch merged upstream

* Mon Oct 15 2018 Remi Collet <remi@remirepo.net> - 1.25.0-3
- add upstream patch for PHP 7.3

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.25.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul  2 2018 Remi Collet <remi@remirepo.net> - 1.25.0-1
- update to 1.25.0
- use range dependencies

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.24.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.24.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 26 2017 Remi Collet <remi@remirepo.net> - 1.24.1-1
- Update to 1.24.1
- drop patch merged upstream

* Mon Jun 26 2017 Remi Collet <remi@remirepo.net> - 1.24.0-1
- Update to 1.24.0
- use phpunit6 on F26+
- add patch for PHP 5.3 in EL-6 from
  https://github.com/theseer/Autoload/pull/78

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.23.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Dec 21 2016 Remi Collet <remi@fedoraproject.org> - 1.23.0-1
- update to 1.23.0

* Sat Aug 13 2016 Remi Collet <remi@fedoraproject.org> - 1.22.0-1
- update to 1.22.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.21.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Nov 11 2015 Remi Collet <remi@fedoraproject.org> - 1.21.0-1
- update to 1.21.0

* Sun Oct  4 2015 Remi Collet <remi@fedoraproject.org> - 1.20.3-1
- update to 1.20.3

* Sat Jul 25 2015 Remi Collet <remi@fedoraproject.org> - 1.20.0-1
- update to 1.20.0

* Thu Jul 16 2015 Remi Collet <remi@fedoraproject.org> - 1.19.2-2
- swicth from eZ to Zeta Components

* Tue Jul 14 2015 Remi Collet <remi@fedoraproject.org> - 1.19.2-1
- update to 1.19.2

* Thu Jul  2 2015 Remi Collet <remi@fedoraproject.org> - 1.19.0-1
- update to 1.19.0

* Wed Jul  1 2015 Remi Collet <remi@fedoraproject.org> - 1.18.0-1
- update to 1.18.0
- load dependencies in the autoloader (not in the command)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.17.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 15 2015 Remi Collet <remi@fedoraproject.org> - 1.17.0-1
- Update to 1.17.0

* Tue Nov 25 2014 Remi Collet <remi@fedoraproject.org> - 1.16.2-1
- Update to 1.16.2
- switch from pear to github sources

* Wed Nov 12 2014 Remi Collet <remi@fedoraproject.org> - 1.16.0-2
- define date.timezone in phpab command to avoid warning

* Tue Sep 02 2014 Remi Collet <remi@fedoraproject.org> - 1.16.0-1
- Update to 1.16.0

* Thu Aug 14 2014 Remi Collet <remi@fedoraproject.org> - 1.15.1-1
- Update to 1.15.1

* Tue Aug 12 2014 Remi Collet <remi@fedoraproject.org> - 1.15.0-1
- Update to 1.15.0

* Thu Apr 24 2014 Remi Collet <remi@fedoraproject.org> - 1.14.2-1
- Update to 1.14.2

* Sun Apr  6 2014 Remi Collet <remi@fedoraproject.org> - 1.14.1-1
- initial package, version 1.14.1

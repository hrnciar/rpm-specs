# remirepo/fedora spec file for php-myclabs-deep-copy
#
# Copyright (c) 2015-2019 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global gh_commit    969b211f9a51aa1f6c01d1d2aef56d3bd91598e5
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     myclabs
%global gh_project   DeepCopy
%global c_project    deep-copy
%global major        %nil
%global php_home     %{_datadir}/php
%bcond_without       tests

Name:           php-myclabs-deep-copy%{major}
Version:        1.10.1
Release:        2%{?dist}

Summary:        Create deep copies (clones) of your objects

License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
# git snashop to get upstream test suite
Source0:        php-myclabs-deep-copy-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh
Source2:        php-myclabs-deep-copy-autoload.php

BuildArch:      noarch
%if %{with tests}
# For tests
BuildRequires:  php(language) >= 7.1
BuildRequires:  php-reflection
BuildRequires:  php-spl
# From composer.json, "require-dev": {
#        "doctrine/collections": "^1.0",
#        "doctrine/common": "^2.6",
#        "phpunit/phpunit": "^7.1"
BuildRequires: (php-composer(doctrine/collections) >= 1.0   with php-composer(doctrine/collections) < 2)
BuildRequires: (php-composer(doctrine/common)      >= 2.6   with php-composer(doctrine/common)      < 3)
BuildRequires:  phpunit7 >= 7.1
# Required by autoloader
BuildRequires:  php-composer(fedora/autoloader)
%endif

# From composer.json, "require": {
#        "php": "^7.1 || ^8.0"
Requires:       php(language) >= 7.1
# From phpcompatinfo report for version 1.8.0
Requires:       php-reflection
Requires:       php-date
Requires:       php-spl
# Required by autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{gh_owner}/%{c_project}) = %{version}


%description
DeepCopy helps you create deep copies (clones) of your objects.
It is designed to handle cycles in the association graph.


%prep
%setup -q -n %{gh_project}-%{gh_commit}

cp %{SOURCE2} src/%{gh_project}/autoload.php


%build
# Empty build section, most likely nothing required.


%install
: Library
mkdir -p %{buildroot}%{php_home}
cp -pr src/%{gh_project} %{buildroot}%{php_home}/%{gh_project}%{major}


%check
%if %{with tests}
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require '%{buildroot}%{php_home}/%{gh_project}%{major}/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('DeepCopy\\', dirname(__DIR__).'/fixtures/');
\Fedora\Autoloader\Autoload::addPsr4('DeepCopyTest\\', dirname(__DIR__).'/tests/DeepCopyTest/');
require_once '%{php_home}/Doctrine/Common/Collections/autoload.php';
require_once '%{php_home}/Doctrine/Common/autoload.php';
EOF

ret=0
for cmd in php php72 php73 php74 php80; do
  if which $cmd; then
    $cmd -d auto_prepend_file=%{buildroot}%{php_home}/%{gh_project}%{major}/autoload.php \
         %{_bindir}/phpunit7 --verbose || ret=1
  fi
done
exit $ret
%else
: Test suite disabled
%endif


%files
%license LICENSE
%doc composer.json
%doc README.md
%{php_home}/%{gh_project}%{major}


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 30 2020 Remi Collet <remi@remirepo.net> - 1.10.1-1
- update to 1.10.1

* Mon Jun 29 2020 Remi Collet <remi@remirepo.net> - 1.10.0-2
- update to 1.10.0 (no change)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 20 2020 Remi Collet <remi@remirepo.net> - 1.9.5-1
- update to 1.9.5

* Mon Dec 16 2019 Remi Collet <remi@remirepo.net> - 1.9.4-1
- update to 1.9.4

* Mon Aug 12 2019 Remi Collet <remi@remirepo.net> - 1.9.3-1
- update to 1.9.3 (no change)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 15 2019 Remi Collet <remi@remirepo.net> - 1.9.1-1
- update to 1.9.1

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 12 2018 Remi Collet <remi@remirepo.net> - 1.8.1-1
- update to 1.8.1

* Wed May 30 2018 Remi Collet <remi@remirepo.net> - 1.8.0-1
- update to 1.8.0 (no change)
- raise dependency on PHP 7.1
- use phpunit7

* Wed May 30 2018 Remi Collet <remi@remirepo.net> - 1.8.0-0
- update to 1.8.0 (no change)
- boostrap build using phpunit6 (rely on include_path)
- fix autoloader to avoid duplicate definition

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Oct 20 2017 Remi Collet <remi@remirepo.net> - 1.7.0-1
- Update to 1.7.0
- raise dependency on PHP 5.6

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Apr 13 2017 Remi Collet <remi@remirepo.net> - 1.6.1-1
- Update to 1.6.1

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Remi Collet <remi@fedoraproject.org> - 1.6.0-1
- update to 1.6.0

* Tue Nov  1 2016 Remi Collet <remi@fedoraproject.org> - 1.5.5-1
- update to 1.5.5
- switch to fedora/autoloader

* Mon Sep 19 2016 Remi Collet <remi@fedoraproject.org> - 1.5.4-1
- update to 1.5.4

* Tue Sep 13 2016 Remi Collet <remi@fedoraproject.org> - 1.5.3-1
- update to 1.5.3

* Wed Sep  7 2016 Remi Collet <remi@fedoraproject.org> - 1.5.2-1
- update to 1.5.2

* Mon May  2 2016 Remi Collet <remi@fedoraproject.org> - 1.5.1-1
- update to 1.5.1
- run test suite with both PHP 5 and 7 when available

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Nov  8 2015 Remi Collet <remi@fedoraproject.org> - 1.5.0-1
- update to 1.5.0

* Mon Oct  5 2015 Remi Collet <remi@fedoraproject.org> - 1.4.0-1
- update to 1.4.0

* Mon Jul 20 2015 Remi Collet <remi@fedoraproject.org> - 1.3.1-1
- update to 1.3.1 (no change, pr #14 merged)

* Sat Jul  4 2015 Remi Collet <remi@fedoraproject.org> - 1.3.0-1
- initial package, version 1.3.0
- open https://github.com/myclabs/DeepCopy/pull/14 - fix perms

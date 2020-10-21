#
# Fedora spec file for php-guzzlehttp-promises
#
# Copyright (c) 2015-2016 Shawn Iwinski <shawn.iwinski@gmail.com>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     guzzle
%global github_name      promises
%global github_version   1.3.1
%global github_commit    a59da6cf61d80060647ff4d3eb2c03a2bc694646

%global composer_vendor  guzzlehttp
%global composer_project promises

# "php": ">=5.5.0"
%global php_min_ver 5.5.0

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       9%{?github_release}%{?dist}
Summary:       Guzzle promises library

License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}

# GitHub export does not include tests.
# Run php-guzzlehttp-promises.sh to create full source.
Source0:       %{name}-%{github_version}-%{github_commit}.tar.gz
Source1:       %{name}-get-source.sh

BuildArch:     noarch
# Tests
%if %{with_tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: php-composer(phpunit/phpunit)
## phpcompatinfo (computed from version 1.3.1)
BuildRequires: php-json
BuildRequires: php-reflection
BuildRequires: php-spl
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
# phpcompatinfo (computed from version 1.3.1)
Requires:      php-json
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
Promises/A+ [1] implementation that handles promise chaining and resolution
interactively, allowing for "infinite" promise chaining while keeping the
stack size constant.

Autoloader: %{phpdir}/GuzzleHttp/Promise/autoload.php

[1] https://promisesaplus.com/


%prep
%setup -qn %{github_name}-%{github_commit}

: Create autoloader
cat <<'AUTOLOAD' | tee src/autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 */
require_once '%{phpdir}/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('GuzzleHttp\\Promise\\', __DIR__);

require_once __DIR__ . '/functions_include.php';
AUTOLOAD


%build
# Empty build section, nothing required


%install
mkdir -p %{buildroot}%{phpdir}/GuzzleHttp/Promise
cp -rp src/* %{buildroot}%{phpdir}/GuzzleHttp/Promise/


%check
%if %{with_tests}
sed "s#require.*autoload.*#require '%{buildroot}%{phpdir}/GuzzleHttp/Promise/autoload.php';#" \
    -i tests/bootstrap.php

: Upstream tests
%{_bindir}/phpunit --verbose

: Upstream tests with SCLs if available
SCL_RETURN_CODE=0
for SCL in php56 php70 php71; do
    if which $SCL; then
       $SCL %{_bindir}/phpunit || SCL_RETURN_CODE=1
    fi
done
exit $SCL_RETURN_CODE
%else
: Tests skipped
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc *.md
%doc composer.json
%dir %{phpdir}/GuzzleHttp
     %{phpdir}/GuzzleHttp/Promise


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Dec 07 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.3.1-1
- Updated to 1.3.1 (RHBZ #1406764)
- Run upstream tests with SCLs if they are available

* Wed Dec 07 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.3.0-1
- Updated to 1.3.0 (RHBZ #1396687)
- Change autoloader from php-composer(symfony/class-loader) to
  php-composer(fedora/autoloader)

* Sun May 29 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.2.0-1
- Updated to 1.2.0 (RHBZ #1337366)

* Sun Mar 13 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.1.0-1
- Updated to 1.1.0 (RHBZ #1315685)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Oct 26 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.0.3-1
- Updated to 1.0.3 (RHBZ #1272280)

* Sun Aug 16 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.0.2-1
- Updated to 1.0.2 (RHBZ #1253996)

* Sun Jul 19 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.0.1-3
- Use full paths in autoloader

* Wed Jul 08 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.0.1-2
- Add autoloader dependencies
- Modify autoloader

* Mon Jul 06 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.0.1-1
- Initial package

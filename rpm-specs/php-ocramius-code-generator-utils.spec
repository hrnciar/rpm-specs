#
# Fedora spec file for php-ocramius-code-generator-utils
#
# Copyright (c) 2014-2016 Shawn Iwinski <shawn.iwinski@gmail.com>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     Ocramius
%global github_name      CodeGenerationUtils
%global github_version   0.4.1
%global github_commit    862c03de42475fe039e7d0f47966c25ac40a58a8

%global composer_vendor  ocramius
%global composer_project code-generator-utils

# "php": "~7.0"
%global php_min_ver 7.0
# "nikic/php-parser": "~2.0|~3.0"
%global php_parser_min_ver 2.0
%global php_parser_max_ver 4

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       8%{?github_release}%{?dist}
Summary:       A set of code generator utilities built on top of PHP-Parsers

License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}
Source0:       %{url}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
%if %{with_tests}
# composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: php-composer(nikic/php-parser) <  %{php_parser_max_ver}
BuildRequires: php-composer(nikic/php-parser) >= %{php_parser_min_ver}
BuildRequires: php-composer(phpunit/phpunit)  >= 5.0
# phpcompatinfo (computed from version 0.4.0)
BuildRequires: php-pcre
BuildRequires: php-reflection
BuildRequires: php-spl
# Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
Requires:      php-composer(nikic/php-parser) <  %{php_parser_max_ver}
Requires:      php-composer(nikic/php-parser) >= %{php_parser_min_ver}
# phpcompatinfo (computed from version 0.4.0)
Requires:      php-pcre
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
A set of code generator utilities built on top of PHP-Parsers that ease its use
when combined with Reflection.

Autoloader: %{phpdir}/CodeGenerationUtils/autoload.php


%prep
%setup -qn %{github_name}-%{github_commit}


%build
: Create autoloader
cat <<'AUTOLOAD' | tee src/CodeGenerationUtils/autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 *
 * @return \Symfony\Component\ClassLoader\ClassLoader
 */

require_once '/usr/share/php/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('CodeGenerationUtils\\', __DIR__);
\Fedora\Autoloader\Dependencies::required([
    [
        '%{phpdir}/PhpParser3/autoload.php',
        '%{phpdir}/PhpParser2/autoload.php',
    ],
]);
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}
cp -rp src/CodeGenerationUtils %{buildroot}%{phpdir}/


%check
%if %{with_tests}
: Create tests bootstrap
cat <<'BOOTSTRAP' | tee bootstrap.php
<?php
require '%{buildroot}%{phpdir}/CodeGenerationUtils/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('CodeGenerationUtilsTest\\', __DIR__.'/tests/CodeGenerationUtilsTests');
\Fedora\Autoloader\Autoload::addPsr4('CodeGenerationUtilsTestAsset\\', __DIR__.'/tests/CodeGenerationUtilsTestAsset');
BOOTSTRAP

ret=0
for cmd in php php70 php71 php72; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit --verbose --bootstrap bootstrap.php || ret=1
  fi
done
exit $ret
%else
: Tests skipped
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc *.md
%doc composer.json
%{phpdir}/CodeGenerationUtils


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 23 2017 Remi Collet <remi@remirepo.net> - 0.4.1-1
- Update to 0.4.1
- allow nikic/php-parser version 2 and 3

* Wed Feb 22 2017 Remi Collet <remi@fedoraproject.org> - 0.4.0-3
- switch to fedora-autoloader

* Wed Feb 22 2017 Remi Collet <remi@fedoraproject.org> - 0.4.0-2
- implicitly requires php-nikic-php-parser (v2)
- fix FTBFS #1424073

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Nov 30 2016 Remi Collet <remi@fedoraproject.org> - 0.4.0-1
- update to 0.4.0
- raise dependency on php ~7.0
- raise dependency on nikic/php-parser ~2.0

* Wed Oct 12 2016 Remi Collet <remi@fedoraproject.org> - 0.3.2-4
- add missing dependency for autoloader

* Tue Oct 11 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.3.2-3
- Add autoloader

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Aug  9 2015 Remi Collet <remi@fedoraproject.org> - 0.3.2-1
- update to 0.3.2
- raise dependency on nikic/php-parser ~1.3

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 22 2015 Remi Collet <remi@fedoraproject.org> - 0.3.1-2
- fix test suite autoloader (FTBFS detected by Koschei)

* Wed Feb 25 2015 Remi Collet <remi@fedoraproject.org> - 0.3.1-1
- update to 0.3.1 (no change)
- raise nikic/php-parser max version

* Wed Nov 05 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.3.0-2
- Silenced include in autoloader
- Removed debug from %%check

* Mon Oct 27 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.3.0-1
- Initial package

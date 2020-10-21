#
# Fedora spec file for php-patchwork-utf8
#
# Copyright (c) 2015-2017 Shawn Iwinski <shawn.iwinski@gmail.com>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     tchwork
%global github_name      utf8
%global github_version   1.3.1
%global github_commit    30ec6451aec7d2536f0af8fe535f70c764f2c47a

%global composer_vendor  patchwork
%global composer_project utf8

# "php": ">=5.3.0"
%global php_min_ver 5.3.0

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       12%{?github_release}%{?dist}
Summary:       Portable and performant UTF-8, Unicode and Grapheme Clusters for PHP

License:       ASL 2.0 or GPLv2
URL:           https://github.com/%{github_owner}/%{github_name}

# GitHub export does not include tests.
# Run php-patchwork-utf8-get-source.sh to create full source.
Source0:       %{name}-%{github_version}-%{github_commit}.tar.gz
Source1:       %{name}-get-source.sh

# Fix tests for PHP 7.1 negative string offsets
# https://github.com/tchwork/utf8/pull/64
Patch0:        %{name}-pull-request-64.patch

BuildArch:     noarch
# Tests
%if %{with_tests}
BuildRequires: php-composer(phpunit/phpunit)
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: php-iconv
BuildRequires: php-intl
BuildRequires: php-mbstring
BuildRequires: php-pcre
## phpcompatinfo (computed from version 1.3.1)
BuildRequires: php-date
BuildRequires: php-exif
BuildRequires: php-filter
BuildRequires: php-json
BuildRequires: php-reflection
BuildRequires: php-spl
BuildRequires: php-xml
%endif
## Autoloader
BuildRequires: php-fedora-autoloader-devel

# composer.json
Requires:      php(language) >= %{php_min_ver}
Requires:      php-pcre
# composer.json: optional
Requires:      php-iconv
Requires:      php-intl
Requires:      php-mbstring
# phpcompatinfo (computed from version 1.3.1)
#Requires:      php-exif
Requires:      php-filter
Requires:      php-json
Requires:      php-spl
Requires:      php-xml
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
%{summary}.

Autoloder: %{phpdir}/Patchwork/autoload-utf8.php


%prep
%setup -qn %{github_name}-%{github_commit}

: Fix tests for PHP 7.1 negative string offsets
: https://github.com/tchwork/utf8/pull/64
%patch0 -p1

: Remove Windows files
rm -f \
    src/Patchwork/Utf8/WindowsStreamWrapper.php \
    tests/Patchwork/Tests/Utf8/WindowsStreamWrapperTest.php


%build
: Create autoloader
%{_bindir}/phpab --template fedora --output src/Patchwork/autoload-utf8.php src/
cat <<'AUTOLOAD' | tee -a src/Patchwork/autoload-utf8.php

\Patchwork\Utf8\Bootup::initAll();
AUTOLOAD

: Compat autoloader
ln -s autoload-utf8.php src/Patchwork/autoload.php


%install
: Library
mkdir -p %{buildroot}%{phpdir}
cp -rp src/Patchwork %{buildroot}%{phpdir}/

: Data
mkdir -p %{buildroot}%{_datadir}/%{name}
mv %{buildroot}%{phpdir}/Patchwork/Utf8/data %{buildroot}%{_datadir}/%{name}/
ln -s \
    $(realpath --relative-to='%{buildroot}%{phpdir}/Patchwork/Utf8' '%{buildroot}%{_datadir}/%{name}/data') \
    %{buildroot}%{phpdir}/Patchwork/Utf8/data
mv %{buildroot}%{phpdir}/Patchwork/PHP/Shim/charset %{buildroot}%{_datadir}/%{name}/shim-charset
ln -s \
    $(realpath --relative-to='%{buildroot}%{phpdir}/Patchwork/PHP/Shim' '%{buildroot}%{_datadir}/%{name}/shim-charset') \
    %{buildroot}%{phpdir}/Patchwork/PHP/Shim/charset
mv %{buildroot}%{phpdir}/Patchwork/PHP/Shim/unidata %{buildroot}%{_datadir}/%{name}/shim-unidata
ln -s \
    $(realpath --relative-to='%{buildroot}%{phpdir}/Patchwork/PHP/Shim' '%{buildroot}%{_datadir}/%{name}/shim-unidata') \
    %{buildroot}%{phpdir}/Patchwork/PHP/Shim/unidata

%check
%if %{with_tests}
%if 0%{?fedora} >= 30
: Skip tests known to fail
sed \
    -e 's/function testConstants/function SKIP_testConstants/' \
    -e 's/function testIsNormalized/function SKIP_testIsNormalized/' \
    -e 's/function testNormalize/function SKIP_testNormalize/' \
    -i tests/PHP/Shim/NormalizerTest.php
sed 's/function testFilterRequestInputs/function SKIP_testFilterRequestInputs/' \
    -i tests/Utf8/BootupTest.php
sed \
    -e 's/function testStrCase/function SKIP_testStrCase/' \
    -e 's/function testJson_decode/function SKIP_testJson_decode/' \
    -e 's/function testFilter/function SKIP_testFilter/' \
    -i tests/Utf8Test.php
%endif

%{_bindir}/phpunit --verbose \
    --bootstrap %{buildroot}%{phpdir}/Patchwork/autoload-utf8.php
%else
: Tests skipped
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE*
%doc *.md
%doc composer.json
%{phpdir}/Patchwork
%exclude %{phpdir}/Patchwork/Utf8/Compiler.php
%exclude %{phpdir}/Patchwork/Utf8/unicode-data.tbz2
%{_datadir}/%{name}


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 29 2019 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.3.1-9
- Fix install symlink
- Skip tests known to fail on Fedora >= 30

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 19 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.3.1-6
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 25 2017 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.3.1-3
- Fix FTBFS in rawhide (RHBZ #1424074)
- Use php-composer(fedora/autoloader)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jul 23 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.3.1-1
- Updated to 1.3.1 (RHBZ #1332183)

* Tue May 03 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.2.6-1
- Updated to 1.2.6
- Added patch "fix for php 5.5.35/5.6.21/7.0.6"

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Oct 15 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.2.5-1
- Updated to 1.2.5 (RHBZ #1271631)
- Exclude Patchwork/Utf8/Compiler.php

* Tue Sep 22 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.2.3-3
- Update patch for license files

* Sat Sep 19 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.2.3-2
- Add patch for license files

* Fri Sep 11 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.2.3-1
- Initial package

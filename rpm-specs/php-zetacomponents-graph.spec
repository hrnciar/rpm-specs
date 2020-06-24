# remirepo/fedora spec file for php-zetacomponents-graph
#
# Copyright (c) 2015-2016 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%global gh_commit    7efda09f967b92fe38a1fbf0c2090fc4fedb0c73
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     zetacomponents
%global gh_project   Graph
%global cname        graph
%global ezcdir       %{_datadir}/php/ezc
%global with_tests   %{?_without_tests:0}%{!?_without_tests:1}

Name:           php-%{gh_owner}-%{cname}
Version:        1.5.2
Release:        13%{?dist}
Summary:        Zeta Graph Component

License:        ASL 2.0
URL:            http://zetacomponents.org/
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{gh_project}-%{version}-%{gh_short}.tar.gz

# https://github.com/zetacomponents/Graph/pull/16
Patch0:         %{name}-pr16.patch
# Upstream
Patch1:         %{name}-upstream.patch

BuildArch:      noarch
BuildRequires:  %{_bindir}/phpab
%if %{with_tests}
BuildRequires:  %{_bindir}/phpunit
BuildRequires:  php-gd
BuildRequires:  php-composer(%{gh_owner}/base) >= 1.8
BuildRequires:  php-composer(%{gh_owner}/unit-test)
%if 0%{?fedora} > 24
# Used for the test suite
BuildRequires:  glibc-langpack-en
BuildRequires:  glibc-langpack-de
%endif
%endif

# From composer.json, "require": {
#            "zetacomponents/base": "~1.8"
Requires:       php-composer(%{gh_owner}/base) >= 1.8
Requires:       php-composer(%{gh_owner}/base) <  2
# From composer.json, "suggest": {
#            "ext-gd": "Used by the GD driver, one of the choices for generating bitmap images."
Requires:       php-gd
# From phpcompatinfo report for 1.5.2
Requires:       php(language) > 5.3
Requires:       php-date
Requires:       php-dom
Requires:       php-gd
Requires:       php-pcre
Requires:       php-simplexml
Requires:       php-spl
Requires:       php-xml

Provides:       php-composer(%{gh_owner}/%{cname}) = %{version}


%description
A component for creating pie charts, line graphs and other kinds of diagrams.

Documentation is available in the %{name}-doc package.


%package doc
Summary:  Documentation for %{name}
# For License
Requires: %{name} = %{version}-%{release}

%description doc
%{summary}.


%prep
%setup -q -n %{gh_project}-%{gh_commit}

%patch0 -p1
%patch1 -p1

: Drop bundled fonts
rm docs/tutorial/tutorial_font.*
sed -e 's:tutorial_font.ttf:/usr/share/fonts/gnu-free/FreeSans.ttf:' \
    -i docs/tutorial/*php


%build
: Generate a simple autoloader
%{_bindir}/phpab \
   --output src/autoloader.php \
   src
cat <<EOF | tee -a  src/autoloader.php
# Dependencies
require_once '%{ezcdir}/Base/autoloader.php';
EOF


%install
mkdir -p %{buildroot}%{ezcdir}/autoload

: The library
cp -pr src \
       %{buildroot}%{ezcdir}/%{gh_project}
: For ezcBase autoloader
cp -pr src/*_autoload.php \
       %{buildroot}%{ezcdir}/autoload


%check
%if %{with_tests}
: Create test autoloader
mkdir vendor
cat <<EOF | tee vendor/autoload.php
<?php
require '%{ezcdir}/UnitTest/autoloader.php';
require '%{buildroot}%{ezcdir}/%{gh_project}/autoloader.php';
class_alias('PHPUnit_Framework_Constraint', 'PHPUnit\\Framework\\Constraint');
EOF

: Ignore test with erratic result
sed -e 's/testBarChartWithSingleDataPointNumericAxis/SKIP_testBarChartWithSingleDataPointNumericAxis/' \
    -i tests/chart_test.php

: Run test test suite
%{_bindir}/phpunit
%else
: Test suite disabled
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE* CREDITS
%doc ChangeLog
%doc composer.json
%{ezcdir}/autoload/*
%{ezcdir}/%{gh_project}

%files doc
%doc docs design


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Sep 11 2019 Remi Collet <remi@remimrepo.net> - 1.5.2-12
- fix FTBFS #1736437

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Feb 29 2016 Remi Collet <remi@fedoraproject.org> - 1.5.2-5
- add BR glibc-langpack-en, glibc-langpack-de for test suite
  FTBFS detected by Koschei
- ignore 1 test with erratic result

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jul 13 2015 Remi Collet <remi@fedoraproject.org> - 1.5.2-3
- create subpackage for documentation
- minor improvments, from review #1228090 comments

* Thu Jun  4 2015 Remi Collet <remi@fedoraproject.org> - 1.5.2-2
- add upstream patch for LICENSE file

* Wed Jun  3 2015 Remi Collet <remi@fedoraproject.org> - 1.5.2-1
- initial package
- open https://github.com/zetacomponents/Graph/pull/16

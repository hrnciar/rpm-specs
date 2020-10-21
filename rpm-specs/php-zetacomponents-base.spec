# remirepo/fedora spec file for php-zetacomponents-base
#
# Copyright (c) 2015-2017 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%global gh_commit    489e20235989ddc97fdd793af31ac803972454f1
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     zetacomponents
%global gh_project   Base
%global cname        base
%global ezcdir       %{_datadir}/php/ezc
%global with_tests   %{?_without_tests:0}%{!?_without_tests:1}

Name:           php-%{gh_owner}-%{cname}
Version:        1.9.1
Release:        7%{?dist}
Summary:        Zeta Base Component

License:        ASL 2.0
URL:            http://zetacomponents.org/
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{gh_project}-%{version}-%{gh_short}.tar.gz

# Use old PEAR layout
Patch0:         %{name}-layout.patch

BuildArch:      noarch
BuildRequires:  %{_bindir}/phpab
%if %{with_tests}
BuildRequires:  %{_bindir}/phpunit
BuildRequires:  %{_bindir}/convert
BuildRequires:  php-composer(%{gh_owner}/unit-test)
BuildRequires:  php-posix
%endif

# From phpcompatinfo report for 1.9
Requires:       php(language) > 5.3
Requires:       php-pcre
Requires:       php-posix
Requires:       php-simplexml
Requires:       php-spl

Provides:       php-composer(%{gh_owner}/%{cname}) = %{version}


%description
This is the base package of the Zeta components, offering the basic
support that all Components need. In the first version this will be the
autoload support.


%prep
%setup -q -n %{gh_project}-%{gh_commit}

%patch0 -p0


%build
: Generate a simple autoloader
%{_bindir}/phpab \
   --output src/autoloader.php \
   src


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
: Ignore test relying on composer layout
rm tests/file_find_recursive_test.php

: Create test autoloader
mkdir vendor
cat <<EOF | tee vendor/autoload.php
<?php
require '%{ezcdir}/UnitTest/autoloader.php';
require '$PWD/src/autoloader.php';
EOF

: Run test test suite
ret=0
for cmd in php php56 php70 php71 php72; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit || ret=1
  fi
done
exit $ret
%else
: Test suite disabled
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE* CREDITS
%doc ChangeLog
%doc composer.json
%doc docs design
%dir %{ezcdir}
%dir %{ezcdir}/autoload
     %{ezcdir}/autoload/*_autoload.php
     %{ezcdir}/%{gh_project}


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov 29 2017 Remi Collet <remi@remirepo.net> - 1.9.1-1
- Update to 1.9.1

* Mon Oct 30 2017 Remi Collet <remi@fedoraproject.org> - 1.9-6
- fix FTBFS from Koschei, add patch for tests from
  https://github.com/zetacomponents/Base/pull/8

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun  4 2015 Remi Collet <remi@fedoraproject.org> - 1.9-2
- add upstream patch for LICENSE file

* Wed Jun  3 2015 Remi Collet <remi@fedoraproject.org> - 1.9-1
- initial package
- open https://github.com/zetacomponents/UnitTest/issues/4 License
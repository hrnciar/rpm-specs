# spec file for php-mikey179-vfsstream
#
# Copyright (c) 2014-2019 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global gh_commit    231c73783ebb7dd9ec77916c10037eff5a2b6efe
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     bovigo
%global gh_project   vfsStream
%global pk_owner     mikey179
%global pk_project   vfsstream
%global with_tests   %{?_without_tests:0}%{!?_without_tests:1}

Name:           php-%{pk_owner}-%{pk_project}
Version:        1.6.8
Release:        3%{?dist}
Summary:        PHP stream wrapper for a virtual file system

License:        BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{name}-%{version}-%{gh_short}.tar.gz

BuildArch:      noarch
BuildRequires:  php(language) >= 5.3
BuildRequires:  %{_bindir}/phpab
%if %{with_tests}
# From composer.json, "require-dev": {
#        "phpunit/phpunit": "~4.5|^5.0"
BuildRequires:  php-composer(phpunit/phpunit) >= 4.5
%endif

# From composer.json, "require": {
#        "php": ">=5.3.0"
Requires:       php(language) >= 5.3
# From phpcompatifo report for 1.6.0
Requires:       php-date
Requires:       php-dom
Requires:       php-pcre
Requires:       php-posix
Requires:       php-spl
Requires:       php-xml
Requires:       php-zip

# provides both cases for compatibility
Provides:       php-composer(%{pk_owner}/%{pk_project}) = %{version}
Provides:       php-composer(%{pk_owner}/%{gh_project}) = %{version}


%description
vfsStream is a PHP stream wrapper for a virtual file system that may be
helpful in unit tests to mock the real file system.

It can be used with any unit test framework, like PHPUnit or SimpleTest.

To use this library, you just have to add, in your project:
  require_once '%{_datadir}/php/org/bovigo/vfs/autoload.php';


%prep
%setup -q -n %{gh_project}-%{gh_commit}


%build
: Generate autoloader
%{_bindir}/phpab \
    --output src/main/php/org/bovigo/vfs/autoload.php \
             src/main/php/org/bovigo/vfs


%install
mkdir -p                %{buildroot}%{_datadir}/php
cp -pr src/main/php/org %{buildroot}%{_datadir}/php/org


%if %{with_tests}
%check
# erratic result in mock
rm src/test/php/org/bovigo/vfs/vfsStreamWrapperLargeFileTestCase.php

mkdir vendor
ln -s %{buildroot}%{_datadir}/php/org/bovigo/vfs/autoload.php vendor/autoload.php

ret=0
for cmd in php php71 php72 php73 php74; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit \
      --verbose || ret=1
  fi
done
exit $ret
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc *.md
%doc composer.json

%dir %{_datadir}/php/org
%dir %{_datadir}/php/org/bovigo
     %{_datadir}/php/org/bovigo/vfs


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 31 2019 Remi Collet <remi@remirepo.net> - 1.6.8-1
- update to 1.6.8

* Fri Aug  2 2019 Remi Collet <remi@remirepo.net> - 1.6.7-1
- update to 1.6.7

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr  9 2019 Remi Collet <remi@remirepo.net> - 1.6.6-2
- fix vendor

* Tue Apr  9 2019 Remi Collet <remi@remirepo.net> - 1.6.6-1
- update to 1.6.6 (no change)
- project ownership have moved to bovigo

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 16 2018 Remi Collet <remi@remirepo.net> - 1.6.5-5
- ignore 1 failed test related to behavior change in 7.3
  open https://github.com/mikey179/vfsStream/pull/172

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar  5 2018 Remi Collet <remi@remirepo.net> - 1.6.5-3
- provides both mikey179/vfsstream and mikey179/vfsStream

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Aug  4 2017 Remi Collet <remi@remirepo.net> - 1.6.5-1
- Update to 1.6.5

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jul 18 2016 Remi Collet <remi@fedoraproject.org> - 1.6.4-1
- update to 1.6.4

* Wed Apr 13 2016 Remi Collet <remi@fedoraproject.org> - 1.6.3-1
- update to 1.6.3

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 13 2016 Remi Collet <remi@fedoraproject.org> - 1.6.2-1
- update to 1.6.2

* Fri Dec  4 2015 Remi Collet <remi@fedoraproject.org> - 1.6.1-1
- update to 1.6.1

* Wed Oct  7 2015 Remi Collet <remi@fedoraproject.org> - 1.6.0-1
- update to 1.6.0
- add generated autoloader

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Mar 29 2015 Remi Collet <remi@fedoraproject.org> - 1.5.0-1
- update to 1.5.0
- create source from git snapshot for test suite
  see https://github.com/mikey179/vfsStream/issues/108

* Sun Sep 14 2014 Remi Collet <remi@fedoraproject.org> - 1.4.0-1
- update to 1.4.0

* Tue Jul 22 2014 Remi Collet <remi@fedoraproject.org> - 1.3.0-1
- update to 1.3.0
- fix license handling

* Fri Jun  6 2014 Remi Collet <remi@fedoraproject.org> - 1.2.0-2
- provides php-composer(mikey179/vfsstream)

* Tue May 13 2014 Remi Collet <remi@fedoraproject.org> - 1.2.0-1
- initial package

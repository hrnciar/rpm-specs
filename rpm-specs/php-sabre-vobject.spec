# remirepo/fedora spec file for php-sabre-vobject
#
# Copyright (c) 2013-2019 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global gh_commit    129d80533a9ec0d9cacfb50b51180c34edb6874c
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sabre-io
%global gh_project   vobject
%global with_tests   %{?_without_tests:0}%{!?_without_tests:1}

%if 0%{?fedora} >= 26 || 0%{?rhel} >= 8
%global with_cmd 0
%else
%global with_cmd 1
%endif

Name:           php-sabre-vobject
Summary:        Library to parse and manipulate iCalendar and vCard objects
Version:        3.5.3
Release:        14%{?dist}

URL:            http://sabre.io/vobject/
License:        BSD
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{name}-%{version}-%{gh_short}.tar.gz
Source1:        %{name}-autoload.php

# replace composer autloader
Patch0:         %{name}-bin.patch
Patch1:         https://patch-diff.githubusercontent.com/raw/sabre-io/vobject/pull/395.patch
# Adapted upstream patch
Patch2:         c533d42e17e058237f0350ca56c7f01903bb035e.patch
Patch3:         https://patch-diff.githubusercontent.com/raw/sabre-io/vobject/pull/469.patch

BuildArch:      noarch
%if %{with_tests}
BuildRequires:  php-composer(phpunit/phpunit)
BuildRequires:  php(language) >= 5.3.1
BuildRequires:  php-mbstring
BuildRequires:  php-date
BuildRequires:  php-json
BuildRequires:  php-pcre
BuildRequires:  php-spl
BuildRequires:  php-xml
# Autoloader
BuildRequires:  php-composer(fedora/autoloader)
%endif

# From composer.json
#        "php"          : ">=5.3.1",
#        "ext-mbstring" : "*"
Requires:       php(language) >= 5.3.1
Requires:       php-mbstring
# From phpcompatinfo report for version 3.4.5
%if %{with_cmd}
Requires:       php-cli
%endif
Requires:       php-date
Requires:       php-json
Requires:       php-pcre
Requires:       php-spl
Requires:       php-xml
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(sabre/vobject) = %{version}


%description
The VObject library allows you to easily parse and manipulate iCalendar
and vCard objects using PHP. The goal of the VObject library is to create
a very complete library, with an easy to use API.

This project is a spin-off from SabreDAV, where it has been used for several
years. The VObject library has 100% unittest coverage.

Autoloader: %{_datadir}/php/Sabre/VObject/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}

%patch0 -p1 -b .rpm
%patch1 -p1
%patch2 -p1
%patch3 -p1 -b .pr469

cp %{SOURCE1} lib/autoload.php


%build
# nothing to build


%install
# Install as a PSR-0 library
mkdir -p %{buildroot}%{_datadir}/php/Sabre
cp -pr lib %{buildroot}%{_datadir}/php/Sabre/VObject

%if %{with_cmd}
# Install the commands
install -Dpm 0755 bin/vobject \
         %{buildroot}/%{_bindir}/vobject
install -Dpm 0755 bin/generate_vcards \
         %{buildroot}/%{_bindir}/generate_vcards
%endif


%check
%if %{with_tests}
: Fix bootstrap
cd tests
sed -e 's:@BUILDROOT@:%{buildroot}:' -i bootstrap.php

: Run upstream test suite against installed library
ret=0
for cmd in php php56 php70 php71 php72 php73 php74; do
  if which $cmd; then
   $cmd %{_bindir}/phpunit --verbose || ret=1
  fi
done
exit $ret
%else
: Skip upstream test suite
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc *md
%doc composer.json
%{_datadir}/php/Sabre
%if %{with_cmd}
%{_bindir}/vobject
%{_bindir}/generate_vcards
%endif


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Oct  9 2019 Remi Collet <remi@remirepo.net> - 3.5.3-13
- add patch for PHP 7.4 from
  https://github.com/sabre-io/vobject/pull/469

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 15 2018 Remi Collet <remi@remirepo.net> - 3.5.3-10
- add adpated upstream patch for PHP 7.3

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Oct 30 2017 Remi Collet <remi@remirepo.net> - 3.5.3-7
- fix FTBFS from Koschei, add patch for test from
  https://github.com/sabre-io/vobject/pull/395
- sources from https://github.com/sabre-io/vobject/pull/395

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 17 2017 Remi Collet <remi@fedoraproject.org> - 3.5.3-4
- commands moved to php-sabre-vobject4 in F26

* Sat Oct 29 2016 Remi Collet <remi@fedoraproject.org> - 3.5.3-3
- switch from symfony/class-loader to fedora/autoloader

* Fri Oct  7 2016 Remi Collet <remi@fedoraproject.org> - 3.5.3-1
- update to 3.5.3

* Tue Apr 26 2016 Remi Collet <remi@fedoraproject.org> - 3.5.2-1
- update to 3.5.2

* Thu Apr  7 2016 Remi Collet <remi@fedoraproject.org> - 3.5.1-1
- update to 3.5.1

* Fri Mar 11 2016 Remi Collet <remi@fedoraproject.org> - 3.5.0-1
- update to 3.5.0

* Wed Feb 24 2016 Remi Collet <remi@fedoraproject.org> - 3.4.6-1
- update to 3.4.6

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Remi Collet <remi@fedoraproject.org> - 3.2.4-2
- skip failed test

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jul 16 2014 Remi Collet <remi@fedoraproject.org> - 3.2.4-1
- update to 3.2.4

* Wed Jun 18 2014 Remi Collet <remi@fedoraproject.org> - 3.2.3-1
- update to 3.2.3
- add provides php-composer(sabre/vobject)
- url is now http://sabre.io/vobject/

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May  9 2014 Remi Collet <remi@fedoraproject.org> - 3.2.2-1
- update to 3.2.2

* Tue May  6 2014 Remi Collet <remi@fedoraproject.org> - 3.2.1-1
- update to 3.2.1

* Sun Apr  6 2014 Remi Collet <remi@fedoraproject.org> - 3.2.0-1
- update to 3.2.0

* Thu Feb 20 2014 Remi Collet <remi@fedoraproject.org> - 3.1.3-1
- update to 3.1.3

* Tue Dec 31 2013 Remi Collet <remi@fedoraproject.org> - 2.1.3-1
- Initial packaging

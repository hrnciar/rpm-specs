# remirepo/fedora spec file for php-sabre-vobject4
#
# Copyright (c) 2013-2019 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%bcond_without       tests

# For compatibility with SCL
%undefine __brp_mangle_shebangs

%global gh_commit    e17daaf92a12d39e93ab404929673573e3bb85bf
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sabre-io
%global gh_project   vobject

%if 0%{?fedora} >= 26 || 0%{?rhel} >= 8
%global with_cmd 1
%else
%global with_cmd 0
%endif

Name:           php-sabre-vobject4
Summary:        Library to parse and manipulate iCalendar and vCard objects
Version:        4.3.2
Release:        1%{?dist}

URL:            http://sabre.io/vobject/
License:        BSD
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{name}-%{version}-%{gh_short}.tar.gz
Source1:        %{name}-autoload.php

# replace composer autloader
Patch0:         %{name}-bin.patch

BuildArch:      noarch
%if %{with tests}
BuildRequires:  php(language) >= 7.1
BuildRequires:  php-mbstring
BuildRequires:  (php-composer(sabre/xml)    >= 2.1  with php-composer(sabre/xml)     < 3)
BuildRequires:  php-date
BuildRequires:  php-json
BuildRequires:  php-pcre
BuildRequires:  php-spl
BuildRequires:  php-xml
# From composer.json, "require-dev"
#        "friendsofphp/php-cs-fixer": "~2.16.1",
#        "phpunit/phpunit" : "^7.5 || ^8.5 || ^9.0",
#        "phpstan/phpstan": "^0.12"
BuildRequires:  phpunit8 >= 8.5
# Autoloader
BuildRequires:  php-composer(fedora/autoloader)
%endif

# From composer.json, "require"
#        "php"          : "^7.1 || ^8.0",
#        "ext-mbstring" : "*",
#        "sabre/xml"    : "^2.1"
Requires:       php(language) >= 7.1
Requires:       php-mbstring
#
Requires:       (php-composer(sabre/xml)    >= 2.1  with php-composer(sabre/xml)     < 3)
# From phpcompatinfo report for version 4.1.2
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

Autoloader: %{_datadir}/php/Sabre/VObject4/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}

%patch0 -p1 -b .rpm

cp %{SOURCE1} lib/autoload.php


%build
# nothing to build


%install
# Install as a PSR-0 library
mkdir -p %{buildroot}%{_datadir}/php/Sabre
cp -pr lib %{buildroot}%{_datadir}/php/Sabre/VObject4

%if %{with_cmd}
# Install the commands
install -Dpm 0755 bin/vobject \
         %{buildroot}/%{_bindir}/vobject
install -Dpm 0755 bin/generate_vcards \
         %{buildroot}/%{_bindir}/generate_vcards
%endif


%check
%if %{with tests}
: Fix bootstrap
cd tests
sed -e 's:@BUILDROOT@:%{buildroot}:' -i bootstrap.php

opt="--verbose"
if [ $(php -r 'echo PHP_INT_SIZE;') -lt 8 ]; then
  opt="--filter '^((?!(testNeverEnding)).)*$' $opt"
fi

: Run upstream test suite against installed library
ret=0
for cmd in php php72 php73 php74 php80; do
  if which $cmd; then
   $cmd %{_bindir}/phpunit8 $opt || ret=1
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
%{_datadir}/php/Sabre/VObject4
%if %{with_cmd}
%{_bindir}/vobject
%{_bindir}/generate_vcards
%endif

%changelog
* Mon Oct  5 2020 Remi Collet <remi@remirepo.net> - 4.3.2-1
- update to 4.3.2

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 13 2020 Remi Collet <remi@remirepo.net> - 4.3.1-1
- update to 4.3.1

* Sat Feb  1 2020 Remi Collet <remi@remirepo.net> - 4.3.0-1
- update to 4.3.0
- raise dependency on PHP 7.1
- raise dependency on sabre/xml 2.1
- switch to phpunit8

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 14 2020 Remi Collet <remi@remirepo.net> - 4.2.2-1
- update to 4.2.2

* Thu Dec 19 2019 Remi Collet <remi@remirepo.net> - 4.2.1-1
- update to 4.2.1
- drop patch merged upstream
- skip 1 test failing on 32-bit
  https://github.com/sabre-io/vobject/issues/481

* Wed Oct  9 2019 Remi Collet <remi@remirepo.net> - 4.2.0-4
- add patch for PHP 7.4 from
  https://github.com/sabre-io/vobject/pull/469

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul  1 2019 Remi Collet <remi@remirepo.net> - 4.2.0-2
- fix autoloader for sabre/xml version 2

* Wed Feb 20 2019 Remi Collet <remi@remirepo.net> - 4.2.0-1
- update to 4.2.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 15 2018 Remi Collet <remi@remirepo.net> - 4.1.6-3
- add upstream patch for PHP 7.3

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Apr 20 2018 Remi Collet <remi@remirepo.net> - 4.1.6-1
- update to 4.1.6
- undefine __brp_mangle_shebangs

* Fri Mar  9 2018 Remi Collet <remi@remirepo.net> - 4.1.5-1
- update to 4.1.5
- use range dependencies on F27+

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Dec 23 2017 Remi Collet <remi@remirepo.net> - 4.1.4-1
- Update to 4.1.4

* Mon Oct 30 2017 Remi Collet <remi@remirepo.net> - 4.1.3-2
- fix FTBFS fro mKoschei, add patch for test from
  https://github.com/sabre-io/vobject/pull/395

* Thu Oct 19 2017 Remi Collet <remi@remirepo.net> - 4.1.3-1
- Update to 4.1.3
- sources from https://github.com/sabre-io/vobject

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jan 17 2017 Remi Collet <remi@fedoraproject.org> - 4.1.2-1
- rename to php-sabre-vobject4
- raise dependency on PHP version 5.5
- add dependency on sabre/xml

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

* Wed Jul 16 2014 Remi Collet <remi@fedoraproject.org> - 3.2.4-1
- update to 3.2.4

* Wed Jun 18 2014 Remi Collet <remi@fedoraproject.org> - 3.2.3-1
- update to 3.2.3
- add provides php-composer(sabre/vobject)
- url is now http://sabre.io/vobject/

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

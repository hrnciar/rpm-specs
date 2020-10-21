# php-deepdiver-zipstreamer spec file
# forked from remirepo/fedora/php-mcnetic-zipstreamer
#
# Copyright (c) 2018 Remi Collet, Christian Glombek
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%global gh_commit    c8e73ca3204bd0e06abdb0bc533f073b616d6e47
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     DeepDiver1975
%global gh_project   PHPZipStreamer
%global with_tests   1
%global namespace    ZipStreamer

Name:           php-deepdiver-zipstreamer
Version:        1.1.1
Release:        7%{?dist}
Summary:        Stream zip files without i/o overhead

License:        GPLv3+
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{gh_project}-%{version}-%{gh_short}.tar.gz

BuildArch:      noarch
BuildRequires:  php-composer(theseer/autoload)
%if %{with_tests}
BuildRequires:  php(language) >= 5.6.0
BuildRequires:  php-date
BuildRequires:  php-hash
BuildRequires:  php-mbstring
BuildRequires:  php-pcre
BuildRequires:  php-spl
BuildRequires:  php-composer(phpunit/phpunit)
BuildRequires:  php-pecl(Xdebug)
BuildRequires:  php-pecl(pecl_http)
%endif

# From composer.json
#      "php": ">=5.6.0"
Requires:       php(language) >= 5.6.0
# From phpcompatinfo report for version0.7
Requires:       php-date
Requires:       php-hash
Requires:       php-mbstring
Requires:       php-spl
%if 0%{?fedora} > 21
# For compression
Recommends:     php-pecl(pecl_http)
%else
Requires:       php-pecl(pecl_http)
%endif

Obsoletes:      php-mcnetic-zipstreamer < 1:1.0-4
Provides:       php-composer(mcnetic/zipstreamer) = %{version}
Provides:       php-composer(deepdiver/zipstreamer) = %{version}

%description
Simple Class to create zip files on the fly and stream directly to the
HTTP client as the content is added (without using temporary files).

Autoloader: %{_datadir}/php/%{namespace}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}


%build
%{_bindir}/phpab -o src/autoload.php src


%install
mkdir -p   %{buildroot}%{_datadir}/php
cp -pr src %{buildroot}%{_datadir}/php/%{namespace}


%check
%if %{with_tests}
: Ensure we use our autoloader
sed -e '/^ZipStreamer.php/d' -i test/*php

if [ $(php -r "echo PHP_INT_SIZE;") -eq 8 ]; then
  : Run test suite
  %{_bindir}/phpunit \
    --bootstrap %{buildroot}%{_datadir}/php/%{namespace}/autoload.php test/lib
else
  : Ignore test suite as Count64 do not support 32 bits overflow
fi
%else
: Test suite disabled
%endif


%files
%{!?_licensedir:%global license %%doc}
%license COPYING
%doc *.md
%doc composer.json
%{_datadir}/php/%{namespace}


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 24 2018 Christian Glombek <lorbus@fedoraproject.org> - 1.1.1-2
- Remove epoch from virtual provides for mcnetic/zipstreamer

* Sun Apr 22 2018 Christian Glombek <lorbus@fedoraproject.org> - 1.1.1-1
- Update to version 1.1.1

* Fri Feb 9 2018 Christian Glombek <lorbus@fedoraproject.org> - 1.1.0-1
- Update to version 1.1.0
- Switch to DeepDiver1975's maintained fork

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Apr  2 2016 Remi Collet <remi@fedoraproject.org> - 1:1.0.1
- update to 1.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 20 2016 Remi Collet <remi@fedoraproject.org> - 1:0.7.1
- fix version, from review #1296901

* Fri Jan  8 2016 Remi Collet <remi@fedoraproject.org> - 1.7.2
- ensure we use our autoloader during the test suite
- ignore test suite on 32bits build

* Fri Jan  8 2016 Remi Collet <remi@fedoraproject.org> - 1.7.1
- initial package
- add patch to workaround error raised by pecl_http
  see https://github.com/McNetic/PHPZipStreamer/issues/29

# remirepo/fedora spec file for php-owncloud-tarstreamer
#
# Copyright (c) 2016-2020 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global gh_commit    ad48505d1ab54a8e94e6b1cc5297bbed72e956de
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     owncloud
%global gh_project   TarStreamer
%global with_tests   0%{!?_without_tests:1}
%global ns_vendor    ownCloud
%global ns_project   TarStreamer

Name:           php-owncloud-tarstreamer
Version:        2.0.0
Release:        3%{?dist}
Summary:        Streaming dynamic tar files

License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{gh_project}-%{version}%{?prever}-%{gh_short}.tar.gz

BuildArch:      noarch
BuildRequires:  php-composer(theseer/autoload)
BuildRequires:  php-fedora-autoloader-devel
%if %{with_tests}
BuildRequires:  php(language) >= 7.1
BuildRequires:  php-date
BuildRequires:  php-spl
BuildRequires:  php-composer(phpunit/phpunit)
BuildRequires:  php-pear(Archive_Tar)
BuildRequires:  php-pecl(Xdebug)
%endif

# From composer.json
#      "php": ">=7.1"
Requires:       php(language) >= 7.1
# From phpcompatinfo report for version 2.0.0
Requires:       php-date
Requires:       php-spl

Provides:       php-composer(owncloud/tarstreamer) = %{version}%{?prever}


%description
A library for dynamically streaming dynamic tar files without
the need to have the complete file stored on the server.

Autoloader: %{_datadir}/php/%{ns_vendor}/%{ns_project}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}


%build
: Generate a simple autoloader
%{_bindir}/phpab -t fedora -o src/autoload.php src


%install
: Create a PSR-0 tree
mkdir -p   %{buildroot}%{_datadir}/php/%{ns_vendor}
cp -pr src %{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}


%check
%if %{with_tests}
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require_once '%{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}/autoload.php';
require_once '/usr/share/pear/Archive/Tar.php';
EOF

: Run test suite
ret=0
cd tests
for cmd in php php71 php72 php73 php74; do
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
%license LICENSE
%doc composer.json
%{_datadir}/php/%{ns_vendor}


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 10 2020 Remi Collet <remi@remirepo.net> - 2.0.0-1
- update to 2.0.0 (no change since 0.1.2)
- raise dependency on PHP 7.1

* Fri Jan 10 2020 Remi Collet <remi@remirepo.net> - 0.1.2-1
- update to 0.1.2

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 12 2019 Remi Collet <remi@remirepo.net> - 0.1.1-1
- update to 0.1.1

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May  2 2016 Remi Collet <remi@fedoraproject.org> - 0.1.0-1
- update to 0.1.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.2.beta3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan  8 2016 Remi Collet <remi@fedoraproject.org> - 0.1-0.1.beta3
- initial package

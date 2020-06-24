# remirepo/fedora spec file for php-icewind-streams
#
# Copyright (c) 2015-2020 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
# Github information
%global gh_commit    77d750ccc654c0eda4a41fedb2dbd71053755790
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     icewind1991
%global gh_project   Streams
# Packagist information
%global pk_vendor    icewind
%global pk_name      streams
# Namespace information
%global ns_vendor    Icewind
%global ns_name      Streams

Name:           php-%{pk_vendor}-%{pk_name}
Version:        0.7.2
Release:        1%{?dist}
Summary:        A set of generic stream wrappers

License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{url}/archive/%{gh_commit}/%{name}-%{version}-%{gh_short}.tar.gz

BuildArch:      noarch
# For tests
BuildRequires:  php(language) >= 5.6
# From composer.json, "require-dev": {
#		"satooshi/php-coveralls": "v2.1.0",
#		"phpunit/phpunit": "^5.7"
BuildRequires:  php-composer(phpunit/phpunit) >= 5.7
BuildRequires:  php-composer(theseer/autoload)
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer.json, "require": {
#      "php": ">=5.3"
Requires:       php(language) >= 5.6
# From phpcompatinfo report for version 0.7.2
Requires:       php-hash
Requires:       php-spl
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_vendor}/%{pk_name}) = %{version}


%description
Generic stream wrappers for php.

Autoloader: %{_datadir}/php/%{ns_vendor}/%{ns_name}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}


%build
: Generate classmap autoloader
%{_bindir}/phpab --template fedora --output src/autoload.php src


%install
# Restore PSR-0 tree
mkdir -p   %{buildroot}%{_datadir}/php/%{ns_vendor}
cp -pr src %{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_name}


%check
cd tests
: Generate a simple autoloader for test suite
%{_bindir}/phpab --output bootstrap.php .
echo "require '%{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_name}/autoload.php';" >> bootstrap.php

: Run the test suite
ret=0
for cmd in php php56 php70 php71 php72 php73 php74; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit || ret=1
  fi
done
exit $ret


%files
%{!?_licensedir:%global license %%doc}
%license LICENCE
%doc composer.json
%doc *.md
%dir %{_datadir}/php/%{ns_vendor}
     %{_datadir}/php/%{ns_vendor}/%{ns_name}


%changelog
* Thu Apr  9 2020 Remi Collet <remi@remirepo.net> - 0.7.2-1
- update to 0.7.2
- raise dependency on PHP 5.6
- switch to classmap autoloader

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb 18 2019 Remi Collet <remi@remirepo.net> - 0.7.1-1
- update to 0.7.1

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Apr 25 2018 Remi Collet <remi@remirepo.net> - 0.6.1-1
- update to 0.6.1

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 30 2018 Remi Collet <remi@remirepo.net> - 0.6.0-1
- Update to 0.6.0

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec  5 2016 Remi Collet <remi@fedoraproject.org> - 0.5.2-1
- update to 0.5.2

* Thu Oct 27 2016 Remi Collet <remi@fedoraproject.org> - 0.5.1-1
- update to 0.5.1
- switch from symfony/class-loader to fedora/autoloader

* Fri Jun  3 2016 Remi Collet <remi@fedoraproject.org> - 0.4.1-1
- update to 0.4.1

* Thu Mar 17 2016 Remi Collet <remi@fedoraproject.org> - 0.4.0-1
- update to 0.4.0

* Thu Mar 17 2016 Remi Collet <remi@fedoraproject.org> - 0.3.0-1
- version 0.3.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Sep  1 2015 Remi Collet <remi@fedoraproject.org> - 0.2.0-1
- initial package, version 0.2.0

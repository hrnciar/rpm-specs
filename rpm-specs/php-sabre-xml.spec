# remirepo/fedora spec file for php-sabre-xml
#
# Copyright (c) 2016-2019 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global gh_commit    a367665f1df614c3b8fefc30a54de7cd295e444e
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sabre-io
%global gh_project   xml
%global with_tests   0%{!?_without_tests:1}

Name:           php-sabre-%{gh_project}
Summary:        XML library that you may not hate
Version:        1.5.1
Release:        7%{?dist}

URL:            https://github.com/%{gh_owner}/%{gh_project}
License:        BSD
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{name}-%{version}-%{gh_short}.tar.gz
Source1:        %{name}-autoload.php

BuildArch:      noarch
%if %{with_tests}
BuildRequires:  php(language) >= 5.5.5
BuildRequires:  php-xmlwriter
BuildRequires:  php-xmlreader
BuildRequires:  php-dom
BuildRequires: (php-composer(sabre/uri) >= 1.0   with  php-composer(sabre/uri) <  3)
BuildRequires:  php-pcre
BuildRequires:  php-spl
# From composer.json, "require-dev": {
#        "sabre/cs": "~1.0.0",
#        "phpunit/phpunit" : "~4.8|~5.7"
BuildRequires:  php-composer(phpunit/phpunit)
# Autoloader
BuildRequires:  php-composer(fedora/autoloader)
%endif

# From composer.json, "require" : {
#        "php" : ">=5.5.5",
#        "ext-xmlwriter" : "*",
#        "ext-xmlreader" : "*",array
#        "ext-dom" : "*",
#        "lib-libxml" : ">=2.6.20",
#        "sabre/uri" : ">=1.0,<3.0.0"
Requires:       php(language) >= 5.5.5
Requires:       php-xmlwriter
Requires:       php-xmlreader
Requires:       php-dom
Requires:      (php-composer(sabre/uri) >= 1.0   with  php-composer(sabre/uri) <  3)
# From phpcompatinfo report for version 1.4.0
Requires:       php-pcre
Requires:       php-spl
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(sabre/xml) = %{version}


%description
The sabre/xml library is a specialized XML reader and writer.

Autoloader: %{_datadir}/php/Sabre/Xml/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}

cp %{SOURCE1} lib/autoload.php


%build
# nothing to build


%install
# Install as a PSR-0 library
mkdir -p %{buildroot}%{_datadir}/php/Sabre
cp -pr lib %{buildroot}%{_datadir}/php/Sabre/Xml


%check
%if %{with_tests}
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require_once '%{buildroot}%{_datadir}/php/Sabre/Xml/autoload.php';
// Tests
require_once '%{_datadir}/php/Symfony/Component/ClassLoader/Psr4ClassLoader.php';
\Fedora\Autoloader\Autoload::addPsr4('Sabre\\Xml\\', dirname(__DIR__).'/tests/Sabre/Xml/');
EOF
cd tests

: Run upstream test suite against installed library
ret=0
for cmd in php php70 php71 php72 php73 php74; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit || ret=1
  fi
done
exit $ret
%else
: Skip upstream test suite
%endif


%files
%license LICENSE
%doc *md
%doc composer.json
%{_datadir}/php/Sabre/Xml


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul  5 2019 Remi Collet <remi@remirepo.net> - 1.5.1-5
- fix autoloader for sabre/uri v1 and v2

* Fri Jul  5 2019 Remi Collet <remi@remirepo.net> - 1.5.1-4
- fix autoloader for sabre/uri v1 and v2

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan  9 2019 Remi Collet <remi@remirepo.net> - 1.5.1-1
- update to 1.5.1

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun  5 2018 Remi Collet <remi@remirepo.net> - 1.5.0-6
- fix project URL

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Oct 29 2016 Remi Collet <remi@fedoraproject.org> - 1.5.0-2
- switch from symfony/class-loader to fedora/autoloader

* Mon Oct 10 2016 Remi Collet <remi@fedoraproject.org> - 1.5.0-1
- update to 1.5.0
- raise dependency on PHP 5.5

* Fri May 20 2016 Remi Collet <remi@fedoraproject.org> - 1.4.2-1
- update to 1.4.2

* Tue Mar 29 2016 Remi Collet <remi@fedoraproject.org> - 1.4.1-1
- update to 1.4.1

* Fri Mar 11 2016 Remi Collet <remi@fedoraproject.org> - 1.4.0-1
- Initial packaging


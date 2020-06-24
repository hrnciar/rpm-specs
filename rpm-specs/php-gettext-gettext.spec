%global gh_owner     oscarotero
%global gh_project   Gettext


Name:       php-gettext-gettext
Version:    4.7.0
Release:    3%{?dist}
BuildArch:  noarch

License:    MIT
Summary:    PHP gettext manager
URL:        https://github.com/%{gh_owner}/%{gh_project}
Source0:    %{url}/archive/v%{version}.tar.gz
# Upstream strips the tests from the tarball, so we have to generate it manually.
# dltests.sh is used to do this, and is included in this repository.
Source1:    tests-v%{version}.tar.bz2
Patch0:     230.patch

BuildRequires: dos2unix
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
BuildRequires: (php-composer(gettext/languages) >= 2.3.0 with php-composer(gettext/languages) < 3)
%else
BuildRequires: php-gettext-languages >= 2.3.0
%endif
BuildRequires: phpunit

Requires:   php(language) >= 5.4.0
Requires:   php-date
Requires:   php-dom
Requires:   php-gettext
Requires:   php-json
Requires:   php-pcre
Requires:   php-simplexml
Requires:   php-spl
Requires:   php-tokenizer

%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
Requires:  (php-composer(gettext/languages) >= 2.3.0 with php-composer(gettext/languages) < 3)
%else
Requires:   php-gettext-languages >= 2.3.0
%endif

Provides:   php-composer(gettext/gettext) = %{version}


%description
Gettext is a PHP (5.3) library to import/export/edit gettext from PO,
MO, PHP, JS files, etc.

Autoloader: %{_datadir}/php/Gettext/autoload.php


%prep
%setup -a1 -n Gettext-%{version}
%patch0 -p1

# The documentation has the wrong newline codes
dos2unix *.md


%build
: Create autoloader
cat <<'AUTOLOAD' | tee src/autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 */
require_once '%{_datadir}/php/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('Gettext\\', __DIR__);

\Fedora\Autoloader\Dependencies::required(array(
    '%{_datadir}/php/Gettext/Languages/autoloader.php'
));

AUTOLOAD


%install
install -d -p -m 0755 %{buildroot}/%{_datadir}/php
install -d -p -m 0755 %{buildroot}/%{_datadir}/php/Gettext

cp -ar src/* %{buildroot}/%{_datadir}/php/Gettext/


%check
sed -i "s:include_once.*:\ninclude_once '%{buildroot}/%{_datadir}/php/Gettext/autoload.php';:" tests/bootstrap.php

# gettext has some optional dependencies that we are not integrating with at this time (we can later
# if desired). Thus, we need to skip the tests on these integration points since they will fail
# without the dependencies. There is an upstream issue about compatibility issues with Twig:
# https://github.com/oscarotero/Gettext/issues/137

: run upstream test suite with all installed PHP versions
ret=0
for cmd in php php71 php72 php73 php74; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit --bootstrap tests/bootstrap.php --filter ^\(\(?!\(testBlade\|testTwig\)\).\)*$ tests
  fi
done
exit $ret

%files
%license LICENSE
%doc CHANGELOG.md
%doc composer.json
%doc CONTRIBUTING.md
%doc README.md
%{_datadir}/php/Gettext/*


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 10 2019 Remi Collet <remi@remirepo.net> - 4.7.0-2
- update to 4.7.0
- use range dependencies
- add patch for PHP 7.4 from
- https://github.com/oscarotero/Gettext/pull/230

* Thu Oct 10 2019 Sundeep Anand <suanand@fedoraproject.org> - 4.7.0-1
- Update to 4.7.0 (#1759099).
- https://github.com/oscarotero/Gettext/blob/v4.7.0/CHANGELOG.md

* Wed Sep 11 2019 Sundeep Anand <suanand@fedoraproject.org> - 4.6.3-2
- Fix dependencies.

* Tue Sep 10 2019 Sundeep Anand <suanand@fedoraproject.org> - 4.6.3-1
- Update to 4.6.3 (#1742047).
- https://github.com/oscarotero/Gettext/blob/v4.6.3/CHANGELOG.md

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jul 29 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 4.6.0-1
- Update to 4.6.0 (#1595474).
- https://github.com/oscarotero/Gettext/blob/v4.6.0/CHANGELOG.md

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun May 20 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 4.5.0-1
- Update to 4.5.0 (#1571010).
- https://github.com/oscarotero/Gettext/blob/v4.5.0/CHANGELOG.md

* Sun Feb 25 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 4.4.4-1
- Update to 4.4.4 (#1548216).
- https://github.com/oscarotero/Gettext/blob/v4.4.4/CHANGELOG.md

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Dec 17 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 4.4.3-1
- Update to 4.4.3 (#1450031).
- https://github.com/oscarotero/Gettext/blob/v4.4.3/CHANGELOG.md

* Tue Oct 31 2017 Remi Collet <remi@remirepo.net> - 3.5.9-7
- fix FTBFS from Koschei
- add upstream patch for PHP 7.2
- add patch for bigendian from https://github.com/oscarotero/Gettext/pull/159

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Apr 02 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 3.5.9-5
- Depend on php-dom and php-simplexml.
- Don't provide /usr/share/php/Gettext.

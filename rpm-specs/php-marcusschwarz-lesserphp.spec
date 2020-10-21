%global composer_vendor   marcusschwarz
%global composer_project  lesserphp

%{!?phpdir:  %global phpdir  %{_datadir}/php}
%global pkgdir %{phpdir}/%{composer_vendor}-%{composer_project}

%global with_tests 1

Name:    php-%{composer_vendor}-%{composer_project}
Version: 0.5.4
Release: 6%{?dist}

Summary: A compiler for LESS written in PHP
License: MIT or GPLv3
URL:     https://www.maswaba.de/lesserphpdocs/

%global repo_owner  MarcusSchwarz
%global repo_name   lesserphp
Source0: https://github.com/%{repo_owner}/%{repo_name}/archive/v%{version}/%{repo_name}-%{version}.tar.gz

# A yet-unmerged Pull Request submitted upstream by someone else.
# Fixes uses of deprecated syntax and old PHPUnit code.
#
# https://github.com/MarcusSchwarz/lesserphp/pull/18
Patch0: lesserphp--pullrequest-18.patch

BuildArch: noarch

%if 0%{?with_tests}
BuildRequires: php-composer(phpunit/phpunit) >= 4.8.35
%endif
BuildRequires: php-fedora-autoloader-devel

Requires: php-cli >= 5.3.0
Requires: php-ctype
Requires: php-date
Requires: php-fileinfo
Requires: php-pcre
Requires: php-composer(fedora/autoloader)

# Composer
Provides: php-composer(%{composer_vendor}/%{composer_project}) = %{version}

# This project is a fork of lessphp, which was previously packaged for Fedora
Obsoletes: php-lessphp <= 0.5.0+0


%description
lesserphp is a compiler that generates CSS from a superset language which adds
a collection of convenient features often seen in other languages.
All CSS is compatible with LESS, so you can start using new features
with your existing CSS.

It is designed to be compatible with less.js (https://lesscss.org/),
and suitable as a drop-in replacement for PHP projects.

Autoloader: %{pkgdir}/autoload.php


%prep
%autosetup -p1 -n %{repo_name}-%{version}

# Lessify is broken upstream and we don't want to install it
rm lessify lessify.inc.php

# Fix include paths
sed -e 's|^require $path."lessc.inc.php";$|require "%{pkgdir}/lessc.inc.php";|' -i plessc

# Fix homepage link in composer.json (still points to pre-fork page)
sed -e 's|"http://leafo.net/lessphp/"|"https://www.maswaba.de/lesserphpdocs/"|' -i composer.json


%build
# Create autoloader
phpab \
  --template fedora \
  --output autoload.php \
  lessc.inc.php
cat autoload.php


%install
# Library
install -d -m 755 %{buildroot}%{pkgdir}
install -m 644 -p autoload.php lessc.inc.php %{buildroot}%{pkgdir}/

# Executables
install -d -m 755 %{buildroot}%{_bindir}
install -m 0755 -p plessc  %{buildroot}%{_bindir}/plessc


%check
%if 0%{?with_tests}
phpunit --verbose --bootstrap %{buildroot}%{pkgdir}/autoload.php
%endif


%files
%license LICENSE
%doc *.md
%doc composer.json
%{pkgdir}/
%{_bindir}/plessc


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Mar 13 2020 Artur Iwicki <fedora@svgames.pl> - 0.5.4-5
- Fix FedoraAutoloader-related Requires/BuildRequires

* Thu Mar 12 2020 Artur Iwicki <fedora@svgames.pl> - 0.5.4-4
- Include a patch to address uses of deprecated syntax in plessc
- Do not include "lessify" in the package (broken upstream code)

* Tue Mar 10 2020 Artur Iwicki <fedora@svgames.pl> - 0.5.4-3
- Add a fake revision number to the "Obsoletes: php-lessphp" tag
- Make executables include required files directly, instead of using the autoloader

* Sat Mar 07 2020 Artur Iwicki <fedora@svgames.pl> - 0.5.4-2
- Fix the License: tag
- Preserve timestamps during %%install

* Mon Mar 02 2020 Artur Iwicki <fedora@svgames.pl> - 0.5.4-1
- Initial packaging

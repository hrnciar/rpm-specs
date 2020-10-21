# Fedora spec file for php-markdown
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#
%global gh_commit    c83178d49e372ca967d1a8c77ae4e051b3a3c75c
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     michelf
%global gh_project   php-markdown

Name:        php-markdown
Version:     1.9.0
Release:     3%{?dist}
Summary:     Markdown implementation in PHP

License:     BSD
URL:         https://michelf.ca/projects/php-markdown/
Source0:     %{name}-%{version}-%{gh_short}.tgz
Source1:     makesrc.sh

BuildArch:   noarch
BuildRequires: php-fedora-autoloader-devel
# For tests
#       "require-dev": {
#               "phpunit/phpunit": ">=4.3 <5.8"
BuildRequires: phpunit

Requires:    php(language) >= 5.3
Requires:    php-pcre
Requires:    php-composer(fedora/autoloader)

Provides:    php-composer(michelf/php-markdown) = %{version}


%description
This is a PHP implementation of John Gruber's Markdown.
It is almost completely compliant with the reference implementation.

This packages provides the classic version %{classic_version} and the new
library version %{version}.

Autoloader: %{_datadir}/php/Michelf/markdown-autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}
mv License.md LICENSE


%build
: Generate simple autoloader
%{_bindir}/phpab \
    --template fedora \
    --output Michelf/markdown-autoload.php \
    Michelf
cat Michelf/markdown-autoload.php


%install
install -d %{buildroot}%{_datadir}/php/

# PSR-0 library
cp -pr Michelf %{buildroot}%{_datadir}/php/Michelf


%check
php -r '
require_once "%{buildroot}%{_datadir}/php/Michelf/markdown-autoload.php";
  $ver = Michelf\Markdown::MARKDOWNLIB_VERSION;
  echo "Version=$ver, expected=%{version}\n";
  return (version_compare($ver, "%{version}", "=") ? 0 : 1);
'
cat << 'EOF' | tee bs.php
<?php
require "%{buildroot}%{_datadir}/php/Michelf/markdown-autoload.php";
require "test/bootstrap.php";
EOF

ret=0
for php in php php72 php73 php74
do
  if which $php
  then
    $php %{_bindir}/phpunit --bootstrap bs.php || ret=1
  fi
done
exit $ret


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc composer.json
%doc *.md
# Library version
%{_datadir}/php/Michelf


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec  2 2019 Remi Collet <remi@remirepo.net> - 1.9.0-1
- update to 1.9.0
- run upstream test suite

* Fri Jul 26 2019 Remi Collet <remi@remirepo.net> - 1.8.0-6
- drop old classic version
- use git snapshot as next version will have test suite
- add patch for PHP 7.4, adapted for 1.8.0 from
  https://github.com/michelf/php-markdown/pull/316

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 15 2018 Remi Collet <remi@remirepo.net> - 1.8.0-1
- Mardown PSR-0/PSR-4 library version 1.8.0

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Oct 30 2016 Remi Collet <remi@fedoraproject.org> - 1.7.0-1
- Mardown PSR-0 library version 1.7.0
- switch to fedora/autoloader
- add minimal %%check for version and autoloader

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Dec 26 2015 Remi Collet <remi@fedoraproject.org> - 1.6.0-1
- Mardown PSR-0 library version 1.6.0
- add simple autoloader

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Mar  2 2015 Remi Collet <remi@fedoraproject.org> - 1.5.0-1
- Mardown PSR-0 library version 1.5.0
- fix license handling
- add provides php-composer(michelf/php-markdown)
- fix project URL

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May  6 2014 Remi Collet <remi@fedoraproject.org> - 1.4.1-1
- Mardown PSR-0 library version 1.4.1

* Mon Dec 02 2013 Remi Collet <remi@fedoraproject.org> - 1.4.0-1
- Mardown PSR-0 library version 1.4.0 (sources 1.2.8)
- Mardown classic library version 1.0.2

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jun 15 2013 Remi Collet <remi@fedoraproject.org> - 1.2.7-1
- Mardown PSR-0 library version 1.2.7 (added)
- Mardown classic library version 1.0.1q (updated)

* Tue Jan 29 2013 Remi Collet <remi@fedoraproject.org> - 1.0.1p-1
- Updated to 1.0.1p
- don't requires php

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1n-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1n-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1n-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon May 03 2010 Rakesh Pandit <rakesh@fedoraproject.irg> 1.0.1n-1
- Updated to 1.0.1n

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1m-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun May 24 2009 Rakesh Pandit <rakesh@fedoraproject.irg> 1.0.1m-2
- Fixed mixed use of space and tabs, using install in place of cp

* Sun May 24 2009 Rakesh Pandit <rakesh@fedoraproject.org> 1.0.1m-1
- Initial package

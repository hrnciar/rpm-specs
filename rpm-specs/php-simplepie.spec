#
# Fedora spec file for php-simplepie
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#
%global gh_commit    20b30e4bbbed7fd2a6ffbab48e3a2e0f96087b6a
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     simplepie
%global gh_project   simplepie
%global gh_version   1.5.4
%global with_tests   0%{!?_without_tests:1}

Name:       php-%{gh_project}
Version:    %{gh_version}
Release:    3%{?dist}
Summary:    A simple Atom/RSS parsing library for PHP

Group:      Development/Libraries
License:    BSD
URL:        http://simplepie.org/

# Use a git snapshot as upstream remove tests from distribution
Source0:       %{name}-%{gh_version}-%{gh_short}.tgz
# Script to pull the git snapshot
Source1:       %{name}-makesrc.sh

# Adapt autoloader for installation tree
Patch0:     %{name}-rpm.patch

BuildArch:  noarch
%if %{with_tests}
# From composer.json, "require-dev"
#		"phpunit/phpunit": "~5.4.3 || ~6.5"
BuildRequires:    phpunit6 >= 6.5
%global phpunit %{_bindir}/phpunit6
%endif

# from composer.json, "require"
#               "php": ">=5.6.0",
#               "ext-pcre": "*",
#               "ext-xml": "*",
#               "ext-xmlreader": "*"
Requires:    php(language) >= 5.6
Requires:    php-pcre
Requires:    php-xml
Requires:    php-xmlreader
# from composer.json, "suggests"
#               "ext-curl": "",
#               "ext-iconv": "",
#               "ext-intl": "",
#               "ext-mbstring": "",
Requires:    php-curl
Requires:    php-iconv
Requires:    php-intl
Requires:    php-mbstring
# from phpcompatinfo
Requires:    php-IDNA_Convert
Requires:    php-date
Requires:    php-dom
Requires:    php-libxml
Requires:    php-pdo
Requires:    php-reflection
# Optional: memcache, memcached, redis, zlib

Provides:       php-composer(%{gh_owner}/%{gh_project}) = %{version}


%description
SimplePie is a very fast and easy-to-use class, written in PHP, that puts the 
'simple' back into 'really simple syndication'. Flexible enough to suit 
beginners and veterans alike, SimplePie is focused on speed, ease of use, 
compatibility and standards compliance.

Autoloader: %{_datadir}/php/%{name}/autoloader.php


%prep
%setup -qn %{gh_project}-%{gh_commit}

%patch0 -p1 -b .rpm

# fix rpmlint warnings
find . -type f -exec chmod -x {} \;
# drop demo; contains flash files
rm -rf demo


%build
#non-empty build section to quell the belching that rpmlint does with an empty build


%install
mkdir -p %{buildroot}/%{_datadir}/php/
cp -ar library %{buildroot}/%{_datadir}/php/%{name}

install -pm 644 autoloader.php \
    %{buildroot}/%{_datadir}/php/%{name}/autoloader.php


%if %{with_tests}
%check
sed -e 's:@PATH@:%{buildroot}/%{_datadir}/php/%{name}:' \
    -i tests/bootstrap.php

ret=0
for cmdarg in "php %{phpunit}" "php56 %{_bindir}/phpunit" php70 php71 php72 php73 php74; do
  if which $cmdarg; then
    set $cmdarg
    $1 ${2:-%{_bindir}/phpunit6} --verbose || ret=1
  fi
done
exit $ret
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE.txt
%doc composer.json
%doc README.markdown
%doc ROADMAP.md
%{_datadir}/php/%{name}


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 18 2019 Remi Collet <remi@remirepo.net> - 1.5.4-1
- update to 1.5.4
- drop patch merged upstream

* Wed Oct  9 2019 Remi Collet <remi@remirepo.net> - 1.5.3-1
- update to 1.5.3
- add patch for PHP 7.4 from
  https://github.com/simplepie/simplepie/pull/628

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct  2 2018 Remi Collet <remi@remirepo.net> - 1.5.2-1
- update to 1.5.2
- raise dependency on PHP 5.6
- switch to phpunit6
- fix LICENSE installation

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Nov 14 2017 Remi Collet <remi@remirepo.net> - 1.5.1-1
- Update to 1.5.1
- run test suite with all version when SCL available
- add spec file License headers (MIT per FPCA)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Apr 25 2017 Johan Cwiklinski <jcwiklinski AT teclib DOT com> - 1.5-1
- Last upstream release

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jan 07 2017 Johan Cwiklinski <johan AT x-tnd DOT be> - 1.4.3-2
- Drop demo directory that contains flash files (bz #1000260)

* Sun Nov 27 2016 Johan Cwiklinski <johan AT x-tnd DOT be> - 1.4.3-1
- Last upstream release
- Change upstream download URL, use script to get tests
- provide php-composer(simplepie/simplepie)
- Backport some changes from Remi's specfile

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jan  2 2013 Remi Collet <remi@fedoraproject.org> - 1.3.1-3
- fix for php 5.3.3 (RHEL-6)
- disable test suite on RHEL-5
- better fix for rpmlint warnings
  (version-control-internal-file and script-without-shebang)

* Sun Dec 16 2012 Remi Collet <remi@fedoraproject.org> - 1.3.1-2
- really install library
- provides autoloader.php
- run tests

* Wed Dec 12 2012 Nick Bebout <nb@fedoraproject.org> - 1.3.1-1
- Update to 1.3.1

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Aug 30 2011 Adam Williamson <awilliam@redhat.com> - 1.2-1
- bump to 1.2 (a mere two years late!)

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Apr 23 2009 David Nalley <david@gnsa.us> 1.1.3-3
- used version macro in source url
- stopped using two different macros for buildroot
- stopped using macro for mkdir
- moved chmods to immediately after setup in prep
- removed line that rm compatibility_test
- used a single line to copy create.php and simplepie.inc
* Thu Apr 23 2009 David Nalley <david@gnsa.us> 1.1.3-2
- Removed php asa requires since php-IDNA_convert pulls it in
* Wed Apr 22 2009 David Nalley <david@gnsa.us> 1.1.3-1
- Initial packaging efforts


%global github_owner   smarty-php
%global github_name    smarty
%global github_version 3.1.33
%global github_commit  dd55b23121e55a3b4f1af90a707a6c4e5969530f

%global composer_vendor  smarty
%global composer_project smarty

# "php": ">=5.2"
%global php_min_ver 5.2

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-Smarty
Summary:       Smarty - the compiling PHP template engine
Version:       %{github_version}
Release:       4%{?dist}

License:       LGPLv3
URL:           http://www.smarty.net
Source0:       https://github.com/%{github_owner}/%{github_name}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
# composer.json
BuildRequires: php(language) >= %{php_min_ver}
# Library version value check
BuildRequires: php-cli

Requires:      php(language) >= %{php_min_ver}
# phpcompatinfo (computed from version 3.1.33)
Requires:      php-ctype
Requires:      php-date
Requires:      php-mbstring
Requires:      php-pcre
Requires:      php-spl
Requires:      php-zlib

# php-{COMPOSER_VENDOR}-{COMPOSER_PROJECT}
Provides:      php-%{composer_vendor}-%{composer_project} = %{version}-%{release}
# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
Smarty is a template engine for PHP, facilitating the separation of
presentation (HTML/CSS) from application logic. This implies that PHP
code is application logic, and is separated from the presentation.

Autoloader: %{phpdir}/Smarty/autoload.php


%prep
%setup -qn %{github_name}-%{github_commit}


%build
# Empty build section, nothing required


%install
mkdir -p %{buildroot}%{phpdir}
cp -rp libs %{buildroot}%{phpdir}/Smarty

: Standard autoloader
ln -s bootstrap.php %{buildroot}%{phpdir}/Smarty/autoload.php


%check
: Library version value check
php -r '
    require_once "%{buildroot}%{phpdir}/Smarty/autoload.php";
    $version = Smarty::SMARTY_VERSION;
    echo "Version $version (expected %{version})\n";
    exit(version_compare("%{version}", "$version", "=") ? 0 : 1);
'


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc change_log.txt
%doc composer.json
%doc NEW_FEATURES.txt
%doc README.md
%doc SMARTY*.txt
%{phpdir}/Smarty


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.33-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.33-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.33-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 22 2019 Shawn Iwinski <shawn@iwin.ski> - 3.1.33-1
- Update to 3.1.33
- RHBZ #s: 1532492, 1532493, 1532494, 1628739, 1628740, 1628741, 1631095, 1631096, 1631098
- CVEs: CVE-2017-1000480, CVE-2018-13982, CVE-2018-16831
- License LGPLv2+ => LGPLv3

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.21-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.21-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.21-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.21-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.21-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.21-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.21-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Oct 23 2014 Johan Cwiklinski <johan AT x-tnd DOT be> - 3.1.21-2
- Fix requires

* Thu Oct 23 2014 Johan Cwiklinski <johan AT x-tnd DOT be> - 3.1.21-1
- New upstream release
- Fix version constant

* Wed Oct 15 2014 Johan Cwiklinski <johan AT x-tnd DOT be> - 3.1.20-1
- New upstream release

* Thu Jul 31 2014 Johan Cwiklinski <johan AT x-tnd DOT be> - 3.1.19-2
- Add composer provides

* Wed Jul 30 2014 Johan Cwiklinski <johan AT x-tnd DOT be> - 3.1.19-1
- Last upstream release

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May 10 2014 Johan Cwiklinski <johan AT x-tnd DOT be> - 3.1.18-1
- Last upstream release

* Sun Dec 22 2013 Johan Cwiklinski <johan AT x-tnd DOT be> - 3.1.16-1
- Last upstream release

* Sun Dec 08 2013 Johan Cwiklinski <johan AT x-tnd DOT be> - 3.1.15-1
- Last upstream release

* Thu Aug 08 2013 Johan Cwiklinski <johan AT x-tnd DOT be> - 3.1.14-1
- Last upstream release

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Feb 12 2013 Johan Cwiklinski <johan AT x-tnd DOT be> - 3.1.13-1
- Last upstream release
- Missing mbstring require

* Sun Nov 25 2012 Johan Cwiklinski <johan AT x-tnd DOT be> - 3.1.12-2
- Really fix requires (see bz #700179 comment #30)

* Sun Nov 25 2012 Johan Cwiklinski <johan AT x-tnd DOT be> - 3.1.12-1
- Update to 3.1.12
- Remove CVE-2012-4437 patch that has been included in that release
- Requires php-common instead of php

* Thu Sep 20 2012 Jon Ciesla <limburgher@gmail.com> - 3.1.11-1
- Update to 3.1.11, patch for CVE-2012-4437, BZ 858989.

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 22 2012 Johan Cwiklinski <johan AT x-tnd DOT be> - 3.1.10-1
- Update to 3.1.10

* Mon May 07 2012 Jon Ciesla <limburgher@gmail.com> - 3.1.8-1
- Update to 3.1.8, BZ 819162.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.26-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Oct 11 2009 Christopher Stone <chris.stone@gmail.com> 2.6.26-1
- Upstream sync
- Update %%source0 and %%URL

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon May 25 2009 Christopher Stone <chris.stone@gmail.com> 2.6.25-1
- Upstream sync

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Nov 02 2008 Christopher Stone <chris.stone@gmail.com> 2.6.20-2
- Add security patch (bz #469648)
- Add RHL dist tag conditional for Requires

* Mon Oct 13 2008 Christopher Stone <chris.stone@gmail.com> 2.6.20-1
- Upstream sync

* Wed Feb 20 2008 Christopher Stone <chris.stone@gmail.com> 2.6.19-1
- Upstream sync
- Update %%license
- Fix file encoding

* Sun Apr 29 2007 Christopher Stone <chris.stone@gmail.com> 2.6.18-1
- Upstream sync

* Wed Feb 21 2007 Christopher Stone <chris.stone@gmail.com> 2.6.16-2
- Minor spec file changes/cleanups

* Fri Feb 09 2007 Orion Poplawski <orion@cora.nwra.com> 2.6.16-1
- Update to 2.6.16
- Install in /usr/share/php/Smarty
- Update php version requirement

* Tue May 16 2006 Orion Poplawski <orion@cora.nwra.com> 2.6.13-1
- Update to 2.6.13

* Tue Nov  1 2005 Orion Poplawski <orion@cora.nwra.com> 2.6.10-2
- Fix Source0 URL.

* Thu Oct 13 2005 Orion Poplawski <orion@cora.nwra.com> 2.6.10-1
- Initial Fedora Extras version

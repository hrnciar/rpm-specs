#
# RPM spec file for php-psr-http-message
#
# Copyright (c) 2014-2016 Shawn Iwinski <shawn.iwinski@gmail.com>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     php-fig
%global github_name      http-message
%global github_version   1.0.1
%global github_commit    f6561bf28d520154e4b0ec72be95418abe6d9363

%global composer_vendor  psr
%global composer_project http-message

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       8%{?github_release}%{?dist}
Summary:       Common interface for HTTP messages (PSR-7)

License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}
Source0:       %{url}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
# Autoload generation
BuildRequires: %{_bindir}/phpab
# For tests
BuildRequires: php-cli

# phpcompatinfo (computed from version 1.0)
Requires:      php(language) >= 5.3.0

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
This package holds all interfaces/classes/traits related to PSR-7 [1].

Note that this is not a HTTP message implementation of its own. It is merely an
interface that describes a HTTP message. See the specification for more details.

Autoloader: %{phpdir}/Psr/Http/Message/autoload.php

[1] http://www.php-fig.org/psr/psr-7/


%prep
%setup -qn %{github_name}-%{github_commit}


%build
: Generate autoloader
%{_bindir}/phpab --nolower --output src/autoload.php src


%install
mkdir -p %{buildroot}%{phpdir}/Psr/Http/Message
cp -rp src/* %{buildroot}%{phpdir}/Psr/Http/Message/


%check
: Test autoloader
php -r '
require "%{buildroot}%{phpdir}/Psr/Http/Message/autoload.php";
exit (interface_exists("Psr\\Http\\Message\\UriInterface") ? 0 : 1);
'


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc *.md
%doc composer.json
%dir %{phpdir}/Psr
%dir %{phpdir}/Psr/Http
     %{phpdir}/Psr/Http/Message


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Aug  7 2016 Remi Collet <remi@fedoraproject.org> - 1.0.1-1
- update to 1.0.1 (only comments)
- add check for autoloader

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 30 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.0-1
- Updated to 1.0 (BZ #1218459)
- Added autoloader

* Mon Apr 13 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.10.1-1
- Updated to 0.10.1 (BZ #1187918)

* Sun Apr 12 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.9.2-1
- Updated to 0.9.2 (BZ #1187918)

* Wed Jan 28 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.7.0-1
- Updated to 0.7.0 (BZ #1183600)

* Tue Jan 27 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.6.0-1
- Updated to 0.6.0 (BZ #1183600)

* Thu Nov 20 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.5.1-1
- Updated to 0.5.1 (BZ #1163322)

* Thu Oct 30 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.4.0-1
- Initial package

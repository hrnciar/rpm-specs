# remirepo/fedora spec file for php-zetacomponents-unit-test
#
# Copyright (c) 2015-2019 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%global gh_commit    95f0c2e113994f88ab866779d673e285d3da7e66
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     zetacomponents
%global gh_project   UnitTest
%global cname        unit-test
%global ezcdir       %{_datadir}/php/ezc

Name:           php-%{gh_owner}-%{cname}
Version:        1.1.2
Release:        4%{?dist}
Summary:        Zeta UnitTest Component

License:        ASL 2.0
URL:            http://zetacomponents.org/
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{gh_project}-%{version}-%{gh_short}.tar.gz

BuildArch:      noarch
BuildRequires:  php-fedora-autoloader-devel

# From phpcompatinfo report for 1.0.2
Requires:       php(language) > 5.3
Requires:       php-pcre
Requires:       php-reflection
Requires:       php-spl
Requires:       php-composer(phpunit/phpunit)
# Also use Exception for Base, skipped to avoid circular dep.
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{gh_owner}/%{cname}) = %{version}


%description
UnitTest is an internal component which extends PhpUnit to facilitate test
running and reports of the components themselves.

For this reason, there is no tutorial for this component. If you really want
to use it for some reason it's sane to expect some community support on IRC or
the mailing list.


%prep
%setup -q -n %{gh_project}-%{gh_commit}


%build
: Generate a simple autoloader
%{_bindir}/phpab \
   --template fedora \
   --output src/autoloader.php \
   src


%install
mkdir -p %{buildroot}%{ezcdir}/autoload

: The library
cp -pr src \
       %{buildroot}%{ezcdir}/%{gh_project}
: For ezcBase autoloader
cp -pr src/*_autoload.php \
       %{buildroot}%{ezcdir}/autoload


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE* CREDITS
%doc ChangeLog
%doc composer.json
%doc docs design
%dir %{ezcdir}
%dir %{ezcdir}/autoload
     %{ezcdir}/autoload/*_autoload.php
     %{ezcdir}/%{gh_project}


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb 27 2019 Remi Collet <remi@remirepo.net> - 1.1.2-1
- update to 1.1.2

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jun 29 2015 Remi Collet <remi@fedoraproject.org> - 1.0.2-3
- fix depedency on phpunit (EL-6)

* Thu Jun  4 2015 Remi Collet <remi@fedoraproject.org> - 1.0.2-2
- add upstream patch for LICENSE file

* Wed Jun  3 2015 Remi Collet <remi@fedoraproject.org> - 1.0.2-1
- initial package
- open https://github.com/zetacomponents/UnitTest/issues/4 License
- open https://github.com/zetacomponents/UnitTest/pull/5 phpunit 4
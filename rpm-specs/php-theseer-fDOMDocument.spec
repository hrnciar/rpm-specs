# remirepo/fedora spec file for php-theseer-fDOMDocument
#
# Copyright (c) 2013-2019 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%global gh_commit    6e8203e40a32a9c770bcb62fe37e68b948da6dca
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     theseer
%global gh_project   fDOMDocument
%global php_home     %{_datadir}/php/TheSeer
%global pear_name    fDOMDocument
%global pear_channel pear.netpirates.net

Name:           php-theseer-fDOMDocument
Version:        1.6.6
Release:        8%{?dist}
Summary:        An Extension to PHP standard DOM

License:        BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{name}-%{version}-%{gh_short}.tar.gz

BuildArch:      noarch
BuildRequires:  php(language) >= 5.3.3
# For test
%if 0%{?fedora} >= 26 || 0%{?rhel} >= 8
%global phpunit %{_bindir}/phpunit6
%else
%global phpunit %{_bindir}/phpunit
%endif
BuildRequires:  %{phpunit}
BuildRequires:  php-dom
BuildRequires:  php-libxml
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer.json, requires
#        "php": ">=5.3.3",
#        "ext-dom": "*",
#        "lib-libxml": "*"
Requires:       php(language) >= 5.3.3
Requires:       php-dom
Requires:       php-libxml
# From phpcompatinfo report for version 1.6.0
Requires:       php-pcre
Requires:       php-spl
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-pear(%{pear_channel}/%{pear_name}) = %{version}
Provides:       php-composer(theseer/fdomdocument) = %{version}


%description
An Extension to PHP's standard DOM to add various convenience methods
and exceptions by default


%prep
%setup -q -n %{gh_project}-%{gh_commit}


%build
: Generate a simple classmap autoloader
%{_bindir}/phpab --template fedora --output src/autoload.php src


%install
mkdir -p   %{buildroot}%{php_home}
cp -pr src %{buildroot}%{php_home}/%{gh_project}


%check
ret=0
for cmd in "php %{phpunit}" "php56 %{_bindir}/phpunit" php70 php71 php72; do
  if which $cmd; then
    set $cmd
    $1 ${2:-%{_bindir}/phpunit6} \
      --bootstrap %{buildroot}%{php_home}/%{gh_project}/autoload.php \
      --verbose || ret=1
  fi
done
exit $ret


%post
if [ -x %{_bindir}/pear ]; then
  %{_bindir}/pear uninstall --nodeps --ignore-errors --register-only \
      %{pear_channel}/%{pear_name} >/dev/null || :
fi


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc README.md composer.json
%{php_home}/%{gh_project}


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb 20 2019 Remi Collet <remi@remirepo.net> - 1.6.6-6
- cleanup for EL-8

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jul  2 2017 Remi Collet <remi@remirepo.net> - 1.6.6-1
- Update to 1.6.6

* Mon Apr 24 2017 Remi Collet <remi@remirepo.net> - 1.6.5-1
- Update to 1.6.5 (no change)
- drop patch merged upstream

* Fri Apr 14 2017 Remi Collet <remi@remirepo.net> - 1.6.2-1
- Update to 1.6.2
- use phpunit6 when available
- add fix for PHP 7.2 and PHPUnit 6 from
  https://github.com/theseer/fDOMDocument/pull/29

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu May 28 2015 Remi Collet <remi@fedoraproject.org> - 1.6.1-1
- Update to 1.6.1

* Wed Nov 26 2014 Remi Collet <remi@fedoraproject.org> - 1.6.0-2
- switch from pear to github sources

* Sun Sep 14 2014 Remi Collet <remi@fedoraproject.org> - 1.6.0-1
- Update to 1.6.0
- provide php-composer(theseer/fdomdocument)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Feb 19 2014 Remi Collet <remi@fedoraproject.org> - 1.5.0-1
- Update to 1.5.0

* Sat Dec 21 2013 Remi Collet <remi@fedoraproject.org> - 1.4.3-1
- Update to 1.4.3 (stable)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jun 30 2013 Remi Collet <remi@fedoraproject.org> - 1.4.2-1
- Update to 1.4.2

* Sun Apr 28 2013 Remi Collet <remi@fedoraproject.org> - 1.4.1-1
- Version 1.4.1 (stable) - API 1.4.0 (stable)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Oct 28 2012 Remi Collet <remi@fedoraproject.org> - 1.3.2-1
- Version 1.3.2 (stable) - API 1.3.0 (stable)
- run test units

* Thu Oct 11 2012 Remi Collet <remi@fedoraproject.org> - 1.3.1-1
- Version 1.3.1 (stable) - API 1.3.0 (stable)
- Initial packaging


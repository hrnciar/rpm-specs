# spec file for php-theseer-directoryscanner
#
# Copyright (c) 2014-2017 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global gh_commit    549aa9fdbc47d50365db42d9ade35fdef65f854c
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     theseer
%global gh_project   DirectoryScanner
%global php_home     %{_datadir}/php/TheSeer
%global pear_name    DirectoryScanner
%global pear_channel pear.netpirates.net

Name:           php-theseer-directoryscanner
Version:        1.3.2
Release:        8%{?dist}
Summary:        A recursive directory scanner and filter

License:        BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{gh_project}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  php(language) >= 5.3.1
BuildRequires:  %{_bindir}/phpunit

# From composer.json
Requires:       php(language) >= 5.3.1
# From phpcompatinfo report for 1.3.0
Requires:       php-fileinfo
Requires:       php-spl

Provides:       php-composer(theseer/directoryscanner) = %{version}
Provides:       php-pear(%{pear_channel}/%{pear_name}) = %{version}


%description
A recursive directory scanner and filter.


%prep
%setup -q -n %{gh_project}-%{gh_commit}


%build
# Empty build section, most likely nothing required.


%install
mkdir -p   %{buildroot}%{php_home}
cp -pr src %{buildroot}%{php_home}/%{gh_project}


%check
ret=0
for cmd in php56 php70 php71 php; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit \
         --bootstrap %{buildroot}%{php_home}/%{gh_project}/autoload.php \
         --verbose \
         --no-coverage || ret=1
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
%doc composer.json
%dir %{php_home}
%{php_home}/%{gh_project}


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Mar 10 2017 Remi Collet <remi@remirepo.net> - 1.3.2-1
- Update to 1.3.2 (no change)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Nov 25 2014 Remi Collet <remi@fedoraproject.org> - 1.3.1-1
- update to 1.3.1
- switch from pear to github sources
- enable test suite

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Apr  6 2014 Remi Collet <remi@fedoraproject.org> - 1.3.0-1
- initial package, version 1.3.0
# remirepo/fedora spec file for php-sebastian-object-reflector
#
# Copyright (c) 2017 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global bootstrap    0
%global gh_commit    773f97c67f28de00d397be301821b06708fca0be
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sebastianbergmann
%global gh_project   object-reflector
%global pk_vendor    sebastian
%global pk_project   %{gh_project}
%global major        %nil
%global ns_vendor    SebastianBergmann
%global ns_project   ObjectReflector
%global php_home     %{_datadir}/php
%if %{bootstrap}
%global with_tests   0%{?_with_tests:1}
%else
%global with_tests   0%{!?_without_tests:1}
%endif

Name:           php-%{pk_vendor}-%{pk_project}%{major}
Version:        1.1.1
Release:        7%{?dist}
Summary:        Allows reflection of object attributes

License:        BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{name}-%{version}-%{gh_short}.tar.gz

BuildArch:      noarch
BuildRequires:  php(language) >= 7.0
BuildRequires:  php-fedora-autoloader-devel
%if %{with_tests}
# from composer.json, "require-dev": {
#        "phpunit/phpunit": "^6.0"
BuildRequires:  phpunit6
%endif

# from composer.json
#        "php": "^7.0"
Requires:       php(language) >= 7.0
# from phpcompatinfo report for version 1.0.0
Requires:       php-reflection
Requires:       php-spl
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}


%description
Allows reflection of object attributes, including inherited
and non-public ones.


%prep
%setup -q -n %{gh_project}-%{gh_commit}


%build
# Generate the Autoloader
%{_bindir}/phpab --template fedora --output src/autoload.php src
sed -e 's:/usr/share/php/::' -i src/autoload.php


%install
mkdir -p   %{buildroot}%{php_home}/%{ns_vendor}
cp -pr src %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}


%check
%if %{with_tests}
mkdir vendor
%{_bindir}/phpab --output vendor/autoload.php tests/_fixture
cat << 'EOF' | tee -a vendor/autoload.php
require_once '%{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php';
EOF

: Run upstream test suite
ret=0
for cmd in php70 php71 php; do
  if which $cmd; then
    %{_bindir}/php -d include_path=.:%{buildroot}%{_datadir}/php:%{_datadir}/php \
    %{_bindir}/phpunit6  --verbose || ret=1
  fi
done
exit $ret
%else
: bootstrap build with test suite disabled
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc README.md composer.json
%dir %{php_home}/%{ns_vendor}
     %{php_home}/%{ns_vendor}/%{ns_project}%{major}


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Mar 29 2017 Remi Collet <remi@remirepo.net> - 1.1.1-1
- Update to 1.1.1

* Thu Mar 16 2017 Remi Collet <remi@remirepo.net> - 1.1.0-1
- Update to 1.1.0

* Sun Mar 12 2017 Remi Collet <remi@remirepo.net> - 1.0.0-1
- initial package
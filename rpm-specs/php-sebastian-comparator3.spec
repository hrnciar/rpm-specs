# remirepo/fedora spec file for php-sebastian-comparator3
#
# Copyright (c) 2014-2018 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global bootstrap    0
%global gh_commit    5de4fc177adf9bce8df98d8d141a7559d7ccf6da
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sebastianbergmann
%global gh_project   comparator
%global pk_vendor    sebastian
%global pk_project   %{gh_project}
%global major        3
%global php_home     %{_datadir}/php
%global ns_vendor    SebastianBergmann
%global ns_project   Comparator
%if %{bootstrap}
%global with_tests   %{?_with_tests:1}%{!?_with_tests:0}
%else
%global with_tests   %{?_without_tests:0}%{!?_without_tests:1}
%endif

Name:           php-%{pk_vendor}-%{pk_project}%{major}
Version:        3.0.2
Release:        5%{?dist}
Summary:        Compare PHP values for equality

License:        BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{name}-%{version}-%{gh_short}.tar.gz

BuildArch:      noarch
BuildRequires:  php(language) >= 7.1
BuildRequires:  (php-composer(%{pk_vendor}/diff) >= 3.0     with php-composer(%{pk_vendor}/diff) <  4)
BuildRequires:  (php-composer(%{pk_vendor}/exporter) >= 3.1 with php-composer(%{pk_vendor}/exporter) <  4)
BuildRequires:  php-fedora-autoloader-devel
%if %{with_tests}
# from composer.json, "require-dev": {
#        "phpunit/phpunit": "^7.1"
BuildRequires:  phpunit7 >= 7.1
%endif

# from composer.json
#        "php": "^7.1",
#        "sebastian/diff": "^3.0",
#        "sebastian/exporter": "^3.1"
Requires:       php(language) >= 7.1
Requires:       (php-composer(%{pk_vendor}/diff) >= 3.0     with php-composer(%{pk_vendor}/diff) <  4)
Requires:       (php-composer(%{pk_vendor}/exporter) >= 3.1 with php-composer(%{pk_vendor}/exporter) <  4)
# from phpcompatinfo report for version 3.0.0
Requires:       php-date
Requires:       php-dom
Requires:       php-spl
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}


%description
This component provides the functionality to compare PHP values for equality.

Autoloader: %{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}


%build
# Generate the Autoloader
phpab --template fedora --output src/autoload.php src

# Rely on include_path as in PHPUnit dependencies
cat <<EOF | tee -a src/autoload.php

\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/%{ns_vendor}/Diff3/autoload.php',
    '%{php_home}/%{ns_vendor}/Exporter3/autoload.php',
]);
EOF


%install
mkdir -p   %{buildroot}%{php_home}/%{ns_vendor}
cp -pr src %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}


%check
%if %{with_tests}
mkdir vendor
%{_bindir}/phpab --template fedora --output vendor/autoload.php tests/_fixture

: Run upstream test suite
ret=0
for cmd in php php71 php72 php73; do
  if which $cmd; then
    $cmd -d auto_prepend_file=%{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php \
      %{_bindir}/phpunit7 --no-coverage --verbose || ret=1
  fi
done
exit $ret
%else
: bootstrap build with test suite disabled
%endif


%files
%doc README.md composer.json
%{!?_licensedir:%global license %%doc}
%license LICENSE

%{php_home}/%{ns_vendor}/%{ns_project}%{major}


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jul 12 2018 Remi Collet <remi@remirepo.net> - 3.0.2-1
- update to 3.0.2

* Tue Jun 19 2018 Remi Collet <remi@remirepo.net> - 3.0.1-1
- update to 3.0.1

* Wed Apr 18 2018 Remi Collet <remi@remirepo.net> - 3.0.0-1
- update to 3.0.0
- rename to php-sebastian-comparator3
- raise dependency on PHP 7.1
- raise dependency on sebastian/diff 3.0
- use phpunit7

* Fri Feb  2 2018 Remi Collet <remi@remirepo.net> - 2.1.3-1
- Update to 2.1.3 (no change)
- allow sebastian/diff v3
- use range dependencies on F27+

* Fri Jan 12 2018 Remi Collet <remi@remirepo.net> - 2.1.2-1
- Update to 2.1.2

* Sat Dec 23 2017 Remi Collet <remi@remirepo.net> - 2.1.1-1
- Update to 2.1.1

* Fri Nov  3 2017 Remi Collet <remi@remirepo.net> - 2.1.0-1
- Update to 2.1.0
- raise dependency on sebastian/exporter 3.1

* Fri Aug  4 2017 Remi Collet <remi@remirepo.net> - 2.0.2-1
- Update to 2.0.2
- raise dependency on sebastian/diff 2.0
- raise various dependencies on latest minor version

* Wed Jul 12 2017 Remi Collet <remi@remirepo.net> - 2.0.1-1
- Update to 2.0.1

* Fri Mar  3 2017 Remi Collet <remi@fedoraproject.org> - 2.0.0-1
- update to 3.0.0
- rename to php-sebastian-comparator2
- raise dependency on PHP 7
- raise dependency on sebastian/exporter 3

* Sun Jan 29 2017 Remi Collet <remi@fedoraproject.org> - 1.2.4-1
- update to 1.2.4

* Sun Jan 29 2017 Remi Collet <remi@fedoraproject.org> - 1.2.3-1
- update to 1.2.3

* Tue Nov 22 2016 Remi Collet <remi@fedoraproject.org> - 1.2.2-1
- update to 1.2.2 (no change)
- allow sebastian/exporter 2.0

* Thu Nov 17 2016 Remi Collet <remi@fedoraproject.org> - 1.2.1-1
- update to 1.2.1
- switch to fedora/autoloader

* Sun Jul 26 2015 Remi Collet <remi@fedoraproject.org> - 1.2.0-1
- update to 1.2.0

* Mon Jun 29 2015 Remi Collet <remi@fedoraproject.org> - 1.1.1-3
- manage dependencies in autoloader

* Fri Jan 30 2015 Remi Collet <remi@fedoraproject.org> - 1.1.1-1
- update to 1.1.1
- raise dependency on sebastian/diff >= 1.2
- raise dependency on sebastian/exporter >= 1.2

* Thu Dec  4 2014 Remi Collet <remi@fedoraproject.org> - 1.1.0-1
- update to 1.1.0

* Sun Oct  5 2014 Remi Collet <remi@fedoraproject.org> - 1.0.1-1
- update to 1.0.1
- enable test suite

* Fri Jul 18 2014 Remi Collet <remi@fedoraproject.org> - 1.0.0-2
- add composer dependencies

* Sat May  3 2014 Remi Collet <remi@fedoraproject.org> - 1.0.0-1
- initial package

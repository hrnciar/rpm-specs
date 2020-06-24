# remirepo/fedora spec file for php-doctrine-event-manager
#
# Copyright (c) 2018-2019 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%global bootstrap    0
%global gh_commit    629572819973f13486371cb611386eb17851e85c
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     doctrine
%global gh_project   event-manager
# packagist
%global pk_vendor    %{gh_owner}
%global pk_project   %{gh_project}
# Namespace
%global ns_vendor    Doctrine
%global ns_project   Common
%global ns_subproj   EventManager
%if %{bootstrap}
%global with_tests   0%{?_with_tests:1}
%else
%global with_tests   0%{!?_without_tests:1}
%endif

Name:           php-%{pk_vendor}-%{pk_project}
Version:        1.1.0
Release:        2%{?dist}
Summary:        Simple PHP event system

License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
BuildRequires:  php-fedora-autoloader-devel
%if %{with_tests}
BuildRequires:  php(language) >= 7.1
BuildRequires:  phpunit7
%endif

# From composer.json
#        "php": "^7.1"
Requires:       php(language) >= 7.1
# From phpcompatinfo report for version 1.0.0: only "core"
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}
# Split off doctrine/common
Conflicts:      php-doctrine-common < 1:2.9


%description
The Doctrine Event Manager is a simple PHP event system that was built
to be used with the various Doctrine projects.

Autoloader: %{_datadir}/php/%{ns_vendor}/%{ns_project}/%{ns_subproj}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}


%build
: Generate a simple autoloader
mkdir lib/%{ns_vendor}/%{ns_project}/%{ns_subproj}
%{_bindir}/phpab \
    --output lib/%{ns_vendor}/%{ns_project}/%{ns_subproj}/autoload.php \
    --template fedora \
    lib/%{ns_vendor}/%{ns_project}


%install
mkdir -p                              %{buildroot}%{_datadir}/php/%{ns_vendor}
cp -pr lib/%{ns_vendor}/%{ns_project} %{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}


%check
%if %{with_tests}
: Generate autoloader
mkdir vendor
%{_bindir}/phpab \
    --output vendor/autoload.php \
    --template fedora \
    tests
cat << 'EOF' | tee -a vendor/autoload.php
require "%{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}/%{ns_subproj}/autoload.php";
EOF

: Run test suite
ret=0
for cmd in php php71 php72 php73 php74; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit7 \
        --bootstrap vendor/autoload.php \
        --verbose || ret=1
  fi
done
exit $ret
%else
: Test suite disabled
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc *.md
%doc composer.json
%dir %{_datadir}/php/%{ns_vendor}/
     %{_datadir}/php/%{ns_vendor}/%{ns_project}/


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 12 2019 Remi Collet <remi@remirepo.net> - 1.1.0-1
- update to 1.1.0

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 22 2018 Remi Collet <remi@remirepo.net> - 1.0.0-2
- fix conflicts

* Thu Oct 18 2018 Remi Collet <remi@remirepo.net> - 1.0.0-1
- initial package, version 1.0.0

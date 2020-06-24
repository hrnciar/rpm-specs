# remirepo/fedora spec file for php-phplang-scope-exit
#
# Copyright (c) 2019 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%global with_tests   0%{!?_without_tests:1}
# Github
%global gh_commit    8b5a1cbc54df7c1d14916711fb339e67d08cb3dd
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     phplang
%global gh_project   scope-exit
# Packagist
%global pk_vendor    %{gh_owner}
%global pk_project   %{gh_project}
# Namespace
%global ns_vendor    PhpLang
%global ns_project   %nil
%global major        %nil

Name:           php-%{pk_vendor}-%{pk_project}%{major}
Version:        1.0.0
Release:        3%{?gh_date?%{gh_date}git%{gh_short}}%{?dist}
Summary:        Emulation of SCOPE_EXIT construct from C++

License:        BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{name}-%{version}-%{?gh_short}.tar.gz

BuildArch:      noarch
%if %{with_tests}
BuildRequires:  php(language)
# For tests, from composer.json "require-dev": {
#        "phpunit/phpunit": "*",
BuildRequires:  php-composer(phpunit/phpunit)
%global phpunit %{_bindir}/phpunit
# For autoloader
BuildRequires:  php-fedora-autoloader-devel
%endif

Requires:       php(language)
# From phpcompatinfo report for 1.0.3
# only Core
# For generated autoloader
Requires:       php-composer(fedora/autoloader)

# Composer
Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}


%description
This simple class provides an implementation of C++'s SCOPE_EXIT, or GoLang's
defer.

To use, assign an instance of this object to a local variable. When that
variable falls out of scope (or is explicitly unset), the callback passed
to the constructor will be invoked. This is useful, for example, to aid
cleanup at the end of a function.

Autoloader: %{_datadir}/php/%{ns_vendor}/%{pk_project}-autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}


%build
%{_bindir}/phpab -t fedora -o src/%{pk_project}-autoload.php src


%install
: Library
mkdir -p      %{buildroot}%{_datadir}/php
cp -pr src    %{buildroot}%{_datadir}/php/%{ns_vendor}


%check
%if %{with_tests}
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require '%{buildroot}%{_datadir}/php/%{ns_vendor}/%{pk_project}-autoload.php';
EOF

ret=0
for cmd in php php56 php70 php71 php72 php73 php74; do
   if which $cmd; then
      $cmd %{phpunit} --no-coverage --verbose . || ret=1
   fi
done
exit $ret
%else
: Test suite disabled
%endif


%files
%license LICENSE
%doc composer.json
%doc README.md
%{_datadir}/php/%{ns_vendor}


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Sep 19 2019 Remi Collet <remi@remirepo.net> - 1.0.0-2
- add commit to include LICENSE file (no change)

* Thu Sep 12 2019 Remi Collet <remi@remirepo.net> - 1.0.0-1
- initial package
- open https://github.com/phplang/scope-exit/issues/2 missing LICENSE
- open https://github.com/phplang/scope-exit/pull/3 add LICENSE

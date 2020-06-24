#
# Fedora spec file for php-patchwork-jsqueeze
#
# Copyright (c) 2016 Adam Williamson <awilliam@redhat.com>
#                    Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     tchwork
%global github_name      jsqueeze
%global github_version   2.0.5
%global github_commit    693d64850eab2ce6a7c8f7cf547e1ab46e69d542

%global composer_vendor  patchwork
%global composer_project jsqueeze

# "php": ">=5.3.0"
%global php_min_ver 5.3.0

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:           php-%{composer_vendor}-%{composer_project}
Version:        %{github_version}
Release:        8%{?dist}
Summary:        Efficient JavaScript minification

License:        ASL 2.0 or GPLv2
URL:            https://github.com/%{github_owner}/%{github_name}

# GitHub export does not include tests.
# Run php-patchwork-jsqueeze-get-source.sh to create full source.
Source0:       %{name}-%{github_version}-%{github_commit}.tar.gz
Source1:       %{name}-get-source.sh

BuildArch:      noarch
# Autoloader
BuildRequires: %{_bindir}/phpab
# Tests
%if %{with_tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: php-composer(phpunit/phpunit)
## phpcompatinfo (computed from version 2.0.5)
BuildRequires: php-pcre
%endif

Requires:       php(language) >= %{php_min_ver}
# phpcompatinfo (computed from version 2.0.5)
Requires:       php-pcre

Provides:       php-composer(%{composer_vendor}/%{composer_project}) = %{version}


%description
JSqueeze shrinks / compresses / minifies / mangles Javascript code.

It's a single PHP class that is developed, maintained and thoroughly
tested since 2003 on major JavaScript frameworks (e.g. jQuery).

JSqueeze operates on any parse error free JavaScript code, even when
semi-colons are missing.

In term of compression ratio, it compares to YUI Compressor and
UglifyJS.

Autoloader: %{phpdir}/Patchwork/autoload-jsqueeze.php


%prep
%setup -qn %{github_name}-%{github_commit}


%build
: Generate autoloader
%{_bindir}/phpab --output src/autoload-jsqueeze.php src/
cat src/autoload-jsqueeze.php


%install
mkdir -p %{buildroot}%{phpdir}/Patchwork
cp -pr src/* %{buildroot}%{phpdir}/Patchwork/


%check
%if %{with_tests}
%{_bindir}/phpunit --verbose \
    --bootstrap %{buildroot}%{phpdir}/Patchwork/autoload-jsqueeze.php
%else
: Tests skipped
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE.*
%doc *.md
%doc composer.json
%dir %{phpdir}/Patchwork
     %{phpdir}/Patchwork/autoload-jsqueeze.php
     %{phpdir}/Patchwork/JSqueeze.php


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Oct 10 2016 Shawn Iwinski <shawn@iwin.ski> - 2.0.5-1
- Update to 2.0.5 (RHBZ #1383300, #1383302)
- Add spec license

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Apr 25 2015 Adam Williamson <awilliam@redhat.com> - 2.0.2-1
- new release 2.0.2

* Mon Mar 16 2015 Adam Williamson <awilliam@redhat.com> - 2.0.1-2
- backport a couple of bugfixes from upstream

* Thu Jan 01 2015 Adam Williamson <awilliam@redhat.com> - 2.0.1-1
- new release, adjust for upstream PSR-4 layout change, add licenses

* Mon Dec 29 2014 Adam Williamson <awilliam@redhat.com> - 1.0.5-1
- initial package

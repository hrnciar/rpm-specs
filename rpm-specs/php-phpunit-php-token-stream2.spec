# remirepo/fedora spec file for php-phpunit-php-token-stream2
#
# Copyright (c) 2010-2015 Christof Damian, Remi Collet
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please, preserve the changelog entries
#
%global bootstrap    0
%global gh_commit    791198a2c6254db10131eecfe8c06670700904db
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sebastianbergmann
%global gh_project   php-token-stream
%global pk_vendor    phpunit
%global pk_project   %{gh_project}
%global major        2
%global php_home     %{_datadir}/php
# Fake NS for directory layout
%global ns_vendor    SebastianBergmann
%global ns_project   PhpTokenStream
%if %{bootstrap}
%global with_tests   0%{?_with_tests:1}
%else
%global with_tests   0%{!?_without_tests:1}
%endif

Name:           php-%{pk_vendor}-%{pk_project}%{major}
Version:        2.0.2
Release:        6%{?dist}
Summary:        Wrapper around PHP tokenizer extension

License:        BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{name}-%{version}-%{gh_short}.tar.gz

BuildArch:      noarch
BuildRequires:  php-fedora-autoloader-devel
%if %{with_tests}
BuildRequires:  php(language) >= 7.0
BuildRequires:  php-tokenizer
# from composer.json, "require-dev": {
#        "phpunit/phpunit": "^6.2.4"
BuildRequires:  phpunit6 >= 6.2.4
BuildRequires:  php-pcre
BuildRequires:  php-spl
%endif

# from composer.json
#        "php": "^7.0",
#        "ext-tokenizer": "*"
Requires:       php(language) >= 7.0
Requires:       php-tokenizer
# from phpcompatinfo report for version 2.0.1
Requires:       php-pcre
Requires:       php-spl
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}


%description
Wrapper around PHP tokenizer extension.

Autoloader: %{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}


%build
# Generate the Autoloader
%{_bindir}/phpab --template fedora --output src/autoload.php src


%install
mkdir -p   %{buildroot}%{php_home}/%{ns_vendor}
cp -pr src %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}


%check
%if %{with_tests}
mkdir vendor
touch vendor/autoload.php

: Run upstream test suite
ret=0
for cmd in php php70 php71 php72; do
  if which $cmd; then
    $cmd -d auto_prepend_file=%{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php \
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
%doc composer.json
%doc *.md
%dir %{php_home}/%{ns_vendor}
     %{php_home}/%{ns_vendor}/%{ns_project}%{major}


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Nov 28 2017 Remi Collet <remi@remirepo.net> - 2.0.2-1
- Update to 2.0.2

* Mon Nov  6 2017 Remi Collet <remi@remirepo.net> - 2.0.1-1
- rename to php-phpunit-php-token-stream2

* Mon Aug 21 2017 Remi Collet <remi@remirepo.net> - 2.0.1-1
- Update to 2.0.1

* Fri Aug  4 2017 Remi Collet <remi@remirepo.net> - 2.0.0-1
- Update to 2.0.0
- raise dependency on PHP 7.0
- switch to phpunit6

* Mon Feb 27 2017 Remi Collet <remi@fedoraproject.org> - 1.4.11-1
- Update to 1.4.11

* Thu Feb 23 2017 Remi Collet <remi@fedoraproject.org> - 1.4.10-1
- Update to 1.4.10

* Wed Nov 16 2016 Remi Collet <remi@fedoraproject.org> - 1.4.9-1
- Update to 1.4.9
- switch to fedora/autoloader

* Tue Sep 15 2015 Remi Collet <remi@fedoraproject.org> - 1.4.8-1
- Update to 1.4.8

* Tue Sep 15 2015 Remi Collet <remi@fedoraproject.org> - 1.4.7-1
- Update to 1.4.7 (broken)

* Fri Aug 21 2015 Remi Collet <remi@fedoraproject.org> - 1.4.6-1
- Update to 1.4.6

* Thu Aug 13 2015 Remi Collet <remi@fedoraproject.org> - 1.4.5-1
- Update to 1.4.5

* Thu Aug 13 2015 Remi Collet <remi@fedoraproject.org> - 1.4.4-1
- Update to 1.4.4

* Thu Jul  2 2015 Remi Collet <remi@fedoraproject.org> - 1.4.3-2
- fix autoloader

* Fri Jun 19 2015 Remi Collet <remi@fedoraproject.org> - 1.4.3-1
- Update to 1.4.3

* Fri Jun 12 2015 Remi Collet <remi@fedoraproject.org> - 1.4.2-1
- Update to 1.4.2

* Wed Apr  8 2015 Remi Collet <remi@fedoraproject.org> - 1.4.1-1
- Update to 1.4.1

* Sun Jan 18 2015 Remi Collet <remi@fedoraproject.org> - 1.4.0-1
- Update to 1.3.0

* Sun Aug 31 2014 Remi Collet <remi@fedoraproject.org> - 1.3.0-1
- Update to 1.3.0
- enable tests during build

* Wed Jun 25 2014 Remi Collet <remi@fedoraproject.org> - 1.2.2-5
- composer dependencies

* Wed Apr 30 2014 Remi Collet <remi@fedoraproject.org> - 1.2.2-3
- cleanup pear registry

* Tue Apr 29 2014 Remi Collet <remi@fedoraproject.org> - 1.2.2-2
- sources from github

* Mon Mar 03 2014 Remi Collet <remi@fedoraproject.org> - 1.2.2-1
- Update to 1.2.2

* Fri Sep 13 2013 Remi Collet <remi@fedoraproject.org> - 1.2.1-1
- Update to 1.2.1

* Mon Aug 05 2013 Remi Collet <remi@fedoraproject.org> - 1.2.0-1
- Update to 1.2.0

* Mon Jul 29 2013 Remi Collet <remi@fedoraproject.org> - 1.1.7-1
- Update to 1.1.7

* Sat Oct  6 2012 Remi Collet <RPMS@FamilleCollet.com> - 1.1.5-1
- upstream 1.1.5

* Mon Sep 24 2012 Remi Collet <RPMS@FamilleCollet.com> - 1.1.4-1
- upstream 1.1.4

* Thu Feb 23 2012 Remi Collet <RPMS@FamilleCollet.com> - 1.1.3-1
- upstream 1.1.3

* Mon Jan 16 2012 Remi Collet <RPMS@FamilleCollet.com> - 1.1.2-1
- upstream 1.1.2

* Fri Nov 11 2011 Remi Collet <remi@fedoraproject.org> - 1.1.1-1
- upstream 1.1.1, rebuild for remi repository

* Thu Nov 10 2011 Christof Damian <christof@damian.net> - 1.1.1-1
- upstream 1.1.1

* Tue Nov 01 2011 Remi Collet <remi@fedoraproject.org> - 1.1.0-1
- upstream 1.1.0
- no more phptok script in bindir

* Sun Dec  5 2010 Remi Collet <RPMS@FamilleCollet.com> - 1.0.1-1
- rebuild for remi repository

* Sat Dec  4 2010 Christof Damian <christof@damian.net> - 1.0.1-1
- upstream 1.0.1

* Sun Sep 26 2010 Christof Damian <christof@damian.net> - 1.0.0-1
- upstream 1.0.0 final 

* Sat Jul 31 2010 Christof Damian <christof@damian.net> - 1.0.0-1.RC1
- upstream 1.0.0RC1

* Mon Jun 21 2010 Christof Damian <christof@damian.net> - 1.0.0-1.beta1
- upstream 1.0.0beta1
- included phptok script
- macros for version workaround

* Tue Feb 23 2010 Remi Collet <RPMS@FamilleCollet.com> - 0.9.1-2
- rebuild for remi repository

* Tue Feb 23 2010 Christof Damian <christof@damian.net> - 0.9.1-2
- fix spelling

* Thu Feb 4 2010 Christof Damian <christof@damian.net> 0.9.1-1
- initial packaging

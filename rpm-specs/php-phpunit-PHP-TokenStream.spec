# remirepo/fedora spec file for php-phpunit-PHP-TokenStream
#
# Copyright (c) 2010-2015 Christof Damian, Remi Collet
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please, preserve the changelog entries
#
%global bootstrap    0
%global gh_commit    1ce90ba27c42e4e44e6d8458241466380b51fa16
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sebastianbergmann
%global gh_project   php-token-stream
%global php_home     %{_datadir}/php
%global pear_name    PHP_TokenStream
%global pear_channel pear.phpunit.de
%if %{bootstrap}
%global with_tests   0%{?_with_tests:1}
%else
%global with_tests   0%{!?_without_tests:1}
%endif

Name:           php-phpunit-PHP-TokenStream
Epoch:          1
Version:        1.4.12
Release:        6%{?dist}
Summary:        Wrapper around PHP tokenizer extension

License:        BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{name}-%{version}-%{gh_short}.tar.gz

BuildArch:      noarch
BuildRequires:  php(language) >= 5.3.3
BuildRequires:  php-fedora-autoloader-devel
%if %{with_tests}
BuildRequires:  php-pear-PHPUnit >= 3.7.0
%endif

# From composer.json
#        "php": ">=5.3.3",
#        "ext-tokenizer": "*"
Requires:       php(language) >= 5.3.3
Requires:       php-tokenizer
# From phpcompatinfo report for version 1.4.11
Requires:       php-pcre
Requires:       php-spl
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(phpunit/%{gh_project}) = %{version}

# For compatibility with PEAR mode
Provides:       php-pear(%{pear_channel}/%{pear_name}) = %{version}


%description
Wrapper around PHP tokenizer extension.


%prep
%setup -q -n %{gh_project}-%{gh_commit}


%build
phpab \
  --template fedora \
  --output   src/Token/Stream/Autoload.php \
  src


%install
mkdir -p   %{buildroot}%{php_home}
cp -pr src %{buildroot}%{php_home}/PHP


%if %{with_tests}
%check
mkdir vendor
touch vendor/autoload.php

: Run upstream test suite
cd build
ret=0
for cmd in php php70 php71 php72; do
  if which $cmd; then
    $cmd -d auto_prepend_file=%{buildroot}%{php_home}/PHP/Token/Stream/Autoload.php \
      %{_bindir}/phpunit  --verbose || ret=1
  fi
done
exit $ret
%endif


%post
if [ -x %{_bindir}/pear ]; then
   %{_bindir}/pear uninstall --nodeps --ignore-errors --register-only \
      %{pear_channel}/%{pear_name} >/dev/null || :
fi


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc *.md
%doc composer.json
%{php_home}/PHP


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.4.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.4.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.4.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.4.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.4.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Dec  5 2017 Remi Collet <remi@remirepo.net> - 1.4.12-1
- Update to 1.4.12

* Mon Aug 21 2017 Remi Collet <remi@remirepo.net> - 2.0.1-1
- Update to 2.0.1

* Fri Aug  4 2017 Remi Collet <remi@remirepo.net> - 2.0.0-1
- Update to 2.0.0
- raise dependency on PHP 7.0
- switch to phpunit6

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb 27 2017 Remi Collet <remi@fedoraproject.org> - 1.4.11-1
- Update to 1.4.11

* Thu Feb 23 2017 Remi Collet <remi@fedoraproject.org> - 1.4.10-1
- Update to 1.4.10

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Nov 16 2016 Remi Collet <remi@fedoraproject.org> - 1.4.9-1
- Update to 1.4.9
- switch to fedora/autoloader

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Sep 15 2015 Remi Collet <remi@fedoraproject.org> - 1.4.8-1
- Update to 1.4.8

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

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 12 2015 Remi Collet <remi@fedoraproject.org> - 1.4.2-1
- Update to 1.4.2

* Wed Apr  8 2015 Remi Collet <remi@fedoraproject.org> - 1.4.1-1
- Update to 1.4.1

* Sun Jan 18 2015 Remi Collet <remi@fedoraproject.org> - 1.4.0-1
- Update to 1.4.0

* Sun Aug 31 2014 Remi Collet <remi@fedoraproject.org> - 1.3.0-1
- Update to 1.3.0
- enable tests during build
- fix license handling

* Wed Jun 25 2014 Remi Collet <remi@fedoraproject.org> - 1.2.2-5
- composer dependencies

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Apr 30 2014 Remi Collet <remi@fedoraproject.org> - 1.2.2-3
- cleanup pear registry

* Tue Apr 29 2014 Remi Collet <remi@fedoraproject.org> - 1.2.2-2
- sources from github

* Mon Mar 03 2014 Remi Collet <remi@fedoraproject.org> - 1.2.2-1
- Update to 1.2.2

* Sun Nov  3 2013 Christof Damian <christof@damian.net> - 1.2.1-1
- upstream 1.2.1

* Sun Aug  4 2013 Christof Damian <christof@damian.net> - 1.2.0-1
- upstream 1.2.0

* Tue Jul 30 2013 Christof Damian <christof@damian.net> - 1.1.7-1
- upstream 1.1.7

* Fri Feb 22 2013 Remi Collet <remi@fedoraproject.org> - 1.1.5-3
- fix metadata location, FTBFS #914372

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Oct 12 2012 Christof Damian <christof@damian.net> - 1.1.5-1
- upstream 1.1.5

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Mar  2 2012 Christof Damian <christof@damian.net> - 1.1.3-1
- upstream 1.1.3

* Tue Jan 17 2012 Remi Collet <remi@fedoraproject.org> - 1.1.2-1
- Update to 1.1.2 (stable) - API 1.1.0 (stable)
- unmacro current command

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Nov 10 2011 Christof Damian <christof@damian.net> - 1.1.1-1
- upstream 1.1.1

* Tue Nov  1 2011 Christof Damian <christof@damian.net> - 1.1.0-2
- removed phptok command
- added doc dir

* Tue Nov  1 2011 Christof Damian <christof@damian.net> - 1.1.0-1
- upstream 1.1.0

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

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

* Tue Feb 23 2010 Christof Damian <christof@damian.net> - 0.9.1-2
- fix spelling

* Thu Feb 4 2010 Christof Damian <christof@damian.net> 0.9.1-1
- initial packaging


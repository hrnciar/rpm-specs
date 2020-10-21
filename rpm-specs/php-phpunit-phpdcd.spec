%global gh_commit    10246f167713d0bd0b74540ca81e4caf30b72157
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sebastianbergmann
%global gh_project   phpdcd
%global php_home     %{_datadir}/php/SebastianBergmann
%global pear_name    phpdcd
%global pear_channel pear.phpunit.de
%global with_tests   %{?_without_tests:0}%{!?_without_tests:1}

Name:           php-phpunit-phpdcd
Version:        1.0.2
Release:        12%{?dist}
Summary:        Dead Code Detector (DCD) for PHP code

License:        BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{gh_project}-%{version}.tar.gz

# Autoload template
Source1:        Autoload.php.in

# Fix for RPM, use autoload
Patch0:         %{gh_project}-rpm.patch

BuildArch:      noarch
BuildRequires:  php(language) >= 5.3.3
BuildRequires:  %{_bindir}/phpab
%if %{with_tests}
BuildRequires:  %{_bindir}/phpunit
BuildRequires:  php-phpunit-FinderFacade >= 1.1.0
BuildRequires:  php-phpunit-Version >= 1.0.3
BuildRequires:  php-symfony-console >= 2.2.0
BuildRequires:  php-phpunit-PHP-Timer >= 1.0.4
BuildRequires:  php-phpunit-PHP-TokenStream >= 1.1.3
%endif

# From composer.json
Requires:       php(language) >= 5.3.3
Requires:       php-phpunit-FinderFacade >= 1.1.0
Requires:       php-phpunit-Version >= 1.0.3
Requires:       php-symfony-console >= 2.2.0
Requires:       php-phpunit-PHP-Timer >= 1.0.4
Requires:       php-phpunit-PHP-TokenStream >= 1.1.3
# From phpcompatinfo report for version 1.0.2
Requires:       php-pcre
Requires:       php-spl

Provides:       php-pear(%{pear_channel}/%{pear_name}) = %{version}


%description
phpdcd is a Dead Code Detector (DCD) for PHP code. It scans a PHP project
for all declared functions and methods and reports those as being "dead 
code" that are not called at least once.


%prep
%setup -q -n %{gh_project}-%{gh_commit}

%patch0 -p1 -b .rpm


%build
phpab \
  --output   src/Autoload.php \
  --template %{SOURCE1} \
  src


%install
mkdir -p   %{buildroot}%{php_home}
cp -pr src %{buildroot}%{php_home}/PHPDCD

install -D -p -m 755 phpdcd %{buildroot}%{_bindir}/phpdcd


%if %{with_tests}
%check
phpunit \
   --bootstrap src/Autoload.php \
   -d date.timezone=UTC \
   tests
%endif


%post
if [ -x %{_bindir}/pear ]; then
   %{_bindir}/pear uninstall --nodeps --ignore-errors --register-only \
      %{pear_channel}/%{pear_name} >/dev/null || :
fi


%files
%doc LICENSE README.md composer.json
%{php_home}/PHPDCD
%{_bindir}/phpdcd


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

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

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun May  4 2014 Remi Collet <remi@fedoraproject.org> - 1.0.2-1
- update to 1.0.2
- sources from github
- run test suite during build
- drop dependencies on php-phpunit-File_Iterator, php-ezc-ConsoleTools
- add dependencies on php-phpunit-FinderFacade, php-phpunit-Version
  php-symfony-console

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Feb 23 2013 Christof Damian <christof@damian.net> - 0.9.3-4
- use pear_metadir FTBFS 914375

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Mar 24 2012 Christof Damian <christof@damian.net> - 0.9.3-1
- upstream 0.9.3

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Feb 4 2010 Christof Damian <christof@damian.net> 0.9.2-1
- initial packaging

